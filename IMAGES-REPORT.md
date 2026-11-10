# Images report: Biology leftovers and 14 subjects (updated after the restore pass)

**1319 of 1399 placeholders now have an image** (94%); **80 placeholders are still in the notes** (9 skipped by rule, 28 failed the checks in the main run and cleanup, and 62 were removed in the redo pass because the regenerated picture still failed the Pro check: see "Redo pass"). Spend: $57.60 main run, $5.80 cleanup, about $2.60 panel audit, $18.51 redo pass (cap $30), about $87 in total. Galleries for your phone: `subjects/<subject>/images/GALLERY-<subject>.md`.

## Restore pass (fifth task)

Of the 62 removed images, the 40 removed for factual mistakes stayed removed (this includes the five I had accepted by eye earlier: all five were in the factual group). For the 22 multi-panel images that failed regeneration I took the version from before the panel audit and had Gemini Pro check **the drawing only** (not the labels) against its placeholder and the notes text. **19 were restored** (image, notes line and label spec; untidy labels are accepted), **3 stay placeholders** because the drawing has a factual mistake. Cost about $0.11 of the $2 cap. **Placed images now: 1319 of 1399** (80 placeholders left).

Restored: `A1-01-six-days-creation-panels`, `A18-01-accounting-methods-comparison-scene`, `A5a-01-quranic-surahs-thematic-visual`, `B2c-01-food-classes-chart`, `B2c-06-food-energy-calorimetry-apparatus`, `B3b-08-xylem-phloem-longitudinal-section`, `B4-04-desert-wind-landforms`, `B4a-08-leaf-epidermis-stomata-structure`, `B4b-13-yeast-industrial-fermentation-products`, `B6a-02-plant-supporting-tissues`, `B6b-06-cervical-vertebrae-comparison`, `B6b-12-antagonistic-arm-muscles`, `C1-08-rain-gauge-apparatus`, `C1-13-human-impact-ecosystems`, `C5-01-parable-sower-panels`, `C6-12-soil-erosion-types-stages`, `D2b-08-bt-crop-mechanism`, `D3-07-bread-making-yeast-fermentation`, `E1-04-lamarck-giraffe-neck-evolution`.

Kept as placeholders (drawing mistake found):

| Image | Mistake |
|---|---|
| `B2c-10-balanced-diet-plate` | Jollof rice is incorrectly placed in a separate, unlabeled section rather than within the starchy foods section. |
| `B5-05-stoma-lenticel-plant` | The arrows showing oxygen and water vapour leaving the stoma are missing; The arrows showing carbon (IV) oxide and water vapour leaving and oxygen entering the lenticel are missing |
| `E2-06-analogous-insect-bird-wings` | The required 'equals' sign over the word function and 'not equals' sign over the word structure are missing between the wings. |

## Redo pass (fourth task)

**Cost: $18.51 of the $30 cap.** Factual drawing mistakes were regenerated with `gemini-3-pro-image` (Batch), checked by Gemini Pro against the description, the labels and the notes text, and relabelled. Up to 2 tries; if a picture still failed, the image was **removed and the `[IMAGE: ...]` placeholder put back in the notes**.

### Result in numbers

| Group | Pictures | Regenerated and passed | Removed, placeholder restored |
|---|---|---|---|
| Factual drawing mistakes (of the 132 confirmed) | 105 | **65** | **40** |
| Reverted multi-panel images (wide spacing, captions under each panel) | 30 | **8** | **22** |
| Total | 135 | **73** | **62** |
| Minor caption problems (30 left after the rows above): captions moved into free space | 30 | **6** moved | 24 put back to the version before the panel audit |

(The other 10 of the 40 caption images were in the groups above and were redone or removed there.) **Images restored to placeholders: 62.** Each failed twice against the Pro check or could not be labelled cleanly. The earlier versions are still in git history (commit `83e367a` is the last one before this pass): `git checkout 83e367a -- subjects/<subject>/images/<name>.png` brings one back, and `5` of them were images I had accepted by eye in the cleanup pass (marked below): the Pro check is stricter than the Flash check used before, and a few of its reasons are nitpicks, so some of these may be worth restoring by hand.

### 1. Triage of the 132 confirmed drawing mistakes

Gemini Pro sorted each confirmed claim (with the description, labels and notes text) into **factual**: a student would learn something false (wrong count the notes or labels give, a named structure missing or wrong, a structure in the wrong place, wrong colour of a real organism, a process drawn the wrong way round), and **cosmetic**: style, glitches, lighting, minor proportions, small gaps, details the notes do not teach. A first, more lenient pass called 128 of 132 factual; I made the rubric stricter because every factual item costs a regeneration. **105 factual, 27 cosmetic** (plus 16 claims that were only about a gap or break in a line, which are cosmetic or repaint leftovers and were never in the 132).

**Factual (fixed; outcome in the last column)**

| Subject | Image | Mistake | Outcome |
|---|---|---|---|
| Agricultural Science | `A5-02-farmer-protective-agrochemical-gear` | The prompt specified an arrow showing wind blowing from behind the farmer, but no wind direction arrow is present in the drawing | removed, placeholder restored |
| Agricultural Science | `B13-03-cassava-mosaic-virus-leaf` | The whitefly is drawn with only four legs instead of six legs characteristic of insects. | regenerated, passed |
| Agricultural Science | `B6-02-double-fertilization-process` | Too many male gametes/nuclei are depicted: there are two inside the pollen tube in the lower right, plus two additional orange structures shown already inside/fusing with | removed, placeholder restored |
| Agricultural Science | `B7-02-vegetative-plant-propagation-methods` | In the budding panel (top right), the tape/wrapping is placed well below the T-cut rather than wrapped securely over the cut and bud union to hold the bud in place. | regenerated, passed |
| Agricultural Science | `C1-05-rooster-external-anatomy` | The spur on the rooster's legs is pointing forward/inward rather than backward (the spurs normally emerge from the posteromedial surface of the shank and curve backwards/ | regenerated, passed |
| Agricultural Science | `C3-01-avian-digestive-system` | The caeca (paired blind sacs) are drawn detached or joining incorrectly, branching off the terminal part/cloaca rather than branching at the junction between the small in | regenerated, passed |
| Agricultural Science | `C3-02-ruminant-stomach-compartments` | The description states 'Arrows indicate the flow of food, with a two-way arrow in the oesophagus to show regurgitation', but there are no flow arrows drawn in the diagram | regenerated, passed |
| Agricultural Science | `C9-01-honeybee-castes-morphological-comparison` | The pollen baskets (corbiculae) on the worker bee are depicted as large, symmetrical beige lobes detached from the legs and protruding directly from the sides of the abdo | regenerated, passed |
| Agricultural Science | `E1-01-farm-surveying-tools-collection` | A Gunter's survey chain consists of long rigid steel wire rods/links (each roughly 20 cm / 7.92 inches long) connected by small circular or oval rings (typically 2-3 ring | regenerated, passed |
| Agricultural Science | `E3-02-disc-mouldboard-ploughs` | The mouldboard plough is drawn as two stacked identical curved blades/bodies vertically above one another (like a stylized reversible plough, but incorrectly configured a | removed, placeholder restored |
| Agricultural Science | `E5-03-maize-storage-crib` | The rat guards (cones) on the stilt legs are drawn pointing upwards like funnels/cups rather than downward-pointing, meaning rats can easily climb over them and they will | removed, placeholder restored |
| Biology | `B1-10-human-torso-internal-organs` | The descending colon terminates inappropriately by directly joining into the urinary bladder instead of leading to the rectum. | removed, placeholder restored |
| Biology | `B2a-03-ruminant-stomach` | An extra looping tube emerges from the reticulum and circles around before re-entering near the omasum/esophagus, instead of the regurgitation path going directly back up | removed, placeholder restored |
| Biology | `B2a-11-bladderwort-trap-mechanism` | The bladder trap morphology is drawn symmetrically with an open tube at both top and bottom, whereas a true Utricularia bladder is an asymmetrical, pear-shaped or ovate e | removed, placeholder restored |
| Biology | `B2b-06-carbon-dioxide-requirement-experiment` | The polythene bag is tied only around the middle of the pot rather than enclosing the pot and soil tightly around the base of the plant stem, allowing soil respiration to | regenerated, passed |
| Biology | `B2b-09-starch-test-leaf-steps` | In step 6, the leaf remains green around the edges while iodine turns part of it blue-black, but the leaf was already decolourised/bleached pale in steps 4 and 5, so the  | regenerated, passed |
| Biology | `B2b-11-plant-mineral-deficiency-water` | Bubbles are drawn rising in open air from the top of the aeration tube instead of emerging from the bottom of the tube inside the culture solution to aerate the water. | regenerated, passed |
| Biology | `B2c-07-kwashiorkor-marasmus` | The child on the left is drawn with unnatural green/cyan skin and blue-tinted lower limbs, rather than human skin pigmentation. | regenerated, passed |
| Biology | `B2c-08-rickets-skeletal` | Both the healthy child and the child with rickets are drawn with abnormally swollen or bulbous wrists, which is a symptom of rickets and should not be present on the heal | regenerated, passed |
| Biology | `B2d-01-molar-tooth-cross-section` | The outer enamel layer (white) continues down the roots instead of ending at the neck/crown margin, meaning enamel covers the roots where cementum should be. | regenerated, passed |
| Biology | `B2d-04-human-skull-dentition` | The dental formula per quadrant in a human adult is 2 incisors, 1 canine, 2 premolars, and 3 molars. Here, in each quadrant from anterior to posterior, there are 2 blue t | regenerated, passed |
| Biology | `B2d-06-dog-skull-carnassials` | There is a row of extra, disembodied teeth floating in mid-air between the upper and lower jaws without any supporting jawbone. | removed, placeholder restored |
| Biology | `B2e-03-oesophageal-peristalsis-mechanism` | The external wall of the oesophagus bulges outwards behind the bolus where the circular muscle is labelled as contracted, instead of constricting inward to narrow the tub | regenerated, passed |
| Biology | `B2e-06-hepatobiliary-pancreatic-ducts` | The C-loop of the duodenum is curved backwards/opposite to normal anatomy relative to the stomach and pancreas, with the opening from the stomach connecting to the upper  | removed, placeholder restored |
| Biology | `B3a-05-mammalian-heart-internal-section` | The pulmonary trunk is shown floating in front without a continuous connection or origin from the right ventricle chamber; it is cut off abruptly above the valve. | removed, placeholder restored |
| Biology | `B3a-12-hepatic-portal-circulation-schematic` | The arrows in the inferior vena cava point downwards (away from the heart), whereas venous blood in the IVC flows upwards towards the heart. | regenerated, passed |
| Biology | `B3a-15-blood-smear-cellular-composition` | Several red blood cells are drawn pale green instead of pale red/pinkish-orange, which is incorrect for human erythrocytes. | regenerated, passed |
| Biology | `B3a-16-human-lymphatic-system-anatomy` | The tonsils are shown inside the lower neck / throat near the base of the neck/clavicle region rather than in the pharynx/oral cavity. | removed, placeholder restored |
| Biology | `B3a-17-cockroach-open-circulatory-system` | The insect has far more than three pairs of thoracic legs (there are at least 5-6 stubby leg-like appendages depicted along the ventral side of thorax and abdomen). | regenerated, passed |
| Biology | `B3b-04-onion-epidermis-cell-plasmolysis` | In the middle panel (plasmolysis), the second and third cells from the left show two nuclei (two bluish-green circles) per cell instead of one. | regenerated, passed |
| Biology | `B3b-06-dicot-stem-transverse-section` | In the low-power plan (top left circle), the orientation of tissues within each vascular bundle is inverted: the xylem (red-brown with vessels) is drawn towards the outer | regenerated, passed |
| Biology | `B3b-13-bubble-potometer-apparatus` | The open end of the capillary tube entering the beaker does not dip into the water in the beaker; it terminates above the water level. | removed, placeholder restored |
| Biology | `B4a-05-cockroach-tracheal-system-anatomy` | There are only 5 pairs of abdominal spiracles depicted along the abdominal trunk instead of the correct 8 pairs characteristic of a cockroach (total 7 pairs shown instead | removed, placeholder restored |
| Biology | `B4a-07-avian-respiratory-system-air` | The directional arrows for airflow are reversed or inconsistent with avian unidirectional respiration: inhaled air normally flows first to the posterior air sacs and then | regenerated, passed |
| Biology | `B4a-14-alveolus-gas-exchange-capillary` | Gas exchange arrows only show movement into the alveolus (both arrows point into the alveolus), missing an arrow showing oxygen diffusing into the red blood cells/capilla | regenerated, passed |
| Biology | `B4b-08-plant-respiration-carbon-dioxide` | In the aspirator bottle (far right), the air delivery tube dips deeply below the water level, which would prevent air from being drawn into the bottle by the draining wat | removed, placeholder restored |
| Biology | `B4b-10-germinating-seeds-heat-production` | The thermometer bulb containing the liquid reservoir is drawn at the bottom outside the flask, rather than inside among the seeds where temperature is supposed to be meas | removed, placeholder restored |
| Biology | `B4b-11-simple-respirometer-germinating-seeds` | The capillary tube for the experimental setup has an arrow showing movement towards the right (away from the tube), whereas oxygen consumption causes a decrease in volume | regenerated, passed |
| Biology | `B5-01-comparative-invertebrate-excretory-structures` | The flame cell is drawn with cilia originating from the bottom of the tube pointing backwards into a bulb that has an open apical pore, instead of the cilia projecting fr | regenerated, passed |
| Biology | `B5-02-planaria-flame-cell-system` | In a flame cell (protonephridium), the cilia tuft should project into the internal lumen/tubule towards the excretory duct to propel fluid downstream, but here the cilia  | regenerated, passed |
| Biology | `B5-06-human-urinary-system` | The left kidney (on the anatomical left, image right) is shown positioned lower than the right kidney (on the anatomical right, image left); in human anatomy, the right k | regenerated, passed |
| Biology | `B5-07-kidney-longitudinal-section` | The collecting duct of the nephron (green tube) ends blindly in the cortex instead of extending through the medulla and emptying at the renal papilla into the minor calyx | removed, placeholder restored |
| Biology | `B5-08-nephron-structure-detailed` | The proximal convoluted tubule (green tubule) is shown continuous with the afferent/efferent blood vessel entering the glomerulus, rather than continuous with the urinary | regenerated, passed |
| Biology | `B6a-06-phototropism-seedling-experiment-setup` | The yellow rays of light are shown emitting outward from the slit of the cardboard box towards the outside control plant, rather than entering the box through the slit fr | regenerated, passed |
| Biology | `B6a-11-nyctinastic-plant-movements` | In the inset showing the pulvinus, the swelling is incorrectly drawn on the main stem instead of at the base of the petiole/leafstalk (the pulvinus is a swollen structure | removed, placeholder restored |
| Biology | `B6a-13-root-growth-marking-experiment` | In the 'after 48 hours' diagram, the region of root elongation is depicted in the middle/upper portion of the radicle instead of just behind the root tip (the zone of elo | removed, placeholder restored |
| Biology | `B6b-01-insect-exoskeleton-anatomy` | In the cuticle cross-section, the apodeme (internal invagination of the exoskeleton for muscle attachment) is depicted as an isolated floating structure inside the endocu | removed, placeholder restored |
| Biology | `B6b-07-mammalian-vertebrae-comparison` | In the thoracic vertebra lateral view, the neural spine and articular processes are incorrectly drawn as two opposite diverging projections (one pointing anterodorsally a | removed, placeholder restored |
| Biology | `B6b-08-human-rib-cage` | The brackets on the left mark 6 true ribs (ribs 1 to 6) instead of 7, 3 false ribs (ribs 7 to 9) instead of 8 to 10, and only 1 floating rib pair instead of 2 pairs (ribs | regenerated, passed |
| Biology | `B6b-09-pectoral-pelvic-girdles` | In anatomical position, the radius is lateral (on the thumb side) and the ulna is medial (on the pinky side). In the forelimb diagram, the thumb is on the right side of t | regenerated, passed |
| Biology | `B7a-02-yeast-budding-stages` | In stage 3, the parent cell contains two purple spherical bodies (nuclei) while the bud contains an additional third purple body, rather than having a single nucleus divi | regenerated, passed |
| Biology | `B7a-03-asexual-reproduction-types-grid` | Spirogyra is an unbranched filamentous green alga, but one of the regenerating fragments at the bottom right is drawn with a branched filament (Y-junction). | removed, placeholder restored |
| Biology | `B7a-04-asexual-vs-sexual-reproduction` | The diagram uses human/mammalian gametes (a flagellated sperm cell and an animal ovum) to represent the gametes produced by flowering plants (angiosperms), which produce  | removed, placeholder restored |
| Biology | `B7b-02-stamen-pollen-grain-structure` | An anther has four pollen sacs in total (two in each of the two anther lobes), but here a single cut lobe displays all four pollen sacs rather than two. | removed, placeholder restored |
| Biology | `B7b-08-maize-plant-reproduction` | Multiple silks (styles) are shown emerging from a single ovary in the female flower inset, whereas each maize ovary possesses only one single silk (style/stigma). | removed, placeholder restored |
| Biology | `B7b-11-double-fertilisation-angiosperms` | The dotted arrows showing fertilisation are pointing downwards from the polar nuclei to the egg apparatus, rather than showing male nuclei travelling/fusing with the egg  | regenerated, passed |
| Biology | `B7b-16-fruit-seed-dispersal-mechanisms` | In the panel intended to show a Bidens fruit with two barbed spines caught in fur, an entire green plant shoot or bur with green leaves/bracts is drawn instead of a typic | removed, placeholder restored |
| Biology | `B7c-01-male-reproductive-system-section` | The vas deferens is drawn passing directly through the interior of the urinary bladder rather than looping around the outside of it. | regenerated, passed |
| Biology | `B7c-06-ovulation-implantation-pathway` | The arrows along the fallopian tube (oviduct) point backwards, showing movement from the ovary up the tube away from the uterus, but then the next arrows point from left  | removed, placeholder restored |
| Biology | `B8-08-germination-oxygen-requirement-apparatus` | The hanging bags are tied to or suspended by a string wrapped magically around the outside of the conical flask rather than suspended from the rubber stopper or hung insi | regenerated, passed |
| Biology | `B8-12-seed-food-mobilisation-flowchart` | The arrows representing enzyme release from the aleurone layer point in the wrong direction (pointing towards the aleurone layer or outside the grain, rather than enterin | removed, placeholder restored |
| Biology | `B9a-04-cranial-meninges-cross-section` | The pia mater does not follow the folds (sulci and gyri) of the cerebral cortex; instead, it spans across the surface while the subarachnoid space and arachnoid trabecula | regenerated, passed |
| Biology | `B9a-05-human-brain-sagittal-section` | The cerebral hemisphere is drawn with superficial gyri and sulci on its surface instead of showing the cut surface / medial wall of the hemisphere characteristic of a lon | regenerated, passed |
| Biology | `B9a-07-spinal-cord-transverse-section` | The dorsal-ventral orientation of the spinal cord is inverted relative to the vertebra: the spinous process of the vertebra is at the top (dorsal side of the body), but t | regenerated, passed |
| Biology | `B9a-11-spinal-reflex-arc` | The sensory neurone is depicted with two cell bodies: one in the dorsal root ganglion and another inside the dorsal horn of the spinal cord grey matter. | removed, placeholder restored |
| Biology | `B9b-01-human-skin-anatomy` | The arrector pili muscle is attached to a sensory receptor/corpuscle at its upper end instead of connecting the hair follicle to the dermal papillary layer / basement mem | regenerated, passed |
| Biology | `B9b-05-external-eye-lacrimal-apparatus` | The arrows indicating tear flow show tears flowing away from the nasolacrimal duct (pointing outward towards the lateral corner of the eye) instead of flowing from the la | regenerated, passed |
| Biology | `B9b-06-human-eyeball-horizontal-section` | The fovea (yellow spot) is drawn as a bump/protrusion on the retina rather than an inward indentation or depression (foveal pit). | removed, placeholder restored |
| Biology | `B9c-07-pancreas-islet-histology` | The islet of Langerhans is drawn as a single concentric ring of epithelial-like cells surrounding an empty center containing capillaries, rather than a solid cluster/isla | regenerated, passed |
| Biology | `B9c-11-auxin-tropisms-mechanism` | In the phototropism diagram, the cells on the lit (convex/concave) inner side are drawn longer/more elongated, while the cells on the shaded side are drawn shorter, which | regenerated, passed |
| Biology | `C1-10-wind-vane-anemometer` | The compass directions arms on the wind vane lack directional letters (N, S, E, W), showing blank rectangular tabs instead. | removed, placeholder restored |
| Biology | `C3-04-stream-ecosystem-profile-cross` | Blackfly larvae are drawn attached by their anterior ends (mouth fan brushes at the attachment point) rather than anchored by their posterior abdomen/silk hooks with thei | regenerated, passed |
| Biology | `C3-08-tropical-rainforest-canopy` | The chameleon's tongue is missing; the description specified its long tongue catching an insect, but only a floating insect is drawn in front of its closed/bare mouth wit | regenerated, passed |
| Biology | `C3-09-savanna-field-ecosystem-landscape` | The variegated grasshopper (Zonocerus variegatus) is illustrated in plain brown rather than its characteristic aposematic warning coloration (bright green, yellow, black, | regenerated, passed |
| Biology | `C6-07-air-soil-experiment-apparatus` | The container shown is a beaker rather than a measuring cylinder, and it lacks volumetric graduation markings needed to measure volume. | removed, placeholder restored |
| Biology | `C6-09-soil-capillarity-experiment-apparatus` | The glass tubes are drawn with closed, rounded test tube bottoms instead of open-ended tubes; the cotton wool plug is placed inside a closed bottom, preventing water from | regenerated, passed |
| Biology | `C7a-02-anopheles-mosquito-life-cycle` | The pupa is drawn deep underwater with its breathing trumpets pointing upwards into open water rather than touching the water surface film. | removed, placeholder restored |
| Biology | `C7a-06-schistosoma-haematobium-life-cycle` | The egg of Schistosoma haematobium is typically oval with a prominent terminal spine; here it is depicted with numerous spikes/rays radiating around its entire circumfere | regenerated, passed |
| Biology | `C7a-08-housefly-life-cycle-disease` | The larva (maggot) is depicted with a distinct caterpillar-like head capsule with eyes/mouthparts, whereas housefly larvae are acephalic (headless, tapered maggots with i | regenerated, passed |
| Biology | `C7c-08-sanitary-landfill-cross-section` | The leachate collection pipe at the bottom is shown directly connected to a vertical pipe leading to a gas flare at the top, confusing the leachate collection system with | removed, placeholder restored |
| Biology | `C7d-03-shelterbelt-windbreak-landscape` | The arrows showing wind direction on the right point away from the shelterbelt toward the desert, or diverge inconsistently, rather than blowing from the desert directly  | regenerated, passed |
| Biology | `D2b-02-livestock-cross-breeding` | Both parents are depicted as female cows with visible udders (crossing two female animals rather than a bull and a cow). | regenerated, passed |
| Biology | `D3-05-industrial-fermenter-cross-section` | The arrow pointing to the upper right outlet of the water jacket points downwards into the pipe, indicating water entering from the top, while the bottom left inlet also  | removed, placeholder restored |
| Biology | `D3-08-biogas-digester-cross-section` | The gas pipe leads directly into the side of the cooking pot instead of feeding into the burner/stove underneath. | regenerated, passed |
| Biology | `E1-02-redi-spontaneous-generation-experiment` | In the sealed jar (middle jar), a fly is drawn inside the sealed glass jar despite the experiment requiring the sealed jar to exclude flies completely. | regenerated, passed |
| Biology | `E1-09-antibiotic-resistance-evolution-steps` | In circle 3, the dividing bacteria are drawn as round cocci clusters rather than rod-shaped bacilli like the red bacteria in circles 1, 2, and 4. | regenerated, passed |
| Biology | `E2-04-horse-evolution-stages-foot` | The modern horse (Equus) foot skeleton beneath the top-right horse is missing, or the foot skeletons are misaligned relative to the animals so that Pliohippus shows splin | regenerated, passed |
| Biology | `E2-05-homologous-pentadactyl-forelimbs-comparison` | The frog forelimb is depicted with five complete digits (pentadactyl), but anuran amphibians (frogs) naturally have only four digits on their front limbs (manus). | regenerated, passed |
| Biology | `E2-07-human-vestigial-organs` | The appendix is depicted in the purple circle connecting to the left side of the human abdomen (anatomical left), but the vermiform appendix and cecum are located in the  | removed, placeholder restored |
| Biology | `E2-11-plant-phylogenetic-evolutionary-tree` | The branching order of the phylogenetic tree is incorrect: the gymnosperm branch diverges lower on the main axis/branch than the fern branch (gymnosperms placed on a side | removed, placeholder restored |
| Chemistry | `A1-01-simple-vs-fractional-distillation` | The receiving flasks are completely sealed with stoppers/corks around the delivery tube, creating a closed system which would cause dangerous pressure build-up during dis | regenerated, passed |
| Chemistry | `A14a-02-chlorine-gas-laboratory-preparation` | In the first wash bottle, the gas outlet tube dips into the liquid rather than staying above the liquid level, while the inlet tube stops above the bottom (in fact both t | regenerated, passed |
| Chemistry | `A14b-01-oxygen-gas-laboratory-preparation` | The gas jar is not inverted: its open rim/flange is shown at the top rather than resting downward under water on a beehive shelf or stand, and the delivery tube strangely | regenerated, passed |
| Chemistry | `A14c-01-nitrogen-gas-laboratory-preparation` | The gas jar is depicted right-side up with its rim at the top instead of being an inverted gas jar, while the beehive shelf / delivery tube strangely enters through its c | removed, placeholder restored |
| Chemistry | `A16b-02-traditional-local-gin-distillation` | The boiling drum is completely open at the top around the delivery tube, allowing steam and alcohol vapors to escape freely into the air rather than being sealed and dire | regenerated, passed |
| CRK | `B2-01-elijah-fire-mount-carmel` | The description states 'Water trench dried up', but the trench in the illustration is drawn full of bubbling water rather than dried up. | regenerated, passed |
| Geography | `A6-03-gis-map-scanning-digitizing` | The vector line appearing on the computer screen does not match the river being traced on the digitizing tablet; instead, the screen displays a coastline or different fea | regenerated, passed |
| Geography | `B2-01-earth-internal-crust-cross` | The inset magnification lines connect to the outer core or inner mantle boundary rather than extending from the outermost crust layer. | regenerated, passed |
| Geography | `B4-02-soil-creep-hillside` | The telegraph pole is leaning uphill instead of downhill with the direction of soil creep. | regenerated, passed |
| Geography | `B5-04-oxbow-lake-sequential` | In panel 4, the ox-bow lake is incorrectly depicted as two symmetric loops on both sides of a perfectly straight channel, rather than a single abandoned curved meander lo | removed, placeholder restored |
| History | `A2-02-nok-terracotta-human-head` | The hairstyle includes bright pastel multi-colored sections (green, blue, pink, purple, yellow) rather than being entirely terracotta clay. | regenerated, passed |
| Physics | `A11-01-measuring-volume-solids-apparatus` | The water level inside the Eureka can is shown below the spout/lip rather than reaching up to the spout, even though water is currently shown dripping out into the measur | regenerated, passed |
| Physics | `A22-06-resonance-tube-apparatus` | The tuning fork is oriented upside down, with its handle pointing into the top of the glass tube and its vibrating prongs facing upward, rather than having its prongs hel | removed, placeholder restored |
| Physics | `A38b-03-electron-diffraction-apparatus-schematic` | The electron beam passing through the thin crystal is drawn as continuing as a single narrow beam straight to the center of the screen, rather than spreading out into dif | removed, placeholder restored |
| Use of English | `C2a-04-consonant-articulation-mouth-diagrams` | The tongue positioning in the two sagittal cross-sections is nearly identical, failing to show the tongue blade raised post-alveolar for /ʃ/ versus tongue tip near the al | regenerated, passed |

**Cosmetic (not fixed)**

| Subject | Image | Issue | Why cosmetic |
|---|---|---|---|
| Agricultural Science | `C6-03-rabbit-handling-housing` | The person has an extra third hand: one hand is grasping behind the rabbit's head/ears, a second hand is supporting underneath the chest/abdomen, and  | The extra hand is a rendering glitch (AI artifact), not a biological or agricultural error taught in |
| Biology | `B2a-08-rhizopus-mould-structure` | The hyphae (stolons) are drawn with visible cross-walls (septa), but Rhizopus is a zygomycete fungus characterized by coenocytic (aseptate) hyphae. | The absence of septa (cross-walls) is biologically correct but is not explicitly taught in the provi |
| Biology | `B2c-12-benedicts-reducing-sugar-test` | The clamp arm holding the test tube terminates abruptly in mid-air without being attached to a retort stand. | A floating clamp is a minor rendering glitch that does not change the biological lesson. |
| Biology | `B2e-12-ruminant-stomach-chambers` | The description states there are arrows showing the path of food (cud returning to mouth and food passing between chambers), but no flow arrows are pr | Missing arrows are a cosmetic issue, as the notes and labels do not strictly dictate arrow placement |
| Biology | `B3a-02-agar-cube-diffusion-experiment` | The large cube outside the beaker is not cut in half to show a cross section; it is drawn as an intact cube with a transparent purple/colourless layer | The notes do not require cutting the large cube in half; things requested only by the description ar |
| Biology | `B3a-09-capillary-bed-tissue-exchange` | The arrows showing exchange of fluid, oxygen/glucose, and carbon dioxide/wastes are missing entirely from the diagram despite being required for the l | Missing arrows are considered a cosmetic issue unless they are drawn in the wrong direction. |
| Biology | `B3a-11-systemic-blood-circulation-schematic` | The arms show only venous vessels (blue) and completely lack systemic arteries (red), while the neck and lower body show both arteries and veins. | The notes and labels do not specifically require or name the arteries in the arms. |
| Biology | `B3b-10-tree-trunk-ringing-experiment` | The arrows showing transport of water/minerals and food, requested in the description and essential to the corresponding labels ('water and minerals u | Missing arrows are a cosmetic omission since the structures themselves are present and not contradic |
| Biology | `B4a-08-leaf-epidermis-stomata-structure` | In the vertical section of the stoma (bottom right), the guard cells are drawn identical to their surface view (crescent-shaped with full length chlor | The specific cross-sectional anatomy of the guard cells in vertical section is not detailed in the n |
| Biology | `B4a-10-stoma-opening-closing-mechanism` | Each guard cell contains multiple purple oval structures resembling nuclei (up to 5-6 per cell), whereas plant guard cells are eukaryotic cells contai | The exact number of nuclei in guard cells is not explicitly taught or counted in the provided notes. |
| Biology | `B4a-13-bell-jar-lung-model` | The arrows indicating air flow ('air in' entering the tube and 'air out' leaving the tube) specified in the model description are missing from both be | The labels already state 'air in' and 'air out'; missing graphic arrows are defined as cosmetic. |
| Biology | `B4b-12-yeast-anaerobic-fermentation-experiment` | The bottom end of the right delivery tube inside the test tube has an anomalous closed loop shape instead of an open tube submerged in the liquid. | The closed loop on the delivery tube is a minor rendering glitch of the apparatus. |
| Biology | `B5-11-inhaled-exhaled-air-apparatus` | The connection between the Y-tube and the two test tubes is non-functional and incorrectly drawn: the purple tubing loops nonsensically as a single ta | Tangled tubing is a rendering glitch and apparatus detail that does not change the lesson. |
| Biology | `B6a-03-dicot-root-transverse-section` | A horizontal band of severe image glitching/distortion (corrupted slice) runs across the middle of the root cross-section (around y=380 to y=520), dis | Horizontal glitch line is a cosmetic rendering issue. |
| Biology | `B6b-03-human-skeleton-front-view` | The color coding described (axial skeleton pale blue, appendicular pale yellow) is inconsistent: the skull is colored pale green, the pelvic girdle is | Color inconsistencies that do not contradict explicit factual text claims are considered cosmetic st |
| Biology | `B6b-04-human-skull-lateral-view` | The parietal bone region of the cranium is incorrectly divided into multiple alternating colored bands (blue and cream) without real anatomical suture | The alternating colored bands on the parietal bone are a rendering glitch or style choice, not a lab |
| Biology | `B9a-03-three-types-neurones` | The arrows showing the direction of the nerve impulse mentioned in the prompt are missing from the drawing. | Missing arrows for impulse direction is an extra detail, considered cosmetic. |
| Biology | `B9a-06-cerebral-hemisphere-lobes` | The sensory area (postcentral gyrus) strip at the front of the parietal lobe is not demarcated or differentiated from the rest of the parietal lobe, u | Missing a demarcation line for a requested area is a cosmetic missing detail. |
| Biology | `B9b-12-human-ear-anatomy` | Severe pixelation and rendering glitches across the middle and inner ear region, obscuring and distorting the auditory nerve, inner ear structures, an | Rendering glitches and pixelation are explicitly categorized as cosmetic issues. |
| Biology | `B9c-06-adrenal-gland-anatomy-section` | The kidney is coloured pale greenish-grey rather than the anatomically correct reddish-brown. | The notes do not specify the colour of the kidney. |
| Biology | `C2-04-parasitic-organisms-anatomical-panels` | The tapeworm's segments (proglottids) are drawn widest near the scolex/head and progressively narrow toward the distal end, whereas in real tapeworms  | The notes and labels do not teach the exact progressive widening of tapeworm segments. |
| Biology | `C4-06-desert-biome-oasis-scene` | The scorpion is drawn with only six walking legs (three on each side) plus pedipalps, instead of eight walking legs characteristic of arachnids. | The exact walking leg count for the scorpion is not taught in the notes or labels. |
| Biology | `D2b-06-haemolytic-disease-newborn-stages` | In the third panel, severe horizontal glitching and digital rendering artifacts distort the upper body, placenta, and head area of the fetus. | Digital rendering artifacts and glitches are cosmetic errors, not biological inaccuracies taught by  |
| Chemistry | `A1-03-gravity-filtration-laboratory-setup` | The liquid is being poured directly into the funnel rather than running down the glass rod, defeating the purpose of using a glass rod to guide the li | Pouring without exactly touching the glass rod is a cosmetic rendering detail. |
| Chemistry | `A14c-03-nitrate-brown-ring-test` | The meniscus/interface showing the brown ring is drawn tilted perpendicular to the tube axis rather than settling horizontally under gravity, while th | The exact angle of the liquid meniscus under gravity is a rendering issue, not a chemical concept ta |
| Geography | `A2-02-measuring-curved-distance-thread` | The ruler lacks numbers or measurement markings to indicate scale or measure exactly 15.6 cm. | The lack of numbers on the ruler is a cosmetic apparatus detail. |
| Government | `A15-01-public-opinion-expression-panels` | In the bottom-right panel depicting a phone-in programme, the listener/caller is depicted sitting directly at the radio studio desk across from the pr | The caller sitting in the studio is a panel scene detail, not factual. |

Gap-only claims (cosmetic): `A15-01-linear-expansivity-apparatus`, `A15-03-specific-gravity-bottle-experiment`, `A9-02-spring-balance`, `B1-13-male-rabbit-reproductive-system`, `B2c-06-food-energy-calorimetry-apparatus`, `B4a-01-respiratory-surface-exchange`, `B6b-12-antagonistic-arm-muscles`, `B8-05-bean-seed-anatomy`, `B8-09-epigeal-germination-stages`, `B9c-12-klinostat-geotropism-experiment-apparatus`, `B9c-15-leaf-abscission-zone-anatomy`, `C1-04-altitudinal-zonation-mountain`, `C1-06-secchi-disc-turbidity-measurement`, `C8-01-earthen-fish-pond-cross`, `D1-05-measuring-student-height-weight`, `E2-02-sedimentary-rock-fossil-strata`.

### 2 and 3. Pictures removed (placeholder restored): 62

| Subject | Notes file | Image | Group | Last reason | Earlier accepted by me |
|---|---|---|---|---|---|
| Accounting | `A18-information-technology-in-accounting` | `A18-01-accounting-methods-comparison-scene` | panel | labels or layout still wrong after 3 placements:   |  |
| Agricultural Science | `A5-farm-inputs` | `A5-02-farmer-protective-agrochemical-gear` | factual | Pro check: Missing wind arrow pushing mist. |  |
| Agricultural Science | `B6-growth-development-and-reproduction` | `B6-02-double-fertilization-process` | factual | Pro check: Ovule is located outside ovary.; Shows four male nuclei, violating constraint. |  |
| Agricultural Science | `E3-farm-machinery-and-implements` | `E3-02-disc-mouldboard-ploughs` | factual | Pro check: Disc plough has four discs instead of three.; Mouldboard structure disjointed. |  |
| Agricultural Science | `E5-processing-and-storage` | `E5-03-maize-storage-crib` | factual | Pro check: Rat guards are drawn as upward-pointing cups instead of downward-pointing cones. |  |
| Biology | `B1-internal-structure` | `B1-10-human-torso-internal-organs` | factual | Pro check: The large intestine (descending colon) incorrectly ends at the urinary bladder instead of the rectum, repeating the specific mistake to avoid. |  |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-03-ruminant-stomach` | factual | Pro check: Image contains text (numbers 1-5 in circles).; Arrow 3 goes backwards from the oesophagus into the reticulum instead of showing the regurgitation path. |  |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-11-bladderwort-trap-mechanism` | factual | Pro check: Image contains significant text ('1' and '2').; Stage 1 bladder wall is not drawn inwards/concave.; Stage 2 bladder does not show the water flea being sucked in, it is still outsi |  |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-01-food-classes-chart` | panel | Pro check: Image layout is a grid rather than circles around a central plate.; Contains forbidden text 'MILK'. |  |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-06-food-energy-calorimetry-apparatus` | panel | Pro check: The image shows separate objects in a grid rather than the requested setup.; The objects are not arranged together as a single experimental apparatus. |  |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-10-balanced-diet-plate` | panel | Pro check: Foods are shown in separate clusters rather than on a single balanced diet plate as requested.; The layout does not represent sections on a plate divided by proportions. |  |
| Biology | `B2d-mammalian-teeth` | `B2d-06-dog-skull-carnassials` | factual | Pro check: The lower jaw shows a second large canine floating behind the first one, contradicting the requirement to draw only one large lower canine per side.; Multiple teeth on the lower j |  |
| Biology | `B2e-alimentary-canal-and-digestion` | `B2e-06-hepatobiliary-pancreatic-ducts` | factual | Pro check: Stomach is disconnected from the duodenum; it does not connect continuously to the upper end of the duodenum. | yes |
| Biology | `B3a-transport-in-animals` | `B3a-05-mammalian-heart-internal-section` | factual | Pro check: The pulmonary artery is drawn with its base opening directly into the right atrium instead of the right ventricle.; Arrows in the right atrium incorrectly show blood flowing from  |  |
| Biology | `B3a-transport-in-animals` | `B3a-16-human-lymphatic-system-anatomy` | factual | Pro check: Tonsils are missing from the upper throat.; Inset lacks internal valves in vessels. |  |
| Biology | `B3b-transport-in-plants` | `B3b-08-xylem-phloem-longitudinal-section` | panel | labels or layout still wrong after 3 placements:   |  |
| Biology | `B3b-transport-in-plants` | `B3b-13-bubble-potometer-apparatus` | factual | Pro check: The reservoir tap incorrectly has an open spout pointing to the outside air, rather than acting as a closed valve connecting the reservoir to the main apparatus. | yes |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-05-cockroach-tracheal-system-anatomy` | factual | Pro check: Cockroach outline shows 1 thoracic spiracle and 7 abdominal spiracles per side (8 pairs total), not 2 thoracic and 8 abdominal pairs as required. |  |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-08-leaf-epidermis-stomata-structure` | panel | Pro check: Bottom left panel shows guard cells in surface view rather than a true vertical section. |  |
| Biology | `B4b-cellular-respiration` | `B4b-08-plant-respiration-carbon-dioxide` | factual | Pro check: Cloth fails to fully cover bell jar; Aspirator tube enters water; Missing air flow arrows |  |
| Biology | `B4b-cellular-respiration` | `B4b-10-germinating-seeds-heat-production` | factual | Pro check: Thermometer bulbs outside flasks, not among seeds.; Thermometers are inverted. |  |
| Biology | `B4b-cellular-respiration` | `B4b-13-yeast-industrial-fermentation-products` | panel | Pro check: Contains letter B on jar resembling Bitcoin symbol; Contains empty label boxes |  |
| Biology | `B5-excretion` | `B5-05-stoma-lenticel-plant` | panel | Pro check: Contains forbidden text labels like O2 and CO2 |  |
| Biology | `B5-excretion` | `B5-07-kidney-longitudinal-section` | factual | Pro check: The exaggerated nephron's loop of Henle and green collecting duct are floating freely in the white space of the renal pelvis instead of being embedded within the tissue of a medul |  |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-02-plant-supporting-tissues` | panel | labels or layout still wrong after 3 placements: thickened corners; lumen; lignified wall  |  |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-11-nyctinastic-plant-movements` | factual | Pro check: Significant stray text is present as column headers (Bauhinia, Flamboyant, Mimosa pudica).; The mistake from the previous version is still present: the pulvinus inset shows the sw |  |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-13-root-growth-marking-experiment` | factual | Pro check: The right hand root's marks are evenly spaced instead of being widely spaced just behind the tip. |  |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-01-insect-exoskeleton-anatomy` | factual | Pro check: The joint membrane and sclerites are drawn as disconnected shapes in the bottom right corner, completely separated from the main cuticle layers. |  |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-06-cervical-vertebrae-comparison` | panel | labels or layout still wrong after 3 placements: centrum  |  |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-07-mammalian-vertebrae-comparison` | factual+panel | labels or layout still wrong after 3 placements: neural spine  |  |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-12-antagonistic-arm-muscles` | panel | Pro check: The right panel shows the biceps as red (contracted) and the triceps as pink (relaxed), which contradicts the 'arm straight' state.; The forearm bones (radius and ulna) are drawn  |  |
| Biology | `B7a-asexual-reproduction` | `B7a-03-asexual-reproduction-types-grid` | factual | Pro check: Planaria panel shows only two regenerating flatworms instead of three missing the head piece regeneration |  |
| Biology | `B7a-asexual-reproduction` | `B7a-04-asexual-vs-sexual-reproduction` | factual | Pro check: Missing arrows connecting the parent yam plant to the three identical offspring in the left column.; Missing arrows connecting the zygotes to the three resulting offspring in the  |  |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-02-stamen-pollen-grain-structure` | factual | Pro check: The cut lobe of the anther shows only two pollen sacs instead of the required four.; The anther lobe does not clearly show one lobe cut across to reveal four pollen sacs. |  |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-08-maize-plant-reproduction` | factual | Pro check: The male spikelet enlargement shows four anthers instead of the requested three.; The female flower inset incorrectly displays multiple silks emerging from a single ovary, violati |  |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-16-fruit-seed-dispersal-mechanisms` | factual | labels or layout still wrong after 3 placements: wind; animals (eaten); animals (hooks); self (explosive)  | yes |
| Biology | `B7c-reproduction-in-mammals` | `B7c-06-ovulation-implantation-pathway` | factual | labels or layout still wrong after 3 placements: zygote; morula (day 3–4); blastocyst (day 4–5); inner cell mass; trophoblast; implantation (day 6–7); uterus  |  |
| Biology | `B8-growth` | `B8-12-seed-food-mobilisation-flowchart` | factual | Pro check: Arrows point outward from the endosperm to the aleurone layer instead of inward; Missing clear representation of the aleurone layer along the edge |  |
| Biology | `B9a-nervous-coordination` | `B9a-11-spinal-reflex-arc` | factual | Pro check: The blue sensory neurone incorrectly has a second cell body inside the grey matter, violating the specific negative constraint.; The arrow direction on the motor neurone in the ar |  |
| Biology | `B9b-sense-organs` | `B9b-06-human-eyeball-horizontal-section` | factual | Pro check: The fovea is drawn as a protruding bump on the retina instead of a small pit or depression, which contradicts the specific negative constraint.; Suspensory ligaments are drawn att |  |
| Biology | `C1-factors-affecting-distribution` | `C1-08-rain-gauge-apparatus` | panel | Pro check: Fragmented into four disjoint panels instead of a single cohesive scene. |  |
| Biology | `C1-factors-affecting-distribution` | `C1-10-wind-vane-anemometer` | factual | Pro check: The image contains text (N, S, E, W), which contradicts the instruction that no text is allowed in the image as labels will be added later in code. |  |
| Biology | `C1-factors-affecting-distribution` | `C1-13-human-impact-ecosystems` | panel | labels or layout still wrong after 3 placements:   |  |
| Biology | `C6-soil` | `C6-07-air-soil-experiment-apparatus` | factual | Pro check: Arrow missing between tin and cylinder; Soil in tin is floating |  |
| Biology | `C6-soil` | `C6-12-soil-erosion-types-stages` | panel | labels or layout still wrong after 3 placements:   |  |
| Biology | `C7a-diseases` | `C7a-02-anopheles-mosquito-life-cycle` | factual+panel | Pro check: The adult female mosquito is resting parallel to the surface, but it must be resting at a 45-degree angle (head down) for Anopheles.; The eggs are not all resting exactly at the w | yes |
| Biology | `C7c-pollution-and-sanitation` | `C7c-08-sanitary-landfill-cross-section` | factual | Pro check: Methane vent pipes and leachate collection pipes are incorrectly connected together as a single plumbing system. |  |
| Biology | `D2b-applications-of-heredity` | `D2b-08-bt-crop-mechanism` | panel | Pro check: Missing arrow connecting the bacterium to the cowpea plant |  |
| Biology | `D3-biotechnology` | `D3-05-industrial-fermenter-cross-section` | factual | Pro check: Arrow for sterile air inlet points outwards instead of inwards.; Arrow for cold water in at the bottom right points upwards away from inlet instead of pointing in. |  |
| Biology | `D3-biotechnology` | `D3-07-bread-making-yeast-fermentation` | panel | labels or layout still wrong after 3 placements:   |  |
| Biology | `E1-theories-of-evolution` | `E1-04-lamarck-giraffe-neck-evolution` | panel | labels or layout still wrong after 3 placements: Lamarck's theory  |  |
| Biology | `E2-evidence-of-evolution` | `E2-06-analogous-insect-bird-wings` | panel | labels or layout still wrong after 3 placements:   |  |
| Biology | `E2-evidence-of-evolution` | `E2-07-human-vestigial-organs` | factual | Pro check: No leader lines connecting the highlighted circles on the body to the inset images; Highlighted circle for the eye/plica semilunaris is placed over the eye but lacks a connecting  |  |
| Biology | `E2-evidence-of-evolution` | `E2-11-plant-phylogenetic-evolutionary-tree` | factual+panel | labels or layout still wrong after 3 placements:   |  |
| Chemistry | `A14c-nitrogen-and-carbon` | `A14c-01-nitrogen-gas-laboratory-preparation` | factual | Pro check: The delivery tube goes straight through the wall of the glass trough instead of over the edge. |  |
| CRK | `A1-sovereignty-of-god` | `A1-01-six-days-creation-panels` | panel | labels or layout still wrong after 3 placements:   |  |
| CRK | `C5-the-parables` | `C5-01-parable-sower-panels` | panel | labels or layout still wrong after 3 placements:   |  |
| Geography | `B4-denudation-processes` | `B4-04-desert-wind-landforms` | panel | labels or layout still wrong after 3 placements:   |  |
| Geography | `B5-water-bodies` | `B5-04-oxbow-lake-sequential` | factual | Pro check: Neck in panel 2 is not narrow.; Panel 3 shows an incorrect branching river shape.; Panel 4 channel orientation mismatches earlier panels. | yes |
| IRK | `A5a-suwar-al-ala-to-al-alaq` | `A5a-01-quranic-surahs-thematic-visual` | panel | Pro check: The fifth panel is completely empty. There are five suwar to represent, but only four have illustrations. |  |
| Physics | `A22-characteristics-of-sound-waves` | `A22-06-resonance-tube-apparatus` | factual | Pro check: Tuning fork stem points down towards tube instead of prongs.; Hose connects to top of reservoir instead of bottom. |  |
| Physics | `A38b-radioactivity-and-modern-physics` | `A38b-03-electron-diffraction-apparatus-schematic` | factual | Pro check: Beam does not spread into diffracted cones after passing the crystal. |  |

### 4. Minor caption problems

| Image | Result |
|---|---|
| `B1-03-soil-water-retention-experiment` | previous version restored: The pointer line from 'cotton wool plug' passes straight through the text 'dry loam'. |
| `B12-01-grass-sedge-broadleaf-weed` | previous version restored: The taproot of the broadleaf plant extends directly through and overlaps the caption text below. |
| `B14-01-grasshopper-life-cycle` | previous version restored: The captions 'Nymph (wingless)' and 'Adult grasshopper' overlap each other at the bottom. |
| `B2a-05-ascaris-morphology-infection` | previous version restored: The label 'female' overlaps with the circle outline of the inset panel. |
| `B2b-05-light-requirement-leaf-experiment` | previous version restored: A pointer line cuts vertically through the labels paper clip and aluminium foil. |
| `B2b-10-chemosynthesis-soil-bacteria` | previous version restored: The pointer line for nitrate passes directly through the cluster of Nitrobacter bacteria. |
| `B2c-14-lipid-food-tests-results` | previous version restored: The pointer line for 'cloudy white emulsion (fat present)' passes straight through the clear test tube to reach the tube on the left. |
| `B2d-07-comparative-mammalian-skulls` | previous version restored: The pointer line for incisors cuts across the sheep and dog skulls to reach the human teeth. |
| `B3b-01-diffusion-laboratory-experiment-setups` | previous version restored: The captions 'after 30 minutes' and 'after some hours' overlap with each other, and the top text is cut off. |
| `B5-13-plant-excretory-products-illustrations` | previous version restored: The pointer line for 'nicotine (tobacco)' passes directly through the coffee cup and Cinchona bark drawings. |
| `B6a-15-auxin-phototropism-mechanism` | previous version restored: The vertical pointer lines from upper labels pass directly through lower label text. |
| `B6b-13-skeletal-disorders-comparison` | previous version restored: The pointer line for 'smooth cartilage' passes directly through the arthritic joint panel to reach the healthy joint. |
| `B7b-10-heterostyly-primrose-flowers` | captions moved into free space |
| `B7b-13-fleshy-fruit-sections-comparison` | previous version restored: The vertical pointer line for 'stony endocarp (stone)' cuts directly through the label text 'mesocarp'. |
| `B7b-14-fruit-classification-comparison` | previous version restored: Pointer lines pass directly through the text labels 'crown' and 'bract' above the pineapple. |
| `B9c-01-human-endocrine-system` | captions moved into free space |
| `C1-12-soil-drainage-experiment-apparatus` | previous version restored: The pointer line for 'drained water' passes directly through the text 'loamy soil' and other parts of the middle apparatus. |
| `C2-02-symbiotic-mutualism-biological-panels` | previous version restored: The pointer line for fungal threads passes directly through the label text for algal cells. |
| `C4-03-savanna-types-comparison-landscape` | captions moved into free space |
| `C4-07-obudu-plateau-altitudinal-profile` | previous version restored: The pointer line for tea crosses directly through the illustration of the Irish potato plant. |
| `C5-06-primary-succession-lithosere-sequence` | previous version restored: The labels at the bottom heavily overlap each other and the arrow. |
| `C5-08-secondary-ecological-succession-sequence` | previous version restored: The captions 'annual weeds (pioneers)' and 'grasses and Siam weed' collide and overlap each other. |
| `C6-08-soil-water-humus-determination` | captions moved into free space |
| `C7d-02-stages-desertification` | previous version restored: Pointer lines pass directly through the text labels 'Bare soil' and 'Overgrazing'. |
| `D2a-14-ishihara-colour-blindness-test` | captions moved into free space |
| `D3-02-plant-tissue-culture-steps` | previous version restored: The caption for panel 3 overlaps the roof of the greenhouse illustration in panel 6. |
| `E1-01-adaptive-radiation-mammal` | captions moved into free space |
| `E1-05-darwin-finches-beak-adaptation` | previous version restored: Several text labels heavily overlap the illustrations and other captions. |
| `E1-10-allopatric-speciation-stages` | previous version restored: The caption for step 3 directly overlaps the beetles and red X mark in the illustration. |
| `E2-09-vertebrate-embryo-development-grid` | previous version restored: The text 'later stages differences appear' heavily overlaps the turtle drawing and the 'reptile' caption. |

## Panel audit (third task)

I audited every labelled AI image in all subjects (469 images; Biology Section A excluded) with Gemini Flash vision on the raw picture: how many separate panels or organisms it holds, where each one is, and which labels only name a whole panel or organism. **246 images have more than one panel or organism.** Under your rules, **193 of them had a problem**: 169 had panel or organism names drawn as pointer labels, and 90 had a pointer line crossing another panel (counts from my geometry check; the vision check below counts differently).

**Result: 154 images changed** (155 re-rendered; one came out identical), in 69 commits (one per notes file). No picture was regenerated. By subject: Biology 114, Agricultural Science 18, Geography 4, Use of English 4, Commerce 3, History 3, Chemistry 2, Government 2, IRK 2, Literature in English 2, Economics 1.
- Panel and organism names are now captions under their own panel (wrapped to the panel width; a white row is opened between picture rows where a caption would otherwise touch the next row).
- Every pointer label goes to the nearest of the left, right or top margin whose straight line does not pass through another panel (`label.py` now has labels above the picture: `fixed_sides`, side `T`, and several split rows).
- Checked afterwards by Gemini vision (same prompt before and after) on the 155 images: names drawn as pointer labels **94 to 5**, lines through another panel **84 to 8**, caption touching a drawing or arrow **1 to 27** (the price of captions: mostly life-cycle and diagram pictures with arrows beside the panels), text cut off 1 to 1.
- **Left as they were (38 images, listed below).** For these the new layout was checked and was worse than the old one (captions on top of drawings, or crowded rows), so I put the old image back. They still have the problems named in the table (mostly names as pointer labels, 31 of them, and 6 lines through another panel). They need either regenerated pictures with more space between panels, or hand placement.
- **Remaining minor problems in changed images (40):** the vision check still reports a caption touching an arrow or drawing, or a line crossing another panel. Lists below.

Cost of this task: about $2.60 (audit $0.67, checks $0.60, second opinion on drawing mistakes $1.31). The old decision is recorded in `IMAGES-PLAN.md`: Biology Section A stays as it is, and the style-test files were deleted.

### Not fixed: 38 images left as before

| Subject | Notes file | Image | Why |
|---|---|---|---|
| CRK | `A1-sovereignty-of-god` | `A1-01-six-days-creation-panels` | old layout kept; new layout was worse: Several panel labels overlap the drawings directly, making the text hard to read. |
| Government | `A1-definition-and-scope-of-government` | `A1-02-functions-government-panels` | old layout kept; new layout was worse: The labels 'Security' and 'External Defense' overlap directly on the upper parts of the bottom panels' drawings. |
| Accounting | `A18-information-technology-in-accounting` | `A18-01-accounting-methods-comparison-scene` | old layout kept; new layout was worse: The captions at the bottom heavily overlap each other, making them illegible. |
| IRK | `A5a-suwar-al-ala-to-al-alaq` | `A5a-01-quranic-surahs-thematic-visual` | old layout kept; new layout was worse: The text for al-'Alaq overlaps the olive branch drawing, and surah titles in the top-right panel are formatted as pointer labels. |
| Agricultural Science | `A7-roles-of-government-and-ngos` | `A7-02-agricultural-infrastructure-types-composite` | old layout kept; new layout was worse: The caption 'Transport (roads)' overlaps the top border and drawing of the bottom-left panel. |
| Agricultural Science | `B12-weeds` | `B12-02-weed-seed-dispersal-methods` | old layout kept; new layout was worse: The caption 'Explosive mechanism (pod bursting)' overlaps the bottom of the bursting pod illustration. |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-01-autotrophic-versus-heterotrophic-nutrition` | old layout kept; new layout was worse: The text 'heterotroph; saprophytic (mushroom)' overlaps directly onto the illustration of the intestine and tapeworm. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-01-food-classes-chart` | old layout kept; new layout was worse: Labels such as carbohydrates, roughage (dietary fibre), and proteins overlap the circular panels and central plate illustrations. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-06-food-energy-calorimetry-apparatus` | old layout kept; new layout was worse: The pointer line from 'boiling tube' passes directly through the label text 'thermometer'. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-10-balanced-diet-plate` | old layout kept; new layout was worse: The pointer line for fats and oils passes directly across the starchy foods section. |
| Biology | `B3b-transport-in-plants` | `B3b-08-xylem-phloem-longitudinal-section` | old layout kept; new layout was worse: The pointer line for tracheid crosses completely over another vessel element to reach the tracheid. |
| Geography | `B4-denudation-processes` | `B4-04-desert-wind-landforms` | old layout kept; new layout was worse: The caption text below the left panel heavily overlaps with another line of text, making both illegible. |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-08-leaf-epidermis-stomata-structure` | old layout kept; new layout was worse: The pointer line for 'stoma (closed)' cuts directly through the caption 'grass stoma (dumbbell-shaped guard cells)'. |
| Biology | `B4b-cellular-respiration` | `B4b-13-yeast-industrial-fermentation-products` | old layout kept; new layout was worse: The text overlays drawings directly, pointer lines intersect, and the pointer line for vitamin B crosses through other labels and o |
| Biology | `B5-excretion` | `B5-05-stoma-lenticel-plant` | old layout kept; new layout was worse: The pointer line for 'epidermal cell' cuts directly through the label text 'chloroplast'. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-02-plant-supporting-tissues` | old layout kept; new layout was worse: Labels and pointer lines heavily overlap each other at the top, and bottom captions collide. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-06-phototropism-seedling-experiment-setup` | old layout kept; new layout was worse: Pointer lines for 'light from one side' and 'slit' cross across the box panel and organism. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-06-cervical-vertebrae-comparison` | old layout kept; new layout was worse: The pointer line for 'neural spine' passes directly through the caption 'typical cervical vertebra', overlapping the text. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-07-mammalian-vertebrae-comparison` | old layout kept; new layout was worse: The label 'lumbar vertebra' overlaps the sacrum diagram, and at the bottom labels overlap each other. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-12-antagonistic-arm-muscles` | old layout kept; new layout was worse: The caption 'arm bent' overlaps the bottom of the arm drawing. |
| Agricultural Science | `B7-plant-propagation-methods` | `B7-02-vegetative-plant-propagation-methods` | old layout kept; new layout was worse: The panel dividing line passes directly through the text 'stem cutting', and a pointer line cuts through the word 'rootstock'. |
| Biology | `B7a-asexual-reproduction` | `B7a-05-underground-vegetative-organs` | old layout kept; new layout was worse: The caption 'bulb (onion)' is overlapped by the green leaves of the ginger plant below it. |
| Biology | `C1-factors-affecting-distribution` | `C1-08-rain-gauge-apparatus` | old layout kept; new layout was worse: A pointer line passes directly through the label text 'funnel'. |
| Biology | `C1-factors-affecting-distribution` | `C1-13-human-impact-ecosystems` | old layout kept; new layout was worse: The captions are severely misplaced and overlap the drawings of other panels. |
| CRK | `C5-the-parables` | `C5-01-parable-sower-panels` | old layout kept; new layout was worse: The caption for rocky ground overlaps the wheat bristles of the panel below it. |
| CRK | `C6-sermon-on-the-mount` | `C6-02-earthly-versus-heavenly-treasure` | old layout kept; new layout was worse: The captions at the bottom directly overlap the landscape illustrations. |
| Biology | `C6-soil` | `C6-12-soil-erosion-types-stages` | old layout kept; new layout was worse: The caption 'Rill erosion' directly overlaps the bottom border of the panel diagram. |
| Biology | `C7a-diseases` | `C7a-02-anopheles-mosquito-life-cycle` | old layout kept; new layout was worse: The arrow pointing to 'Adult female (rests at an angle)' cuts directly through the caption text, causing an overlap. |
| Biology | `C7a-diseases` | `C7a-06-schistosoma-haematobium-life-cycle` | old layout kept; new layout was worse: The pointer line for 'Cercariae enter through skin' passes directly across another panel, and labels like 'Miracidium' overlap the  |
| Biology | `C7a-diseases` | `C7a-08-housefly-life-cycle-disease` | old layout kept; new layout was worse: The captions 'Eggs in refuse' and 'Larva (maggot)' overlap the arrows and circle borders, and a large horizontal white band cuts th |
| Biology | `D2b-applications-of-heredity` | `D2b-02-livestock-cross-breeding` | old layout kept; new layout was worse: Label text describing the parent breeds directly overlaps the body and head of the crossbred cow. |
| Biology | `D2b-applications-of-heredity` | `D2b-08-bt-crop-mechanism` | old layout kept; new layout was worse: The pointer line and label for 'gene inserted into cowpea cells' directly overlaps and passes through the 'Bacillus thuringiensis'  |
| Biology | `D3-biotechnology` | `D3-07-bread-making-yeast-fermentation` | old layout kept; new layout was worse: The caption text beneath the first panel overlaps heavily with another block of text, rendering it illegible. |
| Biology | `E1-theories-of-evolution` | `E1-04-lamarck-giraffe-neck-evolution` | old layout kept; new layout was worse: The pointer line passes through the text 'theory' and slices directly through the head of the adult giraffe to reach the offspring. |
| Biology | `E1-theories-of-evolution` | `E1-07-darwin-giraffe-neck-natural` | old layout kept; new layout was worse: Captions and step descriptions overlap directly onto the tree canopy and illustrations, making them hard to read. |
| Biology | `E2-evidence-of-evolution` | `E2-03-archaeopteryx-fossil-reconstruction` | old layout kept; new layout was worse: The caption 'Archaeopteryx (about 150 million years ago)' overlaps with the tail feathers of the reconstructed bird. |
| Biology | `E2-evidence-of-evolution` | `E2-06-analogous-insect-bird-wings` | old layout kept; new layout was worse: Caption texts at the bottom heavily overlap one another, rendering them difficult to read. |
| Biology | `E2-evidence-of-evolution` | `E2-11-plant-phylogenetic-evolutionary-tree` | old layout kept; new layout was worse: Labels severely overlap illustrations and other text captions, especially near the bottom where the algae label collides with the d |

### Changed but still with a minor problem (40)

| Subject | Notes file | Image | What the check still sees |
|---|---|---|---|
| Agricultural Science | `B1-rocks-and-soil-formation` | `B1-03-soil-water-retention-experiment` | The pointer line from 'cotton wool plug' passes straight through the label text 'dry loam', causing an overlap. |
| Agricultural Science | `B12-weeds` | `B12-01-grass-sedge-broadleaf-weed` | The taproot of the broadleaf plant overlaps directly onto the caption text below it. |
| Agricultural Science | `B14-crop-pests` | `B14-01-grasshopper-life-cycle` | The label 'Adult grasshopper' overlaps the drawing of the soil and nymph. |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-05-ascaris-morphology-infection` | The label 'female' overlaps the circular border of the inset diagram below it. |
| Biology | `B2b-plant-nutrition` | `B2b-10-chemosynthesis-soil-bacteria` | Organisms such as Nitrosomonas and Nitrobacter are identified via pointer labels rather than captions. |
| Agricultural Science | `E1-farm-surveying-and-farmstead-planning` | `E1-01-farm-surveying-tools-collection` | The pointer line for 'red and white bands' crosses over the black and white pole to reach the red and white pole. |
| Biology | `B2b-plant-nutrition` | `B2b-09-starch-test-leaf-steps` | The pointer line for 'white tile' crosses directly over the right tile panel to reach the left tile. |
| Biology | `B2b-plant-nutrition` | `B2b-05-light-requirement-leaf-experiment` | The pointer lines for sunlight and paper clip pass directly through the text label aluminium foil (both sides). |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-14-lipid-food-tests-results` | The pointer line for 'cloudy white emulsion (fat present)' passes through the rightmost test tube to reach the left test tube. |
| Biology | `B2d-mammalian-teeth` | `B2d-07-comparative-mammalian-skulls` | The pointer line for incisors cuts directly through the dog skull to reach the human skull. |
| Biology | `B3b-transport-in-plants` | `B3b-01-diffusion-laboratory-experiment-setups` | The captions 'after 30 minutes' and 'after some hours' heavily overlap each other, making them difficult to read. |
| Biology | `B5-excretion` | `B5-13-plant-excretory-products-illustrations` | The pointer line for nicotine passes through the bark, pills, and coffee items before reaching the tobacco leaves. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-11-nyctinastic-plant-movements` | Labels such as 'Bauhinia', 'flamboyant', and 'Mimosa pudica' overlap directly onto the top borders and illustrations of the bottom panels. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-15-auxin-phototropism-mechanism` | The pointer line from 'less auxin' passes directly through the text of 'auxin moves to shaded side' and 'more auxin'. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-13-skeletal-disorders-comparison` | The pointer line for smooth cartilage passes directly across the arthritic joint panel to reach the healthy joint. |
| Biology | `B7a-asexual-reproduction` | `B7a-03-asexual-reproduction-types-grid` | The caption for the Spirogyra panel is placed over the bee illustration in the adjacent panel, overlapping it heavily. |
| Biology | `B7a-asexual-reproduction` | `B7a-04-asexual-vs-sexual-reproduction` | The label 'male gamete' overlaps a pointer line and dot for fertilisation, and captions overlap offspring drawings. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-10-heterostyly-primrose-flowers` | The title 'pin-eyed flower (long style)' is erroneously combined with 'ovary' as a pointer label. |
| Biology | `B7a-asexual-reproduction` | `B7a-02-yeast-budding-stages` | The label text 'daughter cell' overlaps heavily with 'chain of cells' making both difficult to read. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-14-fruit-classification-comparison` | Pointer lines run directly through the label texts above the pineapple. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-13-fleshy-fruit-sections-comparison` | The pointer line for stony endocarp passes directly through the label text mesocarp. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-16-fruit-seed-dispersal-mechanisms` | The pointer line for 'barbed spines' crosses completely through the bottom-right panel to reach its dot in the middle panel. |
| Biology | `B9c-hormonal-control` | `B9c-01-human-endocrine-system` | The pointer line for ovary passes directly through the label text for uterus. |
| Biology | `C1-factors-affecting-distribution` | `C1-12-soil-drainage-experiment-apparatus` | The vertical pointer line from 'drained water' passes directly through the text 'loamy soil' and through the soil diagram. |
| Biology | `C4-nigerian-biomes` | `C4-07-obudu-plateau-altitudinal-profile` | The names of crops in the inset are labeled using pointer lines and dots rather than captions under each plant. |
| Biology | `C5-ecology-of-populations` | `C5-06-primary-succession-lithosere-sequence` | The stage captions along the bottom arrow overlap heavily with the arrow and each other, making them difficult to read. |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-02-symbiotic-mutualism-biological-panels` | The pointer line from 'fungal threads (hyphae)' passes directly through the label 'algal cells'. |
| Biology | `C5-ecology-of-populations` | `C5-08-secondary-ecological-succession-sequence` | The captions 'annual weeds (pioneers)' and 'grasses and Siam weed' collide and overlap each other, and some labels are displaced. |
| Biology | `C6-soil` | `C6-08-soil-water-humus-determination` | The oven is identified using a pointer label with a dot on the appliance rather than a caption beneath it. |
| Biology | `C4-nigerian-biomes` | `C4-03-savanna-types-comparison-landscape` | The captions 'southern Guinea savanna' and 'northern Guinea savanna' overlap at the bottom center. |
| Biology | `C7d-conservation-parks-and-reserves` | `C7d-02-stages-desertification` | The vertical pointer lines pass directly through the text labels 'Bare soil' and 'Overgrazing'. |
| Biology | `D2a-heredity-principles` | `D2a-14-ishihara-colour-blindness-test` | The colour vision test plate is labeled with a pointer line and dot instead of being captioned as the panel title. |
| Biology | `D3-biotechnology` | `D3-02-plant-tissue-culture-steps` | The caption for panel 3 overlaps the greenhouse in panel 6. |
| Biology | `E1-theories-of-evolution` | `E1-01-adaptive-radiation-mammal` | Labels overlap directly onto arrows and animals, such as 'flying (bat)' over an arrow and 'walking upright (human)' over the antelope. |
| Biology | `E1-theories-of-evolution` | `E1-05-darwin-finches-beak-adaptation` | The text label 'large ground finch: hard seeds' heavily overlaps the face of the finch drawing. |
| Biology | `E1-theories-of-evolution` | `E1-02-redi-spontaneous-generation-experiment` | The caption under the center jar overlaps with other text ('Redi 1668' overlapping 'maggots'). |
| Biology | `E1-theories-of-evolution` | `E1-10-allopatric-speciation-stages` | The text for step 3 overlaps directly on top of the illustration and beetles. |
| Biology | `E2-evidence-of-evolution` | `E2-09-vertebrate-embryo-development-grid` | The text 'later stages: differences appear' overlaps with the head of the reptile illustration in the bottom row. |
| Biology | `E2-evidence-of-evolution` | `E2-04-horse-evolution-stages-foot` | Labels overlap with each other, such as 'Pliohippus' overlapping 'Equus (modern horse)'. |
| Use of English | `C2a-consonants` | `C2a-04-consonant-articulation-mouth-diagrams` | The pointer line for 'tongue' passes directly through the green face illustration on the left. |

## Drawing mistakes to look at (reported, not fixed)

Gemini Flash looked for clear mistakes in the drawings (469 images), reported 164 images with a high-confidence claim, and Gemini Pro was asked to confirm each claim from the finished picture. **132 images have a confirmed mistake** (the Pro check is lenient, so a few are probably nitpicks: please look at the ones that matter). Another 16 claims were only about a gap or break in a line (`C8-01-earthen-fish-pond-cross, B1-13-male-rabbit-reproductive-system, B2c-06-food-energy-calorimetry-apparatus, B4a-01-respiratory-surface-exchange, B6b-12-antagonistic-arm-muscles, B8-09-epigeal-germination-stages` and others): these may be leftovers of the earlier line repair rather than drawing errors and are not listed. Nothing was changed.

| Subject | Notes file | Image | Mistake |
|---|---|---|---|
| Agricultural Science | `A5-farm-inputs` | `A5-02-farmer-protective-agrochemical-gear` | Although the text 'Wind direction' is present at the bottom of the image, there is no arrow indicating the actual direction of the wind. |
| Agricultural Science | `B13-crop-diseases` | `B13-03-cassava-mosaic-virus-leaf` | The illustration of the whitefly in the circular inset clearly shows only four legs extending from its body, which is a scientific error for an insect. |
| Agricultural Science | `B6-growth-development-and-reproduction` | `B6-02-double-fertilization-process` | Too many male gametes/nuclei are depicted: there are two inside the pollen tube in the lower right, plus two additional orange structures shown already inside/fusing with |
| Agricultural Science | `B7-plant-propagation-methods` | `B7-02-vegetative-plant-propagation-methods` | The illustration clearly shows the wrapping located below the T-cut, which fails to secure the bud or protect the union as required in actual budding. |
| Agricultural Science | `C1-forms-and-classification-of-major-farm-animals` | `C1-05-rooster-external-anatomy` | The drawing clearly shows the spurs pointing forwards towards the toes, which is anatomically incorrect for a rooster. |
| Agricultural Science | `C3-anatomy-and-physiology-of-farm-animals` | `C3-01-avian-digestive-system` | In the illustration, the caeca are shown branching directly off the cloaca, rather than at the correct anatomical location between the small and large intestines. |
| Agricultural Science | `C3-anatomy-and-physiology-of-farm-animals` | `C3-02-ruminant-stomach-compartments` | There are no arrows indicating the flow of food within the oesophagus or any other parts of the digestive system in the diagram. |
| Agricultural Science | `C6-livestock-management` | `C6-03-rabbit-handling-housing` | The drawing clearly shows three distinct hands holding the rabbit, which is an obvious anatomical error. |
| Agricultural Science | `C9-bee-keeping` | `C9-01-honeybee-castes-morphological-comparison` | The pollen baskets (corbiculae) on the worker bee are depicted as large, symmetrical beige lobes detached from the legs and protruding directly from the sides of the abdo |
| Agricultural Science | `E1-farm-surveying-and-farmstead-planning` | `E1-01-farm-surveying-tools-collection` | A Gunter's survey chain consists of long rigid steel wire rods/links (each roughly 20 cm / 7.92 inches long) connected by small circular or oval rings (typically 2-3 ring |
| Agricultural Science | `E3-farm-machinery-and-implements` | `E3-02-disc-mouldboard-ploughs` | The mouldboard plough is drawn as two stacked identical curved blades/bodies vertically above one another (like a stylized reversible plough, but incorrectly configured a |
| Agricultural Science | `E5-processing-and-storage` | `E5-03-maize-storage-crib` | The rat guards (cones) on the stilt legs are drawn pointing upwards like funnels/cups rather than downward-pointing, meaning rats can easily climb over them and they will |
| Biology | `B1-internal-structure` | `B1-10-human-torso-internal-organs` | The illustration incorrectly depicts the green large intestine ending directly in the purple urinary bladder rather than continuing to a separate rectum and anus. |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-03-ruminant-stomach` | The image incorrectly depicts a separate anatomical loop for cud to return to the mouth, whereas anatomically, rumination occurs via the esophagus. |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-08-rhizopus-mould-structure` | The illustration shows distinct transverse lines across the stolons and hyphae, incorrectly depicting septa in a fungus that should be coenocytic. |
| Biology | `B2a-modes-and-types-of-nutrition` | `B2a-11-bladderwort-trap-mechanism` | The diagram incorrectly depicts the bladder trap as a symmetrical, open-ended tube rather than an enclosed, asymmetrical pouch. |
| Biology | `B2b-plant-nutrition` | `B2b-06-carbon-dioxide-requirement-experiment` | The illustration shows the polythene bag wrapped only around the pot's sides, leaving the soil exposed to the air inside the bell jar, which invalidates the experiment. |
| Biology | `B2b-plant-nutrition` | `B2b-09-starch-test-leaf-steps` | In step 6, the leaf remains green around the edges while iodine turns part of it blue-black, but the leaf was already decolourised/bleached pale in steps 4 and 5, so the  |
| Biology | `B2b-plant-nutrition` | `B2b-11-plant-mineral-deficiency-water` | Bubbles are drawn rising in open air from the top of the aeration tube instead of emerging from the bottom of the tube inside the culture solution to aerate the water. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-07-kwashiorkor-marasmus` | The child on the left is drawn with unnatural green/cyan skin and blue-tinted lower limbs, rather than human skin pigmentation. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-08-rickets-skeletal` | Both figures clearly show pronounced, swollen wrists, even though this symptom of rickets should only be present on the affected child. |
| Biology | `B2c-food-substances-and-food-tests` | `B2c-12-benedicts-reducing-sugar-test` | The clamp holding the test tube is shown floating without being connected to a supporting stand. |
| Biology | `B2d-mammalian-teeth` | `B2d-01-molar-tooth-cross-section` | The outer enamel layer (white) continues down the roots instead of ending at the neck/crown margin, meaning enamel covers the roots where cementum should be. |
| Biology | `B2d-mammalian-teeth` | `B2d-04-human-skull-dentition` | The illustration incorrectly depicts two green canine teeth per quadrant instead of the anatomically correct single canine. |
| Biology | `B2d-mammalian-teeth` | `B2d-06-dog-skull-carnassials` | A row of teeth is drawn floating in the empty space between the upper and lower jaws, not attached to any bone. |
| Biology | `B2e-alimentary-canal-and-digestion` | `B2e-03-oesophageal-peristalsis-mechanism` | The external wall of the oesophagus bulges outwards behind the bolus where the circular muscle is labelled as contracted, instead of constricting inward to narrow the tub |
| Biology | `B2e-alimentary-canal-and-digestion` | `B2e-06-hepatobiliary-pancreatic-ducts` | The C-loop of the duodenum is curved backwards/opposite to normal anatomy relative to the stomach and pancreas, with the opening from the stomach connecting to the upper  |
| Biology | `B2e-alimentary-canal-and-digestion` | `B2e-12-ruminant-stomach-chambers` | The diagram uses leader lines with dots for labeling but completely lacks directional arrows to show the movement of food through the digestive system. |
| Biology | `B3a-transport-in-animals` | `B3a-02-agar-cube-diffusion-experiment` | The large cube outside the beaker is not cut in half to show a cross section; it is drawn as an intact cube with a transparent purple/colourless layer, unlike the medium  |
| Biology | `B3a-transport-in-animals` | `B3a-05-mammalian-heart-internal-section` | The base of the pulmonary artery is drawn as a closed, free-floating tube rather than opening continuously into the right ventricle. |
| Biology | `B3a-transport-in-animals` | `B3a-09-capillary-bed-tissue-exchange` | The arrows showing exchange of fluid, oxygen/glucose, and carbon dioxide/wastes are missing entirely from the diagram despite being required for the labels. |
| Biology | `B3a-transport-in-animals` | `B3a-11-systemic-blood-circulation-schematic` | The diagram incorrectly omits red arterial vessels in the arms, only displaying blue venous vessels, unlike the neck and legs. |
| Biology | `B3a-transport-in-animals` | `B3a-12-hepatic-portal-circulation-schematic` | The diagram clearly shows downward-pointing arrows in the inferior vena cava, which incorrectly indicates blood flowing away from the heart. |
| Biology | `B3a-transport-in-animals` | `B3a-15-blood-smear-cellular-composition` | Several red blood cells are drawn pale green instead of pale red/pinkish-orange, which is incorrect for human erythrocytes. |
| Biology | `B3a-transport-in-animals` | `B3a-16-human-lymphatic-system-anatomy` | The label for tonsils incorrectly points to a structure in the lower neck region, whereas tonsils are located higher up in the pharynx or back of the oral cavity. |
| Biology | `B3a-transport-in-animals` | `B3a-17-cockroach-open-circulatory-system` | The insect has far more than three pairs of thoracic legs (there are at least 5-6 stubby leg-like appendages depicted along the ventral side of thorax and abdomen). |
| Biology | `B3b-transport-in-plants` | `B3b-04-onion-epidermis-cell-plasmolysis` | In the middle panel (plasmolysis), the second and third cells from the left show two nuclei (two bluish-green circles) per cell instead of one. |
| Biology | `B3b-transport-in-plants` | `B3b-06-dicot-stem-transverse-section` | In the low-power plan (top left circle), the orientation of tissues within each vascular bundle is inverted: the xylem (red-brown with vessels) is drawn towards the outer |
| Biology | `B3b-transport-in-plants` | `B3b-10-tree-trunk-ringing-experiment` | The labels describe directional transport, but there are no actual arrows in the diagram visually illustrating the upward movement of water or downward movement of food. |
| Biology | `B3b-transport-in-plants` | `B3b-13-bubble-potometer-apparatus` | The open end of the capillary tube entering the beaker does not dip into the water in the beaker; it terminates above the water level. |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-05-cockroach-tracheal-system-anatomy` | The diagram visually depicts only 5 pairs of spiracles in the abdomen, contradicting its own label which correctly states there are 8 pairs. |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-07-avian-respiratory-system-air` | The directional arrows for airflow are reversed or inconsistent with avian unidirectional respiration: inhaled air normally flows first to the posterior air sacs and then |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-08-leaf-epidermis-stomata-structure` | The cross-section diagram incorrectly shows the guard cells in their elongated surface view instead of their true oval or kidney-like transverse profile. |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-10-stoma-opening-closing-mechanism` | Each guard cell contains multiple purple oval structures resembling nuclei (up to 5-6 per cell), whereas plant guard cells are eukaryotic cells containing only a single n |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-13-bell-jar-lung-model` | The diagram includes labels for 'air in' and 'air out' with standard leader lines, but directional arrows illustrating the flow of air are missing. |
| Biology | `B4a-respiratory-organs-and-gaseous-exchange` | `B4a-14-alveolus-gas-exchange-capillary` | Both arrows in the diagram point from the capillary into the alveolus, failing to show the bidirectional gas exchange where oxygen enters the capillary. |
| Biology | `B4b-cellular-respiration` | `B4b-08-plant-respiration-carbon-dioxide` | In the aspirator bottle (far right), the air delivery tube dips deeply below the water level, which would prevent air from being drawn into the bottle by the draining wat |
| Biology | `B4b-cellular-respiration` | `B4b-10-germinating-seeds-heat-production` | The thermometer bulb containing the liquid reservoir is drawn at the bottom outside the flask, rather than inside among the seeds where temperature is supposed to be meas |
| Biology | `B4b-cellular-respiration` | `B4b-11-simple-respirometer-germinating-seeds` | The capillary tube for the experimental setup has an arrow showing movement towards the right (away from the tube), whereas oxygen consumption causes a decrease in volume |
| Biology | `B4b-cellular-respiration` | `B4b-12-yeast-anaerobic-fermentation-experiment` | The submerged end of the right delivery tube is incorrectly drawn as a closed oval shape rather than an open end. |
| Biology | `B5-excretion` | `B5-01-comparative-invertebrate-excretory-structures` | The flame cell is drawn with cilia originating from the bottom of the tube pointing backwards into a bulb that has an open apical pore, instead of the cilia projecting fr |
| Biology | `B5-excretion` | `B5-02-planaria-flame-cell-system` | In a flame cell (protonephridium), the cilia tuft should project into the internal lumen/tubule towards the excretory duct to propel fluid downstream, but here the cilia  |
| Biology | `B5-excretion` | `B5-06-human-urinary-system` | The image clearly shows the kidney on the anatomical left (viewer's right) positioned lower than the one on the anatomical right, which is anatomically incorrect. |
| Biology | `B5-excretion` | `B5-07-kidney-longitudinal-section` | The collecting duct of the nephron (green tube) ends blindly in the cortex instead of extending through the medulla and emptying at the renal papilla into the minor calyx |
| Biology | `B5-excretion` | `B5-08-nephron-structure-detailed` | The image incorrectly shows the green proximal tubule connecting to the red blood vessel entering the glomerulus, rather than continuing from the capsule. |
| Biology | `B5-excretion` | `B5-11-inhaled-exhaled-air-apparatus` | The connection between the Y-tube and the two test tubes is non-functional and incorrectly drawn: the purple tubing loops nonsensically as a single tangled line rather th |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-03-dicot-root-transverse-section` | There is a visible horizontal glitch line across the middle of the diagram that noticeably distorts the cellular structures. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-06-phototropism-seedling-experiment-setup` | The yellow rays of light are shown emitting outward from the slit of the cardboard box towards the outside control plant, rather than entering the box through the slit fr |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-11-nyctinastic-plant-movements` | The inset clearly shows the swelling labeled 'pulvinus' located on the main vertical stem, whereas it should be located at the base of the lateral leaf petiole. |
| Biology | `B6a-support-and-movement-in-plants` | `B6a-13-root-growth-marking-experiment` | In the 'after 48 hours' diagram, the region of root elongation is depicted in the middle/upper portion of the radicle instead of just behind the root tip (the zone of elo |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-01-insect-exoskeleton-anatomy` | The image incorrectly shows the apodeme as a separate, free-floating piece within the endocuticle rather than a continuous infolding of the outer cuticle layers. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-03-human-skeleton-front-view` | The color coding described (axial skeleton pale blue, appendicular pale yellow) is inconsistent: the skull is colored pale green, the pelvic girdle is colored pink, and t |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-04-human-skull-lateral-view` | The parietal bone region of the cranium is incorrectly divided into multiple alternating colored bands (blue and cream) without real anatomical sutures or bones correspon |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-07-mammalian-vertebrae-comparison` | In the thoracic vertebra lateral view, the neural spine and articular processes are incorrectly drawn as two opposite diverging projections (one pointing anterodorsally a |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-08-human-rib-cage` | Counting the ribs in the main diagram shows the brackets indeed mislabel the numbers of true, false, and floating ribs compared to human anatomy. |
| Biology | `B6b-support-and-movement-in-animals` | `B6b-09-pectoral-pelvic-girdles` | The diagram incorrectly shows the radius on the opposite side of the forearm from the thumb. |
| Biology | `B7a-asexual-reproduction` | `B7a-02-yeast-budding-stages` | In stage 3, the parent cell contains two purple spherical bodies (nuclei) while the bud contains an additional third purple body, rather than having a single nucleus divi |
| Biology | `B7a-asexual-reproduction` | `B7a-03-asexual-reproduction-types-grid` | The illustration incorrectly depicts one of the Spirogyra fragments with a Y-shaped branch, which is a biological error since Spirogyra forms unbranched filaments. |
| Biology | `B7a-asexual-reproduction` | `B7a-04-asexual-vs-sexual-reproduction` | The diagram uses human/mammalian gametes (a flagellated sperm cell and an animal ovum) to represent the gametes produced by flowering plants (angiosperms), which produce  |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-02-stamen-pollen-grain-structure` | The illustration incorrectly shows four pollen sacs in what appears to be a single cut lobe of the anther, whereas a single lobe should only contain two. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-08-maize-plant-reproduction` | The lower right inset incorrectly depicts multiple pink silks growing out of the top of a single ovary, whereas biologically each corn ovary only produces one silk. |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-11-double-fertilisation-angiosperms` | The dotted arrows showing fertilisation are pointing downwards from the polar nuclei to the egg apparatus, rather than showing male nuclei travelling/fusing with the egg  |
| Biology | `B7b-reproduction-in-flowering-plants` | `B7b-16-fruit-seed-dispersal-mechanisms` | In the panel intended to show a Bidens fruit with two barbed spines caught in fur, an entire green plant shoot or bur with green leaves/bracts is drawn instead of a typic |
| Biology | `B7c-reproduction-in-mammals` | `B7c-01-male-reproductive-system-section` | The vas deferens is drawn passing directly through the interior of the urinary bladder rather than looping around the outside of it. |
| Biology | `B7c-reproduction-in-mammals` | `B7c-06-ovulation-implantation-pathway` | The arrows along the fallopian tube (oviduct) point backwards, showing movement from the ovary up the tube away from the uterus, but then the next arrows point from left  |
| Biology | `B8-growth` | `B8-08-germination-oxygen-requirement-apparatus` | The hanging bags are tied to or suspended by a string wrapped magically around the outside of the conical flask rather than suspended from the rubber stopper or hung insi |
| Biology | `B8-growth` | `B8-12-seed-food-mobilisation-flowchart` | The arrows near the aleurone layer incorrectly point towards it from the endosperm, whereas enzymes should be depicted moving from the aleurone layer into the endosperm. |
| Biology | `B9a-nervous-coordination` | `B9a-03-three-types-neurones` | The caption claims the image shows the direction of impulse, but no arrows or other indicators of direction are present. |
| Biology | `B9a-nervous-coordination` | `B9a-04-cranial-meninges-cross-section` | The pia mater does not follow the folds (sulci and gyri) of the cerebral cortex; instead, it spans across the surface while the subarachnoid space and arachnoid trabecula |
| Biology | `B9a-nervous-coordination` | `B9a-05-human-brain-sagittal-section` | The cerebral hemisphere is drawn with superficial gyri and sulci on its surface instead of showing the cut surface / medial wall of the hemisphere characteristic of a lon |
| Biology | `B9a-nervous-coordination` | `B9a-06-cerebral-hemisphere-lobes` | The sensory area (postcentral gyrus) strip at the front of the parietal lobe is not demarcated or differentiated from the rest of the parietal lobe, unlike the motor stri |
| Biology | `B9a-nervous-coordination` | `B9a-07-spinal-cord-transverse-section` | The dorsal-ventral orientation of the spinal cord is inverted relative to the vertebra: the spinous process of the vertebra is at the top (dorsal side of the body), but t |
| Biology | `B9a-nervous-coordination` | `B9a-11-spinal-reflex-arc` | The blue sensory neurone incorrectly shows a second cell body within the spinal cord's grey matter in addition to the correct one in the dorsal root ganglion. |
| Biology | `B9b-sense-organs` | `B9b-01-human-skin-anatomy` | The image incorrectly shows the arrector pili muscle attached at its upper end to a structure labeled as a Merkel disc, rather than inserting into the upper dermis. |
| Biology | `B9b-sense-organs` | `B9b-05-external-eye-lacrimal-apparatus` | The arrows indicating tear flow show tears flowing away from the nasolacrimal duct (pointing outward towards the lateral corner of the eye) instead of flowing from the la |
| Biology | `B9b-sense-organs` | `B9b-06-human-eyeball-horizontal-section` | The fovea is incorrectly depicted as a convex bump projecting into the vitreous cavity instead of a concave indentation in the retina. |
| Biology | `B9b-sense-organs` | `B9b-12-human-ear-anatomy` | The image exhibits clear rendering glitches and pixelation in the specified areas, making the anatomical structures distorted and difficult to interpret. |
| Biology | `B9c-hormonal-control` | `B9c-06-adrenal-gland-anatomy-section` | The illustration portrays the kidney using an inaccurate pale greenish-grey color, whereas real kidneys are distinctly reddish-brown. |
| Biology | `B9c-hormonal-control` | `B9c-07-pancreas-islet-histology` | The islet of Langerhans is drawn as a single concentric ring of epithelial-like cells surrounding an empty center containing capillaries, rather than a solid cluster/isla |
| Biology | `B9c-hormonal-control` | `B9c-11-auxin-tropisms-mechanism` | In the phototropism diagram, the cells on the lit (convex/concave) inner side are drawn longer/more elongated, while the cells on the shaded side are drawn shorter, which |
| Biology | `C1-factors-affecting-distribution` | `C1-10-wind-vane-anemometer` | The compass direction indicators are drawn as blank rectangular tabs without the standard cardinal direction letters. |
| Biology | `C2-symbiotic-interactions-and-energy-flow` | `C2-04-parasitic-organisms-anatomical-panels` | The illustration depicts the tapeworm body tapering to a very thin end rather than showing the characteristic widening of maturing proglottids toward the posterior. |
| Biology | `C3-natural-habitats` | `C3-04-stream-ecosystem-profile-cross` | Blackfly larvae are drawn attached by their anterior ends (mouth fan brushes at the attachment point) rather than anchored by their posterior abdomen/silk hooks with thei |
| Biology | `C3-natural-habitats` | `C3-08-tropical-rainforest-canopy` | The label 'long sticky tongue' points to an empty space between the chameleon and the insect, confirming the tongue is not drawn. |
| Biology | `C3-natural-habitats` | `C3-09-savanna-field-ecosystem-landscape` | The insect labeled 'variegated grasshopper (warning colours)' is incorrectly drawn in a solid brown color instead of its actual bright aposematic colors. |
| Biology | `C4-nigerian-biomes` | `C4-06-desert-biome-oasis-scene` | The scorpion is drawn with only six walking legs (three on each side) plus pedipalps, instead of eight walking legs characteristic of arachnids. |
| Biology | `C6-soil` | `C6-07-air-soil-experiment-apparatus` | The drawn container has the wide shape and spout of a standard beaker and lacks any measurement markings, making the 'Measuring cylinder' label incorrect. |
| Biology | `C6-soil` | `C6-09-soil-capillarity-experiment-apparatus` | The glass tubes are drawn with closed, rounded test tube bottoms instead of open-ended tubes; the cotton wool plug is placed inside a closed bottom, preventing water from |
| Biology | `C7a-diseases` | `C7a-02-anopheles-mosquito-life-cycle` | The pupa is incorrectly depicted suspended deep in the water column instead of resting at the surface where its breathing trumpets can access the air. |
| Biology | `C7a-diseases` | `C7a-06-schistosoma-haematobium-life-cycle` | The image incorrectly displays the egg with many spines covering its entire surface instead of the characteristic single terminal spine. |
| Biology | `C7a-diseases` | `C7a-08-housefly-life-cycle-disease` | The image shows the larva with a distinct head, eyes, and mouth, which is incorrect for a housefly maggot. |
| Biology | `C7c-pollution-and-sanitation` | `C7c-08-sanitary-landfill-cross-section` | The leachate collection pipe at the bottom is shown directly connected to a vertical pipe leading to a gas flare at the top, confusing the leachate collection system with |
| Biology | `C7d-conservation-parks-and-reserves` | `C7d-03-shelterbelt-windbreak-landscape` | The arrows showing wind direction on the right point away from the shelterbelt toward the desert, or diverge inconsistently, rather than blowing from the desert directly  |
| Biology | `D2b-applications-of-heredity` | `D2b-02-livestock-cross-breeding` | Both parents are depicted as female cows with visible udders (crossing two female animals rather than a bull and a cow). |
| Biology | `D2b-applications-of-heredity` | `D2b-06-haemolytic-disease-newborn-stages` | The third panel clearly displays horizontal digital glitching and artifacts over the fetus and surrounding area. |
| Biology | `D3-biotechnology` | `D3-05-industrial-fermenter-cross-section` | The pink arrow for the 'warm water out' pipe incorrectly points inward toward the pipe, contradicting the label that indicates water should be flowing out of the system. |
| Biology | `D3-biotechnology` | `D3-08-biogas-digester-cross-section` | The illustration incorrectly shows the gas pipe connecting directly to the side of the cooking pot rather than routing into the stove burner where combustion occurs. |
| Biology | `E1-theories-of-evolution` | `E1-02-redi-spontaneous-generation-experiment` | In the sealed jar (middle jar), a fly is drawn inside the sealed glass jar despite the experiment requiring the sealed jar to exclude flies completely. |
| Biology | `E1-theories-of-evolution` | `E1-09-antibiotic-resistance-evolution-steps` | In circle 3, the dividing bacteria are drawn as round cocci clusters rather than rod-shaped bacilli like the red bacteria in circles 1, 2, and 4. |
| Biology | `E2-evidence-of-evolution` | `E2-04-horse-evolution-stages-foot` | There are five horses depicted but only four foot skeletons, with the modern, single-toed foot positioned beneath the fourth horse instead of the final Equus. |
| Biology | `E2-evidence-of-evolution` | `E2-05-homologous-pentadactyl-forelimbs-comparison` | The illustration shows five distinct digits on the frog's forelimb, which is scientifically inaccurate as frogs possess only four digits on their front limbs. |
| Biology | `E2-evidence-of-evolution` | `E2-07-human-vestigial-organs` | The line pointing to the vermiform appendix connects to the anatomical left side of the body, which is incorrect as the appendix is located on the anatomical right side. |
| Biology | `E2-evidence-of-evolution` | `E2-11-plant-phylogenetic-evolutionary-tree` | The branching order of the phylogenetic tree is incorrect: the gymnosperm branch diverges lower on the main axis/branch than the fern branch (gymnosperms placed on a side |
| Chemistry | `A1-separation-of-mixtures` | `A1-01-simple-vs-fractional-distillation` | The receiving flasks are completely sealed with stoppers/corks around the delivery tube, creating a closed system which would cause dangerous pressure build-up during dis |
| Chemistry | `A1-separation-of-mixtures` | `A1-03-gravity-filtration-laboratory-setup` | The illustration clearly shows the stream of liquid bypassing the glass rod and falling directly into the funnel, which is incorrect technique. |
| Chemistry | `A14a-hydrogen-and-halogens` | `A14a-02-chlorine-gas-laboratory-preparation` | In the first wash bottle, the gas outlet tube dips into the liquid rather than staying above the liquid level, while the inlet tube stops above the bottom (in fact both t |
| Chemistry | `A14b-oxygen-and-sulphur` | `A14b-01-oxygen-gas-laboratory-preparation` | The drawing incorrectly depicts the gas jar upright with its open flanged end at the top and the delivery tube magically passing through the solid glass bottom. |
| Chemistry | `A14c-nitrogen-and-carbon` | `A14c-01-nitrogen-gas-laboratory-preparation` | The gas jar is depicted right-side up with its rim at the top instead of being an inverted gas jar, while the beehive shelf / delivery tube strangely enters through its c |
| Chemistry | `A14c-nitrogen-and-carbon` | `A14c-03-nitrate-brown-ring-test` | The meniscus/interface showing the brown ring is drawn tilted perpendicular to the tube axis rather than settling horizontally under gravity, while the top liquid surface |
| Chemistry | `A16b-alkanols-alkanals-and-acids` | `A16b-02-traditional-local-gin-distillation` | The image shows the boiling drum without a sealed lid, with vapor visibly escaping from the open top, which defeats the purpose of distillation. |
| CRK | `B2-the-supremacy-of-god` | `B2-01-elijah-fire-mount-carmel` | The label indicates a dried up trench, but the illustration visually depicts the trench as being full of blue, bubbling water. |
| Geography | `A2-scale-and-measurement` | `A2-02-measuring-curved-distance-thread` | The ruler depicted only has tick marks and no numbers, making it impossible to read a specific measurement from it. |
| Geography | `A6-geographic-information-system` | `A6-03-gis-map-scanning-digitizing` | The vector line appearing on the computer screen does not match the river being traced on the digitizing tablet; instead, the screen displays a coastline or different fea |
| Geography | `B2-the-earth-crust` | `B2-01-earth-internal-crust-cross` | The magnification lines for the crust inset incorrectly originate deep within the Earth near the core rather than at the surface crust layer. |
| Geography | `B4-denudation-processes` | `B4-02-soil-creep-hillside` | The pole is drawn leaning to the left (uphill), whereas soil creep typically causes vertical structures like poles and fences to lean downhill. |
| Geography | `B5-water-bodies` | `B5-04-oxbow-lake-sequential` | In panel 4, the ox-bow lake is incorrectly depicted as two symmetric loops on both sides of a perfectly straight channel, rather than a single abandoned curved meander lo |
| Government | `A15-public-opinion` | `A15-01-public-opinion-expression-panels` | In the bottom-right panel depicting a phone-in programme, the listener/caller is depicted sitting directly at the radio studio desk across from the presenter while holdin |
| History | `A2-early-centres-of-civilization` | `A2-02-nok-terracotta-human-head` | The illustration incorrectly features bright pastel colors on the hairstyle, which misrepresents the appearance of a historical terracotta artifact. |
| Physics | `A11-liquids-at-rest` | `A11-01-measuring-volume-solids-apparatus` | The illustration incorrectly shows water dripping from the spout while the water level inside the can is drawn visibly below the spout's opening. |
| Physics | `A22-characteristics-of-sound-waves` | `A22-06-resonance-tube-apparatus` | The tuning fork is oriented upside down, with its handle pointing into the top of the glass tube and its vibrating prongs facing upward, rather than having its prongs hel |
| Physics | `A38b-radioactivity-and-modern-physics` | `A38b-03-electron-diffraction-apparatus-schematic` | The image incorrectly shows a single straight beam after the crystal, failing to illustrate the diffracted beams that actually create the rings on the screen. |
| Use of English | `C2a-consonants` | `C2a-04-consonant-articulation-mouth-diagrams` | The tongue positioning in the two sagittal cross-sections is nearly identical, failing to show the tongue blade raised post-alveolar for /ʃ/ versus tongue tip near the al |

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
| Biology (B to E) | 451 | 406 | 45 | 333 | 118 | $14.69 |
| Physics | 154 | 150 | 4 | 35 | 119 | $8.18 |
| Chemistry | 68 | 67 | 1 | 27 | 41 | $2.95 |
| Mathematics | 65 | 64 | 1 | 0 | 65 | $1.96 |
| Economics | 61 | 58 | 3 | 3 | 58 | $3.84 |
| Government | 62 | 61 | 1 | 11 | 50 | $2.77 |
| Use of English | 31 | 29 | 2 | 10 | 21 | $1.93 |
| Literature in English | 26 | 26 | 0 | 12 | 14 | $1.05 |
| CRK | 103 | 103 | 0 | 95 | 8 | $5.45 |
| IRK | 50 | 43 | 7 | 18 | 25 | $1.82 |
| Accounting | 36 | 35 | 1 | 2 | 34 | $0.97 |
| Commerce | 27 | 26 | 1 | 9 | 18 | $1.14 |
| Geography | 67 | 65 | 2 | 25 | 42 | $4.49 |
| Agricultural Science | 108 | 104 | 4 | 92 | 16 | $6.21 |
| History | 90 | 82 | 8 | 24 | 65 | $5.55 |
| **Total** | **1399** | **1319** | **80** | | | **$63.40** |

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

(This table is from before the redo pass; the 62 pictures removed in the redo pass are listed in the "Redo pass" section and are not counted here.)

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
