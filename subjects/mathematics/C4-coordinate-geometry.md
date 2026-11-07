# JAMB Mathematics Notes: Coordinate Geometry

## What JAMB expects

This topic is Section III, Topic 4 of the JAMB Mathematics syllabus: Geometry and Trigonometry – Coordinate Geometry. It covers how to analyse straight lines and points on a grid mathematically.

The syllabus covers four content items:
- **a.** midpoint and gradient of a line segment;
- **b.** distance between two points;
- **c.** parallel and perpendicular lines;
- **d.** equations of straight lines.

By the end of these notes, you should be able to:
1. determine the midpoint and gradient of a line segment;
2. find the distance between two points;
3. identify conditions for parallelism and perpendicularity;
4. find the equation of a line in the two-point form, point-slope form, slope intercept form and the general form.

Coordinate geometry (also known as analytic geometry) links algebra with geometry using the Cartesian coordinate system. Every point on the plane is defined by an $(x, y)$ coordinate pair. 

---

## Midpoint and gradient of a line segment

This section explains how to locate the exact middle of a line segment and how to measure its steepness. 

### The midpoint of a line segment
The **midpoint** is the point that divides a line segment into two equal halves. To find it, you simply calculate the average of the $x$-coordinates and the average of the $y$-coordinates of the two endpoints.

For any two points $A(x_1, y_1)$ and $B(x_2, y_2)$, the coordinates of the midpoint $M(x, y)$ are given by the formula:
$$M(x, y) = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$$

[IMAGE: A Cartesian coordinate plane showing a line segment connecting point A(-3, 6) and point B(5, -2). The midpoint M(1, 2) is clearly marked with a distinct dot. The axes should have grid lines and labels. Clean flat textbook illustration, white background.]

**Worked Example 1: Finding the midpoint**
Find the midpoint of the line segment joining the points $A(-3, 6)$ and $B(5, -2)$.
1. Identify the given coordinates: $x_1 = -3$, $y_1 = 6$, $x_2 = 5$, $y_2 = -2$.
2. Apply the midpoint formula for the $x$-coordinate: $x = \frac{-3 + 5}{2} = \frac{2}{2} = 1$.
3. Apply the formula for the $y$-coordinate: $y = \frac{6 + (-2)}{2} = \frac{4}{2} = 2$.
4. The midpoint is $M(1, 2)$.

**Worked Example 2: Finding an unknown endpoint**
The midpoint of a line segment is $M(4, -1)$. If one endpoint is $P(1, 5)$, find the coordinates of the other endpoint $Q(x, y)$.
1. Set up the midpoint formula for the $x$-coordinate: $\frac{1 + x}{2} = 4$.
2. Multiply both sides by 2: $1 + x = 8$.
3. Solve for $x$: $x = 7$.
4. Set up the midpoint formula for the $y$-coordinate: $\frac{5 + y}{2} = -1$.
5. Multiply both sides by 2: $5 + y = -2$.
6. Solve for $y$: $y = -7$.
7. The other endpoint is $Q(7, -7)$.

> **Common Mistake:** Students often subtract the coordinates instead of adding them when finding the midpoint. Always remember that a midpoint is an **average**, which requires addition!

### The gradient (slope) of a line segment
The **gradient** (usually denoted by the letter $m$) measures the steepness and direction of a straight line. It is defined as the ratio of the vertical change ("rise") to the horizontal change ("run") between any two points on the line.

For any two points $A(x_1, y_1)$ and $B(x_2, y_2)$, the gradient formula is:
$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$
where $\Delta y$ means "change in $y$" and $\Delta x$ means "change in $x$".

**Understanding gradient values:**
- A **positive gradient** means the line goes up from left to right.
- A **negative gradient** means the line goes down from left to right.
- A **zero gradient** means the line is completely horizontal.
- An **undefined gradient** means the line is completely vertical (because the change in $x$ is 0, and you cannot divide by zero).

[IMAGE: A diagram illustrating the concept of gradient (slope). A line passes through two points on a grid. A right-angled triangle is drawn below the line connecting the two points, showing a vertical "Rise" (\Delta y) and a horizontal "Run" (\Delta x). The line has a positive slope. Clean flat textbook style, white background.]

**Worked Example 3: Finding the gradient**
Find the gradient of the line passing through the points $C(-2, -4)$ and $D(3, 6)$.
1. Identify the given coordinates: $x_1 = -2, y_1 = -4$ and $x_2 = 3, y_2 = 6$.
2. Substitute into the gradient formula: $m = \frac{6 - (-4)}{3 - (-2)}$.
3. Simplify the signs (two negatives make a positive): $m = \frac{6 + 4}{3 + 2}$.
4. Calculate the fraction: $m = \frac{10}{5}$.
5. The gradient is $m = 2$.

**Worked Example 4: Finding an unknown coordinate from a given gradient**
The line joining $A(k, 3)$ and $B(4, 9)$ has a gradient of $2$. Find the value of $k$.
1. Substitute the known values into the gradient formula: $2 = \frac{9 - 3}{4 - k}$.
2. Simplify the numerator: $2 = \frac{6}{4 - k}$.
3. Cross-multiply to eliminate the fraction: $2(4 - k) = 6$.
4. Divide both sides by 2: $4 - k = 3$.
5. Rearrange to solve for $k$: $k = 4 - 3 = 1$.
6. The value of $k$ is $1$.

## Distance between two points

The distance $d$ between any two points on a Cartesian plane is found using an application of Pythagoras' theorem. If you draw a right-angled triangle between two points, the horizontal distance is $\Delta x$ and the vertical distance is $\Delta y$. The line segment between the points is the hypotenuse.

The distance formula between points $A(x_1, y_1)$ and $B(x_2, y_2)$ is:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Worked Example 5: Simple distance calculation**
Find the distance between the point $P(3, 4)$ and the origin $(0, 0)$.
1. Identify the coordinates: $x_1 = 0, y_1 = 0$ and $x_2 = 3, y_2 = 4$.
2. Apply the distance formula: $d = \sqrt{(3 - 0)^2 + (4 - 0)^2}$.
3. Simplify inside the brackets: $d = \sqrt{3^2 + 4^2}$.
4. Square the numbers: $d = \sqrt{9 + 16} = \sqrt{25}$.
5. The distance is $5$ units.

**Worked Example 6: Distance with negative coordinates**
Calculate the distance between $A(-1, 5)$ and $B(4, -7)$.
1. Identify the coordinates: $x_1 = -1, y_1 = 5$ and $x_2 = 4, y_2 = -7$.
2. Apply the formula: $d = \sqrt{(4 - (-1))^2 + (-7 - 5)^2}$.
3. Simplify the brackets carefully: $d = \sqrt{(5)^2 + (-12)^2}$.
4. Square the numbers (remember a negative squared is positive): $d = \sqrt{25 + 144}$.
5. Add the values: $d = \sqrt{169}$.
6. The distance is $13$ units.

**Worked Example 7: Finding a missing coordinate given the distance**
The distance between the points $X(2, y)$ and $Y(5, 1)$ is $5$ units. Find the possible values of $y$.
1. Set up the distance formula: $5 = \sqrt{(5 - 2)^2 + (1 - y)^2}$.
2. Square both sides to remove the square root: $25 = (3)^2 + (1 - y)^2$.
3. Simplify the squared number: $25 = 9 + (1 - y)^2$.
4. Subtract 9 from both sides: $16 = (1 - y)^2$.
5. Take the square root of both sides (remember to include $\pm$): $\pm 4 = 1 - y$.
6. Solve for the two possible cases:
   - Case 1: $1 - y = 4 \implies y = -3$.
   - Case 2: $1 - y = -4 \implies y = 5$.
7. The possible values are $y = -3$ or $y = 5$.

> **Common Mistake:** Forgetting to take the square root at the very end of the distance formula. If you calculate $d^2 = 100$, make sure to state that $d = 10$. Also, ensure you square the differences **before** you add them. You cannot simplify $\sqrt{a^2 + b^2}$ into $a + b$.

## Parallel and perpendicular lines

We can use gradients to determine if two lines will never meet (parallel) or if they meet at exactly $90^\circ$ (perpendicular).

### 1. Conditions for parallel lines
Two straight lines are **parallel** if they have exactly the same steepness and direction. Therefore, their gradients must be equal.
If a line $L_1$ has gradient $m_1$ and a line $L_2$ has gradient $m_2$, they are parallel if:
$$m_1 = m_2$$

### 2. Conditions for perpendicular lines
Two straight lines are **perpendicular** if they intersect at a right angle ($90^\circ$). In this case, their gradients are negative reciprocals of one another.
The condition for perpendicularity is:
$$m_1 \times m_2 = -1 \quad \text{or} \quad m_1 = -\frac{1}{m_2}$$
*Note: This rule does not apply if one line is horizontal ($m=0$) and the other is vertical (undefined gradient), though they are still perpendicular.*

[IMAGE: Two sets of intersecting lines on a coordinate plane. On the left, two parallel lines with positive gradients, labelled L_1 and L_2, with small arrows indicating they are parallel. On the right, two lines intersecting at exactly 90 degrees, marked with a small square right-angle symbol, labelled L_3 and L_4. Clean flat textbook style, white background.]

### 3. Collinear points
Points are **collinear** if they lie on the exact same straight line. To prove that three points $A$, $B$, and $C$ are collinear, you must show that the gradient between $A$ and $B$ is the same as the gradient between $B$ and $C$.
$$m_{AB} = m_{BC}$$

**Worked Example 8: Checking perpendicularity**
Determine whether the line passing through $A(2, 4)$ and $B(4, 8)$ is perpendicular to the line passing through $C(1, -2)$ and $D(5, -4)$.
1. Find the gradient of line $AB$: $m_1 = \frac{8 - 4}{4 - 2} = \frac{4}{2} = 2$.
2. Find the gradient of line $CD$: $m_2 = \frac{-4 - (-2)}{5 - 1} = \frac{-2}{4} = -\frac{1}{2}$.
3. Check the product of the gradients: $m_1 \times m_2 = 2 \times \left(-\frac{1}{2}\right) = -1$.
4. Since the product is $-1$, the lines are indeed perpendicular.

**Worked Example 9: Finding an unknown using parallel lines**
Line $L_1$ has a gradient of $\frac{2}{3}$. Line $L_2$ passes through the points $(1, 3)$ and $(4, k)$ and is parallel to $L_1$. Find $k$.
1. Because the lines are parallel, $m_2 = m_1 = \frac{2}{3}$.
2. Write the gradient formula for $L_2$: $m_2 = \frac{k - 3}{4 - 1} = \frac{k - 3}{3}$.
3. Equate the two gradients: $\frac{k - 3}{3} = \frac{2}{3}$.
4. Since the denominators are the same, the numerators must be equal: $k - 3 = 2$.
5. Solve for $k$: $k = 5$.

**Worked Example 10: Collinear points**
Show that the points $P(-1, -4)$, $Q(1, 0)$, and $R(3, 4)$ are collinear.
1. Find the gradient of the line segment $PQ$: $m_{PQ} = \frac{0 - (-4)}{1 - (-1)} = \frac{4}{2} = 2$.
2. Find the gradient of the line segment $QR$: $m_{QR} = \frac{4 - 0}{3 - 1} = \frac{4}{2} = 2$.
3. Since $m_{PQ} = m_{QR}$ and they share the common point $Q$, all three points lie on the same straight line (they are collinear).

## Equations of straight lines

An equation of a straight line gives the mathematical relationship between the $x$ and $y$ coordinates of every point on that line. JAMB requires you to know and convert between four specific forms.

### 1. Slope-intercept form ($y = mx + c$)
This is the most common form used for graphing and finding the gradient.
- $m$ is the **gradient** (slope).
- $c$ is the **$y$-intercept** (the point where the line crosses the vertical $y$-axis, i.e., when $x = 0$).

**Worked Example 11:** Find the equation of a line with a gradient of $-3$ and a $y$-intercept of $5$.
1. Identify the given values: $m = -3$, $c = 5$.
2. Substitute them directly into $y = mx + c$.
3. The equation is $y = -3x + 5$.

### 2. Point-slope form ($y - y_1 = m(x - x_1)$)
Use this form when you know the gradient ($m$) and any single point $(x_1, y_1)$ on the line.

**Worked Example 12:** Find the equation of the line passing through $(-2, 4)$ with a gradient of $\frac{1}{2}$.
1. Identify the given values: $x_1 = -2, y_1 = 4$, and $m = \frac{1}{2}$.
2. Apply the point-slope form: $y - 4 = \frac{1}{2}(x - (-2))$.
3. Simplify the bracket: $y - 4 = \frac{1}{2}(x + 2)$.
4. Multiply through by 2 to remove the fraction: $2(y - 4) = 1(x + 2)$.
5. Expand: $2y - 8 = x + 2$.
6. Rearrange all terms to one side: $x - 2y + 10 = 0$.

### 3. Two-point form ($\frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}$)
Use this form when you are given exactly two points and no gradient. The right side of the formula is simply calculating the gradient $m$, meaning this is just a variation of the point-slope form.

**Worked Example 13:** Find the equation of the line passing through the points $(1, -3)$ and $(4, 6)$.
1. First, find the gradient $m$: $m = \frac{6 - (-3)}{4 - 1} = \frac{9}{3} = 3$.
2. Now, use the point-slope form with the first point $(1, -3)$: $y - (-3) = 3(x - 1)$.
3. Simplify and expand: $y + 3 = 3x - 3$.
4. Rearrange all terms to one side: $3x - y - 6 = 0$.

### 4. General form ($Ax + By + C = 0$)
In this form, $A$, $B$, and $C$ are usually integers. This is the standard way options are presented in JAMB exams. To extract the gradient and $y$-intercept from the general form, you must rearrange it back into the slope-intercept form ($y = mx + c$).

**Worked Example 14:** Find the gradient and $y$-intercept of the line $2x + 5y - 10 = 0$.
1. Isolate the $y$-term on one side: $5y = -2x + 10$.
2. Divide every term by 5 to get $y$ by itself: $y = -\frac{2}{5}x + 2$.
3. Compare this to $y = mx + c$.
4. The gradient is $m = -\frac{2}{5}$ and the $y$-intercept is $c = 2$.

**Worked Example 15:** Find the equation of the line passing through $(3, 2)$ which is perpendicular to the line $3x - 2y + 6 = 0$.
1. First, find the gradient of the given line. Rearrange $3x - 2y + 6 = 0$ to get $y$ by itself: $2y = 3x + 6 \implies y = \frac{3}{2}x + 3$.
2. The gradient of the original line is $m_1 = \frac{3}{2}$.
3. Because the new line is perpendicular, its gradient $m_2$ is the negative reciprocal: $m_2 = -\frac{2}{3}$.
4. Use the point-slope form with the new gradient and point $(3, 2)$: $y - 2 = -\frac{2}{3}(x - 3)$.
5. Multiply through by 3 to clear the fraction: $3(y - 2) = -2(x - 3)$.
6. Expand both sides: $3y - 6 = -2x + 6$.
7. Rearrange into the general form: $2x + 3y - 12 = 0$.

### JAMB Shortcuts for Parallel and Perpendicular Lines
When you are given an equation in the general form $Ax + By + C = 0$ and asked to find a parallel or perpendicular line passing through a point $(x_1, y_1)$, use these massive time-savers:

- **For a parallel line:** Keep the $x$ and $y$ coefficients exactly the same. The equation is $Ax + By = k$. To find $k$, plug in the coordinates of the given point: $k = A(x_1) + B(y_1)$.
- **For a perpendicular line:** Swap the coefficients of $x$ and $y$, and **change the sign** in the middle. The equation becomes $Bx - Ay = k$. Find $k$ by plugging in the point: $k = B(x_1) - A(y_1)$.

*Let's re-solve Worked Example 15 using the shortcut:*
Find the line perpendicular to $3x - 2y + 6 = 0$ passing through $(3, 2)$.
1. The given line is $3x - 2y + 6 = 0$. Here $A = 3$ and $B = -2$.
2. For a perpendicular line, the shortcut formula is $Bx - Ay = k$.
3. Substitute $A$ and $B$: $-2x - 3y = k$.
4. Substitute the point $(3, 2)$ to find $k$: $k = -2(3) - 3(2) = -6 - 6 = -12$.
5. The equation is $-2x - 3y = -12$.
6. Multiply everything by $-1$ to make it neat: $2x + 3y = 12 \implies 2x + 3y - 12 = 0$. (Matches perfectly, and is much faster!)

## Key terms

| Term | Meaning |
| --- | --- |
| Coordinate Plane | A 2D surface formed by intersecting $x$ (horizontal) and $y$ (vertical) axes, used to plot points. |
| Midpoint | The exact middle point of a line segment, dividing it into two equal parts. |
| Gradient (Slope) | A measure of the steepness and direction of a straight line, calculated as "rise over run". |
| Collinear Points | Three or more points that lie exactly on the same straight line. |
| Parallel Lines | Lines in the same plane that never intersect and have identical gradients. |
| Perpendicular Lines | Lines that intersect at exactly a $90^\circ$ angle; the product of their gradients is $-1$. |
| $y$-intercept | The point where a line crosses the vertical $y$-axis (the value of $y$ when $x = 0$). |
| General Form | The equation of a straight line written as $Ax + By + C = 0$. |

## Exam tips and common mistakes

- **Do not confuse distance and midpoint formulas!** Distance uses subtraction and squaring. Midpoint uses addition and dividing by two.
- **Pay attention to negative signs.** When substituting negative coordinates into formulas that already contain minus signs (like gradient or distance), use brackets. For example, $4 - (-2)$ correctly becomes $4 + 2 = 6$.
- **Perpendicular gradient rule.** If $m_1 = 4$, the perpendicular gradient is $m_2 = -\frac{1}{4}$. Do not just change the sign ($-4$) and do not just flip the fraction ($\frac{1}{4}$)—you must do **both**.
- **Extracting gradients from general equations.** In the equation $3x - 2y + 7 = 0$, the gradient is NOT $3$. You must rearrange it into the form $y = mx + c$ to reveal the true gradient ($m = \frac{3}{2}$).
- **Horizontal and vertical lines.** A horizontal line has a gradient of $0$ and its equation is $y = c$. A vertical line has an undefined gradient and its equation is $x = k$.

## Quick summary

1. The midpoint of a line segment is the average of the coordinates: $M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$.
2. The gradient $m$ measures a line's steepness: $m = \frac{y_2 - y_1}{x_2 - x_1}$.
3. The distance between two points is calculated using Pythagoras' theorem: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
4. Parallel lines have equal gradients ($m_1 = m_2$).
5. Perpendicular lines intersect at $90^\circ$, and their gradients multiply to give $-1$ ($m_1 \times m_2 = -1$).
6. Points are collinear if the gradient calculated between any pair of the points is exactly the same.
7. Equations of lines can be written in slope-intercept form ($y = mx + c$), point-slope form ($y - y_1 = m(x - x_1)$), or general form ($Ax + By + C = 0$).

## Practice questions

**1. Find the distance between the points $P(3, -2)$ and $Q(-5, 4)$.**

- A. $8$
- B. $10$
- C. $14$
- D. $100$

**Answer: B.**
1. Identify the coordinates: $x_1 = 3, y_1 = -2$ and $x_2 = -5, y_2 = 4$.
2. Write the distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
3. Substitute the values: $d = \sqrt{(-5 - 3)^2 + (4 - (-2))^2}$.
4. Simplify inside the brackets: $d = \sqrt{(-8)^2 + (6)^2}$.
5. Square the terms: $d = \sqrt{64 + 36} = \sqrt{100}$.
6. Calculate the final value: $d = 10$.
Option D is incorrect because it stops at $100$ and forgets to take the square root, a common mistake.

**2. The midpoint of a line segment joining $A(x, 5)$ and $B(-2, y)$ is $M(2, 1)$. Find the values of $x$ and $y$.**

- A. $x = 6, y = -3$
- B. $x = 4, y = -3$
- C. $x = 6, y = 3$
- D. $x = 0, y = -1$

**Answer: A.**
1. Use the midpoint formula: $M(x, y) = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$.
2. Equate the $x$-coordinates: $\frac{x - 2}{2} = 2$.
3. Solve for $x$: multiply by $2$ to get $x - 2 = 4$, so $x = 6$.
4. Equate the $y$-coordinates: $\frac{5 + y}{2} = 1$.
5. Solve for $y$: multiply by $2$ to get $5 + y = 2$, so $y = -3$.
Option B is the result of forgetting to multiply by $2$ when solving for $x$ ($x - 2 = 2 \implies x = 4$, instead of $x - 2 = 4$).

**3. Find the gradient of the line passing through the points $(-1, 4)$ and $(2, -5)$.**

- A. $-3$
- B. $-\frac{1}{3}$
- C. $\frac{1}{3}$
- D. $3$

**Answer: A.**
1. Identify the points: $x_1 = -1, y_1 = 4$ and $x_2 = 2, y_2 = -5$.
2. Apply the gradient formula: $m = \frac{y_2 - y_1}{x_2 - x_1}$.
3. Substitute the values: $m = \frac{-5 - 4}{2 - (-1)}$.
4. Simplify the numerator and denominator: $m = \frac{-9}{3}$.
5. Divide to get the final gradient: $m = -3$.
Option D has the right size but the wrong sign. It comes from subtracting in the wrong order: $\frac{y_1 - y_2}{x_2 - x_1} = \frac{9}{3} = 3$.

**4. Find the equation of the line passing through $(2, -3)$ and parallel to the line $3x + y - 5 = 0$.**

- A. $3x + y + 3 = 0$
- B. $3x + y - 3 = 0$
- C. $x - 3y - 11 = 0$
- D. $3x - y - 9 = 0$

**Answer: B.**
1. Using the shortcut for parallel lines, keep the $x$ and $y$ terms the same: $3x + y = k$.
2. Substitute the given point $(2, -3)$ to find $k$: $k = 3(2) + (-3)$.
3. Simplify: $k = 6 - 3 = 3$.
4. The equation is $3x + y = 3$.
5. Rearrange into general form: $3x + y - 3 = 0$.
Alternatively, making $y$ the subject of the original equation gives $m = -3$. Using the point-slope form $y - (-3) = -3(x - 2)$ leads to the same answer. Option D results from confusing the gradient as positive $3$.

**5. If the lines $2y - kx + 4 = 0$ and $y - 4x - 2 = 0$ are perpendicular, find the value of $k$.**

- A. $-\frac{1}{4}$
- B. $-\frac{1}{2}$
- C. $\frac{1}{2}$
- D. $8$

**Answer: B.**
1. Find the gradient of the first line: $2y = kx - 4 \implies y = \frac{k}{2}x - 2$. The gradient $m_1 = \frac{k}{2}$.
2. Find the gradient of the second line: $y = 4x + 2$. The gradient $m_2 = 4$.
3. Since they are perpendicular, their product must be $-1$: $m_1 \times m_2 = -1$.
4. Substitute the gradients: $\left(\frac{k}{2}\right) \times 4 = -1$.
5. Simplify: $2k = -1 \implies k = -\frac{1}{2}$.
Option D is chosen by students who mistakenly equate the gradients as if the lines were parallel ($k/2 = 4 \implies k=8$).

**6. Find the equation of the straight line passing through the points $(3, 1)$ and $(-2, -9)$.**

- A. $2x + y - 7 = 0$
- B. $2x - y - 5 = 0$
- C. $x - 2y - 1 = 0$
- D. $x + 2y - 5 = 0$

**Answer: B.**
1. First, find the gradient: $m = \frac{-9 - 1}{-2 - 3} = \frac{-10}{-5} = 2$.
2. Use the point-slope form with the first point $(3, 1)$: $y - y_1 = m(x - x_1)$.
3. Substitute the values: $y - 1 = 2(x - 3)$.
4. Expand the bracket: $y - 1 = 2x - 6$.
5. Rearrange into general form: $2x - y - 5 = 0$.
Option C occurs if you mistakenly calculate the gradient as "run over rise" ($\frac{1}{2}$) instead of "rise over run".

**7. Let $P$ be the midpoint of the line segment joining $A(-4, 2)$ and $B(2, 10)$. Find the distance of $P$ from the origin $(0, 0)$.**

- A. $10$
- B. $\sqrt{148}$
- C. $\sqrt{37}$
- D. $5$

**Answer: C.**
1. Calculate the midpoint $P$: $P = \left( \frac{-4 + 2}{2}, \frac{2 + 10}{2} \right)$.
2. Simplify the coordinates of $P$: $P = \left( \frac{-2}{2}, \frac{12}{2} \right) = (-1, 6)$.
3. Find the distance from $P(-1, 6)$ to the origin $(0, 0)$.
4. Apply the distance formula: $d = \sqrt{(-1 - 0)^2 + (6 - 0)^2}$.
5. Square the values: $d = \sqrt{(-1)^2 + (6)^2} = \sqrt{1 + 36}$.
6. Add the terms: $d = \sqrt{37}$.
Option B results from carelessly adding the original coordinates together to get $(-2, 12)$ without dividing by 2 to find the true midpoint.

**8. The equation of a line is $4x - 3y + 12 = 0$. Find its gradient and $y$-intercept respectively.**

- A. gradient $-\frac{4}{3}$, intercept $4$
- B. gradient $\frac{4}{3}$, intercept $-4$
- C. gradient $\frac{4}{3}$, intercept $4$
- D. gradient $4$, intercept $12$

**Answer: C.**
1. Start with the general equation: $4x - 3y + 12 = 0$.
2. Rearrange to make $y$ the subject (slope-intercept form, $y = mx + c$).
3. Move $-3y$ to the right side to make it positive: $3y = 4x + 12$.
4. Divide every term by $3$: $y = \frac{4}{3}x + 4$.
5. Compare to $y = mx + c$: the gradient $m = \frac{4}{3}$ and the $y$-intercept $c = 4$.
Option A has the correct intercept but the wrong sign on the gradient. It comes from using $m = -\frac{A}{B}$ with $B = 3$ instead of $B = -3$, which gives $-\frac{4}{3}$ instead of $\frac{4}{3}$.

**9. The points $P(1, 2)$, $Q(3, y)$, and $R(4, 11)$ are collinear. Find the value of $y$.**

- A. $5$
- B. $6$
- C. $7$
- D. $8$

**Answer: D.**
1. Because the points are collinear, the gradient of $PQ$ equals the gradient of $PR$ (or $QR$).
2. Find the gradient of $PR$: $m_{PR} = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$.
3. Write the expression for the gradient of $PQ$: $m_{PQ} = \frac{y - 2}{3 - 1} = \frac{y - 2}{2}$.
4. Equate the two gradients: $\frac{y - 2}{2} = 3$.
5. Multiply both sides by 2: $y - 2 = 6$.
6. Solve for $y$: $y = 8$.
Option C might result from small arithmetic errors during cross-multiplication.

**10. A straight line has a gradient of $-\frac{1}{2}$ and passes through the point $(-4, 3)$. Which of the following is the equation of the line?**

- A. $x + 2y - 2 = 0$
- B. $x - 2y + 10 = 0$
- C. $2x + y + 5 = 0$
- D. $x + 2y - 10 = 0$

**Answer: A.**
1. Identify the given values: $m = -\frac{1}{2}$ and point $(x_1, y_1) = (-4, 3)$.
2. Use the point-slope form: $y - y_1 = m(x - x_1)$.
3. Substitute the values carefully: $y - 3 = -\frac{1}{2}(x - (-4))$.
4. Simplify the bracket: $y - 3 = -\frac{1}{2}(x + 4)$.
5. Multiply through by 2 to clear the fraction: $2(y - 3) = -1(x + 4)$.
6. Expand: $2y - 6 = -x - 4$.
7. Move all terms to the left side: $x + 2y - 6 + 4 = 0 \implies x + 2y - 2 = 0$.
Option D comes from getting the double-negative sign wrong when substituting the $x$-coordinate, resulting in $x - 4$ instead of $x + 4$.
