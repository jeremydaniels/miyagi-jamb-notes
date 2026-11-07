# JAMB Physics Notes: Capacitors

## What JAMB expects

This topic is Section A, Topic 29 of the JAMB Physics syllabus: Capacitors. It covers the following content items:

* (i) types and functions of capacitors;
* (ii) parallel plate capacitors;
* (iii) capacitance of a capacitor;
* (iv) the relationship between capacitance, area separation of plates and medium between the plates $C = \frac{EA}{d}$;
* (v) capacitors in series and parallel;
* (vi) energy stored in a capacitor.

By the end of these notes, you should be able to:

* i. determine uses of capacitors;
* ii. analyse parallel plate capacitors;
* iii. determine the capacitance of a capacitor;
* iv. analyse the factors that affect the capacitance of a capacitor;
* v. solve problems involving the arrangement of a capacitor;
* vi. determine the energy stored in capacitors.

**Note on the syllabus wording:** The JAMB syllabus writes the formula for the capacitance of a parallel plate capacitor as $C = \frac{EA}{d}$. The use of the letter $E$ is a typographical error for the standard Greek letter epsilon ($\varepsilon$), which represents the *permittivity* of the medium. In physics, $E$ usually stands for electric field or energy. Throughout these notes, we will use the correct standard symbol $\varepsilon$. Furthermore, the phrase "area separation of plates" is missing a comma and simply means "area, separation of plates". 

## Types and functions of capacitors

**Objective i: determine uses of capacitors.**
**Content (i): types and functions of capacitors.**

A **capacitor** is an electrical device designed to store electrical charge and electrical energy. It consists of two electrical conductors separated by an insulator (called a **dielectric**). When connected to a voltage source, equal and opposite charges build up on the two conductors.

### Common types of capacitors
Capacitors are named after the type of dielectric material used between their plates.

1. **Electrolytic capacitors:** These provide a very large capacitance in a small volume. They are **polarised**, meaning they have a positive leg and a negative leg, and must be connected the right way round in a circuit, otherwise they can explode.
2. **Ceramic capacitors:** Small, non-polarised capacitors (often shaped like tiny discs or beads) that use ceramic as the dielectric. They are widely used in high-frequency circuits.
3. **Paper and Mica capacitors:** These use waxed paper or mica sheets as dielectrics. They are general-purpose capacitors used in many older and modern electronic devices.
4. **Variable capacitors:** These have a capacitance that can be adjusted manually, usually by turning a knob that changes how much the metal plates overlap. 

### Functions and uses of capacitors
Capacitors are essential components in almost all electronic circuits. Their main uses include:

* **Storing charge and energy:** Capacitors can store energy slowly and release it very quickly. For example, in a camera flash, a capacitor charges up from a small battery and then releases all its energy in a fraction of a second to produce a bright flash.
* **Smoothing in power supplies:** When converting Alternating Current (AC) from the mains (e.g., from NEPA/power holding companies or generators) to Direct Current (DC) for electronics, rectifiers produce a "bumpy" DC. Capacitors act as reservoirs, smoothing out these bumps to provide a steady DC voltage.
* **Tuning radio and TV circuits:** A variable capacitor is connected to an inductor (a coil of wire) to form a tuning circuit. Turning the tuning knob on a radio changes the capacitance, allowing you to select different radio stations (frequencies).
* **Blocking DC while passing AC:** Capacitors do not allow continuous Direct Current (DC) to flow through them because of the insulator between their plates. However, they allow Alternating Current (AC) to pass. This is useful in audio amplifiers to pass the sound signal (AC) while blocking the battery voltage (DC).
* **Timing and delay circuits:** Because it takes a predictable amount of time for a capacitor to charge and discharge through a resistor, they are used in timing circuits (like the blinking indicator lights on an okada or car).

## Parallel plate capacitors

**Objective ii: analyse parallel plate capacitors.**
**Content (ii): parallel plate capacitors.**

The simplest and most common theoretical model of a capacitor is the **parallel plate capacitor**. 

It consists of two flat, parallel conducting plates, each with an area $A$, separated by a small distance $d$. The space between the plates is filled with a dielectric (which can simply be air or a vacuum, or a material like glass, paper, or plastic).

[IMAGE: A clean textbook illustration showing a parallel plate capacitor. Two parallel vertical rectangular metal plates, one marked with positive signs (+) and the other with negative signs (-). A battery is connected across them with wires. Uniform electric field lines (straight arrows) point from the positive plate to the negative plate. Labels to add later: "Positive plate (+Q)", "Negative plate (-Q)", "Electric field E", "Distance d", "Battery (V)". Clean flat textbook style, white background.]

### How it works
When the plates are connected to the terminals of a battery of voltage $V$:
1. Electrons are pulled from the plate connected to the positive terminal, leaving it with a net positive charge $+Q$.
2. These electrons are pushed onto the plate connected to the negative terminal, giving it a net negative charge $-Q$.
3. The two plates now have **equal and opposite charges**.
4. An **electric field** is created in the gap between the plates, pointing from the positive plate to the negative plate. The strength of this uniform electric field is given by $E = \frac{V}{d}$ (where $E$ is the electric field in $\text{V m}^{-1}$, $V$ is the voltage in $\text{V}$, and $d$ is the distance in $\text{m}$).

Although the total net charge of the entire capacitor is zero ($+Q - Q = 0$), we say the capacitor "stores a charge $Q$".

## Capacitance of a capacitor

**Objective iii: determine the capacitance of a capacitor.**
**Content (iii): capacitance of a capacitor.**

The **capacitance** ($C$) of a capacitor is the measure of its ability to store charge. It is defined as the ratio of the charge ($Q$) stored on *one* of the plates to the potential difference ($V$) across them.

$$C = \frac{Q}{V}$$

Where:
* $C$ = Capacitance in **Farads (F)**
* $Q$ = Charge in **Coulombs (C)**
* $V$ = Potential difference (voltage) in **Volts (V)**

**The Farad:** One Farad ($1\ \text{F}$) is the capacitance of a capacitor that stores a charge of $1\ \text{Coulomb}$ when a potential difference of $1\ \text{Volt}$ is applied across it. 

A Farad is a massive unit. In practical circuits, you will almost always use prefixes:
* **Microfarad ($\mu\text{F}$):** $1\ \mu\text{F} = 10^{-6}\ \text{F}$
* **Nanofarad ($\text{nF}$):** $1\ \text{nF} = 10^{-9}\ \text{F}$
* **Picofarad ($\text{pF}$):** $1\ \text{pF} = 10^{-12}\ \text{F}$

### Worked examples: calculating charge and capacitance

**1. A $500\ \mu\text{F}$ capacitor in a radio circuit is connected to a $9\ \text{V}$ battery. Calculate the charge stored in the capacitor.**
1. State the formula: $Q = CV$ (rearranged from $C = \frac{Q}{V}$)
2. Substitute with units: $C = 500 \times 10^{-6}\ \text{F}$, $V = 9\ \text{V}$
3. Calculate: $Q = (500 \times 10^{-6}) \times 9 = 4500 \times 10^{-6}\ \text{C}$
4. Answer: $Q = 4.5 \times 10^{-3}\ \text{C}$ (or $4.5\ \text{mC}$)

**2. A capacitor stores $1.2 \times 10^{-4}\ \text{C}$ of charge when a potential difference of $24\ \text{V}$ is applied across its plates. Calculate its capacitance.**
1. State the formula: $C = \frac{Q}{V}$
2. Substitute with units: $C = \frac{1.2 \times 10^{-4}\ \text{C}}{24\ \text{V}}$
3. Calculate: $C = 0.05 \times 10^{-4}\ \text{F} = 5.0 \times 10^{-6}\ \text{F}$
4. Answer: $C = 5.0\ \mu\text{F}$

## Factors affecting the capacitance of a capacitor

**Objective iv: analyse the factors that affect the capacitance of a capacitor.**
**Content (iv): the relationship between capacitance, area separation of plates and medium between the plates $C = \frac{EA}{d}$.**

The capacitance of a parallel plate capacitor depends solely on its physical geometry and the material between the plates. It does *not* depend on the voltage applied or the charge stored. 

The three factors that affect capacitance are:
1. **The overlapping Area of the plates ($A$):** Capacitance is directly proportional to the area. Larger plates can hold more charge. ($C \propto A$)
2. **The distance of separation between the plates ($d$):** Capacitance is inversely proportional to the distance. Moving the plates closer together increases the attraction between the positive and negative charges, allowing more charge to be stored for the same voltage. ($C \propto \frac{1}{d}$)
3. **The dielectric medium between the plates ($\varepsilon$):** Different insulating materials allow electric fields to form through them with different ease. This property is called **permittivity** ($\varepsilon$). Using a better dielectric increases the capacitance.

Combining these gives the standard formula:

$$C = \frac{\varepsilon A}{d}$$

*(Note: As explained in the syllabus wording section, JAMB writes this as $C = \frac{EA}{d}$, treating $E$ as $\varepsilon$.)*

Where:
* $C$ = Capacitance in Farads ($\text{F}$)
* $A$ = Overlapping area of the plates in square metres ($\text{m}^2$)
* $d$ = Distance of separation in metres ($\text{m}$)
* $\varepsilon$ = Permittivity of the dielectric material in Farads per metre ($\text{F m}^{-1}$)

[IMAGE: A diagram illustrating the factors affecting a parallel plate capacitor. Two rectangular plates are shown in 3D perspective. The overlapping area is shaded and labeled 'Area (A)'. The small gap between them is labeled 'Distance (d)'. A solid block representing an insulating medium is partially inserted between the plates, labeled 'Dielectric (permittivity ε)'. Clean flat textbook style, white background.]

### Understanding permittivity and dielectrics

The permittivity $\varepsilon$ of a material is usually expressed in relation to the permittivity of a vacuum (or free space), denoted by $\varepsilon_0$. 

* $\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F m}^{-1}$ (This value is usually given in the JAMB paper). Air is usually treated as a vacuum because its permittivity is almost identical to $\varepsilon_0$.
* The **relative permittivity** or **dielectric constant** ($\varepsilon_r$) of a material is a ratio (it has no unit) comparing how good the material is compared to a vacuum. For example, paper has $\varepsilon_r \approx 3$, and ceramic can have $\varepsilon_r > 1000$.

The total permittivity is: $\varepsilon = \varepsilon_r \times \varepsilon_0$.
Therefore, the formula can be written as:

$$C = \frac{\varepsilon_r \varepsilon_0 A}{d}$$

If you insert a dielectric of relative permittivity $\varepsilon_r$ into a capacitor that previously had air between its plates, its new capacitance becomes: $C_{new} = \varepsilon_r \times C_{air}$.

### Worked examples: factors affecting capacitance

**3. A parallel plate capacitor has rectangular plates measuring $10\ \text{cm}$ by $5\ \text{cm}$, separated by a distance of $1\ \text{mm}$ in air. Calculate its capacitance. ($\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F m}^{-1}$)**
1. Convert dimensions to SI units: 
   Area $A = 0.1\ \text{m} \times 0.05\ \text{m} = 0.005\ \text{m}^2$. 
   Distance $d = 1 \times 10^{-3}\ \text{m}$.
2. State the formula for air: $C = \frac{\varepsilon_0 A}{d}$
3. Substitute: $C = \frac{8.85 \times 10^{-12} \times 0.005}{1 \times 10^{-3}}$
4. Calculate: $C = \frac{4.425 \times 10^{-14}}{1 \times 10^{-3}} = 4.425 \times 10^{-11}\ \text{F}$
5. Answer: $C = 44.25 \times 10^{-12}\ \text{F} = 44.25\ \text{pF}$

**4. If the distance between the plates of a capacitor is halved, and the area is tripled, what happens to its capacitance?**
1. Use proportional reasoning: $C \propto \frac{A}{d}$
2. If $A$ becomes $3A$, the numerator is multiplied by $3$.
3. If $d$ becomes $\frac{d}{2}$, dividing by a half is the same as multiplying by $2$.
4. Total change: $C_{new} \propto \frac{3A}{d / 2} = 6 \frac{A}{d}$.
5. Answer: The capacitance is multiplied by $6$.

## Capacitors in series and parallel

**Objective v: solve problems involving the arrangement of a capacitor.**
**Content (v): capacitors in series and parallel.**

In circuits, capacitors can be combined to achieve a desired total capacitance. The rules for calculating the equivalent (total) capacitance of capacitors are the **exact opposite** of the rules for resistors.

[IMAGE: Circuit diagrams comparing capacitors in series and parallel. Left side: Three capacitors (C1, C2, C3) connected in a single straight line (series) to a voltage source. Right side: Three capacitors (C1, C2, C3) connected in separate parallel branches to a voltage source. Labels to add later: "Series Connection", "1/C = 1/C1 + 1/C2 + 1/C3", "Parallel Connection", "C = C1 + C2 + C3". Clean flat textbook style, white background.]

### 1. Capacitors in parallel
When capacitors are connected in parallel, they are connected across the same two points. 
* **Voltage ($V$) is the same** across all capacitors.
* **Total charge ($Q_T$) is shared** among the capacitors: $Q_T = Q_1 + Q_2 + Q_3 \dots$
* **Total capacitance ($C_p$)** is the sum of the individual capacitances:

$$C_p = C_1 + C_2 + C_3 + \dots$$

Connecting capacitors in parallel **increases** the overall capacitance because you are effectively increasing the total area of the plates.

### 2. Capacitors in series
When capacitors are connected in a chain, one after the other.
* **Charge ($Q$) is the same** on all capacitors in the series branch (because the charge on one plate repels an equal charge to the next).
* **Total voltage ($V_T$) is shared** among the capacitors: $V_T = V_1 + V_2 + V_3 \dots$
* **Total capacitance ($C_s$)** is found using the reciprocal formula:

$$\frac{1}{C_s} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots$$

*Shortcut for exactly two capacitors in series:*
$$C_s = \frac{C_1 \times C_2}{C_1 + C_2} \quad \text{("product over sum")}$$

Connecting capacitors in series **decreases** the overall capacitance because you are effectively increasing the total distance between the outermost plates.

### Worked examples: circuit arrangements

**5. Two capacitors of $3\ \mu\text{F}$ and $6\ \mu\text{F}$ are connected in series across a $12\ \text{V}$ battery. Calculate the equivalent capacitance and the potential difference across the $3\ \mu\text{F}$ capacitor.**
1. Equivalent capacitance (series): $\frac{1}{C_s} = \frac{1}{3} + \frac{1}{6} = \frac{2+1}{6} = \frac{3}{6} = \frac{1}{2}$.
2. Invert: $C_s = 2\ \mu\text{F}$.
3. Calculate the total charge (which is the same for each in series): $Q_T = C_s \times V_T = 2\ \mu\text{F} \times 12\ \text{V} = 24\ \mu\text{C}$.
4. Calculate voltage across the $3\ \mu\text{F}$ capacitor: $V_1 = \frac{Q_1}{C_1} = \frac{24\ \mu\text{C}}{3\ \mu\text{F}} = 8\ \text{V}$.
5. Answer: Equivalent capacitance is $2\ \mu\text{F}$; the voltage across the $3\ \mu\text{F}$ capacitor is $8\ \text{V}$.

**6. Three capacitors of $2\ \mu\text{F}$, $4\ \mu\text{F}$, and $5\ \mu\text{F}$ are connected in parallel. Calculate their equivalent capacitance.**
1. Parallel formula: $C_p = C_1 + C_2 + C_3$
2. Substitute: $C_p = 2 + 4 + 5 = 11\ \mu\text{F}$.
3. Answer: $11\ \mu\text{F}$.

## Energy stored in a capacitor

**Objective vi: determine the energy stored in capacitors.**
**Content (vi): energy stored in a capacitor.**

Charging a capacitor requires work. As charge builds up on the plates, the electric field between them resists the addition of more charge (like charges repel). The work done by the battery to push the charges onto the plates is stored as **electrical potential energy** in the electric field between the plates.

The energy ($W$ or $E$) stored in a capacitor can be calculated using three different formulas, depending on which variables you know. They are derived from the fact that the average voltage during charging is $\frac{1}{2}V$.

1. When you know Capacitance ($C$) and Voltage ($V$):
$$W = \frac{1}{2} C V^2$$

2. When you know Charge ($Q$) and Voltage ($V$):
$$W = \frac{1}{2} Q V$$

3. When you know Charge ($Q$) and Capacitance ($C$):
$$W = \frac{Q^2}{2C}$$

Where:
* $W$ = Energy stored in Joules ($\text{J}$)
* $C$ = Capacitance in Farads ($\text{F}$)
* $V$ = Voltage in Volts ($\text{V}$)
* $Q$ = Charge in Coulombs ($\text{C}$)

### Worked examples: calculating stored energy

**7. A $4\ \mu\text{F}$ capacitor is charged to $100\ \text{V}$. Calculate the energy stored in it.**
1. State formula: $W = \frac{1}{2} C V^2$
2. Convert units: $C = 4 \times 10^{-6}\ \text{F}$
3. Substitute: $W = \frac{1}{2} \times (4 \times 10^{-6}) \times (100)^2$
4. Calculate: $W = 2 \times 10^{-6} \times 10000 = 0.02\ \text{J}$
5. Answer: $0.02\ \text{J}$ (or $2.0 \times 10^{-2}\ \text{J}$)

**8. A capacitor stores $3.0 \times 10^{-3}\ \text{J}$ of energy when it holds a charge of $6.0 \times 10^{-4}\ \text{C}$. Calculate its capacitance.**
1. State formula: $W = \frac{Q^2}{2C}$
2. Rearrange for C: $C = \frac{Q^2}{2W}$
3. Substitute: $C = \frac{(6.0 \times 10^{-4})^2}{2 \times 3.0 \times 10^{-3}}$
4. Calculate: $C = \frac{36 \times 10^{-8}}{6.0 \times 10^{-3}} = 6.0 \times 10^{-5}\ \text{F}$
5. Answer: $C = 60\ \mu\text{F}$

## Key terms

| Term | Meaning |
| --- | --- |
| **Capacitor** | A device used to store electrical charge and energy, consisting of two conductors separated by an insulator. |
| **Capacitance ($C$)** | The ratio of charge stored on one plate of a capacitor to the potential difference across it ($C = Q/V$). Unit: Farad (F). |
| **Dielectric** | The insulating material (e.g., air, paper, ceramic) placed between the plates of a capacitor. |
| **Farad ($\text{F}$)** | The SI unit of capacitance. 1 Farad is 1 Coulomb per Volt. |
| **Permittivity ($\varepsilon$)** | A measure of how easily a dielectric material allows an electric field to be established within it. |
| **Relative permittivity ($\varepsilon_r$)** | Also known as the dielectric constant; the ratio of the permittivity of a substance to the permittivity of a vacuum. |
| **Microfarad ($\mu\text{F}$)** | One millionth of a Farad ($10^{-6}\ \text{F}$). Very common in exam questions. |

## Exam tips and common mistakes

* **Wrong units (Prefixes):** Forgetting to convert microfarads ($\mu\text{F} = 10^{-6}\ \text{F}$) or picofarads ($\text{pF} = 10^{-12}\ \text{F}$) to standard Farads before calculating energy or charge.
* **Confusing Resistor and Capacitor rules:** This is the most common mistake. For capacitors, **Parallel = Add** ($C_1 + C_2$), and **Series = Reciprocals** ($1/C_1 + 1/C_2$). This is the exact *opposite* of the rules for resistors!
* **Forgetting to square the voltage:** In the energy formula $W = \frac{1}{2} C V^2$, many students calculate $\frac{1}{2} \times C \times V$ instead of squaring $V$.
* **Area unit errors:** When calculating the area of the plates from cm, remember that $1\ \text{cm}^2 = 10^{-4}\ \text{m}^2$, not $10^{-2}\ \text{m}^2$.
* **Properties in Series vs Parallel:** Remember that in a series circuit, the *charge* is constant on all capacitors. In a parallel circuit, the *voltage* is constant across all capacitors.

## Quick summary

1. A capacitor stores electrical charge and energy. Uses include smoothing DC power supplies, tuning radios, blocking DC, and powering flashes.
2. Capacitance is defined as the charge stored per unit voltage: $C = \frac{Q}{V}$.
3. For a parallel plate capacitor, capacitance increases if the area of the plates ($A$) increases, or if a better dielectric ($\varepsilon$) is used. It decreases if the distance ($d$) between the plates increases: $C = \frac{\varepsilon A}{d}$.
4. When capacitors are in parallel, their total capacitance is the sum: $C_p = C_1 + C_2 + \dots$
5. When capacitors are in series, the total capacitance is found using reciprocals: $\frac{1}{C_s} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$
6. The energy stored in a capacitor is given by $W = \frac{1}{2} C V^2$, $W = \frac{1}{2} Q V$, or $W = \frac{Q^2}{2C}$.

## Practice questions

**1. Which of the following is NOT a function of a capacitor?**
- A. Blocking direct current (DC)
- B. Smoothing rectified alternating current (AC)
- C. Generating electrical power
- D. Tuning radio frequencies

**Answer: C.** Capacitors store and release electrical energy; they do not generate their own power.

**2. A $2000\ \mu\text{F}$ capacitor is connected across a $12\ \text{V}$ battery. Calculate the charge stored in it.**
- A. $1.67 \times 10^{-4}\ \text{C}$
- B. $2.40 \times 10^{-2}\ \text{C}$
- C. $2.40 \times 10^{4}\ \text{C}$
- D. $1.44 \times 10^{-1}\ \text{C}$

**Answer: B.** 
1. $Q = C V$
2. $Q = (2000 \times 10^{-6}\ \text{F}) \times 12\ \text{V}$
3. $Q = 24000 \times 10^{-6}\ \text{C} = 0.024\ \text{C} = 2.40 \times 10^{-2}\ \text{C}$.
*(Mistake behind option C: forgetting to convert microfarads to Farads, just doing $2000 \times 12$).*

**3. If the distance between the plates of a parallel plate capacitor is halved, and the overlapping area of the plates is doubled, the capacitance will:**
- A. Be halved
- B. Remain the same
- C. Be doubled
- D. Be quadrupled

**Answer: D.** 
1. $C = \frac{\varepsilon A}{d}$.
2. If area becomes $2A$ and distance becomes $\frac{d}{2}$.
3. $C_{new} = \frac{\varepsilon (2A)}{d / 2} = 4 \left( \frac{\varepsilon A}{d} \right) = 4C$. The capacitance is multiplied by 4 (quadrupled).

**4. Two capacitors, $C_1 = 3\ \mu\text{F}$ and $C_2 = 6\ \mu\text{F}$, are connected in series. What is their equivalent capacitance?**
- A. $0.5\ \mu\text{F}$
- B. $2.0\ \mu\text{F}$
- C. $4.5\ \mu\text{F}$
- D. $9.0\ \mu\text{F}$

**Answer: B.** 
1. In series, $\frac{1}{C_s} = \frac{1}{3} + \frac{1}{6} = \frac{2}{6} + \frac{1}{6} = \frac{3}{6} = \frac{1}{2}$.
2. Invert to get $C_s = 2.0\ \mu\text{F}$. 
*(Mistake behind option D: adding them up directly, which is the rule for capacitors in parallel or resistors in series).*

**5. A capacitor of capacitance $4\ \mu\text{F}$ stores $8.0 \times 10^{-4}\ \text{J}$ of energy. What is the potential difference across its plates?**
- A. $10\ \text{V}$
- B. $20\ \text{V}$
- C. $200\ \text{V}$
- D. $400\ \text{V}$

**Answer: B.**
1. $W = \frac{1}{2} C V^2$
2. $8.0 \times 10^{-4} = \frac{1}{2} \times (4 \times 10^{-6}) \times V^2$
3. $8.0 \times 10^{-4} = 2 \times 10^{-6} \times V^2$
4. $V^2 = \frac{8.0 \times 10^{-4}}{2 \times 10^{-6}} = 4 \times 10^2 = 400$
5. $V = \sqrt{400} = 20\ \text{V}$. 
*(Mistake behind option D: forgetting to find the square root at the final step).*

**6. Which of the following dielectric materials would result in the highest capacitance if used in a parallel plate capacitor, assuming the plate dimensions remain the same?**
- A. Air ($\varepsilon_r = 1.0$)
- B. Paper ($\varepsilon_r = 3.5$)
- C. Mica ($\varepsilon_r = 6.0$)
- D. Ceramic ($\varepsilon_r = 1200$)

**Answer: D.** Capacitance is directly proportional to the relative permittivity ($\varepsilon_r$) of the dielectric. The material with the highest relative permittivity (Ceramic) will give the highest capacitance.

**7. Three identical capacitors, each of capacitance $C$, are connected in parallel. Their equivalent capacitance is $C_p$. If they are reconnected in series, their equivalent capacitance is $C_s$. What is the ratio $C_p : C_s$?**
- A. 1 : 9
- B. 3 : 1
- C. 9 : 1
- D. 1 : 3

**Answer: C.** 
1. In parallel, $C_p = C + C + C = 3C$.
2. In series, $\frac{1}{C_s} = \frac{1}{C} + \frac{1}{C} + \frac{1}{C} = \frac{3}{C}$, so $C_s = \frac{C}{3}$.
3. Ratio $C_p : C_s = 3C : \frac{C}{3} = 9 : 1$.

**8. In a given parallel plate capacitor, increasing the potential difference between the plates will:**
- A. Increase the capacitance
- B. Decrease the capacitance
- C. Increase the charge stored
- D. Decrease the charge stored

**Answer: C.** For a physical capacitor, its capacitance ($C$) is constant (set by its area, distance, and dielectric). Since $Q = CV$, increasing the voltage ($V$) will directly increase the charge ($Q$) stored on the plates.

**9. A $5\ \mu\text{F}$ capacitor and a $10\ \mu\text{F}$ capacitor are connected in parallel across a $6\ \text{V}$ battery. What is the total energy stored in the circuit?**
- A. $6.0 \times 10^{-5}\ \text{J}$
- B. $1.8 \times 10^{-4}\ \text{J}$
- C. $2.7 \times 10^{-4}\ \text{J}$
- D. $5.4 \times 10^{-4}\ \text{J}$

**Answer: C.** 
1. Total capacitance in parallel: $C_p = 5\ \mu\text{F} + 10\ \mu\text{F} = 15\ \mu\text{F}$.
2. Total energy: $W = \frac{1}{2} C_p V^2$
3. $W = \frac{1}{2} \times (15 \times 10^{-6}) \times 6^2 = \frac{1}{2} \times 15 \times 10^{-6} \times 36$
4. $W = 15 \times 10^{-6} \times 18 = 270 \times 10^{-6}\ \text{J} = 2.7 \times 10^{-4}\ \text{J}$. 
*(Mistake behind option D: forgetting the $\frac{1}{2}$ in the energy formula, getting $15 \times 36 = 5.4 \times 10^{-4}\ \text{J}$).*

**10. A parallel plate capacitor has a capacitance of $20\ \text{pF}$ in air. The area of the plates is $0.01\ \text{m}^2$. Calculate the separation distance between the plates. ($\varepsilon_0 = 8.85 \times 10^{-12}\ \text{F m}^{-1}$)**
- A. $1.77 \times 10^{-3}\ \text{m}$
- B. $2.21 \times 10^{-3}\ \text{m}$
- C. $4.43 \times 10^{-3}\ \text{m}$
- D. $8.85 \times 10^{-3}\ \text{m}$

**Answer: C.**
1. Formula: $C = \frac{\varepsilon_0 A}{d}$, which rearranges to $d = \frac{\varepsilon_0 A}{C}$.
2. Substitute with units: $C = 20 \times 10^{-12}\ \text{F}$, $A = 0.01\ \text{m}^2$.
3. $d = \frac{8.85 \times 10^{-12} \times 0.01}{20 \times 10^{-12}}$
4. The $10^{-12}$ terms cancel out: $d = \frac{0.0885}{20} = 0.004425\ \text{m}$.
5. In standard form: $d = 4.43 \times 10^{-3}\ \text{m}$.
