"""Shared helpers for the Gemini tools: REST client (standard library only),
cost calculation and the cost log.

The API key is read from GEMINI_API_KEY and sent only in a request header.
It is never printed, logged or written to disk; error text is scrubbed.
"""
import base64
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = Path(os.environ.get("GEMINI_WORK_DIR", ROOT / ".gemini-work"))
COST_LOG = WORK / "costs.jsonl"
PRICING_FILE = ROOT / "tools" / "gemini_pricing.json"
API = "https://generativelanguage.googleapis.com/v1beta"
_lock = threading.Lock()


def load_pricing():
    return json.loads(PRICING_FILE.read_text())


def default_model():
    return load_pricing()["default_model"]


def _key():
    k = os.environ.get("GEMINI_API_KEY", "")
    if not k:
        sys.exit("GEMINI_API_KEY is not set.")
    return k


def scrub(text):
    k = os.environ.get("GEMINI_API_KEY", "")
    return text.replace(k, "[KEY]") if k else text


def cost_of(model, usage):
    """Upper-bound cost in USD from a usageMetadata dict."""
    p = load_pricing()["models"].get(model)
    if p is None:
        p = max(load_pricing()["models"].values(), key=lambda m: m["output"])
    tin = usage.get("promptTokenCount", 0) + usage.get("toolUsePromptTokenCount", 0)
    tout = usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)
    long = tin > p.get("long_threshold", 10**12)
    rin = p["input_long"] if long else p["input"]
    rout = p["output_long"] if long else p["output"]
    return (tin * rin + tout * rout) / 1e6


def pdf_part(path):
    data = base64.b64encode(Path(path).read_bytes()).decode()
    return {"inline_data": {"mime_type": "application/pdf", "data": data}}


def call_gemini(parts, *, system=None, model=None, code_execution=False,
                json_schema=None, max_output_tokens=65536, temperature=None,
                subject="", file="", task="", timeout=1200, attempts=5):
    """One generateContent call. Returns dict(text, usage, cost, finish, model).
    Logs tokens and cost to the cost log. Retries transient errors."""
    model = model or default_model()
    body = {"contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"maxOutputTokens": max_output_tokens}}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    if code_execution:
        body["tools"] = [{"code_execution": {}}]
    if json_schema:
        body["generationConfig"]["responseMimeType"] = "application/json"
        body["generationConfig"]["responseSchema"] = json_schema
    if temperature is not None:
        body["generationConfig"]["temperature"] = temperature
    req_data = json.dumps(body).encode()
    url = f"{API}/models/{model}:generateContent"
    last = ""
    for i in range(attempts):
        req = urllib.request.Request(url, data=req_data, method="POST", headers={
            "Content-Type": "application/json", "x-goog-api-key": _key()})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                resp = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            msg = scrub(e.read().decode(errors="replace"))[:500]
            last = f"HTTP {e.code}: {msg}"
            if e.code not in (408, 429, 500, 502, 503, 504):
                raise RuntimeError(last)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = scrub(f"{type(e).__name__}: {e}")
        time.sleep(min(10 * 3 ** i, 120))
    else:
        raise RuntimeError(f"Gemini call failed after {attempts} attempts: {last}")

    usage = resp.get("usageMetadata", {})
    cands = resp.get("candidates") or []
    if not cands:
        raise RuntimeError("No candidates returned: " + scrub(json.dumps(resp.get("promptFeedback", resp)))[:400])
    cand = cands[0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", [])
                   if not p.get("thought"))
    cost = cost_of(model, usage)
    parts_out = cand.get("content", {}).get("parts", [])
    code_runs = sum(1 for p in parts_out if "executableCode" in p)
    code_errors = sum(1 for p in parts_out if p.get("codeExecutionResult", {}).get("outcome", "OUTCOME_OK") != "OUTCOME_OK")
    log_cost(subject=subject, file=file, task=task, model=model, usage=usage, cost=cost,
             finish=cand.get("finishReason", ""), code_runs=code_runs)
    return {"text": text, "usage": usage, "cost": cost, "model": model,
            "finish": cand.get("finishReason", ""), "code_runs": code_runs, "code_errors": code_errors}


def log_cost(*, subject, file, task, model, usage, cost, finish="", code_runs=0):
    WORK.mkdir(parents=True, exist_ok=True)
    rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "subject": subject, "file": file, "task": task, "model": model,
           "input_tokens": usage.get("promptTokenCount", 0),
           "tool_input_tokens": usage.get("toolUsePromptTokenCount", 0),
           "output_tokens": usage.get("candidatesTokenCount", 0),
           "thinking_tokens": usage.get("thoughtsTokenCount", 0),
           "cached_tokens": usage.get("cachedContentTokenCount", 0),
           "cost_usd": round(cost, 5), "finish": finish, "code_runs": code_runs}
    with _lock, COST_LOG.open("a") as f:
        f.write(json.dumps(rec) + "\n")


def read_costs(subject=None):
    if not COST_LOG.exists():
        return []
    rows = [json.loads(l) for l in COST_LOG.read_text().splitlines() if l.strip()]
    return [r for r in rows if subject is None or r["subject"] == subject]


def subject_spend(subject):
    return sum(r["cost_usd"] for r in read_costs(subject))


def print_costs(subject=None):
    rows = read_costs(subject)
    per = {}
    for r in rows:
        k = (r["subject"], r["file"] or r["task"])
        d = per.setdefault(k, [0, 0, 0, 0.0])
        d[0] += r["input_tokens"] + r["tool_input_tokens"]
        d[1] += r["output_tokens"] + r["thinking_tokens"]
        d[2] += 1
        d[3] += r["cost_usd"]
    print(f"{'subject':<14}{'file / task':<52}{'calls':>6}{'in tok':>10}{'out tok':>10}{'USD':>9}")
    tot = {}
    for (s, f), (i, o, n, c) in sorted(per.items()):
        print(f"{s:<14}{f:<52}{n:>6}{i:>10}{o:>10}{c:>9.3f}")
        tot[s] = tot.get(s, 0) + c
    for s, c in tot.items():
        print(f"TOTAL {s}: ${c:.2f}")
    if not load_pricing().get("verified"):
        print("(prices in tools/gemini_pricing.json are unverified list prices; costs are upper bounds)")


def strip_fence(text):
    """Remove an outer ```markdown fence if the model wrapped its answer in one."""
    t = text.strip()
    m = re.match(r"^```(?:markdown|md)?\s*\n(.*)\n```$", t, re.S)
    return (m.group(1) if m else t).strip() + "\n"


def subject_title(subject):
    return subject.replace("-", " ").title()
