# JAMB Physics Notes: Friction

## What JAMB expects

This topic is Section A, Topic 6 of the JAMB Physics syllabus. It covers the principles of friction in both solids and fluids.

The syllabus covers the following content items:
- (i) static and dynamic friction;
- (ii) coefficient of limiting friction and its determination;
- (iii) advantages and disadvantages of friction;
- (iv) reduction of friction;
- (v) qualitative treatment of viscosity and terminal velocity;
- (vi) Stoke's law.

By the end of these notes, you should be able to:
1. differentiate between static and dynamic friction;
2. determine the coefficient of limiting friction;
3. compare the advantages and disadvantages of friction;
4. suggest ways by which friction can be reduced;
5. analyse factors that affect viscosity and terminal velocity;
6. apply Stoke's law.

---

## What is Friction?

**Friction** is a force that opposes the relative motion (or tendency of motion) between two surfaces in contact. 

Even surfaces that look perfectly smooth, like glass, have microscopic hills and valleys (irregularities). When two surfaces are placed together, these irregularities interlock. Friction is the force required to break these interlocks so that sliding can occur. 

### Laws of Solid Friction
JAMB frequently tests your knowledge of the laws governing solid friction. They are:
1. **Friction opposes motion:** It always acts in the opposite direction to the direction of motion or intended motion.
2. **Depends on the nature of the surfaces:** Friction depends on what the materials are made of and how rough or smooth they are.
3. **Independent of the area of contact:** Whether a brick rests on its wide face or its narrow face, the frictional force remains the same.
4. **Proportional to normal reaction:** The frictional force ($F$) is directly proportional to the perpendicular force pressing the surfaces together, known as the normal reaction ($R$).
5. **Dynamic friction is less than limiting friction:** It takes more force to start moving a resting object than it takes to keep it moving.

[IMAGE: A rectangular block on a horizontal table. Four labelled arrows show the forces acting on it: Weight (W) pointing downwards from the centre, Normal Reaction (R) pointing vertically upwards, an Applied Force (P) pointing to the right, and Frictional Force (F) pointing to the left along the boundary between the block and the table. Clean flat textbook illustration, white background.]

---

## Differentiating Between Static and Dynamic Friction

**Objective i: differentiate between static and dynamic friction.**

When you try to push a heavy generator, it does not move immediately. As you push harder, the friction matches your push until it reaches a maximum point. Once the generator starts moving, it suddenly feels a little easier to push. This behaviour highlights the two main types of solid friction.

### 1. Static Friction
**Static friction** is the friction between two solid surfaces that are not moving relative to each other. It is a "self-adjusting" force. If you push a block with $10\ \text{N}$ and it does not move, the static friction is exactly $10\ \text{N}$. 

The maximum value of static friction, which occurs exactly at the point when the body is just about to slip, is called **limiting friction**.

### 2. Dynamic (Kinetic) Friction
**Dynamic friction** (also called kinetic friction) is the friction between two surfaces that are in relative motion (sliding or rolling past each other). 

Dynamic friction is divided into two types:
* **Sliding friction:** When one surface slides over another (e.g., pushing a box across the floor).
* **Rolling friction:** When an object rolls over a surface (e.g., a car tyre or a ball bearing). Rolling friction is always much smaller than sliding friction.

### Comparison of Static and Dynamic Friction

| Feature | Static Friction | Dynamic (Kinetic) Friction |
| :--- | :--- | :--- |
| **State of motion** | Acts when objects are at rest relative to each other | Acts when objects are moving relative to each other |
| **Magnitude** | Self-adjusting; increases as the applied force increases, up to a maximum | Remains fairly constant regardless of the speed of motion |
| **Maximum value** | Reaches a peak called *limiting friction* | Always strictly less than the limiting static friction |
| **Coefficient** | Higher coefficient ($\mu_s$) | Lower coefficient ($\mu_k$) |

[IMAGE: A line graph of Frictional Force (y-axis) against Applied Force (x-axis). The graph starts at the origin and rises as a straight, sloping line at a 45-degree angle (labelled "Static Friction: F = Applied Force"). At the very top of this peak, it is labelled "Limiting Friction". After the peak, the line drops slightly and then continues as a horizontal straight line to the right, labelled "Dynamic (Kinetic) Friction". Clean flat textbook style, white background.]

---

## Determining the Coefficient of Limiting Friction

**Objective ii: determine the coefficient of limiting friction.**

From the laws of friction, the limiting frictional force ($F$) is directly proportional to the normal reaction ($R$). 
$$F \propto R$$
$$F = \mu R$$

Where:
* $F$ is the frictional force (in Newtons, $\text{N}$)
* $R$ is the normal reaction (in Newtons, $\text{N}$)
* $\mu$ (the Greek letter mu) is a constant known as the **coefficient of friction**. 

**Note on units:** Because $\mu = \frac{F}{R}$, it is a ratio of two forces. Therefore, the coefficient of friction **has no unit**. 

### Methods of Determining the Coefficient of Friction

JAMB expects you to know two standard laboratory methods to determine $\mu$.

#### 1. The Horizontal Plane Method
**Apparatus:** A wooden block, string, smooth pulley, scale pan, and known masses.
**Procedure:** 
1. Place a block of known mass $m$ on a horizontal table. Its normal reaction is $R = mg$.
2. Attach a string to the block, pass it over the pulley at the edge of the table, and attach a scale pan.
3. Gradually add small masses to the pan until the block *just* begins to slide.
**Calculation:** The total weight of the pan and the masses gives the pulling force, which is equal to the limiting friction $F$. The coefficient is calculated as:
$$\mu = \frac{F}{R} = \frac{F}{mg}$$

#### 2. The Inclined Plane Method
**Apparatus:** An adjustable inclined wooden plane, a block, and a protractor.
**Procedure:** 
1. Place the block on the horizontal plane.
2. Gradually tilt the plane upwards, increasing the angle until the block *just* begins to slide down.
3. Measure this exact angle, known as the **angle of repose** ($\theta$).
**Calculation:** At the point of sliding, the component of the block's weight pulling it down the plane ($mg \sin \theta$) is exactly balanced by the limiting friction ($F$). The normal reaction is $mg \cos \theta$. 
$$F = mg \sin \theta$$
$$R = mg \cos \theta$$
$$\mu = \frac{F}{R} = \frac{mg \sin \theta}{mg \cos \theta} = \tan \theta$$

**Textbook variation:** You may see the term **angle of friction**. The angle of friction is the angle between the normal reaction and the resultant of the normal reaction and the frictional force. Numerically, the angle of friction is exactly equal to the angle of repose. $\mu = \tan \theta$ applies to both.

[IMAGE: A block of mass m resting on an inclined plane at an angle theta to the horizontal. Arrows show the forces: Weight (mg) acting straight down, Normal Reaction (R) acting perpendicular to the surface upwards, the weight component down the slope (mg sin theta), and Friction (F) acting up the slope. Clean flat textbook style, white background.]

### Worked Examples on Coefficient of Friction

**Worked Example 1 (Horizontal Plane)**
A wooden box of mass $8\ \text{kg}$ rests on a horizontal concrete floor. If the coefficient of limiting friction between the box and the floor is $0.4$, calculate the minimum horizontal force required to make the box start moving. (Take $g = 10\ \text{m s}^{-2}$)

**Step-by-step working:**
1. **Write the formula:** $F = \mu R$.
2. **Calculate the normal reaction ($R$):** On a flat horizontal floor, the normal reaction equals the weight. 
   $R = mg = 8\ \text{kg} \times 10\ \text{m s}^{-2} = 80\ \text{N}$.
3. **Substitute the values:** $F = 0.4 \times 80\ \text{N}$.
4. **State the final answer:** $F = 32\ \text{N}$.

**Worked Example 2 (Inclined Plane)**
A block of mass $5\ \text{kg}$ is placed on a plane inclined at $30^\circ$ to the horizontal. If the coefficient of dynamic friction is $0.2$, calculate the frictional force experienced by the block as it slides down. (Take $g = 10\ \text{m s}^{-2}$)

**Step-by-step working:**
1. **Write the formula:** $F_k = \mu R$.
2. **Find the normal reaction ($R$):** On an inclined plane, the normal reaction is $R = mg \cos \theta$.
3. **Substitute the values:** $R = 5\ \text{kg} \times 10\ \text{m s}^{-2} \times \cos(30^\circ)$. Since $\cos(30^\circ) = \frac{\sqrt{3}}{2}$, 
   $R = 50 \times \frac{\sqrt{3}}{2} = 25\sqrt{3}\ \text{N}$.
4. **Calculate the frictional force:** $F_k = 0.2 \times 25\sqrt{3}\ \text{N}$.
5. **State the final answer:** $F_k = 5\sqrt{3}\ \text{N}$. (In JAMB, answers with angles like $30^\circ$ or $60^\circ$ are often left in surd form).

---

## Advantages and Disadvantages of Friction

**Objective iii: compare the advantages and disadvantages of friction.**

Friction is often called a "necessary evil" because we cannot live without it, but it also causes many problems in machines. 

### Comparison Table

| Advantages (Why we need friction) | Disadvantages (Why friction is a problem) |
| :--- | :--- |
| **Locomotion:** Friction between our shoes and the ground prevents us from slipping when walking. | **Wear and tear:** Friction causes moving machine parts (like pistons in an engine or gears) to wear out over time. |
| **Braking:** The friction between brake pads and wheels allows cars, okadas (motorcycles), and bicycles to slow down and stop safely. | **Energy loss:** Friction converts useful mechanical energy into waste heat, reducing the efficiency of machines (e.g., generators overheating). |
| **Grip and holding:** Without friction, nails and screws would pull out of wood, and we would not be able to hold pens or tools. | **Slowing down motion:** It acts as a drag on vehicles, meaning more fuel is burned to overcome air resistance and road friction. |
| **Sharpening and grinding:** Friction is used when sharpening cutlasses on a grindstone or striking a match to light a fire. | **Noise production:** High friction can cause loud screeching noises in poorly maintained machinery. |

---

## Reducing Friction

**Objective iv: suggest ways by which friction can be reduced.**

Because of its disadvantages, engineers design machines to minimise friction. Common methods include:

1. **Lubrication:** Applying oil or grease between moving metal parts (like in car engines or bicycle chains). The lubricant fills the microscopic valleys on the surfaces, keeping the solid parts separated by a thin fluid layer. Fluid friction is much lower than solid friction.
2. **Ball bearings and roller bearings:** These are small steel balls or cylinders placed between two moving surfaces (like inside a wheel axle). They convert sliding friction into rolling friction, which is significantly smaller.
3. **Streamlining:** To reduce air or water resistance (fluid friction), vehicles like airplanes, racing cars, and ships are designed with a smooth, pointed, aerodynamic shape.
4. **Polishing surfaces:** Smoothing out rough surfaces reduces the irregularities that cause friction, though polishing too much can actually increase friction due to molecular attraction.

---

## Viscosity and Terminal Velocity

**Objective v: analyse factors that affect viscosity and terminal velocity.**

### What is Viscosity?
**Viscosity** is the internal friction between the layers of a fluid (liquid or gas) as they slide past one another. It is a measure of a fluid's resistance to flow. 
* Thick, sticky fluids like engine oil, honey, and glycerin have **high viscosity**; they flow slowly.
* Thin fluids like water and petrol have **low viscosity**; they flow easily.

**Comparing Solid Friction and Viscosity:**
1. Solid friction is largely independent of velocity, but viscous drag depends heavily on the relative velocity of the moving object or fluid layers.
2. Solid friction is independent of the area of contact, but viscosity depends on the surface area of the layers in contact.
3. Solid friction occurs at the surfaces, whereas viscosity happens within the bulk of the fluid.

### Factors Affecting Viscosity
The main factor affecting viscosity is **temperature**, but its effect differs between liquids and gases:
* **In liquids:** As temperature increases, the viscosity **decreases**. This is why cold engine oil is very thick and hard to pour, but flows easily once the car engine heats up.
* **In gases:** As temperature increases, the viscosity **increases**. The rapidly moving gas molecules collide more frequently, causing more drag.

### Terminal Velocity
When an object, like a stone or a raindrop, falls through a viscous fluid (like air or water), it experiences three main forces:
1. **Weight ($W$):** Acting downwards due to gravity.
2. **Upthrust ($U$):** The buoyant force acting upwards.
3. **Viscous Drag ($F$):** The fluid friction acting upwards, opposing the motion.

As the object falls, its velocity increases. Because viscous drag increases with velocity, the upward drag force grows larger and larger. Eventually, a point is reached where the total upward forces perfectly balance the downward weight:
$$W = U + F$$

At this point, the net force on the falling object is zero. According to Newton's First Law, its acceleration becomes zero, and it falls at a constant, maximum speed. This constant speed is called the **terminal velocity**.

[IMAGE: A spherical object falling through a fluid. Arrows show Weight (W) acting downwards from the centre, while Upthrust (U) and Viscous Drag (F) point vertically upwards from the top. A side note reads "At terminal velocity: W = U + F, Acceleration = 0". Clean flat textbook style, white background.]

---

## Stoke's Law

**Objective vi: apply Stoke's law.**

Sir George Stokes studied objects falling through fluids and developed a formula for the viscous drag force acting on a small sphere falling at low speeds. 

**Stoke's Law** states that the viscous drag force ($F$) on a spherical body of radius $r$ moving with velocity $v$ through a fluid of viscosity $\eta$ is given by:
$$F = 6\pi \eta r v$$

Where:
* $F$ = viscous drag force (in $\text{N}$)
* $\eta$ (Greek letter eta) = **coefficient of viscosity** of the fluid (in $\text{Pa s}$ or $\text{N s m}^{-2}$)
* $r$ = radius of the sphere (in $\text{m}$)
* $v$ = velocity of the sphere (in $\text{m s}^{-1}$)

### Deriving the Terminal Velocity Formula
For a sphere of radius $r$, the volume is $\frac{4}{3}\pi r^3$.
* **Weight ($W$):** $W = \text{mass} \times g = (\text{Volume} \times \text{Density of sphere}) \times g = \frac{4}{3}\pi r^3 \rho g$
* **Upthrust ($U$):** $U = (\text{Volume of fluid displaced} \times \text{Density of fluid}) \times g = \frac{4}{3}\pi r^3 \sigma g$
  (where $\rho$ is the density of the sphere and $\sigma$ is the density of the fluid).

At terminal velocity ($v_t$), $W = U + F$:
$$\frac{4}{3}\pi r^3 \rho g = \frac{4}{3}\pi r^3 \sigma g + 6\pi \eta r v_t$$

Rearranging to solve for $v_t$:
$$6\pi \eta r v_t = \frac{4}{3}\pi r^3 g (\rho - \sigma)$$
$$v_t = \frac{2r^2 g (\rho - \sigma)}{9\eta}$$

JAMB occasionally tests this final formula in calculation questions or asks you to identify the relationship (e.g., $v_t$ is directly proportional to the square of the radius, $r^2$).

### Worked Examples on Stoke's Law

**Worked Example 3 (Calculating Viscous Drag)**
A small steel ball of radius $2.0 \times 10^{-3}\ \text{m}$ falls at a steady velocity of $0.1\ \text{m s}^{-1}$ through engine oil. If the coefficient of viscosity of the oil is $0.5\ \text{N s m}^{-2}$, calculate the viscous drag on the ball.

**Step-by-step working:**
1. **Write Stoke's Law:** $F = 6\pi \eta r v$.
2. **Substitute the given values with units:** 
   $F = 6 \times \pi \times 0.5\ \text{N s m}^{-2} \times (2.0 \times 10^{-3}\ \text{m}) \times 0.1\ \text{m s}^{-1}$.
3. **Calculate the numerical value:** 
   $6 \times 0.5 = 3$.
   $3 \times 2.0 \times 10^{-3} \times 0.1 = 6.0 \times 10^{-4}$.
4. **State the final answer with its unit:** $F = 6.0\pi \times 10^{-4}\ \text{N}$.

**Worked Example 4 (Calculating Terminal Velocity)**
A tiny metal sphere of radius $1.0 \times 10^{-3}\ \text{m}$ falls through a fluid of viscosity $0.2\ \text{Pa s}$. The difference in density between the sphere and the fluid is $9000\ \text{kg m}^{-3}$. Calculate its terminal velocity. (Take $g = 10\ \text{m s}^{-2}$)

**Step-by-step working:**
1. **Write the terminal velocity formula:** $v_t = \frac{2r^2 g (\rho - \sigma)}{9\eta}$.
2. **Substitute the values with units:** 
   $v_t = \frac{2 \times (1.0 \times 10^{-3}\ \text{m})^2 \times 10\ \text{m s}^{-2} \times 9000\ \text{kg m}^{-3}}{9 \times 0.2\ \text{Pa s}}$.
3. **Simplify the numerator:** $(1.0 \times 10^{-3})^2 = 1.0 \times 10^{-6}$.
   $2 \times 1.0 \times 10^{-6} \times 10 \times 9000 = 0.18$.
4. **Simplify the denominator:** $9 \times 0.2 = 1.8$.
5. **Calculate and state the final answer:** $v_t = \frac{0.18}{1.8} = 0.1\ \text{m s}^{-1}$.

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Friction** | A force that opposes relative motion between surfaces in contact. |
| **Static friction** | Friction between two bodies that are not moving relative to each other. |
| **Limiting friction** | The maximum static frictional force just before motion begins. |
| **Dynamic (kinetic) friction** | Friction between bodies that are moving relative to each other. |
| **Coefficient of friction ($\mu$)** | The ratio of the limiting frictional force to the normal reaction ($F/R$). It has no units. |
| **Angle of repose ($\theta$)** | The maximum angle of an inclined plane at which an object can rest before sliding. |
| **Normal reaction ($R$)** | The perpendicular force acting on an object pressing against a surface. |
| **Viscosity** | The internal fluid friction opposing the flow of a liquid or gas. |
| **Terminal velocity** | The constant maximum velocity reached by an object falling through a fluid when upward and downward forces balance. |
| **Stoke's Law** | The formula $F = 6\pi \eta r v$ used to calculate the viscous drag on a falling sphere. |

---

## Exam tips and common mistakes

* **Coefficient of friction has no units.** A common trap in JAMB is to offer options like $0.5\ \text{N}$ and $0.5$. Always pick the one without units for $\mu$.
* **Normal reaction changes on slopes.** Do not always assume $R = mg$. On a horizontal surface, $R = mg$. But on an inclined plane, $R = mg \cos \theta$. 
* **Terminal velocity means zero acceleration.** Do not confuse terminal velocity with maximum acceleration. At terminal velocity, the net force is zero, so $a = 0$.
* **Viscosity in liquids vs gases.** Remember that heating a liquid makes it *less* viscous, but heating a gas makes it *more* viscous. 
* **Check units in Stoke's Law.** JAMB may give the radius in millimetres ($\text{mm}$) or centimetres ($\text{cm}$). You must convert it to metres ($\text{m}$) before using the formula.

---

## Quick summary

1. Friction is a force that opposes motion. It depends on the nature of the surfaces and the normal reaction, but is independent of the area of contact.
2. Static friction occurs before motion starts, reaching a maximum called limiting friction. Dynamic friction acts during motion and is always less than limiting friction.
3. The coefficient of friction is the ratio $\mu = \frac{F}{R}$. On an inclined plane, it is equal to $\tan \theta$ at the angle of repose.
4. While friction causes wear and tear and wastes energy, it is essential for walking, braking, and gripping objects.
5. Solid friction can be reduced by using lubricants, ball bearings (to convert sliding into rolling), or streamlining.
6. Viscosity is fluid friction. In liquids, viscosity decreases as temperature increases.
7. Terminal velocity is reached when an object falling through a fluid experiences an upward force (upthrust + viscous drag) that exactly equals its downward weight ($W = U + F$).
8. Stoke's law gives the viscous drag on a sphere as $F = 6\pi \eta r v$.

---

## Practice questions

**1. The maximum frictional force that must be overcome before a body can just begin to move over another is called:**
- A. dynamic friction
- B. sliding friction
- C. kinetic friction
- D. limiting friction

**Answer: D.** Limiting friction is the maximum value of static friction, reached exactly at the point when the body is about to slip.

**2. A horizontal force of $30\ \text{N}$ is required to just move a $10\ \text{kg}$ block resting on a horizontal floor. Calculate the coefficient of limiting friction. (Take $g = 10\ \text{m s}^{-2}$)**
- A. $0.20$
- B. $0.25$
- C. $0.30$
- D. $3.00$

**Answer: C.** 
1. Formula: $F = \mu R$. 
2. Normal reaction on a horizontal floor: $R = mg = 10 \times 10 = 100\ \text{N}$. 
3. Substitute: $30 = \mu \times 100$. 
4. $\mu = 30 / 100 = 0.30$. 
A common mistake is forgetting to multiply mass by $g$ to find $R$, which leads to the wrong answer of $3.00$ (option D).

**3. A wooden block begins to slide down an inclined plane when the angle of inclination is $30^\circ$. What is the coefficient of limiting friction?**
- A. $\frac{1}{2}$
- B. $\frac{\sqrt{3}}{2}$
- C. $\frac{1}{\sqrt{3}}$
- D. $\sqrt{3}$

**Answer: C.** 
1. The coefficient of friction equals the tangent of the angle of repose. 
2. $\mu = \tan \theta$. 
3. $\mu = \tan(30^\circ) = \frac{1}{\sqrt{3}}$.

**4. Which of the following best distinguishes viscosity from solid friction?**
- A. Viscosity only opposes motion
- B. Viscosity depends on the relative velocity of the moving layers
- C. Solid friction depends on the area of contact
- D. Viscosity is independent of temperature

**Answer: B.** Viscous drag is directly proportional to the relative velocity of the fluid layers or the falling object ($F = 6\pi \eta r v$), whereas solid friction is mostly independent of velocity once motion has started.

**5. Which of the following is NOT an advantage of friction?**
- A. Walking without slipping
- B. Braking of vehicles
- C. Sharpening knives on a grindstone
- D. Overheating in generator bearings

**Answer: D.** Overheating and energy loss due to friction in machines (like generator bearings) is a major disadvantage of friction, not an advantage.

**6. Friction in a machine is most effectively reduced by replacing sliding friction with rolling friction using:**
- A. lubricants
- B. ball bearings
- C. sandpaper
- D. stream-lining

**Answer: B.** Ball bearings (or roller bearings) convert sliding friction into rolling friction, which involves much less resistance. Lubricants reduce friction but do not change sliding to rolling.

**7. A small metal ball of radius $2.0 \times 10^{-3}\ \text{m}$ falls at a steady velocity of $0.05\ \text{m s}^{-1}$ through oil of viscosity $0.4\ \text{Pa s}$. What is the viscous drag?**
- A. $2.4\pi \times 10^{-4}\ \text{N}$
- B. $1.2\pi \times 10^{-4}\ \text{N}$
- C. $4.8\pi \times 10^{-3}\ \text{N}$
- D. $2.4\pi \times 10^{-5}\ \text{N}$

**Answer: A.** 
1. Formula: $F = 6\pi \eta r v$. 
2. Substitute: $F = 6 \times \pi \times 0.4 \times (2.0 \times 10^{-3}) \times 0.05$. 
3. Calculate: $0.4 \times 0.05 = 0.02$. 
4. $6 \times 2.0 \times 10^{-3} \times 0.02 = 0.024 \times 10^{-2} = 2.4 \times 10^{-4}$. 
5. The answer is $2.4\pi \times 10^{-4}\ \text{N}$.

**8. When the temperature of a liquid increases, its viscosity:**
- A. increases
- B. decreases
- C. remains constant
- D. becomes zero

**Answer: B.** In liquids, an increase in temperature gives molecules more kinetic energy, reducing the cohesive forces between them, which lowers the viscosity (it flows easier).

**9. A spherical body falling through a viscous liquid reaches terminal velocity when:**
- A. the upthrust equals the viscous drag
- B. its acceleration is equal to $g$
- C. the sum of the upthrust and viscous drag equals its weight
- D. its weight is entirely balanced by the upthrust

**Answer: C.** At terminal velocity, the net force is zero. This happens when the downward force (Weight) is exactly balanced by the total upward forces (Upthrust + Viscous drag). Therefore, $W = U + F$.

**10. A wooden block of mass $4\ \text{kg}$ rests on a horizontal floor. The coefficient of dynamic friction is $0.2$. If a constant horizontal force of $20\ \text{N}$ is applied to the block, what is its acceleration? (Take $g = 10\ \text{m s}^{-2}$)**
- A. $2\ \text{m s}^{-2}$
- B. $3\ \text{m s}^{-2}$
- C. $5\ \text{m s}^{-2}$
- D. $8\ \text{m s}^{-2}$

**Answer: B.** 
1. Find normal reaction: $R = mg = 4 \times 10 = 40\ \text{N}$. 
2. Find kinetic friction opposing motion: $F_k = \mu R = 0.2 \times 40 = 8\ \text{N}$. 
3. Find the net forward force: $F_{net} = \text{Applied force} - F_k = 20 - 8 = 12\ \text{N}$. 
4. Apply Newton's second law ($F = ma$) to find acceleration: $a = \frac{12}{4} = 3\ \text{m s}^{-2}$. 
A common mistake is using the full $20\ \text{N}$ force ($20 / 4 = 5\ \text{m s}^{-2}$, option C) and forgetting to subtract the friction.
