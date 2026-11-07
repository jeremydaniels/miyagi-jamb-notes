# JAMB Mathematics Notes: Inequalities

## What JAMB expects

This topic is Section II, Topic 3 of the JAMB Mathematics syllabus: Inequalities. It has two content items:

* a. analytical and graphical solutions of linear inequalities;
* b. quadratic inequalities with integral roots only.

By the end of these notes, you should be able to:

1. solve problems on linear and quadratic inequalities;
2. interpret graphs of inequalities.

## Analytical and graphical solutions of linear inequalities

An inequality is a mathematical statement that compares two expressions that are not necessarily equal. We use the following symbols:

| Symbol | Meaning | Number Line Symbol | Boundary Line on Graph |
| --- | --- | --- | --- |
| $<$ | Less than | Open circle ($\circ$) | Dashed (broken) line |
| $\le$ | Less than or equal to | Closed circle ($\bullet$) | Solid line |
| $>$ | Greater than | Open circle ($\circ$) | Dashed (broken) line |
| $\ge$ | Greater than or equal to | Closed circle ($\bullet$) | Solid line |

### Analytical solutions

Solving a linear inequality analytically is very similar to solving a linear equation, with one **crucial difference**: 

* **Rule of flipping:** Whenever you multiply or divide both sides of an inequality by a **negative number**, you must flip the inequality sign (e.g., $<$ becomes $>$, and $\ge$ becomes $\le$). Adding or subtracting does not change the sign. Multiplying or dividing by a positive number does not change the sign.

**Example 1: Analytical solution of a linear inequality**
Solve $3x - 5 < 7$.

1. Add $5$ to both sides: $3x < 7 + 5$
2. $3x < 12$
3. Divide both sides by $3$ (a positive number, so the sign stays the same):
4. $x < 4$

### Graphical solutions on a number line

A single linear inequality with one variable (like $x \ge -2$) is often represented on a number line. 

**Example 2: Number line graph**
Graph $x \ge -2$ on a number line.

1. Locate $-2$ on the number line.
2. Draw a **closed circle** ($\bullet$) at $-2$ because the symbol is $\ge$ (it includes "equal to").
3. Draw a thick line or an arrow pointing to the right, covering all numbers greater than $-2$.

[IMAGE: A horizontal number line with a shaded closed circle at -2 and a thick line with an arrow pointing to the right. Labels to add later: "-3, -2, -1, 0, 1", "x >= -2". Clean flat textbook style, white background.]

### Graphical solutions on a Cartesian plane (x-y plane)

An inequality with two variables (like $y > 2x + 1$) is represented on a Cartesian plane. It defines a whole region.

**Example 3: Cartesian graph**
Find the graphical solution for $y > 2x + 1$.

1. **Find the boundary line:** Treat it as an equation: $y = 2x + 1$. Find two points. If $x=0$, $y=1$ (point $0,1$). If $y=0$, $x=-0.5$ (point $-0.5,0$).
2. **Draw the line:** Because the symbol is $>$, draw a **dashed line** through these points.
3. **Determine the region:** Pick a test point not on the line, usually $(0,0)$. Substitute $x=0, y=0$ into $y > 2x + 1$.
   $0 > 2(0) + 1 \Rightarrow 0 > 1$. This is **false**. Therefore, the origin is not in the required region.
4. **Shade:** The required region is the side of the line that does not contain $(0,0)$. 

**Textbook variation on shading:** In some mathematics textbooks, the required (true) region is shaded. However, in WAEC and JAMB, it is common to shade the **unwanted (false) region** so that the required region is left completely clear and unshaded. This is especially useful when graphing multiple inequalities. Always read the exam question carefully! In these notes, unless stated otherwise, we assume the unshaded region is the required region.

[IMAGE: Cartesian plane showing a dashed straight line passing through (0, 1) and (-0.5, 0). The region below the line (containing the origin) is shaded with light grey diagonal lines. The region above the line is clear and unshaded. Labels to add later: "y", "x", "y = 2x + 1", "Unwanted region (shaded)", "Required region: y > 2x + 1". Clean flat textbook style, white background.]

## Quadratic inequalities with integral roots

A quadratic inequality contains an $x^2$ term, such as $x^2 - 5x + 6 > 0$. The JAMB syllabus specifies **integral roots only**, which means the quadratic equation $x^2 - 5x + 6 = 0$ will have whole number solutions (integers), and you can easily solve it by factorising. You will not need the quadratic formula.

### How to solve quadratic inequalities analytically

**Never** solve a quadratic inequality by just writing $x > a$ and $x > b$. This is a massive mistake. You must find the critical values and then determine the correct region using a quick sketch or test points.

**Example 4: Using a parabola sketch**
Solve $x^2 - 5x + 6 > 0$.

1. **Factorise:** Find two numbers that multiply to $+6$ and add to $-5$. They are $-2$ and $-3$.
   $(x - 2)(x - 3) > 0$.
2. **Find the roots:** The roots (critical values) are $x = 2$ and $x = 3$.
3. **Sketch the parabola:** Because the coefficient of $x^2$ is positive ($+1$), the parabola is U-shaped. It crosses the x-axis at $2$ and $3$.
4. **Find the range:** We want the expression to be $> 0$. This means we want the parts of the curve that are **above** the x-axis. Looking at a U-shape, the curve goes above the x-axis on the outside of the roots.
5. **Answer:** $x < 2$ or $x > 3$.

[IMAGE: U-shaped parabola on a Cartesian plane crossing the horizontal x-axis at 2 and 3. The sections of the parabola that rise above the x-axis on the left and right are drawn with a thick solid line. Labels to add later: "x", "2", "3", "y = x^2 - 5x + 6", "+", "+". Clean flat textbook style, white background.]

**Example 5: Using the number line test**
Solve $8 - 2x - x^2 \le 0$.

1. **Make $x^2$ positive:** Multiply the entire inequality by $-1$. Remember to **flip the sign**!
   $x^2 + 2x - 8 \ge 0$.
2. **Factorise:** $(x + 4)(x - 2) \ge 0$.
3. **Find the roots:** $x = -4$ and $x = 2$.
4. **Number line test:** These roots divide the number line into three regions: $x \le -4$, $-4 \le x \le 2$, and $x \ge 2$. Pick a test point in each.
   * Test $x = -5$: $(-5+4)(-5-2) = (-1)(-7) = 7 \ge 0$. (True)
   * Test $x = 0$: $(0+4)(0-2) = (4)(-2) = -8 \ge 0$. (False)
   * Test $x = 3$: $(3+4)(3-2) = (7)(1) = 7 \ge 0$. (True)
5. **Answer:** The true regions are on the outside. So, $x \le -4$ or $x \ge 2$.

## Solving problems on linear and quadratic inequalities

Now we apply these rules to solve more complex JAMB-style problems.

**Example 6: Fractional linear inequality**
Solve $\frac{x-3}{2} - \frac{2x-1}{3} > 1$.

1. To remove the fractions, multiply every term by the Lowest Common Multiple (LCM) of $2$ and $3$, which is $6$.
   $6 \left( \frac{x-3}{2} \right) - 6 \left( \frac{2x-1}{3} \right) > 6(1)$
2. Simplify the multipliers:
   $3(x - 3) - 2(2x - 1) > 6$
3. Expand the brackets carefully (watch the signs!):
   $3x - 9 - 4x + 2 > 6$
4. Collect like terms:
   $-x - 7 > 6$
5. Move $-7$ to the other side:
   $-x > 13$
6. Multiply by $-1$ and **flip the sign**:
   $x < -13$.

**Example 7: Compound linear inequality**
Solve $3x - 2 \le x + 4 < 2x + 5$.

A compound inequality has three parts. Split it into two separate inequalities, solve them independently, and combine the answers.

1. **First part:** $3x - 2 \le x + 4$
   $3x - x \le 4 + 2 \Rightarrow 2x \le 6 \Rightarrow x \le 3$.
2. **Second part:** $x + 4 < 2x + 5$
   $x - 2x < 5 - 4 \Rightarrow -x < 1$. Multiply by $-1$ and flip: $x > -1$.
3. **Combine:** We need $x \le 3$ AND $x > -1$. This means $x$ is between $-1$ and $3$. We write this as:
   $-1 < x \le 3$.

**Example 8: Word problem**
A school bus charges ₦500 per student for a trip to the National Museum in Lagos. The cost to rent the bus is ₦12,000. How many students must go on the trip for the school to make a profit of at least ₦3,000?

1. Let $n$ be the number of students.
2. Revenue from students = $500n$.
3. Profit = Revenue $-$ Cost = $500n - 12000$.
4. The profit must be "at least" (which means $\ge$) ₦3,000:
   $500n - 12000 \ge 3000$
5. Solve for $n$:
   $500n \ge 15000 \Rightarrow n \ge 30$.
6. **Answer:** At least 30 students must go on the trip.

**Example 9: Special quadratic inequality**
Solve $(x-1)^2 > 4$.

1. Expand or move the 4. Let's move the 4: $(x-1)^2 - 4 > 0$.
2. This is a difference of two squares: $a^2 - b^2 = (a-b)(a+b)$.
   $((x-1) - 2)((x-1) + 2) > 0$
3. $(x - 3)(x + 1) > 0$.
4. Roots are $3$ and $-1$.
5. The parabola is U-shaped and we want $> 0$ (above the x-axis, outside regions).
6. **Answer:** $x < -1$ or $x > 3$.

## Interpreting graphs of inequalities

JAMB frequently tests your ability to look at a shaded graph and deduce the inequality. 

### Steps for interpreting graphs

1. **Find the equation of the line:** Identify two points where the line crosses the grid clearly and find the gradient ($m$) and y-intercept ($c$). 
2. **Check the line type:** If it is solid, the inequality contains $=$ ($\le$ or $\ge$). If it is dashed, it is strictly $<$ or $>$.
3. **Use a test point:** Pick a point clearly inside the required (unshaded) region and plug it into your equation to see whether it evaluates to less than or greater than.

**Example 10: Single linear graph**
A required (unshaded) region is bounded by a solid line passing through $(0, -2)$ and $(2, 0)$. The point $(2, 1)$ is inside the required region. Find the inequality.

1. **Equation:** Gradient $m = \frac{0 - (-2)}{2 - 0} = \frac{2}{2} = 1$. The y-intercept is $-2$. So, $y = x - 2$.
2. **Line type:** It is solid, so we will use $\le$ or $\ge$.
3. **Test point:** The point $(2, 1)$ is in the required region. Substitute $x=2, y=1$ into the relationship between $y$ and $x-2$.
   $y = 1$ and $x - 2 = 2 - 2 = 0$.
   Since $1 > 0$, we have $y > x - 2$.
4. **Combine:** Because the line is solid, the final inequality is $y \ge x - 2$.

**Example 11: A system of linear inequalities**
A required (unshaded) region on a Cartesian plane is a triangle in the first quadrant bounded by the y-axis, the x-axis, and a dashed line passing through $(0, 4)$ and $(4, 0)$. Define the region.

1. **First two lines:** Bounded by the positive axes means $x \ge 0$ and $y \ge 0$.
2. **Third line equation:** Gradient $m = \frac{0 - 4}{4 - 0} = -1$. The y-intercept is $4$. Equation: $y = -x + 4$, which rearranges to $x + y = 4$.
3. **Third line type:** It is dashed, so we use $<$ or $>$.
4. **Test point:** The region is a triangle near the origin, so $(1, 1)$ is inside it. 
   $x + y = 1 + 1 = 2$.
   Since $2 < 4$, the inequality is $x + y < 4$.
5. **Answer:** The region is defined by $x \ge 0$, $y \ge 0$, $x + y < 4$.

[IMAGE: Cartesian plane showing the first quadrant. A dashed straight line passes through (0, 4) and (4, 0). The triangle formed by the x-axis, y-axis, and the dashed line is clear (unshaded), while the regions outside this triangle are shaded with light grey diagonal lines. Labels to add later: "y", "x", "4" on y-axis, "4" on x-axis, "x + y = 4", "Required region R". Clean flat textbook style, white background.]

**Example 12: Interpreting a quadratic inequality graph**
The graph shows a parabola crossing the x-axis at $x = -2$ and $x = 4$. It is a U-shape (opens upwards). The required region is marked above the x-axis. Find the inequality.

1. **Find the roots:** The roots are $x = -2$ and $x = 4$. 
2. **Build the equation:** Working backwards from the roots, the factors must be $(x+2)$ and $(x-4)$. 
   $(x+2)(x-4) = x^2 - 2x - 8 = 0$.
3. **Check orientation:** Since it is U-shaped, the coefficient of $x^2$ is positive, so $y = x^2 - 2x - 8$.
4. **Determine sign:** The required region is above the x-axis, meaning $y > 0$.
5. **Answer:** The inequality is $x^2 - 2x - 8 > 0$.

## Key terms

| Term | Meaning |
| --- | --- |
| Inequality | A mathematical statement showing that two expressions are not necessarily equal (using $<, >, \le, \ge$) |
| Boundary line | The straight line on a Cartesian graph that separates the required region from the unwanted region |
| Solid line | Used for $\le$ or $\ge$, meaning points on the line are included in the solution |
| Dashed line | Used for $<$ or $>$, meaning points on the line are not included |
| Test point | A coordinate (like $(0,0)$) plugged into an inequality to check which side of a boundary line is true |
| Quadratic inequality | An inequality containing an $x^2$ term (e.g., $x^2 + 5x + 6 > 0$) |
| Integral roots | Solutions to an equation that are whole numbers (e.g., $x=2$ or $x=-3$), meaning the expression can be easily factorised |
| Compound inequality | Two inequalities combined into one continuous statement (e.g., $-2 < x \le 5$) |

## Exam tips and common mistakes

* **Sign flipping:** The most common mistake in linear inequalities is forgetting to flip the inequality sign when multiplying or dividing by a negative number. Always remember: if $-2x < 8$, then $x > -4$.
* **Cross-multiplying fractions:** Be very careful when cross-multiplying inequalities with fractions. It is safer to multiply all terms by the Lowest Common Multiple (LCM) of the denominators to avoid accidentally multiplying by a hidden negative.
* **Quadratic mistakes:** Never solve a quadratic inequality like a linear one. If $(x - 2)(x - 5) > 0$, it is **wrong** to say $x > 2$ and $x > 5$. You must sketch the curve or use a number line to find the correct outside regions: $x < 2$ or $x > 5$.
* **Graph shading conventions:** Textbooks vary. Some shade the required region, but most WAEC and JAMB past questions shade the *unwanted* region to leave the required region clean (especially for systems of inequalities). Read the question carefully to know which region is required!
* **Solid vs dashed lines:** Always check if a line is solid (includes $=$) or dashed (strict inequality). This can help you eliminate wrong options instantly in multiple-choice questions.

## Quick summary

1. Inequalities are solved much like normal equations, but the inequality sign must flip ($<$ becomes $>$, etc.) when you multiply or divide both sides by a negative number.
2. A single inequality can be represented on a number line using open circles ($\circ$) for $<$ and $>$ and closed circles ($\bullet$) for $\le$ and $\ge$.
3. On a Cartesian graph, inequalities define whole regions. You draw the boundary line (dashed or solid) and use a test point like $(0,0)$ to decide which side is true.
4. When interpreting graphs, find the equation of the boundary line using two points, check if it is solid or dashed, and use a test point in the required region to find the correct inequality sign.
5. Quadratic inequalities with integral roots can be solved analytically by factorising to find the roots (critical values).
6. To find the true region for a quadratic inequality, sketch the U-shaped or n-shaped parabola, or test points on a number line. A "$< 0$" for a positive U-shaped parabola always means the region *between* the roots.
7. Compound inequalities (like $a < x \le b$) should be split into two separate inequalities, solved independently, and then combined back together by finding where their solutions overlap.

## Practice questions

**1. Solve the inequality $2x - 3 \le 5x + 9$.**

- A. $x \ge -4$
- B. $x \le -4$
- C. $x \ge 4$
- D. $x \le 4$

**Answer: A.** 
1. Move the $x$ terms to one side and constants to the other: $2x - 5x \le 9 + 3$.
2. Simplify: $-3x \le 12$.
3. Divide by $-3$ and **flip the sign**: $x \ge -4$. (Option B is the trap for forgetting to flip the sign).

**2. Solve $\frac{1}{2}(3x - 2) < \frac{1}{3}(x + 4)$.**

- A. $x > 2$
- B. $x < 2$
- C. $x < \frac{14}{5}$
- D. $x > \frac{14}{5}$

**Answer: B.** 
1. Multiply the entire inequality by the LCM of the denominators, which is 6: $6 \times \frac{1}{2}(3x - 2) < 6 \times \frac{1}{3}(x + 4)$.
2. $3(3x - 2) < 2(x + 4)$.
3. Expand: $9x - 6 < 2x + 8$.
4. Collect like terms: $9x - 2x < 8 + 6 \Rightarrow 7x < 14$.
5. Divide by 7: $x < 2$.

**3. Find the range of values of $x$ for which $3 - 2x \le 7$ and $4x - 1 < 11$.**

- A. $-2 < x \le 3$
- B. $-2 \le x < 3$
- C. $-3 < x \le 2$
- D. $x \ge -2 \text{ or } x < 3$

**Answer: B.** 
1. Solve the first inequality: $3 - 2x \le 7 \Rightarrow -2x \le 4 \Rightarrow x \ge -2$.
2. Solve the second inequality: $4x - 1 < 11 \Rightarrow 4x < 12 \Rightarrow x < 3$.
3. Combine the two conditions: $x$ must be greater than or equal to $-2$ AND less than $3$.
4. The combined range is $-2 \le x < 3$.

**4. Solve the inequality $x^2 - 7x + 10 \le 0$.**

- A. $x \le 2 \text{ or } x \ge 5$
- B. $2 \le x \le 5$
- C. $-5 \le x \le -2$
- D. $x \le -5 \text{ or } x \ge -2$

**Answer: B.** 
1. Factorise the quadratic expression: $(x - 2)(x - 5) \le 0$.
2. The roots are $x = 2$ and $x = 5$.
3. Sketching the U-shaped parabola, we want the region $\le 0$ (below the x-axis).
4. This occurs between the roots: $2 \le x \le 5$.

**5. Find the range of values of $x$ which satisfies $15 - 2x - x^2 \ge 0$.**

- A. $x \le -5 \text{ or } x \ge 3$
- B. $-3 \le x \le 5$
- C. $-5 \le x \le 3$
- D. $x \le -3 \text{ or } x \ge 5$

**Answer: C.** 
1. Multiply the inequality by $-1$ to make the $x^2$ positive, and remember to flip the sign: $x^2 + 2x - 15 \le 0$.
2. Factorise: $(x + 5)(x - 3) \le 0$.
3. The roots are $x = -5$ and $x = 3$.
4. We want the region $\le 0$, which is between the roots. 
5. Result: $-5 \le x \le 3$.

**6. The integer values of $x$ that satisfy the inequality $-1 < 2x - 3 \le 5$ are:**

- A. 1, 2, 3, 4
- B. 2, 3, 4
- C. 1, 2, 3
- D. 2, 3, 4, 5

**Answer: B.** 
1. Add 3 to all parts of the compound inequality: $-1 + 3 < 2x \le 5 + 3 \Rightarrow 2 < 2x \le 8$.
2. Divide all parts by 2: $1 < x \le 4$.
3. The inequality says $x$ is strictly greater than 1, but less than or equal to 4. 
4. The integers in this range are 2, 3, and 4.

**7. A required (unshaded) region on a Cartesian plane is bounded by a solid line passing through $(0, 2)$ and $(-2, 0)$, and a dashed line passing through $(0, 4)$ and $(2, 0)$. If the origin $(0,0)$ is inside this required region, which system of inequalities defines it?**

- A. $y - x \le 2$ and $y + 2x < 4$
- B. $y - x \ge 2$ and $y + 2x < 4$
- C. $y - x \le 2$ and $y + 2x > 4$
- D. $y - x < 2$ and $y + 2x \le 4$

**Answer: A.** 
1. First line passes through $(0, 2)$ and $(-2, 0)$. Gradient $m = 1$. Equation is $y = x + 2$, or $y - x = 2$. It is solid, and origin $(0,0)$ is inside. Substitute $(0,0)$ into $y - x$: $0 - 0 = 0$. Since $0 \le 2$, the inequality is $y - x \le 2$.
2. Second line passes through $(0, 4)$ and $(2, 0)$. Gradient $m = -2$. Equation is $y = -2x + 4$, or $y + 2x = 4$. It is dashed, and origin $(0,0)$ is inside. Substitute $(0,0)$ into $y + 2x$: $0 + 0 = 0$. Since $0 < 4$, the inequality is $y + 2x < 4$.
3. The system is $y - x \le 2$ and $y + 2x < 4$.

**8. Solve the inequality $x^2 - 9 > 0$.**

- A. $-3 < x < 3$
- B. $x < -3 \text{ or } x > 3$
- C. $-3 \le x \le 3$
- D. $x \le -3 \text{ or } x \ge 3$

**Answer: B.** 
1. Recognize this as a difference of two squares and factorise: $(x - 3)(x + 3) > 0$.
2. The roots are $x = 3$ and $x = -3$.
3. The parabola is U-shaped and we want $> 0$ (above the x-axis). This happens on the outside edges, away from the roots.
4. Result: $x < -3 \text{ or } x > 3$.

**9. A student has ₦1,200 to spend on pens and pencils. A pen costs ₦150 and a pencil costs ₦50. If he must buy exactly 4 pens, what is the maximum number of pencils he can buy?**

- A. 12
- B. 10
- C. 14
- D. 8

**Answer: A.** 
1. Cost of exactly 4 pens = $4 \times 150 = 600$ naira.
2. Let the number of pencils be $x$. Cost of pencils = $50x$.
3. Total cost must be less than or equal to total money: $600 + 50x \le 1200$.
4. $50x \le 1200 - 600 \Rightarrow 50x \le 600$.
5. Divide by 50: $x \le 12$. The maximum number of pencils is 12.

**10. The graph of a quadratic inequality is a U-shaped parabola that crosses the x-axis at $x = -1$ and $x = 4$. The required region is marked below the x-axis. What is the inequality?**

- A. $x^2 - 3x - 4 > 0$
- B. $x^2 - 3x - 4 \le 0$
- C. $x^2 - 3x - 4 < 0$
- D. $x^2 + 3x - 4 < 0$

**Answer: C.** 
1. The roots are $x = -1$ and $x = 4$. Working backwards, the factors are $(x+1)$ and $(x-4)$.
2. Multiply the factors to get the equation: $(x+1)(x-4) = x^2 - 4x + x - 4 = x^2 - 3x - 4 = 0$.
3. The curve is U-shaped, so the $x^2$ coefficient is positive (which matches $x^2 - 3x - 4$).
4. The required region is below the x-axis, meaning strictly less than zero (no solid boundary lines mentioned).
5. The inequality is $x^2 - 3x - 4 < 0$.
