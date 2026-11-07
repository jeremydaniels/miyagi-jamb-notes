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


def _price(model):
    p = load_pricing()["models"].get(model)
    if p is None:
        p = max(load_pricing()["models"].values(), key=lambda m: m["output"])
    return p


def cost_of(model, usage, batch=False, discounted=False):
    """USD cost from a usageMetadata dict. Default: LIST price (no cache discount, upper bound).
    discounted=True applies the cached-token rate (pricing 'cached_input_fraction', unverified);
    batch=True applies the Batch API factor (pricing 'batch_factor', unverified)."""
    pr = load_pricing()
    p = _price(model)
    tin = usage.get("promptTokenCount", 0) + usage.get("toolUsePromptTokenCount", 0)
    tout = usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)
    long = tin > p.get("long_threshold", 10**12)
    rin = p["input_long"] if long else p["input"]
    rout = p["output_long"] if long else p["output"]
    cached = min(usage.get("cachedContentTokenCount", 0), tin) if discounted else 0
    frac = pr.get("cached_input_fraction", 0.25)
    cost = ((tin - cached) * rin + cached * rin * frac + tout * rout) / 1e6
    return cost * (pr.get("batch_factor", 0.5) if batch else 1.0)


def safety_limit():
    return float(load_pricing().get("safety_limit_usd", 100))


def pdf_part(path):
    data = base64.b64encode(Path(path).read_bytes()).decode()
    return {"inline_data": {"mime_type": "application/pdf", "data": data}}


def build_body(parts, *, system=None, code_execution=False, json_schema=None,
               max_output_tokens=65536, temperature=None, thinking=None):
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
    if thinking:
        body["generationConfig"]["thinkingConfig"] = {"thinkingLevel": thinking}
    return body


def _http(method, url, body=None, timeout=1200, attempts=5):
    data = json.dumps(body).encode() if body is not None else None
    last = ""
    for i in range(attempts):
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Content-Type": "application/json", "x-goog-api-key": _key()})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = scrub(e.read().decode(errors="replace"))[:600]
            last = f"HTTP {e.code}: {msg}"
            if e.code not in (408, 429, 500, 502, 503, 504):
                raise RuntimeError(last)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = scrub(f"{type(e).__name__}: {e}")
        time.sleep(min(10 * 3 ** i, 120))
    raise RuntimeError(f"Gemini call failed after {attempts} attempts: {last}")


def parse_response(resp, model, *, subject="", file="", task="", batch=False):
    """Turn a GenerateContentResponse dict into our result dict and log its cost."""
    usage = resp.get("usageMetadata", {})
    cands = resp.get("candidates") or []
    if not cands:
        raise RuntimeError("No candidates returned: " + scrub(json.dumps(resp.get("promptFeedback", resp)))[:400])
    cand = cands[0]
    parts_out = cand.get("content", {}).get("parts", [])
    text = "".join(p.get("text", "") for p in parts_out if not p.get("thought"))
    code_runs = sum(1 for p in parts_out if "executableCode" in p)
    code_errors = sum(1 for p in parts_out if p.get("codeExecutionResult", {}).get("outcome", "OUTCOME_OK") != "OUTCOME_OK")
    cost = cost_of(model, usage, batch=batch)
    est = cost_of(model, usage, batch=batch, discounted=True)
    log_cost(subject=subject, file=file, task=task, model=model, usage=usage, cost=cost,
             finish=cand.get("finishReason", ""), code_runs=code_runs, est=est, batch=batch)
    return {"text": text, "usage": usage, "cost": cost, "est": est, "model": model,
            "finish": cand.get("finishReason", ""), "code_runs": code_runs, "code_errors": code_errors}


def call_gemini(parts, *, system=None, model=None, code_execution=False,
                json_schema=None, max_output_tokens=65536, temperature=None, thinking=None,
                subject="", file="", task="", timeout=1200, attempts=5):
    """One generateContent call. Returns dict(text, usage, cost, est, finish, ...).
    Logs tokens and cost to the cost log. Retries transient errors."""
    model = model or default_model()
    body = build_body(parts, system=system, code_execution=code_execution, json_schema=json_schema,
                      max_output_tokens=max_output_tokens, temperature=temperature, thinking=thinking)
    resp = _http("POST", f"{API}/models/{model}:generateContent", body, timeout, attempts)
    return parse_response(resp, model, subject=subject, file=file, task=task)


# ---- Batch API (about half price; results arrive within hours) ----

def submit_batch(requests, model, display_name):
    """requests: {key: request body from build_body}. Returns the batch name (batches/...)."""
    body = {"batch": {"display_name": display_name[:100],
                      "input_config": {"requests": {"requests": [
                          {"request": b, "metadata": {"key": k}} for k, b in requests.items()]}}}}
    resp = _http("POST", f"{API}/models/{model}:batchGenerateContent", body, timeout=600)
    return resp["name"], resp


def get_batch(name):
    return _http("GET", f"{API}/{name}", timeout=120)


def batch_state(resp):
    return (resp.get("metadata", {}) or {}).get("state") or resp.get("state", "")


def batch_results(resp):
    """-> {key: (response_dict | None, error_dict | None)} from a finished batch."""
    cands = [resp.get("response"), (resp.get("metadata") or {}).get("output"), resp]
    items = None
    for c in cands:
        if not isinstance(c, dict):
            continue
        inl = c.get("inlinedResponses")
        if inl is not None:
            items = inl.get("inlinedResponses", []) if isinstance(inl, dict) else inl
            break
    out = {}
    for it in items or []:
        key = (it.get("metadata") or {}).get("key")
        out[key] = (it.get("response"), it.get("error"))
    return out


def check_safety(subject, extra=0.0):
    """Stop (SystemExit) if this subject's list-price spend plus `extra` would pass the safety limit."""
    lim, spent = safety_limit(), subject_spend(subject)
    if spent + extra > lim:
        sys.exit(f"SAFETY LIMIT: {subject} has used ${spent:.2f} (list price) and the next step could add about "
                 f"${extra:.2f}, passing the ${lim:.0f} per-subject limit. Stopping. Tell the user before raising "
                 f"safety_limit_usd in tools/gemini_pricing.json.")


def run_batch_rounds(subject, label, keys, make_body, handle, rounds, model, poll=60, log=print):
    """Run keys through the Batch API in rounds (round 0 = first attempt, later rounds = retries).
    make_body(key, attempt, prev) -> request body; handle(key, result, error, attempt) -> (status, prev)
    where status is 'done', 'retry' or 'fail'. State is saved so an interrupted run resumes its batch.
    Returns {key: status}."""
    sdir = WORK / "batches"
    sdir.mkdir(parents=True, exist_ok=True)
    sfile = sdir / f"{subject}-{label}.json"
    state = json.loads(sfile.read_text()) if sfile.exists() else {}
    active = [k for k in keys if k in state.get("active", keys)] if state else list(keys)
    attempt = state.get("attempt", 0)
    prev = state.get("prev", {})
    final = {}
    while active and attempt <= rounds:
        name = state.get("name") if state.get("attempt") == attempt else None
        if not name:
            check_safety(subject)
            bodies = {k: make_body(k, attempt, prev.get(k)) for k in active}
            name, _ = submit_batch(bodies, model, f"{subject}-{label}-r{attempt}")
            state = {"attempt": attempt, "name": name, "active": active, "prev": prev}
            sfile.write_text(json.dumps(state))
            log(f"[batch] {label} round {attempt}: submitted {len(active)} request(s) as {name}")
        while True:
            resp = get_batch(name)
            st = batch_state(resp)
            if resp.get("done") or st in ("BATCH_STATE_SUCCEEDED", "BATCH_STATE_FAILED",
                                          "BATCH_STATE_CANCELLED", "BATCH_STATE_EXPIRED"):
                break
            time.sleep(poll)
        if st != "BATCH_STATE_SUCCEEDED":
            log(f"[batch] {name} ended as {st}")
        results = batch_results(resp)
        nxt = []
        for k in active:
            r, e = results.get(k, (None, {"message": "missing from batch output"}))
            result = None
            if r is not None:
                try:
                    result = parse_response(r, model, subject=subject, file=k,
                                            task=f"{label}" if attempt == 0 else f"{label}-retry{attempt}", batch=True)
                except Exception as ex:
                    e = {"message": scrub(str(ex))}
            status, p = handle(k, result, e, attempt)
            if status == "retry" and attempt < rounds:
                nxt.append(k)
                prev[k] = p
            else:
                final[k] = "done" if status == "done" else "fail"
        active = nxt
        attempt += 1
        state = {"attempt": attempt, "name": None, "active": active, "prev": prev}
        sfile.write_text(json.dumps(state))
    if sfile.exists():
        sfile.unlink()
    return final


def cost_report(subject):
    """Print writing / verification / setup totals for a subject, at list price and estimated real price."""
    rows = read_costs(subject)
    def tot(f, field):
        return sum(r.get(field, r["cost_usd"]) for r in rows if f(r["task"]))
    groups = [("setup (transcribe + plan)", lambda t: t in ("transcribe", "plan")),
              ("writing", lambda t: t.startswith("notes") or t.startswith("coverage")),
              ("verification", lambda t: t.startswith("verify"))]
    print(f"COST {subject}")
    for name, f in groups:
        print(f"  {name:<28} list ${tot(f, 'cost_usd'):>7.2f}   est ${tot(f, 'cost_est_usd'):>7.2f}")
    print(f"  {'TOTAL':<28} list ${sum(r['cost_usd'] for r in rows):>7.2f}   est ${sum(r.get('cost_est_usd', r['cost_usd']) for r in rows):>7.2f}")
    print("  (list = no cache discount, normal price; est = cached-token and Batch discounts applied. "
          "Discount rates are assumptions in tools/gemini_pricing.json until checked against Google's price page.)")


def log_cost(*, subject, file, task, model, usage, cost, finish="", code_runs=0, est=None, batch=False):
    WORK.mkdir(parents=True, exist_ok=True)
    rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "subject": subject, "file": file, "task": task, "model": model,
           "input_tokens": usage.get("promptTokenCount", 0),
           "tool_input_tokens": usage.get("toolUsePromptTokenCount", 0),
           "output_tokens": usage.get("candidatesTokenCount", 0),
           "thinking_tokens": usage.get("thoughtsTokenCount", 0),
           "cached_tokens": usage.get("cachedContentTokenCount", 0),
           "cost_usd": round(cost, 5), "cost_est_usd": round(cost if est is None else est, 5),
           "batch": batch, "finish": finish, "code_runs": code_runs}
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
