# JAMB Physics Notes: Elasticity: Hooke's Law and Young's Modulus

## What JAMB expects

This file covers Topic 9 of the JAMB Physics syllabus: Elasticity: Hooke's law and Young's modulus.

It covers the following content items:
- (i) elastic limit, yield point, breaking point;
- (ii) the spring balance as a device for measuring force;
- (iii) work done per unit volume in springs and elastic strings.

By the end of these notes, you should be able to:
1. Interpret force-extension curves.
2. Interpret Hooke's law and Young's modulus of a material.
3. Use spring balance to measure force.
4. Determine the work done in spring and elastic strings.

## Hooke's Law and Young's Modulus

**Objective ii: interpret Hooke's law and Young's modulus of a material.**

### Elasticity and Hooke's Law
**Elasticity** is the ability of a material to regain its original shape and size after the applied force (the deforming force) that stretched or compressed it has been removed. Materials that behave this way, such as rubber bands and steel springs, are said to be **elastic**.

Hooke's Law states that **provided the elastic limit of an elastic material is not exceeded, the extension of the material is directly proportional to the applied force**.

Mathematically:
$$F \propto e$$
$$F = ke$$

Where:
- $F$ is the applied force or load in Newtons ($\text{N}$).
- $e$ is the extension (or compression) in metres ($\text{m}$). Extension is the new length minus the original length ($e = L_1 - L_0$).
- $k$ is the **force constant** (also known as the elastic constant, spring constant, or stiffness) of the material. Its unit is Newtons per metre ($\text{N m}^{-1}$).

The force constant $k$ tells us how stiff a spring is. A large $k$ means the spring is very stiff and requires a large force to stretch it, like the thick shock absorbers on a motorcycle (okada) or a car. A small $k$ means it is easily stretched, like the spring inside a pen.

**Worked Example 1: Calculating force constant**
A spring stretches by $0.2\ \text{m}$ when a pulling force of $50\ \text{N}$ is applied to it. Calculate its force constant.
1. State Hooke's law formula: $F = ke$.
2. Rearrange to make $k$ the subject: $k = \frac{F}{e}$.
3. Substitute the given values with units: $k = \frac{50\ \text{N}}{0.2\ \text{m}}$.
4. Calculate the answer: $k = 250\ \text{N m}^{-1}$.
The force constant is $250\ \text{N m}^{-1}$.

**Worked Example 2: Finding extension**
The force constant of a spiral spring is $400\ \text{N m}^{-1}$. What will be the extension if a mass of $5\ \text{kg}$ is suspended from its end? (Take $g = 10\ \text{m s}^{-2}$).
1. Calculate the force (weight) exerted by the mass: $F = mg = 5\ \text{kg} \times 10\ \text{m s}^{-2} = 50\ \text{N}$.
2. State Hooke's law: $F = ke$.
3. Rearrange to find extension: $e = \frac{F}{k}$.
4. Substitute the values: $e = \frac{50\ \text{N}}{400\ \text{N m}^{-1}}$.
5. Calculate the answer: $e = 0.125\ \text{m}$.
The extension is $0.125\ \text{m}$ (or $12.5\ \text{cm}$).

### Tensile Stress, Strain, and Young's Modulus

When comparing the strength of different materials (like steel versus copper), relying on the force constant $k$ is not enough because $k$ changes depending on how thick or long the wire is. Instead, physicists use stress, strain, and Young's modulus, which depend only on the *material* itself, regardless of its shape or size.

**Tensile Stress**
Tensile stress is the applied force per unit cross-sectional area of the material. It tells us how much force is spread over the thickness of the wire.
$$ \text{Stress} = \frac{\text{Force}}{\text{Area}} = \frac{F}{A} $$
Where:
- $F$ is the force in Newtons ($\text{N}$).
- $A$ is the cross-sectional area in square metres ($\text{m}^2$).
- The unit of stress is Newtons per square metre ($\text{N m}^{-2}$) or Pascals ($\text{Pa}$).

**Tensile Strain**
Tensile strain is the ratio of the extension to the original length of the material. It measures the fractional stretch of the wire.
$$ \text{Strain} = \frac{\text{Extension}}{\text{Original length}} = \frac{e}{L} $$
Where:
- $e$ is the extension in metres ($\text{m}$).
- $L$ is the original length in metres ($\text{m}$).
- Strain has **no unit** because it is a ratio of two lengths (metres divided by metres). It is dimensionless.

**Young's Modulus**
Young's modulus ($Y$ or $E$) is defined as the ratio of tensile stress to tensile strain, provided the elastic limit is not exceeded. It is a measure of the inherent stiffness of a material.
$$ Y = \frac{\text{Tensile Stress}}{\text{Tensile Strain}} = \frac{F/A}{e/L} $$
$$ Y = \frac{F L}{A e} $$
Where:
- $Y$ is Young's modulus in Newtons per square metre ($\text{N m}^{-2}$) or Pascals ($\text{Pa}$).

**Worked Example 3: Young's Modulus**
A power distribution cable of length $50\ \text{m}$ and cross-sectional area $1.0 \times 10^{-5}\ \text{m}^2$ is pulled tightly during installation with a tension force of $200\ \text{N}$. If the Young's modulus of the cable material is $1.0 \times 10^{11}\ \text{N m}^{-2}$, calculate the extension of the cable.
1. Identify the given values: $F = 200\ \text{N}$, $L = 50\ \text{m}$, $A = 1.0 \times 10^{-5}\ \text{m}^2$, $Y = 1.0 \times 10^{11}\ \text{N m}^{-2}$.
2. State the formula for extension derived from Young's modulus: $e = \frac{F L}{A Y}$.
3. Substitute with units: $e = \frac{200\ \text{N} \times 50\ \text{m}}{1.0 \times 10^{-5}\ \text{m}^2 \times 1.0 \times 10^{11}\ \text{N m}^{-2}}$.
4. Calculate the numerator: $200 \times 50 = 10000\ \text{N m}$.
5. Calculate the denominator: $1.0 \times 10^{-5} \times 1.0 \times 10^{11} = 1.0 \times 10^6\ \text{N}$.
6. Divide to find extension: $e = \frac{10000}{1000000} = 0.01\ \text{m}$.
The extension is $0.01\ \text{m}$ (or $1\ \text{cm}$).

> **Common mistake:** Forgetting to convert extensions from $\text{mm}$ or $\text{cm}$ to metres before calculating Young's modulus.
> *Wrong working:* With $e = 2\ \text{mm}$, area $= 0.001\ \text{m}^2$, force $= 100\ \text{N}$, length $= 4\ \text{m}$, calculating $Y = \frac{100 \times 4}{0.001 \times 2} = 200000\ \text{Pa}$.
> *Corrected version:* First convert $e = 2\ \text{mm} = 0.002\ \text{m}$, then calculate $Y = \frac{100 \times 4}{0.001 \times 0.002} = 200,000,000\ \text{Pa}$.

## Force-Extension Curves

**Objective i: interpret force-extension curves.**
**Content (i): elastic limit, yield point, breaking point.**

When a metal wire is stretched by gradually increasing the weight on it until it finally snaps, we can plot a graph of the applied Force ($F$) against the Extension ($e$). This force-extension curve shows us exactly how materials behave under stress.

[IMAGE: A line graph showing a Force (y-axis) against extension (x-axis) curve for a typical metal wire. The curve starts as a straight line from the origin to a point 'P' (Proportional limit). Shortly after 'P' is point 'E' (Elastic limit), where the line begins to curve. Further along is point 'Y' (Yield point) where the curve dips slightly and flattens out, indicating plastic flow. The curve then rises to a peak 'M' (Maximum load or Ultimate tensile strength), and finally ends at a lower point 'B' (Breaking point) where the wire snaps. Labels to add later: "Force, F (N)", "Extension, e (m)", "P (Proportional limit)", "E (Elastic limit)", "Y (Yield point)", "M (Maximum load)", "B (Breaking point)", "Elastic region", "Plastic region". Clean flat textbook illustration, white background.]

Here is what the key points on the curve mean:
- **Proportional Limit (P):** The maximum point up to which Hooke's Law is obeyed. The graph is a perfect straight line from the origin up to P, meaning force is directly proportional to extension.
- **Elastic Limit (E):** The maximum force the material can withstand and still return completely to its original length when the stretching force is removed. The region up to E is called the **elastic region**. If stretched beyond E, the material will have a permanent stretch (it will not go back to zero). 
- **Yield Point (Y):** Beyond the elastic limit, the material begins to stretch rapidly even without adding much extra force. The material has "yielded" and is now undergoing **plastic deformation** (behaving like soft dough).
- **Maximum Load (M):** Also called the Ultimate Tensile Strength. This is the greatest force the material can bear before it starts to thin out locally (a process called *necking*).
- **Breaking Point (B):** The point at which the wire finally snaps or breaks entirely.

*Note on textbook variation: Some textbooks treat the proportional limit and the elastic limit as the exact same point for simplicity, but strictly speaking, the elastic limit lies just slightly after the proportional limit.*

> **Common mistake:** Assuming the elastic limit and proportional limit are identical. While they are very close, Hooke's law ($F = ke$) stops exactly at the proportional limit, whereas the material can still behave elastically slightly beyond this up to the elastic limit.

## The Spring Balance

**Objective iii: use spring balance to measure force.**
**Content (ii): the spring balance as a device for measuring force.**

A **spring balance** (or Newton meter) is a simple mechanical instrument used to measure force. It works entirely on the principle of **Hooke's Law**. 

[IMAGE: Illustration of a spring balance (Newton meter). A tubular casing with a hook at the top for suspension and a hook at the bottom where a load is attached. Inside the casing, a coiled spring is visible or implied, connected to an indicator (pointer) that slides along a vertical scale on the outside of the casing. The scale is marked in Newtons (N) and usually grams (g) or kilograms (kg). Labels to add later: "Suspension ring", "Spring", "Indicator / Pointer", "Scale (N)", "Load (Force)". Clean flat textbook illustration, white background.]

Inside the casing is a stiff spring attached to a pointer. When you hang an object on the hook, its weight (a downward force) stretches the spring. Because Hooke's law says $F \propto e$, the distance the pointer moves down the scale is directly proportional to the force applied. The scale is calibrated to read this force directly in Newtons ($\text{N}$). 

*Practical note:* In Nigerian markets, spring balances are frequently used to weigh goods (like bags of rice or scrap metal) and the scales are marked in kilograms ($\text{kg}$). While kilograms measure *mass*, the spring is actually responding to the *weight* (the force of gravity) of the item pulling on it.

**Worked Example 4: The market spring balance**
A trader uses a spring balance to weigh a bag of beans. The spring inside the balance has a force constant of $2000\ \text{N m}^{-1}$ and it extends by $0.05\ \text{m}$ when the bag is hung on it. What is the mass of the bag of beans? (Take $g = 10\ \text{m s}^{-2}$).
1. Apply Hooke's Law to find the force (weight) stretching the spring: $F = ke$.
2. Substitute the values: $F = 2000\ \text{N m}^{-1} \times 0.05\ \text{m} = 100\ \text{N}$.
3. Recall the relationship between weight and mass: $W = mg$, so $F = mg$.
4. Rearrange to find mass: $m = \frac{F}{g}$.
5. Substitute to get mass: $m = \frac{100\ \text{N}}{10\ \text{m s}^{-2}} = 10\ \text{kg}$.
The mass of the bag of beans is $10\ \text{kg}$.

> **Common mistake:** Reading a spring balance marked in $\text{kg}$ as measuring weight directly in physics problems.
> *Wrong working:* Stating the weight is $10\ \text{kg}$.
> *Corrected version:* The mass is $10\ \text{kg}$. The actual weight (which is a force) is $W = mg = 10\ \text{kg} \times 10\ \text{m s}^{-2} = 100\ \text{N}$.

## Energy Stored: Work Done in Springs and Strings

**Objective iv: determine the work done in spring and elastic strings.**

When you stretch or compress a spring, you apply a force over a distance. This means you are doing **work**, which is stored in the spring as **elastic potential energy**.

Because the required force increases steadily from zero to $F$ as the spring stretches, we must use the *average* force to calculate the work done.
$$ \text{Average force} = \frac{0 + F}{2} = \frac{1}{2}F $$

Therefore, the work done $W$ is:
$$ W = \text{Average force} \times \text{extension} $$
$$ W = \frac{1}{2} F e $$

Since Hooke's Law states $F = ke$, we can substitute $F$ to get a second useful version of the formula:
$$ W = \frac{1}{2} (ke) e = \frac{1}{2} k e^2 $$
Where:
- $W$ is work done or energy stored in Joules ($\text{J}$).
- $F$ is the maximum applied force in Newtons ($\text{N}$).
- $e$ is the extension in metres ($\text{m}$).
- $k$ is the force constant in Newtons per metre ($\text{N m}^{-1}$).

**Graphical interpretation:** The work done is equal to the **area under the force-extension graph** up to the given extension point. Because the graph in the elastic region is a straight line starting from the origin, the shape is a triangle. The area of a triangle is $\frac{1}{2} \times \text{base} \times \text{height}$, which perfectly matches the formula $\frac{1}{2} \times e \times F$.

**Worked Example 5: Energy in a catapult**
A rubber catapult used by a child has a force constant of $300\ \text{N m}^{-1}$. If the child stretches the catapult by $0.1\ \text{m}$, calculate the energy stored (work done) in the rubber.
1. State the formula for elastic potential energy using the force constant: $W = \frac{1}{2} k e^2$.
2. Substitute the given values: $W = \frac{1}{2} \times 300\ \text{N m}^{-1} \times (0.1\ \text{m})^2$.
3. Calculate the square of the extension: $(0.1\ \text{m})^2 = 0.01\ \text{m}^2$.
4. Multiply: $W = 150\ \text{N m}^{-1} \times 0.01\ \text{m}^2 = 1.5\ \text{J}$.
The energy stored in the catapult is $1.5\ \text{J}$.

> **Common mistake:** Using the basic work formula $W = F e$ for springs, completely forgetting the $\frac{1}{2}$ factor.
> *Wrong working:* With force $= 50\ \text{N}$ and extension $= 0.2\ \text{m}$, calculating $W = 50\ \text{N} \times 0.2\ \text{m} = 10\ \text{J}$.
> *Corrected version:* You must use average force: $W = \frac{1}{2} F e = \frac{1}{2} \times 50\ \text{N} \times 0.2\ \text{m} = 5\ \text{J}$.

### Work done per unit volume

**Content (iii): work done per unit volume in springs and elastic strings.**

In material science, we often want to know how much energy is stored in every cubic metre of the stretched material. 
The total volume $V$ of a uniform wire is its cross-sectional area $A$ multiplied by its original length $L$ (so $V = A L$).

We can find the work done per unit volume by dividing the work equation by the volume equation:
$$ \frac{\text{Work}}{\text{Volume}} = \frac{\frac{1}{2} F e}{A L} = \frac{1}{2} \left( \frac{F}{A} \right) \left( \frac{e}{L} \right) $$

Recognising that $\frac{F}{A}$ is Stress and $\frac{e}{L}$ is Strain, we get:
$$ \text{Work done per unit volume} = \frac{1}{2} \times \text{Stress} \times \text{Strain} $$
- The unit is Joules per cubic metre ($\text{J m}^{-3}$).

**Worked Example 6: Work done per unit volume**
A metal wire undergoes a tensile stress of $4.0 \times 10^7\ \text{N m}^{-2}$ which produces a tensile strain of $0.002$. Calculate the work done per unit volume in the wire.
1. State the formula: $\frac{W}{V} = \frac{1}{2} \times \text{Stress} \times \text{Strain}$.
2. Substitute the values: $\frac{W}{V} = \frac{1}{2} \times 4.0 \times 10^7\ \text{N m}^{-2} \times 0.002$.
3. Multiply the values: $\frac{W}{V} = 2.0 \times 10^7 \times 0.002 = 40000\ \text{J m}^{-3}$.
The work done per unit volume is $4.0 \times 10^4\ \text{J m}^{-3}$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Elasticity** | The ability of a material to return to its original shape and size after a deforming force is removed. |
| **Hooke's Law** | States that the extension of an elastic material is directly proportional to the applied force, provided the elastic limit is not exceeded ($F = ke$). |
| **Force Constant ($k$)** | The force required to produce a unit extension in a spring. Also called stiffness. |
| **Elastic Limit** | The maximum force a material can bear and still return to its original length when the force is removed. |
| **Yield Point** | The point beyond the elastic limit where the material stretches rapidly and permanently with little or no extra force. |
| **Tensile Stress** | The applied force per unit cross-sectional area ($F/A$). |
| **Tensile Strain** | The ratio of the extension to the original length of the material ($e/L$). It has no units. |
| **Young's Modulus ($Y$)** | The ratio of tensile stress to tensile strain for a given material ($FL/Ae$). |

## Exam tips and common mistakes

- **Area conversions are a huge pitfall!** To convert area in square millimetres ($\text{mm}^2$) to square metres ($\text{m}^2$), you must square the prefix: $1\ \text{mm}^2 = 10^{-6}\ \text{m}^2$. (Do not use $10^{-3}$, which is only for length). Similarly, $1\ \text{cm}^2 = 10^{-4}\ \text{m}^2$.
- **Do not forget the half in Work Done!** The most common mistake in calculating work done in a spring is using $W = Fe$. It must be $W = \frac{1}{2}Fe$ because you are taking the area of the triangle under the curve.
- **Do not confuse proportional limit with elastic limit.** The proportional limit is where Hooke's Law stops working (the graph stops being a straight line). The elastic limit is where the material loses its elasticity and suffers permanent stretch.
- **Strain is unitless.** If a question asks for the unit of tensile strain, the correct answer is "no unit" or "dimensionless". Stress and Young's modulus both share the unit of pressure ($\text{N m}^{-2}$ or $\text{Pa}$).
- **Convert extensions to metres.** JAMB frequently gives extension in $\text{cm}$ or $\text{mm}$. Always divide by $100$ ($\text{cm}$) or $1000$ ($\text{mm}$) before substituting into formulas like $F=ke$ or work done.

## Quick summary

1. Hooke's Law states that force is directly proportional to extension ($F = ke$), up to the proportional limit.
2. The force constant $k$ measures the stiffness of the spring.
3. The force-extension curve points in order are: Proportional limit, Elastic limit, Yield point, Maximum load, and Breaking point.
4. A spring balance relies on Hooke's Law to measure forces (and weights) because the stretch of its spring is proportional to the applied force.
5. Tensile stress is Force / Area, and tensile strain is extension / original length.
6. Young's modulus is the ratio of tensile stress to tensile strain, representing the stiffness of a material independent of its dimensions.
7. Work done (energy stored) in stretching a string is given by $W = \frac{1}{2} F e$ or $W = \frac{1}{2} k e^2$, which corresponds to the area under the force-extension graph.
8. Work done per unit volume is $\frac{1}{2} \times \text{Stress} \times \text{Strain}$.

## Practice questions

**1. Hooke's law states that:**
- A. the extension of a spring is inversely proportional to the applied force, provided the elastic limit is not exceeded
- B. the applied force is directly proportional to the extension, provided the elastic limit is not exceeded
- C. the stress is equal to the strain, provided the yield point is not exceeded
- D. the work done is equal to force times extension

**Answer: B.**
1. Recall the mathematical expression for Hooke's law: $F = ke$.
2. Identify that force $F$ and extension $e$ are on opposite sides of the equation, indicating they are directly proportional.
3. Note the standard physical condition: this strictly applies only before the material exceeds its elastic limit.
*Mistake for option A:* incorrectly assuming an inverse relationship where $F \propto \frac{1}{e}$.

**2. The point on a force-extension graph beyond which the material can no longer return to its original length when the stretching force is removed is the:**
- A. proportional limit
- B. yield point
- C. elastic limit
- D. breaking point

**Answer: C.**
1. Define the elastic limit as the maximum force point $F_{\text{elastic}}$ where the material retains its elasticity.
2. Recognize that removing the force below this point returns extension to $e = 0\ \text{m}$.
3. Beyond this point, removing the force leaves a permanent plastic extension where $e > 0\ \text{m}$.
*Mistake for option A:* confusing the elastic limit with the proportional limit (the point where the graph simply stops being a straight line, ending Hooke's law).

**3. A spring balance reads $10\ \text{N}$ when its spring is extended by $2.0\ \text{cm}$. What is the force constant of the spring in $\text{N m}^{-1}$?**
- A. $5\ \text{N m}^{-1}$
- B. $20\ \text{N m}^{-1}$
- C. $500\ \text{N m}^{-1}$
- D. $5000\ \text{N m}^{-1}$

**Answer: C.** 
1. Convert extension from centimetres to metres: $e = 2.0\ \text{cm} = 0.02\ \text{m}$.
2. State Hooke's Law formula: $F = ke$.
3. Rearrange to find the force constant: $k = \frac{F}{e}$.
4. Substitute the values: $k = \frac{10\ \text{N}}{0.02\ \text{m}}$.
5. Calculate the answer: $k = 500\ \text{N m}^{-1}$. 
*Mistake for option A:* directly calculating $\frac{10\ \text{N}}{2.0\ \text{cm}}$ without converting $\text{cm}$ to $\text{m}$.

**4. A wire is stretched by a force of $100\ \text{N}$ producing an extension of $0.2\ \text{m}$. Calculate the work done in stretching the wire.**
- A. $2\ \text{J}$
- B. $10\ \text{J}$
- C. $20\ \text{J}$
- D. $500\ \text{J}$

**Answer: B.**
1. State the formula for work done on a string: $W = \frac{1}{2} F e$.
2. Substitute the given values: $W = \frac{1}{2} \times 100\ \text{N} \times 0.2\ \text{m}$.
3. Calculate the product: $W = 50\ \text{N} \times 0.2\ \text{m}$.
4. Final answer: $W = 10\ \text{J}$.
*Mistake for option C:* using the generic work formula $W = F e$ and forgetting the $\frac{1}{2}$ factor.

**5. Which of the following correctly defines Young's modulus?**
- A. The ratio of tensile strain to tensile stress
- B. The ratio of tensile stress to tensile strain
- C. The product of force and extension
- D. The ratio of extension to original length

**Answer: B.**
1. State the symbol for Young's modulus: $Y$.
2. State the formula defining it: $Y = \frac{\text{Stress}}{\text{Strain}}$.
3. Conclude that it is the ratio of tensile stress to tensile strain.
*Mistake for option A:* inverting the formula as $\frac{\text{Strain}}{\text{Stress}}$, which actually gives the reciprocal of Young's modulus.

**6. A wire of length $3.0\ \text{m}$ and cross-sectional area $2.0 \times 10^{-6}\ \text{m}^2$ is extended by $1.5\ \text{mm}$ when a force of $120\ \text{N}$ is applied. Calculate its Young's modulus.**
- A. $1.2 \times 10^{11}\ \text{N m}^{-2}$
- B. $1.2 \times 10^8\ \text{N m}^{-2}$
- C. $6.0 \times 10^7\ \text{N m}^{-2}$
- D. $2.4 \times 10^5\ \text{N m}^{-2}$

**Answer: A.**
1. Convert extension to SI units: $e = 1.5\ \text{mm} = 1.5 \times 10^{-3}\ \text{m}$.
2. State the Young's modulus formula: $Y = \frac{F L}{A e}$.
3. Substitute the values: $Y = \frac{120\ \text{N} \times 3.0\ \text{m}}{2.0 \times 10^{-6}\ \text{m}^2 \times 1.5 \times 10^{-3}\ \text{m}}$.
4. Calculate the numerator: $120 \times 3.0 = 360\ \text{N m}$.
5. Calculate the denominator: $2.0 \times 10^{-6} \times 1.5 \times 10^{-3} = 3.0 \times 10^{-9}\ \text{m}^3$.
6. Divide to find $Y$: $Y = \frac{360}{3.0 \times 10^{-9}} = 1.2 \times 10^{11}\ \text{N m}^{-2}$.
*Mistake for option B:* forgetting to convert $1.5\ \text{mm}$ to metres, leaving $e = 1.5\ \text{m}$.

**7. On a force-extension curve, the yield point represents the point at which:**
- A. the material stops obeying Hooke's law ($F = ke$)
- B. the material breaks entirely
- C. the material undergoes a large plastic deformation with little or no added force
- D. the material reaches its ultimate tensile strength

**Answer: C.**
1. Identify the yield point location on the force-extension graph.
2. Note that at this specific point, the extension $e$ increases rapidly.
3. Observe that the force $F$ remains practically constant.
4. Conclude this represents a large plastic deformation.
*Mistake for option A:* confusing the yield point with the proportional limit, which is where Hooke's law $F = ke$ ends.

**8. A metal wire experiences a tensile stress of $5.0 \times 10^7\ \text{N m}^{-2}$ and a tensile strain of $4.0 \times 10^{-3}$. What is the work done per unit volume in stretching the wire?**
- A. $1.0 \times 10^5\ \text{J m}^{-3}$
- B. $2.0 \times 10^5\ \text{J m}^{-3}$
- C. $6.25 \times 10^9\ \text{J m}^{-3}$
- D. $1.25 \times 10^{10}\ \text{J m}^{-3}$

**Answer: A.**
1. State the formula for work done per unit volume: $\frac{W}{V} = \frac{1}{2} \times \text{Stress} \times \text{Strain}$.
2. Substitute the given values: $\frac{W}{V} = \frac{1}{2} \times 5.0 \times 10^7\ \text{N m}^{-2} \times 4.0 \times 10^{-3}$.
3. Calculate the product of stress and strain: $\frac{W}{V} = \frac{1}{2} \times 200,000\ \text{J m}^{-3}$.
4. Calculate the final answer: $100,000\ \text{J m}^{-3} = 1.0 \times 10^5\ \text{J m}^{-3}$.
*Mistake for option B:* omitting the $\frac{1}{2}$ factor and simply multiplying stress and strain.

**9. What is the SI unit of tensile strain?**
- A. Metre ($\text{m}$)
- B. Newton per metre ($\text{N m}^{-1}$)
- C. Pascal ($\text{Pa}$)
- D. It has no unit

**Answer: D.**
1. State the mathematical formula for tensile strain: $\text{Strain} = \frac{e}{L}$.
2. Substitute the standard SI unit for extension $e$, which is metres ($\text{m}$).
3. Substitute the standard SI unit for length $L$, which is metres ($\text{m}$).
4. Divide the units to see they cancel out: $\frac{\text{m}}{\text{m}} = 1$, leaving it dimensionless.
*Mistake for option A:* giving the unit for extension alone instead of the strain ratio.

**10. A force-extension graph for an elastic string is a straight line passing through the origin. If the string is extended by $10\ \text{cm}$ under a maximum force of $50\ \text{N}$, what is the energy stored in the string?**
- A. $500\ \text{J}$
- B. $250\ \text{J}$
- C. $5.0\ \text{J}$
- D. $2.5\ \text{J}$

**Answer: D.**
1. Convert extension from centimetres to metres: $e = 10\ \text{cm} = 0.1\ \text{m}$.
2. State the formula for energy stored (work done): $W = \frac{1}{2} F e$.
3. Substitute the correct values: $W = \frac{1}{2} \times 50\ \text{N} \times 0.1\ \text{m}$.
4. Calculate the product: $W = 25\ \text{N} \times 0.1\ \text{m} = 2.5\ \text{J}$.
*Mistake for option B:* using the extension in $\text{cm}$ instead of metres to incorrectly get $\frac{1}{2} \times 50 \times 10 = 250\ \text{J}$.
