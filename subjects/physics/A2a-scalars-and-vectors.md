# JAMB Physics Notes: Scalars and Vectors

## What JAMB expects

This topic is Section A, Topic 2a of the JAMB Physics syllabus: Scalars and Vectors. It covers the following content items:
- (i) definition of scalar and vector quantities;
- (ii) examples of scalar and vector quantities;
- (iii) relative velocity;
- (iv) resolution of vectors into two perpendicular directions including graphical methods of solution.

By the end of these notes, you should be able to:
1. distinguish between scalar and vector quantities;
2. give examples of scalar and vector quantities;
3. determine the resultant of two or more vectors;
4. determine relative velocity;
5. resolve vectors into two perpendicular components;
6. use graphical methods to solve vector problems.

---

## Defining Scalars and Vectors

**Objective i: distinguish between scalar and vector quantities.**
**Content (i): definition of scalar and vector quantities.**

In physics, every measurable physical quantity can be classified into one of two groups based on whether direction matters. These two groups are **scalars** and **vectors**.

- A **scalar quantity** is a physical quantity that has **magnitude (size) only**, but no direction. 
  To fully describe a scalar, you only need a number and its unit. For example, if a bag of Nigerian rice has a mass of $50\ \text{kg}$, the value $50\ \text{kg}$ tells you everything about its mass. It does not make sense to say the mass is pointing "North".
  
- A **vector quantity** is a physical quantity that has **both magnitude and direction**.
  To fully describe a vector, you must state its size, its unit, and the direction in which it acts. For example, if a boy pushes a broken-down car, stating that he applies a force of $200\ \text{N}$ is incomplete. You must also state *where* the force is directed (e.g., $200\ \text{N}$ towards the East).

### Distinguishing between them

When JAMB asks you to distinguish between scalars and vectors, the key difference is always the **direction**. Furthermore, scalar quantities are added or subtracted using normal arithmetic (e.g., $2\ \text{kg} + 3\ \text{kg} = 5\ \text{kg}$). Vector quantities cannot always be added simply; their directions must be taken into account using vector addition methods.

| Feature | Scalar Quantity | Vector Quantity |
| --- | --- | --- |
| **Definition** | Has magnitude only | Has both magnitude and direction |
| **Addition method** | Ordinary algebraic addition | Vector addition (geometric/graphical) |
| **Representation** | Just a symbol, e.g., $m$ for mass | A letter with an arrow on top ($\vec{F}$) or a bold letter ($\mathbf{F}$) |

---

## Examples of Scalars and Vectors

**Objective ii: give examples of scalar and vector quantities.**
**Content (ii): examples of scalar and vector quantities.**

JAMB tests this objective very often by giving you a list of quantities and asking you to pick out the scalars or the vectors. Memorising these common examples is essential.

| Scalar Quantities | Vector Quantities |
| --- | --- |
| Distance | Displacement |
| Speed | Velocity |
| Mass | Weight (a force due to gravity) |
| Time | Acceleration |
| Temperature | Force |
| Energy (Kinetic, Potential, Heat) | Momentum |
| Work | Impulse |
| Power | Electric Field Intensity |
| Electric Charge | Magnetic Flux Density |
| Volume, Density, Pressure | Moment of a Force (Torque) |

**Common mistakes to avoid:**
- **Distance vs Displacement:** Distance is a scalar (how far you travelled). Displacement is a vector (how far you are from the starting point in a straight line, with direction). 
- **Mass vs Weight:** Mass is scalar (amount of matter in an object). Weight is a vector (the downward force of gravity acting on that mass).
- **Work and Energy:** Even though forces (vectors) are involved in work, both work and energy are **scalars**.

---

## Resultant of Vectors

**Objective iii: determine the resultant of two or more vectors.**

When two or more vectors act on the same body, their combined effect can be represented by a single vector. This single vector is called the **resultant**.

The method used to find the resultant depends on the angle between the vectors.

### 1. Vectors in the same line (Collinear vectors)
- **Same direction:** Add the magnitudes. The direction remains the same.
  *Example:* A force of $10\ \text{N}$ and another of $5\ \text{N}$ acting East on a body.
  Resultant $R = 10\ \text{N} + 5\ \text{N} = 15\ \text{N}$ due East.
- **Opposite directions:** Subtract the smaller magnitude from the larger one. The direction is that of the larger vector.
  *Example:* $10\ \text{N}$ acting East and $4\ \text{N}$ acting West.
  Resultant $R = 10\ \text{N} - 4\ \text{N} = 6\ \text{N}$ due East.

### 2. Vectors acting at right angles ($90^\circ$)
If two vectors act at right angles to each other, use **Pythagoras' theorem** to find the magnitude of the resultant, and trigonometric ratios to find the direction.

**Worked Example 1:**
A boy walks $3\ \text{km}$ East and then $4\ \text{km}$ North. What is the magnitude of his resultant displacement?

**Solution:**
1. Recognise that East and North are at right angles ($90^\circ$). Let $x = 3\ \text{km}$ and $y = 4\ \text{km}$.
2. Write the formula for Pythagoras' theorem: $R^2 = x^2 + y^2$.
3. Substitute the values: $R^2 = 3^2 + 4^2$.
4. Calculate the squares: $R^2 = 9 + 16 = 25$.
5. Take the square root: $R = \sqrt{25}$.
6. State the final answer with its unit: $R = 5\ \text{km}$.

### 3. Vectors acting at an acute or obtuse angle
When two vectors act at an angle $\theta$ (other than $90^\circ$ or $180^\circ$) to each other, we use the **Parallelogram Law of Vectors**.

**The Parallelogram Law** states that if two vectors acting at a point are represented in magnitude and direction by the adjacent sides of a parallelogram, their resultant is represented in magnitude and direction by the diagonal of the parallelogram drawn from the common point.

To find the magnitude of the resultant $R$ of two vectors $F_1$ and $F_2$ separated by an angle $\theta$, we use the **cosine rule** adapted for the parallelogram diagonal:
$$R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$$

**Worked Example 2:**
Two forces of $5\ \text{N}$ and $3\ \text{N}$ act on a particle at an angle of $60^\circ$ to each other. Calculate the magnitude of the resultant force.

**Solution:**
1. State the formula for the resultant: $R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$.
2. Substitute the values with units: $F_1 = 5\ \text{N}$, $F_2 = 3\ \text{N}$, $\theta = 60^\circ$.
3. Calculate the cosine term: $\cos 60^\circ = 0.5$.
4. Substitute into the formula: $R = \sqrt{5^2 + 3^2 + 2(5)(3)(0.5)}$.
5. Evaluate the expression: $R = \sqrt{25 + 9 + 15}$.
6. Sum the terms: $R = \sqrt{49}$.
7. State the final answer with its unit: $R = 7\ \text{N}$.

**JAMB Shortcut for Vectors:**
If two **equal** vectors of magnitude $F$ act at an angle of $120^\circ$ to each other, their resultant is also $F$.
*Proof:* $R = \sqrt{F^2 + F^2 + 2(F)(F)\cos 120^\circ}$. Since $\cos 120^\circ = -0.5$, $R = \sqrt{2F^2 - F^2} = \sqrt{F^2} = F$.
Memorise this trick, as JAMB loves testing it to save you time!

[IMAGE: A parallelogram diagram showing two vectors F1 and F2 starting from a common origin point O, separated by an angle theta. The diagonal from O is labelled R for resultant. Dashed lines complete the parallelogram to show F1 and F2 on the opposite sides. Clean flat textbook illustration, white background.]

---

## Resolution of Vectors

**Objective v: resolve vectors into two perpendicular components.**
**Content (iv): resolution of vectors into two perpendicular directions...**

Just as two vectors can be combined into one resultant, a single vector can be broken down (resolved) into two perpendicular parts called **components**. These components are usually chosen to be horizontal (along the x-axis) and vertical (along the y-axis).

If a force $F$ acts at an angle $\theta$ to the **horizontal axis**, we can resolve it into:
- The **horizontal component** ($F_x$): $$F_x = F \cos \theta$$
- The **vertical component** ($F_y$): $$F_y = F \sin \theta$$

*Note:* If the angle given is to the vertical, the sine and cosine swap places. Always sketch a triangle to be sure.

[IMAGE: A right-angled triangle showing a vector F as the hypotenuse acting at an angle theta to the horizontal base. The horizontal base is labelled Fx = F cos(theta), and the vertical opposite side is labelled Fy = F sin(theta). Clean flat textbook illustration, white background.]

**Worked Example 3:**
A man drags a heavy box along the ground using a rope. The rope makes an angle of $30^\circ$ with the horizontal and the tension in the rope is $100\ \text{N}$. Calculate the effective force pulling the box horizontally. (Take $\cos 30^\circ = 0.866$).

**Solution:**
1. Identify the needed component. Since the box moves horizontally, we need the horizontal component $F_x$.
2. State the formula: $F_x = F \cos \theta$.
3. Substitute the given values: $F = 100\ \text{N}$, $\theta = 30^\circ$.
4. Calculate: $F_x = 100 \times 0.866$.
5. State the final answer with its unit: $F_x = 86.6\ \text{N}$.

---

## Graphical Methods of Solution

**Objective vi: use graphical methods to solve vector problems.**
**Content (iv): ...including graphical methods of solution.**

Vectors can also be added graphically by drawing them to scale. This is useful when dealing with more than two vectors.

### 1. The Triangle of Vectors
When two vectors are added, you can draw them "head-to-tail". 
1. Choose a scale (e.g., $1\ \text{cm}$ represents $10\ \text{N}$).
2. Draw the first vector as a line of appropriate length in the correct direction.
3. From the **tip** (head) of the first vector, draw the second vector in its correct direction.
4. The **resultant** is the line drawn from the **tail** (start) of the first vector to the **tip** of the second vector.

**Triangle of Forces Rule for Equilibrium:**
If three vectors acting at a point can be represented in magnitude and direction by the three sides of a closed triangle taken in order (head-to-tail continuously), the vectors are in **equilibrium** (their resultant is zero).

### 2. The Polygon of Vectors
If more than two vectors act on a body, you can continue the head-to-tail drawing process.
Draw the first vector, attach the second to its tip, attach the third to the tip of the second, and so on. The resultant is the single vector drawn from the starting point of the first vector straight to the tip of the final vector. If the polygon closes completely, the resultant is zero and the object is in equilibrium.

[IMAGE: On the left, a tip-to-tail triangle showing Vector A, then Vector B starting from A's tip. The resultant R connects the start of A to the tip of B. On the right, a polygon showing four vectors A, B, C, D placed head-to-tail, with a resultant R closing the gap from the start of A to the tip of D. Clean flat textbook illustration, white background.]

---

## Relative Velocity

**Objective iv: determine relative velocity.**
**Content (iii): relative velocity.**

**Relative velocity** is the velocity of one body as observed from another moving body. 
Because the observer is also moving, the apparent speed and direction of the other object differ from its actual speed over the ground.

If body A has a velocity $V_A$ and body B has a velocity $V_B$, the velocity of A *relative to* B (written as $V_{AB}$) is given by:
$$V_{AB} = V_A - V_B$$

This is a vector subtraction. Let's look at the three common cases JAMB tests:

### 1. Bodies moving in the same direction
If two cars are moving along the same straight road in the same direction, subtract the observer's speed from the target's speed.
- If Car A is moving at $100\ \text{km h}^{-1}$ East and Car B is moving at $80\ \text{km h}^{-1}$ East.
- Velocity of A relative to B: $V_{AB} = 100 - 80 = 20\ \text{km h}^{-1}$ East. (To the driver in Car B, Car A is pulling ahead at $20\ \text{km h}^{-1}$).

### 2. Bodies moving in opposite directions
If two bodies are moving towards or away from each other, their relative velocity magnitude is the **sum** of their speeds. (Because one direction is positive and the opposite is negative, $V_A - (-V_B) = V_A + V_B$).

**Worked Example 4:**
A bus travels from Lagos to Benin at a steady speed of $60\ \text{km h}^{-1}$. A car travels from Benin to Lagos on the same road at a steady speed of $90\ \text{km h}^{-1}$. What is the velocity of the car relative to the bus?

**Solution:**
1. Establish a direction system. Let towards Benin be positive (bus $V_b = 60\ \text{km h}^{-1}$) and towards Lagos be negative (car $V_c = -90\ \text{km h}^{-1}$).
2. State the formula for the velocity of the car relative to the bus: $V_{cb} = V_c - V_b$.
3. Substitute the values: $V_{cb} = -90 - 60$.
4. Calculate: $V_{cb} = -150\ \text{km h}^{-1}$.
5. State the final answer: The magnitude is $150\ \text{km h}^{-1}$, and the negative sign means it is in the direction of Lagos. Thus, $150\ \text{km h}^{-1}$ towards Lagos.

### 3. Bodies moving perpendicularly
When bodies move at right angles, we find the relative velocity using vector subtraction triangles and Pythagoras' theorem. 
Velocity of A relative to B is $V_A - V_B$, which is the same as $V_A + (-V_B)$. This means we take the vector $V_A$, reverse the direction of $V_B$, and add them using Pythagoras.

**Worked Example 5:**
A boat crosses a river travelling due East at $4\ \text{m s}^{-1}$. The river current flows due North at $3\ \text{m s}^{-1}$. Calculate the resultant velocity of the boat relative to the stationary riverbank (earth).

**Solution:**
1. Notice that the boat's engine speed (East) and the current (North) are independent and act at $90^\circ$ to each other.
2. State the formula for perpendicular vectors (Pythagoras): $R = \sqrt{V_{boat}^2 + V_{river}^2}$.
3. Substitute the values: $R = \sqrt{4^2 + 3^2}$.
4. Calculate the squares: $R = \sqrt{16 + 9}$.
5. Sum them up: $R = \sqrt{25}$.
6. State the final answer with its unit: $R = 5\ \text{m s}^{-1}$.

---

## Key terms

| Term | Meaning |
| --- | --- |
| **Scalar Quantity** | A physical quantity with only magnitude and no direction (e.g., mass, time). |
| **Vector Quantity** | A physical quantity with both magnitude and direction (e.g., force, velocity). |
| **Resultant** | A single vector that produces the same effect as two or more vectors acting together. |
| **Resolution of Vectors** | Breaking down a single vector into two perpendicular components. |
| **Component** | The part of a vector acting in a specific direction (usually horizontal or vertical). |
| **Equilibrium** | A state where the resultant of all forces (or vectors) acting on an object is zero. |
| **Relative Velocity** | The velocity of a moving object as observed from another moving observer. |

## Exam tips and common mistakes

- **Scalar vs Vector checklist:** Always remember that Work, Energy, Power, and Temperature are **scalars**, even though students often confuse them for vectors.
- **Wrong trigonometry function:** When resolving vectors, a common mistake is using sine for the horizontal component when the angle given is to the horizontal. Remember: if the angle $\theta$ is to the horizontal, horizontal is $F \cos \theta$ and vertical is $F \sin \theta$.
- **Forgetting units in components:** A vector component is still a physical quantity. If the original vector is in Newtons ($N$), the component must also be in Newtons ($N$).
- **Relative velocity sign errors:** When bodies move in opposite directions, you must **add** their speeds to find the magnitude of relative velocity. When they move in the same direction, you **subtract**.
- **Calculators in JAMB:** You will not have a scientific calculator. Look out for the 3-4-5 triangle, the 5-12-13 triangle, or angles like $60^\circ$ ($\cos 60^\circ = 0.5$) and $120^\circ$ ($\cos 120^\circ = -0.5$), which can be solved easily by hand.

## Quick summary

1. Scalar quantities have only magnitude, while vector quantities have both magnitude and direction.
2. Mass, time, distance, and work are scalars; weight, displacement, velocity, and force are vectors.
3. The resultant of two vectors acting in the same direction is their sum; in opposite directions, it is their difference.
4. For perpendicular vectors, the resultant magnitude is found using Pythagoras' theorem ($R = \sqrt{x^2 + y^2}$).
5. Vectors can be resolved into horizontal ($F \cos \theta$) and vertical ($F \sin \theta$) components when $\theta$ is measured from the horizontal.
6. A closed triangle of vectors drawn tip-to-tail indicates that the three vectors are in equilibrium (resultant is zero).
7. Relative velocity is found by vector subtraction ($V_A - V_B$). For opposite directions, speeds add up; for the same direction, speeds subtract.

## Practice questions

**1. A physical quantity is defined as a vector if it has:**
- A. magnitude only
- B. magnitude and direction
- C. direction only
- D. mass and volume

**Answer: B.** A vector quantity is completely specified by both its magnitude (size) and its direction.

**2. Which of the following contains only scalar quantities?**
- A. Mass, speed and temperature
- B. Velocity, momentum and force
- C. Distance, acceleration and work
- D. Displacement, power and energy

**Answer: A.** Mass, speed, and temperature are all scalars. Option B contains only vectors. Options C and D contain mixtures.

**3. A boy pulls a toy cart with a force of $15\ \text{N}$ due East, while his friend pulls the same cart with a force of $10\ \text{N}$ due West. What is the resultant force on the cart?**
- A. $25\ \text{N}$ due East
- B. $25\ \text{N}$ due West
- C. $5\ \text{N}$ due East
- D. $5\ \text{N}$ due West

**Answer: C.** 
1. Determine the vectors: $15\ \text{N}$ East and $10\ \text{N}$ West.
2. Since they are collinear and in opposite directions, subtract them: $15\ \text{N} - 10\ \text{N} = 5\ \text{N}$.
3. The direction is that of the larger force, which is East. Resultant is $5\ \text{N}$ due East.
*Mistake behind Option A:* Adding the forces as if they acted in the same direction.

**4. Two forces of magnitude $5\ \text{N}$ and $3\ \text{N}$ act on a particle at an angle of $60^\circ$ to each other. Calculate the magnitude of the resultant force.**
- A. $4\ \text{N}$
- B. $7\ \text{N}$
- C. $8\ \text{N}$
- D. $15\ \text{N}$

**Answer: B.** 
1. Formula: $R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$.
2. Substitute: $R = \sqrt{5^2 + 3^2 + 2(5)(3)\cos 60^\circ}$.
3. Calculate: $R = \sqrt{25 + 9 + 2(15)(0.5)}$.
4. Simplify: $R = \sqrt{34 + 15} = \sqrt{49}$.
5. Final Answer: $7\ \text{N}$.
*Mistake behind Option C:* Simply adding $5 + 3 = 8$ without accounting for the angle.

**5. A force of $100\ \text{N}$ is applied to a block at an angle of $60^\circ$ to the horizontal. What is the effective force moving the block horizontally?**
- A. $50.0\ \text{N}$
- B. $86.6\ \text{N}$
- C. $100.0\ \text{N}$
- D. $200.0\ \text{N}$

**Answer: A.** 
1. The horizontal component formula is $F_x = F \cos \theta$.
2. Substitute: $F_x = 100 \cos 60^\circ$.
3. Evaluate: $\cos 60^\circ = 0.5$.
4. Calculate: $F_x = 100 \times 0.5 = 50.0\ \text{N}$.
*Mistake behind Option B:* Using $\sin 60^\circ$ (which calculates the vertical component) instead of $\cos 60^\circ$.

**6. A bus travels from Lagos to Ibadan at a steady speed of $80\ \text{km h}^{-1}$. A car travels from Ibadan to Lagos on the same road at a steady speed of $100\ \text{km h}^{-1}$. What is the velocity of the car relative to the bus?**
- A. $20\ \text{km h}^{-1}$ towards Ibadan
- B. $20\ \text{km h}^{-1}$ towards Lagos
- C. $180\ \text{km h}^{-1}$ towards Ibadan
- D. $180\ \text{km h}^{-1}$ towards Lagos

**Answer: D.** 
1. Let Lagos to Ibadan be positive (Bus $V_b = 80\ \text{km h}^{-1}$).
2. The car is going Ibadan to Lagos, so it is negative (Car $V_c = -100\ \text{km h}^{-1}$).
3. Velocity of car relative to bus is $V_{cb} = V_c - V_b$.
4. Substitute: $V_{cb} = -100 - 80 = -180\ \text{km h}^{-1}$.
5. The negative sign means it points towards Lagos.
*Mistake behind Option B:* Subtracting the magnitudes ($100 - 80 = 20$) as if they were travelling in the same direction.

**7. Two sprinters X and Y are running in the same direction. X runs at $10\ \text{m s}^{-1}$ and Y runs at $8\ \text{m s}^{-1}$. Find the velocity of X relative to Y.**
- A. $2\ \text{m s}^{-1}$
- B. $8\ \text{m s}^{-1}$
- C. $10\ \text{m s}^{-1}$
- D. $18\ \text{m s}^{-1}$

**Answer: A.** 
1. Both are in the same direction. $V_x = 10\ \text{m s}^{-1}$, $V_y = 8\ \text{m s}^{-1}$.
2. Velocity of X relative to Y is $V_{xy} = V_x - V_y$.
3. Substitute: $V_{xy} = 10 - 8$.
4. Calculate: $2\ \text{m s}^{-1}$.
*Mistake behind Option D:* Adding the speeds, which is only done if they are running in opposite directions.

**8. If three forces acting at a point can be represented in magnitude and direction by the three sides of a closed triangle taken in order, the forces are in:**
- A. motion
- B. acceleration
- C. equilibrium
- D. collision

**Answer: C.** This is the Triangle of Forces theorem. A closed polygon or triangle of vectors drawn head-to-tail indicates that the resultant is zero, meaning the object is in equilibrium.

**9. A boat travels due East across a river at $4\ \text{m s}^{-1}$. The river flows due South at $3\ \text{m s}^{-1}$. What is the resultant velocity of the boat relative to the earth?**
- A. $1\ \text{m s}^{-1}$
- B. $5\ \text{m s}^{-1}$
- C. $7\ \text{m s}^{-1}$
- D. $12\ \text{m s}^{-1}$

**Answer: B.** 
1. The velocities are at right angles (East and South).
2. Use Pythagoras' theorem: $R = \sqrt{V_{boat}^2 + V_{river}^2}$.
3. Substitute: $R = \sqrt{4^2 + 3^2}$.
4. Calculate: $R = \sqrt{16 + 9} = \sqrt{25}$.
5. Final Answer: $5\ \text{m s}^{-1}$.
*Mistake behind Option C:* Arithmetically adding $4 + 3 = 7$ instead of using vector addition.

**10. Two equal forces of $10\ \text{N}$ each act on a body at an angle of $120^\circ$ to each other. The magnitude of the resultant force is:**
- A. $0\ \text{N}$
- B. $10\ \text{N}$
- C. $14\ \text{N}$
- D. $20\ \text{N}$

**Answer: B.** 
1. Formula: $R = \sqrt{F^2 + F^2 + 2F \cdot F \cdot \cos 120^\circ}$.
2. Substitute: $R = \sqrt{10^2 + 10^2 + 2(10)(10)(-0.5)}$.
3. Calculate: $R = \sqrt{100 + 100 - 100} = \sqrt{100}$.
4. Final Answer: $10\ \text{N}$. (This is a standard shortcut rule to memorise).
*Mistake behind Option D:* Adding the forces algebraically as if they acted in the same straight line.
