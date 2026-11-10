# Images report: Biology leftovers and 14 subjects (updated after the cleanup pass)

**1362 of 1399 placeholders now have an image** (97%); **37 placeholders are still in the notes** (9 skipped by rule, 28 failed the checks). Spend: **$57.60** for the main run plus **$5.80** for the cleanup pass (cap $10) = **$63.40**; the $120 cap was never near. Galleries for your phone: `subjects/<subject>/images/GALLERY-<subject>.md`.

## Cleanup pass (second task)

**1. Junk scan (labels, captions, alt text, text inside code drawings).** New `tools/textfmt.py` turns formulas, ions, units and caret/underscore notation into real subscripts and superscripts (CO₂, H₂SO₄, KClO₃, Ca(OH)₂, Fe²⁺, m², cm³, s⁻¹, x², 2³). It leaves names and variables alone (vitamin B12, F1, Q1, IC1, s1, quotations). It is used by `label.py`, by every code template and by `style.save`.
- Labelled pictures: 17 re-rendered from the saved coordinates: stray quotes and `CO_2` (Chemistry A12-03), `KClO3 + MnO2`, `O3`, `O2`, `N2`, `Rh+`, a junk `"1` label (Geography B7-01, label removed), and 11 captions (below).
- Captions: 2 captions were only junk (`"1`, `"1.`: Government A1-01, CRK B9-02), removed; 9 run-on captions without punctuation (FIFO/LIFO, livestock systems, bread making, Pasteur, suffrage timeline, colonial rule, At-tatfif, Majlis ash-Shura, Shari'ah v Western) were rewritten using only the words they already had.
- Code drawings: 4 template drawings re-rendered with subscripts (Contact process, Solvay, fractional distillation, binary place values); 4 free-form drawings redrawn and passed the check (Biology C7c-04, Chemistry A2-01 and A2-02, Mathematics D1-01). **One not fixed:** Biology C2-11 (greenhouse effect) still has plain "CO2" in the picture, because the redraw came out stretched and failed the check; the old picture was kept.
- A real defect found on the way: 14 template flowcharts had dark text on dark fills (teal, red, dark grey). Templates now choose white text on dark fills; those 14 were re-rendered.
- Alt text: 4 files fixed (AgNO₃, H₂S/SO₂/H₂O, KNO₃, x²). Numbers in step labels such as "1 peel" and "2 cm cube" are real content and were left.
- Not changed: variables such as F1, L1, m1 and D1 stay as typed in the drawings.

**2. Biology relabel scars.** I tried a Gemini vision check on every recovered picture (4 zoomed tiles each, 318 images). It flagged 284 of 318 images with 2,885 marks, mostly ordinary outlines, so it cannot be trusted and I did not use it to decide anything. I looked at crops at 4x myself instead and found the real problem: the first repair left soft, blurred bands (about 9 px) where a leader line had crossed an outline. I replaced the repair: each line is removed by interpolating across a thin band (11 px, from the line geometry replayed from the old layout) in the direction that crosses the line, dots are filled from their surroundings. All 262 images were rebuilt again from the originals in git (`tools/rebuild_all.py`). At normal viewing size I see no marks in the 12 images I looked at; **at 4x zoom a faint soft band remains where a line crossed a dark outline.** I did not flag single images because I could not measure this reliably.

**3. Label lines.** The final Gemini check of all 296 changed images reported something for 124 images, again mostly noise, but it led me to a real fault in my label layout: two lines could share a corridor or run through another label's dot (Ascaris male/female, the Benedict tubes). `label.py` now also counts "line passes within 12 px of another dot" as a conflict, swaps slots until there is none, and restacks. All 507 labelled images in all subjects were re-rendered with it and compressed.

**4. The 59 failed placeholders.** I looked at every rejected picture (39 AI generations and 37 code drawings) myself.
- **Accepted, check was too strict (15):** B1-11 rabbit digestive system (try 0 has all parts; the failed try had printed labels), B1-12 urinary system (vessels on the correct sides; kidney height is a nitpick), B2e-06 hepatobiliary ducts (stomach does join the duodenum), B3b-13 potometer (arrow and reservoir correct in try 0), B7b-16 seed dispersal (try 0 has six clean panels), C7a-02 Anopheles life cycle (larva lies flat under the surface), A5-02 prismatic compass (the "N" was on the other try), B5-04 oxbow lake (a good four-stage sequence), C6-03 rabbit handling (two hands, not three), B2-01 Elijah on Carmel (altar, fire, steaming trench; stone count cannot be verified), B8-02 Ezekiel (no hand of God, by the CRK rule; the label "Hand of God offering the word" was left out); and 4 code drawings: D1-12 ABO compatibility (correct, self-donation loops missing), A7-01 feudal pyramid, C1-01 Nigeria protectorates sketch map, B4-01 Benin timeline.
- **Retried once with Pro and a simplified description (44):** the description was rewritten by Gemini Flash (fewer labels, no legends or callouts, no state borders on maps, no counts above four), then one Pro generation or two Pro code attempts. **16 of the 44 passed** and are placed.
- **Still placeholders (28 failed + 9 skipped):** see the table below. Accepted images carry a note in this report only; nothing else marks them.
- Cost of the cleanup pass: $5.80 of the $10 cap (retries, the scar and recheck calls, simplified descriptions).

**5. Other changes.** `tools/rebuild_raw.py` now uses one temporary file per process (parallel runs could collide); `make_images.py` has `--rounds`, `--code-attempts`, `--pro` and `--simplified`; the stretched-canvas guard in `style.save` (18 in maximum) fixed a Mathematics drawing that exceeded Pillow's size limit. "My notes" had nothing to add.

## Images placed and left per subject

| Subject | Placeholders | Placed | Left | AI pictures (planned) | Code drawings (planned) | Cost (main run) |
|---|---|---|---|---|---|---|
| Biology (B to E) | 451 | 441 | 10 | 333 | 118 | $14.69 |
| Physics | 154 | 152 | 2 | 35 | 119 | $8.18 |
| Chemistry | 68 | 68 | 0 | 27 | 41 | $2.95 |
| Mathematics | 65 | 64 | 1 | 0 | 65 | $1.96 |
| Economics | 61 | 58 | 3 | 3 | 58 | $3.84 |
| Government | 62 | 61 | 1 | 11 | 50 | $2.77 |
| Use of English | 31 | 29 | 2 | 10 | 21 | $1.93 |
| Literature in English | 26 | 26 | 0 | 12 | 14 | $1.05 |
| CRK | 103 | 103 | 0 | 95 | 8 | $5.45 |
| IRK | 50 | 43 | 7 | 18 | 25 | $1.82 |
| Accounting | 36 | 35 | 1 | 2 | 34 | $0.97 |
| Commerce | 27 | 26 | 1 | 9 | 18 | $1.14 |
| Geography | 67 | 66 | 1 | 25 | 42 | $4.49 |
| Agricultural Science | 108 | 108 | 0 | 92 | 16 | $6.21 |
| History | 90 | 82 | 8 | 24 | 65 | $5.55 |
| **Total** | **1399** | **1362** | **37** | | | **$63.40** |

(The cost column is the running spend per subject including the cleanup pass work that was logged against that subject; the total includes reclassification.)

Cost per subject includes image generation, code-drawing, checks and label placement. The total also includes $0.35 for reclassifying all placeholders. Re-rendering the Biology labels cost nothing (no pictures were regenerated). Prices are the unverified list prices in `tools/gemini_pricing.json`; Batch is assumed to be half price.

## What changed in the tools (Step 1)

- **`tools/label.py`**: leader lines no longer cross (labels sit on the side of their dot, and slots are swapped until no two lines cross); region labels (`regions` list, for example cortex and medulla) end in a bigger dot inside the region; the font is at least 2.2% of the final image width (about 28 to 45 px), long labels wrap; process notes go in a caption under the picture (`caption_below`); stray quotes and `CO_2` style text are cleaned.
- **`tools/codedraw/templates.py`**: fixed layout templates for flowchart, cycle, hub (concept map), graph, chart (bar, pie, stacked), table, timeline and T-account. Gemini only writes a JSON spec; the template measures the text, sizes the boxes, keeps every font at 14 pt or more and moves labels away from curves and from each other. Figures that no template fits (geometry, circuits, rays, maps, structures) still use free-form code, but `style.save` now raises every font to 14 pt, nudges overlapping text apart, and the pipeline rejects stretched drawings. If a template cannot express a figure after three tries, the pipeline tries free-form code twice.
- **`tools/rebuild_raw.py`**: the raw Biology pictures were not stored, so the finished images were taken apart: the old layout was replayed to find the picture and every leader line, the lines were filled in from their neighbours, and the pictures were labelled again with the new `label.py` from the saved coordinates. **262 of 262 Biology B to E labelled images were re-rendered; none failed.** The 81 code-drawn Biology images were run again with the new style: 60 were redrawn and replaced, 18 were kept as they were because the redraw failed the layout check, 3 raised errors and were kept.
- **`tools/reclassify.py`**: every placeholder was sorted again (see Step 2 below); `IMAGES-CLASSIFICATION.csv` has new columns `old_group`, `template`, `parts`, `regions`, `caption`, `reclass_note`.
- **Pipeline** (`tools/make_images.py`): works for any subject, one Batch registry per subject so runs can go in parallel, Flash first and Pro for retries, per-subject style text and the CRK/IRK rules, `--retry-failed`, one label may be left out if it is the only part not visible (none needed), and a lock so parallel runs commit one at a time.

## Reclassification (Step 2)

Gemini Flash re-read all 1,046 unplaced placeholders (cost $0.35). 53 moved from code to AI (anatomy, plant sections, apparatus and realistic objects), a few moved from AI to code (for example a ledger or flowchart), maps stay code-drawn sketches, and 9 were set to skip (portraits of real people and Arabic script). Pointer labels now go only on real parts; process annotations ("oxygen in", "inspiration", test results, measurements) became one caption line under the picture. Full table: `IMAGES-CLASSIFICATION.csv`.

| Old group | New group | Placeholders |
|---|---|---|
| AI | CODE | 6 |
| CODE | AI | 51 |
| CODE | FLAG | 6 |
| CODE | SKIP | 1 |
| FLAG | AI | 2 |
| FLAG | SKIP | 8 |

## Still placeholders: reasons

| Reason | Count |
|---|---|
| code drawing failed the layout/content check | 22 |
| skipped by rule (real-person portrait or Arabic script) | 9 |
| picture failed the structure check | 4 |
| labels could not be placed on the right parts | 2 |

Skipped by rule: 7 IRK images that need Arabic script, 1 Government portrait grid and 1 History portrait of a real person. The rest failed the structure or layout checks after three tries and, for the 44 retried in the cleanup pass, after one more Pro try. Most are complex anatomy or apparatus, and maps with many places or regions.

| Subject | Notes file | Image | Why it is still a placeholder |
|---|---|---|---|
| Biology | `B2d-mammalian-teeth` | `B2d-02-types-human-teeth` | labels still wrong after 3 placements: one long root; premolar; one or two roots; molar |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-18-coleoptile-tropism-experiments` | raw check: In the bottom row, the second shoot has an intact curved tip with the block resting on the side, rather than a flat decapitated cut top with the block placed on the left half. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-12-fruit-placentation-types` | raw check: The 2-by-3 grid is missing the bottom row middle diagram showing basal placentation with a single ovule at the base. |
| Biology | `B7c-reproduction-in-mammals` | `B7c-09-contraceptive-methods-overview` | labels still wrong after 3 placements: male condom; oviduct cut and tied; box titles: natural; barrier; implant; intrauterine device; uterus; hormonal; female condom |
| Biology | `B9c-hormonal-control` | `B9c-02-negative-feedback-flow` | code image: the code failed: er     TEMPLATES[spec["template"]](spec, out)     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/tools/codedraw/templates.py", line  |
| Biology | `B9d-homeostasis` | `B9d-07-osmoregulation-adh-feedback-flowchart` | code image: Diagram is structured into two vertical downward branches instead of upper and lower circular loops around a central box; Neither Concentrated Urine nor Dilute Urine connects bac |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-07-savanna-food-web-network` | code image: The vertical layout is upside-down: Grass is at the top and Hawk is at the bottom, contradicting the bottom-to-top level specifications.; Agama Lizard is placed on a separate fif |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-10-carbon-cycle-schematic` | code image: Missing pictorial elements including cloud, tree, goat, factory, underground layer, dead log, and volcano; Elements arranged in an abstract circular flowchart instead of a landsc |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-13-nitrogen-cycle-flow` | code image: the code failed: er     TEMPLATES[spec["template"]](spec, out)     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/tools/codedraw/templates.py", line  |
| Biology | `C4-nigerian-biomes` | `C4-08-map-nigeria-state-biomes` | code image: the code failed: es=vertices)     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   File "/usr/local/lib/python3.13/site-packages/matplotlib/_api/__init__.py", line 259, in check_ |
| Physics | `A25b-refraction-glass-prism-lenses` | `A25b-02-convex-concave-lens-rays` | code image: In the right diagram, the central ray reflects off the lens instead of passing straight through undeflected; In both diagrams, the label Image overlaps the ray line |
| Physics | `A34-force-on-current-carrying-conductor` | `A34-01-fleming-left-hand-rule` | raw check: The middle finger is folded into the palm instead of being fully extended and pointing horizontally to the right at right angles to the thumb and index finger.; Only index finger  |
| Mathematics | `B6-matrices-and-determinants` | `B6-02-determinant-expansion-schematic` | code image: The arrow labeled Expand points to the left instead of pointing to the right |
| Economics | `A10-market-structures` | `A10-02-short-run-competitive-firm` | code image: Plots share a single set of axes instead of each having its own P and Q axes; In the Loss plot, the shaded loss rectangle does not reach the ATC curve at the profit-maximizing qu |
| Economics | `A14-public-finance` | `A14-01-tax-incidence-supply-demand` | code image: Panel B lacks separate vertical and horizontal axes; Shaded tax rectangles do not start from the vertical axis in either panel; Line S2 overlaps the Consumer label in both panels |
| Economics | `A17-industry-and-industrialization` | `A17-01-map-nigeria-industrial-clusters` | code image: The label Ikeja: IT & Manufacturing overlaps with the label Nnewi: Auto parts; Missing prominent dot for Ikeja near the southwest coast |
| Government | `B3-process-of-decolonization` | `B3-02-nigerian-nationalist-leaders-portraits` | portrait of a real person or Arabic script: placeholder kept |
| Use of English | `C1b-diphthongs-and-triphthongs` | `C1b-01-diphthongs-vowel-quadrilateral-chart` | code image: The label /ɔɪ/ at the top-left is upside down.; Lines severely overlap text labels (/eɪ/, /ʊə/, /aʊ/, and /əʊ/ are all crossed by arrow shafts).; Labels and arrowheads are jumble |
| Use of English | `C2a-consonants` | `C2a-03-consonant-articulation-sagittal-diagrams` | raw check: In the right diagram, the tongue tip does not press firmly against the gum ridge directly behind the upper front teeth; instead, the tongue is retracted and cupped, leaving a gap  |
| IRK | `A1b-preservation-of-the-glorious-quran` | `A1b-01-ancient-writing-materials` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A1d-divine-authenticity-of-the-glorious-quran` | `A1d-02-manuscript-evolution-pictorial` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A4b-suwar-al-kawthar-to-an-nas` | `A4b-01-surah-al-kawthar-quranic` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6a-hadith-sciences-and-collections` | `A6a-02-hadith-isnad-matn-structure` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6a-hadith-sciences-and-collections` | `A6a-03-al-muwatta-book-stand` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6b-selected-ahadith-of-an-nawawi` | `A6b-01-nawawi-forty-hadith-manuscript` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `B9-articles-of-faith` | `B9-02-revealed-holy-books-display` | portrait of a real person or Arabic script: placeholder kept |
| Accounting | `A18-information-technology-in-accounting` | `A18-02-data-processing-cycle-flowchart` | code image: Connecting lines lack arrowheads to indicate the direction of the cycle |
| Commerce | `A6a-aids-to-trade-advertising-banking-communication` | `A6a-01-communication-process-loop-flowchart` | code image: the code failed: er     TEMPLATES[spec["template"]](spec, out)     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/tools/codedraw/templates.py", line  |
| Geography | `D2-economic-and-human-geography` | `D2-01-nigeria-cash-crop-distribution` | code image: the code failed: ^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/.image-work/code/gen/D2-01-nigeria-cash-crop-distribution.py", line 24, in draw     ax.plot(poly[:, 0], poly[:,  |
| History | `A1-land-and-peoples-of-the-nigeria-area` | `A1-01-vegetation-map-nigeria-area` | code image: the code failed:  raise ValueError("'codes' must be a 1D list or array with the "     ...<2 lines>...                      f"but your codes have shape {codes.shape}") ValueError: |
| History | `C2-amalgamation-of-1914` | `C2-02-portrait-lord-frederick-lugard` | portrait of a real person or Arabic script: placeholder kept |
| History | `C5-social-development-under-colonial-rule` | `C5-01-map-colonial-rail-resources` | code image: the code failed: ])     ~~~~^^^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/.image-work/code/gen/C5-01-map-colonial-rail-resources.py", line 15, in draw     ax.plot(poly[:, 0] |
| History | `D11-nigeria-in-international-organizations` | `D11-01-map-ecowas-member-states` | code image: Internal national borders are drawn across ECOWAS member states instead of showing them merged without internal lines; Côte d'Ivoire is omitted from the ECOWAS shading, leaving a |
| History | `D2-nigerian-civil-war` | `D2-02-map-nigerian-civil-war` | code image: Outer country outline of Nigeria is completely missing; Red arrow bypasses rather than passes through Benin City; Red arrow overlaps the label Ore |
| History | `D7-babangida-regime` | `D7-02-historical-map-nigeria-states` | code image: The outer outline of Nigeria is completely missing |
| History | `D9-abacha-regime` | `D9-02-map-nigeria-states` | code image: Bayelsa label overlaps the southern border line of the map |
| History | `G1-new-imperialism-and-european-occupation` | `G1-01-historical-colonial-map-africa` | code image: Internal borders are drawn throughout the continent despite requesting none; The German East Africa region is uncolored white rather than matching Cameroon; Extra disclaimer text |

## Needs teacher review

- **All CRK images (100) and all IRK images (42)**, marked "Needs teacher review" in their galleries (`subjects/crk/images/GALLERY-crk.md`, `subjects/irk/images/GALLERY-irk.md`). CRK: Jesus and angels in a respectful flat style, God shown only by symbols such as light and clouds (the checker rejects pictures that show Jesus or angels where the scene did not ask for them). IRK: faceless figures, no prophets, no Arabic text.

- **Sketch maps** (Geography, History, Government, Economics, Biology, CRK, IRK, Literature): drawn in code from Natural Earth outlines with approximate zones and routes, captioned as sketches. They are fine for teaching positions but not for exact borders (for example the states of 1967, 1976 and 1991 are not shown with exact borders). A teacher should glance at them.
- **Biology re-labelled pictures**: the pictures are unchanged but some old label lists include process notes (for example in the breathing mechanism figure), which now show in a larger font.

## Cost

| Item | Cost |
|---|---|
| Main run: image generation, code drawing, checks, label placement (15 subjects) | $57.25 |
| Main run: reclassification | $0.35 |
| **Main run total** | **$57.60** |
| Cleanup pass (retries, simplified descriptions, rechecks, scar check; cap $10) | $5.80 |
| **Total** | **$63.40** |

Per-subject figures are in the table near the top. Re-rendering labels, the text formatter and the repairs cost nothing (no pictures were regenerated except the 16 retried placeholders). Batch mode was used for picture generation (about $0.034 per Flash image at the assumed half price); prices are the unverified list prices in `tools/gemini_pricing.json`.
