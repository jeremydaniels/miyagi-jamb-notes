# JAMB Physics Notes: Heat Transfer

## What JAMB expects

This topic covers Section A, Topic 19 of the JAMB Physics syllabus: Heat Transfer. It includes the following content items:

* (i) conduction, convection and radiation as modes of heat transfer;
* (ii) temperature gradient, thermal conductivity and heat flux;
* (iii) effect of the nature of the surface on the energy radiated and absorbed by it;
* (iv) the conductivities of common materials;
* (v) the thermos flask/vacuum flask;
* (vi) land and sea breeze;
* (vii) combustion engines.

By the end of these notes, you should be able to:

* i. differentiate between conduction, convection and radiation as modes of heat transfer;
* ii. solve problems on temperature gradient, thermal conductivity and heat flux;
* iii. assess the effect of the nature of the surface on the energy radiated and absorbed by it;
* iv. compare the conductivities of common materials;
* v. relate the component part of the working of the thermos flask;
* vi. differentiate between land and sea breeze;
* vii. analyse the principles of operating internal combustion jet engines, rockets;
* viii. understand the advantages and disadvantages of electric engine over combustion engine.

---

## Modes of Heat Transfer

**Objective i: differentiate between conduction, convection and radiation as modes of heat transfer.**

Heat is a form of energy that flows from a region of higher temperature to a region of lower temperature. This transfer of thermal energy happens in three different ways: **conduction**, **convection**, and **radiation**. 

### 1. Conduction
Conduction is the transfer of heat through a material without any bulk movement of the material itself. It is the primary mode of heat transfer in **solids**. 
When one end of a solid is heated, the atoms or molecules at that end gain kinetic energy and vibrate more vigorously. They collide with neighbouring particles, passing the energy along the material. Metals are excellent conductors because they also have "free electrons" that drift through the metal, carrying thermal energy quickly from the hot end to the cold end.

### 2. Convection
Convection is the transfer of heat by the actual physical movement of the heated fluid (a liquid or a gas). 
When a fluid is heated, it expands, becomes less dense, and rises. The colder, denser fluid moves down to replace it. This creates a continuous cycle known as a **convection current**. For example, when you boil a pot of water on a gas cooker, the water at the bottom gets hot, rises to the top, and the cooler water sinks to be heated.

### 3. Radiation
Radiation is the transfer of heat in the form of electromagnetic waves (specifically, infrared radiation). Unlike conduction and convection, radiation **does not require a material medium**; it can travel through a perfect vacuum (empty space). This is how the heat from the Sun reaches the Earth through the vacuum of space.

### Comparison Table

| Feature | Conduction | Convection | Radiation |
| --- | --- | --- | --- |
| **Medium required?** | Yes (mostly solids) | Yes (liquids and gases) | No (can travel through a vacuum) |
| **Movement of particles?** | No bulk movement (only vibration) | Actual bulk movement of particles | No particles involved (waves) |
| **Speed of transfer** | Slow | Moderate | Very fast (speed of light: $3 \times 10^8\ \text{m s}^{-1}$) |
| **Example** | An iron rod left in a fire getting hot at the other end | Boiling water; warm air rising above a fire | Feeling the heat of the sun or a campfire from a distance |

[IMAGE: A three-part illustration. Left: a hand holding a metal rod with its tip in a campfire (labeled "Conduction"). Middle: arrows showing water circulating in a pot over the fire, with warm water rising and cool water sinking (labeled "Convection"). Right: wavy lines carrying heat directly from the fire to a pair of hands held beside it (labeled "Radiation"). Clean flat textbook illustration, white background.]

---

## Temperature Gradient, Thermal Conductivity and Heat Flux

**Objective ii: solve problems on temperature gradient, thermal conductivity and heat flux.**

When heat flows through a solid by conduction, the rate at which the heat flows depends on the material, its dimensions, and the temperature difference across it.

### Temperature Gradient
The **temperature gradient** is the rate at which temperature changes with distance along a material. If a material has a hot face at temperature $\theta_2$ and a cold face at temperature $\theta_1$, separated by a thickness or length $L$, the temperature gradient is:

$$ \text{Temperature Gradient} = \frac{\theta_2 - \theta_1}{L} = \frac{\Delta \theta}{L} $$

*   **Unit:** Kelvin per metre ($\text{K m}^{-1}$) or degrees Celsius per metre ($^\circ\text{C m}^{-1}$). Since we are dealing with a temperature *difference*, $1\ \text{K}$ difference is exactly equal to $1^\circ\text{C}$ difference. 

### Rate of Heat Transfer
The rate of heat transfer (or heat flow rate) is the amount of heat energy $Q$ transferred per second ($t$). 

$$ H = \frac{Q}{t} $$

*   **Unit:** Joules per second ($\text{J s}^{-1}$) or Watts ($\text{W}$).

The rate of heat transfer $H$ through a uniform slab is:
1. Directly proportional to the cross-sectional area $A$.
2. Directly proportional to the temperature difference $\Delta \theta$.
3. Inversely proportional to the length or thickness $L$.

Putting this together gives the fundamental formula for thermal conduction:

$$ \frac{Q}{t} = \frac{k A (\theta_2 - \theta_1)}{L} $$

*   **$Q$** = Total heat transferred in joules ($\text{J}$).
*   **$t$** = Time taken in seconds ($\text{s}$).
*   **$A$** = Cross-sectional area in square metres ($\text{m}^2$).
*   **$\Delta \theta$** = Temperature difference ($\text{K}$ or $^\circ\text{C}$).
*   **$L$** = Length or thickness in metres ($\text{m}$).
*   **$k$** = **Thermal conductivity**, a constant that depends on the material. Its unit is $\text{W m}^{-1}\ \text{K}^{-1}$.

### Heat Flux
**Heat flux** is the rate of heat transfer *per unit cross-sectional area*. 

$$ \Phi = \frac{H}{A} = \frac{Q}{A t} = \frac{k (\theta_2 - \theta_1)}{L} $$

*   **Unit:** Watts per square metre ($\text{W m}^{-2}$).

*Textbook variation note:* Some older Nigerian textbooks use the term "heat flux" loosely to mean just the total rate of heat flow ($Q/t$). However, in standard physics and JAMB exams, "heat flux" usually strictly means heat flow per unit area ($W\ m^{-2}$). Always check the units in the options to see which one JAMB wants.

### Worked Examples

**1. Calculating Temperature Gradient**
A solid concrete wall is $0.2\ \text{m}$ thick. The temperature on the outside is $35^\circ\text{C}$ and on the inside is $25^\circ\text{C}$. Calculate the temperature gradient across the wall.

*Working:*
1. State the given values: $\theta_2 = 35^\circ\text{C}$, $\theta_1 = 25^\circ\text{C}$, $L = 0.2\ \text{m}$.
2. Calculate the temperature difference: $\Delta \theta = 35 - 25 = 10\ \text{K}$.
3. Apply the formula: $\text{Temperature gradient} = \frac{\Delta \theta}{L}$.
4. Substitute: $\frac{10}{0.2} = 50$.
5. State the answer with unit: $50\ \text{K m}^{-1}$.

**2. Calculating Heat Flux**
A glass window has a thickness of $0.005\ \text{m}$ ($5\ \text{mm}$) and a thermal conductivity of $0.8\ \text{W m}^{-1}\ \text{K}^{-1}$. During the harmattan, the temperature inside a room is $25^\circ\text{C}$ while outside is $15^\circ\text{C}$. Calculate the heat flux through the glass.

*Working:*
1. State the formula for heat flux: $\Phi = \frac{k \Delta \theta}{L}$.
2. Identify values: $k = 0.8\ \text{W m}^{-1}\ \text{K}^{-1}$, $\Delta \theta = 25 - 15 = 10\ \text{K}$, $L = 0.005\ \text{m}$.
3. Substitute: $\Phi = \frac{0.8 \times 10}{0.005}$.
4. Calculate: $\Phi = \frac{8}{0.005} = 1600$.
5. State the answer with unit: $1600\ \text{W m}^{-2}$.

**3. Calculating Total Heat Transferred**
A copper rod of length $0.5\ \text{m}$ and cross-sectional area $4.0 \times 10^{-4}\ \text{m}^2$ connects a boiling water bath at $100^\circ\text{C}$ to an ice bath at $0^\circ\text{C}$. If the thermal conductivity of copper is $400\ \text{W m}^{-1}\ \text{K}^{-1}$, calculate the total heat transferred through the rod in $1\ \text{minute}$.

*Working:*
1. Convert time to seconds: $t = 1\ \text{minute} = 60\ \text{s}$.
2. Identify values: $k = 400\ \text{W m}^{-1}\ \text{K}^{-1}$, $A = 4.0 \times 10^{-4}\ \text{m}^2$, $\Delta \theta = 100 - 0 = 100\ \text{K}$, $L = 0.5\ \text{m}$.
3. State the formula for total heat: $Q = \frac{k A \Delta \theta t}{L}$.
4. Substitute values: $Q = \frac{400 \times (4.0 \times 10^{-4}) \times 100 \times 60}{0.5}$.
5. Simplify the numerator: $400 \times 0.0004 = 0.16$. Then $0.16 \times 100 = 16$. Then $16 \times 60 = 960$.
6. Divide by length: $Q = \frac{960}{0.5} = 1920$.
7. State the answer with unit: $1920\ \text{J}$.

**Common Mistake:** Forgetting to convert time into seconds (e.g. using $1$ minute instead of $60\ \text{s}$) or thickness from mm to m. Always stick to standard SI units.

---

## Radiation: Effect of the Nature of the Surface

**Objective iii: assess the effect of the nature of the surface on the energy radiated and absorbed by it.**

All objects emit radiant heat (infrared radiation). However, the rate at which a surface emits or absorbs radiation depends heavily on its colour and texture.

*   **Dull, black (or dark) surfaces** are the **best absorbers** of radiant heat. They are also the **best emitters** (radiators) of heat.
*   **Shiny, white (or highly polished) surfaces** are **poor absorbers** and **poor emitters** of radiant heat. Instead, they reflect most of the radiation that hits them.

**Leslie's Cube Experiment**
This principle is usually demonstrated using a hollow metal box called a Leslie's cube, which has four different vertical faces (e.g., dull black, shiny black, dull white, and shiny silver). When filled with boiling water, a thermopile (a heat sensor) placed at equal distances from each face will detect the highest radiation from the dull black face and the lowest from the shiny silver face.

**Everyday Examples in Nigeria:**
*   **Roofing:** A rusty, dark zinc roof will absorb a lot of heat from the sun, making the house hot. Painting the roof white or using shiny aluminium reflects the sun's radiation, keeping the interior cooler.
*   **Clothing:** Wearing dark clothes on a hot, sunny afternoon in Lagos makes you feel much hotter than wearing white clothes, because dark colours absorb more radiant heat.
*   **Cooling fins:** The cooling fins on the cylinder block of an Okada (motorcycle) engine are often painted dull black so they can emit (radiate) heat rapidly away from the engine.

---

## Conductivities of Common Materials

**Objective iv: compare the conductivities of common materials.**

Materials vary widely in their ability to conduct heat (their thermal conductivity, $k$). 

### Good Conductors
Materials with high thermal conductivity allow heat to pass through them quickly. **Metals** are generally excellent conductors because of their free electrons. 
*Examples:* Silver (the best), Copper, Aluminium, Iron, Brass.
*Uses:* Copper and aluminium are used to make cooking pots and frying pans because they conduct heat rapidly from the fire to the food. 

### Poor Conductors (Insulators)
Materials with low thermal conductivity strongly resist the flow of heat. **Non-metals, liquids, and gases** are generally poor conductors. 
*Examples:* Wood, plastic, glass, cork, asbestos, air, and water.
*Uses:* 
*   The handles of cooking pots are made of wood or hard plastic so they do not conduct heat to the user's hands.
*   Many houses in rural Nigeria use thatch roofs. Thatch traps a lot of air (a very poor conductor), making it a good insulator. This keeps the house cool in the dry season and warm during the cold harmattan nights, unlike metal roofs which conduct heat rapidly.

| Material | Thermal Conductivity ($k$) | Classification |
| --- | --- | --- |
| Copper | $\approx 400\ \text{W m}^{-1}\ \text{K}^{-1}$ | Excellent conductor |
| Aluminium | $\approx 235\ \text{W m}^{-1}\ \text{K}^{-1}$ | Very good conductor |
| Iron / Steel | $\approx 50\ \text{W m}^{-1}\ \text{K}^{-1}$ | Good conductor |
| Glass | $\approx 0.8\ \text{W m}^{-1}\ \text{K}^{-1}$ | Poor conductor (Insulator) |
| Wood | $\approx 0.15\ \text{W m}^{-1}\ \text{K}^{-1}$ | Insulator |
| Air | $\approx 0.025\ \text{W m}^{-1}\ \text{K}^{-1}$ | Excellent Insulator |

---

## The Thermos Flask (Vacuum Flask)

**Objective v: relate the component part of the working of the thermos flask.**

The thermos flask (or vacuum flask) is a device designed to keep hot liquids hot and cold liquids cold for a long time. It achieves this by drastically reducing heat transfer by all three modes: conduction, convection, and radiation.

### Component Parts and How They Work:
1. **The Vacuum:** The flask consists of a double-walled glass (or stainless steel) vessel. The space between the two walls is evacuated (air is removed) to form a vacuum. **Function:** A vacuum contains no particles, so it completely prevents heat transfer by **conduction and convection**, since both require a material medium.
2. **Silvered Walls:** The inner surfaces of the double walls facing the vacuum are coated with a shiny silver layer. **Function:** Shiny surfaces are poor emitters and poor absorbers. This minimises heat transfer by **radiation**. Heat from a hot liquid is reflected back inward, and heat from the outside is reflected away.
3. **Cork or Plastic Stopper (and support pads):** The top of the flask is sealed with a stopper, and the inner glass bottle rests on pads. **Function:** Cork and plastic are insulators (poor conductors), which minimises **conduction** through the top and bottom. The stopper also seals the flask tightly to prevent hot air from escaping, stopping **convection** to the atmosphere.

[IMAGE: A cross-sectional diagram of a thermos flask. Key labels: "Plastic stopper" at the top, "Double-walled glass vessel", "Vacuum" indicating the space between the walls, "Silvered inner surfaces" on the glass walls, "Cork support pad" at the bottom, and "Outer casing". Clean flat textbook illustration, white background.]

---

## Convection: Land and Sea Breezes

**Objective vi: differentiate between land and sea breeze.**

Coastal regions (like Lagos) experience natural convection currents in the atmosphere known as land and sea breezes. This happens because **land heats up faster and cools down faster than water**. (In Physics terms, water has a much higher specific heat capacity than soil or rock).

### Sea Breeze (Occurs during the Day)
During a sunny day, the land absorbs heat and warms up much faster than the sea. The air immediately above the land gets hot, expands, and rises (convection). The colder, denser air over the sea flows inward towards the land to replace the rising hot air. This cool wind blowing from the sea to the land is the **sea breeze**.

### Land Breeze (Occurs at Night)
At night, the land cools down much faster than the sea. The sea remains relatively warm. Therefore, the air above the sea is warmer, so it expands and rises. The cooler, denser air from the land flows outwards towards the sea to replace it. This wind blowing from the land to the sea is the **land breeze**.

| Feature | Sea Breeze | Land Breeze |
| --- | --- | --- |
| **When it occurs** | Daytime | Nighttime |
| **Warmer surface** | Land is hotter | Sea is hotter |
| **Direction of wind** | From Sea $\rightarrow$ to Land | From Land $\rightarrow$ to Sea |

---

## Combustion Engines and Rockets

**Objective vii: analyse the principles of operating internal combustion jet engines, rockets.**

Engines that convert heat energy (from burning fuel) into mechanical energy are called heat engines.

### 1. Internal Combustion Engines
In an internal combustion engine (ICE), the burning of fuel occurs *inside* the engine cylinders.
*   **Petrol Engines:** A mixture of petrol vapour and air is drawn into the cylinder, compressed by a piston, and then ignited by an electric spark from a **spark plug**. The explosion produces hot gases that expand rapidly, pushing the piston down.
*   **Diesel Engines:** Only air is drawn in and heavily compressed, causing it to become intensely hot. Diesel fuel is then injected and it instantly ignites due to the heat of the compressed air (no spark plug is needed). 

### 2. Jet Engines
Jet engines (used in aeroplanes) are continuous internal combustion engines. They draw in a large amount of atmospheric air from the front, compress it using spinning blades, mix it with jet fuel, and ignite it. The hot, expanding gases shoot out of the back exhaust at extreme speeds. According to **Newton's Third Law of Motion** (action and reaction), the backward force of the expelled gases creates an equal and opposite forward force (**thrust**) that drives the aircraft forward.
*Note:* A jet engine **requires oxygen from the surrounding atmosphere** to burn its fuel.

### 3. Rockets
Rockets operate on the exact same principle of thrust (Newton's Third Law) as jet engines—propelling hot gases backward to move forward. However, there is one crucial difference: **space is a vacuum** with no air. 
Therefore, rockets must carry their own oxygen supply (an **oxidiser**, like liquid oxygen) alongside their fuel. Because they do not rely on atmospheric air, rockets can operate outside the Earth's atmosphere.

---

## Electric Engines vs Combustion Engines

**Objective viii: understand the advantages and disadvantages of electric engine over combustion engine.**

Electric engines (or electric motors) convert electrical energy (stored in batteries) directly into mechanical energy. They are becoming popular worldwide as alternatives to traditional internal combustion engines (ICE).

### Advantages of Electric Engines
1. **Zero Emissions:** They do not produce exhaust gases (like carbon (IV) oxide or harmful pollutants), making them environmentally friendly.
2. **High Efficiency:** Electric motors convert a much higher percentage of stored energy into actual movement compared to combustion engines, which waste most of their energy as heat.
3. **Quiet Operation:** They run almost silently, reducing noise pollution.
4. **Fewer Moving Parts:** They do not require oil changes, spark plugs, or complex gearboxes, meaning they have lower maintenance costs.

### Disadvantages of Electric Engines
1. **Charging Time:** Refueling a combustion engine takes only a few minutes, whereas charging an electric battery can take hours.
2. **Dependence on the Power Grid:** They require a reliable electricity supply to charge. In places like Nigeria where grid power can be inconsistent, operating an electric vehicle requires costly alternatives like solar panels.
3. **Limited Range:** They often cannot travel as far on a single charge as a petrol car can on a full tank.
4. **High Initial Cost:** The large lithium-ion batteries make electric vehicles expensive to buy initially, and replacing a degraded battery is very costly.

---

## Key terms

| Term | Meaning |
| --- | --- |
| Conduction | Heat transfer through a material by molecular vibration without bulk movement of particles. |
| Convection | Heat transfer through a fluid (liquid or gas) by actual bulk movement of the heated particles. |
| Radiation | Heat transfer by electromagnetic waves, which does not require a material medium. |
| Temperature Gradient | The change in temperature per unit length along a material ($\text{K m}^{-1}$). |
| Thermal Conductivity ($k$) | A measure of how easily a material allows heat to pass through it by conduction. |
| Heat Flux | The rate of heat energy transferred per unit cross-sectional area ($\text{W m}^{-2}$). |
| Vacuum | A space entirely devoid of matter (contains no particles). |
| Internal Combustion Engine | An engine where fuel is burned inside the engine cylinder (e.g. petrol, diesel). |
| Thrust | The forward driving force produced by the backward expulsion of gases (in jets and rockets). |

---

## Exam tips and common mistakes

*   **Heat Flux vs Rate of Heat Transfer:** Read the question carefully! Rate of heat transfer is $Q/t$ (measured in Watts). Heat flux is $Q/(At)$ (measured in $\text{W m}^{-2}$). Always verify which one the examiner is asking for by looking at the units in the options.
*   **Temperature Units:** For temperature *differences* ($\Delta \theta$), you do not need to add $273$ to convert Celsius to Kelvin. A change of $10^\circ\text{C}$ is exactly a change of $10\ \text{K}$.
*   **Black vs White:** Never forget that dull black is both the best absorber AND the best emitter. (Many students mistakenly think it is only a good absorber).
*   **Jets vs Rockets:** JAMB loves to test this. Jet = needs atmospheric air. Rocket = carries its own oxidiser. 
*   **Sea breeze vs Land breeze timing:** Sea breeze happens by Day; Land breeze happens by Night. 

---

## Quick summary

1. Heat is transferred by conduction (in solids, no bulk movement), convection (in fluids, bulk movement), and radiation (electromagnetic waves, through vacuum).
2. The rate of heat conduction is given by $H = \frac{k A \Delta \theta}{L}$. Heat flux is the rate of heat transfer per unit area ($\text{W m}^{-2}$).
3. Dull, black surfaces are the best absorbers and emitters of radiant heat; shiny, silvery surfaces are the worst.
4. Metals are good conductors of heat, whereas non-metals, liquids, and gases (like wood, plastic, air) are poor conductors (insulators).
5. A thermos flask reduces heat loss: a vacuum stops conduction and convection, while silvered walls stop radiation.
6. A sea breeze blows from sea to land during the day because the land heats up faster than the sea. A land breeze occurs at night.
7. Internal combustion engines burn fuel inside the cylinder. Jet engines use atmospheric air, but rockets carry their own oxygen, allowing them to work in space.
8. Electric engines are highly efficient and produce no exhaust emissions, but they take a long time to charge and are limited by battery range and grid reliability.

---

## Practice questions

**1. Which of the following modes of heat transfer requires a material medium and involves the actual movement of heated particles?**
- A. Conduction
- B. Convection
- C. Radiation
- D. Expansion

**Answer: B.** Convection is the transfer of heat by the bulk displacement of particles in fluids (liquids and gases). Conduction uses a medium but has no bulk movement, and radiation does not require a medium.

**2. A glass window has a thermal conductivity of $0.8\ \text{W m}^{-1}\ \text{K}^{-1}$ and a thickness of $0.004\ \text{m}$. If the temperature difference across the window is $15\ \text{K}$, calculate the heat flux through the glass.**
- A. $12\ \text{W m}^{-2}$
- B. $3000\ \text{W m}^{-2}$
- C. $0.048\ \text{W m}^{-2}$
- D. $300\ \text{W m}^{-2}$

**Answer: B.** 
1. Heat flux $\Phi = \frac{k \Delta \theta}{L}$. 
2. Substitute values: $\Phi = \frac{0.8 \times 15}{0.004}$.
3. Calculate: $\Phi = \frac{12}{0.004} = 3000\ \text{W m}^{-2}$.
*(Mistake behind A: Forgetting to divide by the thickness $L$.)*

**3. In a thermos flask, the heat loss by radiation is minimised by the**
- A. vacuum between the double walls
- B. plastic stopper
- C. silvered surfaces of the walls
- D. cork support pads

**Answer: C.** Silvered (shiny) surfaces are poor emitters and poor absorbers of radiation, thus reflecting radiant heat. The vacuum prevents conduction and convection.

**4. Why is the cooling fin of a motorcycle engine usually painted dull black?**
- A. To make it a good conductor of heat
- B. To make it a poor absorber of heat
- C. To make it a good emitter of radiant heat
- D. To prevent the engine from rusting

**Answer: C.** A dull black surface is the best emitter of radiant heat, which helps the engine dissipate (lose) heat rapidly to the surroundings. 

**5. Which of the following is true about a sea breeze?**
- A. It occurs at night when the sea is hotter than the land.
- B. It occurs during the day when the land is hotter than the sea.
- C. It blows from the land towards the sea.
- D. It is caused by conduction of heat from land to sea.

**Answer: B.** During the day, land heats up faster than the sea. Air over the land rises, and cooler air from the sea blows in to replace it (sea breeze). 

**6. The primary reason why a rocket can travel in outer space, but a jet engine cannot, is that**
- A. rockets are built with stronger metals
- B. rockets carry their own oxygen supply
- C. jet engines use electric motors
- D. jet engines are too heavy to escape gravity

**Answer: B.** Space is a vacuum with no air. A jet engine relies on drawing in atmospheric oxygen to burn fuel, whereas a rocket carries an oxidiser (its own oxygen supply).

**7. An advantage of an electric engine over an internal combustion engine is that the electric engine**
- A. has a much longer range per fuel load
- B. requires atmospheric oxygen to function
- C. operates with higher efficiency and zero exhaust emissions
- D. can be recharged in less than two minutes

**Answer: C.** Electric engines convert a higher percentage of stored energy directly into movement and do not emit harmful exhaust gases. However, their charging time is a disadvantage.

**8. Which of the following materials is the best insulator of heat?**
- A. Copper
- B. Aluminium
- C. Air
- D. Iron

**Answer: C.** Air is a gas and a very poor conductor of heat (an excellent insulator). The others are metals, which are very good conductors.

**9. A metal rod of length $0.5\ \text{m}$ is heated such that one end is at $100^\circ\text{C}$ and the other end is at $20^\circ\text{C}$. What is the temperature gradient along the rod?**
- A. $160\ \text{K m}^{-1}$
- B. $40\ \text{K m}^{-1}$
- C. $80\ \text{K m}^{-1}$
- D. $200\ \text{K m}^{-1}$

**Answer: A.** 
1. Formula: $\text{Temperature gradient} = \frac{\Delta \theta}{L}$. 
2. $\Delta \theta = 100 - 20 = 80\ \text{K}$. 
3. Substitute: $\frac{80}{0.5} = 160\ \text{K m}^{-1}$. 
*(Mistake behind C: Calculating only the temperature difference and forgetting to divide by the length of $0.5\ \text{m}$.)*

**10. A wall of thickness $0.1\ \text{m}$ and cross-sectional area $2.0\ \text{m}^2$ has a thermal conductivity of $0.05\ \text{W m}^{-1}\ \text{K}^{-1}$. If the temperature difference across it is $40^\circ\text{C}$, calculate the rate of heat transfer through the wall.**
- A. $4\ \text{W}$
- B. $20\ \text{W}$
- C. $40\ \text{W}$
- D. $400\ \text{W}$

**Answer: C.** 
1. Formula: $H = \frac{k A \Delta \theta}{L}$. 
2. Substitute values: $H = \frac{0.05 \times 2.0 \times 40}{0.1}$. 
3. Simplify the numerator: $0.05 \times 2.0 = 0.1$. Then $0.1 \times 40 = 4$. 
4. Divide by $L$: $\frac{4}{0.1} = 40\ \text{W}$.
*(Mistake behind A: Multiplying $k$, $A$, and $\Delta \theta$, but forgetting to divide by the thickness $L$.)*
