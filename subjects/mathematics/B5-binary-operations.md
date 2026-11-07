# JAMB Mathematics Notes: Binary Operations

## What JAMB expects

This file covers SECTION II: ALGEBRA, Topic 5 (Binary Operations) of the JAMB Mathematics syllabus. It includes the following content items:

- (a) properties of closure, commutativity, associativity and distributivity;
- (b) identity and inverse elements (simple cases only).

By the end of these notes, you should be able to:

1. solve problems involving closure, commutativity, associativity and distributivity;
2. solve problems involving identity and inverse elements.

## What is a binary operation?

A **binary operation** is a mathematical rule for combining two elements from a particular set to produce another element. You are already very familiar with the basic binary operations: addition ($+$), subtraction ($-$), multiplication ($\times$), and division ($\div$). When we add two numbers, for instance $3 + 4 = 7$, we are applying the binary operation of addition to the numbers 3 and 4 to get a single result, 7.

In JAMB Mathematics, questions on this topic usually invent *new* operations. They use symbols like $\ast$, $\oplus$, $\otimes$, $\Delta$, or $\circ$ to define a specific rule. For example, a question might define an operation as $x \ast y = x + y - 2$. This simply means: "To combine any two numbers $x$ and $y$, add them together and then subtract 2." Just as mixing water and garri yields a new product (eba) based on a specific process, a binary operation combines two numbers using a defined rule to yield a specific numerical result.

**Sets of numbers**
Binary operations are always defined on a specific set of numbers. Some common sets you will see in exams include:
- $\mathbb{R}$: The set of all real numbers (all integers, fractions, decimals, and irrational numbers like surds).
- $\mathbb{Z}$: The set of integers (..., $-2, -1, 0, 1, 2$, ...).
- $\mathbb{N}$: The set of natural numbers ($1, 2, 3$, ...).
- $\mathbb{Q}$: The set of rational numbers (any number that can be written as a fraction).

## Properties of closure, commutativity, associativity and distributivity

This section covers the fundamental mathematical properties that govern how binary operations behave. Knowing these definitions is crucial because JAMB questions will explicitly ask you to verify if a given operation satisfies one or more of these properties.

### 1. Closure property

A set is said to be **closed** under a binary operation if combining *any* two elements from that set always produces a result that is also a member of the same set. There must be absolutely no exceptions. 

If you can find even one pair of numbers in the set that, when combined, produces a result outside the set, the operation is *not closed*. 

[IMAGE: A Venn diagram labeled 'Set of Natural Numbers (N)'. Two numbers, 3 and 5, are inside the set circle. An arrow labeled 'Subtraction (3 - 5)' points from these numbers to a result '-2', which is drawn outside the set boundary, visually indicating that the set of natural numbers is not closed under subtraction. Style: clean flat textbook illustration, white background.]

### 2. Commutativity

An operation $\ast$ is **commutative** if the order in which you combine the elements does not change the final result. In simpler terms, you can swap the numbers around and still get the same answer.

**Rule for commutativity:** 
$$a \ast b = b \ast a$$ 
for all elements $a$ and $b$ in the set.

- Addition and multiplication of ordinary numbers are commutative ($3+4 = 4+3$ and $3 \times 4 = 4 \times 3$).
- Subtraction and division are *not* commutative ($3-4 \neq 4-3$, because $-1 \neq 1$).

[IMAGE: A balance scale diagram illustrating commutativity. On the left scale pan is a block labeled 'a' stacked with a block labeled 'b'. On the right scale pan is a block labeled 'b' stacked with a block labeled 'a' (reversed order). The scale is perfectly balanced. Below it, the equation 'a * b = b * a' is displayed. Style: clean flat textbook illustration, white background.]

### 3. Associativity

An operation $\ast$ is **associative** if, when combining three elements, the way you group them with brackets does not change the result. It is about moving the brackets, not rearranging the order of the letters.

**Rule for associativity:** 
$$(a \ast b) \ast c = a \ast (b \ast c)$$ 
for all elements $a, b, c$ in the set.

- Addition and multiplication are associative. For instance, $(2 + 3) + 4 = 5 + 4 = 9$, which is exactly the same as $2 + (3 + 4) = 2 + 7 = 9$.
- Subtraction and division are not associative.

### 4. Distributivity

Distributivity involves **two** different binary operations working together. An operation $\ast$ distributes over another operation $\oplus$ if applying $\ast$ to a combination made by $\oplus$ gives the same result as applying $\ast$ to each element separately and then combining the outcomes with $\oplus$.

**Rule for distributivity:** 
$$a \ast (b \oplus c) = (a \ast b) \oplus (a \ast c)$$

- In everyday arithmetic, multiplication distributes over addition: $2 \times (3 + 4) = (2 \times 3) + (2 \times 4)$.
- Addition does *not* distribute over multiplication: $2 + (3 \times 4) \neq (2 + 3) \times (2 + 4)$.

## Solving problems involving closure, commutativity, associativity and distributivity

JAMB questions will require you to apply the properties defined above to novel operations, often involving algebra. You may also be asked to evaluate operations presented in a tabular format (Cayley tables). 

### Examples on Closure

**Worked Example 1: Closure on Natural Numbers**
Determine if the set of natural numbers $\mathbb{N} = \{1, 2, 3, \dots\}$ is closed under subtraction.

**Solution:**
1. Choose two natural numbers, for example, 3 and 5.
2. Apply the subtraction operation: $3 - 5 = -2$.
3. Check the result: $-2$ is an integer, but it is not a natural number (natural numbers are strictly positive integers).
4. Because we found a result outside the set, the set of natural numbers is **not closed** under subtraction.

**Worked Example 2: Closure on Real Numbers**
A binary operation $\ast$ is defined on the set of all real numbers $\mathbb{R}$ by $a \ast b = \frac{a}{b}$. Is the operation closed?

**Solution:**
1. We must check if there is any real number combination that breaks the rule. Consider what happens if we choose $b = 0$, which is a real number.
2. The operation gives $a \ast 0 = \frac{a}{0}$. Division by zero is mathematically undefined.
3. Because the result is undefined, it is not a real number.
4. Therefore, the operation is **not closed** on the set of all real numbers. (Note: if the question had specified the set of *non-zero* real numbers, it would be closed).

### Examples on Commutativity

**Worked Example 3: Verifying Commutativity Algebraically**
An operation $\oplus$ is defined on the set of real numbers by $x \oplus y = x^2 + y^2 - xy$. Is the operation commutative?

**Solution:**
1. First, evaluate $x \oplus y$. The rule is already given as $x^2 + y^2 - xy$.
2. Next, evaluate $y \oplus x$. To do this, replace every $x$ with $y$ and every $y$ with $x$ in the original rule. This gives $y \oplus x = y^2 + x^2 - yx$.
3. Compare the two expressions. Since basic addition is commutative ($y^2 + x^2 = x^2 + y^2$) and multiplication is commutative ($yx = xy$), the two expressions are algebraically identical.
4. Since $x \oplus y = y \oplus x$, the operation is **commutative**.

### Examples on Associativity

**Worked Example 4: Verifying Associativity**
A binary operation $\ast$ is defined by $p \ast q = p + q + 2$. Show whether or not $\ast$ is associative.

**Solution:**
1. First, evaluate the left-hand side of the associativity rule: $(p \ast q) \ast r$.
   - Solve the bracket first: $p \ast q = p + q + 2$.
   - Now apply $\ast$ to the result $(p+q+2)$ and the element $r$. Treat $(p+q+2)$ as the "first term".
   - The rule for $\ast$ says "add the first term, the second term, and 2".
   - Result: $(p+q+2) + r + 2 = p + q + r + 4$.
2. Next, evaluate the right-hand side of the associativity rule: $p \ast (q \ast r)$.
   - Solve the bracket first: $q \ast r = q + r + 2$.
   - Now apply $\ast$ to $p$ and the result $(q+r+2)$.
   - Result: $p + (q+r+2) + 2 = p + q + r + 4$.
3. Compare both sides. Since $(p \ast q) \ast r = p \ast (q \ast r)$, the operation is **associative**.

> **Common Mistakes with Properties:** 
> A very common error is confusing commutativity with associativity. Remember: commutativity is about **swapping the order** of two items ($a, b \rightarrow b, a$). Associativity is about **moving the brackets** among three items without changing their left-to-right order. Also, ensure you substitute carefully when evaluating brackets for associativity; a sign error is very easy to make if you do not use parentheses when substituting.

### Examples on Distributivity

**Worked Example 5: Distributivity of operations**
Let operations $\otimes$ and $\oplus$ be defined on real numbers such that $x \otimes y = xy$ (standard multiplication) and $x \oplus y = x + y$ (standard addition). Verify that $\otimes$ distributes over $\oplus$.

**Solution:**
1. We need to check the distributivity rule: $a \otimes (b \oplus c) = (a \otimes b) \oplus (a \otimes c)$.
2. Evaluate the left-hand side:
   - First, solve the bracket: $b \oplus c = b + c$.
   - Next, apply $\otimes$: $a \otimes (b+c) = a(b+c) = ab + ac$.
3. Evaluate the right-hand side:
   - First, solve the separate brackets: $a \otimes b = ab$ and $a \otimes c = ac$.
   - Next, apply $\oplus$ to combine them: $(ab) \oplus (ac) = ab + ac$.
4. Since both sides yield $ab + ac$, the operation $\otimes$ distributes over $\oplus$.

### Solving problems using Operation Tables (Cayley Tables)

JAMB sometimes presents binary operations in a table (called a Cayley table). You need to know how to read properties directly from the table.

Consider the operation $\ast$ on the set $S = \{w, x, y, z\}$ given by the table:

| $\ast$ | $w$ | $x$ | $y$ | $z$ |
|--------|-----|-----|-----|-----|
| **$w$**| $x$ | $y$ | $w$ | $z$ |
| **$x$**| $y$ | $z$ | $x$ | $w$ |
| **$y$**| $w$ | $x$ | $y$ | $z$ |
| **$z$**| $z$ | $w$ | $z$ | $y$ |

**How to check for Closure from a table:**
Scan every single cell inside the body of the table. If every result is a member of the original set $\{w, x, y, z\}$, then the operation is closed. In this table, all outcomes are either $w, x, y,$ or $z$. The set is closed.

**How to check for Commutativity from a table:**
Draw a diagonal line from the top-left cell to the bottom-right cell (the main diagonal). If the table is a perfect mirror reflection across this diagonal line, the operation is commutative. 
Let us check: $w \ast x = y$, and $x \ast w = y$. $w \ast z = z$, but $z \ast w = z$. $x \ast z = w$, and $z \ast x = w$. All corresponding parts match, so it is commutative.

## Identity and inverse elements (simple cases only)

This section covers two of the most heavily tested concepts in JAMB binary operations: finding the identity element and finding the inverse element. You must understand how they relate to each other.

### The Identity Element ($e$)

The **identity element** (usually represented by the letter $e$) is a special element in the set that, when combined with any element $a$, leaves $a$ exactly as it was. It does not change the value of the other element.

**Rule for Identity:** 
$$a \ast e = a \quad \text{and} \quad e \ast a = a$$

- For standard addition, the identity element is **0** (because $a + 0 = a$).
- For standard multiplication, the identity element is **1** (because $a \times 1 = a$).

### The Inverse Element ($a^{-1}$)

The **inverse element** of a number $a$ (often written as $a^{-1}$) is the specific element that, when combined with $a$, "cancels it out" and produces the identity element $e$.

**Rule for Inverse:** 
$$a \ast a^{-1} = e \quad \text{and} \quad a^{-1} \ast a = e$$

- For standard addition, the inverse of $a$ is $-a$ (since $a + (-a) = 0$, where 0 is the additive identity).
- For standard multiplication, the inverse of $a$ is $\frac{1}{a}$ (since $a \times \frac{1}{a} = 1$, where 1 is the multiplicative identity).

[IMAGE: A three-step flowchart for finding an inverse element. Step 1 box: 'Set up equation a * e = a'. Arrow points to Step 2 box: 'Solve for the identity element (e)'. Arrow points to Step 3 box: 'Set up equation a * a⁻¹ = e and solve for a⁻¹'. Style: clean flat textbook illustration, white background.]

## Solving problems involving identity and inverse elements

### Finding the Identity Element algebraically

**How to find the identity element for a new operation:**
1. Set up the equation $a \ast e = a$ (or $x \ast e = x$, depending on the variables used).
2. Substitute the rule for the operation $\ast$ into the left-hand side, treating $e$ as your unknown variable.
3. Solve the equation for $e$. 
4. *Important limit:* The identity element must be a standalone number or constant. If your final answer for $e$ still contains the variable $a$, then the operation has no unique identity element.

**Worked Example 6: Finding the Identity Element**
A binary operation is defined by $x \ast y = x + y - 5$. Find the identity element.

**Solution:**
1. Set up the identity equation: $x \ast e = x$.
2. Apply the operation rule to the left side: $x + e - 5 = x$.
3. Subtract $x$ from both sides to isolate terms with $e$: $e - 5 = 0$.
4. Solve for $e$: $e = 5$.
The identity element is 5.

**Worked Example 7: Identity Element involving Multiplication**
The operation $\oplus$ is defined by $p \oplus q = p + q + pq$. Find the identity element.

**Solution:**
1. Set up the identity equation: $p \oplus e = p$.
2. Apply the operation rule: $p + e + pe = p$.
3. Subtract $p$ from both sides: $e + pe = 0$.
4. Factor out the common term $e$: $e(1 + p) = 0$.
5. For this product to equal zero for all valid values of $p$, $e$ must be equal to 0. 
The identity element is 0.

### Finding the Inverse Element algebraically

**How to find the inverse of an element:**
1. You **must** first find the identity element $e$. If you do not calculate $e$, it is logically impossible to find the inverse!
2. Let the inverse of the number be $y$.
3. Set up the equation $a \ast y = e$.
4. Apply the rule for $\ast$, substitute the value of $e$ you found in Step 1, and solve the equation to find $y$.

> **Common Mistake:** Many students attempt to find the inverse without calculating the identity element first, or they blindly assume the identity is always 0 or 1. Every newly defined operation has its own specific identity element. Always calculate $e$ first!

**Worked Example 8: Finding the Inverse of a Specific Number**
An operation $\ast$ is defined on the set of real numbers by $x \ast y = x + y - 3$. Find the inverse of the number 7.

**Solution:**
1. **Find the identity element $e$ first:**
   - $x \ast e = x$
   - $x + e - 3 = x$
   - $e - 3 = 0 \implies e = 3$.
2. **Find the inverse of 7:** Let the inverse of 7 be $y$.
   - $7 \ast y = e$
   - We know $e = 3$, so substitute it in: $7 \ast y = 3$.
   - Apply the operation rule to $7 \ast y$: $7 + y - 3 = 3$.
   - Simplify the left side: $4 + y = 3$.
   - Solve for $y$: $y = 3 - 4 = -1$.
The inverse of 7 is -1. 
*(You can verify this by checking if $7 \ast (-1)$ gives the identity 3: $7 + (-1) - 3 = 3$. It works!)*

**Worked Example 9: Finding the Inverse of a General Element**
A binary operation is defined by $a \ast b = \frac{ab}{4}$. Find the inverse of a general element $a$.

**Solution:**
1. **Find the identity $e$:**
   - $a \ast e = a$
   - Apply the rule: $\frac{ae}{4} = a$
   - Cross-multiply: $ae = 4a$.
   - Divide both sides by $a$ (assuming $a \neq 0$): $e = 4$.
2. **Find the inverse of $a$:** Let the inverse be $a^{-1}$.
   - $a \ast a^{-1} = e$
   - Substitute $e = 4$: $\frac{a \cdot a^{-1}}{4} = 4$
   - Cross-multiply: $a \cdot a^{-1} = 16$.
   - Divide by $a$: $a^{-1} = \frac{16}{a}$.
The inverse of any non-zero element $a$ under this operation is $\frac{16}{a}$.

### Finding Identity and Inverses using Tables

Let us revisit the operation table from earlier. 

| $\ast$ | $w$ | $x$ | $y$ | $z$ |
|--------|-----|-----|-----|-----|
| **$w$**| $x$ | $y$ | $w$ | $z$ |
| **$x$**| $y$ | $z$ | $x$ | $w$ |
| **$y$**| $w$ | $x$ | $y$ | $z$ |
| **$z$**| $z$ | $w$ | $z$ | $y$ |

**To find the identity element from a table:**
Look for the row that is exactly identical to the top header row, and the column that is exactly identical to the leftmost header column. The element where they intersect is the identity element.
- The header row is $w, x, y, z$. Look at row **$y$**; it reads $w, x, y, z$. 
- The header column is $w, x, y, z$. Look at column **$y$**; it reads $w, x, y, z$. 
- Therefore, the identity element $e$ is **$y$**.

**To find the inverse of an element from a table:**
Since we know the identity is $y$, to find the inverse of any element, we find where the result is $y$.
- Inverse of $w$: Look across row $w$ until you find $y$. It is under column $x$. So, $w \ast x = y$. Therefore, $w^{-1} = x$.
- Inverse of $x$: Look across row $x$ until you find $y$. It is under column $w$. So, $x \ast w = y$. Therefore, $x^{-1} = w$.
- Inverse of $z$: Look across row $z$ until you find $y$. It is under column $z$. So, $z \ast z = y$. Therefore, $z^{-1} = z$ (it is its own inverse).

## Key terms

| Term | Meaning |
| --- | --- |
| Binary operation | A mathematical rule for combining two elements from a set to produce a single result. |
| Closure | A property where combining any two elements from a set always produces a result that belongs to the same set. |
| Commutativity | A property where changing the order of the elements does not change the result ($a \ast b = b \ast a$). |
| Associativity | A property where changing the grouping brackets of three elements does not change the result ($(a \ast b) \ast c = a \ast (b \ast c)$). |
| Distributivity | A property where one operation distributes over another, just like multiplication distributes over addition ($a \otimes (b \oplus c) = (a \otimes b) \oplus (a \otimes c)$). |
| Identity element ($e$) | A special element that leaves any other element unchanged when combined with it ($a \ast e = a$). |
| Inverse element ($a^{-1}$) | An element that, when combined with a given element $a$, cancels it out to produce the identity element ($a \ast a^{-1} = e$). |
| Cayley table | A grid or matrix that shows the outcomes of a binary operation for a finite set of elements. |

## Exam tips and common mistakes

- **Always find the identity element first** before trying to find the inverse of an element. A widespread mistake is wrongly assuming the identity is 0 or 1 without analyzing the specific operation's rule.
- **Pay close attention to signs** when checking for commutativity or associativity. Operations involving subtraction or division are rarely commutative or associative. 
- **When checking associativity**, solve the bracket first. Treat the entire outcome of the bracket as a single entity when you combine it with the third element. Failure to do this correctly leads to algebraic messes.
- **Do not mix up variables.** When finding the identity, your goal is to isolate and solve for $e$. Treat the other variable (like $x$ or $p$) as a constant that should hopefully cancel out. 
- **In substitution questions** (e.g., evaluate $3 \ast 4$ if $a \ast b = a - 2b$), always substitute the first number for the first letter and the second number for the second letter in exactly the order they appear. Reversing them will give you the wrong answer unless the operation is commutative.
- **Reading Tables.** When reading a table, the standard convention is that for $a \ast b$, $a$ is taken from the leftmost vertical column and $b$ is taken from the top horizontal row.

## Quick summary

1. A binary operation applies a specific mathematical rule to combine two elements of a set into a single element.
2. An operation is closed if the result of combining any two elements is always found within the original defined set.
3. An operation is commutative if reversing the order does not change the result ($a \ast b = b \ast a$).
4. An operation is associative if changing the position of brackets does not change the final outcome ($(a \ast b) \ast c = a \ast (b \ast c)$).
5. The identity element $e$ is the unique value that satisfies $a \ast e = a$ and $e \ast a = a$. It acts like the number 0 does for standard addition.
6. The inverse element $a^{-1}$ cancels out an element to leave the identity, satisfying $a \ast a^{-1} = e$.
7. Finding an inverse algebraically is always a vital two-step process: you must calculate the identity element $e$ first, and then substitute it into $a \ast a^{-1} = e$ to find the inverse.

## Practice questions

**1. A binary operation $\ast$ on the set of real numbers is defined by $x \ast y = \frac{xy}{2}$. Evaluate $3 \ast (4 \ast 5)$.**

- A. 10
- B. 15
- C. 20
- D. 30

**Answer: B.** 
1. Following the order of operations, evaluate the bracket first: $4 \ast 5$.
2. Using the rule, $4 \ast 5 = \frac{4 \times 5}{2} = \frac{20}{2} = 10$.
3. Substitute this result back into the expression: we now need to evaluate $3 \ast 10$.
4. Using the rule again, $3 \ast 10 = \frac{3 \times 10}{2} = \frac{30}{2} = 15$.
The mistake behind option A is calculating only the bracket and forgetting to evaluate the outer operation with 3.

**2. An operation $\otimes$ is defined by $a \otimes b = a^2 - b^2$. Evaluate $(3 \otimes 2) \otimes 4$.**

- A. -9
- B. 9
- C. 11
- D. -11

**Answer: B.**
1. Evaluate the bracket first: $3 \otimes 2$.
2. Substitute into the rule: $3^2 - 2^2 = 9 - 4 = 5$.
3. Now evaluate the full expression using the result: $5 \otimes 4$.
4. Substitute into the rule: $5^2 - 4^2$.
5. $25 - 16 = 9$.

**3. A binary operation $\oplus$ is defined on the set of integers by $p \oplus q = p + q - 2$. Find the identity element.**

- A. 0
- B. 1
- C. 2
- D. -2

**Answer: C.**
1. The formula for finding the identity element is $p \oplus e = p$.
2. Apply the given rule for $\oplus$ to the left side: $p + e - 2 = p$.
3. Subtract $p$ from both sides to isolate $e$: $e - 2 = 0$.
4. Solve for $e$: $e = 2$.

**4. Using the operation $x \ast y = x + y - 2xy$, find the inverse of $3$.**

- A. $-\frac{3}{5}$
- B. $\frac{3}{5}$
- C. $-\frac{1}{3}$
- D. $\frac{5}{3}$

**Answer: B.**
1. First, find the identity element $e$: set $x \ast e = x$.
2. Apply the rule: $x + e - 2xe = x$. 
3. Subtract $x$ from both sides to get $e - 2xe = 0$. 
4. Factor out $e$: $e(1 - 2x) = 0$. For this to hold for all $x$, $e$ must be $0$.
5. Now, let $y$ be the inverse of 3. Use the inverse rule: $3 \ast y = e$.
6. Since $e = 0$, we have $3 \ast y = 0$.
7. Apply the operation rule to the left side: $3 + y - 2(3)(y) = 0$.
8. Simplify the equation: $3 + y - 6y = 0$.
9. Collect terms: $3 - 5y = 0 \implies 5y = 3 \implies y = \frac{3}{5}$.

**5. A binary operation $\Delta$ is defined by $m \Delta n = m + n + mn$. Which of the following statements is true?**
**I. $\Delta$ is commutative**
**II. $\Delta$ is associative**
**III. The identity element is 0**

- A. I and II only
- B. I and III only
- C. II and III only
- D. I, II and III

**Answer: D.**
1. Commutativity check: $m \Delta n = m+n+mn$. Reversing it gives $n \Delta m = n+m+nm$. Since standard addition and multiplication are commutative, they are equal. Statement I is true.
2. Associativity check: $(m \Delta n) \Delta p = (m+n+mn) \Delta p$. Treat $(m+n+mn)$ as the first term. The rule gives $(m+n+mn) + p + (m+n+mn)p = m+n+p+mn+mp+np+mnp$. 
3. Check the other grouping: $m \Delta (n \Delta p) = m \Delta (n+p+np) = m + (n+p+np) + m(n+p+np) = m+n+p+np+mn+mp+mnp$. The results are algebraically identical, so statement II is true.
4. Identity check: $m \Delta e = m \implies m + e + me = m \implies e + me = 0 \implies e(1+m) = 0 \implies e = 0$. Statement III is true. All statements are correct.

**6. A binary operation $\ast$ is defined on the set of real numbers by $x \ast y = x + y - 4$. Find the inverse of 5.**

- A. 3
- B. 4
- C. -3
- D. 5

**Answer: A.**
1. First, find the identity element $e$: set $x \ast e = x$.
2. Apply the rule: $x + e - 4 = x$.
3. Subtract $x$ from both sides: $e - 4 = 0 \implies e = 4$.
4. Now, find the inverse of 5. Let the inverse be $y$. Set $5 \ast y = e$.
5. Substitute $e = 4$: $5 \ast y = 4$.
6. Apply the operation rule to the left side: $5 + y - 4 = 4$.
7. Simplify: $1 + y = 4 \implies y = 3$.

**7. Which of the following binary operations is NOT commutative on the set of real numbers?**

- A. $a \ast b = a + b - ab$
- B. $a \ast b = \frac{a+b}{ab}$
- C. $a \ast b = a^2 + b^2$
- D. $a \ast b = a - b + ab$

**Answer: D.**
1. An operation is commutative if $a \ast b = b \ast a$. We test each option by swapping the letters.
2. Option A: $b \ast a = b + a - ba$. This rearranges to $a + b - ab$. It is commutative.
3. Option B: $b \ast a = \frac{b+a}{ba}$. This rearranges to $\frac{a+b}{ab}$. It is commutative.
4. Option C: $b \ast a = b^2 + a^2$. This rearranges to $a^2 + b^2$. It is commutative.
5. Option D: $b \ast a = b - a + ba$. Because subtraction is not commutative ($a - b \neq b - a$), this expression is not algebraically equal to $a - b + ab$. Therefore, Option D is not commutative.

**8. A binary operation $\circ$ is defined by $p \circ q = 2p - q$. Evaluate $4 \circ (3 \circ 2)$.**

- A. 4
- B. 6
- C. 8
- D. -4

**Answer: A.**
1. Solve the bracket first: $3 \circ 2$.
2. Substitute $p=3$ and $q=2$ into the rule: $2(3) - 2 = 6 - 2 = 4$.
3. Now evaluate the outer operation using this result: $4 \circ 4$.
4. Substitute $p=4$ and $q=4$ into the rule: $2(4) - 4 = 8 - 4 = 4$.

**9. Find the identity element under the operation $\ast$ defined by $a \ast b = \frac{ab}{3}$, where $a$ and $b$ are non-zero real numbers.**

- A. 1
- B. 3
- C. $\frac{1}{3}$
- D. 0

**Answer: B.**
1. Set up the equation for the identity element: $a \ast e = a$.
2. Apply the operation rule to the left side: $\frac{ae}{3} = a$.
3. Multiply both sides by 3 to clear the fraction: $ae = 3a$.
4. Divide both sides by $a$ (allowed since $a \neq 0$): $e = 3$.

**10. A binary operation on the set of real numbers is defined by $x \ast y = x + y + 3$. Find the inverse of 5.**

- A. -5
- B. 5
- C. -11
- D. -8

**Answer: C.**
1. First, find the identity element $e$: set $x \ast e = x$.
2. Apply the rule: $x + e + 3 = x$. 
3. Subtract $x$ from both sides: $e + 3 = 0 \implies e = -3$.
4. Next, find the inverse of 5. Let the inverse be $y$. Set $5 \ast y = e$.
5. Substitute $e = -3$: $5 \ast y = -3$.
6. Apply the operation rule to the left side: $5 + y + 3 = -3$.
7. Simplify: $y + 8 = -3$.
8. Solve for $y$: $y = -3 - 8 = -11$.
*(The common mistake behind option D is incorrectly assuming the identity element is 0, which would give $y + 8 = 0 \implies y = -8$.)*
