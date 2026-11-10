# Biology images report (Sections B to E)

Run finished. **353 of 451 placeholders now have an image** (78%); 98 placeholders are still in the notes. Image spend was **$37.65** of the $40 cap (the cap was not reached). Gallery for your phone: `subjects/biology/images/GALLERY-biology.md`.

## Images placed per section

| Section | Placeholders | Placed | Still placeholders |
|---|---|---|---|
| B | 282 | 220 | 62 |
| C | 99 | 80 | 19 |
| D | 46 | 37 | 9 |
| E | 24 | 16 | 8 |
| **Total** | **451** | **353** | **98** |

Of the 353 placed: **272 AI images** (with labels where the placeholder had a label list) and **81 code-drawn** (matplotlib). Each notes file has its own commit with its images, prompts, label coordinates and, for code images, the drawing script (`tools/specs/biology/`).

## Decisions carried out

- `CLAUDE.md` now has the Gemini-only image rules and the decisions in `IMAGES-PLAN.md`.
- A2c: "parotid" corrected to "parotoid" in the notes text and in the toad-frog image label (patched with Pillow, same font and style).
- Pilot problems redone: tadpole (outside only, no organs), heart (left ventricle wall thickest: passed on the third try with Pro), nephron (wide afferent and narrow efferent arterioles; the automatic check kept objecting to how the capsule joins the tubule although the picture looks right, so I looked at it and accepted it myself), phototropism (redrawn in code: mica sheet vertical on the shaded side, sleeve experiment bending).
- **Batch test:** 15 images in 127 seconds at $0.034 each against $0.069 standard; quality was the same model's output, so Batch was used for the rest (all first generations and retries). The Batch discount is assumed to be half price; it is not verified against Google's billing.
- Models: `gemini-3.1-flash-image` for first tries, `gemini-3-pro-image` for the four pilot problems and for retries. Gemini Flash vision did all checks and found all label positions; Gemini never wrote label text (all text comes from the placeholders, drawn by `label.py`).

## Failed or flagged (placeholder left in the notes)

**98 placeholders:** 31 AI pictures that failed the structure check after two generations, 27 AI pictures whose labels could not be placed reliably after three tries, and 40 code-drawn images that failed the layout check after three attempts. Reasons in the table.

| Notes file | Image | Kind | Why it failed |
|---|---|---|---|
| `B1-internal-structure` | `B1-11-rabbit-digestive-system-dissection` | raw check | The pancreatic duct is not visible or distinguishable within or leading from the diffuse pancreas. |
| `B1-internal-structure` | `B1-12-mammalian-urinary-system` | raw check | In ventral view, the vena cava is anatomically on the anatomical right and aorta on the anatomical left, but here their lateral positions are reversed; The right kidney i |
| `B1-internal-structure` | `B1-14-female-rabbit-reproductive-system` | raw check | Urethra and bladder lie alongside the reproductive tract rather than connecting properly into a vestibule or urinogenital sinus ventral to the vagina; The vagina and vest |
| `B2b-plant-nutrition` | `B2b-03-photosynthesis-stages-schematic` | code image | The green ATP arrow passes directly through the 'RuBP (5C)' label box; The orange cycle arrow passes directly through the 'using ATP' label box; A blue line cuts through  |
| `B2b-plant-nutrition` | `B2b-09-starch-test-leaf-steps` | raw check | Panel 6 bottle contains text Iodine |
| `B2c-food-substances-and-food-tests` | `B2c-07-kwashiorkor-marasmus` | labels | flaky skin patches; marasmus |
| `B2c-food-substances-and-food-tests` | `B2c-14-lipid-food-tests-results` | labels | cloudy white emulsion (fat present); clear (no fat) |
| `B2d-mammalian-teeth` | `B2d-02-types-human-teeth` | labels | one root; canine; one long root; premolar; one or two roots; molar |
| `B2e-alimentary-canal-and-digestion` | `B2e-06-hepatobiliary-pancreatic-ducts` | raw check | The image contains prominent text labels, captions, and leader lines throughout instead of being an unlabelled illustration.; The anatomical orientation is reversed or mi |
| `B2e-alimentary-canal-and-digestion` | `B2e-09-pepsin-ph-experiment-tubes` | labels | clear (protein digested); B: neutral; cloudy; C: alkaline; cloudy; D: boiled pepsin; cloudy (control); water bath at 37 °C; thermometer |
| `B2e-alimentary-canal-and-digestion` | `B2e-11-nutrient-absorption-pathway` | code image | The label 'hepatic portal vein' overlaps the central lacteal and the capillary lines; Missing arrow showing glucose and amino acids entering the blood capillaries (only a |
| `B3a-transport-in-animals` | `B3a-02-agar-cube-diffusion-experiment` | labels | 3 cm cube |
| `B3a-transport-in-animals` | `B3a-03-double-circulatory-system-schematic` | code image | Text inside lung boxes (left lung, right lung) and the HEART label have very low contrast and are hard to read; The lung boxes are labelled left lung on viewer's left and |
| `B3a-transport-in-animals` | `B3a-04-single-versus-double-circulation` | code image | In the mammal double circulation diagram, the blue pathway is incorrectly connected: blood from the body should enter the right atrium and then flow from the right ventri |
| `B3a-transport-in-animals` | `B3a-11-systemic-blood-circulation-schematic` | code image | Leader line from pulmonary artery label crosses directly through the lungs label in the right lung box. |
| `B3a-transport-in-animals` | `B3a-12-hepatic-portal-circulation-schematic` | code image | Most villi capillaries inside the small intestine are disconnected and do not join into the hepatic portal vein; Left renal vein is missing a directional flow arrow |
| `B3a-transport-in-animals` | `B3a-13-centrifuged-blood-composition-chart` | code image | In the pie chart, colors and labels are reversed: the yellow (larger) slice is labeled 'about 45% cells' instead of plasma, and the dark red slice is labeled 'about 55% p |
| `B3a-transport-in-animals` | `B3a-17-cockroach-open-circulatory-system` | labels | direction of flow |
| `B3b-transport-in-plants` | `B3b-13-bubble-potometer-apparatus` | raw check | The water reservoir is positioned upside down below the tap, so water cannot flow by gravity to reset the bubble in the tube. |
| `B3b-transport-in-plants` | `B3b-15-root-pressure-manometer-experiment` | raw check | The cut upper shoot of the plant is nonsensically floating in mid-air above the stump instead of being removed |
| `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-02-amoeba-earthworm-respiration` | labels | carbon dioxide out; oxygen in; dorsal pore; cuticle |
| `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-07-avian-respiratory-system-air` | raw check | The airflow arrows show the incorrect direction and sequence: they indicate air traveling from anterior sacs through the lungs to posterior sacs and out behind the bird,  |
| `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-14-alveolus-gas-exchange-capillary` | labels | carbon dioxide diffuses into alveolus; oxygen diffuses into blood |
| `B4b-cellular-respiration` | `B4b-03-krebs-citric-acid-cycle` | code image | Acetyl CoA is not shown joining oxaloacetic acid to form citric acid; oxaloacetic acid (4C) and citric acid (6C) are floating outside the cycle without connecting arrows  |
| `B4b-cellular-respiration` | `B4b-05-aerobic-cellular-respiration-overview` | code image | The purple dashed line passes directly through the upper carbon dioxide out label; The dashed orange inner mitochondrial line passes through the MITOCHONDRION label at th |
| `B4b-cellular-respiration` | `B4b-06-pyruvic-acid-fate-branching` | code image | Redundant text in the bottom boxes: both the descriptive outcomes and the requested labels are displayed together (e.g. carbon dioxide and water and many ATP below aerobi |
| `B4b-cellular-respiration` | `B4b-08-plant-respiration-carbon-dioxide` | raw check | The first flask lacks an inlet tube for incoming atmospheric air to bubble through the potassium hydroxide solution.; The bell jar is connected via a single three-way T-j |
| `B4b-cellular-respiration` | `B4b-11-simple-respirometer-germinating-seeds` | raw check | The control tube has two capillary tubes inserted into its bung instead of one; The horizontal measuring scale is missing |
| `B5-excretion` | `B5-01-comparative-invertebrate-excretory-structures` | raw check | In panel 3, the nephrostome (ciliated funnel) is located entirely within the same segment rather than passing through the anterior septum from the preceding coelomic segm |
| `B5-excretion` | `B5-03-earthworm-nephridium-excretory-structure` | raw check | The intestine is missing from the cut-open earthworm segment. |
| `B5-excretion` | `B5-09-urine-formation-schematic-flowchart` | code image | The arrow at the bottom of the collecting duct points upward into the tubule rather than downward toward 'urine to pelvis'. |
| `B5-excretion` | `B5-11-inhaled-exhaled-air-apparatus` | raw check | The test tubes lack bungs or stoppers, meaning air cannot be properly drawn through or bubbled via the delivery tubes; In the inhaled tube (left), the tube connecting to  |
| `B6a-support-and-movement-in-plants` | `B6a-11-nyctinastic-plant-movements` | raw check | Bauhinia leaf at night is shown open rather than folded together along the midrib; Flamboyant leaflets at night are still spread rather than folded together in pairs |
| `B6a-support-and-movement-in-plants` | `B6a-13-root-growth-marking-experiment` | raw check | In the right diagram, the ink marks near the seed at the top are close together, but the marks are elongated throughout the middle and bottom rather than demonstrating el |
| `B6a-support-and-movement-in-plants` | `B6a-17-auxin-concentration-response-curve` | code image | The label 'stimulation (+)' overlaps with the 'optimum for root' label box, cutting off and obscuring text. |
| `B6a-support-and-movement-in-plants` | `B6a-18-coleoptile-tropism-experiments` | raw check | In the top row, the coleoptiles bend to the left, away from the light source coming from the right, instead of bending towards the light.; In the bottom row, the agar blo |
| `B6b-support-and-movement-in-animals` | `B6b-05-human-vertebral-column` | raw check | Rib stubs on the thoracic vertebrae are missing, so the required part rib cannot be labelled |
| `B6b-support-and-movement-in-animals` | `B6b-06-cervical-vertebrae-comparison` | raw check | Image contains duplicated rows of three vertebrae instead of a single side-by-side set; Axis in the middle lacks visible transverse foramina vertebrarterial canals |
| `B6b-support-and-movement-in-animals` | `B6b-08-human-rib-cage` | raw check | The rib count is incorrect: only 10 pairs of ribs are depicted, with only a single floating rib pair at the bottom instead of the required 12 pairs of ribs with two float |
| `B6b-support-and-movement-in-animals` | `B6b-09-pectoral-pelvic-girdles` | raw check | The left diagram shows a left upper limb and pectoral girdle seen from the front, or a right limb from behind, rather than the requested right forelimb from the front.; T |
| `B7b-reproduction-in-flowering-plants` | `B7b-10-heterostyly-primrose-flowers` | labels | thrum-eyed flower (short style); ovary; titles: pin-eyed flower (long style) |
| `B7b-reproduction-in-flowering-plants` | `B7b-12-fruit-placentation-types` | raw check | The image contains printed numbers (1, 4, 5, 6) which violate the rule that illustrations must contain no text or numbers |
| `B7b-reproduction-in-flowering-plants` | `B7b-13-fleshy-fruit-sections-comparison` | raw check | Tomato is cut longitudinally instead of across, and seeds are attached around the perimeter rather than on a central placenta; Coconut lacks the thick fibrous husk layer  |
| `B7b-reproduction-in-flowering-plants` | `B7b-16-fruit-seed-dispersal-mechanisms` | raw check | The image contains text labels naming each fruit and seed, violating the rule that it must contain no text or labels. |
| `B7c-reproduction-in-mammals` | `B7c-07-foetus-pregnant-uterus` | labels | vagina; inset labels: mother's blood space |
| `B7c-reproduction-in-mammals` | `B7c-09-contraceptive-methods-overview` | labels | oviduct cut and tied; box titles: natural; barrier; calendar (rhythm method); thermometer (temperature method); male condom; hormonal; injectable; diaphragm; intrauterine |
| `B8-growth` | `B8-04-seed-germination-mass-change` | code image | The green dry mass curve passes directly through the dry mass label box at the top right, overlapping the label. |
| `B8-growth` | `B8-06-maize-grain-anatomy` | raw check | In the longitudinal section, the embryo anatomy is fundamentally incorrect and confused: the scutellum is drawn as an internal oval rather than bordering the endosperm, a |
| `B8-growth` | `B8-12-seed-food-mobilisation-flowchart` | code image | The arrows are mislabeled: the arrow going toward the aleurone layer is labeled 'soluble sugars and amino acids' instead of 'gibberellin'; The arrows delivering nutrients |
| `B9a-nervous-coordination` | `B9a-02-motor-neurone-structure` | labels | node of Ranvier; axon; direction of impulse; synaptic knobs; Schwann cell; axon terminals |
| `B9a-nervous-coordination` | `B9a-03-three-types-neurones` | labels | direction of impulse; titles: sensory neurone; motor neurone |
| `B9a-nervous-coordination` | `B9a-10-synapse-structure` | labels | calcium ions enter |
| `B9a-nervous-coordination` | `B9a-14-conditioned-reflex-pavlov-experiment` | labels | bell + food |
| `B9b-sense-organs` | `B9b-14-inner-ear-balance-organs` | labels | ampulla; utriculus |
| `B9c-hormonal-control` | `B9c-02-negative-feedback-flow` | code image | The legend box overlaps the left side of the brain illustration; Hypothalamus is shown as a separate rectangular box below the brain rather than being highlighted within  |
| `B9c-hormonal-control` | `B9c-05-thyroid-gland-anatomy-goitre` | labels | left lobe; right lobe; thyroid gland; isthmus |
| `B9c-hormonal-control` | `B9c-14-fruit-ripening-ethylene` | labels | ethylene gas |
| `B9d-homeostasis` | `B9d-01-homeostasis-negative-feedback` | code image | The horizontal band is centrally positioned rather than at the top |
| `B9d-homeostasis` | `B9d-03-thermoregulation-line-graph-comparison` | code image | The legend box overlaps and obscures the callout box for endotherm / constant body temperature near the top |
| `B9d-homeostasis` | `B9d-04-skin-section-temperature-regulation` | raw check | No shunt vessel (arteriovenous anastomosis) connecting the arteriole to the venule is shown. |
| `B9d-homeostasis` | `B9d-07-osmoregulation-adh-feedback-flowchart` | code image | Both beakers are drawn the same size rather than a small beaker and a large beaker; The return arrow from the lower beaker overlaps the upper border of its card container |
| `B9d-homeostasis` | `B9d-10-blood-glucose-regulation-flowchart` | code image | The flow line connecting the insulin dots to cells take up glucose intersects and crosses the arrow line descending from the liver and muscle to normal blood glucose. |
| `C1-factors-affecting-distribution` | `C1-03-nigeria-rainfall-vegetation-map` | code image | the code failed: es=vertices)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/matplotlib/_api/__init__.py", line 259, i |
| `C2-symbiotic-interactions-and-energy-flow` | `C2-07-savanna-food-web-network` | code image | The label 'secondary consumers' is cut off and overlapped by the praying mantis box, displaying as 'secondary consun'; The label 'primary consumers' is cut off and overla |
| `C2-symbiotic-interactions-and-energy-flow` | `C2-08-ecological-pyramids-comparison-charts` | code image | In the pyramid of energy, the vertical bar lines run directly through the text labels 10 kJ and 100 kJ, causing text to overlap lines |
| `C2-symbiotic-interactions-and-energy-flow` | `C2-10-carbon-cycle-schematic` | code image | Text for fossil fuels (coal, oil, gas) is white on a pale yellow background and barely readable; Atmospheric reservoir is drawn as a rounded box rather than a cloud; No d |
| `C2-symbiotic-interactions-and-energy-flow` | `C2-13-nitrogen-cycle-flow` | code image | The lightning bolt points into the goat box instead of forming nitric acid in rain that reaches the soil; Rain lines labelled 'nitric acid in rain' emerge from underneath |
| `C2-symbiotic-interactions-and-energy-flow` | `C2-14-root-nodule-anatomy` | labels | nodule cortex; infected cells with Rhizobium; N2 from soil air; sugars from plant to bacteria |
| `C3-natural-habitats` | `C3-04-stream-ecosystem-profile-cross` | raw check | The fish is facing downstream with the water current arrows instead of upstream against the current. |
| `C4-nigerian-biomes` | `C4-01-map-nigerian-vegetation-belts` | code image | the code failed: on3.13/site-packages/matplotlib/patches.py", line 1262, in __init__
    self.set_xy(xy)
    ~~~~~~~~~~~^^^^
  File "/usr/local/lib/python3.13/site-packag |
| `C4-nigerian-biomes` | `C4-08-map-nigeria-state-biomes` | code image | the code failed: import not allowed: shapely.geometry |
| `C5-ecology-of-populations` | `C5-01-sigmoid-j-shaped-population` | code image | Vertical axis line cuts through the label number of individuals (population size) on both graphs; On the right graph, the green peak line overlaps the population crash la |
| `C5-ecology-of-populations` | `C5-02-demographic-population-age-pyramids` | code image | In the stable and contracting pyramids, the age group labels are plotted directly on top of the blue male bars instead of being placed in a central column between the bar |
| `C5-ecology-of-populations` | `C5-07-hydrosere-pond-succession-sequence` | labels | time |
| `C6-soil` | `C6-03-soil-texture-particle-comparison` | labels | Sandy soil; Loamy soil; Clayey soil; Soil crumb; Clay particles |
| `C6-soil` | `C6-04-soil-structure-types` | labels | Platy; Blocky |
| `C7a-diseases` | `C7a-01-map-africa-meningitis-belt` | code image | The label 'Dry season: about December to June' overlaps the bottom border of the inset box; The subtitle 'Sketch map: zones are approximate' overlaps the continental outl |
| `C7a-diseases` | `C7a-02-anopheles-mosquito-life-cycle` | raw check | The larva is drawn floating obliquely down in the water rather than lying flat and parallel just below the water surface as characteristic of Anopheles; The adult mosquit |
| `C7a-diseases` | `C7a-08-housefly-life-cycle-disease` | raw check | Text label vomit is present in the central illustration |
| `C7b-drug-abuse` | `C7b-05-drug-rehabilitation-flow` | code image | Arrowheads are missing on connecting lines between steps 7 and 1, 1 and 2, 3 and 4, and 4 and 5 |
| `C7c-pollution-and-sanitation` | `C7c-03-ozone-layer-depletion-schematic` | raw check | Text present in the inset: chemical symbols Cl, O3, and O2 are written on the atoms/molecules; The ozone layer does not show a thinner gap or ozone hole on the right; the |
| `D1-variation-in-population` | `D1-12-abo-blood-transfusion-compatibility` | code image | The curved arrow above circle O overlaps the title ABO Blood Group Compatibility; The legend label arrow = can donate to is cut off and overlaps the AB circle; The curved |
| `D2a-heredity-principles` | `D2a-02-human-male-karyotype` | code image | The label 'sex chromosomes' overlaps and partially obscures the number '17' below chromosome pair 17 |
| `D2a-heredity-principles` | `D2a-04-dna-ladder-helix` | code image | The double helix on the right does not match the molecule on the left, having 6 rungs with a different base sequence instead of 7 rungs matching the ladder.; A stray vert |
| `D2a-heredity-principles` | `D2a-06-monohybrid-gene-transmission` | code image | Fertilisation arrows from eggs to zygotes 1 and 2 are swapped: eggs with a incorrectly connects to zygote AA, while eggs with A incorrectly connects to zygote Aa |
| `D2a-heredity-principles` | `D2a-13-haemophilia-sex-linked-pedigree` | code image | Characters overlap in the genotype labels X^H X^H and X^H X^h below the daughter icons; Blue fertilization lines cut straight through the chromosome icons of all four chi |
| `D2b-applications-of-heredity` | `D2b-01-plant-breeding-programme-flowchart` | code image | Box 5 is missing check marks on the selected plants |
| `D2b-applications-of-heredity` | `D2b-05-sickle-cell-trait-counselling` | code image | The AS badge box for the mother overlaps and partially covers the mother stick figure; The SS sickle-cell anaemia (25%) label box overlaps the bottom border line of the P |
| `D3-biotechnology` | `D3-07-bread-making-yeast-fermentation` | raw check | Panel 2 inset includes stray text CO2 |
| `D3-biotechnology` | `D3-08-biogas-digester-cross-section` | labels | gas pipe and valve |
| `E1-theories-of-evolution` | `E1-02-redi-spontaneous-generation-experiment` | labels | sealed jar: no maggots; gauze-covered jar: no maggots on meat |
| `E1-theories-of-evolution` | `E1-03-pasteur-swan-neck-flask` | labels | Pasteur (about 1860) |
| `E2-evidence-of-evolution` | `E2-04-horse-evolution-stages-foot` | labels | increase in size; forest to grassland |
| `E2-evidence-of-evolution` | `E2-05-homologous-pentadactyl-forelimbs-comparison` | raw check | The bird wing anatomy is biologically incorrect, showing five distinct elongated digits instead of fused carpometacarpus and reduced digits.; The bat wing digits are draw |
| `E2-evidence-of-evolution` | `E2-06-analogous-insect-bird-wings` | labels | analogous structures (convergent evolution) |
| `E2-evidence-of-evolution` | `E2-10-biogeography-lungfish-world-map` | code image | The arrow between South America and the Galápagos finch points eastward toward South America instead of pointing from South America to the Galápagos Islands; In Australia |
| `E2-evidence-of-evolution` | `E2-11-plant-phylogenetic-evolutionary-tree` | code image | A long green line from the fern cuts straight up across several branches and labels all the way to the top of the diagram; The label 'angiosperms (flowering plants)' is m |
| `E2-evidence-of-evolution` | `E2-14-chromosome-structural-mutations` | code image | The centromere label box overlaps band A on the first normal chromosome, partially obscuring the band and letter.; In the translocation diagram, the second chromosome is  |

## Cost

| Item | Cost |
|---|---|
| Image generation, this run (flash and pro, standard and batch) | $22.74 |
| Writing the code-drawn images (Gemini) | $7.50 |
| Checking code-drawn images | $1.39 |
| Finding label positions | $3.26 |
| Checking labelled images | $2.00 |
| Checking unlabelled images | $0.75 |
| **Total this run** | **$37.65** |
| Pilot (before this run) | $1.51 |

Per placed image the run cost about **$0.107** (including all the failures and retries). Prices are unverified list prices; Batch is assumed to be half price.

## Spot-check by me

I looked at about 20 finished images across B, C, D and E (labelled anatomy, experiment apparatus, graphs, flowcharts) and at every pilot-problem image. Labels were on the right parts in nearly all of them. Faults I saw: a few leader lines cross each other (bladderwort trap, rib and vertebra comparisons); region labels such as cortex and medulla end in white space (acceptable for regions); small text in some code-drawn flowcharts (E1 natural selection) is readable but tiny. I accepted two code images myself that failed only on minor layout points: B1-02 (monocot root) and B2a-02 (nutrition flowchart).

## What I would change for the other subjects

1. **Draw anatomy and plant sections with the AI model, not in code.** Gemini classed the transverse sections of roots and leaves as code-drawn; matplotlib could not draw them well (three were redone as AI images). The classification step should treat any biological section or organism as AI, and keep code for graphs, charts, flowcharts, tables, circuits and geometry.
2. **Be gentler on annotation labels.** 27 pictures failed only because their label list holds process notes ("inspiration", "oxygen in", test results) that do not point at one part. Either keep such notes as captions under the picture, or let the label step place the parts that are real and put the annotations in a caption line.
3. **Code-drawn images need a simpler target.** 40 of about 120 code images failed on overlap or small layout faults. A fixed library of layouts (flowchart, cycle, graph, table) would work better than asking the model to write free-form drawing code each time; the failure rate was highest for dense schematic diagrams.
4. **The raw-picture check is strict about complex anatomy** (31 failed). Some failures are real (wrong rib count, missing intestine), others are nitpicks. A second opinion step on the failures, by me, would save re-rolls; I used it only for the nephron.
5. **Cost.** Expect about $0.10 per placed image with these settings. The costly parts were failed images (each failure costs a Flash and a Pro generation plus checks) and label placement. Cheaper options that did not hurt quality: Batch for all generation, Flash for first tries, low thinking for the label check.
6. **Stray text** appeared in about a third of first tries (numbers on panels, caption words) even with a no-text rule; the check catches it and a re-roll usually fixes it. Removing words like "numbered" from prompts helped.
7. **Sensitive subjects (CRK, IRK):** not run here. Plan the same pipeline with the teacher-review marking from the decisions, and keep Arabic text and real-person portraits out of the AI step.
8. **Resumability.** The run was interrupted twice (a restart and a cost change). Saving each Batch job name so results can be fetched again (added mid-run) should stay.

## Files

- `tools/make_images.py`: the whole pipeline; `tools/make_gallery.py`: the gallery page; prompts and label coordinates in `tools/specs/biology/*-prompts.json` and `*-labels.json`; code-drawn scripts in `tools/specs/biology/code/`.
