# JAMB Mathematics Notes: Differentiation

## What JAMB expects

This topic is Section IV, Topic 1 of the JAMB Mathematics syllabus: Differentiation. It covers the following content items:

- **a.** limit of a function;
- **b.** differentiation of explicit algebraic and simple trigonometrical functions – sine, cosine and tangent.

By the end of these notes, you should be able to:

1. find the limit of a function;
2. differentiate explicit algebraic and simple trigonometrical functions.

Differentiation is a core part of calculus. It deals with finding the rate at which things change. Before we can understand differentiation, we must first understand the concept of a limit. 

## Limit of a function

**Objective i: find the limit of a function.**  
**Content a: limit of a function.**

The **limit** of a function is the value that the function approaches as the input value (often $x$) gets closer and closer to a particular number. We write this as $\lim_{x \to a} f(x) = L$, which is read as "the limit of $f(x)$ as $x$ approaches $a$ is $L$".

[IMAGE: A graph of the function y = (x^2 - 4)/(x - 2), which looks exactly like the straight line y = x + 2, but with a small empty circle (a hole) exactly at the point (2, 4) to show the function is undefined there. An arrow along the x-axis approaches the value 2 from both sides, and corresponding arrows along the y-axis approach the value 4 from both sides. Labels to add later: "y-axis", "x-axis", "Curve y = (x^2 - 4)/(x - 2)", "x approaches 2", "y approaches 4", "Hole at (2, 4)". Clean flat textbook style, white background.]

### 1. Direct substitution

The easiest way to find a limit is to substitute the number directly into the function. If you get a normal number as your answer, you are done!

**Example 1**  
Evaluate $\lim_{x \to 2} (3x^2 - 4x + 5)$.

**Working:**
1. Substitute $x = 2$ directly into the expression: $3(2)^2 - 4(2) + 5$.
2. Calculate the powers: $3(4) - 8 + 5$.
3. Multiply and add: $12 - 8 + 5 = 9$.

**Answer:** The limit is $9$.

### 2. Limits yielding indeterminate forms ($0/0$)

Sometimes, direct substitution gives you $\frac{0}{0}$. In mathematics, this is called an **indeterminate form**. It does not mean the answer is $0$, and it does not mean the limit is undefined. It simply means you have more work to do. You must **factorise** the numerator and denominator, cancel out the common factor that is causing the zero, and then substitute again.

**Example 2 (Difference of two squares)**  
Evaluate $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$.

**Working:**
1. Try direct substitution: $\frac{3^2 - 9}{3 - 3} = \frac{9 - 9}{0} = \frac{0}{0}$. This is indeterminate, so we must factorise.
2. Recognise that the numerator $x^2 - 9$ is a difference of two squares: $x^2 - 3^2 = (x - 3)(x + 3)$.
3. Rewrite the limit: $\lim_{x \to 3} \frac{(x - 3)(x + 3)}{x - 3}$.
4. Cancel the common factor $(x - 3)$ from the top and bottom: $\lim_{x \to 3} (x + 3)$.
5. Substitute $x = 3$ into the simplified expression: $3 + 3 = 6$.

**Answer:** The limit is $6$.

**Example 3 (Quadratic expression)**  
Evaluate $\lim_{x \to 2} \frac{2x^2 - x - 6}{x - 2}$.

**Working:**
1. Try direct substitution: $\frac{2(2)^2 - 2 - 6}{2 - 2} = \frac{8 - 2 - 6}{0} = \frac{0}{0}$. We must factorise.
2. Factorise the numerator $2x^2 - x - 6$. We need two numbers that multiply to $2 \times -6 = -12$ and add to $-1$. Those numbers are $-4$ and $3$.
3. Split the middle term: $2x^2 - 4x + 3x - 6 = 2x(x - 2) + 3(x - 2) = (2x + 3)(x - 2)$.
4. Rewrite the limit: $\lim_{x \to 2} \frac{(2x + 3)(x - 2)}{x - 2}$.
5. Cancel the common factor $(x - 2)$: $\lim_{x \to 2} (2x + 3)$.
6. Substitute $x = 2$: $2(2) + 3 = 4 + 3 = 7$.

**Answer:** The limit is $7$.

**Example 4 (Sum or difference of two cubes)**  
Evaluate $\lim_{x \to -1} \frac{x^3 + 1}{x + 1}$.

**Working:**
1. Direct substitution gives $\frac{(-1)^3 + 1}{-1 + 1} = \frac{-1 + 1}{0} = \frac{0}{0}$.
2. Factorise the numerator. Remember the rule for the sum of two cubes: $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$.
3. Apply this to $x^3 + 1^3$: $(x + 1)(x^2 - x(1) + 1^2) = (x + 1)(x^2 - x + 1)$.
4. Rewrite the limit: $\lim_{x \to -1} \frac{(x + 1)(x^2 - x + 1)}{x + 1}$.
5. Cancel $(x + 1)$: $\lim_{x \to -1} (x^2 - x + 1)$.
6. Substitute $x = -1$: $(-1)^2 - (-1) + 1 = 1 + 1 + 1 = 3$.

**Answer:** The limit is $3$.

### Optional, beyond the JAMB syllabus: L'Hôpital's Rule

> **This section is optional and is not part of the JAMB syllabus.** JAMB expects you to find limits by substitution and factorisation, as shown above. L'Hôpital's Rule is normally taught after secondary school. It is included only for curious students and for checking answers. Do not rely on it, and do not use it unless you have already learnt differentiation (next section).

If direct substitution gives $\frac{0}{0}$, **L'Hôpital's Rule** says: differentiate the numerator, differentiate the denominator, and then substitute the value of $x$.

As a check, let us solve Example 3 again: $\lim_{x \to 2} \frac{2x^2 - x - 6}{x - 2}$.
1. Differentiate the numerator $2x^2 - x - 6$ to get $4x - 1$.
2. Differentiate the denominator $x - 2$ to get $1$.
3. Divide them: $\frac{4x - 1}{1} = 4x - 1$.
4. Substitute $x = 2$: $4(2) - 1 = 8 - 1 = 7$, the same answer as the factorisation method.

> **Common Mistake:** When using L'Hôpital's Rule, do **not** use the quotient rule. Just differentiate the top on its own, and the bottom on its own. Also, remember you can only use this rule if substitution gives $\frac{0}{0}$.

## Differentiation of explicit algebraic and simple trigonometrical functions

**Objective ii: differentiate explicit algebraic and simple trigonometrical functions.**  
**Content b: differentiation of explicit algebraic and simple trigonometrical functions – sine, cosine and tangent.**

Differentiation is the process of finding the **derivative** of a function. The derivative tells us the rate of change of one quantity with respect to another. On a graph, the derivative represents the **gradient (or slope)** of the tangent to the curve at any given point.

If a function is written as $y$, its derivative with respect to $x$ is written as $\frac{dy}{dx}$ (pronounced "dee-why by dee-ex"). If the function is written as $f(x)$, its derivative is written as $f'(x)$.

[IMAGE: A 2D Cartesian coordinate system showing a smooth curve, such as y = x^2. A straight tangent line touches the curve exactly at a point P(x, y). A small right-angled triangle is drawn under the tangent line near P, labelled with vertical rise 'dy' and horizontal run 'dx' to show the gradient of the line. Labels to add later: "y-axis", "x-axis", "Curve y = f(x)", "Tangent line", "P(x, y)", "dy", "dx", "Gradient = dy/dx". Clean flat textbook style, white background.]

### 1. Differentiating basic polynomials

To differentiate a basic term like $ax^n$, we use the **Power Rule**: multiply the term by the current power, and then subtract $1$ from the power. 
$$ \frac{d}{dx}(ax^n) = anx^{n-1} $$

**Rules to remember:**
- The derivative of $x$ is $1$.
- The derivative of a constant number (like $5$, $-7$, or $100$) is $0$, because a constant never changes.
- To differentiate a long polynomial, differentiate each term one by one (this is the sum and difference rule).

**Example 1**  
Find $\frac{dy}{dx}$ if $y = 5x^3 - 2x^2 + 7x - 1$.

**Working:**
1. Differentiate $5x^3$: multiply by $3$ to get $15$, subtract $1$ from power to get $2$. Result: $15x^2$.
2. Differentiate $-2x^2$: multiply by $2$ to get $-4$, subtract $1$ from power to get $1$. Result: $-4x$.
3. Differentiate $7x$: the $x$ drops away. Result: $7$.
4. Differentiate $-1$: it is a constant, so it becomes $0$.

**Answer:** $\frac{dy}{dx} = 15x^2 - 4x + 7$.

### 2. Differentiating fractional and negative powers

JAMB often hides the powers using fractions or square roots. Before differentiating, you must rewrite the expression in the standard index form $ax^n$ using the laws of indices.
- $\frac{1}{x^n} = x^{-n}$
- $\sqrt{x} = x^{\frac{1}{2}}$

**Example 2**  
Find $\frac{dy}{dx}$ if $y = \frac{1}{x^2} + \sqrt{x}$.

**Working:**
1. Rewrite the expression in index form: $y = x^{-2} + x^{\frac{1}{2}}$.
2. Differentiate $x^{-2}$ using the power rule: $-2 \times x^{-2 - 1} = -2x^{-3}$.
3. Differentiate $x^{\frac{1}{2}}$ using the power rule: $\frac{1}{2} \times x^{\frac{1}{2} - 1} = \frac{1}{2}x^{-\frac{1}{2}}$.
4. Combine them: $\frac{dy}{dx} = -2x^{-3} + \frac{1}{2}x^{-\frac{1}{2}}$.
5. Write it back in a neat fraction format (JAMB options usually look like this): $\frac{dy}{dx} = -\frac{2}{x^3} + \frac{1}{2\sqrt{x}}$.

### 3. The Chain Rule (Function of a function)

When a function is "inside" another function (for example, an algebraic expression raised to a power), we use the **Chain Rule**. The formal formula is:
$$ \frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx} $$

However, for JAMB, the quickest way to apply the chain rule to an expression like $y = (ax+b)^n$ is:
1. Treat the bracket as a single letter and differentiate the outer power (bring the power down, reduce power by 1).
2. Differentiate the inside of the bracket.
3. Multiply both results together.

**Example 3**  
Find the derivative of $y = (2x + 1)^3$.

**Working (Shortcut method):**
1. Differentiate the outside power: $3(2x + 1)^2$.
2. Differentiate the inside expression $(2x + 1)$: the derivative is $2$.
3. Multiply them together: $3(2x + 1)^2 \times 2 = 6(2x + 1)^2$.

**Answer:** $6(2x + 1)^2$.

**Example 4 (With a square root)**  
Differentiate $y = \sqrt{x^2 + 1}$.

**Working:**
1. Rewrite the square root as a power: $y = (x^2 + 1)^{\frac{1}{2}}$.
2. Differentiate the outside power: $\frac{1}{2}(x^2 + 1)^{-\frac{1}{2}}$.
3. Differentiate the inside expression $(x^2 + 1)$: the derivative is $2x$.
4. Multiply them together: $\frac{1}{2}(x^2 + 1)^{-\frac{1}{2}} \times 2x$.
5. The $2$ and the $\frac{1}{2}$ cancel out, leaving: $x(x^2 + 1)^{-\frac{1}{2}}$.
6. Rewrite neatly: $\frac{x}{\sqrt{x^2 + 1}}$.

### 4. The Product Rule

When two separate functions of $x$ are multiplied together, we use the **Product Rule**. Let the two functions be $u$ and $v$. The rule is:
$$ \frac{dy}{dx} = v\frac{du}{dx} + u\frac{dv}{dx} $$
*(A simple way to remember it: keep the second, differentiate the first; plus keep the first, differentiate the second).*

**Example 5**  
If $y = (2x - 3)(x^2 + 4)$, find $\frac{dy}{dx}$.

**Working (using the Product Rule):**
1. Let $u = 2x - 3$ and $v = x^2 + 4$.
2. Differentiate $u$: $\frac{du}{dx} = 2$.
3. Differentiate $v$: $\frac{dv}{dx} = 2x$.
4. Apply the formula: $(x^2 + 4)(2) + (2x - 3)(2x)$.
5. Expand the brackets: $2x^2 + 8 + 4x^2 - 6x$.
6. Collect like terms: $6x^2 - 6x + 8$.

*(Note: For polynomials, you could also expand the brackets first to get $y = 2x^3 - 3x^2 + 8x - 12$, and differentiate normally. You will get the exact same answer: $6x^2 - 6x + 8$. However, you must know the product rule for when expansion is impossible, such as $x \sin x$).*

### 5. The Quotient Rule

When one function of $x$ is divided by another, we use the **Quotient Rule**. If $y = \frac{u}{v}$, where $u$ is the top (numerator) and $v$ is the bottom (denominator), the rule is:
$$ \frac{dy}{dx} = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2} $$
*(A simple way to remember it: Bottom times derivative of Top, MINUS Top times derivative of Bottom, all over Bottom squared. The order is strict because of the minus sign).*

**Example 6**  
Find the derivative of $y = \frac{x^2 + 1}{x - 1}$.

**Working:**
1. Let $u = x^2 + 1$ (the top). Differentiating gives $\frac{du}{dx} = 2x$.
2. Let $v = x - 1$ (the bottom). Differentiating gives $\frac{dv}{dx} = 1$.
3. Substitute into the formula: $\frac{(x - 1)(2x) - (x^2 + 1)(1)}{(x - 1)^2}$.
4. Expand the top brackets carefully (watch the minus sign!): $\frac{2x^2 - 2x - x^2 - 1}{(x - 1)^2}$.
5. Simplify the top: $\frac{x^2 - 2x - 1}{(x - 1)^2}$.

> **Common Mistake:** Writing the quotient rule backwards as $u\frac{dv}{dx} - v\frac{du}{dx}$. This will give you the wrong sign for your final answer. Always start with the bottom ($v$).

### 6. Differentiation of simple trigonometric functions

The JAMB syllabus requires you to know how to differentiate the three simple trigonometric functions: $\sin x$, $\cos x$ and $\tan x$. 

Memorise these three standard derivatives:
- $\frac{d}{dx}(\sin x) = \cos x$
- $\frac{d}{dx}(\cos x) = -\sin x$
- $\frac{d}{dx}(\tan x) = \sec^2 x$ 

*(Note: $\sec x$ is the reciprocal of $\cos x$, so $\sec^2 x$ means $\frac{1}{\cos^2 x}$).*

These basic rules can be combined with the Chain, Product, or Quotient rules.

**Example 7 (Chain Rule with Trig)**  
Find $\frac{dy}{dx}$ if $y = \sin(5x)$.

**Working:**
1. Differentiate the outside function ($\sin$) to get $\cos$. So, $\sin(5x)$ becomes $\cos(5x)$.
2. Differentiate the inside function ($5x$) to get $5$.
3. Multiply them together: $5 \times \cos(5x) = 5\cos(5x)$.

**Example 8 (Chain Rule with Powers)**  
Differentiate $y = \tan^3 x$.

**Working:**
1. Rewrite it so the power is clear: $y = (\tan x)^3$.
2. Apply the chain rule. Differentiate the outside power: $3(\tan x)^2$.
3. Differentiate the inside function ($\tan x$) to get $\sec^2 x$.
4. Multiply them together: $3(\tan x)^2 \times \sec^2 x = 3\tan^2 x \sec^2 x$.

**Example 9 (Product Rule with Trig)**  
Find $\frac{dy}{dx}$ if $y = x \cos x$.

**Working:**
1. This is a product. Let $u = x$ and $v = \cos x$.
2. Differentiating $u$ gives $\frac{du}{dx} = 1$.
3. Differentiating $v$ gives $\frac{dv}{dx} = -\sin x$.
4. Apply the product rule formula: $v\frac{du}{dx} + u\frac{dv}{dx}$.
5. Substitute the values: $(\cos x)(1) + (x)(-\sin x)$.
6. Simplify: $\cos x - x\sin x$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Limit** | The value a function approaches as the input gets closer to a specific number. |
| **Indeterminate form** | A result like $\frac{0}{0}$ that requires further work (factorisation) to solve. |
| **Differentiation** | The mathematical process of finding the derivative (rate of change) of a function. |
| **Derivative** | An expression that gives the gradient or rate of change of a curve at any point. Written as $\frac{dy}{dx}$ or $f'(x)$. |
| **Chain rule** | A formula for differentiating composite functions (a function inside another function). |
| **Product rule** | A formula for differentiating two functions that are multiplied together. |
| **Quotient rule** | A formula for differentiating one function divided by another function. |

## Exam tips and common mistakes

- **Don't leave a limit as $\frac{0}{0}$:** If you substitute your value and get zero divided by zero, factorise the top and bottom, cancel the common factor, and substitute again. (L'Hôpital's rule also works, but it is optional and not in the JAMB syllabus.)
- **Convert roots and fractions first:** Before you use the power rule, always rewrite roots as fractional powers (e.g., $\sqrt{x} = x^{1/2}$) and denominators as negative powers (e.g., $\frac{1}{x^3} = x^{-3}$).
- **The derivative of a constant is 0:** Many students accidentally leave a constant the same when differentiating. If $y = 3x^2 + 7$, $\frac{dy}{dx}$ is just $6x$. The $+ 7$ becomes zero.
- **Watch the minus sign for Cosine:** The derivative of $\sin x$ is $\cos x$, but the derivative of $\cos x$ is **$-\sin x$**. Forgetting this minus sign is the most common trig mistake in JAMB.
- **Quotient rule order matters:** The formula is $\frac{vu' - uv'}{v^2}$. Do not swap the top terms to $uv' - vu'$, or your answer will have the wrong sign. Start with the bottom variable, $v$.

## Quick summary

1. The limit of a function is evaluated by direct substitution. If the result is a normal number, that is your answer.
2. If direct substitution results in the indeterminate form $\frac{0}{0}$, you must factorise and cancel common terms to find the true limit.
3. Differentiation finds the derivative, which represents the gradient of a curve or the rate of change. 
4. The Power Rule states that if $y = ax^n$, then $\frac{dy}{dx} = anx^{n-1}$.
5. The Chain Rule ($\frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx}$) is used for differentiating a function of a function, such as an expression in a bracket raised to a power.
6. The Product Rule ($\frac{dy}{dx} = v\frac{du}{dx} + u\frac{dv}{dx}$) is used when two functions of $x$ are multiplied.
7. The Quotient Rule ($\frac{dy}{dx} = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}$) is used when one function is divided by another.
8. For trigonometric functions: differentiate $\sin x$ to get $\cos x$; $\cos x$ to get $-\sin x$; and $\tan x$ to get $\sec^2 x$.

## Practice questions

**1. Evaluate $\lim_{x \to 1} (4x^3 - 3x + 2)$.**

- A. $3$
- B. $5$
- C. $0$
- D. $1$

**Answer: A.**
1. Attempt direct substitution by replacing $x$ with $1$.
2. $4(1)^3 - 3(1) + 2$
3. $= 4(1) - 3 + 2$
4. $= 4 - 3 + 2 = 3$.

**2. Find the limit of $\frac{x^2 - 4x + 4}{x - 2}$ as $x \to 2$.**

- A. $2$
- B. $0$
- C. $4$
- D. Undefined

**Answer: B.**
1. Direct substitution gives $\frac{2^2 - 4(2) + 4}{2 - 2} = \frac{4 - 8 + 4}{0} = \frac{0}{0}$. 
2. Factorise the numerator $x^2 - 4x + 4$: it becomes $(x - 2)(x - 2)$.
3. The limit becomes $\lim_{x \to 2} \frac{(x - 2)(x - 2)}{x - 2}$.
4. Cancel the common factor $(x - 2)$ to get $\lim_{x \to 2} (x - 2)$.
5. Substitute $x = 2$ again: $2 - 2 = 0$. (Do not assume that getting $\frac{0}{0}$ initially means the limit is "Undefined").

**3. Evaluate $\lim_{x \to -3} \frac{2x^2 + 5x - 3}{x + 3}$.**

- A. $7$
- B. $-7$
- C. $-1$
- D. $0$

**Answer: B.**
1. Direct substitution gives $\frac{2(-3)^2 + 5(-3) - 3}{-3 + 3} = \frac{18 - 15 - 3}{0} = \frac{0}{0}$, so we must factorise.
2. Factorise the numerator: we need two numbers that multiply to $2 \times -3 = -6$ and add to $5$. They are $6$ and $-1$. So $2x^2 + 5x - 3 = 2x^2 + 6x - x - 3 = 2x(x + 3) - 1(x + 3) = (2x - 1)(x + 3)$.
3. Rewrite the limit: $\lim_{x \to -3} \frac{(2x - 1)(x + 3)}{x + 3}$, then cancel $(x + 3)$ to get $\lim_{x \to -3} (2x - 1)$.
4. Substitute $x = -3$: $2(-3) - 1 = -6 - 1 = -7$. Option A ($7$) comes from a sign error when substituting.

**4. Find the derivative of $y = 3x^4 - 2x^3 + 5x - 7$.**

- A. $12x^3 - 6x^2 + 5$
- B. $12x^3 - 6x^2 - 7$
- C. $12x^4 - 6x^3 + 5x$
- D. $7x^3 - 5x^2 + 5$

**Answer: A.**
1. Differentiate $3x^4$ to get $12x^3$.
2. Differentiate $-2x^3$ to get $-6x^2$.
3. Differentiate $5x$ to get $5$.
4. The constant $-7$ differentiates to $0$. 
5. Combine them: $12x^3 - 6x^2 + 5$.

**5. Find $\frac{dy}{dx}$ if $y = 2\sqrt{x} + \frac{3}{x}$.**

- A. $\frac{1}{\sqrt{x}} + \frac{3}{x^2}$
- B. $\frac{1}{2\sqrt{x}} - \frac{3}{x^2}$
- C. $\frac{1}{\sqrt{x}} - \frac{3}{x^2}$
- D. $\frac{2}{\sqrt{x}} - \frac{3}{x^2}$

**Answer: C.**
1. Rewrite the expression in index notation: $y = 2x^{\frac{1}{2}} + 3x^{-1}$.
2. Differentiate $2x^{\frac{1}{2}}$: $2 \times \frac{1}{2}x^{\frac{1}{2} - 1} = 1x^{-\frac{1}{2}} = \frac{1}{\sqrt{x}}$.
3. Differentiate $3x^{-1}$: $3 \times -1x^{-1 - 1} = -3x^{-2} = -\frac{3}{x^2}$.
4. Combine the terms: $\frac{1}{\sqrt{x}} - \frac{3}{x^2}$.

**6. Differentiate $y = (3x - 2)^4$ with respect to $x$.**

- A. $4(3x - 2)^3$
- B. $12(3x - 2)^3$
- C. $12(3x - 2)^4$
- D. $4(3x - 2)^5$

**Answer: B.**
1. Use the chain rule. Treat $(3x - 2)$ as the inner function.
2. Differentiate the outside power: $4(3x - 2)^3$.
3. Differentiate the inside expression: $\frac{d}{dx}(3x - 2) = 3$.
4. Multiply them together: $4(3x - 2)^3 \times 3 = 12(3x - 2)^3$. Option A is incorrect because the student forgot to multiply by the derivative of the inside bracket.

**7. If $y = x^2 \sin x$, find $\frac{dy}{dx}$.**

- A. $2x \cos x$
- B. $x^2 \cos x - 2x \sin x$
- C. $x^2 \cos x + 2x \sin x$
- D. $2x \sin x - x^2 \cos x$

**Answer: C.**
1. Use the product rule since $x^2$ is multiplied by $\sin x$. Let $u = x^2$ and $v = \sin x$.
2. Find $u' = 2x$.
3. Find $v' = \cos x$.
4. Apply the formula $vu' + uv'$: $(\sin x)(2x) + (x^2)(\cos x)$.
5. Rearrange neatly: $x^2 \cos x + 2x \sin x$.

**8. Evaluate $\frac{dy}{dx}$ for $y = \frac{x + 1}{x - 1}$.**

- A. $\frac{2}{(x - 1)^2}$
- B. $\frac{-2}{(x - 1)^2}$
- C. $\frac{2x}{(x - 1)^2}$
- D. $\frac{-1}{(x - 1)^2}$

**Answer: B.**
1. Use the quotient rule. Let the top $u = x + 1$ and the bottom $v = x - 1$.
2. Find $u' = 1$ and $v' = 1$.
3. Apply the formula $\frac{vu' - uv'}{v^2}$.
4. Substitute: $\frac{(x - 1)(1) - (x + 1)(1)}{(x - 1)^2}$.
5. Expand the numerator: $\frac{x - 1 - x - 1}{(x - 1)^2}$.
6. Simplify to get $\frac{-2}{(x - 1)^2}$. Option A is a common error resulting from getting the quotient rule formula backward.

**9. Find the derivative of $y = 2\cos(3x)$.**

- A. $-6\sin(3x)$
- B. $6\sin(3x)$
- C. $-2\sin(3x)$
- D. $2\sin(3x)$

**Answer: A.**
1. Use the chain rule. The outside function is $2\cos()$ and the inside is $3x$.
2. Differentiate the outside function: the derivative of $\cos$ is $-\sin$, giving $-2\sin(3x)$.
3. Differentiate the inside function: the derivative of $3x$ is $3$.
4. Multiply them: $-2\sin(3x) \times 3 = -6\sin(3x)$. (Remembering that the derivative of cosine yields a negative value is crucial here).

**10. Differentiate $y = \tan^2 x$ with respect to $x$.**

- A. $2\tan x$
- B. $\sec^2 x$
- C. $2\sec^2 x$
- D. $2\tan x \sec^2 x$

**Answer: D.**
1. Rewrite the expression as $y = (\tan x)^2$.
2. Apply the chain rule. Bring down the power: $2(\tan x)^1$.
3. Differentiate the inside function $\tan x$: its derivative is $\sec^2 x$.
4. Multiply them together: $2\tan x \times \sec^2 x = 2\tan x \sec^2 x$.
