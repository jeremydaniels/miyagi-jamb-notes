# Computer Studies: cost estimate (for approval; nothing below has been run)

All figures are Gemini list prices from `tools/gemini_pricing.json` with the assumed 50% Batch discount already applied (the discount rate is unverified). Claude usage and web searches are not included. The $100 per-subject safety limit is far away in every case.

## Notes (43 files)

| | Words written | Writing | Verification | Setup (real, spent) | Total |
|---|---|---|---|---|---|
| Low | about 111,000 | $2.49 | $1.11 | $0.36 | **$3.96** |
| **Central** | **about 131,000** | **$3.93** | **$2.62** | **$0.36** | **$6.91** |
| High | about 161,000 | $9.67 | $4.35 | $0.36 | **$14.38** |

How it was made:
- `PLAN.md` targets add up to 201,500 words. Gemini's targets run high: in the five subjects written most recently the notes came out at 0.57 to 0.70 of target (Accounting 0.60, Commerce 0.70, Geography 0.68, Agricultural Science 0.64, History 0.57). Central uses 0.65, low 0.55, high 0.80.
- Rates per 1,000 words from those five runs (real logged costs): writing $0.022 to $0.065 (central $0.030; Accounting and Agricultural Science were the dear ones because of the code tool and retries); verification $0.010 to $0.027 (central $0.020). The high case uses the top of both ranges and also covers retries and re-verifying fixed files.
- Computer Studies uses Gemini code execution as "optional" (many files have nothing to calculate), so the writing rate sits between the plain subjects (about $0.022 to $0.027) and the calculation-heavy Accounting ($0.059).
- Setup is the real logged cost: transcription $0.252 and planning $0.110.

## Images (current pipeline: Batch, Flash for generation, Gemini Pro for the final drawing check)

| | Placeholders | AI pictures | Code drawings | Cost |
|---|---|---|---|---|
| Low | about 50 | 25 | 25 | **$1.75** |
| **Central** | **about 80** | **40** | **40** | **$3.93** |
| High | about 120 | 60 | 60 | **$8.46** |

How it was made:
- Past subjects had 0.4 to 0.7 image placeholders per 1,000 words of notes (Accounting 0.49, Commerce 0.37, Government 0.52, Geography 0.68, Physics 0.69). Central uses 0.60 per 1,000 words on about 131,000 words.
- Split assumed 50/50. Computer Studies suits code drawing (flowcharts, logic gate symbols, truth-table figures, network topologies, the SDLC diagram, number-conversion layouts); the AI pictures are devices, cables and connectors, printers, robots and screen scenes.
- Per picture, all-in: AI about $0.07 (Flash Batch generation about $0.034 per try with retries, Flash placement and unlabelled/labelled checks, the final Pro drawing check at about $0.01, and an allowance of about 10% of pictures needing a Pro regeneration, as in the redo pass); code drawing about $0.03. Low and high use $0.05/$0.02 and $0.10/$0.04.
- For scale, past subjects: Accounting 36 images $0.97; Geography 67 images $4.49; Physics 154 images $8.18.
- Portraits of real people (Babbage, Pascal, Hollerith and so on) are skipped by rule and keep their placeholder text.

## Combined, central case

Notes $6.91 + images $3.93 = **about $10.84** (range about $5.7 to $22.8).
