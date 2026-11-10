# Images report: Biology leftovers and 14 subjects

Run finished. **1331 of 1399 placeholders now have an image** (95%); **68 placeholders are still in the notes** (9 skipped by rule, the rest failed the checks after three tries). Spend for this run: **$57.60** of the $120 cap (the cap was not reached). Galleries for your phone: `subjects/<subject>/images/GALLERY-<subject>.md`.

Scope: Biology Sections B to E (451 placeholders, 353 already placed before this run) plus the other 14 subjects. Biology Section A and the remaining 10 subjects were left alone, and no notes text was edited (only alt text, which came with the image placement).

## Images placed and left per subject

| Subject | Placeholders | Placed | Left | AI pictures (planned) | Code drawings (planned) | Cost |
|---|---|---|---|---|---|---|
| Biology (B to E) | 451 | 431 | 20 | 333 | 118 | $10.89 |
| Physics | 154 | 147 | 7 | 35 | 119 | $7.59 |
| Chemistry | 68 | 67 | 1 | 27 | 41 | $2.87 |
| Mathematics | 65 | 63 | 2 | 0 | 65 | $1.87 |
| Economics | 61 | 58 | 3 | 3 | 58 | $3.65 |
| Government | 62 | 60 | 2 | 11 | 50 | $2.77 |
| Use of English | 31 | 28 | 3 | 10 | 21 | $1.76 |
| Literature in English | 26 | 26 | 0 | 12 | 14 | $1.05 |
| CRK | 103 | 100 | 3 | 95 | 8 | $5.36 |
| IRK | 50 | 42 | 8 | 18 | 25 | $1.75 |
| Accounting | 36 | 35 | 1 | 2 | 34 | $0.95 |
| Commerce | 27 | 26 | 1 | 9 | 18 | $1.11 |
| Geography | 67 | 63 | 4 | 25 | 42 | $4.42 |
| Agricultural Science | 108 | 107 | 1 | 92 | 16 | $6.20 |
| History | 90 | 78 | 12 | 24 | 65 | $5.00 |
| **Total** | **1399** | **1331** | **68** | | | **$57.60** |

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
| code drawing failed the layout/content check | 37 |
| picture failed the structure check (3 generations) | 19 |
| skipped by rule (real-person portrait or Arabic script) | 9 |
| labels could not be placed on the right parts | 2 |
| error: Image size (305357220 pixels) exceeds limit of 178956 | 1 |

Rules were followed: every image was generated with no text, checked, labelled in code from Gemini's positions, checked again, and flagged after repeated failure (two re-rolls, then one more fresh pass). I did not override the automatic checks. Many raw-check failures are about complex anatomy or apparatus (rib counts, tube connections, organ positions) where Gemini draws plausible but wrong pictures; a few are strict. Skipped by rule: 7 IRK images that need Arabic script, 1 Government portrait grid and 1 History portrait of a real person.

| Subject | Notes file | Image | Why it is still a placeholder |
|---|---|---|---|
| Biology | `B1-internal-structure` | `B1-11-rabbit-digestive-system-dissection` | raw check: Image contains text labels and leader lines throughout, violating the rule that the picture must contain no text or labels. |
| Biology | `B1-internal-structure` | `B1-12-mammalian-urinary-system` | raw check: In ventral view the right kidney should be on the viewer left and drawn slightly more cranial than the left, but here the kidney on the viewer left is drawn lower than the one on the right; |
| Biology | `B2d-mammalian-teeth` | `B2d-02-types-human-teeth` | labels still wrong after 3 placements: one long root; premolar; one or two roots; molar |
| Biology | `B2e-alimentary-canal-and-digestion` | `B2e-06-hepatobiliary-pancreatic-ducts` | raw check: The stomach is disconnected from the duodenum rather than connecting via the pyloric sphincter.; The bile duct connects into the pancreatic duct outside the duodenum rather than emptying to |
| Biology | `B3b-transport-in-plants` | `B3b-13-bubble-potometer-apparatus` | raw check: The arrow shows the bubble moving away from the shoot towards the beaker instead of towards the shoot; The cut stem of the leafy shoot does not reach into the water inside the flask; The fl |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-18-coleoptile-tropism-experiments` | raw check: In the top row, the second coleoptile has a severed tip floating above it rather than being a decapitated coleoptile with the tip removed; In the bottom row, the agar blocks are disproporti |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-12-fruit-placentation-types` | labels still wrong after 3 placements: free-central; central column; titles under each: marginal; axile; basal; parietal; superficial |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-16-fruit-seed-dispersal-mechanisms` | raw check: The middle left section is empty; only five panels are present instead of six distinct rounded boxes grouped properly. |
| Biology | `B7c-reproduction-in-mammals` | `B7c-09-contraceptive-methods-overview` | raw check: The chart has six boxes instead of the five requested, splitting the IUD category across two separate boxes. |
| Biology | `B9c-hormonal-control` | `B9c-02-negative-feedback-flow` | code image: Legend box boundary line overlaps the main title text |
| Biology | `B9d-homeostasis` | `B9d-07-osmoregulation-adh-feedback-flowchart` | code image: Arrow overlaps directly with text in the small volume of concentrated urine box; Box for urine volumes overlaps the collecting duct boxes |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-07-savanna-food-web-network` | code image: Missing arrow from rat to snake; Missing arrow from praying mantis to Agama lizard; Incorrect arrow from praying mantis to snake; The label secondary consumers overlaps the connector line  |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-10-carbon-cycle-schematic` | code image: the code failed: *map(cbook.sanitize_sequence, args),         **{k: cbook.sanitize_sequence(v) for k, v in kwargs.items()})   File "/usr/local/lib/python3.13/site-packages/matplotlib/axes/ |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-13-nitrogen-cycle-flow` | code image: Text label nitric acid in rain is cut off behind the goat box; Text label ammonification by putrefying bacteria overlaps the nitrites box border; Multiple arrows cross through text labels  |
| Biology | `C4-nigerian-biomes` | `C4-08-map-nigeria-state-biomes` | code image: Sahel savanna is depicted as a full-width horizontal strip placing Sokoto in the Sahel, contradicting the description where Sahel is only in northern Borno and Yobe and Sokoto belongs to t |
| Biology | `C7a-diseases` | `C7a-02-anopheles-mosquito-life-cycle` | raw check: The larva is drawn floating deep underwater and tilted diagonally rather than lying flat and parallel just below the water surface, and it incorrectly has a prominent breathing siphon typic |
| Biology | `D1-variation-in-population` | `D1-12-abo-blood-transfusion-compatibility` | code image: Curved self-donation arrows on each circle are missing or failed to render properly |
| Biology | `D2a-heredity-principles` | `D2a-06-monohybrid-gene-transmission` | code image: Fertilisation arrows to the second zygote (Aa) are incorrect: sperm with A does not connect to it, and it incorrectly receives two arrows from the maternal eggs instead of one from each pa |
| Biology | `D2b-applications-of-heredity` | `D2b-05-sickle-cell-trait-counselling` | code image: Gamete circles A and S above the second column overlap heavily with each other and with the label Mother's gametes; Label in bottom right cell reads $S instead of SS and overlaps the verti |
| Biology | `E2-evidence-of-evolution` | `E2-06-analogous-insect-bird-wings` | raw check: The bird wing skeleton incorrectly depicts a five-fingered human-like hand instead of the fused hand bones and reduced digits characteristic of avian wings. |
| Physics | `A18-structure-of-matter-kinetic-theory` | `A18-02-capillary-action-meniscus-comparison` | raw check: In the mercury tube on the right, the liquid level inside the tube is shown higher than the beaker level instead of lower than the beaker level. |
| Physics | `A20b-wave-characteristics-and-properties` | `A20b-01-wave-reflection-ray` | code image: Angle labels 'i' and 'r' overlap with blue wavefront lines; The arc marking the angle of reflection is drawn inconsistently and crosses the normal line; The incident wave direction ray col |
| Physics | `A24-reflection-of-light` | `A24-02-concave-mirror-image-ray` | code image: Panel 1 reflected rays do not all converge at focal point F; Panel 2 ray tracing is incomplete and erroneous with a ray ending in empty space; Panel 4 ray tracing is physically incorrect w |
| Physics | `A25b-refraction-glass-prism-lenses` | `A25b-02-convex-concave-lens-rays` | code image: In both diagrams, the image arrows do not align with or reach the intersection points of the traced rays.; In the left diagram, the image arrow is placed before the intersection point of t |
| Physics | `A2b-measurement-position-distance` | `A2b-01-vernier-caliper-reading` | code image: Numbers 4 and 5 overlap on the vernier scale; The bottom boundary line cuts directly through the Vernier Scale text label |
| Physics | `A34-force-on-current-carrying-conductor` | `A34-01-fleming-left-hand-rule` | raw check: The second finger (middle finger) is curled into the palm instead of being extended at 90 degrees to the thumb and first finger |
| Physics | `A5-equilibrium-of-forces` | `A5-04-principle-moments-balance` | code image: Missing triangular wedge pivot at the 50 cm mark; Missing hanging block of 60 g at the 30 cm mark; Missing hanging block of 40 g at the 80 cm mark; Text overlap between Counter-clockwise m |
| Chemistry | `A14a-hydrogen-and-halogens` | `A14a-03-hydrogen-chloride-fountain-experiment` | raw check: The flask is drawn with two separate necks instead of a single-necked round-bottom flask with a two-hole stopper; The water dropper is inserted into a side branch rather than through a two- |
| Mathematics | `A3-indices-logarithms-and-surds` | `A3-02-index-logarithmic-form-mapping` | code image: Connecting lines intersect and overlap the text log; Redundant disconnected label boxes appear in the center of the diagram |
| Mathematics | `B6-matrices-and-determinants` | `B6-02-determinant-expansion-schematic` | error: Image size (305357220 pixels) exceeds limit of 178956970 pixels, could be decompression bomb DOS attack. |
| Economics | `A10-market-structures` | `A10-02-short-run-competitive-firm` | code image: The image completely fails to match the description; it shows chemistry plots of Period 3 atomic and ionic radii instead of economics graphs for a perfectly competitive firm |
| Economics | `A14-public-finance` | `A14-01-tax-incidence-supply-demand` | code image: In Panel A, the dashed line S2 passes directly through the text 'Consumer's burden', causing text and line overlap. |
| Economics | `A17-industry-and-industrialization` | `A17-01-map-nigeria-industrial-clusters` | code image: The map outline of Nigeria is completely missing, leaving the icons and labels floating in empty space. |
| Government | `A7-political-ideologies` | `A7-01-feudal-system-social-pyramid` | code image: The label King - owns all land extends outside the top layer and overlaps the pyramid borders; Missing figures described in each layer including the king with crown, nobles, knights in arm |
| Government | `B3-process-of-decolonization` | `B3-02-nigerian-nationalist-leaders-portraits` | portrait of a real person or Arabic script: placeholder kept |
| Use of English | `C1b-diphthongs-and-triphthongs` | `C1b-01-diphthongs-vowel-quadrilateral-chart` | code image: Labels for /əʊ/ ('go') and /ɔɪ/ ('boy') are swapped, incorrectly labeling the glide trajectories. |
| Use of English | `C2a-consonants` | `C2a-02-rp-consonant-classification-chart` | code image: The label (zoo) overlaps the horizontal grid line between the Fricative and Affricate rows; The labels (shoe) and (chair) cross over the cell border lines into the rows below; The phonetic |
| Use of English | `C2a-consonants` | `C2a-03-consonant-articulation-sagittal-diagrams` | raw check: In the left diagram, the tongue tip is positioned behind the lower teeth instead of resting between the upper and lower teeth with air flowing over it; In the right diagram, the tongue tip  |
| CRK | `A3-leadership-qualities` | `A3-01-joseph-interpreting-pharaoh-dream` | raw check: Thought bubbles show only three cows each instead of seven fat cows and seven thin cows as required by the narrative description. |
| CRK | `B2-the-supremacy-of-god` | `B2-01-elijah-fire-mount-carmel` | raw check: Water trench is filled with boiling water rather than dried up as required by the label specifications |
| CRK | `B8-holiness-and-divine-call` | `B8-02-prophet-ezekiel-calling-scene` | raw check: Hand of God offering the word is missing; Ezekiel is not reaching up with open mouth to eat the scroll as described |
| IRK | `A1b-preservation-of-the-glorious-quran` | `A1b-01-ancient-writing-materials` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A1d-divine-authenticity-of-the-glorious-quran` | `A1d-02-manuscript-evolution-pictorial` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A4b-suwar-al-kawthar-to-an-nas` | `A4b-01-surah-al-kawthar-quranic` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6a-hadith-sciences-and-collections` | `A6a-02-hadith-isnad-matn-structure` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6a-hadith-sciences-and-collections` | `A6a-03-al-muwatta-book-stand` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `A6b-selected-ahadith-of-an-nawawi` | `A6b-01-nawawi-forty-hadith-manuscript` | portrait of a real person or Arabic script: placeholder kept |
| IRK | `B12-sources-and-schools-of-law` | `B12-03-islamic-madhhab-distribution-map` | code image: Legend labels are misaligned with color swatches: the green swatch has no text, the blue swatch is paired with Maliki, and Hanafi lacks a dedicated swatch; Legend box covers part of West A |
| IRK | `B9-articles-of-faith` | `B9-02-revealed-holy-books-display` | portrait of a real person or Arabic script: placeholder kept |
| Accounting | `A18-information-technology-in-accounting` | `A18-02-data-processing-cycle-flowchart` | code image: Connecting circular loop is missing arrowheads to indicate the direction of the cycle; Stage icons are missing and represented as literal bracketed text placeholders |
| Commerce | `A6a-aids-to-trade-advertising-banking-communication` | `A6a-01-communication-process-loop-flowchart` | code image: The red noise lightning bolt line overlaps and crosses directly through the text Message |
| Geography | `A5-elementary-surveying` | `A5-02-prismatic-compass` | raw check: The distant ranging pole is misaligned with the sighting axis between the prism and sighting vane; The sighting axis points away from the ranging pole rather than directly through the sight |
| Geography | `B5-water-bodies` | `B5-04-oxbow-lake-sequential` | raw check: Panel 1 shows an impossible self-intersecting or bifurcating loop instead of a normal river meander.; Panel 2 shows an enclosed kidney-bean shaped loop that has no river flowing in or out.; |
| Geography | `D1-broad-outline-of-nigeria` | `D1-01-nigeria-states-political-map` | code image: The 36 states of Nigeria are not shown; instead, arbitrary wavy lines are drawn across the map. |
| Geography | `D2-economic-and-human-geography` | `D2-01-nigeria-cash-crop-distribution` | code image: Legend box overlaps and cuts off the Groundnut & Cotton text label in the north; Lacks clear state boundaries required by the description; State name labels are extremely faint and partial |
| Agricultural Science | `C6-livestock-management` | `C6-03-rabbit-handling-housing` | raw check: The person holding the rabbit has three hands: one supporting the rump, one on top of the head or scruff, and an extra disembodied hand gripping the rabbit's chest. |
| History | `A1-land-and-peoples-of-the-nigeria-area` | `A1-01-vegetation-map-nigeria-area` | code image: the code failed: raw(sys.argv[1])     ~~~~^^^^^^^^^^^^^   File "/home/user/miyagi-jamb-notes/.image-work/code/gen/A1-01-vegetation-map-nigeria-area.py", line 16, in draw     if not raw_pol |
| History | `B4-benin` | `B4-01-timeline-th-century-benin` | code image: Text Economic prosperity & overlaps the left border line of the Oba Adolo box; Text British naval expedition overlaps the left border line of the Oba Ovonramwen box |
| History | `B8-european-penetration-and-impact` | `B8-01-map-european-niger-explorers` | code image: Title at the top is partially cut off and overlapped by the legend box |
| History | `C1-establishment-of-colonial-rule-up-to-1914` | `C1-01-map-nigeria-protectorates` | code image: Bottom caption text Sketch map: zones are approximate overlaps the map border line; Protectorate boundary dashed line stops abruptly in the center instead of spanning across the territory |
| History | `C2-amalgamation-of-1914` | `C2-02-portrait-lord-frederick-lugard` | portrait of a real person or Arabic script: placeholder kept |
| History | `C2-amalgamation-of-1914` | `C2-03-map-colonial-railways` | code image: The blue railway line to Kano overlaps directly over the text Northern Provinces; The blue railway line between Port Harcourt and Enugu overlaps directly over the text Southern Provinces |
| History | `C5-social-development-under-colonial-rule` | `C5-01-map-colonial-rail-resources` | code image: The legend box overlaps and partially obscures the Jos label and the branch line; The western railway line ends prematurely and does not reach the Kano label; The icons for train, ship, co |
| History | `D11-nigeria-in-international-organizations` | `D11-01-map-ecowas-member-states` | code image: Senegal, The Gambia, and Guinea-Bissau are incorrectly shaded as non-member states (tan) instead of ECOWAS member states (pale green); In the legend, the star symbol is misaligned below it |
| History | `D2-nigerian-civil-war` | `D2-02-map-nigerian-civil-war` | code image: Callout box for Federal Advance overlaps the Benue-Plateau state label; Sweeping offensive arrow into Mid-West is reduced to a faint, barely visible dashed line; Lagos label lacks a point  |
| History | `D7-babangida-regime` | `D7-02-historical-map-nigeria-states` | code image: The external national borders and coastline of Nigeria are missing, leaving outer state boundaries open and incomplete; An unexplained blue circle is shown next to Rivers |
| History | `D9-abacha-regime` | `D9-02-map-nigeria-states` | code image: Legend text in the upper left overlaps heavily with the country border line; State polygons are fragmented, poorly aligned with borders, and leave large gaps rather than forming a complete |
| History | `G1-new-imperialism-and-european-occupation` | `G1-01-historical-colonial-map-africa` | code image: Legend text labels are vertically misaligned with the color swatches, incorrectly pairing colors with colonial powers; Stray blue line fragments appear floating above the northern boundary |

## Needs teacher review

- **All CRK images (100) and all IRK images (42)**, marked "Needs teacher review" in their galleries (`subjects/crk/images/GALLERY-crk.md`, `subjects/irk/images/GALLERY-irk.md`). CRK: Jesus and angels in a respectful flat style, God shown only by symbols such as light and clouds (the checker rejects pictures that show Jesus or angels where the scene did not ask for them). IRK: faceless figures, no prophets, no Arabic text.

- **Sketch maps** (Geography, History, Government, Economics, Biology, CRK, IRK, Literature): drawn in code from Natural Earth outlines with approximate zones and routes, captioned as sketches. They are fine for teaching positions but not for exact borders (for example the states of 1967, 1976 and 1991 are not shown with exact borders). A teacher should glance at them.
- **Biology re-labelled pictures**: the pictures are unchanged but some old label lists include process notes (for example in the breathing mechanism figure), which now show in a larger font.

## Cost

| Item | Cost |
|---|---|
| Biology | $10.89 |
| Physics | $7.59 |
| Chemistry | $2.87 |
| Mathematics | $1.87 |
| Economics | $3.65 |
| Government | $2.77 |
| Use of English | $1.76 |
| Literature in English | $1.05 |
| CRK | $5.36 |
| IRK | $1.75 |
| Accounting | $0.95 |
| Commerce | $1.11 |
| Geography | $4.42 |
| Agricultural Science | $6.20 |
| History | $5.00 |
| Reclassification | $0.35 |
| **Total this run** | **$57.60** |

Per placed image this run cost about $0.059. Batch mode was used for all picture generation (about $0.034 per Flash image at the assumed half price).
