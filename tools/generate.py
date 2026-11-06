"""Generate unlabelled images with the OpenAI Images API and log the real cost.

Usage:
  python tools/generate.py PROMPTS.json [name ...]   # generate all (or only the named) images
  python tools/generate.py --total                   # print the running cost so far

PROMPTS.json is a list of [name, prompt] pairs. The house style below is added
to every prompt. Images are saved to <work>/raw/<name>.png (see common.py).

The API key is read by the OpenAI client from the OPENAI_API_KEY environment
variable. Never print, log or commit it.
"""
import argparse, base64, json, os, sys, threading
from concurrent.futures import ThreadPoolExecutor
from common import RAW, COST_LOG

MODEL, SIZE, QUALITY = "gpt-image-2", "1024x1024", "medium"
# USD per 1M tokens for gpt-image-2 (standard, non-batch). Check OpenAI's pricing
# page and update these before a new batch.
PRICE = {"text_in": 5.00, "image_in": 8.00, "image_out": 30.00, "text_out": 10.00}
EST_PER_IMAGE = 0.06   # reserved per in-flight call when checking the budget

STYLE = ("Clean, flat educational illustration like a modern {subject} textbook. Pure white background. "
         "Consistent soft colour palette (soft greens, blues, pinks, lavender, warm creams). Smooth outlines, "
         "no photorealism, no shadows or gradients beyond gentle shading. Leave clear white space around the subject "
         "so labels can be added later. ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO LABELS, NO ARROWS, NO LEADER LINES anywhere in the image.")

_lock = threading.Lock()
_reserved = 0.0


def total():
    if not os.path.exists(COST_LOG):
        return 0.0
    with open(COST_LOG) as f:
        return sum(json.loads(line)["cost"] for line in f if line.strip())


def cost_of(usage):
    u = usage or {}
    din = u.get("input_tokens_details") or {}
    dout = u.get("output_tokens_details") or {}
    text_in = din.get("text_tokens", u.get("input_tokens", 0))
    image_in = din.get("image_tokens", 0)
    text_out = dout.get("text_tokens", 0)
    image_out = dout.get("image_tokens", u.get("output_tokens", 0) - text_out)
    return (text_in * PRICE["text_in"] + image_in * PRICE["image_in"]
            + image_out * PRICE["image_out"] + text_out * PRICE["text_out"]) / 1e6


def generate(client, name, prompt, budget, subject):
    global _reserved
    with _lock:
        if total() + _reserved + EST_PER_IMAGE > budget:
            return f"{name}: SKIPPED - running total ${total():.4f} is too close to the ${budget:.2f} budget"
        _reserved += EST_PER_IMAGE
    try:
        r = client.images.generate(model=MODEL, prompt=prompt + "\n\nStyle: " + STYLE.format(subject=subject),
                                   size=SIZE, quality=QUALITY, n=1)
        usage = r.usage.model_dump() if r.usage else {}
        cost = cost_of(usage)
        with open(os.path.join(RAW, name + ".png"), "wb") as f:
            f.write(base64.b64decode(r.data[0].b64_json))
        with _lock:
            with open(COST_LOG, "a") as f:
                f.write(json.dumps({"name": name, "model": MODEL, "usage": usage, "cost": cost}) + "\n")
            return f"{name}: ${cost:.4f} (running total ${total():.4f})"
    except Exception as e:  # report and carry on with the rest of the batch
        return f"{name}: FAILED - {type(e).__name__}: {e}"
    finally:
        with _lock:
            _reserved -= EST_PER_IMAGE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompts", nargs="?")
    ap.add_argument("names", nargs="*")
    ap.add_argument("--budget", type=float, default=5.00, help="stop before the running total passes this (USD)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--subject", default="biology", help='fills "like a modern ___ textbook" in the style text')
    ap.add_argument("--total", action="store_true", help="print the running cost and exit")
    a = ap.parse_args()
    if a.total or not a.prompts:
        print(f"Running total: ${total():.4f}")
        return
    from openai import OpenAI
    client = OpenAI()
    with open(a.prompts) as f:
        jobs = [j for j in json.load(f) if not a.names or j[0] in a.names]
    with ThreadPoolExecutor(a.workers) as ex:
        for line in ex.map(lambda j: generate(client, j[0], j[1], a.budget, a.subject), jobs):
            print(line, flush=True)


if __name__ == "__main__":
    sys.exit(main())
