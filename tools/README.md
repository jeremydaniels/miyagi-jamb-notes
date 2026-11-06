# Image tools

These scripts make the labelled diagrams in `biology/images/`. They work the same way for any subject.

The process: generate each picture **with no text**, look at it, add the labels yourself with Pillow, look again, and fix anything wrong. The model often puts parts in slightly odd places, so never place labels without looking at the image first.

## Setup

```bash
pip install openai pillow
export OPENAI_API_KEY=...        # never print, log or commit it
```

Working files go in `.image-work/` at the repo root, which is git-ignored. To put them somewhere else, set `IMAGE_WORK_DIR`. That folder holds:

- `raw/`: unlabelled images from the API
- `costs.jsonl`: one line per API call, with its token usage and cost in USD
- `preview/`: gridded and zoomed copies for reading coordinates

## Scripts

| Script | What it does |
|---|---|
| `generate.py` | Calls OpenAI (`gpt-image-2`, 1024x1024, quality "medium"), adds the house style to each prompt, saves `raw/<name>.png` and logs the real cost from the returned token usage. It skips a call if the running total plus that call could go over `--budget` (default $5). |
| `preview.py` | `grid` draws a pixel grid on a raw image. `zoom` enlarges a small area. `small` shrinks a finished labelled image so you can check it. |
| `label.py` | Reads a label spec and draws the labels, leader lines, captions and arrows. Saves the final PNG to `biology/images/` (change with `--out`). |
| `place_images.py` | Replaces the `[IMAGE: ...]` lines in a notes file, in order, with `![alt](images/NAME.png)`. |
| `common.py` | Shared paths and fonts. Uses Inter if it is installed, otherwise DejaVu Sans. |

## Doing a topic (example: chemistry C1)

1. **Write the prompts.** Read every `[IMAGE: ...]` placeholder in the notes and make `tools/specs/chemistry/C1-prompts.json`, a list of `[name, prompt]` pairs. Name each image after its topic file (e.g. `C1-...`). Describe what to draw, where each part goes and the colours. Don't ask for labels, because the style text already forbids any text in the image.
2. **Generate:**
   ```bash
   python tools/generate.py tools/specs/chemistry/C1-prompts.json --subject chemistry
   python tools/generate.py tools/specs/chemistry/C1-prompts.json C1-some-image   # redo just one image
   python tools/generate.py --total                                               # running cost
   ```
3. **Look at every raw image** and check it is accurate (correct number of parts, correct shapes, no stray text). Regenerate any that are wrong with a stricter prompt; for example, "EXACTLY THREE lips" fixed the Ascaris head.
4. **Find coordinates:**
   ```bash
   python tools/preview.py grid C1-some-image
   python tools/preview.py zoom C1-some-image 400 300 520 420 4
   ```
   Then check that each dot will land on the right part, not on the white background next to it.
5. **Write the label spec** `tools/specs/chemistry/C1-labels.json`. All the options are listed at the top of `label.py`. A short example:
   ```json
   {"C1-some-image": {
      "labels":   [["Nucleus", [430, 380], "L", 320], ["Cell wall", [283, 620], "R"]],
      "captions": [["Plant cell", 255, 0]],
      "arrows":   [[[100, 500], [200, 500]]]
   }}
   ```
6. **Render, then check the result:**
   ```bash
   python tools/label.py tools/specs/chemistry/C1-labels.json --out chemistry/images
   python tools/preview.py small C1-some-image   # only for images in biology/images; otherwise open the PNG directly
   ```
   Look at every labelled image. Fix any dot that misses its part, any lines that cross and any text that overlaps, then render again.
7. **Place the images in the notes:**
   ```bash
   python tools/place_images.py chemistry/C1-....md "C1-image-a=Alt text for image a" "C1-image-b=..."
   ```
8. Commit the notes, images and specs for that topic, then push.

## The biology specs

`specs/biology/` holds the prompts and label specs used for A1 to A3. They are worked examples. The label coordinates only fit the original raw images, which are not committed because they take a lot of space. If you regenerate an image you get a different picture, so its labels must be placed again.

Two raw images were also edited by hand before labelling:

- `A2c-tapeworm-life-cycle`: the model kept drawing 4 hooks on the embryo, so the hooks were painted over and redrawn as 6.
- `A2c-ascaris`: regenerated with a stricter prompt (already in `A2c-prompts.json`).

## Cost

With `gpt-image-2` at 1024x1024 and quality "medium", each image used about 1,756 output image tokens and about 250 text input tokens, which is about $0.054. The rates in `generate.py` (`PRICE`) are per 1M tokens: $5 text input and $30 image output. Check them against OpenAI's pricing page before each batch. The 69 calls for A1 to A3 cost $3.71.
