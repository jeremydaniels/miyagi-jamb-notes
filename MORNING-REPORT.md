# Morning report: Computer Studies

Computer Studies is planned, written, verified and illustrated, and everything is committed and pushed to `main` (one commit per notes file, one per fix, one per topic's images). Nothing stopped at a limit: notes cost $6.31 (safety limit $100) and images $4.74 (cap $15).

## Files written
- **42 notes files, about 134,000 words** (plan target 201,000; the notes came out at about two thirds of target, as in earlier subjects). 0 files flagged, 0 failed. All went through one Batch round plus a Batch repair round for 8 files.
- Plan changes you approved: number-base conversions and binary arithmetic kept in `B2b-data-representation-and-number-bases.md`; H1 merged into H2 as `H1-definition-and-branches-of-ai.md` (the definition first, then the branches). H3 and H4 keep their syllabus numbers; the tools did not need renumbering.
- Syllabus errors are taught correctly with a short "Note on the syllabus wording": Memory Base Register (usually Memory Buffer Register), XOR/NOR comparator (an XNOR in effect), Ubuntu as a browser, SPSS as a spreadsheet, Java in both the interpreted and compiled lists (explained as bytecode compiled then run by a virtual machine), "Programme" maintenance, "Terra bytes", Dreamview, Micromedia. Discontinued products are named as the syllabus names them, with hedged current equivalents.

## Verification: problems found and fixed
`verify_notes.py` (Batch, default thinking) checked all 42 files and reported **4 problems**. I confirmed each by hand and recomputed the numbers in Python:
1. **B2b binary addition (two examples):** the carry rows were shifted one column right of where the carries go. Results were right (11+13=24; 45+238=283, then 27 after dropping the 9th bit). I rebuilt both blocks from computed carries.
2. **C4 AutoCAD:** the notes said it stands for "Automatic Computer-Aided Design". The "Auto" comes from the maker, Autodesk. Fixed in two places, with a note that some textbooks give the other expansion.
3. **I4 Question 5:** the explanation named "System Administrator", which was not one of the options. Option B is now System Administrator.
4. **Mine, not the verifier's:** B2b Q3's explanation of the wrong options was vague ("if you miscount place values"). It now says option D (31) comes from reading 11101 as 11111.
Re-verification of B2b, C4 and I4 gave 0 problems; the other 39 files needed no change. I also ran every Python block in the notes (G1, G2, G4): all run, and the one stated output (`6`) is right; one fragment (a simple-interest line) is meant to be partial. All B2b conversions, additions, subtractions and multiplications and the practice answers were recomputed and are right. Not independently confirmed beyond the verifier: the other files' prose facts (the verifier found nothing).

## Images: placed and left
- 86 placeholders: 31 AI, 54 code-drawn, 1 map. **78 images placed, 8 placeholders left** (89 percent after the B1d fix below). Gallery: `subjects/computer-studies/images/GALLERY-computer-studies.md`.
- Pipeline as asked: Flash image generation in Batch, no text in the pictures, labels by `label.py`, captions under panels, flowcharts, tables, charts and circuits drawn in code, final drawing checks by Gemini Pro, up to 2 retries.
- **Left as placeholders (failed the Pro check twice):** `A2-02` three panels of computer types (stray numbers and a dollar sign in the picture); `E1-02` cold and warm boot comparison (panels stacked, not side by side); `C2-01` Excel window; `C2-02` spreadsheet with a small table; `C4-03` three-stage CorelDraw steps; `C5-02` PowerPoint ribbon; `C6-01` Dreamweaver split screen; `F6-02` email versus website. Five are software-screen mock-ups that code drawing cannot yet lay out cleanly.
- **Fixes I made during the run:**
  - Logic gates: I added standard gate symbols to `tools/codedraw/style.py` (`gate()`), and the code-drawing prompt now tells the model to use them. My first version drew the NOT gate without its inversion circle; the failed B1d symbols image exposed it. I fixed the helper and drew that image from a small script (`tools/specs/computer-studies/B1d-gate-symbols.py`, three separate panels). The Pro check passed it. The comparator image was not affected; I moved its output label off the wire.
  - Flowcharts: the template had no input/output parallelogram, so the G3 algorithm flowcharts showed "Read L, B" and "Print A" as plain text. I added a parallelogram shape and told the prompt to use standard symbols; G3-02 and G3-03 were re-rendered from their saved specs (no model calls) and pass the Pro check.
- Tool additions (no new dependencies; matplotlib and Pillow were already allowed): `make_images.py --pro-check` and `--cap`, `classify_subject.py`, a multi-topic plan entry (`Topic: A + B`), and fenced code blocks allowed for this subject in `notes_checks.py`.

## A teacher should check
- **Number bases and binary arithmetic (B2b):** beyond what the objectives name; kept at your request.
- **Syllabus oddities** and the notes' wording of them: `B1c` (MBR), `B1d` (comparator as XNOR), `F3` (browser list), `C2` (SPSS), `G5` (Java), plus the long "Transcription notes" at the end of `syllabus.md`.
- **Fast-changing content:** Word, Excel, Access, CorelDraw, PowerPoint and Dreamweaver features and menus (C1 to C6), AI branches and applications (H1, H3, H4), and cyber threats (I2, I3). These are hedged ("at the time of writing"), but a teacher should skim them for product names that may be dated, and the Nigerian telecom and payment examples (F1, F2, F3).
- **Generations of computers (A2):** books give different year ranges; the notes give the common ones and say so.
- **Code in G1 to G5:** Python was run; BASIC, C and Java snippets are marked as shown for recognition (traced by hand, not run).
- **Images:** screen and device pictures (B1b, F7 cables and connectors, E2 maintenance, E3 room layout) were checked by the Pro check and by me on a sample (comparator, gates, flowcharts, topologies, loom, RAM, connectors, Access table); one RAM chip carries a decorative logo. A teacher should glance at the hardware pictures for realism, especially connector pin counts.

## Cost (Gemini, list price with the assumed 50 percent Batch discount; Claude usage not included)
| Item | Cost |
|---|---|
| Setup (transcription $0.252, planning $0.110) | $0.36 |
| Writing (42 files, 2 batch rounds) | $3.60 |
| Verification (42 files, plus 3 re-checks) | $2.34 |
| **Notes total** | **$6.31** (est. with cache and Batch discounts: $5.75) |
| Images: Flash generation $1.06, Pro regeneration $0.57, code drawing $1.40, Pro checks $1.69, classification $0.02 | $4.74 |
| **Total** | **$11.05** |
The estimate in `subjects/computer-studies/ESTIMATE.md` was $6.91 for notes (actual $6.31) and $3.93 for images (actual $4.74).

---

# Previous report (overnight run: Accounting, Commerce, Geography, Agricultural Science, History)

# Morning report: Run 1 (Accounting, Commerce, Geography, Agricultural Science, History)

All five subjects are written, verified and committed to `main` (one commit per notes file, one per fix). No file is flagged or missing, and no subject came near the $100 safety limit. No images were made (placeholders only).

**Read this first (4 things):**
1. **History has no open verifier findings.** 5 findings that the web could not settle were closed by editor decision (standard textbook position); the rest were confirmed against a source before I changed anything. The sources are in `HISTORY-VERIFICATION-LOG.md`.
2. **I fixed a bug in `tools/notes_checks.py`.** The coverage check read only the first word of an objective id, so every Agricultural Science objective without a number failed. 32 of 45 files were flagged on the first run. I fixed the check and re-checked the saved attempts locally (no new API calls), and all 32 passed. The failed retries still cost money (see cost).
3. **Word counts are well below Gemini's plan targets** (about 0.6 to 0.8 of target). That fits earlier subjects. Nothing was padded and nothing was cut.
4. **Cost** was about **$38.04** at list price (**$34.60** with the assumed discounts). Details at the bottom.

---

## Files written

| Subject | Files | Words | Flagged | Notes |
|---|---|---|---|---|
| Accounting (Principles of Accounts) | 18 of 18 | about 73,800 | 0 | all passed the structure checks first time |
| Commerce | 18 of 18 | about 73,300 | 0 | all passed first time |
| Geography | 24 of 24 | about 100,400 | 0 | all passed first time |
| Agricultural Science | 45 of 45 | about 184,200 | 0 (32 flagged by the checker bug, all recovered) | 13 passed first time, 32 recovered locally after the fix |
| History | 42 of 42 | about 163,800 | 0 | 41 passed first time, 1 needed a retry |
| **Total** | **147 of 147** | **about 595,500** | **0** | |

The transcription notes now say the PDFs are official IBASS extracts and no longer say "not official". The source's own typos and errors are still flagged. The rules files have the length-guide rule, the "Note" convention and (History) the neutrality rules for D3 to D10.

## Verification and fixes

Every file was verified. Each reported problem was checked before editing: numbers were recomputed in Python, wording and facts were judged by hand, and History facts were confirmed on the web first. Files whose fix changed a number or a fact were re-verified.

| Subject | Problems reported (first pass) | Confirmed and fixed | After re-verification |
|---|---|---|---|
| Accounting | 6 | 6 | 0 left (2 new wording points on A9 and A12 fixed on the second pass) |
| Commerce | 5 | 5 | 0 left |
| Geography | 12 | 12 | 0 left in the re-verified files |
| Agricultural Science | 27 | 27 | 0 left (second pass found 5 more, all closed) |
| History | 24 (22 distinct issues) | 22 issues closed (17 on web sources, 5 by editor decision) | 0 open |

**Main problems found and fixed**
- **Accounting:** four practice-question explanations that named the wrong mistake for a wrong option (A6 Q1, A9 Q2, A15 Q2); a goodwill write-off tip that said "new partners" instead of "all partners" (A15); a ledger label (A13); a fire-damage example that did not have enough information to solve (A9); a table row that called discount received an expense (A12).
- **Commerce:** commerce placed in the "secondary and tertiary" stage (now tertiary); manufacturing called "direct production"; a communication diagram that put decoding before the receiver; lateral merger and amalgamation wrongly listed as synonyms of conglomerate.
- **Geography:** a wrong explanation of a scale-exaggeration answer (A3); earth circumference figures that did not match the diameters (B1, now 40,075 km and 40,008 km); Lake Bosumtwi called volcanic (now impact crater); Great Lakes as tarns; "U-shaped" river valleys; Chad listed in ECOWAS; Igbo settlements as nucleated (hedged); pH scale 0 to 14; a confusing question stem (B9).
- **Agricultural Science:** yam listed as a dicot; cassava roots listed as plantable; Calgon called flocculating; strip cropping called mechanical; Sussex fowl as a broiler; guano for poultry manure; "oxen" for bulls; demand versus quantity demanded (D2); the farmer-to-agent ratio written the wrong way round (D6); Gunter's chain "exactly 20.12 m"; seed rate versus total seed requirement (B7); cocoa as a short-day plant; sleeping sickness versus nagana; praying mantis spelling.
- **History:** see `HISTORY-VERIFICATION-LOG.md` for each item and its source. Examples: nine (not eleven) states created in 1991; petrol price under the ING (70 kobo to 5 naira, not 3.25); Kabbah restored in March 1998; Udoji commission set up in 1972; Northern delegates (not Southern politicians) were jeered in Lagos in 1953; the 1917 bank was the Colonial Bank; the UAC merger partners; the Sikasso siege failed; the OIC's old name.

**Syllabus errors handled as you asked** (teach what JAMB expects, then a "Note" with the correct or current position):
- Accounting A3 (IASB is not Nigerian) and A7 (LIFO not allowed under IFRS) have Notes. Commerce A11 and A14 have Notes on the NGX and the FCCPC. Geography B2 has a Note that the lithosphere is the fourth sphere. All time-sensitive points say "at the time of writing".

## History facts confirmed or left for you

The full table with sources is in `HISTORY-VERIFICATION-LOG.md`. Summary:
- **Confirmed and fixed:** 17 verifier findings (first pass), plus 5 on the second pass and 3 on the third pass, each against Britannica, Wikipedia, a university or journal source, a national library record or established Nigerian press. Sources are named in the log.
- **New findings from the first follow-up re-verification: all closed (second follow-up run).** Re-verification of the changed files then reported 0 problems.
  1. **C5 image:** now describes the Lagos to Kano line and the colonial eastern line (Port Harcourt, Enugu, Kafanchan, Kaduna, with a branch to Jos); the Maiduguri extension is noted as completed after independence (early 1960s). Editor decision.
  2. **B2 Question 4:** the explanation now matches the main text (Mai Ibrahim executed; his heir Ali killed in battle). Editor decision.
  3. **C4 railway:** now starts in 1896 (Wikipedia, AJOL article). The "reached Abeokuta in 1898" detail was not added because no source gave it.
  4. **C4 African Continental Bank:** sources conflict (1944, 1948, 1949), so the text says "Azikiwe's bank, which became the African Continental Bank (ACB) in the 1940s".
- **Spot-checked, no change needed:** about a dozen dates and names (Usman dan Fodio's death in 1817, Abacha's death on 8 June 1998, 29 May 1999, Adwa on 1 March 1896, Muhammad Ali 1805, Ismail 1863 and 1879, the 1882 occupation, the Civil War dates, Lagos 1851 and 1861, Gowon's dates, Nigeria joining the OIC in 1986, the 1 October 1963 constitution).
- **Closed by editor decision (follow-up run), previously open:** all items below were changed to the standard textbook position and logged in `HISTORY-VERIFICATION-LOG.md`:
  1. **A4, gold:** removed as an export of the Nigeria area (a note says gold from goldfields further west passed through Hausaland in transit). Main exports: slaves, leather goods, kola, ivory, cloth.
  2. **A4 Q6, Oyo horses:** the explanation and question stem now say Borno got horses through the Trans-Saharan trade and Oyo through trade with the north (Hausaland and Borno).
  3. **B2, Ngazargamu:** now says the court settled there under Mai Ali Gaji in the late 15th century, and that sources give different exact dates.
  4. **C4, gold dust:** removed; cowries, manillas, brass rods and cloth strips remain.
  5. **C5, railway map:** the "A" shape wording is gone; the image now describes the Lagos to Kano and Port Harcourt to Maiduguri lines.
  6. **E1, Umar Tall's son:** now written "Ahmadu Tall (Ahmadu Seku)" throughout, including the exam tip and Question 2.
  7. **Agricultural Science A3, acha:** moved out of the Sahel crop list; a note says it is a northern Nigeria crop, especially on the Jos Plateau.

## Tool changes this run (all committed)
- `tools/notes_checks.py`: the coverage-map parser now accepts multi-word ids (needed for syllabi whose objectives have no numbers).
- No other tool, price or setting was changed. No dependency was added.

## Cost (Gemini, USD)

| Subject | Setup | Writing | Verification | Total (list) | Total (est) |
|---|---|---|---|---|---|
| Accounting | 0.16 | 4.30 | 2.00 | 6.46 | 5.09 |
| Commerce | 0.21 | 1.66 | 0.74 | 2.60 | 2.48 |
| Geography | 0.26 | 2.69 | 1.99 | 4.94 | 4.57 |
| Agricultural Science | 0.24 | 11.87 | 3.63 | 15.75 | 14.65 |
| History | 0.30 | 3.69 | 4.30 | 8.29 | 7.81 |
| **Total** | **1.17** | **24.21** | **12.66** | **38.04** | **34.60** |

- **Against the estimate ($34.70 central, $68.23 high):** the list total is $38.04, about 10% above the central figure. Agricultural Science is $4.58 above its estimate because 32 files were written, rejected by the checker bug and retried (about $5 to $6 of wasted retries). History writing was cheaper than estimated (no code tool) and its verification was dearer.
- The list figure already includes the assumed 50% Batch discount from `tools/gemini_pricing.json` (unverified). Not included: web searches and Claude usage.

## Anything a teacher should double-check
- **History D3 to D10 (regimes):** written from well-established facts only, with no judgments, as you asked. A History teacher should skim D3 to D10 and D11 (Nigeria in international organisations) for balance and for any date they know to be disputed.
- **History:** the five items closed by editor decision (they follow the standard textbook position, not a web source), the pre-colonial titles and terms in A3 and the Ekumeku dates (the syllabus prints 1898 to 1911; some sources differ). Shaka's birth year ("about 1787") and Vegkop (1836) were not checked by web search.
- **Accounting:** worked examples are checked by Gemini's code tool and again by the verifier. A tutor should skim A6, A9, A13 and A15 for layout and for the Dr/Cr presentation.
- **Commerce and Accounting, Nigerian institutions and laws** (NGX, FCCPC, FRCN, IPPIS, TSA): hedged as "at the time of writing"; confirm current names before release.
- **Geography:** the Part I practical topics (maps, scale, cross profiles) are explained in words and `[IMAGE: ...]` placeholders. A teacher should check the map-reading exercises against a real topographical sheet, because the examples are made up.
- **Agricultural Science:** figures such as seed rates, spacing, fertilizer rates and yields are examples and are marked that way. Classification of cattle breeds (for example Red Bororo) varies between textbooks and is hedged in C1.
- **Search-result note:** one web result contained an embedded instruction aimed at AI readers. I did not follow it.
