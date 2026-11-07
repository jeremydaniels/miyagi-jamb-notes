# JAMB Physics Notes: Introductory Electronics

## What JAMB expects

This file covers Section A, Topic 39 of the JAMB Physics syllabus: Introductory Electronics. It covers the following content items:
- i. distinction between metals, semiconductors and insulators (elementary knowledge of band gap is required);
- ii. intrinsic and extrinsic semiconductors (n-type and p-type semiconductors);
- iii. uses of semiconductors and diodes in rectification and transistors in amplification;
- iv. elementary knowledge of diodes and transistors.

By the end of these notes, you should be able to:
1. differentiate between conductors, semi- conductors and insulators;
2. distinguish between intrinsic and extrinsic semiconductors;
3. distinguish between electron and hole carriers;
4. analyse diodes and transistor;
5. relate diodes to rectification and transistor to amplification.

*(Note on the syllabus wording: The official JAMB syllabus skips objective numeral "v" and jumps from "iv" directly to "vi". In these notes, we have mapped the objective "relate diodes to rectification and transistor to amplification" to "v" to maintain sequential numbering. The syllabus also contains a minor typo in objective i, spelling semiconductors as "semi- conductors".)*

## Distinguishing Between Conductors, Semiconductors and Insulators

**Objective i: differentiate between conductors, semi- conductors and insulators; Content item i: distinction between metals, semiconductors and insulators.**

To understand why some materials conduct electricity well while others do not, we use **Energy Band Theory**. In a single isolated atom, electrons exist in specific, discrete energy levels. However, in a solid piece of material where billions of atoms are packed closely together in a crystal lattice, their electron energy levels interact and merge to form continuous bands of energy.

There are three key regions in band theory that you must know:
1. **Valence band:** This is the highest energy band that contains electrons at absolute zero temperature ($0\ \text{K}$). The electrons here are firmly bound to their individual atoms by covalent bonds.
2. **Conduction band:** This is the energy band immediately above the valence band. When electrons gain enough energy to jump into this band, they break free from their atoms and can move easily through the material to conduct electricity.
3. **Forbidden energy gap (Band gap, $E_g$):** This is the gap in energy between the valence band and the conduction band. Electrons cannot exist in this gap. The size of this gap determines whether a material acts as a conductor, a semiconductor, or an insulator. The unit used for this energy gap is usually the electron-volt ($\text{eV}$).

### Comparison Table: Conductors, Semiconductors, and Insulators

| Feature | Conductors (Metals) | Semiconductors | Insulators |
| --- | --- | --- | --- |
| **Band gap ($E_g$)** | No gap ($E_g = 0\ \text{eV}$) | Small gap ($E_g \approx 1\ \text{eV}$) | Large gap ($E_g > 3\ \text{eV}$) |
| **Energy Bands** | Valence and conduction bands **overlap**. | Small forbidden gap separates the valence and conduction bands. | Huge forbidden gap separates the valence and conduction bands. |
| **Electron movement** | Electrons are free to move into the conduction band at any temperature. | At $0\ \text{K}$, no electrons can cross. At room temperature, some gain enough thermal energy to jump across. | Electrons do not have enough energy to jump the large gap under normal conditions. |
| **Conductivity** | Very high | Moderate (between conductors and insulators) | Very low (practically zero) |
| **Effect of Temperature on Resistance** | Resistance **increases** as temperature rises (positive temperature coefficient). | Resistance **decreases** as temperature rises (negative temperature coefficient). | Resistance remains very high, though it may decrease slightly at extreme temperatures. |
| **Examples** | Copper, Aluminum, Gold, Iron | Silicon ($1.1\ \text{eV}$ gap), Germanium ($0.7\ \text{eV}$ gap) | Glass, Wood, Rubber, Diamond ($5.5\ \text{eV}$ gap) |

*(Note: Textbooks sometimes vary slightly on the exact band gap value defining an insulator, often stating $>3\ \text{eV}$ or $>5\ \text{eV}$. JAMB focuses on the conceptual difference: zero gap for metals, small gap for semiconductors, large gap for insulators).*

[IMAGE: Three side-by-side energy band diagrams. Left: Conductor (metal), showing the lower valence band and upper conduction band overlapping (no gap). Middle: Semiconductor, showing a small forbidden energy gap (labeled ~1 eV) between the valence band and conduction band. Right: Insulator, showing a large forbidden energy gap (labeled >3 eV) between the bands. Clean flat textbook illustration, white background, clearly labeled vertical energy axes pointing upwards.]

## Intrinsic and Extrinsic Semiconductors

**Objective ii: distinguish between intrinsic and extrinsic semiconductors; Content item ii: intrinsic and extrinsic semiconductors.**

### Intrinsic Semiconductors
An **intrinsic semiconductor** is a pure semiconductor material with no impurities added. The most common examples are highly purified crystals of **Silicon (Si)** and **Germanium (Ge)**, which belong to Group IV of the periodic table. 
- At absolute zero ($0\ \text{K}$), all four valence electrons of each silicon atom form perfect covalent bonds with four neighboring atoms. Because there are no free electrons, an intrinsic semiconductor acts as a perfect insulator.
- As temperature increases, thermal energy breaks some of these covalent bonds. An electron is freed into the conduction band, leaving behind an empty space in the valence band called a **hole**.
- This process is called thermal generation of electron-hole pairs. In an intrinsic semiconductor, the number of free electrons ($n_e$) is always exactly equal to the number of holes ($n_h$).

### Extrinsic Semiconductors
Because intrinsic semiconductors are poor conductors at room temperature, scientists deliberately add tiny amounts of carefully chosen impurities to them to dramatically increase their conductivity. 
- This deliberate addition of impurities is called **doping**.
- The resulting impure semiconductor is called an **extrinsic semiconductor**.

Extrinsic semiconductors are divided into two types depending on the chemical group of the impurity added:

| Feature | n-type Semiconductor | p-type Semiconductor |
| --- | --- | --- |
| **Meaning of name** | "n" stands for Negative. | "p" stands for Positive. |
| **Impurity added** | **Pentavalent** (Group V) elements, which have 5 valence electrons. | **Trivalent** (Group III) elements, which have 3 valence electrons. |
| **Examples of impurity** | Phosphorus (P), Arsenic (As), Antimony (Sb) | Boron (B), Aluminum (Al), Gallium (Ga), Indium (In) |
| **How it works** | 4 of the 5 electrons form bonds. The 5th electron is left free to conduct electricity. | The 3 electrons form bonds, leaving a missing 4th bond. This empty space is a "hole". |
| **Type of impurity** | **Donor** (donates an extra electron). | **Acceptor** (creates a hole that can accept an electron). |
| **Majority charge carriers**| Electrons | Holes |
| **Minority charge carriers**| Holes | Electrons |

[IMAGE: Two side-by-side crystal lattice structures of silicon (Si). Left (n-type): A central Phosphorus (P) atom replaces a Si atom, with four covalent bonds to neighboring Si atoms and one extra "free electron" highlighted in red. Right (p-type): A central Boron (B) atom replaces a Si atom, with three covalent bonds and one missing bond leaving a "hole" highlighted as an empty white circle. Clean flat textbook illustration, white background.]

## Electron and Hole Carriers

**Objective iii: distinguish between electron and hole carriers.**

In metals, electric current is carried entirely by moving electrons. In semiconductors, however, current is carried by two different entities simultaneously: **electrons** and **holes**.

1. **Electrons:** 
   - They are negatively charged fundamental particles.
   - In semiconductors, free electrons exist in the **conduction band**.
   - They move freely through the crystal lattice when a voltage is applied, moving toward the positive terminal.

2. **Holes:**
   - A hole is simply the absence (or vacancy) of an electron in a covalent bond.
   - It acts precisely like a **positively charged** particle.
   - Holes exist in the **valence band**.
   - When a voltage is applied, a nearby bound electron jumps into a hole to fill it. When it does, it leaves a new hole behind in its previous position. As electrons hop one way to fill holes, the holes effectively "move" in the opposite direction toward the negative terminal.

Both the physical movement of free electrons in the conduction band and the apparent movement of holes in the valence band contribute to the total electric current in a semiconductor. 

## Elementary Knowledge of Diodes and Transistors

**Objective iv: analyse diodes and transistor; Content item iv: elementary knowledge of diodes and transistors.**

### The p-n Junction Diode
When a piece of p-type semiconductor is permanently joined to a piece of n-type semiconductor, the boundary between them is called a **p-n junction**. A two-terminal device containing one p-n junction is called a **semiconductor diode**.
- **Depletion layer:** Immediately after the junction is formed, some free electrons from the n-side diffuse across the boundary and fill holes on the p-side. This creates a narrow region at the junction stripped of all free charge carriers, called the depletion layer. It sets up an internal barrier voltage (about $0.7\ \text{V}$ for silicon) that stops further electron flow.

A diode can be connected to an external battery (biased) in two ways:
1. **Forward Bias:** The positive terminal of the battery is connected to the p-type material, and the negative terminal to the n-type. The external voltage pushes carriers toward the junction, **narrowing** the depletion layer. The barrier voltage is overcome, and a large current flows easily.
2. **Reverse Bias:** The positive terminal is connected to the n-type material, and the negative terminal to the p-type. The carriers are pulled away from the junction. The depletion layer **widens**, acting as a strong insulator. Almost zero current flows.

[IMAGE: Two circuit diagrams of a p-n junction diode. Top (Forward Bias): The p-region is connected to the positive terminal of a battery and the n-region to the negative terminal; the depletion layer is shown as very narrow, with arrows indicating current flow. Bottom (Reverse Bias): The p-region is connected to the negative terminal and the n-region to the positive terminal; the depletion layer is shown as wide, with a crossed-out arrow indicating no current flow. Clean flat textbook illustration, white background.]

### Transistors (Bipolar Junction Transistors)
A transistor is a semiconductor device made of three alternating doped layers, forming two p-n junctions. The three regions are:
1. **Emitter (E):** Heavily doped to supply a large number of charge carriers into the device.
2. **Base (B):** Very thin and lightly doped. It acts as a control gate regulating the flow of carriers.
3. **Collector (C):** Moderately doped and physically the largest region, designed to collect the charge carriers and dissipate heat.

There are two types of bipolar junction transistors:
- **npn transistor:** A p-type base is sandwiched between an n-type emitter and an n-type collector. (This is the most common type).
- **pnp transistor:** An n-type base is sandwiched between a p-type emitter and a p-type collector.

[IMAGE: Circuit symbols for transistors. Left: npn transistor with Emitter (E), Base (B), and Collector (C), where the arrow on the emitter points outwards (Not Pointing iN). Right: pnp transistor with E, B, C, where the arrow on the emitter points inwards (Pointing iN Proudly). Clean flat textbook illustration, white background.]

### Transistor Calculations
In any transistor, the current flowing out of (or into) the emitter is the sum of the very small current in the base and the large current in the collector.
$$I_E = I_B + I_C$$
where:
- $I_E$ = Emitter current (unit: Amperes, $\text{A}$, often $\text{mA}$)
- $I_B$ = Base current (unit: Amperes, $\text{A}$, often $\mu\text{A}$)
- $I_C$ = Collector current (unit: Amperes, $\text{A}$, often $\text{mA}$)

Transistors also have current gain parameters when used in circuits:
- **Common-Base Current Gain ($\alpha$):** The ratio of collector current to emitter current. Because the base takes a tiny fraction of the current, $\alpha$ is always slightly less than 1 (usually $0.95$ to $0.99$).
  $$\alpha = \frac{I_C}{I_E}$$
- **Common-Emitter Current Gain ($\beta$):** The ratio of collector current to base current. Because the base current is very small, $\beta$ is a large number (typically $20$ to $500$).
  $$\beta = \frac{I_C}{I_B}$$
- **Relationship between $\alpha$ and $\beta$:**
  $$\beta = \frac{\alpha}{1 - \alpha} \quad \text{and} \quad \alpha = \frac{\beta}{1 + \beta}$$
  *(Note: $\alpha$ and $\beta$ are ratios of currents, so they have **no unit**).*

---
**Worked Example 1**
A transistor has a base current of $50\ \mu\text{A}$ and a collector current of $2.0\ \text{mA}$. Calculate the emitter current in $\text{mA}$.

1. **Identify given values with units:** Base current $I_B = 50\ \mu\text{A}$, Collector current $I_C = 2.0\ \text{mA}$.
2. **Convert to matching units:** It is necessary to convert $I_B$ to $\text{mA}$ so that it matches $I_C$ and the requested final unit. Since $1\ \text{mA} = 1000\ \mu\text{A}$, divide by $1000$:
   $I_B = \frac{50\ \mu\text{A}}{1000} = 0.05\ \text{mA}$.
3. **Write the formula:** The fundamental current equation for a transistor is:
   $I_E = I_B + I_C$
4. **Substitute the values with units:**
   $I_E = 0.05\ \text{mA} + 2.0\ \text{mA}$
5. **Calculate the final answer:**
   $I_E = 2.05\ \text{mA}$
   The emitter current is $2.05\ \text{mA}$.

---
**Worked Example 2**
In a common-base configuration, a transistor has a current gain $\alpha$ of $0.98$. If the emitter current is $5.0\ \text{mA}$, calculate the collector current.

1. **Identify given values:** Current gain $\alpha = 0.98$ (no unit), Emitter current $I_E = 5.0\ \text{mA}$.
2. **Write the formula for alpha:** $\alpha$ is defined as the ratio of collector current to emitter current:
   $\alpha = \frac{I_C}{I_E}$
3. **Rearrange the formula to find the collector current ($I_C$):** Multiply both sides by $I_E$:
   $I_C = \alpha \times I_E$
4. **Substitute the values with units:**
   $I_C = 0.98 \times 5.0\ \text{mA}$
5. **Calculate the final answer:**
   $I_C = 4.9\ \text{mA}$
   The collector current is $4.9\ \text{mA}$.

---
**Worked Example 3**
A transistor used in a radio receiver has a common-base current gain ($\alpha$) of $0.95$. Calculate its common-emitter current gain ($\beta$).

1. **Identify given value:** $\alpha = 0.95$ (no unit).
2. **Write the formula relating $\alpha$ and $\beta$:**
   $\beta = \frac{\alpha}{1 - \alpha}$
3. **Substitute the value of $\alpha$:**
   $\beta = \frac{0.95}{1 - 0.95}$
4. **Perform the subtraction in the denominator:**
   $\beta = \frac{0.95}{0.05}$
5. **Calculate the final answer:**
   $\beta = 19$
   The common-emitter current gain is $19$ (no unit).

## Applications: Rectification and Amplification

**Objective v: relate diodes to rectification and transistor to amplification; Content item iii: uses of semiconductors and diodes in rectification and transistors in amplification.**

### 1. Diodes in Rectification
Because a p-n junction diode only allows current to flow easily in one direction (during forward bias), its most important application is **rectification**. 
- **Rectification** is the process of converting alternating current (AC, which periodically reverses direction, like the $240\ \text{V}$ mains electricity supplied by NEPA/distribution companies) into direct current (DC, which flows in only one direction, like the current from a battery).
- For example, when using a phone charger, the charger circuit contains diodes to convert the AC from the wall socket into the $5\ \text{V}$ DC required to safely charge your phone battery.
- **Half-wave rectification:** Uses a single diode in series with a load. It only allows the positive half of the AC wave to pass, while completely blocking the negative half. The resulting DC output is pulsed and inefficient.
- **Full-wave rectification:** Uses two diodes (with a center-tapped transformer) or four diodes (arranged in a bridge rectifier). This clever arrangement flips the negative half of the AC wave into a positive half, creating a much smoother and continuous DC output without gaps.

[IMAGE: Three voltage-time graphs stacked vertically. Top: An input alternating current (AC) sinusoidal wave swinging above and below the zero-voltage line. Middle: Output of a half-wave rectifier showing only the positive half-cycles (humps) and flat lines at zero for the negative half-cycles. Bottom: Output of a full-wave rectifier showing continuous positive half-cycles ("humps") with no gaps. Clean flat textbook style, white background, axes labeled Voltage and Time.]

### 2. Transistors in Amplification
A major use of transistors in consumer electronics (such as radios, televisions, and public address systems in Nigerian markets and places of worship) is **amplification**.
- **Amplification** is the process of increasing the amplitude (strength) of a weak electrical signal.
- In a common-emitter amplifier circuit, the small signal you want to amplify (like the tiny electrical voltage generated by a microphone) is fed into the **Base** terminal of the transistor. 
- Because of the transistor's structure, a small fluctuation in the base current causes a massive, proportional change in the **Collector** current. 
- Therefore, the weak input signal is transformed into a powerful output signal that retains the exact same shape and frequency but is strong enough to drive a large loudspeaker. 

## Key terms

| Term | Meaning |
| --- | --- |
| **Energy Band Gap ($E_g$)** | The forbidden energy region between the valence band and the conduction band where no electrons can exist. |
| **Conductor** | A material with no band gap; valence and conduction bands overlap, allowing easy electron flow. |
| **Insulator** | A material with a very large band gap, preventing electrons from reaching the conduction band. |
| **Semiconductor** | A material with a small band gap that acts as an insulator at $0\ \text{K}$ but conducts at higher temperatures. |
| **Intrinsic Semiconductor** | A highly pure semiconductor (e.g., pure Silicon or Germanium) without any added impurities. |
| **Extrinsic Semiconductor** | A semiconductor that has been doped with impurities to dramatically increase its conductivity. |
| **Doping** | The deliberate addition of specific impurities to a pure semiconductor lattice. |
| **n-type Semiconductor** | Doped with a pentavalent (donor) impurity; majority carriers are electrons. |
| **p-type Semiconductor** | Doped with a trivalent (acceptor) impurity; majority carriers are holes. |
| **Hole** | A vacancy in a covalent bond that acts as a mobile positive charge carrier. |
| **Diode** | A two-terminal semiconductor device with one p-n junction that allows current to flow in only one direction. |
| **Rectification** | The process of converting alternating current (AC) into direct current (DC) using diodes. |
| **Transistor** | A three-terminal semiconductor device (Emitter, Base, Collector) used for amplification or switching. |
| **Amplification** | The process of increasing the strength of a weak electrical signal using a transistor. |

## Exam tips and common mistakes

- **Mistaking the effect of temperature:** Remember that heating a metal *increases* its resistance, but heating a semiconductor *decreases* its resistance (because heat pushes more electrons into the conduction band, increasing charge carriers).
- **Unit mismatch in transistor math:** A very common mistake in JAMB is adding base current ($I_B$) given in microamperes ($\mu\text{A}$) directly to collector current ($I_C$) given in milliamperes ($\text{mA}$) without converting. Always convert $\mu\text{A}$ to $\text{mA}$ by dividing by $1000$ before adding.
  - *Wrong working:* $I_E = 50\ \mu\text{A} + 2\ \text{mA} \rightarrow 52\ \text{mA}$ (Incorrect).
  - *Correct working:* $I_E = 0.05\ \text{mA} + 2.0\ \text{mA} = 2.05\ \text{mA}$.
- **Mixing up doping impurities:** "p-type" requires "tri-valent" impurities (like Boron). "n-type" requires "penta-valent" impurities (like Phosphorus). An easy way to remember is **P**-type uses Group **3** (positive holes), **N**-type uses Group **5** (negative extra electrons).
- **Confusing $\alpha$ and $\beta$:** $\alpha$ (common-base gain) is always a decimal slightly less than 1. $\beta$ (common-emitter gain) is always a large whole number (e.g., $50$ to $200$). 
- **Diodes vs Transistors:** Diodes **rectify** (AC to DC). Transistors **amplify** (boost signals).

## Quick summary

1. In band theory, conductors have overlapping valence and conduction bands, insulators have a very large band gap, and semiconductors have a small band gap (about $1\ \text{eV}$).
2. The resistance of a semiconductor decreases as temperature increases (it has a negative temperature coefficient), unlike metals which become more resistive.
3. Intrinsic semiconductors are pure. Extrinsic semiconductors are doped with impurities to improve conductivity.
4. n-type semiconductors are doped with pentavalent impurities and use free electrons as majority charge carriers.
5. p-type semiconductors are doped with trivalent impurities and use holes as majority charge carriers.
6. A p-n junction diode conducts current when forward-biased and blocks it when reverse-biased, making it highly useful for converting AC to DC (rectification).
7. Transistors (npn or pnp) have three terminals (Emitter, Base, Collector) and are primarily used for amplifying weak signals.
8. For any transistor, Emitter current = Base current + Collector current ($I_E = I_B + I_C$).

## Practice questions

**1. Which of the following correctly differentiates a semiconductor from a metal?**
- A. Its resistance increases with an increase in temperature
- B. Its resistance decreases with an increase in temperature
- C. Its conductivity is permanently higher than that of a metal
- D. It has no energy gap between its valence and conduction bands

**Answer: B.**
1. Recall the effect of temperature on a metal: heating increases atomic vibrations, which increases resistance (positive temperature coefficient).
2. Recall the effect of temperature on a semiconductor: heating gives electrons enough energy to jump the band gap ($E_g \approx 1\ \text{eV}$), creating more charge carriers.
3. Conclude that this increase in carriers decreases the resistance of the semiconductor (negative temperature coefficient).
The mistake behind the most tempting wrong option (A) is assuming a semiconductor's resistance increases when heated, exactly like a metal, forgetting they have opposite temperature coefficients.

**2. In an n-type semiconductor, the majority charge carriers are:**
- A. Protons
- B. Holes
- C. Electrons
- D. Neutrons

**Answer: C.**
1. Identify that "n-type" stands for negative-type semiconductor.
2. Recall that n-type semiconductors are doped with pentavalent impurities (e.g., Phosphorus).
3. Note that each pentavalent atom provides one extra free electron ($e^-$) that does not fit into the 4-bond silicon lattice.
4. Conclude that these extra negative electrons are the majority charge carriers.
The mistake behind the most tempting wrong option (B) is confusing the properties of an n-type semiconductor with a p-type semiconductor, where holes would be the majority carriers.

**3. To produce a p-type semiconductor, pure silicon is doped with a:**
- A. Trivalent impurity
- B. Tetravalent impurity
- C. Pentavalent impurity
- D. Hexavalent impurity

**Answer: A.**
1. Identify that a "p-type" semiconductor requires a deficit of electrons to create positive "holes".
2. Recognize that pure silicon has $4$ valence electrons (tetravalent).
3. To create a missing bond (a hole), we must add an atom with fewer than $4$ valence electrons.
4. Conclude that a trivalent (Group III) impurity, which has $3$ valence electrons, is required.
The mistake behind the most tempting wrong option (C) is selecting a pentavalent impurity, which would create an n-type semiconductor rather than the requested p-type.

**4. Which of the following is true about a p-n junction diode in reverse bias?**
- A. The depletion layer narrows and current flows easily
- B. The p-type region is connected to the positive terminal of the battery
- C. The depletion layer widens and it hardly conducts current
- D. Electrons are pushed across the junction into the p-type region

**Answer: C.**
1. Define reverse bias: the p-type region is connected to the negative terminal of an external voltage ($V < 0\ \text{V}$), and the n-type to the positive terminal.
2. Note the effect on charge carriers: holes in the p-type and electrons in the n-type are pulled away from the junction by the battery's terminals.
3. Conclude that the depletion layer widens as a result, creating a large barrier that blocks current flow.
The mistake behind the most tempting wrong option (A) is describing the behavior of a forward-biased diode, where the depletion layer narrows, instead of a reverse-biased diode.

**5. A major application of a transistor in an electronic circuit is as an:**
- A. Amplifier
- B. Rectifier
- C. Inductor
- D. Alternator

**Answer: A.**
1. Identify the function of a transistor in signal processing: it uses a very small input base current ($I_B$) to control a much larger output collector current ($I_C$).
2. Recall that this process of boosting a weak electrical signal into a strong one is called amplification.
3. Conclude that the transistor acts as an amplifier.
The mistake behind the most tempting wrong option (B) is confusing the application of a transistor (amplification) with that of a diode (rectification).

**6. In a given transistor circuit, the base current is $40\ \mu\text{A}$ and the emitter current is $1.54\ \text{mA}$. Calculate the collector current.**
- A. $1.94\ \text{mA}$
- B. $1.50\ \text{mA}$
- C. $1.14\ \text{mA}$
- D. $1.58\ \text{mA}$

**Answer: B.**
1. Write the transistor current formula: $I_E = I_B + I_C$.
2. Rearrange to solve for the collector current: $I_C = I_E - I_B$.
3. Convert the base current to matching units: $I_B = 40\ \mu\text{A} = 0.04\ \text{mA}$.
4. Substitute the values with units: $I_C = 1.54\ \text{mA} - 0.04\ \text{mA}$.
5. Calculate the result: $I_C = 1.50\ \text{mA}$.
The mistake behind the most tempting wrong option (C) is subtracting $0.4\ \text{mA}$ instead of $0.04\ \text{mA}$ due to a wrong unit conversion from $40\ \mu\text{A}$ to $\text{mA}$. Option D ($1.58\ \text{mA}$) comes from wrongly adding the values ($1.54 + 0.04$) instead of subtracting, and option A ($1.94\ \text{mA}$) from adding with the wrong unit conversion ($1.54 + 0.40$).

**7. The common-base current gain ($\alpha$) of a transistor is $0.98$. What is its common-emitter current gain ($\beta$)?**
- A. $0.02$
- B. $49$
- C. $50$
- D. $98$

**Answer: B.**
1. Write the formula relating $\alpha$ and $\beta$: $\beta = \frac{\alpha}{1 - \alpha}$.
2. Substitute the given value ($\alpha = 0.98$): $\beta = \frac{0.98}{1 - 0.98}$.
3. Calculate the denominator: $1 - 0.98 = 0.02$.
4. Calculate the final ratio: $\beta = \frac{0.98}{0.02} = 49$.
The mistake behind the most tempting wrong option (C) is using the incorrect formula $\beta = \frac{1}{1 - \alpha}$, calculating $\frac{1}{0.02} = 50$.

**8. The process of converting alternating current (AC) to direct current (DC) using semiconductor diodes is known as:**
- A. Amplification
- B. Rectification
- C. Modulation
- D. Induction

**Answer: B.**
1. Recall the definitions of the listed electrical processes.
2. Identify that an alternating current (AC) repeatedly reverses direction, while direct current (DC) flows in one direction.
3. Recognize that diodes only allow current to flow in one direction (forward bias).
4. Conclude that using diodes to turn AC into DC is called rectification.
The mistake behind the most tempting wrong option (A) is identifying the function of a transistor (amplification) instead of the function of a diode (rectification).

**9. In energy band theory, an insulator is characterized by:**
- A. Overlapping valence and conduction bands
- B. A very small forbidden energy gap
- C. A partially filled conduction band at $0\ \text{K}$
- D. A very large forbidden energy gap

**Answer: D.**
1. Recall that the forbidden energy gap ($E_g$) is the energy required to move an electron from the valence band to the conduction band.
2. Identify that in a conductor, the bands overlap ($E_g = 0\ \text{eV}$).
3. Identify that in a semiconductor, the gap is small ($E_g \approx 1\ \text{eV}$).
4. Conclude that an insulator cannot easily conduct because it has a very large forbidden energy gap (typically $E_g > 3\ \text{eV}$).
The mistake behind the most tempting wrong option (A) is selecting the band structure of a metal (overlapping bands) instead of an insulator.

**10. A transistor in a common-emitter circuit has a current gain ($\beta$) of $100$. If the base current is $20\ \mu\text{A}$, what is the emitter current in $\text{mA}$?**
- A. $2.00\ \text{mA}$
- B. $2.02\ \text{mA}$
- C. $20.02\ \text{mA}$
- D. $22.00\ \text{mA}$

**Answer: B.**
1. Write the formula relating collector current to base current: $I_C = \beta \times I_B$.
2. Substitute the values: $I_C = 100 \times 20\ \mu\text{A} = 2000\ \mu\text{A}$.
3. Convert $I_C$ and $I_B$ to $\text{mA}$: $I_C = \frac{2000\ \mu\text{A}}{1000} = 2.00\ \text{mA}$ and $I_B = \frac{20\ \mu\text{A}}{1000} = 0.02\ \text{mA}$.
4. Write the formula for emitter current: $I_E = I_B + I_C$.
5. Calculate the final value: $I_E = 0.02\ \text{mA} + 2.00\ \text{mA} = 2.02\ \text{mA}$.
The mistake behind the most tempting wrong option (A) is calculating only the collector current ($I_C = 2.00\ \text{mA}$) and forgetting to add the base current to find the emitter current ($I_E$).
