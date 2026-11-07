# JAMB Mathematics Notes: Integration

## What JAMB expects

This topic is Topic 3 of Section IV: CALCULUS in the JAMB Mathematics syllabus. It introduces the reverse process of differentiation, known as integration. It has two content items:

- (a) integration of explicit algebraic and simple trigonometrical functions;
- (b) area under the curve.

By the end of these notes, you should be able to:

1. solve problems of integration involving algebraic and simple trigonometric functions;
2. calculate area under the curve (simple cases only).

## Integration of algebraic and simple trigonometrical functions

### What is integration?

**Integration** is the reverse process of differentiation. If you know the gradient (derivative) of a function, integration allows you to work backwards to find the original function. Because of this, an integrated function is often called an **antiderivative**.

The symbol for integration is an elongated 'S', written as $\int$. An integration expression always ends with $dx$ (or another variable like $dt$ or $d\theta$), which tells you which variable you are integrating with respect to. The function you are integrating is called the **integrand**.

### The constant of integration ($C$)

When you differentiate a constant number (like $5$, $-10$, or $100$), the result is $0$. Therefore, when you integrate a function to go backwards, you cannot know if there was originally a constant number attached. To account for this, you must always add an arbitrary **constant of integration**, represented by $C$, to every indefinite integral. 

**Textbook variation:** Some textbooks use $c$ for the constant of integration, while others use $k$. They mean exactly the same thing. Some textbooks also refer to the integrated function as the "primitive function".

### Rules for explicit algebraic functions

An explicit algebraic function is an expression made up of polynomials (powers of $x$), roots, and fractions. The fundamental rule for integrating a power of $x$ is the **power rule**:

$$ \int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (\text{where } n \neq -1) $$
where $n$ is the power, and $C$ is the constant of integration.

**Steps for the power rule:**
1. **Add $1$** to the current power.
2. **Divide** the term by the new power.

**Other important algebraic rules:**
- **Constant rule:** $\int a dx = ax + C$ (where $a$ is a constant number).
- **Sum and difference rule:** You can integrate terms separated by $+$ or $-$ one by one. $\int (f(x) \pm g(x)) dx = \int f(x) dx \pm \int g(x) dx$.
- **The exception ($n = -1$):** If the power is $-1$, the power rule would cause division by zero. Instead, the rule is:
  $$ \int \frac{1}{x} dx = \int x^{-1} dx = \ln|x| + C $$
  where $\ln$ is the natural logarithm.
- **Linear composite rule:** A shortcut for expressions like $(ax + b)^n$:
  $$ \int (ax + b)^n dx = \frac{(ax + b)^{n+1}}{a(n+1)} + C $$

### Rules for simple trigonometric functions

The JAMB syllabus requires you to integrate simple cases, mostly involving sine and cosine functions. Notice how the signs are the exact opposite of what you learned in differentiation!

- **Cosine:** $\int \cos x dx = \sin x + C$
- **Sine:** $\int \sin x dx = -\cos x + C$

When there is a constant $a$ multiplying $x$ inside the trigonometric function:
$$ \int \cos(ax) dx = \frac{1}{a} \sin(ax) + C $$
$$ \int \sin(ax) dx = -\frac{1}{a} \cos(ax) + C $$

---

## Solving problems of integration

### Worked examples: Indefinite integrals

**Example 1: Integrating a polynomial**
Evaluate $\int (5x^4 - 2x^3 + 3x - 7) dx$.

**Working:**
1. Apply the power rule to each term separately.
2. For $5x^4$: $\frac{5x^5}{5} = x^5$.
3. For $-2x^3$: $\frac{-2x^4}{4} = -\frac{1}{2}x^4$.
4. For $3x$: $\frac{3x^2}{2} = \frac{3}{2}x^2$.
5. For $-7$: $-7x$.
6. Combine and add $C$: $x^5 - \frac{1}{2}x^4 + \frac{3}{2}x^2 - 7x + C$.

**Example 2: Negative and fractional powers**
Evaluate $\int \left(\frac{3}{x^4} - \sqrt{x}\right) dx$.

**Working:**
1. Rewrite the expression using index notation: $\int (3x^{-4} - x^{1/2}) dx$.
2. Integrate $3x^{-4}$: add 1 to get $-3$, then divide: $\frac{3x^{-3}}{-3} = -x^{-3}$.
3. Integrate $-x^{1/2}$: add 1 to get $\frac{3}{2}$, then divide: $\frac{-x^{3/2}}{3/2} = -\frac{2}{3}x^{3/2}$.
4. Combine and add $C$: $-x^{-3} - \frac{2}{3}x^{3/2} + C$ (which can also be written as $-\frac{1}{x^3} - \frac{2}{3}\sqrt{x^3} + C$).

**Example 3: Simple trigonometric function**
Find $\int (2\cos 3x - \sin x) dx$.

**Working:**
1. The integral of $\cos 3x$ is $\frac{1}{3}\sin 3x$. Multiply by $2$: $\frac{2}{3}\sin 3x$.
2. The integral of $-\sin x$ is $-(-\cos x) = \cos x$.
3. Combine and add $C$: $\frac{2}{3}\sin 3x + \cos x + C$.

### Finding the equation of a curve

Because integration is the reverse of differentiation, JAMB often tests it by giving you the gradient of a curve ($\frac{dy}{dx}$) and asking for the equation of the curve ($y$).

**Example 4: Reconstructing a curve**
The gradient of a slope on a new road in Lagos is given by $\frac{dy}{dx} = 2x - 4$. If the slope passes through the coordinate $(3, 2)$, find the equation of the slope.

**Working:**
1. Integrate the gradient function to find $y$: 
   $$ y = \int (2x - 4) dx = \frac{2x^2}{2} - 4x + C = x^2 - 4x + C $$
2. Substitute the given point $x = 3$ and $y = 2$ to find the value of $C$.
3. $2 = (3)^2 - 4(3) + C$
4. $2 = 9 - 12 + C \Rightarrow 2 = -3 + C \Rightarrow C = 5$
5. The equation of the curve is $y = x^2 - 4x + 5$.

### Definite integrals

While an **indefinite integral** gives you a function with a $+ C$, a **definite integral** gives you a specific numerical value. Definite integrals have lower and upper bounds (limits), written at the bottom and top of the integral sign:
$$ \int_a^b f(x) dx $$
where $a$ is the lower limit and $b$ is the upper limit.

**How to evaluate a definite integral:**
1. Find the antiderivative $F(x)$ (do not add $C$, because it will cancel out anyway).
2. Put it in square brackets with the limits: $[F(x)]_a^b$.
3. Substitute the upper limit $b$ into the function.
4. Substitute the lower limit $a$ into the function.
5. Subtract the lower limit result from the upper limit result: **$F(b) - F(a)$**.

**Example 5: Evaluating a definite integral**
Evaluate $\int_{-1}^2 (3x^2 - 2) dx$.

**Working:**
1. Find the antiderivative: $x^3 - 2x$.
2. Write with limits: $[x^3 - 2x]_{-1}^2$.
3. Evaluate at upper limit ($x = 2$): $(2)^3 - 2(2) = 8 - 4 = 4$.
4. Evaluate at lower limit ($x = -1$): $(-1)^3 - 2(-1) = -1 + 2 = 1$.
5. Subtract lower result from upper result: $4 - 1 = 3$.

> **Common mistakes in solving integration problems:**
> - **Mixing up rules:** Subtracting 1 from the power instead of adding 1 (doing differentiation instead of integration).
>   - *Wrong:* $\int x^3 dx = 3x^2 + C$.
>   - *Correct:* $\int x^3 dx = \frac{x^4}{4} + C$.
> - **Forgetting $+ C$:** Always include it for indefinite integrals!
> - **Wrong signs for trig functions:** The derivative of sine is cosine, but the *integral* of sine is negative cosine!
> - **Subtracting limits backwards:** In a definite integral, always do (Upper Limit) minus (Lower Limit).

---

## Area under the curve

In geometry, you know how to find the area of simple shapes like rectangles and triangles. But how do you find the exact area of a region with a curved boundary? This is the most famous application of the definite integral.

The area bounded by a curve $y = f(x)$, the x-axis, and two vertical lines $x = a$ and $x = b$ is exactly equal to the definite integral:
$$ \text{Area} = \int_a^b f(x) dx $$

[IMAGE: A 2D Cartesian coordinate system with a smooth positive curve y = f(x). The area between the curve, the x-axis, and two vertical dotted lines at x = a and x = b is shaded in a light blue colour. Labels to add later: "y = f(x)", "a" on the x-axis, "b" on the x-axis, "Area = ∫ f(x) dx" inside the shaded region. Clean flat textbook style, white background.]

---

## Calculating area under the curve

JAMB restricts questions to "simple cases only". This means you will mostly deal with areas that sit completely above the x-axis, or simple shapes bounded entirely by the x-axis. 

### Case 1: The limits are given to you

If a question gives you the specific vertical lines (ordinates) bounding the area, you just plug them in as your limits $a$ and $b$.

**Example 6: Area with given limits**
Find the area enclosed by the curve $y = x^2 + 2$, the x-axis, and the ordinates $x = 1$ and $x = 3$.

**Working:**
1. Set up the integral with the given limits: $\int_1^3 (x^2 + 2) dx$.
2. Integrate the function: $[\frac{x^3}{3} + 2x]_1^3$.
3. Evaluate at the upper limit ($x = 3$): $\frac{3^3}{3} + 2(3) = \frac{27}{3} + 6 = 9 + 6 = 15$.
4. Evaluate at the lower limit ($x = 1$): $\frac{1^3}{3} + 2(1) = \frac{1}{3} + 2 = \frac{7}{3}$.
5. Subtract: $15 - \frac{7}{3} = \frac{45}{3} - \frac{7}{3} = \frac{38}{3} = 12\frac{2}{3}$ square units.

### Case 2: The limits are not given (Bounded by the x-axis)

Often, JAMB will ask for the area "bounded by the curve and the x-axis", without giving you $x$ values. This means the curve forms a closed shape with the x-axis itself. To find your limits $a$ and $b$, you must calculate the **x-intercepts** (roots) where the curve crosses the x-axis.

[IMAGE: A 2D Cartesian coordinate system showing an arch shape (downward-opening parabola) representing a bridge. The curve is y = 9 - x². The curve crosses the x-axis at -3 and 3. The entire region between the curve and the x-axis is shaded light blue to represent the concrete cross-section. Labels to add later: "y = 9 - x²", "-3" on the x-axis, "3" on the x-axis, "Area" inside the shaded region. Clean flat textbook style, white background.]

**Example 7: Calculating roots for limits**
A concrete arch for a new bridge in Abuja has an inner curve modeled by the equation $y = 9 - x^2$ (in metres). Calculate the cross-sectional area under the arch and above the ground (the x-axis).

**Working:**
1. Find where the arch meets the ground by setting $y = 0$: 
   $$ 9 - x^2 = 0 \Rightarrow x^2 = 9 \Rightarrow x = -3 \text{ and } x = 3 $$
2. The limits of integration are $a = -3$ and $b = 3$.
3. Set up the integral: $\text{Area} = \int_{-3}^3 (9 - x^2) dx$.
4. Integrate: $[9x - \frac{x^3}{3}]_{-3}^3$.
5. Evaluate at the upper limit ($3$): $9(3) - \frac{3^3}{3} = 27 - 9 = 18$.
6. Evaluate at the lower limit ($-3$): $9(-3) - \frac{(-3)^3}{3} = -27 - \frac{-27}{3} = -27 + 9 = -18$.
7. Subtract the lower result from the upper result: $18 - (-18) = 18 + 18 = 36 \text{ m}^2$.

*(Note: Area is a physical quantity and is always positive. If an area sits completely below the x-axis, calculating the definite integral will give a negative number. Just take the positive absolute value of your answer!)*

## Key terms

| Term | Meaning |
| --- | --- |
| **Integration** | The reverse process of differentiation; finding a function from its derivative. |
| **Integrand** | The mathematical expression or function that is being integrated. |
| **Indefinite integral** | An integral without upper and lower limits, resulting in a general function with a constant $+ C$. |
| **Definite integral** | An integral with specified upper and lower limits, resulting in a numerical value. |
| **Constant of integration ($C$)** | An arbitrary constant added to indefinite integrals because the derivative of any constant is zero. |
| **Limits of integration** | The lower bound ($a$) and upper bound ($b$) used in a definite integral to evaluate area. |
| **Area under a curve** | The geometric area enclosed between a curve, the x-axis, and given vertical boundaries. |

## Exam tips and common mistakes

- **Don't mistake derivatives for integrals!** Check your work by quickly differentiating your final answer in your head. It should take you right back to the original question.
- **Never forget $+ C$:** If a question has no limits (an indefinite integral), the correct option *must* have a constant $C$ (or $k$). Options without it are traps.
- **Beware of zero lower limits:** When evaluating $[F(x)]_0^b$, do not assume that substituting $0$ always gives $0$. For example, $\cos(0) = 1$, not $0$!
- **Find your intercepts correctly:** For area problems where bounds are missing, factorise the quadratic equation carefully to find the x-intercepts. A sign error here ruins the whole calculation.
- **Trigonometric integrals use radians:** If you ever need to substitute an angle into a trigonometric integral, the angle is always treated as radians, not degrees.

## Quick summary

1. Integration is the reverse process of differentiation (finding the antiderivative).
2. For explicit algebraic functions, the power rule is $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ (provided $n \neq -1$).
3. The exception to the power rule is $\int x^{-1} dx = \ln|x| + C$.
4. The integral of simple trigonometric functions are $\int \cos(ax) dx = \frac{1}{a}\sin(ax) + C$ and $\int \sin(ax) dx = -\frac{1}{a}\cos(ax) + C$.
5. Indefinite integrals always include an arbitrary constant of integration, $C$.
6. A definite integral $\int_a^b f(x) dx$ is evaluated by substituting the upper limit and subtracting the result of the lower limit: $F(b) - F(a)$.
7. The exact area under a curve $y = f(x)$ between $x = a$ and $x = b$ is calculated using the definite integral $\int_a^b y dx$.
8. If limits are not given for an area completely bounded by the x-axis, set $y = 0$ to find the x-intercepts, and use them as your limits.

## Practice questions

**1. Evaluate $\int (4x^3 - 3x^2 + 2) dx$.**

- A. $x^4 - x^3 + 2x + C$
- B. $12x^2 - 6x + C$
- C. $x^4 - x^3 + C$
- D. $4x^4 - 3x^3 + 2x + C$

**Answer: A.** The correct evaluation is done as follows:

1. Integrate each term separately by adding 1 to the power and dividing by the new power.
2. $\int 4x^3 dx = \frac{4x^4}{4} = x^4$.
3. $\int -3x^2 dx = -\frac{3x^3}{3} = -x^3$.
4. $\int 2 dx = 2x$.
5. Add the constant of integration $C$: $x^4 - x^3 + 2x + C$. (Option B is the derivative, which is a common mistake).

**2. Evaluate $\int_1^2 (3x^2 - 4x) dx$.**

- A. $0$
- B. $1$
- C. $3$
- D. $-1$

**Answer: B.** The correct evaluation is done as follows:

1. Find the antiderivative: $\frac{3x^3}{3} - \frac{4x^2}{2} = x^3 - 2x$.
2. Write with limits: $[x^3 - 2x]_1^2$.
3. Evaluate at upper limit ($2$): $2^3 - 2(2^2) = 8 - 8 = 0$.
4. Evaluate at lower limit ($1$): $1^3 - 2(1^2) = 1 - 2 = -1$.
5. Subtract: $0 - (-1) = 1$.

**3. Find the integral of $\sin(2x)$ with respect to $x$.**

- A. $\frac{1}{2}\cos(2x) + C$
- B. $-\frac{1}{2}\cos(2x) + C$
- C. $2\cos(2x) + C$
- D. $-2\cos(2x) + C$

**Answer: B.** The correct evaluation is done as follows:

1. The rule for integrating $\sin(ax)$ is $-\frac{1}{a}\cos(ax) + C$.
2. Here, $a = 2$.
3. Therefore, the integral is $-\frac{1}{2}\cos(2x) + C$. (Option C is the derivative).

**4. Find the area bounded by the curve $y = x^3$, the x-axis, and the ordinates $x = 0$ and $x = 2$.**

- A. $4$
- B. $8$
- C. $2$
- D. $\frac{16}{3}$

**Answer: A.** The correct evaluation is done as follows:

1. Set up the integral for the area: $\int_0^2 x^3 dx$.
2. Integrate: $[\frac{x^4}{4}]_0^2$.
3. Evaluate at upper limit: $\frac{2^4}{4} = \frac{16}{4} = 4$.
4. Evaluate at lower limit: $\frac{0^4}{4} = 0$.
5. Difference: $4 - 0 = 4$ square units.

**5. Evaluate $\int \left(\frac{1}{x^2} + \frac{1}{x^3}\right) dx$.**

- A. $-\frac{1}{x} - \frac{1}{2x^2} + C$
- B. $\frac{1}{x} + \frac{1}{2x^2} + C$
- C. $-\frac{1}{x^3} - \frac{1}{2x^4} + C$
- D. $-\frac{2}{x^3} - \frac{3}{x^4} + C$

**Answer: A.** The correct evaluation is done as follows:

1. Rewrite using negative indices: $\int (x^{-2} + x^{-3}) dx$.
2. Add 1 to the powers and divide by the new powers.
3. For $x^{-2}$: $\frac{x^{-1}}{-1} = -x^{-1} = -\frac{1}{x}$.
4. For $x^{-3}$: $\frac{x^{-2}}{-2} = -\frac{1}{2}x^{-2} = -\frac{1}{2x^2}$.
5. Combine and add $C$: $-\frac{1}{x} - \frac{1}{2x^2} + C$. (Option D is the derivative).

**6. Calculate the area between the curve $y = 3x^2 - 2x$, the x-axis, and the lines $x = 1$ and $x = 3$.**

- A. $16$
- B. $18$
- C. $20$
- D. $26$

**Answer: B.** The correct evaluation is done as follows:

1. Set up the integral: $\int_1^3 (3x^2 - 2x) dx$.
2. Find the antiderivative: $[\frac{3x^3}{3} - \frac{2x^2}{2}]_1^3 = [x^3 - x^2]_1^3$.
3. Evaluate at upper limit ($3$): $3^3 - 3^2 = 27 - 9 = 18$.
4. Evaluate at lower limit ($1$): $1^3 - 1^2 = 1 - 1 = 0$.
5. Subtract: $18 - 0 = 18$ square units.

**7. Evaluate $\int_0^{\pi/2} \sin(2x) dx$.**

- A. $0$
- B. $\frac{1}{2}$
- C. $1$
- D. $2$

**Answer: C.** The correct evaluation is done as follows:

1. Find the antiderivative: $[-\frac{1}{2}\cos(2x)]_0^{\pi/2}$.
2. Evaluate at upper limit ($\pi/2$): $-\frac{1}{2}\cos(2 \times \frac{\pi}{2}) = -\frac{1}{2}\cos(\pi) = -\frac{1}{2}(-1) = \frac{1}{2}$.
3. Evaluate at lower limit ($0$): $-\frac{1}{2}\cos(2 \times 0) = -\frac{1}{2}\cos(0) = -\frac{1}{2}(1) = -\frac{1}{2}$.
4. Subtract: $\frac{1}{2} - (-\frac{1}{2}) = \frac{1}{2} + \frac{1}{2} = 1$.

**8. Find $\int (x - 2)^3 dx$.**

- A. $\frac{1}{4}(x - 2)^4 + C$
- B. $3(x - 2)^2 + C$
- C. $\frac{1}{3}(x - 2)^3 + C$
- D. $4(x - 2)^4 + C$

**Answer: A.** The correct evaluation is done as follows:

1. Use the linear substitution rule: $\int (ax+b)^n dx = \frac{(ax+b)^{n+1}}{a(n+1)} + C$.
2. Here $a = 1$, $b = -2$, and $n = 3$.
3. The integral is $\frac{(x-2)^4}{1 \times 4} + C = \frac{1}{4}(x-2)^4 + C$.

**9. Find the area bounded by the curve $y = 6x - x^2$ and the x-axis.**

- A. $18$
- B. $36$
- C. $72$
- D. $108$

**Answer: B.** The correct evaluation is done as follows:

1. The limits are not given, so find the x-intercepts by setting $y = 0$: $6x - x^2 = 0$.
2. Factorise: $x(6 - x) = 0$, giving limits $x = 0$ and $x = 6$.
3. Set up the integral: $\int_0^6 (6x - x^2) dx$.
4. Integrate: $[\frac{6x^2}{2} - \frac{x^3}{3}]_0^6 = [3x^2 - \frac{x^3}{3}]_0^6$.
5. Evaluate at upper limit ($6$): $3(6^2) - \frac{6^3}{3} = 3(36) - \frac{216}{3} = 108 - 72 = 36$.
6. Evaluate at lower limit ($0$): $3(0^2) - \frac{0^3}{3} = 0$.
7. Subtract: $36 - 0 = 36$ square units.

**10. Evaluate $\int_{-1}^1 (2x + 1)^2 dx$.**

- A. $\frac{14}{3}$
- B. $\frac{13}{3}$
- C. $\frac{28}{3}$
- D. $\frac{7}{3}$

**Answer: A.** The correct evaluation is done as follows:

1. Expand the bracket first: $(2x + 1)^2 = (2x + 1)(2x + 1) = 4x^2 + 4x + 1$.
2. Integrate: $[\frac{4x^3}{3} + \frac{4x^2}{2} + x]_{-1}^1 = [\frac{4x^3}{3} + 2x^2 + x]_{-1}^1$.
3. Evaluate at upper limit ($1$): $\frac{4(1)^3}{3} + 2(1)^2 + 1 = \frac{4}{3} + 2 + 1 = \frac{4}{3} + 3 = \frac{13}{3}$.
4. Evaluate at lower limit ($-1$): $\frac{4(-1)^3}{3} + 2(-1)^2 + (-1) = -\frac{4}{3} + 2 - 1 = -\frac{4}{3} + 1 = -\frac{1}{3}$.
5. Subtract lower result from upper result: $\frac{13}{3} - (-\frac{1}{3}) = \frac{13}{3} + \frac{1}{3} = \frac{14}{3}$. (Alternatively, you can solve this quickly using the linear shortcut rule).
