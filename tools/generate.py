"""Generate unlabelled images with the Gemini API (GEMINI_API_KEY) and log the real cost.

Usage:
  python tools/generate.py PROMPTS.json [name ...]   # generate all (or only the named) images
  python tools/generate.py --total                   # print the running cost so far
  python tools/generate.py --models                  # list the image models this key can use

PROMPTS.json is a list of [name, prompt] pairs. The house style below is added
to every prompt. Images are saved to <work>/raw/<name>.png (see common.py).

The key is read from GEMINI_API_KEY by gemini_common (never printed or logged).
Prices (USD per 1M tokens) are best-known list prices and UNVERIFIED: check them
on https://ai.google.dev/gemini-api/docs/pricing. The cost logged per image is
computed from the token counts the API returns.
"""
import argparse, base64, io, json, os, sys, threading
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RAW, COST_LOG
import gemini_common as g
from PIL import Image

DEFAULT_MODEL = "gemini-3-pro-image"
# model -> (text/image input, text output, image output) USD per 1M tokens. UNVERIFIED.
PRICE = {
    "gemini-2.5-flash-image":   (0.30, 2.50, 30.0),
    "gemini-3.1-flash-image":   (0.50, 3.00, 60.0),
    "gemini-3-pro-image":       (2.00, 12.00, 120.0),
}
EST_PER_IMAGE = 0.15   # reserved per in-flight call when checking the budget (covers the dearest model)

STYLE = ("Clean, flat educational illustration like a modern {subject} textbook. Pure white background. "
         "Consistent soft colour palette (soft greens, blues, pinks, lavender, warm creams). Smooth outlines, "
         "no photorealism, no shadows or gradients beyond gentle shading. Leave clear white space around the subject "
         "so labels can be added later. ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO LABELS, NO ARROWS, NO LEADER LINES anywhere in the image. "
         "Square image.")

_lock = threading.Lock()
_reserved = 0.0


def total():
    if not os.path.exists(COST_LOG):
        return 0.0
    with open(COST_LOG) as f:
        return sum(json.loads(line)["cost"] for line in f if line.strip())


def cost_of(model, usage):
    """usage = Gemini usageMetadata. Image output tokens are billed at the image rate."""
    pin, ptext, pimg = PRICE.get(model, max(PRICE.values(), key=lambda p: p[2]))
    tin = usage.get("promptTokenCount", 0)
    out_total = usage.get("candidatesTokenCount", 0)
    img_out = 0
    for d in usage.get("candidatesTokensDetails", []) or []:
        if d.get("modality") == "IMAGE":
            img_out += d.get("tokenCount", 0)
    if not img_out:
        img_out = out_total
    text_out = max(0, out_total - img_out) + usage.get("thoughtsTokenCount", 0)
    return (tin * pin + text_out * ptext + img_out * pimg) / 1e6


def call_image(model, prompt):
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": "1:1"}}}
    resp = g._http("POST", f"{g.API}/models/{model}:generateContent", body, 600, 3)
    usage = resp.get("usageMetadata", {})
    cands = resp.get("candidates") or []
    if not cands:
        raise RuntimeError("no candidates: " + g.scrub(json.dumps(resp.get("promptFeedback", resp)))[:300])
    for p in cands[0].get("content", {}).get("parts", []):
        d = p.get("inlineData") or p.get("inline_data")
        if d and d.get("data"):
            return base64.b64decode(d["data"]), usage
    raise RuntimeError("no image in response (finish: %s)" % cands[0].get("finishReason"))


def generate(model, name, prompt, budget, subject):
    global _reserved
    with _lock:
        if total() + _reserved + EST_PER_IMAGE > budget:
            return f"{name}: SKIPPED - running total ${total():.4f} is too close to the ${budget:.2f} budget"
        _reserved += EST_PER_IMAGE
    try:
        data, usage = call_image(model, prompt + "\n\nStyle: " + STYLE.format(subject=subject))
        cost = cost_of(model, usage)
        Image.open(io.BytesIO(data)).convert("RGB").save(os.path.join(RAW, name + ".png"))
        with _lock:
            with open(COST_LOG, "a") as f:
                f.write(json.dumps({"name": name, "model": model, "usage": usage, "cost": cost}) + "\n")
            return f"{name}: ${cost:.4f} (running total ${total():.4f})"
    except Exception as e:  # report and carry on with the rest of the batch
        return f"{name}: FAILED - {type(e).__name__}: {g.scrub(str(e))[:300]}"
    finally:
        with _lock:
            _reserved -= EST_PER_IMAGE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompts", nargs="?")
    ap.add_argument("names", nargs="*")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--budget", type=float, default=5.00, help="stop before the running total passes this (USD)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--subject", default="biology", help='fills "like a modern ___ textbook" in the style text')
    ap.add_argument("--total", action="store_true", help="print the running cost and exit")
    ap.add_argument("--models", action="store_true", help="list image models available to this key and exit")
    a = ap.parse_args()
    if a.models:
        r = g._http("GET", f"{g.API}/models?pageSize=200", None, 60)
        for m in r.get("models", []):
            if "image" in m["name"] or "banana" in m["name"]:
                print(m["name"], m.get("supportedGenerationMethods"))
        return
    if a.total or not a.prompts:
        print(f"Running total: ${total():.4f}")
        return
    with open(a.prompts) as f:
        jobs = [j for j in json.load(f) if not a.names or j[0] in a.names]
    with ThreadPoolExecutor(a.workers) as ex:
        for line in ex.map(lambda j: generate(a.model, j[0], j[1], a.budget, a.subject), jobs):
            print(line, flush=True)


if __name__ == "__main__":
    sys.exit(main())
