# Images plan (updated after the Gemini pilot)

Scope: every subject folder in `subjects/` (15 subjects). I read "the remaining 10 subjects" in your out-of-scope line as subjects not yet written. If you meant the nine older subjects here, use the two subtotals in the cost table. Biology Sections A1 to A3 are done (67 images, no placeholders left), so only Biology Sections B to E are counted. A classification file with every placeholder is in `IMAGES-CLASSIFICATION.csv`.

## Decisions (recorded after approval)

- **Gemini only** for all AI images, on `GEMINI_API_KEY`. OpenAI is removed from the plan and the tools.
- **matplotlib approved** and installed (version 3.11); noted in the README.
- **CRK:** Jesus and angels in a respectful flat style. **Never depict God**; use symbols such as light or clouds. **IRK:** faceless figures, no prophets, prayer and ablution positions as simple step diagrams. **All of these images are marked "Needs teacher review".**
- **Flags:** maps as simplified code-drawn sketches (Natural Earth data where borders matter). **Portraits of real people and Arabic-script images are skipped** and keep their placeholder text.
- **All 15 subjects** are in scope for the full run later.

## 1. Summary

- **1,399 placeholders** in 451 notes files.
- **AI-generated: 649** (46%). **Code-drawn: 665** (48%). **Skip or flag: 85** (6%).
- **Cost of the AI images (Gemini):** see section 6. Real prices from the pilot: $0.069 per image (Flash) and $0.146 (Pro). The pilot of 10 Biology images cost $1.51 including tests and retries.
- **Biology A3 camouflage image:** yes, it has a mistake (see section 2). It says "Parotid gland"; the notes and the alt text correctly say "parotoid". It needs a one-word fix.
- **Decisions:** recorded in the section above.

## 2. Biology A3 camouflage image

I opened `subjects/biology/images/A3-camouflage-defence.png`. The toad's label reads **"Parotid gland (poison)"**. In toads the poison gland behind the eye is the **parotoid** gland; a *parotid* gland is the salivary gland of mammals. The notes' alt text already says "parotoid", and the notes have no other use of "parotid".
The raw picture is not stored in the repo, so the label cannot be re-rendered from the spec. Options: (1) **recommended, free:** patch the finished PNG (paint the label box white and redraw "Parotoid gland (poison)" with Pillow in the same font); (2) regenerate the picture (about $0.07 with Gemini Flash) and relabel it, which would change the artwork. The other 66 Section A images should get a quick text check against the notes' spelling at the same time (cost: none).

## 3. Counts

| Subject | Placeholders | AI | Code | Flag | AI with a label list |
|---|---|---|---|---|---|
| Accounting | 36 | 3 | 33 | 0 | 2 |
| Agricultural Science | 108 | 68 | 39 | 1 | 48 |
| Biology (Sections B to E) | 451 | 328 | 117 | 6 | 318 |
| Chemistry | 68 | 28 | 40 | 0 | 17 |
| Commerce | 27 | 10 | 17 | 0 | 7 |
| CRK | 103 | 94 | 7 | 2 | 39 |
| Economics | 61 | 1 | 57 | 3 | 1 |
| Geography | 67 | 21 | 36 | 10 | 13 |
| Government | 62 | 13 | 43 | 6 | 8 |
| History | 90 | 23 | 25 | 42 | 9 |
| IRK | 50 | 15 | 22 | 13 | 9 |
| Literature in English | 26 | 12 | 12 | 2 | 4 |
| Mathematics | 65 | 0 | 65 | 0 | 0 |
| Physics | 154 | 27 | 127 | 0 | 9 |
| Use of English | 31 | 6 | 25 | 0 | 3 |
| **Total** | **1399** | **649** | **665** | **85** | **487** |

Per-file counts are in the appendix. "AI with a label list" counts AI placeholders that name the labels to add; the rest are scenes (for example CRK Bible scenes) that need no labels.

## 4. Classification

**Method.** Gemini Flash (about $0.10 in total) read every placeholder and sorted it with the rules below; I then reviewed samples from each group and moved items that were clearly misplaced (Arabic-script images, real people, map-like diagrams). The result is a first pass: the real check happens when the prompts are written.

**AI-generated (649).** Organisms, cells, anatomy, life cycles, apparatus pictures, farm tools and machines, landforms, scenes and Bible scenes. Biology is the bulk (328), then CRK (94), Agricultural Science (68), Chemistry, Physics, and History, Geography, IRK.

**Code-drawn (665).** Anything that must be exact: graphs and curves (physics, economics, maths, biology data), geometry and constructions, ray and wave diagrams, circuits, force diagrams, number lines, chemical structures and energy profiles, flowcharts, timelines, organisation charts, concept maps and tables, and ledger, cheque and statement layouts (accounting). Mathematics (65), Accounting (33) and Economics (57) are almost entirely code-drawn.

**Skip or flag (85).** Maps with real borders or places, portraits of real people, manuscripts and Arabic text. Alternatives are in the table below. By subject: History 42, IRK 13, Geography 10, Biology 6, Government 6, Economics 3, CRK 2, Literature in English 2, Agricultural Science 1.

**Sensitive images inside the AI group** (still classed AI, but I suggest your decision before they are made):
- **CRK:** about 38 scenes show Jesus, God or angels. This is normal in Christian textbooks; I suggest simple, respectful, flat illustrations and a quick review by a CRK teacher.
- **IRK:** about 13 images show people at prayer or ablution, and a few show historical scenes. Many Muslim publishers avoid faces; I suggest figures drawn without faces, and no depiction of the Prophet or any prophet (none is planned). Arabic text is never AI-generated (see below).
- **Arabic text:** six IRK images show Qur'an or hadith text. Image models garble Arabic, so they moved to the flag group: draw the artwork with AI and add the Arabic in code from a verified source, or use a public-domain page.

### Skip or flag list, with alternatives

| Subject | File | What it shows | Suggested alternative |
|---|---|---|---|
| Agricultural Science | `A3-agricultural-ecology` | Nigeria ecological zones map | Vector map derived from Natural Earth or simplified thematic GIS map of Nigeria |
| Biology | `C1-factors-affecting-distribution` | Nigeria rainfall and vegetation map | Schematic map of Nigeria rainfall zones drawn in matplotlib/cartopy or simple polygon outline |
| Biology | `C4-nigerian-biomes` | map of Nigerian vegetation belts | Vector map of Nigerian vegetation zones styled via Natural Earth data |
| Biology | `C4-nigerian-biomes` | map of Nigeria state biomes | Administrative boundary map of Nigeria shaded by biome from Wikimedia Commons |
| Biology | `C7a-diseases` | map of Africa meningitis belt | Schematic vector map of Africa with latitudinal meningitis belt drawn via Python/GeoPandas or Natural Earth base map |
| Biology | `C7d-conservation-parks-and-reserves` | map of Nigeria national parks | Nigeria National Parks Service map or Natural Earth Nigeria shapefile with park points in matplotlib |
| Biology | `E2-evidence-of-evolution` | biogeography lungfish world map | Schematic world map with species distribution markers drawn using GeoPandas or Natural Earth base map |
| CRK | `A4-divine-providence-guidance-and-protection` | tactical battle movement map | Schematic sketch drawn in code with approximate positions and no exact borders, or a public-domain base map (Natural Earth, Wikimedia Commons). |
| CRK | `C19-mission-to-the-gentiles` | map of Paul first journey | Base map from Wikimedia Commons or Natural Earth overlaid with route arrows from Syria to Cyprus and Asia Minor |
| Economics | `A17-industry-and-industrialization` | map of Nigeria industrial clusters | Schematic outline map of Nigeria with industrial labels drawn in code |
| Economics | `A18-natural-resources-and-the-nigerian-economy` | map of Nigeria natural resources | Simplified regional outline map of Nigeria with resource markers generated via code |
| Economics | `A22-international-economic-organizations` | map of ecowas member countries | Simplified regional map of West Africa generated from Natural Earth data |
| Geography | `A1-maps` | map types comparison panel | A schematic 3-panel comparison drawn in code with simplified vector outlines for topographic, choropleth, and sketch maps |
| Geography | `B11-environmental-hazards` | Nigeria environmental hazards map | Natural Earth Nigeria outline with stylized hazard zones in matplotlib |
| Geography | `B5-water-bodies` | world oceans and seas map | Natural Earth world coastline map labelled with matplotlib |
| Geography | `B5-water-bodies` | global ocean currents map | Wikimedia Commons world ocean currents map (Public Domain / CC0) |
| Geography | `C1-population` | global population density map | Natural Earth world base map with population density choropleth |
| Geography | `C3-selected-economic-activities` | world major ocean trade routes | Natural Earth world coastline map plotted with shipping routes via GeoPandas |
| Geography | `D1-broad-outline-of-nigeria` | Nigeria states political map | Natural Earth Nigeria admin-1 states boundaries GeoJSON |
| Geography | `D2-economic-and-human-geography` | Nigeria cash crop distribution map | Nigeria state-level choropleth or region overlay drawn using GeoPandas |
| Geography | `D2-economic-and-human-geography` | Nigeria manufacturing industries map | Nigeria outline map with factory coordinate scatter points via matplotlib |
| Geography | `D3-ecowas` | map of West Africa ECOWAS | Natural Earth administrative vector boundaries for West Africa coloured via matplotlib or geopandas |
| Government | `B3-process-of-decolonization` | Nigerian nationalist leaders portraits grid | Public-domain archival photographs of the eight nationalist leaders from Wikimedia Commons |
| Government | `B4-constitutional-development-in-nigeria` | map of Nigeria three regions 1946 | Simplified 3-region schematic map of Nigeria drawn in Matplotlib |
| Government | `B8-political-parties-and-party-politics-in-post-independence-nigeria` | map of early 1960s Nigeria regions | Schematic map of Nigeria 1960s regional political dominance drawn in Matplotlib |
| Government | `C3-nigerias-relations-with-african-countries` | map of Africa Nigerian foreign policy | Natural Earth map of Africa with intervention arrows from Nigeria |
| Government | `C4-nigeria-in-international-organizations` | map of West Africa ECOWAS members | Natural Earth West Africa base map with highlighted ECOWAS members |
| Government | `D1-international-organizations` | map of West Africa ECOWAS countries | Natural Earth boundary map highlighting ECOWAS states |
| History | `A1-land-and-peoples-of-the-nigeria-area` | vegetation map of Nigeria area | Simplified vegetation belts map of Nigeria using Natural Earth and public-domain ecological zones |
| History | `A2-early-centres-of-civilization` | map of early Nigerian civilizations | Base map of Nigeria with plotted historical archaeological sites |
| History | `A3-origins-and-formation-of-states` | map of pre-colonial Northern Nigeria | Historical boundary sketch of Kanem-Borno and Hausa Bakwai city-states |
| History | `A4-economic-activities-and-growth-of-states` | map of traditional Nigerian trade routes | Regional outline map of North and West Africa with overlay trade arrows |
| History | `A5-external-influences` | map of trans-Saharan trade routes | Historical trans-Saharan trade routes map from Wikimedia Commons |
| History | `A5-external-influences` | flow diagram Triangular Trade route | Schematic sketch drawn in code with approximate positions and no exact borders, or a public-domain base map (Natural Earth, Wikimedia Commons). |
| History | `B1-the-sokoto-caliphate` | map of 19th-century Sokoto Caliphate | Historical map of the Sokoto Caliphate and Borno Empire from Wikimedia Commons |
| History | `B2-kanem-borno` | map of northern Nigeria 19th century | Historical map showing Sokoto Caliphate and Kanem-Borno borders |
| History | `B3-yorubaland` | map of 19th-century Yorubaland | Historical map of 19th-century Yoruba settlements from Wikimedia Commons or schematic Python map |
| History | `B4-benin` | historical map of Benin relations | Historical regional map of Benin Kingdom and neighbors from Wikimedia Commons |
| History | `B5-nupe` | map of 19th-century Nupe | Historical central Nigeria map of Nupe Emirate from Wikimedia Commons |
| History | `B6-igbo` | map of Igboland historical relations | Regional trade map of southeastern Nigeria from Wikimedia Commons or simplified Matplotlib sketch |
| History | `B7-efik` | map of Cross River estuary | 19th-century Old Calabar coastal map from Wikimedia Commons |
| History | `B8-european-penetration-and-impact` | map of European Niger explorers | Historical map of Niger exploration routes from Wikimedia Commons |
| History | `B9-british-conquest-of-the-nigeria-area` | map of Lagos bombardment annexation | 19th-century coastal map of Lagos Colony from Wikimedia Commons |
| History | `C1-establishment-of-colonial-rule-up-to-1914` | map of 1906 Nigeria protectorates | Historical administrative map of 1906 Northern and Southern Nigeria from Wikimedia Commons |
| History | `C2-amalgamation-of-1914` | map of 1910 Nigeria protectorates | Map of Northern and Southern Nigeria protectorates (1910) from Wikimedia Commons |
| History | `C2-amalgamation-of-1914` | portrait of Lord Frederick Lugard | Public-domain archival photograph of Lord Frederick Lugard from Wikimedia Commons |
| History | `C2-amalgamation-of-1914` | map of 1914 colonial railways | Colonial Nigeria railway and provincial map (post-1914) from Wikimedia Commons |
| History | `C3-colonial-administration-after-amalgamation` | map of indirect rule systems | Regional boundary map of colonial Nigeria indirect rule from Wikimedia Commons |
| History | `C4-colonial-economy` | map of colonial railway network | Colonial Nigeria railway network map from Wikimedia Commons |
| History | `C5-social-development-under-colonial-rule` | map of colonial rail and resources | Map of colonial Nigerian rail lines and export centers from Wikimedia Commons |
| History | `C6-constitutional-developments-nationalism-and-independence` | map of 1946 three regions | 1946 Richards Constitution regional map of Nigeria from Wikimedia Commons |
| History | `D1-politics-of-first-republic-and-military-intervention` | map of 1964 four regions | First Republic four regions map of Nigeria from Wikimedia Commons |
| History | `D11-nigeria-in-international-organizations` | map of ECOWAS member states | ECOWAS member states political map from Wikimedia Commons |
| History | `D11-nigeria-in-international-organizations` | map of Nigerian peacekeeping missions | Peacekeeping map of Africa from Wikimedia Commons or Natural Earth basemap |
| History | `D2-nigerian-civil-war` | map of Nigerian civil war | Nigerian civil war 1967 frontlines map from Wikimedia Commons |
| History | `D3-gowon-regime` | map of 1967 twelve states | 1967 twelve states map of Nigeria from Wikimedia Commons |
| History | `D4-murtala-obasanjo-regime` | map of 1976 nineteen states | 1976 nineteen states map of Nigeria from Wikimedia Commons |
| History | `D7-babangida-regime` | historical map of Nigeria states | matplotlib/geopandas sketch of 1991 30-state borders of Nigeria or Wikimedia Commons 1991 Nigeria map |
| History | `D9-abacha-regime` | map of Nigeria 36 states | Python geopandas map of Nigeria 36 states highlighting 6 new states or Natural Earth administrative map |
| History | `E1-islamic-reform-movements-and-state-building` | historical map of West Africa | Simplified schematic map of West African empires or historical map from Wikimedia Commons |
| History | `E2-sierra-leone-liberia-and-missionary-activities` | historical coastal migration map | Schematic coastline map of West Africa drawn with geopandas or Natural Earth base map |
| History | `E3-egypt-under-mohammed-ali-and-khedive-ismail` | historical expansion map | Regional map of Egypt and Middle East with expansion arrows or Wikimedia Commons historical map |
| History | `E3-egypt-under-mohammed-ali-and-khedive-ismail` | battle schematic diagram | Schematic sketch drawn in code with approximate positions and no exact borders, or a public-domain base map (Natural Earth, Wikimedia Commons). |
| History | `F1-ethiopia-in-19th-century` | historical military expedition map | Horn of Africa base map with plotted expedition route or Wikimedia Commons historical map |
| History | `F2-mfecane` | historical migration route map | Schematic southern Africa map with migration arrows or Wikimedia Commons Mfecane map |
| History | `F3-great-trek` | historical frontier expansion map | Schematic Cape Colony frontier map or Wikimedia Commons Great Fish River map |
| History | `G1-new-imperialism-and-european-occupation` | historical colonial map of Africa | Geopandas 1914 colonial Africa map or public domain map from Wikimedia Commons |
| History | `G2-patterns-of-colonial-rule-in-africa` | colonial partition map of Africa | Geopandas 1914 Africa partition map or public domain map from Wikimedia Commons |
| History | `G3-politics-of-decolonization` | thematic decolonization map of Africa | Natural Earth Africa map shaded by independence path or Wikimedia Commons decolonization map |
| History | `G4-apartheid-in-south-africa` | historical land allocation map | Schematic map of South Africa Native Reserves vs white areas or Wikimedia Commons 1913 Land Act map |
| IRK | `A1b-preservation-of-the-glorious-quran` | ancient writing materials illustration | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `A1d-divine-authenticity-of-the-glorious-quran` | manuscript evolution pictorial illustration | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `A4b-suwar-al-kawthar-to-an-nas` | surah al-kawthar quranic manuscript | Vector-rendered Arabic text layout or high-res mushaf page from Wikimedia Commons |
| IRK | `A6a-hadith-sciences-and-collections` | al-muwatta book on stand | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `A6b-selected-ahadith-of-an-nawawi` | nawawi forty hadith manuscript | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `B10b-zakah-sawm-hajj-and-jihad` | hajj pilgrimage route schematic | Schematic sketch drawn in code with approximate positions and no exact borders, or a public-domain base map (Natural Earth, Wikimedia Commons). |
| IRK | `B12-sources-and-schools-of-law` | islamic madhhab distribution map | Blank political base map of Africa and Middle East from Natural Earth shaded with Python |
| IRK | `B9-articles-of-faith` | revealed holy books display | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `C16-the-life-of-prophet-muhammad` | prophet muhammad hijrah route map | Stylised Arabia coastline and route drawn schematically with Matplotlib/GeoPandas |
| IRK | `C18-early-contact-of-islam-with-africa` | early migration to abyssinia map | Red Sea regional base map from Natural Earth with migration route plotted |
| IRK | `C19-the-impact-of-islam-in-west-africa` | mansa musa hajj caravan | Public-domain archival photograph or portrait from Wikimedia Commons; or a simple symbolic sketch with no face. |
| IRK | `C19-the-impact-of-islam-in-west-africa` | timbuktu trade and sankore mosque | Draw the scene with no text, then add the Arabic with Pillow and a verified Qur'an text source (for example the Tanzil text), or use a public-domain mushaf page from Wiki |
| IRK | `C20-contributions-of-islam-to-education` | map of West African Islamic centers | Generate a schematic West Africa coastline and borders in Python with Matplotlib, marking Kano, Sokoto, and Timbuktu. |
| Literature in English | `B2-antony-and-cleopatra` | conceptual Mediterranean map Rome Alexandria | Create a simplified schematic Mediterranean map using Matplotlib and geopandas or Natural Earth base vectors. |
| Literature in English | `B3-so-the-path-does-not-die` | map of Sierra Leone and USA | Use Natural Earth vector outlines rendered via GeoPandas in Python showing West Africa and USA. |

**Overall suggestion for maps.** Most maps need only approximate positions (rainfall belts, vegetation belts, regions, trade routes). Draw them as a simplified labelled sketch in code with no borders, and say in the caption that it is a sketch. Use a public-domain base map (Natural Earth, Wikimedia Commons, or an official government map) only where exact state or country borders matter (for example the 36 states, the three regions of 1946, Africa in 1914).

## 5. Tools and pipeline

### How Biology Section A was made

From `tools/README.md` and `tools/specs/biology/`: the prompts for a topic were written by hand from each placeholder into `A#-prompts.json`; `generate.py` called an image model (1024 by 1024, medium quality, since replaced by Gemini) with a fixed house style (flat textbook illustration, white background, soft palette, **no text**); each raw image was looked at and regenerated if wrong (69 calls for 67 images, **$3.71**, about $0.054 each); coordinates were read off a gridded preview (`preview.py`), labels and leader lines were drawn with Pillow (`label.py`) from `A#-labels.json`, the result was checked again, `place_images.py` swapped each placeholder for the image, and `compress_images.py` cut file size by about 60%. Two raw images were edited by hand (tapeworm hooks, Ascaris).

### Review of the tools

| Tool | Works as is? | Change I would propose |
|---|---|---|
| `generate.py` | **Changed to Gemini** (done in the pilot): `--model`, `--suffix`, `--budget`, cost computed from token counts, `--models` lists the image models. | Done. |
| `preview.py` | Yes (`grid`, `zoom`, `small`) plus a new `sheet` mode (contact sheet, done). | Done. |
| `label.py` | Yes. | None. |
| `place_images.py` | Now takes `N:NAME=alt` to replace one slot (done, tested). Slot numbers count placeholders and already placed images, so they stay stable. | Done. |
| `compress_images.py` | Yes. | None. |
| New: `extract_prompts.py` | Done. | Reads a notes file, pulls out each AI placeholder, strips the label list and inline label text, and writes `-prompts.json` and `-labels-todo.json`. |

### Proposed pipeline (matches Section A)

1. **Extract** the AI placeholders per topic into `tools/specs/<subject>/<topic>-prompts.json` (new `extract_prompts.py`); I check each prompt for counts and positions, because "exactly N parts" fixes most errors (as with the Ascaris lips).
2. **Generate** with `generate.py` (Gemini, square 1024 image, same house style, no text). Review in contact sheets; regenerate bad ones.
3. **Label** only the AI images that have a label list (487 of 649): grid preview, coordinates, `label.py`, then check. The 162 scenes without label lists skip this step and go straight to placing.
4. **Code-drawn images**: matplotlib (approved and installed) with the shared style in `tools/codedraw/style.py` (Inter font, same palette), one function per image; ten samples are in `tools/codedraw/samples.py`. Natural Earth data (public domain, `tools/data/`) where real outlines matter.
5. **Place, compress, commit**: `place_images.py` (with the `N:NAME=alt` change), `compress_images.py`, one commit per topic's images, pushed to `main` (CLAUDE.md rule).
6. Stop and report after each subject: images made, retries, real cost.

### Which image model, and why

**Gemini only**, on `GEMINI_API_KEY`. Models available to the key: `gemini-2.5-flash-image`, `gemini-3.1-flash-image`, `gemini-3-pro-image` (also `nano-banana-pro-preview` and preview variants). I tested the heart prompt on the first three. `gemini-2.5-flash-image` ($0.039) was crude and anatomically wrong. `gemini-3.1-flash-image` ($0.069) and `gemini-3-pro-image` ($0.146) were close; Pro was a little cleaner and better on multi-part experiment diagrams, so the pilot used Flash first and Pro for the hardest four. **Recommendation:** Flash 3.1 as the default, Pro for hard anatomy, multi-panel experiment diagrams and retries.

Both models sometimes write text or numbers despite the no-text rule (4 of 14 first tries) and draw arrows when the placeholder asks for them (the heart). The pipeline paints out stray text with `label.py`'s `whiten` option or re-rolls, and arrows requested in the placeholder are kept or drawn in code.

## 6. Cost estimate (AI images only, Gemini)

Real prices from the pilot, computed from the token counts the API returned: **gemini-3.1-flash-image $0.0686 per image, gemini-3-pro-image $0.1455 per image** (rates are best-known list prices, unverified). Plan: Flash for first tries, Pro for the hardest diagrams (about 15%) and for retries. Expected per image = 85% Flash + 15% Pro = $0.0801, times 1.15 for retries. Low = all Flash, no retries. High = 40% retries on the mixed rate.

| Subject | AI images | Low | Expected | High |
|---|---|---|---|---|
| Accounting | 3 | $0.21 | $0.28 | $0.34 |
| Agricultural Science | 68 | $4.66 | $6.27 | $7.63 |
| Biology (Sections B to E) | 328 | $22.50 | $30.23 | $36.80 |
| Chemistry | 28 | $1.92 | $2.58 | $3.14 |
| Commerce | 10 | $0.69 | $0.92 | $1.12 |
| CRK | 94 | $6.45 | $8.66 | $10.55 |
| Economics | 1 | $0.07 | $0.09 | $0.11 |
| Geography | 21 | $1.44 | $1.94 | $2.36 |
| Government | 13 | $0.89 | $1.20 | $1.46 |
| History | 23 | $1.58 | $2.12 | $2.58 |
| IRK | 15 | $1.03 | $1.38 | $1.68 |
| Literature in English | 12 | $0.82 | $1.11 | $1.35 |
| Mathematics | 0 | $0.00 | $0.00 | $0.00 |
| Physics | 27 | $1.85 | $2.49 | $3.03 |
| Use of English | 6 | $0.41 | $0.55 | $0.67 |
| **Total** | **649** | **$44.52** | **$59.81** | **$72.81** |

The Gemini image models list `batchGenerateContent`, which is usually half price; I have **not** tested it for images, so the table is at standard price. If it works, the expected total would be about half. Code-drawn and flagged images have no API cost.

### Pilot result (done)

Ten Biology B images were generated with Gemini; the real total, including tests and retries, was **$1.51** of the $2 cap. See `PILOT-GALLERY.md` for every image, its cost and the accuracy problems found.

## 7. Remaining decisions

1. **Approve the full run** after the pilot (see `PILOT-GALLERY.md`): model split (Flash default, Pro for hard images and retries), the treatment of stray text, and a Batch API test for half price.
2. **Teacher review:** CRK and IRK images are marked "Needs teacher review" (see Decisions above).
3. **`CLAUDE.md` image rules** still say OpenAI; not changed in this run.

## Appendix: placeholders per file

Columns: total, AI, Code, Flag.

### Accounting

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-nature-and-significance-of-bookkeeping-and-accounting` | 2 | 0 | 2 | 0 |
| `A10-manufacturing-accounts` | 2 | 0 | 2 | 0 |
| `A11-accounts-of-not-for-profit-making-organizations` | 2 | 0 | 2 | 0 |
| `A12-departmental-accounts` | 2 | 0 | 2 | 0 |
| `A13-branch-accounts` | 3 | 0 | 3 | 0 |
| `A14-joint-venture-accounts` | 1 | 0 | 1 | 0 |
| `A15-partnership-accounts` | 2 | 0 | 2 | 0 |
| `A16-introduction-to-company-accounts` | 3 | 0 | 3 | 0 |
| `A17-public-sector-accounting` | 2 | 0 | 2 | 0 |
| `A18-information-technology-in-accounting` | 3 | 1 | 2 | 0 |
| `A2-principles-of-double-entry` | 2 | 0 | 2 | 0 |
| `A3-ethics-professional-and-regulatory-bodies` | 2 | 1 | 1 | 0 |
| `A4-cash-book` | 2 | 0 | 2 | 0 |
| `A5-bank-transactions-and-reconciliation-statements` | 2 | 0 | 2 | 0 |
| `A6-final-accounts-of-a-sole-trader` | 3 | 0 | 3 | 0 |
| `A7-stock-valuation` | 1 | 1 | 0 | 0 |
| `A8-control-accounts` | 1 | 0 | 1 | 0 |
| `A9-incomplete-records-and-single-entry` | 1 | 0 | 1 | 0 |

### Agricultural Science

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-meaning-and-scope-of-agriculture` | 3 | 2 | 1 | 0 |
| `A2-importance-of-agriculture` | 2 | 2 | 0 | 0 |
| `A3-agricultural-ecology` | 2 | 1 | 0 | 1 |
| `A4-agricultural-genetics` | 2 | 0 | 2 | 0 |
| `A5-farm-inputs` | 2 | 2 | 0 | 0 |
| `A6-history-of-agricultural-development` | 2 | 2 | 0 | 0 |
| `A7-roles-of-government-and-ngos` | 2 | 1 | 1 | 0 |
| `B1-rocks-and-soil-formation` | 3 | 0 | 3 | 0 |
| `B10-pasture-and-forage-crops` | 2 | 2 | 0 | 0 |
| `B11-floriculture` | 2 | 2 | 0 | 0 |
| `B12-weeds` | 2 | 2 | 0 | 0 |
| `B13-crop-diseases` | 3 | 3 | 0 | 0 |
| `B14-crop-pests` | 3 | 1 | 2 | 0 |
| `B15-forest-management` | 2 | 2 | 0 | 0 |
| `B2-soil-water-and-soil-conservation` | 3 | 1 | 2 | 0 |
| `B3-soil-fertility` | 3 | 1 | 2 | 0 |
| `B4-land-preparation-and-soil-tillage` | 2 | 1 | 1 | 0 |
| `B5-plant-forms-and-functions` | 4 | 3 | 1 | 0 |
| `B6-growth-development-and-reproduction` | 3 | 1 | 2 | 0 |
| `B7-plant-propagation-methods` | 3 | 2 | 1 | 0 |
| `B8-cropping-systems-and-planting-patterns` | 3 | 2 | 1 | 0 |
| `B9-crop-husbandry` | 3 | 3 | 0 | 0 |
| `C1-forms-and-classification-of-major-farm-animals` | 5 | 5 | 0 | 0 |
| `C2-general-terminologies-in-animal-production` | 2 | 1 | 1 | 0 |
| `C3-anatomy-and-physiology-of-farm-animals` | 2 | 0 | 2 | 0 |
| `C4-reproduction-in-farm-animals` | 2 | 0 | 2 | 0 |
| `C5-animal-nutrition` | 2 | 1 | 1 | 0 |
| `C6-livestock-management` | 4 | 4 | 0 | 0 |
| `C7-animal-health` | 2 | 0 | 2 | 0 |
| `C8-fisheries-and-wildlife` | 2 | 1 | 1 | 0 |
| `C9-bee-keeping` | 3 | 3 | 0 | 0 |
| `D1-factors-of-agricultural-production` | 2 | 1 | 1 | 0 |
| `D2-basic-economic-principles` | 2 | 0 | 2 | 0 |
| `D3-labour-management` | 2 | 2 | 0 | 0 |
| `D4-farm-management` | 1 | 1 | 0 | 0 |
| `D5-marketing-of-agricultural-produce` | 1 | 1 | 0 | 0 |
| `D6-agricultural-extension` | 2 | 1 | 1 | 0 |
| `E1-farm-surveying-and-farmstead-planning` | 3 | 1 | 2 | 0 |
| `E2-simple-farm-tools` | 2 | 2 | 0 | 0 |
| `E3-farm-machinery-and-implements` | 2 | 2 | 0 | 0 |
| `E4-mechanization-and-sources-of-farm-power` | 2 | 2 | 0 | 0 |
| `E5-processing-and-storage` | 4 | 3 | 1 | 0 |
| `E6-introduction-to-biotechnology` | 2 | 0 | 2 | 0 |
| `E7-application-of-ict-in-agriculture` | 2 | 1 | 1 | 0 |
| `E8-agricultural-research-and-statistics` | 1 | 0 | 1 | 0 |

### Biology (Sections B to E)

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `B1-internal-structure` | 14 | 6 | 8 | 0 |
| `B2a-modes-and-types-of-nutrition` | 11 | 10 | 1 | 0 |
| `B2b-plant-nutrition` | 12 | 10 | 2 | 0 |
| `B2c-food-substances-and-food-tests` | 15 | 12 | 3 | 0 |
| `B2d-mammalian-teeth` | 8 | 7 | 1 | 0 |
| `B2e-alimentary-canal-and-digestion` | 12 | 8 | 4 | 0 |
| `B3a-transport-in-animals` | 18 | 10 | 8 | 0 |
| `B3b-transport-in-plants` | 16 | 16 | 0 | 0 |
| `B4a-respiratory-organs-and-gaseous-exchange` | 14 | 14 | 0 | 0 |
| `B4b-cellular-respiration` | 13 | 7 | 6 | 0 |
| `B5-excretion` | 13 | 11 | 2 | 0 |
| `B6a-support-and-movement-in-plants` | 18 | 17 | 1 | 0 |
| `B6b-support-and-movement-in-animals` | 13 | 13 | 0 | 0 |
| `B7a-asexual-reproduction` | 10 | 10 | 0 | 0 |
| `B7b-reproduction-in-flowering-plants` | 16 | 15 | 1 | 0 |
| `B7c-reproduction-in-mammals` | 9 | 8 | 1 | 0 |
| `B8-growth` | 12 | 8 | 4 | 0 |
| `B9a-nervous-coordination` | 14 | 12 | 2 | 0 |
| `B9b-sense-organs` | 19 | 10 | 9 | 0 |
| `B9c-hormonal-control` | 15 | 13 | 2 | 0 |
| `B9d-homeostasis` | 10 | 5 | 5 | 0 |
| `C1-factors-affecting-distribution` | 13 | 10 | 2 | 1 |
| `C2-symbiotic-interactions-and-energy-flow` | 14 | 6 | 8 | 0 |
| `C3-natural-habitats` | 10 | 10 | 0 | 0 |
| `C4-nigerian-biomes` | 9 | 6 | 1 | 2 |
| `C5-ecology-of-populations` | 9 | 5 | 4 | 0 |
| `C6-soil` | 14 | 13 | 1 | 0 |
| `C7a-diseases` | 10 | 7 | 2 | 1 |
| `C7b-drug-abuse` | 5 | 1 | 4 | 0 |
| `C7c-pollution-and-sanitation` | 10 | 7 | 3 | 0 |
| `C7d-conservation-parks-and-reserves` | 5 | 3 | 1 | 1 |
| `D1-variation-in-population` | 14 | 3 | 11 | 0 |
| `D2a-heredity-principles` | 15 | 3 | 12 | 0 |
| `D2b-applications-of-heredity` | 9 | 7 | 2 | 0 |
| `D3-biotechnology` | 8 | 8 | 0 | 0 |
| `E1-theories-of-evolution` | 10 | 9 | 1 | 0 |
| `E2-evidence-of-evolution` | 14 | 8 | 5 | 1 |

### Chemistry

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-separation-of-mixtures` | 3 | 3 | 0 | 0 |
| `A10-electrolysis` | 2 | 0 | 2 | 0 |
| `A11-energy-changes` | 2 | 1 | 1 | 0 |
| `A12-rates-of-chemical-reaction` | 4 | 1 | 3 | 0 |
| `A13-chemical-equilibra` | 2 | 1 | 1 | 0 |
| `A14a-hydrogen-and-halogens` | 3 | 3 | 0 | 0 |
| `A14b-oxygen-and-sulphur` | 3 | 1 | 2 | 0 |
| `A14c-nitrogen-and-carbon` | 4 | 3 | 1 | 0 |
| `A15a-general-and-representative-metals` | 1 | 0 | 1 | 0 |
| `A15b-transition-metals-and-alloys` | 3 | 2 | 1 | 0 |
| `A16a-hydrocarbons` | 5 | 1 | 4 | 0 |
| `A16b-alkanols-alkanals-and-acids` | 4 | 3 | 1 | 0 |
| `A16c-carbohydrates-proteins-polymers` | 2 | 0 | 2 | 0 |
| `A17-chemistry-and-industry` | 3 | 2 | 1 | 0 |
| `A18-astronomical-chemistry` | 3 | 2 | 1 | 0 |
| `A2-chemical-combination` | 4 | 0 | 4 | 0 |
| `A3-kinetic-theory-and-gas-laws` | 3 | 0 | 3 | 0 |
| `A4-atomic-structure-and-bonding` | 3 | 0 | 3 | 0 |
| `A5-nuclear-chemistry` | 4 | 0 | 4 | 0 |
| `A6-solubility` | 3 | 2 | 1 | 0 |
| `A7-environmental-pollution` | 3 | 1 | 2 | 0 |
| `A8-acids-bases-and-salts` | 2 | 1 | 1 | 0 |
| `A9-oxidation-and-reduction` | 2 | 1 | 1 | 0 |

### Commerce

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-commerce` | 1 | 0 | 1 | 0 |
| `A10-money` | 2 | 2 | 0 | 0 |
| `A11-stock-exchange` | 2 | 1 | 1 | 0 |
| `A12-elements-of-business-management` | 3 | 0 | 3 | 0 |
| `A13-elements-of-marketing` | 1 | 0 | 1 | 0 |
| `A14-legal-aspects-of-business` | 2 | 1 | 1 | 0 |
| `A15-commodity-exchange` | 2 | 2 | 0 | 0 |
| `A16-business-environment-and-social-responsibility` | 2 | 1 | 1 | 0 |
| `A2-occupation` | 1 | 0 | 1 | 0 |
| `A3-production` | 1 | 1 | 0 | 0 |
| `A4a-trade-home-trade` | 1 | 0 | 1 | 0 |
| `A4b-trade-foreign-trade` | 1 | 0 | 1 | 0 |
| `A5-purchase-and-sale-of-goods` | 1 | 0 | 1 | 0 |
| `A6a-aids-to-trade-advertising-banking-communication` | 1 | 0 | 1 | 0 |
| `A6b-aids-to-trade-insurance-tourism-transportation-warehousing` | 2 | 2 | 0 | 0 |
| `A7-business-units` | 1 | 0 | 1 | 0 |
| `A8-financing-business` | 2 | 0 | 2 | 0 |
| `A9-trade-associations` | 1 | 0 | 1 | 0 |

### CRK

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-sovereignty-of-god` | 2 | 2 | 0 | 0 |
| `A2-the-covenant` | 2 | 2 | 0 | 0 |
| `A3-leadership-qualities` | 3 | 3 | 0 | 0 |
| `A4-divine-providence-guidance-and-protection` | 2 | 1 | 0 | 1 |
| `A5-parental-responsibility` | 3 | 3 | 0 | 0 |
| `A6-obedience-and-disobedience` | 2 | 2 | 0 | 0 |
| `A7-a-man-after-gods-own-heart` | 2 | 2 | 0 | 0 |
| `A8-decision-making` | 2 | 2 | 0 | 0 |
| `B1-greed-and-its-effects` | 2 | 2 | 0 | 0 |
| `B2-the-supremacy-of-god` | 1 | 1 | 0 | 0 |
| `B3-religious-reforms-in-judah` | 2 | 2 | 0 | 0 |
| `B4-concern-for-judah` | 2 | 2 | 0 | 0 |
| `B5-faith-courage-and-protection` | 2 | 2 | 0 | 0 |
| `B6-gods-message-to-nineveh` | 2 | 2 | 0 | 0 |
| `B7-social-justice-true-religion-and-divine-love` | 2 | 2 | 0 | 0 |
| `B8-holiness-and-divine-call` | 2 | 2 | 0 | 0 |
| `B9-punishment-and-hope` | 2 | 2 | 0 | 0 |
| `C1-birth-and-early-life-of-jesus` | 3 | 3 | 0 | 0 |
| `C10-triumphal-entry-and-cleansing-of-the-temple` | 2 | 2 | 0 | 0 |
| `C11-the-last-supper` | 3 | 3 | 0 | 0 |
| `C12-trials-and-death-of-jesus` | 2 | 2 | 0 | 0 |
| `C13-resurrection-appearances-and-ascension` | 2 | 2 | 0 | 0 |
| `C14-jesus-teachings-about-himself` | 2 | 2 | 0 | 0 |
| `C15-love` | 2 | 1 | 1 | 0 |
| `C16-fellowship-in-the-early-church` | 2 | 2 | 0 | 0 |
| `C17-holy-spirit-and-mission-of-the-church` | 2 | 2 | 0 | 0 |
| `C18-opposition-to-the-gospel-message` | 1 | 1 | 0 | 0 |
| `C19-mission-to-the-gentiles` | 3 | 2 | 0 | 1 |
| `C2-baptism-and-temptation-of-jesus` | 2 | 2 | 0 | 0 |
| `C3-discipleship` | 2 | 2 | 0 | 0 |
| `C4-miracles` | 2 | 2 | 0 | 0 |
| `C5-the-parables` | 2 | 2 | 0 | 0 |
| `C6-sermon-on-the-mount` | 2 | 2 | 0 | 0 |
| `C7-mission-of-the-disciples` | 2 | 2 | 0 | 0 |
| `C8-the-great-confession` | 2 | 2 | 0 | 0 |
| `C9-the-transfiguration` | 1 | 1 | 0 | 0 |
| `D1-justification-by-faith` | 3 | 2 | 1 | 0 |
| `D10-dignity-of-labour` | 3 | 3 | 0 | 0 |
| `D11-the-second-coming-of-christ` | 2 | 2 | 0 | 0 |
| `D12-impartiality` | 2 | 2 | 0 | 0 |
| `D13-effective-prayer` | 2 | 2 | 0 | 0 |
| `D14-christian-living-in-the-community` | 2 | 1 | 1 | 0 |
| `D15-corruption` | 1 | 1 | 0 | 0 |
| `D16-sexual-immorality` | 1 | 1 | 0 | 0 |
| `D2-the-law-and-grace` | 1 | 1 | 0 | 0 |
| `D3-new-life-in-christ` | 1 | 1 | 0 | 0 |
| `D4-christians-as-joint-heirs-with-christ` | 1 | 1 | 0 | 0 |
| `D5-humility` | 2 | 1 | 1 | 0 |
| `D6-forgiveness` | 2 | 1 | 1 | 0 |
| `D7-spiritual-gifts` | 2 | 2 | 0 | 0 |
| `D8-christian-giving` | 2 | 1 | 1 | 0 |
| `D9-civic-responsibility` | 2 | 1 | 1 | 0 |

### Economics

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-economics-as-a-science` | 1 | 0 | 1 | 0 |
| `A10-market-structures` | 6 | 0 | 6 | 0 |
| `A11-national-income` | 2 | 0 | 2 | 0 |
| `A12-money-and-inflation` | 2 | 0 | 2 | 0 |
| `A13-financial-institutions` | 2 | 0 | 2 | 0 |
| `A14-public-finance` | 2 | 0 | 2 | 0 |
| `A15-economic-growth-and-development` | 2 | 0 | 2 | 0 |
| `A16-agriculture-in-nigeria` | 2 | 1 | 1 | 0 |
| `A17-industry-and-industrialization` | 2 | 0 | 1 | 1 |
| `A18-natural-resources-and-the-nigerian-economy` | 2 | 0 | 1 | 1 |
| `A19-business-organizations` | 2 | 0 | 2 | 0 |
| `A2-economic-systems` | 1 | 0 | 1 | 0 |
| `A20-population` | 4 | 0 | 4 | 0 |
| `A21-international-trade` | 2 | 0 | 2 | 0 |
| `A22-international-economic-organizations` | 2 | 0 | 1 | 1 |
| `A23-factors-of-production-and-their-theories` | 2 | 0 | 2 | 0 |
| `A3-methods-and-tools-of-economic-analysis` | 4 | 0 | 4 | 0 |
| `A4-theory-of-demand` | 4 | 0 | 4 | 0 |
| `A5-theory-of-consumer-behaviour` | 4 | 0 | 4 | 0 |
| `A6-theory-of-supply` | 3 | 0 | 3 | 0 |
| `A7-theory-of-price-determination` | 3 | 0 | 3 | 0 |
| `A8-theory-of-production` | 2 | 0 | 2 | 0 |
| `A9-theory-of-costs-and-revenue` | 5 | 0 | 5 | 0 |

### Geography

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-maps` | 2 | 0 | 1 | 1 |
| `A2-scale-and-measurement` | 4 | 1 | 3 | 0 |
| `A3-map-reading-and-interpretation` | 4 | 0 | 4 | 0 |
| `A4-statistical-data-maps-and-diagrams` | 6 | 0 | 6 | 0 |
| `A5-elementary-surveying` | 3 | 1 | 2 | 0 |
| `A6-geographic-information-system` | 3 | 1 | 2 | 0 |
| `B1-the-earth-as-a-planet` | 3 | 1 | 2 | 0 |
| `B10-environmental-interaction` | 2 | 1 | 1 | 0 |
| `B11-environmental-hazards` | 2 | 1 | 0 | 1 |
| `B12-environmental-conservation` | 2 | 1 | 1 | 0 |
| `B2-the-earth-crust` | 3 | 2 | 1 | 0 |
| `B3-volcanism-and-earthquakes` | 3 | 3 | 0 | 0 |
| `B4-denudation-processes` | 4 | 3 | 1 | 0 |
| `B5-water-bodies` | 4 | 1 | 1 | 2 |
| `B6-weather-and-climate` | 3 | 0 | 3 | 0 |
| `B7-vegetation` | 2 | 2 | 0 | 0 |
| `B8-soils` | 2 | 1 | 1 | 0 |
| `B9-environmental-resources` | 2 | 0 | 2 | 0 |
| `C1-population` | 3 | 0 | 2 | 1 |
| `C2-settlement` | 3 | 1 | 2 | 0 |
| `C3-selected-economic-activities` | 3 | 1 | 1 | 1 |
| `D1-broad-outline-of-nigeria` | 1 | 0 | 0 | 1 |
| `D2-economic-and-human-geography` | 2 | 0 | 0 | 2 |
| `D3-ecowas` | 1 | 0 | 0 | 1 |

### Government

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-definition-and-scope-of-government` | 2 | 2 | 0 | 0 |
| `A10-processes-of-legislation` | 1 | 0 | 1 | 0 |
| `A11-citizenship` | 2 | 1 | 1 | 0 |
| `A12-the-electoral-process` | 3 | 1 | 2 | 0 |
| `A13-political-parties-and-party-systems` | 2 | 1 | 1 | 0 |
| `A14-pressure-groups` | 1 | 0 | 1 | 0 |
| `A15-public-opinion` | 1 | 1 | 0 | 0 |
| `A16-the-civil-service-public-service` | 1 | 0 | 1 | 0 |
| `A2-basic-concepts-of-government` | 1 | 0 | 1 | 0 |
| `A3-forms-of-government` | 2 | 1 | 1 | 0 |
| `A4-arms-of-government` | 2 | 0 | 2 | 0 |
| `A5-structures-of-governance` | 2 | 0 | 2 | 0 |
| `A6-systems-of-governance` | 1 | 0 | 1 | 0 |
| `A7-political-ideologies` | 2 | 2 | 0 | 0 |
| `A8-constitution` | 2 | 1 | 1 | 0 |
| `A9-principles-of-democratic-government` | 2 | 0 | 2 | 0 |
| `B1-pre-colonial-polities` | 3 | 0 | 3 | 0 |
| `B10-public-corporations-and-parastatals` | 2 | 0 | 2 | 0 |
| `B11-local-government` | 2 | 1 | 1 | 0 |
| `B12-military-in-nigerian-politics` | 1 | 0 | 1 | 0 |
| `B2-imperialists-penetration` | 2 | 0 | 2 | 0 |
| `B3-process-of-decolonization` | 2 | 0 | 1 | 1 |
| `B4-constitutional-development-in-nigeria` | 3 | 0 | 2 | 1 |
| `B5-post-independence-constitutions` | 2 | 0 | 2 | 0 |
| `B6-institutions-of-government-in-post-independence-nigeria` | 2 | 0 | 2 | 0 |
| `B7-public-commissions-established-by-constitutions` | 1 | 0 | 1 | 0 |
| `B8-political-parties-and-party-politics-in-post-independence-nigeria` | 3 | 1 | 1 | 1 |
| `B9-structure-and-workings-of-nigerian-federalism` | 2 | 0 | 2 | 0 |
| `C1-foreign-policy` | 2 | 0 | 2 | 0 |
| `C2-nigerias-foreign-policy` | 2 | 1 | 1 | 0 |
| `C3-nigerias-relations-with-african-countries` | 2 | 0 | 1 | 1 |
| `C4-nigeria-in-international-organizations` | 2 | 0 | 1 | 1 |
| `D1-international-organizations` | 2 | 0 | 1 | 1 |

### History

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-land-and-peoples-of-the-nigeria-area` | 3 | 1 | 1 | 1 |
| `A2-early-centres-of-civilization` | 4 | 2 | 1 | 1 |
| `A3-origins-and-formation-of-states` | 2 | 0 | 1 | 1 |
| `A4-economic-activities-and-growth-of-states` | 2 | 1 | 0 | 1 |
| `A5-external-influences` | 3 | 1 | 0 | 2 |
| `B1-the-sokoto-caliphate` | 1 | 0 | 0 | 1 |
| `B2-kanem-borno` | 2 | 0 | 1 | 1 |
| `B3-yorubaland` | 2 | 1 | 0 | 1 |
| `B4-benin` | 2 | 0 | 1 | 1 |
| `B5-nupe` | 2 | 1 | 0 | 1 |
| `B6-igbo` | 2 | 1 | 0 | 1 |
| `B7-efik` | 2 | 1 | 0 | 1 |
| `B8-european-penetration-and-impact` | 2 | 1 | 0 | 1 |
| `B9-british-conquest-of-the-nigeria-area` | 3 | 1 | 1 | 1 |
| `C1-establishment-of-colonial-rule-up-to-1914` | 2 | 0 | 1 | 1 |
| `C2-amalgamation-of-1914` | 3 | 0 | 0 | 3 |
| `C3-colonial-administration-after-amalgamation` | 3 | 1 | 1 | 1 |
| `C4-colonial-economy` | 2 | 0 | 1 | 1 |
| `C5-social-development-under-colonial-rule` | 1 | 0 | 0 | 1 |
| `C6-constitutional-developments-nationalism-and-independence` | 3 | 1 | 1 | 1 |
| `D1-politics-of-first-republic-and-military-intervention` | 1 | 0 | 0 | 1 |
| `D10-transition-to-fourth-republic` | 2 | 0 | 2 | 0 |
| `D11-nigeria-in-international-organizations` | 3 | 0 | 1 | 2 |
| `D2-nigerian-civil-war` | 2 | 0 | 1 | 1 |
| `D3-gowon-regime` | 1 | 0 | 0 | 1 |
| `D4-murtala-obasanjo-regime` | 1 | 0 | 0 | 1 |
| `D5-second-republic` | 2 | 0 | 2 | 0 |
| `D6-buhari-regime` | 1 | 1 | 0 | 0 |
| `D7-babangida-regime` | 2 | 0 | 1 | 1 |
| `D8-interim-national-government` | 2 | 0 | 2 | 0 |
| `D9-abacha-regime` | 2 | 0 | 1 | 1 |
| `E1-islamic-reform-movements-and-state-building` | 1 | 0 | 0 | 1 |
| `E2-sierra-leone-liberia-and-missionary-activities` | 2 | 1 | 0 | 1 |
| `E3-egypt-under-mohammed-ali-and-khedive-ismail` | 3 | 1 | 0 | 2 |
| `F1-ethiopia-in-19th-century` | 2 | 0 | 1 | 1 |
| `F2-mfecane` | 2 | 0 | 1 | 1 |
| `F3-great-trek` | 2 | 1 | 0 | 1 |
| `G1-new-imperialism-and-european-occupation` | 2 | 1 | 0 | 1 |
| `G2-patterns-of-colonial-rule-in-africa` | 2 | 1 | 0 | 1 |
| `G3-politics-of-decolonization` | 3 | 1 | 1 | 1 |
| `G4-apartheid-in-south-africa` | 4 | 2 | 1 | 1 |
| `G5-problems-of-nation-building-in-africa` | 2 | 1 | 1 | 0 |

### IRK

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-revelation-of-the-glorious-quran` | 2 | 1 | 1 | 0 |
| `A1b-preservation-of-the-glorious-quran` | 2 | 0 | 1 | 1 |
| `A1c-importance-of-the-glorious-quran` | 1 | 0 | 1 | 0 |
| `A1d-divine-authenticity-of-the-glorious-quran` | 2 | 1 | 0 | 1 |
| `A2-tafsir` | 1 | 0 | 1 | 0 |
| `A3-introduction-to-tajwid` | 1 | 0 | 1 | 0 |
| `A4a-suwar-al-fatihah-to-al-maun` | 1 | 1 | 0 | 0 |
| `A4b-suwar-al-kawthar-to-an-nas` | 1 | 0 | 0 | 1 |
| `A5a-suwar-al-ala-to-al-alaq` | 1 | 1 | 0 | 0 |
| `A5b-suwar-al-qadr-to-selected-ayats` | 1 | 0 | 1 | 0 |
| `A6a-hadith-sciences-and-collections` | 3 | 0 | 2 | 1 |
| `A6b-selected-ahadith-of-an-nawawi` | 4 | 0 | 3 | 1 |
| `A7-moral-lessons-in-the-glorious-quran-and-hadith` | 1 | 0 | 1 | 0 |
| `B10a-ibadah-taharah-and-salah` | 2 | 2 | 0 | 0 |
| `B10b-zakah-sawm-hajj-and-jihad` | 2 | 0 | 1 | 1 |
| `B11-family-matters` | 3 | 0 | 3 | 0 |
| `B12-sources-and-schools-of-law` | 3 | 0 | 2 | 1 |
| `B13-islamic-economic-system` | 2 | 1 | 1 | 0 |
| `B14-islamic-political-system` | 2 | 2 | 0 | 0 |
| `B8-tawhid-shahadah-and-shirk` | 2 | 1 | 1 | 0 |
| `B9-articles-of-faith` | 2 | 0 | 1 | 1 |
| `C15-pre-islamic-arabia-jahiliyyah` | 1 | 1 | 0 | 0 |
| `C16-the-life-of-prophet-muhammad` | 2 | 1 | 0 | 1 |
| `C17-the-rightly-guided-caliphs` | 1 | 0 | 1 | 0 |
| `C18-early-contact-of-islam-with-africa` | 2 | 1 | 0 | 1 |
| `C19-the-impact-of-islam-in-west-africa` | 2 | 0 | 0 | 2 |
| `C20-contributions-of-islam-to-education` | 3 | 2 | 0 | 1 |

### Literature in English

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1a-types-of-drama` | 1 | 1 | 0 | 0 |
| `A1b-dramatic-techniques` | 1 | 1 | 0 | 0 |
| `A1c-interpretation-of-drama` | 1 | 0 | 1 | 0 |
| `A2a-types-of-prose` | 1 | 0 | 1 | 0 |
| `A2b-narrative-techniques-and-devices` | 1 | 1 | 0 | 0 |
| `A2c-textual-analysis-of-prose` | 2 | 1 | 1 | 0 |
| `A3a-types-of-poetry` | 2 | 1 | 1 | 0 |
| `A3b-poetic-devices` | 1 | 0 | 1 | 0 |
| `A3c-poetic-appreciation` | 1 | 0 | 1 | 0 |
| `A4-general-literary-terms-and-principles` | 1 | 0 | 1 | 0 |
| `A5-literary-appreciation` | 1 | 0 | 1 | 0 |
| `B1-marriage-of-anansewa` | 1 | 1 | 0 | 0 |
| `B2-antony-and-cleopatra` | 1 | 0 | 0 | 1 |
| `B3-so-the-path-does-not-die` | 2 | 0 | 1 | 1 |
| `B4-redemption-road` | 2 | 1 | 1 | 0 |
| `B5-path-of-lucas` | 2 | 0 | 2 | 0 |
| `B6-african-prescribed-poems` | 1 | 1 | 0 | 0 |
| `B7a-byron-and-chaucer` | 2 | 2 | 0 | 0 |
| `B7b-adcock-and-gibson` | 2 | 2 | 0 | 0 |

### Mathematics

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-number-bases-modular-arithmetic` | 3 | 0 | 3 | 0 |
| `A2-fractions-decimals-approximations-and-percentages` | 2 | 0 | 2 | 0 |
| `A3-indices-logarithms-and-surds` | 2 | 0 | 2 | 0 |
| `A4-sets` | 3 | 0 | 3 | 0 |
| `B1-polynomials` | 2 | 0 | 2 | 0 |
| `B2-variation` | 3 | 0 | 3 | 0 |
| `B3-inequalities` | 4 | 0 | 4 | 0 |
| `B4-progression` | 2 | 0 | 2 | 0 |
| `B5-binary-operations` | 3 | 0 | 3 | 0 |
| `B6-matrices-and-determinants` | 2 | 0 | 2 | 0 |
| `C1-euclidean-geometry` | 5 | 0 | 5 | 0 |
| `C2-mensuration` | 7 | 0 | 7 | 0 |
| `C3-loci` | 4 | 0 | 4 | 0 |
| `C4-coordinate-geometry` | 3 | 0 | 3 | 0 |
| `C5-trigonometry` | 4 | 0 | 4 | 0 |
| `D1-differentiation` | 2 | 0 | 2 | 0 |
| `D2-application-of-differentiation` | 3 | 0 | 3 | 0 |
| `D3-integration` | 2 | 0 | 2 | 0 |
| `E1-representation-of-data` | 3 | 0 | 3 | 0 |
| `E2-measures-of-location` | 1 | 0 | 1 | 0 |
| `E3-measures-of-dispersion` | 1 | 0 | 1 | 0 |
| `E4-permutation-and-combination` | 2 | 0 | 2 | 0 |
| `E5-probability` | 2 | 0 | 2 | 0 |

### Physics

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-measurements-and-units` | 1 | 0 | 1 | 0 |
| `A10-pressure` | 5 | 2 | 3 | 0 |
| `A11-liquids-at-rest` | 3 | 2 | 1 | 0 |
| `A12-temperature-and-measurement` | 3 | 0 | 3 | 0 |
| `A13-quantity-of-heat` | 2 | 1 | 1 | 0 |
| `A14-change-of-state` | 2 | 1 | 1 | 0 |
| `A15-thermal-expansion` | 4 | 2 | 2 | 0 |
| `A16-gas-laws` | 3 | 0 | 3 | 0 |
| `A17-vapours` | 3 | 2 | 1 | 0 |
| `A18-structure-of-matter-kinetic-theory` | 3 | 0 | 3 | 0 |
| `A19-heat-transfer` | 2 | 1 | 1 | 0 |
| `A20a-wave-production-and-classification` | 2 | 1 | 1 | 0 |
| `A20b-wave-characteristics-and-properties` | 5 | 0 | 5 | 0 |
| `A21-propagation-of-sound-waves` | 3 | 1 | 2 | 0 |
| `A22-characteristics-of-sound-waves` | 6 | 1 | 5 | 0 |
| `A23-light-energy` | 2 | 0 | 2 | 0 |
| `A24-reflection-of-light` | 4 | 0 | 4 | 0 |
| `A25a-refraction-at-plane-surfaces` | 4 | 0 | 4 | 0 |
| `A25b-refraction-glass-prism-lenses` | 2 | 0 | 2 | 0 |
| `A26-optical-instruments` | 3 | 1 | 2 | 0 |
| `A27-dispersion-and-electromagnetic-spectrum` | 2 | 0 | 2 | 0 |
| `A28-electrostatics` | 3 | 0 | 3 | 0 |
| `A29-capacitors` | 3 | 0 | 3 | 0 |
| `A2a-scalars-and-vectors` | 3 | 0 | 3 | 0 |
| `A2b-measurement-position-distance` | 3 | 0 | 3 | 0 |
| `A30-electric-cells` | 3 | 2 | 1 | 0 |
| `A31-current-electricity` | 5 | 0 | 5 | 0 |
| `A32-electrical-energy-and-power` | 2 | 2 | 0 | 0 |
| `A33-magnets-and-magnetic-fields` | 4 | 0 | 4 | 0 |
| `A34-force-on-current-carrying-conductor` | 3 | 2 | 1 | 0 |
| `A35a-electromagnetic-induction` | 5 | 3 | 2 | 0 |
| `A35b-inductance-and-eddy-currents` | 3 | 0 | 3 | 0 |
| `A36-simple-ac-circuits` | 5 | 0 | 5 | 0 |
| `A37-conduction-of-electricity-through-fluids` | 2 | 0 | 2 | 0 |
| `A38a-atomic-structure-and-emissions` | 3 | 0 | 3 | 0 |
| `A38b-radioactivity-and-modern-physics` | 3 | 0 | 3 | 0 |
| `A39-introductory-electronics` | 5 | 0 | 5 | 0 |
| `A3a-newtons-laws-and-types-of-motion` | 2 | 1 | 1 | 0 |
| `A3b-linear-and-projectile-motion` | 5 | 0 | 5 | 0 |
| `A3c-circular-motion-and-shm` | 3 | 0 | 3 | 0 |
| `A4-gravitational-field` | 3 | 0 | 3 | 0 |
| `A40-fibre-optics-and-lasers` | 2 | 1 | 1 | 0 |
| `A5-equilibrium-of-forces` | 5 | 0 | 5 | 0 |
| `A6-friction` | 4 | 0 | 4 | 0 |
| `A7a-work-energy-and-power` | 2 | 0 | 2 | 0 |
| `A7b-energy-sources-and-society` | 2 | 1 | 1 | 0 |
| `A8-simple-machines` | 5 | 0 | 5 | 0 |
| `A9-elasticity` | 2 | 0 | 2 | 0 |

### Use of English

| File | Total | AI | Code | Flag |
|---|---|---|---|---|
| `A1-types-of-passages` | 1 | 1 | 0 | 0 |
| `A5-approved-reading-text` | 1 | 0 | 1 | 0 |
| `B3a-clauses` | 1 | 0 | 1 | 0 |
| `B3b-sentence-patterns` | 1 | 0 | 1 | 0 |
| `B4b-verbs` | 1 | 0 | 1 | 0 |
| `B4c-adjectives-and-adverbs` | 1 | 0 | 1 | 0 |
| `B5a-mood-tense-and-aspect` | 1 | 0 | 1 | 0 |
| `B5c-degree-and-question-tags` | 2 | 2 | 0 | 0 |
| `B6b-punctuation-and-capitalisation` | 1 | 1 | 0 | 0 |
| `B7a-ordinary-and-figurative-usage` | 1 | 0 | 1 | 0 |
| `B7b-idiomatic-usage` | 1 | 1 | 0 | 0 |
| `B8-sentence-interpretation` | 1 | 0 | 1 | 0 |
| `C1a-vowels-monophthongs` | 3 | 1 | 2 | 0 |
| `C1b-diphthongs-and-triphthongs` | 1 | 0 | 1 | 0 |
| `C2a-consonants` | 4 | 0 | 4 | 0 |
| `C2b-consonant-clusters` | 2 | 0 | 2 | 0 |
| `C3-rhymes-and-homophones` | 2 | 0 | 2 | 0 |
| `C4-word-stress` | 3 | 0 | 3 | 0 |
| `C5-emphatic-stress` | 3 | 0 | 3 | 0 |

## Decision: Biology Section A (style test)

A style test redid two Section A images (earthworm, camouflage panels) in Gemini and compared them with the originals and with Section B (see the removed `STYLE-TEST.md`, commit history). The new versions matched Sections B to E better in style but lost detail (the earthworm in particular). **Decision: keep the original Biology Section A images.** The style-test files were deleted; Section A is not to be regenerated. The estimate for redoing all of it (about $8, range $5 to $12) is not needed.
