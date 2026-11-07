# JAMB Mathematics Notes: Application of differentiation

## What JAMB expects

This topic is Section IV, Topic 2 of the JAMB Mathematics syllabus: Application of differentiation. It covers the following content items:

- **a.** rate of change;
- **b.** maxima and minima.

By the end of these notes, you should be able to:

1. solve problems involving applications of rate of change, maxima and minima.

*(Note: The basic rules of differentiation are covered in `D1-differentiation.md`. These notes focus purely on how to apply those rules to solve practical mathematical and real-world problems.)*

## Solving problems involving differentiation

**Objective only: solve problems involving applications of rate of change, maxima and minima.**

Differentiation is an incredibly powerful tool for analysing how things change. In calculus, the derivative $\frac{dy}{dx}$ tells us the **gradient** (or slope) of a curve. Practically, this gradient represents the **rate of change** of $y$ with respect to $x$. 

Whenever a quantity is changing (such as a car's velocity, an expanding balloon's volume, or a trader's profit), we can use differentiation to study it. Furthermore, when the rate of change is zero ($\frac{dy}{dx} = 0$), the graph of the function is flat. This property is what allows us to find the **maximum** or **minimum** values of a function, which is useful in optimization (for example, finding the dimensions that give the maximum area for a farm, or the minimum cost of producing goods).

## Rate of change

**Content a: rate of change.**

The expression $\frac{dy}{dx}$ literally means "the rate at which $y$ changes as $x$ changes". If $y$ represents area and $x$ represents the radius, $\frac{dy}{dx}$ is the rate of change of the area with respect to the radius. 

### Geometrical rates of change

In simple cases, we want to find how quickly a geometrical quantity (like area or volume) changes as its dimensions change.

**Example 1**
Find the rate of change of the volume $V$ of a cube with respect to its side length $x$, when $x = 4 \text{ cm}$.

**Solution:**
1. Write the formula for the volume of a cube in terms of its side length: $V = x^3$.
2. Differentiate $V$ with respect to $x$ to find the rate of change equation:
   $$\frac{dV}{dx} = 3x^2$$
3. Substitute $x = 4$ into the derivative to find the specific rate at that instant:
   $$\frac{dV}{dx} = 3(4^2) = 3(16) = 48$$
   The rate of change is $48 \text{ cm}^2$.

### Related rates (Rates of change with respect to time)

Most real-world changes happen over time ($t$). For example, if a circular pool of water is expanding, its radius $r$ is increasing over time, which means its area $A$ is also increasing over time. We are often given the rate at which the radius changes ($\frac{dr}{dt}$) and asked to find the rate at which the area changes ($\frac{dA}{dt}$).

To solve this, we link the rates together using the **Chain Rule**:
$$\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt}$$

[IMAGE: Three concentric circles representing expanding ripples on water. A straight line is drawn from the centre to the outermost edge, labelled 'r'. An outward-pointing arrow on the outer circle is labelled 'dr/dt' to show expansion. Clean flat textbook style, white background.]

**Example 2**
The radius of a circular metal plate is increasing at a rate of $0.5 \text{ cm/s}$ when heated. Find the rate of increase of its area when the radius is $10 \text{ cm}$.

**Solution:**
1. State the formula for the area of a circle: $A = \pi r^2$.
2. Identify what is required. We need to find $\frac{dA}{dt}$. According to the chain rule:
   $$\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt}$$
3. Differentiate $A$ with respect to $r$ to find $\frac{dA}{dr}$:
   $$\frac{dA}{dr} = 2\pi r$$
4. We are given $\frac{dr}{dt} = 0.5 \text{ cm/s}$ and $r = 10 \text{ cm}$. Substitute these values into the chain rule formula:
   $$\frac{dA}{dt} = 2\pi(10) \times 0.5$$
   $$\frac{dA}{dt} = 20\pi \times 0.5 = 10\pi \text{ cm}^2\text{/s}$$

**Example 3**
A spherical balloon is being pumped up such that its volume increases at a constant rate of $20 \text{ cm}^3\text{/s}$. Find the rate at which its radius is increasing when the radius is $2 \text{ cm}$. *(Volume of a sphere = $\frac{4}{3}\pi r^3$)*.

**Solution:**
1. State the formula for the volume: $V = \frac{4}{3}\pi r^3$.
2. Identify the given values: we are given $\frac{dV}{dt} = 20 \text{ cm}^3\text{/s}$ and asked to find $\frac{dr}{dt}$.
3. Set up the relationship using the chain rule:
   $$\frac{dV}{dt} = \frac{dV}{dr} \times \frac{dr}{dt}$$
4. Differentiate $V$ with respect to $r$:
   $$\frac{dV}{dr} = 3 \times \frac{4}{3}\pi r^2 = 4\pi r^2$$
5. Substitute the known values ($r = 2$ and $\frac{dV}{dt} = 20$) into the chain rule:
   $$20 = 4\pi (2^2) \times \frac{dr}{dt}$$
   $$20 = 16\pi \times \frac{dr}{dt}$$
6. Make $\frac{dr}{dt}$ the subject to find the final answer:
   $$\frac{dr}{dt} = \frac{20}{16\pi} = \frac{5}{4\pi} \text{ cm/s}$$

### Kinematics: Distance, velocity and acceleration

In physics and mathematics, the movement of a particle along a straight line can be described using calculus. 

- **Distance/Displacement ($s$ or $x$):** The position of the object at time $t$.
- **Velocity ($v$):** The rate of change of displacement with respect to time.
  $$v = \frac{ds}{dt}$$
- **Acceleration ($a$):** The rate of change of velocity with respect to time.
  $$a = \frac{dv}{dt} \quad \text{or} \quad a = \frac{d^2s}{dt^2}$$

**Important terms to remember for kinematics:**
- **Initial:** This means at the start, so time $t = 0$.
- **At rest / Stationary:** The object is not moving, which means velocity $v = 0$.
- **Constant velocity:** Velocity is not changing, which means acceleration $a = 0$.

**Example 4**
A particle moves in a straight line such that its distance $s$ metres from a fixed point after $t$ seconds is given by $s = 2t^3 - 3t^2 + 4t - 1$. Find its velocity and acceleration after $2$ seconds.

**Solution:**
1. Find the equation for velocity by differentiating displacement $s$ with respect to time $t$:
   $$v = \frac{ds}{dt} = 6t^2 - 6t + 4$$
2. Substitute $t = 2$ into the velocity equation:
   $$v = 6(2^2) - 6(2) + 4$$
   $$v = 6(4) - 12 + 4 = 24 - 12 + 4 = 16 \text{ m/s}$$
3. Find the equation for acceleration by differentiating velocity $v$ with respect to time $t$:
   $$a = \frac{dv}{dt} = 12t - 6$$
4. Substitute $t = 2$ into the acceleration equation:
   $$a = 12(2) - 6 = 24 - 6 = 18 \text{ m/s}^2$$

**Example 5**
The displacement of a moving car is given by $s = t^3 - 6t^2 + 9t + 5$. At what times is the car at rest?

**Solution:**
1. Recall the definition: "at rest" means the velocity is zero ($v = 0$).
2. Find the velocity equation by differentiating $s$:
   $$v = \frac{ds}{dt} = 3t^2 - 12t + 9$$
3. Set $v = 0$ to find when the car stops:
   $$3t^2 - 12t + 9 = 0$$
4. Divide through by $3$ to make the quadratic equation simpler:
   $$t^2 - 4t + 3 = 0$$
5. Factorise to solve for $t$:
   $$(t - 1)(t - 3) = 0$$
   $$t = 1 \text{ or } t = 3$$
   The car is at rest at $1 \text{ second}$ and $3 \text{ seconds}$.

---

## Maxima and minima

**Content b: maxima and minima.**

When a curve goes up, reaches a peak, and comes back down, that peak is a **local maximum**. When a curve goes down, hits a bottom, and goes back up, that bottom is a **local minimum**. 

At both a maximum and a minimum, the curve is completely flat for a split second. Because the tangent to the curve is horizontal at these points, the gradient is exactly zero.
These points are known as **stationary points** or **turning points**.

### Finding stationary points
To find the coordinates of a stationary point on a curve $y = f(x)$:
1. Differentiate to find the gradient function $\frac{dy}{dx}$.
2. Set $\frac{dy}{dx} = 0$ and solve for $x$.
3. Substitute the $x$-value(s) back into the **original equation** ($y$) to find the corresponding $y$-coordinate.

### The Second Derivative Test

Once you find a stationary point, how do you know if it is a maximum or a minimum? The quickest way in JAMB is to use the **second derivative** ($\frac{d^2y}{dx^2}$). 

- If **$\frac{d^2y}{dx^2} < 0$** (negative), the point is a **Maximum**.
- If **$\frac{d^2y}{dx^2} > 0$** (positive), the point is a **Minimum**.
- If $\frac{d^2y}{dx^2} = 0$, the test fails (it could be a point of inflection, but this is rarely tested in UTME).

*Common mistake: Students often think "negative" means minimum and "positive" means maximum. It is the exact opposite! A negative second derivative means the gradient is decreasing (curving downwards like a frown), which creates a maximum peak.*

[IMAGE: A graph plotted on Cartesian axes showing a smooth curve y = f(x). The curve rises to a peak (local maximum) and then falls to a valley (local minimum). At both the peak and the valley, horizontal dashed lines are drawn to represent the tangents. Labels indicate "Local Maximum, dy/dx = 0, d²y/dx² < 0" at the peak and "Local Minimum, dy/dx = 0, d²y/dx² > 0" at the valley. Clean flat textbook style, white background.]

### Finding maximum and minimum values

**Example 6**
Find the maximum and minimum values of the function $y = 2x^3 - 3x^2 - 12x + 5$.

**Solution:**
1. Differentiate the function to find the gradient:
   $$\frac{dy}{dx} = 6x^2 - 6x - 12$$
2. Equate the gradient to zero to find the stationary points:
   $$6x^2 - 6x - 12 = 0$$
   Divide through by $6$ to simplify:
   $$x^2 - x - 2 = 0$$
   Factorise the quadratic:
   $$(x - 2)(x + 1) = 0 \implies x = 2 \text{ or } x = -1$$
3. Find the second derivative to test each point:
   $$\frac{d^2y}{dx^2} = 12x - 6$$
   - When $x = -1$: $\frac{d^2y}{dx^2} = 12(-1) - 6 = -18$. Since it is **negative**, $x = -1$ gives a **maximum**.
   - When $x = 2$: $\frac{d^2y}{dx^2} = 12(2) - 6 = 18$. Since it is **positive**, $x = 2$ gives a **minimum**.
4. To find the **maximum value**, substitute $x = -1$ into the **original equation**:
   $$y_{max} = 2(-1)^3 - 3(-1)^2 - 12(-1) + 5$$
   $$y_{max} = 2(-1) - 3(1) + 12 + 5 = -2 - 3 + 12 + 5 = 12$$
5. To find the **minimum value**, substitute $x = 2$ into the **original equation**:
   $$y_{min} = 2(2)^3 - 3(2)^2 - 12(2) + 5$$
   $$y_{min} = 2(8) - 3(4) - 24 + 5 = 16 - 12 - 24 + 5 = -15$$

**Example 7**
Find the minimum value of $y = x^2 - 8x + 10$.

**Solution:**
1. Differentiate to find the gradient function: 
   $$\frac{dy}{dx} = 2x - 8$$
2. Equate to zero: 
   $$2x - 8 = 0 \implies 2x = 8 \implies x = 4$$
3. Check the nature of the turning point (this is optional for a simple quadratic opening upwards, but it is good practice): 
   $$\frac{d^2y}{dx^2} = 2$$ 
   Since this is strictly positive, the point is confirmed as a minimum.
4. Find the minimum value by substituting $x = 4$ back into the original equation $y$:
   $$y_{min} = 4^2 - 8(4) + 10 = 16 - 32 + 10 = -6$$
   The minimum value is $-6$.

### Practical optimization problems

Optimization involves using maxima and minima to find the best possible outcome in real-world scenarios, such as maximizing profit, maximizing area, or minimizing cost. 

**Steps for optimization problems:**
1. Identify the quantity you need to maximize or minimize.
2. Write an equation for this quantity in terms of **one** variable. (You may need to use a second piece of given information to eliminate other variables).
3. Differentiate the equation and set it to zero.
4. Solve for the variable and calculate the maximum/minimum value.

**Example 8 (Maximizing Area)**
A farmer in Kano has $40 \text{ m}$ of wire netting to enclose a rectangular pen against a solid straight wall. He only needs to fence three sides because the wall acts as the fourth side. Find the maximum area he can enclose.

[IMAGE: A diagram showing a rectangular enclosure built against an existing straight wall. The straight wall forms one side of the rectangle. The opposite side is labelled 'y' and the two adjacent sides are labelled 'x'. The area inside is shaded. The text reads 'Total length of fence = 2x + y'. Clean flat textbook style, white background.]

**Solution:**
1. Let the two perpendicular sides be $x$ and the parallel side be $y$.
   The total length of the fencing is the sum of these three sides: $2x + y = 40$.
   Make $y$ the subject so we can eliminate it later: $y = 40 - 2x$.
2. We want to maximize the **Area** ($A$). 
   $$A = x \times y$$
   Substitute $y$ to get the area in terms of $x$ only:
   $$A = x(40 - 2x) = 40x - 2x^2$$
3. Differentiate $A$ with respect to $x$ to find the rate of change of area:
   $$\frac{dA}{dx} = 40 - 4x$$
4. Set the derivative to zero to find the maximum area:
   $$40 - 4x = 0 \implies 4x = 40 \implies x = 10 \text{ m}$$
5. If $x = 10$, substitute back into our length equation to find $y$: 
   $$y = 40 - 2(10) = 20 \text{ m}$$
6. Calculate the maximum area:
   $$A_{max} = x \times y = 10 \times 20 = 200 \text{ m}^2$$

**Example 9 (Maximizing Profit)**
The profit $P$ (in naira) made by a trader in Balogun market from selling $x$ bags of rice is given by $P = 200x - 2x^2$. Find the number of bags she must sell to make the maximum profit, and calculate that maximum profit.

**Solution:**
1. We are already given the profit function in terms of one variable ($x$).
   $$P = 200x - 2x^2$$
2. Differentiate $P$ with respect to $x$ to find the rate at which profit changes:
   $$\frac{dP}{dx} = 200 - 4x$$
3. Set the derivative to zero to find the peak profit:
   $$200 - 4x = 0 \implies 4x = 200 \implies x = 50$$
   She must sell **50 bags** of rice to maximize her profit.
4. Calculate the maximum profit by substituting $x = 50$ into the original $P$ equation:
   $$P_{max} = 200(50) - 2(50^2) = 10,000 - 2(2500)$$
   $$P_{max} = 10,000 - 5000 = 5,000$$
   The maximum profit is **₦5,000**.

## Key terms

| Term | Meaning |
| --- | --- |
| **Rate of change** | How fast one quantity changes in relation to another (represented by the derivative $\frac{dy}{dx}$). |
| **Displacement ($s$)** | The distance moved by a particle in a given direction from a fixed point. |
| **Velocity ($v$)** | The rate of change of displacement with respect to time ($\frac{ds}{dt}$). |
| **Acceleration ($a$)** | The rate of change of velocity with respect to time ($\frac{dv}{dt}$ or $\frac{d^2s}{dt^2}$). |
| **Stationary point / Turning point** | A point on a curve where the gradient is exactly zero ($\frac{dy}{dx} = 0$). |
| **Local maximum** | A turning point that is higher than the nearby points (resembles a hill peak). |
| **Local minimum** | A turning point that is lower than the nearby points (resembles a valley bottom). |
| **Second derivative test** | Using $\frac{d^2y}{dx^2}$ to determine if a stationary point is a maximum (if negative) or a minimum (if positive). |
| **Optimization** | The process of using calculus to find the maximum or minimum value of a quantity in a practical problem. |

## Exam tips and common mistakes

- **Mixing up the second derivative rules:** Remember that a **negative** second derivative ($\frac{d^2y}{dx^2} < 0$) indicates a **maximum**, and a **positive** second derivative ($\frac{d^2y}{dx^2} > 0$) indicates a **minimum**.
- **Substituting into the wrong equation:** When finding the maximum or minimum *value*, many students mistakenly substitute their $x$-value back into $\frac{dy}{dx}$ (which will always just give $0$). You must substitute $x$ into the **original equation** $y = f(x)$.
- **Forgetting the chain rule in related rates:** If a sphere's volume is expanding over time, $\frac{dV}{dt}$ is NOT just $4\pi r^2$. You must multiply by the rate of change of the radius: $\frac{dV}{dt} = 4\pi r^2 \times \frac{dr}{dt}$.
- **Kinematics wording:** "Starts from rest" means at $t = 0, v = 0$. "Comes to rest" or "is stationary" means $v = 0$ (at whatever time that happens).
- **Geometric formulas:** JAMB rarely provides formulas for the area of a circle ($A = \pi r^2$) or the volume of a sphere ($V = \frac{4}{3}\pi r^3$) in rate-of-change questions. You must memorize them beforehand.

## Quick summary

1. The derivative $\frac{dy}{dx}$ measures the rate of change of $y$ with respect to $x$.
2. To find the rate of change of a geometric quantity over time, use the chain rule (for example, $\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt}$).
3. In kinematics, velocity is the first derivative of displacement ($v = \frac{ds}{dt}$), and acceleration is the second derivative ($a = \frac{dv}{dt} = \frac{d^2s}{dt^2}$).
4. A curve reaches a maximum or minimum turning point when its gradient is zero ($\frac{dy}{dx} = 0$).
5. Use the second derivative ($\frac{d^2y}{dx^2}$) to test turning points: a negative value means a maximum, a positive value means a minimum.
6. To find the actual maximum or minimum value, solve for $x$ where $\frac{dy}{dx} = 0$, and substitute this $x$ into the original function.
7. Optimization problems require you to set up an equation for the quantity to be maximized or minimized, differentiate it, and equate it to zero.

## Practice questions

**1. Find the minimum value of the function $f(x) = x^2 - 6x + 8$.**

- A. $-1$
- B. $3$
- C. $8$
- D. $0$

**Answer: A.**
1. Differentiate the function: $f'(x) = 2x - 6$.
2. Equate to zero to find the turning point: $2x - 6 = 0 \implies 2x = 6 \implies x = 3$.
3. Substitute $x = 3$ into the original function to find the minimum value: $f(3) = 3^2 - 6(3) + 8 = 9 - 18 + 8 = -1$. (Note: Option B is just the $x$-value, not the minimum value itself. This is a common trap).

**2. The distance covered by a moving particle is $s = 2t^3 - 9t^2 + 12t$. Find the time(s) when the velocity is zero.**

- A. $1\text{ s}$ and $2\text{ s}$
- B. $-1\text{ s}$ and $-2\text{ s}$
- C. $2\text{ s}$ and $3\text{ s}$
- D. $1\text{ s}$ and $3\text{ s}$

**Answer: A.**
1. Differentiate displacement to find velocity: $v = \frac{ds}{dt} = 6t^2 - 18t + 12$.
2. Set velocity to zero: $6t^2 - 18t + 12 = 0$.
3. Divide through by $6$ to simplify: $t^2 - 3t + 2 = 0$.
4. Factorise the quadratic: $(t - 1)(t - 2) = 0 \implies t = 1, t = 2$.

**3. If $y = x^3 - 3x^2 + 5$, find the maximum value of $y$.**

- A. $1$
- B. $2$
- C. $5$
- D. $0$

**Answer: C.**
1. Find the gradient function: $\frac{dy}{dx} = 3x^2 - 6x = 0$.
2. Factorise to find turning points: $3x(x - 2) = 0 \implies x = 0$ or $x = 2$.
3. Test using the second derivative: $\frac{d^2y}{dx^2} = 6x - 6$.
4. At $x = 0$, $\frac{d^2y}{dx^2} = -6$ (negative $\implies$ maximum). At $x = 2$, $\frac{d^2y}{dx^2} = 6$ (positive $\implies$ minimum).
5. We want the maximum value, so we substitute $x = 0$ into the original equation $y$: $y = 0^3 - 3(0^2) + 5 = 5$.

**4. A balloon is pumped such that its volume increases at $10 \text{ cm}^3\text{/s}$. Find the rate of increase of its radius when the radius is $5 \text{ cm}$. (Volume of a sphere = $\frac{4}{3}\pi r^3$).**

- A. $\frac{1}{10\pi} \text{ cm/s}$
- B. $\frac{1}{5\pi} \text{ cm/s}$
- C. $10\pi \text{ cm/s}$
- D. $\frac{2}{5\pi} \text{ cm/s}$

**Answer: A.**
1. State the formula: $V = \frac{4}{3}\pi r^3$.
2. Differentiate with respect to $r$: $\frac{dV}{dr} = 4\pi r^2$.
3. Use the chain rule: $\frac{dV}{dt} = \frac{dV}{dr} \times \frac{dr}{dt}$.
4. Substitute $r = 5$ and $\frac{dV}{dt} = 10$: $10 = 4\pi(5^2) \times \frac{dr}{dt} \implies 10 = 100\pi \times \frac{dr}{dt}$.
5. Make $\frac{dr}{dt}$ the subject: $\frac{dr}{dt} = \frac{10}{100\pi} = \frac{1}{10\pi} \text{ cm/s}$.

**5. Find the coordinates of the minimum turning point of the curve $y = 2x^2 - 8x + 3$.**

- A. $(2, 5)$
- B. $(-2, -5)$
- C. $(2, -5)$
- D. $(-2, 5)$

**Answer: C.**
1. Differentiate and equate to zero: $\frac{dy}{dx} = 4x - 8 = 0 \implies 4x = 8 \implies x = 2$.
2. Substitute $x = 2$ back into $y$ to find the corresponding $y$-coordinate: $y = 2(2^2) - 8(2) + 3 = 2(4) - 16 + 3 = 8 - 16 + 3 = -5$.
3. The coordinates are $(2, -5)$.

**6. The profit $P$ (in naira) made from selling $x$ items is given by the equation $P(x) = 50x - x^2$. Find the maximum profit.**

- A. $₦25$
- B. $₦625$
- C. $₦1,250$
- D. $₦50$

**Answer: B.**
1. Differentiate the profit function: $P'(x) = 50 - 2x$.
2. Set to zero to find the number of items for maximum profit: $50 - 2x = 0 \implies 2x = 50 \implies x = 25$.
3. Substitute $x = 25$ back into the original profit function: $P(25) = 50(25) - (25^2) = 1250 - 625 = 625$. (Option A is just the $x$-value).

**7. Find the rate of change of the volume $V$ of a cube with respect to its side length $x$ when $x = 3 \text{ cm}$.**

- A. $9 \text{ cm}^2$
- B. $18 \text{ cm}^2$
- C. $27 \text{ cm}^2$
- D. $54 \text{ cm}^2$

**Answer: C.**
1. Recall the volume of a cube: $V = x^3$.
2. Find the rate of change with respect to $x$: $\frac{dV}{dx} = 3x^2$.
3. Substitute $x = 3$: $\frac{dV}{dx} = 3(3^2) = 3(9) = 27$. (Option D is $6x^2$, which represents the total surface area, not the rate of change of volume).

**8. A body moves along a straight line such that its distance $s$ metres from a fixed point after $t$ seconds is $s = t^3 - 3t^2 + 5t$. Find the acceleration at $t = 2 \text{ seconds}$.**

- A. $6 \text{ m/s}^2$
- B. $5 \text{ m/s}^2$
- C. $12 \text{ m/s}^2$
- D. $18 \text{ m/s}^2$

**Answer: A.**
1. Find velocity by differentiating displacement: $v = \frac{ds}{dt} = 3t^2 - 6t + 5$.
2. Find acceleration by differentiating velocity: $a = \frac{dv}{dt} = 6t - 6$.
3. Substitute $t = 2$ into the acceleration equation: $a = 6(2) - 6 = 12 - 6 = 6 \text{ m/s}^2$.

**9. What is the maximum value of $y = \sin x + \cos x$ for $0^\circ \le x \le 90^\circ$?**

- A. $1$
- B. $\sqrt{2}$
- C. $2$
- D. $0$

**Answer: B.**
1. Differentiate the function: $\frac{dy}{dx} = \cos x - \sin x$.
2. Set to zero to find the turning point: $\cos x - \sin x = 0 \implies \sin x = \cos x$.
3. Divide both sides by $\cos x$: $\frac{\sin x}{\cos x} = 1 \implies \tan x = 1 \implies x = 45^\circ$.
4. Substitute $x = 45^\circ$ into the original function: $y = \sin 45^\circ + \cos 45^\circ$.
5. Evaluate using standard angles: $y = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2}$.

**10. At what point does the curve $y = x^3 - 12x$ have a local minimum?**

- A. $(2, -16)$
- B. $(-2, 16)$
- C. $(2, 16)$
- D. $(-2, -16)$

**Answer: A.**
1. Find the first derivative: $\frac{dy}{dx} = 3x^2 - 12 = 0$.
2. Solve for $x$: $3x^2 = 12 \implies x^2 = 4 \implies x = 2$ or $x = -2$.
3. Find the second derivative to test the nature: $\frac{d^2y}{dx^2} = 6x$.
4. For a local minimum, the second derivative must be positive. At $x = 2$, $6(2) = 12$ (positive, so it is a minimum).
5. Find the corresponding $y$-coordinate when $x = 2$: $y = 2^3 - 12(2) = 8 - 24 = -16$. The point is $(2, -16)$.
