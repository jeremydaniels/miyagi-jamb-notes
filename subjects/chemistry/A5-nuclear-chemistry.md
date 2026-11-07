# JAMB Chemistry Notes: Nuclear Chemistry

## What JAMB expects

This topic is Section A, Topic 5 of the JAMB Chemistry syllabus: Nuclear Chemistry. It covers the inner workings of the atomic nucleus, how unstable nuclei break down, and the huge amounts of energy they release. 

By the end of these notes, you should be able to:
1. Distinguish between ordinary chemical reaction and nuclear reaction.
2. Differentiate between natural and artificial radioactivity.
3. Compare the properties of the different types of nuclear radiations.
4. Compute simple calculations on the half-life of a radioactive material.
5. Balance simple nuclear equation.
6. Identify the various applications of radioactivity.

**Note on the syllabus wording:** Objective (v) asks you to "balance simple nuclear equation" in the singular, but JAMB questions test this extensively using various different equations, so we will cover the balancing of multiple types of nuclear equations. This topic builds directly on your knowledge of isotopes and atomic structure from `A4-atomic-structure-and-bonding.md`.

---

## Distinguishing between chemical and nuclear reactions

**Objective i: distinguish between ordinary chemical reaction and nuclear reaction.**

Chemistry usually focuses on what happens to the electrons in the outer shells of atoms. In an **ordinary chemical reaction**, atoms interact by sharing, losing, or gaining valence electrons to form new chemical bonds and compounds. The central nucleus of the atom remains completely untouched.

However, in a **nuclear reaction**, changes occur deep inside the nucleus of the atom. Protons and neutrons are rearranged, added, or lost, which means one element actually changes into an entirely different element. The process of changing one element into another is called **transmutation**.

### Comparison Table: Chemical vs. Nuclear Reactions

| Feature | Ordinary Chemical Reaction | Nuclear Reaction |
| :--- | :--- | :--- |
| **Part of the atom involved** | Involves only outer (valence) **electrons**. | Involves protons, neutrons, and other particles in the **nucleus**. |
| **New elements** | No new elements are formed. Atoms are simply rearranged. | **New elements are formed** (transmutation occurs). |
| **Energy changes** | Relatively small amounts of energy are released or absorbed (e.g., in $\text{kJ mol}^{-1}$). | Enormous amounts of energy are released, millions of times greater than chemical reactions. |
| **Mass conservation** | Mass is strictly conserved (Law of Conservation of Mass). | Mass is not strictly conserved. A small amount of mass is converted into energy ($E = mc^2$). |
| **Effect of outside conditions** | Reaction rate is heavily affected by temperature, pressure, concentration, and catalysts. | Reaction rate is completely independent of temperature, pressure, and catalysts. |
| **Isotopes** | Different isotopes of the same element react in almost exactly the same way chemically. | Different isotopes of the same element behave completely differently (e.g., $^{235}_{92}\text{U}$ undergoes fission, $^{238}_{92}\text{U}$ does not). |

---

## Radioactivity: Types, properties and detection of radiations

**Content i: Radioactivity – Types, properties and detection of radiations.**

**Radioactivity** is the spontaneous disintegration (breakdown) of an unstable atomic nucleus to form a more stable nucleus, accompanied by the emission of radiation and energy. 

This phenomenon was discovered by Henri Becquerel in 1896 when he noticed that uranium salts darkened photographic plates. It was further studied by Marie and Pierre Curie, who discovered the radioactive elements polonium and radium. 

### Types of Nuclear Radiations
When an unstable nucleus decays, it emits one or more of three main types of radiation: **Alpha ($\alpha$) particles**, **Beta ($\beta$) particles**, and **Gamma ($\gamma$) rays**.

#### 1. Alpha particles ($\alpha$)
An alpha particle is identical to the nucleus of a helium atom. It consists of 2 protons and 2 neutrons, giving it a mass of 4 atomic mass units (amu) and a charge of $+2$. Its symbol is $^{4}_{2}\text{He}$ or $^{4}_{2}\alpha$.
Because they are heavy and highly charged, alpha particles crash violently into air molecules, knocking electrons off them (**ionization**). Consequently, they lose their energy very quickly and cannot travel far.

#### 2. Beta particles ($\beta$)
A beta particle is a fast-moving electron ejected from the nucleus. Since it is an electron, it has virtually zero mass (approx. $\frac{1}{1840}$ amu) and a charge of $-1$. Its symbol is $^{0}_{-1}\text{e}$ or $^{0}_{-1}\beta$. 
*How can a nucleus emit an electron if it only contains protons and neutrons?* This happens when a neutron in the nucleus breaks apart into a proton (which stays behind) and an electron (which is shot out as a beta particle).

#### 3. Gamma rays ($\gamma$)
Unlike alpha and beta radiations, gamma rays are not particles. They are high-energy **electromagnetic waves** (similar to X-rays but with even shorter wavelengths and higher energy). They have no mass and no charge, represented as $^{0}_{0}\gamma$. They are often emitted immediately after alpha or beta decay to release excess energy from the newly formed nucleus.

### Comparing properties of nuclear radiations
**Objective iii: compare the properties of the different types of nuclear radiations.**

The JAMB syllabus expects you to know how these radiations respond to barriers and electric fields.

| Property | Alpha ($\alpha$) | Beta ($\beta$) | Gamma ($\gamma$) |
| :--- | :--- | :--- | :--- |
| **Nature** | Helium nucleus ($^{4}_{2}\text{He}$) | Fast-moving electron ($^{0}_{-1}\text{e}$) | High-energy electromagnetic wave |
| **Mass** | $4 \text{ amu}$ (heavy) | $\sim \frac{1}{1840} \text{ amu}$ (very light) | $0$ (no mass) |
| **Charge** | $+2$ | $-1$ | $0$ (neutral) |
| **Penetrating power** | Very low. Stopped by a **sheet of paper** or human skin. | Moderate. Stopped by a **thin aluminium sheet** (approx. $5 \text{ mm}$ thick). | Very high. Stopped only by **thick lead** blocks or concrete. |
| **Ionizing power** | Very high (knocks many electrons off gas molecules). | Moderate. | Very low. |
| **Deflection in Electric/Magnetic fields** | Deflected towards the **negative** plate (because it is positive). Deflection is slight due to its heavy mass. | Deflected strongly towards the **positive** plate (because it is negative and very light). | **Not deflected** at all (because it has no charge). |

[IMAGE: A diagram showing the penetrating power of radiations. On the left, a radioactive source inside a lead box emits three rays pointing right. The thick alpha ray ($\alpha$) hits and is stopped completely by a white sheet of paper. The beta ray ($\beta$) easily passes through the paper but is stopped by a grey sheet of aluminium. The wavy gamma ray ($\gamma$) passes through both the paper and the aluminium, but is finally absorbed by a thick dark grey block of lead. Clean flat textbook style, white background.]

[IMAGE: A diagram showing the deflection of radiations in an electric field. A radioactive source at the bottom shoots a beam upwards between two vertical metal plates (the left plate is positively charged '+', the right is negatively charged '-'). The heavy $\alpha$ particle bends slightly towards the negative plate. The light $\beta$ particle bends sharply towards the positive plate. The wavy $\gamma$ ray goes straight up without any bending. Clean flat textbook style, white background.]

### Detection of Radiations
Because radiation is invisible and odourless, we detect it using special instruments that rely on its ionizing or photographic properties:
1.  **Geiger-Müller (GM) counter:** The most common device in laboratories. Radiation enters a tube filled with argon gas and ionizes it, creating a brief pulse of electricity. A counter registers these pulses as clicks or a digital reading. It is excellent for detecting beta and gamma rays.
2.  **Cloud chamber:** A glass chamber filled with supersaturated alcohol vapour. When radiation passes through, it creates a trail of ionized gas particles. The alcohol condenses on these ions, leaving a visible, cloud-like track. Alpha particles leave thick, straight tracks; beta particles leave thin, zig-zag tracks.
3.  **Photographic plates:** Radiation darkens photographic film. This is how radioactivity was discovered, and the principle is used today in radiation badges worn by hospital workers in radiology departments (e.g., at LUTH or UCH).
4.  **Scintillation counter:** Uses a fluorescent screen (like Zinc Sulphide, $\text{ZnS}$) which emits tiny flashes of light (scintillations) when struck by ionizing radiation.

---

## Natural and artificial radioactivity

**Content ii: Natural and artificial radioactivity.**
**Objective ii: differentiate between natural and artificial radioactivity.**

Radioactivity can either happen spontaneously in nature or be induced by human intervention in a laboratory.

### Natural Radioactivity
This is the **spontaneous emission** of radiation by naturally unstable nuclei. Elements with an atomic number greater than $82$ (like Uranium, Radium, and Radon) are naturally unstable due to their massive size. They break down on their own over time, completely unprovoked, emitting alpha, beta, or gamma rays to eventually become a stable element (usually an isotope of Lead). 

### Artificial Radioactivity (Artificial Transmutation)
Stable atoms can be forced to become radioactive. **Artificial radioactivity** occurs when stable nuclei are intentionally bombarded with fast-moving particles (like neutrons, protons, or alpha particles) in a laboratory or nuclear reactor. This bombardment upsets the neutron-to-proton ratio, making the stable nucleus unstable and causing it to emit radiation and change into a new, artificial isotope.
*Note:* Artificial radioactivity was first achieved in 1919 by Ernest Rutherford, who successfully bombarded nitrogen gas with alpha particles to produce an isotope of oxygen.

### Comparison: Natural vs. Artificial Radioactivity

| Feature | Natural Radioactivity | Artificial Radioactivity |
| :--- | :--- | :--- |
| **Cause** | Spontaneous (happens entirely on its own). | Induced (forced by bombarding a stable nucleus). |
| **Material involved** | Occurs in naturally heavy and unstable elements (e.g., Uranium, Thorium). | Usually starts with lighter, highly stable elements (e.g., Nitrogen, Aluminium). |
| **Control** | Cannot be controlled, sped up, or stopped. | Can be controlled by starting or stopping the particle bombardment. |
| **Products** | Generally emits alpha ($\alpha$), beta ($\beta$), or gamma ($\gamma$) rays. | Often emits protons ($^{1}_{1}\text{p}$), neutrons ($^{1}_{0}\text{n}$), or positrons alongside the newly formed isotopes. |

---

## Nuclear stability and radioactive decay

**Content iii: Nuclear stability and radioactive decay.**

What makes one atom stable and another radioactive? The stability of a nucleus depends heavily on its **Neutron-to-Proton ratio (n/p ratio)**.

Inside the nucleus, positively charged protons repel each other strongly due to electrostatic forces. Neutrons act like "nuclear glue," utilizing the *strong nuclear force* to hold the nucleus together. 
- For light elements (up to Calcium, atomic number $20$), a stable nucleus usually has an equal number of protons and neutrons (n/p ratio $\approx 1.0$). For example, $^{12}_{6}\text{C}$ is stable.
- As atoms get heavier, they need increasingly more neutrons than protons to offset the huge repulsion. The stable ratio gradually increases to about $1.5$ for heavy elements like Lead ($^{206}_{82}\text{Pb}$).

If a nucleus has an n/p ratio that is too high, too low, or if it is just too massive (atomic number $> 82$), it will undergo **radioactive decay** to reach a stable state:
1.  **Too many neutrons (n/p too high):** The nucleus undergoes **beta ($\beta$) decay**. A neutron transforms into a proton and an electron. This lowers the neutron count and increases the proton count, bringing the ratio back into balance.
2.  **Too massive ($Z > 82$):** The nucleus undergoes **alpha ($\alpha$) decay**, ejecting 2 protons and 2 neutrons at once to rapidly shed excess mass.

---

## Simple calculations on half-life

**Objective iv: compute simple calculations on the half-life of a radioactive material.**

The **half-life ($t_{1/2}$)** of a radioactive element is the time taken for exactly half of the radioactive atoms present in a given sample to decay. 

Half-life is a constant property for every radioactive isotope. It cannot be altered by temperature, pressure, or chemical combinations. Some isotopes have a half-life of billions of years (like Uranium-238, $t_{1/2} = 4.5 \times 10^9 \text{ years}$), while others have a half-life of a fraction of a second.

[IMAGE: A graph showing radioactive decay. The vertical axis is 'Amount of radioactive substance remaining' starting at $100\%$, then marked down at $50\%$, $25\%$, $12.5\%$. The horizontal axis is 'Time' marked in half-lives ($1, 2, 3, 4$). A smooth downward-curving line passes exactly through the points $(0, 100\%)$, $(1, 50\%)$, $(2, 25\%)$, $(3, 12.5\%)$. Clean flat textbook style, white background.]

### Formulas for Half-life
$N_t$: Amount of radioactive substance remaining at time $t$ (can be in $\text{g}$, $\text{mol}$, or percentage).
$N_0$: Original amount of radioactive substance (in $\text{g}$, $\text{mol}$, or percentage).
$t$: Total time elapsed (in $\text{s}$, $\text{days}$, $\text{years}$).
$t_{1/2}$: Half-life duration (in $\text{s}$, $\text{days}$, $\text{years}$).
$n$: Number of half-lives that have passed (dimensionless).

The simplest way to solve JAMB half-life questions is to use the formula:
$$N_t = N_0 \times \left(\frac{1}{2}\right)^n$$

Where the number of half-lives ($n$) is found by:
$$n = \frac{t}{t_{1/2}}$$

*(Note: While the decay constant formula $\lambda = \frac{0.693}{t_{1/2}}$ is taught in physics, the fractional method above is sufficient for all standard UTME Chemistry questions).*

### Worked Examples

**1. Finding the mass remaining**
A radioactive isotope has a half-life of $5.0 \text{ days}$. If the initial mass of the isotope is $20.0 \text{ g}$, what mass will remain after $15.0 \text{ days}$?

1. **State the given parameters:** Initial mass $N_0 = 20.0 \text{ g}$, total time $t = 15.0 \text{ days}$, half-life $t_{1/2} = 5.0 \text{ days}$.
2. **Calculate the number of half-lives ($n$):** Divide total time by the half-life length. $n = \frac{15.0 \text{ days}}{5.0 \text{ days}} = 3$.
3. **Write the half-life formula:** $N_t = N_0 \times \left(\frac{1}{2}\right)^n$.
4. **Substitute the values:** $N_t = 20.0 \text{ g} \times \left(\frac{1}{2}\right)^3$.
5. **Solve for final mass:** $N_t = 20.0 \text{ g} \times \frac{1}{8} = 2.5 \text{ g}$.
*(JAMB Shortcut: You can also count manually. The mass halves 3 times: $20.0 \text{ g} \rightarrow 10.0 \text{ g} \rightarrow 5.0 \text{ g} \rightarrow 2.5 \text{ g}$.)*

**2. Finding the half-life**
A $100.0 \text{ g}$ sample of a radioactive element decays to $12.5 \text{ g}$ in $60.0 \text{ years}$. Calculate its half-life.

1. **State the given parameters:** $N_0 = 100.0 \text{ g}$, $N_t = 12.5 \text{ g}$, total time $t = 60.0 \text{ years}$.
2. **Determine the number of half-lives ($n$):** Keep halving the original mass until you reach the final mass.
   $100.0 \text{ g} \rightarrow 50.0 \text{ g} \rightarrow 25.0 \text{ g} \rightarrow 12.5 \text{ g}$.
3. **Count the halving steps:** It took exactly 3 steps, so $n = 3$.
4. **Calculate the half-life:** $t_{1/2} = \frac{t}{n} = \frac{60.0 \text{ years}}{3} = 20.0 \text{ years}$.

**3. Finding the original mass**
A certain radioactive sample took $12.0 \text{ s}$ to decay to $4.0 \text{ g}$. If its half-life is $3.0 \text{ s}$, what was its original mass?

1. **State the given parameters:** Final mass $N_t = 4.0 \text{ g}$, total time $t = 12.0 \text{ s}$, half-life $t_{1/2} = 3.0 \text{ s}$.
2. **Calculate the number of half-lives ($n$):** $n = \frac{12.0 \text{ s}}{3.0 \text{ s}} = 4$.
3. **Write the formula and rearrange:** $N_t = N_0 \times \left(\frac{1}{2}\right)^n \implies 4.0 \text{ g} = N_0 \times \left(\frac{1}{2}\right)^4$.
4. **Solve the fraction:** $4.0 \text{ g} = N_0 \times \frac{1}{16}$.
5. **Calculate $N_0$:** $N_0 = 4.0 \text{ g} \times 16 = 64.0 \text{ g}$.

> **Common Mistakes:** When calculating the amount remaining, students sometimes divide the original mass by $n$ (the number of half-lives). 
> *Wrong working:* For $20.0 \text{ g}$ over 3 half-lives, $20.0 \text{ g} / 3 = 6.67 \text{ g}$.
> *Correct working:* Multiply the mass by $(1/2)$ three separate times: $20.0 \text{ g} \times (1/2)^3 = 2.5 \text{ g}$.

---

## Balancing simple nuclear equations

**Objective v: balance simple nuclear equation.**

In any balanced nuclear equation, the sum of the top numbers and the sum of the bottom numbers must be equal on both sides of the arrow.
- **Top numbers (Mass numbers, superscripts, $A$):** The sum of mass numbers on the left = the sum of mass numbers on the right.
- **Bottom numbers (Atomic numbers, subscripts, $Z$):** The sum of atomic numbers on the left = the sum of atomic numbers on the right.

### The particles you must memorize for balancing
- Alpha particle: $^{4}_{2}\text{He}$ or $^{4}_{2}\alpha$
- Beta particle: $^{0}_{-1}\text{e}$ or $^{0}_{-1}\beta$
- Neutron: $^{1}_{0}\text{n}$
- Proton: $^{1}_{1}\text{p}$ or $^{1}_{1}\text{H}$
- Gamma ray: $^{0}_{0}\gamma$ (Does not change mass or atomic number)

### Worked Examples of Balancing

**1. Alpha Decay**
Determine the missing nucleus $Y$ in the equation:
$$^{226}_{88}\text{Ra} \rightarrow ^{A}_{Z}\text{Y} + ^{4}_{2}\text{He}$$

1. **Balance the top numbers (mass):** Left side is $226$. Right side must be $226$. So, $226 = A + 4 \implies A = 226 - 4 = 222$.
2. **Balance the bottom numbers (atomic):** Left side is $88$. Right side must be $88$. So, $88 = Z + 2 \implies Z = 88 - 2 = 86$.
3. **Identify the element:** Look for atomic number $86$ on the periodic table (JAMB typically provides this in the question options). Element $86$ is Radon ($\text{Rn}$).
4. **Final Answer:** The missing nucleus $Y$ is $^{222}_{86}\text{Rn}$.

**2. Beta Decay**
Determine the missing particle $X$ in the equation:
$$^{14}_{6}\text{C} \rightarrow ^{14}_{7}\text{N} + \text{X}$$

1. **Balance the top numbers:** $14 = 14 + \text{mass of X} \implies \text{mass} = 0$.
2. **Balance the bottom numbers:** $6 = 7 + \text{atomic number of X} \implies \text{atomic number} = 6 - 7 = -1$.
3. **Identify the particle:** A particle with a mass of $0$ and an atomic number of $-1$ is a beta particle ($^{0}_{-1}\text{e}$).

**3. Artificial Transmutation**
Find the missing particle $Q$ in the reaction:
$$^{27}_{13}\text{Al} + ^{4}_{2}\text{He} \rightarrow ^{30}_{15}\text{P} + \text{Q}$$

1. **Find total top and bottom numbers on the left:** Total mass = $27 + 4 = 31$. Total atomic number = $13 + 2 = 15$.
2. **Balance the top numbers:** $31 = 30 + \text{mass of Q} \implies \text{mass} = 1$.
3. **Balance the bottom numbers:** $15 = 15 + \text{atomic number of Q} \implies \text{atomic number} = 0$.
4. **Identify the particle:** A particle with mass $1$ and atomic number $0$ is a neutron ($^{1}_{0}\text{n}$).

---

## Nuclear reactions: Nuclear fusion and fission

**Content iv: Nuclear reactions: Nuclear fusion and fission.**

Artificial nuclear reactions can release vast amounts of energy, mainly via two major processes: Nuclear Fission and Nuclear Fusion.

### 1. Nuclear Fission
**Nuclear fission** is the splitting of a heavy, unstable nucleus into two lighter nuclei of roughly equal mass, accompanied by the release of a massive amount of energy and additional neutrons.
This process is usually triggered by bombarding a heavy nucleus with a slow-moving neutron.

*Example equation (Fission of Uranium-235):*
$$^{235}_{92}\text{U} + ^{1}_{0}\text{n} \rightarrow ^{141}_{56}\text{Ba} + ^{92}_{36}\text{Kr} + 3^{1}_{0}\text{n} + \text{Energy}$$

Notice that $1$ neutron starts the reaction, but $3$ neutrons are released at the end. These $3$ new neutrons can hit $3$ more Uranium-235 atoms, releasing $9$ neutrons, which hit $9$ more atoms, and so on. This rapidly multiplying effect is called a **chain reaction**.
- If the chain reaction is **controlled** (by absorbing excess neutrons using boron or cadmium rods), it is used to generate steady electricity in a **nuclear power plant**.
- If the chain reaction is **uncontrolled**, it leads to a massive, instantaneous explosion—an **atomic bomb**. The minimum amount of fissile material needed to sustain this uncontrolled chain reaction is called the **critical mass**.

[IMAGE: Diagram of a nuclear chain reaction. A single blue sphere (a neutron) strikes a large red atom (Uranium-235), which splits into two medium-sized atoms (Barium and Krypton) and releases three new blue neutrons. These three neutrons fly out and each hit another Uranium atom, causing them to split and release more neutrons, creating a cascading tree-like structure of splitting atoms. Clean flat textbook style, white background.]

### 2. Nuclear Fusion
**Nuclear fusion** is the exact opposite of fission. It is the combining of two light nuclei to form a heavier, more stable nucleus, releasing an even greater amount of energy per gram of fuel than fission.

*Example equation (Fusion of hydrogen isotopes):*
$$^{2}_{1}\text{H} + ^{3}_{1}\text{H} \rightarrow ^{4}_{2}\text{He} + ^{1}_{0}\text{n} + \text{Energy}$$
(Deuterium + Tritium $\rightarrow$ Helium + Neutron)

Because both light nuclei are positively charged, they repel each other strongly. To force them to fuse, extreme temperatures (millions of degrees Kelvin) and high pressures are required to overcome the repulsion. Therefore, fusion reactions are also called **thermonuclear reactions**.
- Nuclear fusion is the process that continuously powers the **Sun** and all other stars.
- On Earth, humans have only successfully achieved uncontrolled fusion in the form of the **hydrogen bomb**, which actually requires a smaller atomic (fission) bomb just to provide the initial heat needed to start the fusion!

### Comparing Fission and Fusion

| Feature | Nuclear Fission | Nuclear Fusion |
| :--- | :--- | :--- |
| **Process** | Splitting of a heavy nucleus into lighter ones. | Combining of light nuclei into a heavier one. |
| **Material used** | Heavy elements (e.g., $^{235}_{92}\text{U}$, $^{239}_{94}\text{Pu}$). | Light elements (e.g., $^{2}_{1}\text{H}$, $^{3}_{1}\text{H}$). |
| **Conditions** | Can occur at room temperature if bombarded by a slow neutron. | Requires extremely high temperatures (thermonuclear). |
| **Energy produced** | Very high. | Even higher than fission (about 3 to 4 times more energy per unit mass). |
| **Applications** | Nuclear reactors (power generation), Atomic bombs. | Powers the Sun/stars, Hydrogen bombs. |

---

## Applications of radioactivity

**Objective vi: identify the various applications of radioactivity.**

Despite its severe health risks, radioactivity is incredibly useful in modern society when handled correctly.

1.  **Medicine:** 
    - **Radiotherapy:** Gamma rays from Cobalt-60 ($^{60}\text{Co}$) are directed at tumors to kill cancer cells without invasive surgery. Major hospitals in Nigeria (like LUTH and UCH) have specialized radiotherapy machines for this.
    - **Medical Tracers:** Small amounts of radioactive isotopes are injected into the body to trace biological processes. For example, Iodine-131 ($^{131}\text{I}$) is used to check thyroid gland function, and Sodium-24 ($^{24}\text{Na}$) traces blood flow.
2.  **Scientific Research (Dating):** 
    - **Carbon-14 dating:** Used by archaeologists to find the age of ancient organic remains (such as the famous Nok terracotta artifacts found in Nigeria, which contained organic residue). Living things absorb Carbon-14 while alive; when they die, it slowly decays at a known half-life ($5,730 \text{ years}$).
    - **Uranium-Lead dating:** Used by geologists to date the age of very old rocks and the Earth itself.
3.  **Industry:** 
    - **Thickness gauging:** Beta particles are passed through sheets of paper, plastics, or metal foils during factory manufacturing. If the sheet gets too thick, fewer beta particles pass through to the detector, signaling the machine to press harder.
    - **Pipeline testing:** Gamma rays are used like industrial X-rays to detect hidden cracks or weak welds in underground oil pipelines, a vital technique in the Niger Delta petroleum industry.
4.  **Agriculture:** 
    - Radioactive Phosphorus-32 ($^{32}\text{P}$) is added to fertilizers. By detecting where the radiation goes in the plant, scientists can discover the best way plants absorb nutrients.
    - Radiation is used to induce mutations in seeds to develop new, stronger crop varieties.
5.  **Energy Generation:** 
    - Nuclear reactors use the controlled fission of Uranium-235 to produce massive amounts of heat. This heat boils water into steam, driving turbines to generate electricity. Nigeria possesses a miniature neutron source research reactor (NIRR-1) situated at Ahmadu Bello University in Zaria, used for scientific training rather than power generation.

**Hazards of Radioactivity:** Overexposure to radiation damages living tissue (radiation sickness) and mutates DNA, which can cause cancer and severe birth defects. Therefore, radioactive materials must always be handled with tongs from a safe distance, monitored with radiation badges, and stored in thick lead containers.

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Radioactivity** | Spontaneous breakdown of an unstable atomic nucleus with the emission of radiation and energy. |
| **Transmutation** | The conversion of an atom of one element into an atom of another element. |
| **Half-life ($t_{1/2}$)** | The time taken for exactly half the number of radioactive atoms in a sample to decay. |
| **Alpha particle ($\alpha$)** | A positively charged particle identical to a helium nucleus ($^{4}_{2}\text{He}$). |
| **Beta particle ($\beta$)** | A high-speed electron ($^{0}_{-1}\text{e}$) emitted from the nucleus during decay. |
| **Gamma ray ($\gamma$)** | High-energy electromagnetic radiation with zero mass and zero charge. |
| **Nuclear Fission** | Splitting of a heavy nucleus into two lighter nuclei, releasing immense energy. |
| **Nuclear Fusion** | Combining of two light nuclei into a heavier one, releasing even greater energy. |
| **Chain Reaction** | A self-sustaining reaction where the products (neutrons) from one fission event trigger further fission events. |
| **Isotope Tracer** | A radioactive substance introduced into a chemical or biological system to track processes. |

---

## Exam tips and common mistakes

- **Unit slips in half-life:** Always make sure the total time passed ($t$) and the half-life ($t_{1/2}$) are in the exact same units before dividing them to find $n$. You cannot divide $2 \text{ hours}$ by $30 \text{ minutes}$; convert hours to minutes first!
- **Not knowing the power of 2:** Remember the sequence of fractions remaining: 1 half-life = $1/2$; 2 half-lives = $1/4$; 3 half-lives = $1/8$; 4 half-lives = $1/16$; 5 half-lives = $1/32$.
- **Confusing fusion and fission:** Look at the letters. F**u**sion brings things together (**u**nite). Fi**ss**ion breaks things apart (**s**plit).
- **Gamma has NO mass and NO charge:** In balancing equations, adding a gamma ray ($^{0}_{0}\gamma$) changes absolutely nothing about the mass or atomic number of the products.
- **Isotopes in medicine:** JAMB loves asking about specific isotopes. Memorize: **Iodine-131** for the thyroid, **Cobalt-60** for cancer therapy, and **Carbon-14** for archaeological dating.

---

## Quick summary

1. Nuclear reactions involve changes to the atomic nucleus, form new elements, and release massive energy, unlike chemical reactions which only rearrange outer valence electrons.
2. Natural radioactivity happens spontaneously in heavy elements; artificial radioactivity is forced by bombarding stable nuclei with fast-moving particles.
3. Alpha particles ($^{4}_{2}\text{He}$) are heavy, easily stopped (paper), but highly ionizing. Beta particles ($^{0}_{-1}\text{e}$) are fast electrons with moderate penetration. Gamma rays ($^{0}_{0}\gamma$) are highly penetrating electromagnetic waves stopped only by lead.
4. Half-life is the time it takes for half of a radioactive sample to decay. The remaining mass formula is $N_t = N_0 \times (1/2)^n$, where $n$ is the number of half-lives.
5. In nuclear equations, the sum of superscripts (masses) and the sum of subscripts (atomic numbers) must be exactly equal on both sides of the arrow.
6. Fission splits heavy nuclei (like Uranium), creating chain reactions used in power plants. Fusion joins light nuclei (like Hydrogen) under extreme heat, powering the Sun.
7. Radioactivity has critical uses in cancer therapy (Cobalt-60), tracing diseases (Iodine-131), dating ancient artifacts (Carbon-14), industrial pipeline testing, and energy generation.

---

## Practice questions

**1. Which of the following is true of a nuclear reaction but NOT true of an ordinary chemical reaction?**
- A. Valence electrons are transferred or shared.
- B. Mass is perfectly conserved.
- C. A new element is formed.
- D. The reaction rate increases when temperature is increased.

**Answer: C.** 
1. In an ordinary chemical reaction, atoms merely rearrange their valence electrons (e.g., forming $\text{H}_2\text{O}$).
2. In a nuclear reaction, the nucleus changes its number of protons ($Z$), resulting in a completely new element (e.g., $^{238}_{92}\text{U} \rightarrow ^{234}_{90}\text{Th} + ^{4}_{2}\text{He}$). 
3. The most tempting wrong option is A, because transferring electrons accurately describes a chemical reaction, but not a nuclear one.

**2. The phenomenon of artificial radioactivity was first discovered by bombarding a stable nitrogen nucleus with:**
- A. neutrons
- B. beta particles
- C. alpha particles
- D. gamma rays

**Answer: C.** 
1. Ernest Rutherford originally bombarded stable nitrogen gas ($^{14}_{7}\text{N}$) with a specific heavy particle. 
2. The nuclear equation is $^{14}_{7}\text{N} + ^{4}_{2}\text{He} \rightarrow ^{17}_{8}\text{O} + ^{1}_{1}\text{H}$. 
3. The particle $^{4}_{2}\text{He}$ is an alpha particle. 
4. The most tempting wrong option is A (neutrons), because neutrons are heavily used in modern artificial transmutations (like fission), but Rutherford's pioneering experiment used alpha particles.

**3. Which of the following radiations has the highest penetrating power and zero charge?**
- A. Alpha particles
- B. Beta particles
- C. Gamma rays
- D. Protons

**Answer: C.** 
1. Alpha particles ($^{4}_{2}\text{He}$) have a $+2$ charge and very low penetration. 
2. Beta particles ($^{0}_{-1}\text{e}$) have a $-1$ charge and moderate penetration. 
3. Gamma rays ($^{0}_{0}\gamma$) have $0$ mass and $0$ charge, giving them the highest penetrating power (stopped only by thick lead). 
4. The most tempting wrong option is B (beta particles), because beta penetrates more deeply than alpha, but gamma penetrates far more and is uniquely uncharged.

**4. A radioactive sample has a half-life of $10.0 \text{ days}$. If its initial mass is $80.0 \text{ g}$, what mass will remain after $40.0 \text{ days}$?**
- A. $40.0 \text{ g}$
- B. $5.0 \text{ g}$
- C. $20.0 \text{ g}$
- D. $10.0 \text{ g}$

**Answer: B.** 
1. Determine the number of half-lives: $n = \frac{40.0 \text{ days}}{10.0 \text{ days}} = 4$. 
2. Use the decay formula: $N_t = 80.0 \text{ g} \times (1/2)^4$. 
3. Substitute the fraction: $N_t = 80.0 \text{ g} \times \frac{1}{16} = 5.0 \text{ g}$. 
4. The most tempting wrong option is C ($20.0 \text{ g}$), because a student might mistakenly divide the initial mass by the number of half-lives ($80.0 \text{ g} / 4 = 20.0 \text{ g}$) instead of correctly halving it 4 times.

**5. The mass of a radioactive substance drops from $32.0 \text{ g}$ to $2.0 \text{ g}$ in $60.0 \text{ years}$. What is its half-life?**
- A. $15.0 \text{ years}$
- B. $12.0 \text{ years}$
- C. $30.0 \text{ years}$
- D. $240.0 \text{ years}$

**Answer: A.** 
1. Halve $32.0 \text{ g}$ successively to reach $2.0 \text{ g}$: $32.0 \rightarrow 16.0 \rightarrow 8.0 \rightarrow 4.0 \rightarrow 2.0 \text{ g}$. This requires $n = 4$ halving steps. 
2. Calculate the half-life: $t_{1/2} = \frac{60.0 \text{ years}}{4} = 15.0 \text{ years}$. 
3. The most tempting wrong option is C ($30.0 \text{ years}$), because a student might mistakenly divide $32.0$ by $16.0$ to get $2.0$ and wrongly assume $n = 2$, calculating $\frac{60.0 \text{ years}}{2} = 30.0 \text{ years}$.

**6. In the nuclear reaction $^{238}_{92}\text{U} \rightarrow ^{234}_{90}\text{Th} + \text{X}$, the particle X is:**
- A. a neutron
- B. a beta particle
- C. an alpha particle
- D. a positron

**Answer: C.** 
1. Balance the mass numbers (top): $238 - 234 = 4$. 
2. Balance the atomic numbers (bottom): $92 - 90 = 2$. 
3. Particle X is $^{4}_{2}\text{X}$, which is the helium nucleus, or alpha particle ($^{4}_{2}\text{He}$). 
4. The most tempting wrong option is B (a beta particle, $^{0}_{-1}\text{e}$), because students frequently confuse alpha and beta decay rules, but beta decay would increase the atomic number to $93$.

**7. Balance the following nuclear equation: $^{9}_{4}\text{Be} + ^{4}_{2}\text{He} \rightarrow ^{12}_{6}\text{C} + \text{Y}$. Particle Y is a:**
- A. proton
- B. beta particle
- C. neutron
- D. gamma ray

**Answer: C.** 
1. Calculate the total mass on the left: $9 + 4 = 13$. The right side has Carbon at $12$, so Y's mass is $13 - 12 = 1$. 
2. Calculate the total charge on the left: $4 + 2 = 6$. The right side has Carbon at $6$, so Y's charge is $6 - 6 = 0$. 
3. The particle with mass $1$ and charge $0$ is a neutron, $^{1}_{0}\text{n}$. 
4. The most tempting wrong option is A (proton, $^{1}_{1}\text{p}$), because a student might quickly misadd the bottom numbers ($4+2=5$) or confuse the proton's $+1$ charge with the neutron's $0$ charge.

**8. Which of the following statements correctly distinguishes nuclear fusion from nuclear fission?**
- A. Fusion splits $^{235}_{92}\text{U}$, while fission combines $^{2}_{1}\text{H}$.
- B. Fusion occurs at $25\text{ }^\circ\text{C}$, while fission requires $10^7\text{ K}$.
- C. Fusion combines light nuclei like $^{2}_{1}\text{H}$, while fission splits heavy nuclei like $^{235}_{92}\text{U}$.
- D. Fusion releases $10 \text{ kJ}$, while fission releases $1000 \text{ kJ}$.

**Answer: C.** 
1. Nuclear fusion is the joining of light nuclei (e.g., $^{2}_{1}\text{H} + ^{3}_{1}\text{H} \rightarrow ^{4}_{2}\text{He} + ^{1}_{0}\text{n}$) under extreme heat. 
2. Nuclear fission is the splitting of a heavy nucleus (e.g., $^{235}_{92}\text{U}$) using slow neutrons. 
3. The most tempting wrong option is A, because it perfectly swaps the definitions; students often confuse the English terms "fusion" (uniting) and "fission" (splitting).

**9. Which radioactive isotope is commonly used in medicine to specifically treat cancer of the thyroid gland?**
- A. $^{14}_{6}\text{C}$
- B. $^{131}_{53}\text{I}$
- C. $^{235}_{92}\text{U}$
- D. $^{32}_{15}\text{P}$

**Answer: B.** 
1. Medical treatments use radioisotopes that naturally target specific biological organs based on their chemical properties and half-life ($t_{1/2}$). 
2. The element Iodine naturally accumulates in the thyroid gland. Therefore, Iodine-131 ($^{131}_{53}\text{I}$) is used to deliver localized radiation to destroy thyroid cancer cells. 
3. The most tempting wrong option is A ($^{14}_{6}\text{C}$), because Carbon-14 is the most famous radioisotope, but it is strictly used for archaeological dating, not medical treatment.

**10. Which device detects ionizing radiation by forming visible tracks of condensation in a supersaturated alcohol vapour?**
- A. Geiger-Müller counter
- B. Scintillation counter
- C. Cloud chamber
- D. Photographic plate

**Answer: C.** 
1. Different detectors use different mechanisms: GM counters use ionized argon gas, and scintillation counters use fluorescent screens (like $\text{ZnS}$). 
2. A cloud chamber operates using a supersaturated alcohol vapour. 
3. As charged particles (like $\alpha$ or $\beta$) pass through, they ionize the gas, causing the vapour to condense and leave a visible track. 
4. The most tempting wrong option is A (Geiger-Müller counter), because it is the most well-known radiation detector, but it works by registering electrical pulses in a gas, not visual tracks in a vapour.
