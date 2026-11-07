# JAMB Mathematics Notes: Matrices and Determinants

## What JAMB expects

This topic is Topic 6 of SECTION II: ALGEBRA in the JAMB Mathematics syllabus. It covers the following content items:

* **(a)** algebra of matrices not exceeding $3 \times 3$;
* **(b)** determinants of matrices not exceeding $3 \times 3$;
* **(c)** inverses of $2 \times 2$ matrices;

By the end of these notes, you should be able to:

1. perform basic operations $(\times, +, -, \div)$ on matrices;
2. calculate determinants;
3. compute inverses of $2 \times 2$ matrices.

**Note on the syllabus wording:** The syllabus asks you to perform basic operations $(x, +, -, \div)$ on matrices. The letter "$x$" is a typographical error for the multiplication sign $(\times)$. Furthermore, in strict mathematics, direct division $(\div)$ of one matrix by another is not defined. Instead, "division" is performed by multiplying by the inverse of a matrix (just as dividing by 2 is exactly the same as multiplying by $2^{-1}$, or $\frac{1}{2}$). Also, the syllabus includes a stray note "[excluding quadratic and higher degree equations]". This means that when evaluating determinants to solve for unknown variables in JAMB, you will only be expected to solve linear equations, not quadratic ones.

## Objective i: perform basic operations (x, +, -, ÷) on matrices

### Algebra of matrices not exceeding 3 x 3

A **matrix** (plural: matrices) is a rectangular arrangement of numbers into rows (horizontal lines) and columns (vertical lines), usually enclosed in large curved or square brackets. 

For example, if a trader in Wuse Market sells 3 bags of rice and 2 bags of beans on Monday, and 5 bags of rice and 4 bags of beans on Tuesday, this data can be neatly arranged into a matrix:
$$ \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} $$

* **Element:** Each individual number inside the matrix is called an element.
* **Order (or dimension):** The size of a matrix is given by the number of its rows multiplied by the number of its columns (Rows $\times$ Columns). The matrix above has 2 rows and 2 columns, so its order is $2 \times 2$. A matrix with 3 rows and 2 columns has an order of $3 \times 2$.

### Addition and Subtraction

To add or subtract two matrices, they must have the **exact same order**. If the orders match, you simply add or subtract the numbers in the matching positions (the corresponding elements). If the orders do not match, the matrices cannot be added or subtracted.

**Worked Example 1: Addition and Subtraction of Matrices**

Given $A = \begin{pmatrix} 2 & 3 \\ -1 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 3 & 0 \end{pmatrix}$, find $A + B$ and $A - B$.

**Solution:**

1. For $A + B$, add the elements that share the same positions:
   $$ A + B = \begin{pmatrix} 2+1 & 3+(-2) \\ -1+3 & 4+0 \end{pmatrix} $$
   $$ A + B = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} $$

2. For $A - B$, subtract the corresponding elements:
   $$ A - B = \begin{pmatrix} 2-1 & 3-(-2) \\ -1-3 & 4-0 \end{pmatrix} $$
   $$ A - B = \begin{pmatrix} 1 & 5 \\ -4 & 4 \end{pmatrix} $$

### Scalar Multiplication

A **scalar** is just a single ordinary number (like 2, 5, or -3). To multiply a matrix by a scalar, you multiply every single element inside the matrix by that number.

**Worked Example 2: Scalar Multiplication**

Given $P = \begin{pmatrix} 4 & -3 \\ 2 & 1 \end{pmatrix}$, find $3P$.

**Solution:**

1. Multiply each element inside the matrix $P$ by the scalar 3:
   $$ 3P = \begin{pmatrix} 3 \times 4 & 3 \times -3 \\ 3 \times 2 & 3 \times 1 \end{pmatrix} $$
2. Simplify to get the final matrix:
   $$ 3P = \begin{pmatrix} 12 & -9 \\ 6 & 3 \end{pmatrix} $$

### Matrix Multiplication (x)

Multiplying two matrices is entirely different from addition or scalar multiplication. You do not just multiply corresponding elements. Instead, you multiply the **rows of the first matrix by the columns of the second matrix**.

* **The Rule for Multiplication:** Two matrices can only be multiplied if the number of **columns** in the first matrix equals the number of **rows** in the second matrix.
* **Important:** In matrix algebra, the order of multiplication matters. $AB$ is generally **not equal** to $BA$. Matrix multiplication is not commutative.

[IMAGE: A colourful diagram illustrating matrix multiplication of two 2x2 matrices. On the left, the first matrix has its first row highlighted with a red box and an arrow pointing to the right. The second matrix has its first column highlighted with a blue box and an arrow pointing down. On the right side of the equals sign, the resulting matrix shows the calculation for the top-left element as a combination of the red row's numbers and the blue column's numbers linked by multiplication and addition signs. Labels to add later: "Row 1", "Column 1", "Multiply matching elements and add", "Result goes in Row 1, Column 1". Clean flat textbook style, white background.]

**Worked Example 3: Multiplying $2 \times 2$ matrices**

Given $A = \begin{pmatrix} 2 & 3 \\ -1 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 3 & 0 \end{pmatrix}$, find the product $AB$.

**Solution:**

1. To find the element in Row 1, Col 1 of the answer: multiply Row 1 of $A$ by Col 1 of $B$:
   $$ (2 \times 1) + (3 \times 3) = 2 + 9 = 11 $$
2. To find the element in Row 1, Col 2: multiply Row 1 of $A$ by Col 2 of $B$:
   $$ (2 \times -2) + (3 \times 0) = -4 + 0 = -4 $$
3. To find the element in Row 2, Col 1: multiply Row 2 of $A$ by Col 1 of $B$:
   $$ (-1 \times 1) + (4 \times 3) = -1 + 12 = 11 $$
4. To find the element in Row 2, Col 2: multiply Row 2 of $A$ by Col 2 of $B$:
   $$ (-1 \times -2) + (4 \times 0) = 2 + 0 = 2 $$
5. Put them all together into a new $2 \times 2$ matrix:
   $$ AB = \begin{pmatrix} 11 & -4 \\ 11 & 2 \end{pmatrix} $$

**Worked Example 4: Multiplying $3 \times 3$ matrices**

Given $C = \begin{pmatrix} 1 & 2 & 0 \\ -1 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$ and $D = \begin{pmatrix} 2 & 0 & -1 \\ 1 & 1 & 1 \\ -2 & 3 & 0 \end{pmatrix}$, find the product $CD$.

**Solution:**

We use the same row-by-column method, but now with three elements to multiply and add each time.

1. Find the elements of the first row of $CD$:
   - Row 1, Col 1: $(1 \times 2) + (2 \times 1) + (0 \times -2) = 2 + 2 + 0 = 4$
   - Row 1, Col 2: $(1 \times 0) + (2 \times 1) + (0 \times 3) = 0 + 2 + 0 = 2$
   - Row 1, Col 3: $(1 \times -1) + (2 \times 1) + (0 \times 0) = -1 + 2 + 0 = 1$
2. Find the elements of the second row of $CD$:
   - Row 2, Col 1: $(-1 \times 2) + (3 \times 1) + (1 \times -2) = -2 + 3 - 2 = -1$
   - Row 2, Col 2: $(-1 \times 0) + (3 \times 1) + (1 \times 3) = 0 + 3 + 3 = 6$
   - Row 2, Col 3: $(-1 \times -1) + (3 \times 1) + (1 \times 0) = 1 + 3 + 0 = 4$
3. Find the elements of the third row of $CD$:
   - Row 3, Col 1: $(0 \times 2) + (1 \times 1) + (2 \times -2) = 0 + 1 - 4 = -3$
   - Row 3, Col 2: $(0 \times 0) + (1 \times 1) + (2 \times 3) = 0 + 1 + 6 = 7$
   - Row 3, Col 3: $(0 \times -1) + (1 \times 1) + (2 \times 0) = 0 + 1 + 0 = 1$
4. Combine the results into a single $3 \times 3$ matrix:
   $$ CD = \begin{pmatrix} 4 & 2 & 1 \\ -1 & 6 & 4 \\ -3 & 7 & 1 \end{pmatrix} $$

> **Common mistake:** In an exam rush, many students wrongly multiply matrices term-by-term (multiplying the top-left element by the top-left element, and so on). This is incorrect for matrix multiplication. Always use the row-by-column method!

## Objective ii: calculate determinants

### Determinants of matrices not exceeding 3 x 3

The **determinant** of a square matrix $A$ is a single numerical value calculated from its elements. It is widely used in algebra to find inverses and solve systems of linear equations. It is written as $|A|$ or $\det(A)$. Note that straight vertical lines, like $|A|$, mean determinant, whereas large brackets like $\begin{pmatrix} \end{pmatrix}$ mean the matrix itself.

#### Determinant of a $2 \times 2$ matrix

For a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the formula is:
$$ |A| = ad - bc $$
You multiply the elements on the main diagonal (top-left to bottom-right, $a \times d$) and subtract the product of the elements on the other diagonal (top-right to bottom-left, $b \times c$).

**Worked Example 5: Finding a $2 \times 2$ determinant**

Find the determinant of $M = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$.

**Solution:**

1. Multiply the main diagonal elements: $3 \times 2 = 6$.
2. Multiply the other diagonal elements: $5 \times 1 = 5$.
3. Subtract the second product from the first:
   $$ |M| = 6 - 5 = 1 $$

**Worked Example 6: Unknowns in a determinant**

If $\begin{vmatrix} x & 2 \\ 4 & 5 \end{vmatrix} = 7$, find the value of $x$.

**Solution:**

1. Expand the determinant algebraically by taking the difference of the diagonal products:
   $$ (x \times 5) - (2 \times 4) = 5x - 8 $$
2. Set the expanded expression equal to 7 as given in the problem:
   $$ 5x - 8 = 7 $$
3. Solve the resulting linear equation for $x$:
   $$ 5x = 15 \implies x = 3 $$

#### Determinant of a $3 \times 3$ matrix

To find the determinant of a $3 \times 3$ matrix, we expand it along the first row using smaller $2 \times 2$ matrices called **minors**. We assign alternating signs to the positions in the first row: $+$, $-$, $+$.

For $A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$, the determinant is:
$$ |A| = a\begin{vmatrix} e & f \\ h & i \end{vmatrix} - b\begin{vmatrix} d & f \\ g & i \end{vmatrix} + c\begin{vmatrix} d & e \\ g & h \end{vmatrix} $$

For each element in the top row, you cross out its row and its column, and multiply the element by the $2 \times 2$ determinant that remains.

[IMAGE: A diagram showing the expansion of a 3x3 matrix determinant along the top row. The top row has '+, -, +' written above its elements. Three smaller 2x2 matrices are shown, each multiplied by an element from the top row. The first element is highlighted, and its corresponding row and column are crossed out with light grey lines, leaving the 2x2 matrix that it is multiplied by. Labels to add later: "+, -, + alternating signs", "Cross out row and column", "Multiply by remaining 2x2 determinant". Clean flat textbook style, white background.]

**Worked Example 7: Finding a $3 \times 3$ determinant**

Evaluate the determinant of $E = \begin{pmatrix} 2 & 1 & 3 \\ -1 & 2 & 4 \\ 0 & -3 & 1 \end{pmatrix}$.

**Solution:**

1. The top row is 2, 1, 3. The alternating signs are $+$, $-$, $+$. We set up the expansion:
   $$ |E| = +2\begin{vmatrix} 2 & 4 \\ -3 & 1 \end{vmatrix} - 1\begin{vmatrix} -1 & 4 \\ 0 & 1 \end{vmatrix} + 3\begin{vmatrix} -1 & 2 \\ 0 & -3 \end{vmatrix} $$
2. Calculate the value for the first term (2):
   - The $2 \times 2$ determinant is $(2 \times 1) - (4 \times -3) = 2 - (-12) = 14$.
   - Multiply by $+2$: $+2 \times 14 = 28$.
3. Calculate the value for the second term (1):
   - The $2 \times 2$ determinant is $(-1 \times 1) - (4 \times 0) = -1 - 0 = -1$.
   - Multiply by $-1$: $-1 \times -1 = 1$.
4. Calculate the value for the third term (3):
   - The $2 \times 2$ determinant is $(-1 \times -3) - (2 \times 0) = 3 - 0 = 3$.
   - Multiply by $+3$: $+3 \times 3 = 9$.
5. Add the results together:
   $$ |E| = 28 + 1 + 9 = 38 $$

## Objective iii: compute inverses of 2 x 2 matrices

### Inverses of 2 x 2 matrices

The **inverse** of a square matrix $A$, written as $A^{-1}$, is a matrix that, when multiplied by $A$, gives the **Identity matrix** $I$. The Identity matrix acts just like the number 1 does in regular arithmetic. For a $2 \times 2$ matrix, $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, and $AA^{-1} = I$.

#### Formula for the inverse of a $2 \times 2$ matrix

If $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, its inverse is given by the formula:
$$ A^{-1} = \frac{1}{|A|} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$

**Steps to find the inverse:**
1. Find the determinant: $|A| = ad - bc$.
2. Form the **adjoint** matrix: swap the positions of $a$ and $d$ (the main diagonal), and reverse the signs of $b$ and $c$ (the other diagonal).
3. Multiply the adjoint matrix by the scalar fraction $\frac{1}{|A|}$.

**Worked Example 8: Finding the inverse of a $2 \times 2$ matrix**

Find the inverse of $A = \begin{pmatrix} 4 & -2 \\ 3 & 1 \end{pmatrix}$.

**Solution:**

1. Find the determinant:
   $$ |A| = (4 \times 1) - (-2 \times 3) = 4 - (-6) = 4 + 6 = 10 $$
2. Find the adjoint matrix by swapping 4 and 1, and changing the signs of -2 and 3:
   $$ \text{Adjoint} = \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix} $$
3. Multiply the adjoint by the reciprocal of the determinant $\left(\frac{1}{|A|}\right)$:
   $$ A^{-1} = \frac{1}{10} \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix} = \begin{pmatrix} \frac{1}{10} & \frac{1}{5} \\ -\frac{3}{10} & \frac{2}{5} \end{pmatrix} $$

*(Note: In many JAMB options, the answer is left with the fraction $\frac{1}{10}$ sitting outside the matrix).*

### Singular Matrices

If the determinant $|A| = 0$, then the inverse formula asks you to divide by zero $\left(\frac{1}{0}\right)$, which is mathematically impossible. A matrix with a determinant of exactly zero is called a **singular matrix**, and **it does not have an inverse**. 

**Worked Example 9: Singular matrix condition**

For what value of $k$ is the matrix $P = \begin{pmatrix} 3 & k \\ 2 & 8 \end{pmatrix}$ a singular matrix?

**Solution:**

1. We know a matrix is singular if its determinant is exactly 0.
2. Find the expression for $|P|$ using the determinant rule:
   $$ (3 \times 8) - (k \times 2) = 24 - 2k $$
3. Set $|P| = 0$ and solve for $k$:
   $$ 24 - 2k = 0 $$
   $$ 2k = 24 \implies k = 12 $$

### Matrix "Division" (÷): Solving $AX = B$

If an equation is given as $AX = B$ (where $A$ and $B$ are known matrices, and you want to find the unknown matrix $X$), you isolate $X$ by "dividing" by $A$. In matrix algebra, this division is carried out by multiplying both sides by the inverse of $A$, $A^{-1}$. 

Because matrix multiplication order matters, you must multiply by $A^{-1}$ from the **left side** on both sides of the equation:
$$ A^{-1} (AX) = A^{-1} B \implies X = A^{-1} B $$

**Worked Example 10: Matrix Algebra (Division by inverse)**

Given $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ and $AX = \begin{pmatrix} 4 & -1 \\ 2 & 0 \end{pmatrix}$, find $X$.

**Solution:**

1. To find $X$, we must compute $X = A^{-1} B$, where $B = \begin{pmatrix} 4 & -1 \\ 2 & 0 \end{pmatrix}$.
2. First, find $A^{-1}$:
   - Determinant $|A| = (2 \times 3) - (1 \times 5) = 6 - 5 = 1$.
   - Adjoint of $A = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
   - Since $|A| = 1$, the inverse is identical to the adjoint:
     $$ A^{-1} = \frac{1}{1} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} $$
3. Next, multiply $A^{-1}$ by $B$:
   $$ X = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \begin{pmatrix} 4 & -1 \\ 2 & 0 \end{pmatrix} $$
4. Perform row-by-column multiplication:
   - Row 1, Col 1: $(3 \times 4) + (-1 \times 2) = 12 - 2 = 10$
   - Row 1, Col 2: $(3 \times -1) + (-1 \times 0) = -3 - 0 = -3$
   - Row 2, Col 1: $(-5 \times 4) + (2 \times 2) = -20 + 4 = -16$
   - Row 2, Col 2: $(-5 \times -1) + (2 \times 0) = 5 + 0 = 5$
5. Put the answers into the final matrix:
   $$ X = \begin{pmatrix} 10 & -3 \\ -16 & 5 \end{pmatrix} $$

> **Common mistake:** When asked to solve $AX = B$, a common error is calculating $X = B A^{-1}$ instead of $X = A^{-1} B$. Because $A$ sits on the left of $X$, its inverse must multiply $B$ from the left.

## Key terms

| Term | Meaning |
| --- | --- |
| **Matrix** | A rectangular array of numbers arranged into rows and columns. |
| **Order/Dimension** | The size of a matrix, stated as (Number of Rows) $\times$ (Number of Columns). |
| **Element** | A single number found inside a matrix. |
| **Determinant** | A special scalar value calculated from a square matrix, written as $|A|$. |
| **Minor** | The smaller determinant left behind after crossing out a row and column during a $3 \times 3$ determinant expansion. |
| **Adjoint** | For a $2 \times 2$ matrix, the result of swapping the main diagonal elements and negating the others. |
| **Inverse** | The matrix $A^{-1}$ which, when multiplied by $A$, gives the Identity matrix. |
| **Identity matrix ($I$)** | A matrix with 1s on the main diagonal and 0s elsewhere. Multiplying by it leaves a matrix unchanged ($AI = A$). |
| **Singular matrix** | A matrix whose determinant is exactly 0. It has no inverse. |
| **Scalar** | A single ordinary number that can be used to multiply an entire matrix. |

## Exam tips and common mistakes

* **Matrix multiplication order is strict:** Always do row-by-column multiplication. Remember that $AB$ is not the same as $BA$.
* **Do not divide directly:** If you see an equation like $AX = B$, find the inverse of $A$ and compute $A^{-1} B$. Never put $A^{-1}$ on the right side of $B$.
* **Check your signs in determinants:** In a $2 \times 2$ determinant, you subtract the second product. For example, $(4 \times 1) - (-2 \times 3) = 4 - (-6) = 10$. Beware of minus signs turning into plus signs.
* **Expanding $3 \times 3$ determinants:** Do not forget the alternating signs for the top row: **$+$, $-$, $+$**. The middle term must be multiplied by a negative.
* **Finding the adjoint:** Remember the simple rule for $2 \times 2$ inverses: Swap the main diagonal elements, and change the signs of the other diagonal elements. Do not mix this up.
* **Singular matrix shortcut:** If a JAMB question says a matrix is singular, immediately write an equation setting its determinant to zero.

## Quick summary

1. A matrix is an array of numbers structured in rows and columns; its order is given as Rows $\times$ Columns.
2. Matrices can only be added or subtracted if they share the exact same order, which is done by adding/subtracting corresponding elements.
3. Multiplying by a scalar means multiplying every single element inside the matrix by that number.
4. Matrix multiplication uses a row-by-column method. You can only multiply if the number of columns in the first equals the number of rows in the second.
5. The determinant of a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is calculated as $ad - bc$.
6. A singular matrix has a determinant of 0 and cannot be inverted.
7. The inverse of a $2 \times 2$ matrix is found by swapping the main diagonal elements, reversing the signs of the off-diagonal elements, and multiplying by $\frac{1}{|A|}$.
8. To "divide" by a matrix in an equation like $AX = B$, you multiply both sides by the inverse, obtaining $X = A^{-1} B$.

## Practice questions

**1. Given $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 5 & -1 \\ 0 & 2 \end{pmatrix}$, evaluate $A + 2B$.**

- A. $\begin{pmatrix} 11 & 0 \\ 3 & 8 \end{pmatrix}$
- B. $\begin{pmatrix} 6 & 1 \\ 3 & 6 \end{pmatrix}$
- C. $\begin{pmatrix} 11 & 1 \\ 3 & 6 \end{pmatrix}$
- D. $\begin{pmatrix} -9 & 4 \\ 3 & 0 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. Find $2B$ by multiplying each element in $B$ by 2:
   $$ 2B = \begin{pmatrix} 10 & -2 \\ 0 & 4 \end{pmatrix} $$
2. Add corresponding elements of $A$ and $2B$:
   $$ A + 2B = \begin{pmatrix} 1+10 & 2+(-2) \\ 3+0 & 4+4 \end{pmatrix} $$
3. Simplify the result:
   $$ \begin{pmatrix} 11 & 0 \\ 3 & 8 \end{pmatrix} $$
4. Option B is the common mistake of simply adding $A + B$ without multiplying $B$ by 2 first.

**2. If $P = \begin{pmatrix} 4 & -3 \\ 2 & 1 \end{pmatrix}$ and $Q = \begin{pmatrix} -1 & 5 \\ 0 & 2 \end{pmatrix}$, find $3P - 2Q$.**

- A. $\begin{pmatrix} 14 & -19 \\ 6 & -1 \end{pmatrix}$
- B. $\begin{pmatrix} 10 & -19 \\ 6 & -1 \end{pmatrix}$
- C. $\begin{pmatrix} 14 & 1 \\ 6 & 7 \end{pmatrix}$
- D. $\begin{pmatrix} 14 & -19 \\ 6 & 1 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. Multiply $P$ by 3:
   $$ 3P = \begin{pmatrix} 12 & -9 \\ 6 & 3 \end{pmatrix} $$
2. Multiply $Q$ by 2:
   $$ 2Q = \begin{pmatrix} -2 & 10 \\ 0 & 4 \end{pmatrix} $$
3. Subtract $2Q$ from $3P$:
   $$ \begin{pmatrix} 12 - (-2) & -9 - 10 \\ 6 - 0 & 3 - 4 \end{pmatrix} $$
4. Simplify to get the answer:
   $$ \begin{pmatrix} 14 & -19 \\ 6 & -1 \end{pmatrix} $$
5. Option B is a common mistake resulting from evaluating $12 - 2$ instead of $12 - (-2)$.

**3. Given $X = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$ and $Y = \begin{pmatrix} 0 & 4 \\ -2 & 1 \end{pmatrix}$, evaluate the product $XY$.**

- A. $\begin{pmatrix} 2 & 7 \\ -6 & 7 \end{pmatrix}$
- B. $\begin{pmatrix} 0 & -4 \\ -2 & 3 \end{pmatrix}$
- C. $\begin{pmatrix} -2 & 7 \\ 6 & 7 \end{pmatrix}$
- D. $\begin{pmatrix} 4 & 12 \\ -3 & 5 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. Multiply Row 1 of $X$ by Col 1 of $Y$: $(2 \times 0) + (-1 \times -2) = 0 + 2 = 2$.
2. Multiply Row 1 of $X$ by Col 2 of $Y$: $(2 \times 4) + (-1 \times 1) = 8 - 1 = 7$.
3. Multiply Row 2 of $X$ by Col 1 of $Y$: $(1 \times 0) + (3 \times -2) = 0 - 6 = -6$.
4. Multiply Row 2 of $X$ by Col 2 of $Y$: $(1 \times 4) + (3 \times 1) = 4 + 3 = 7$.
5. Combine to form the resulting matrix:
   $$ XY = \begin{pmatrix} 2 & 7 \\ -6 & 7 \end{pmatrix} $$
6. Option D is the result of computing $YX$. Matrix multiplication is not commutative.

**4. If $\begin{vmatrix} x & 2 \\ 4 & 5 \end{vmatrix} = 7$, find the value of $x$.**

- A. 3
- B. 15
- C. $-\frac{1}{5}$
- D. 0

**Answer: A.** The correct step-by-step working is as follows:

1. Calculate the determinant using the formula (main diagonal minus other diagonal):
   $$ (x \times 5) - (2 \times 4) = 5x - 8 $$
2. Set the expanded determinant equal to the given value (7):
   $$ 5x - 8 = 7 $$
3. Add 8 to both sides of the equation:
   $$ 5x = 15 $$
4. Divide by 5 to solve for $x$:
   $$ x = 3 $$
5. Option C results from accidentally adding instead of subtracting the diagonals, yielding $5x + 8 = 7$.

**5. For what value of $k$ is the matrix $\begin{pmatrix} 3 & k \\ 2 & 8 \end{pmatrix}$ a singular matrix?**

- A. 12
- B. -12
- C. 6
- D. 24

**Answer: A.** The correct step-by-step working is as follows:

1. Recall that a matrix is singular if its determinant equals exactly 0.
2. Find the determinant expression:
   $$ (3 \times 8) - (k \times 2) = 24 - 2k $$
3. Set the determinant equal to zero:
   $$ 24 - 2k = 0 $$
4. Solve for $k$:
   $$ 2k = 24 \implies k = 12 $$
5. Option B happens if a student mistakenly writes the determinant sum as $24 + 2k = 0$.

**6. Evaluate the determinant of the matrix $\begin{pmatrix} 1 & 0 & 2 \\ 3 & -1 & 4 \\ 2 & 1 & 5 \end{pmatrix}$.**

- A. 1
- B. -1
- C. 9
- D. 19

**Answer: A.** The correct step-by-step working is as follows:

1. Expand the determinant along the first row with alternating signs $(+, -, +)$:
   $$ |M| = 1\begin{vmatrix} -1 & 4 \\ 1 & 5 \end{vmatrix} - 0\begin{vmatrix} 3 & 4 \\ 2 & 5 \end{vmatrix} + 2\begin{vmatrix} 3 & -1 \\ 2 & 1 \end{vmatrix} $$
2. Calculate the smaller $2 \times 2$ determinants:
   - For the first: $(-1 \times 5) - (4 \times 1) = -5 - 4 = -9$.
   - For the second: It multiplies by $0$, so it equals $0$.
   - For the third: $(3 \times 1) - (-1 \times 2) = 3 - (-2) = 5$.
3. Substitute these values back:
   $$ |M| = 1(-9) - 0 + 2(5) $$
4. Simplify the expression:
   $$ |M| = -9 + 10 = 1 $$
5. Option B ($-1$) results from calculating each $2 \times 2$ determinant backwards, as $bc - ad$ instead of $ad - bc$: $1(9) - 0 + 2(-5) = -1$.

**7. What is the inverse of the matrix $\begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$?**

- A. $\begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$
- B. $\begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$
- C. $\begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$
- D. $\begin{pmatrix} -2 & 5 \\ 1 & -3 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. Calculate the determinant:
   $$ |A| = (3 \times 2) - (5 \times 1) = 6 - 5 = 1 $$
2. Find the adjoint matrix by swapping the main diagonal elements (3 and 2) and reversing the signs of the off-diagonal elements (5 and 1):
   $$ \text{Adjoint} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} $$
3. Multiply the adjoint by the reciprocal of the determinant $\left(\frac{1}{1}\right)$:
   $$ A^{-1} = 1 \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix} $$
4. Option B is incorrect because the diagonal elements were swapped but the signs of the off-diagonal elements ($5$ and $1$) were not changed.

**8. The inverse of $\begin{pmatrix} 4 & -2 \\ 3 & 1 \end{pmatrix}$ is:**

- A. $\frac{1}{10} \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix}$
- B. $\frac{1}{10} \begin{pmatrix} 4 & 2 \\ -3 & 1 \end{pmatrix}$
- C. $\frac{1}{2} \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix}$
- D. $-\frac{1}{2} \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. Calculate the determinant:
   $$ |A| = (4 \times 1) - (-2 \times 3) = 4 - (-6) = 10 $$
2. Form the adjoint matrix (swap 4 and 1, change the signs of -2 and 3):
   $$ \text{Adjoint} = \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix} $$
3. Multiply the adjoint by $\frac{1}{|A|}$:
   $$ A^{-1} = \frac{1}{10} \begin{pmatrix} 1 & 2 \\ -3 & 4 \end{pmatrix} $$
4. Option D results from a sign error in the determinant ($4 - 6 = -2$, giving the multiplier $-\frac{1}{2}$). Option C is the same error with the sign of the multiplier dropped.

**9. If $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ and $AX = \begin{pmatrix} 4 & -1 \\ 2 & 0 \end{pmatrix}$, find matrix $X$.**

- A. $\begin{pmatrix} 10 & -3 \\ -16 & 5 \end{pmatrix}$
- B. $\begin{pmatrix} 17 & -6 \\ 6 & -2 \end{pmatrix}$
- C. $\begin{pmatrix} 12 & -3 \\ -20 & 5 \end{pmatrix}$
- D. $\begin{pmatrix} -10 & 3 \\ 16 & -5 \end{pmatrix}$

**Answer: A.** The correct step-by-step working is as follows:

1. To isolate $X$ in $AX = B$, multiply both sides by $A^{-1}$ from the left, giving $X = A^{-1} B$.
2. Find the determinant of $A$: $(2 \times 3) - (1 \times 5) = 1$.
3. Find $A^{-1}$:
   $$ A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} $$
4. Multiply $A^{-1}$ by matrix $B$:
   $$ X = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \begin{pmatrix} 4 & -1 \\ 2 & 0 \end{pmatrix} $$
5. Compute the product:
   - Row 1, Col 1: $12 - 2 = 10$
   - Row 1, Col 2: $-3 + 0 = -3$
   - Row 2, Col 1: $-20 + 4 = -16$
   - Row 2, Col 2: $5 + 0 = 5$
   $$ X = \begin{pmatrix} 10 & -3 \\ -16 & 5 \end{pmatrix} $$
6. Option B is obtained by wrongly computing $X = B A^{-1}$. Order matters!

**10. If $\begin{vmatrix} x & 0 & 1 \\ 2 & 1 & -1 \\ 1 & 2 & 3 \end{vmatrix} = 8$, find the value of $x$.**

- A. 1
- B. -1
- C. $\frac{11}{5}$
- D. 5

**Answer: A.** The correct step-by-step working is as follows:

1. Expand the determinant algebraically along the first row:
   $$ x\begin{vmatrix} 1 & -1 \\ 2 & 3 \end{vmatrix} - 0\begin{vmatrix} 2 & -1 \\ 1 & 3 \end{vmatrix} + 1\begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix} = 8 $$
2. Calculate the smaller $2 \times 2$ determinants:
   - First minor: $(1 \times 3) - (-1 \times 2) = 3 - (-2) = 5$.
   - Third minor: $(2 \times 2) - (1 \times 1) = 4 - 1 = 3$.
3. Substitute these values back into the expression:
   $$ x(5) - 0 + 1(3) = 8 $$
4. Simplify and solve the linear equation:
   $$ 5x + 3 = 8 $$
   $$ 5x = 5 \implies x = 1 $$
5. Option C results from miscalculating the sign on the 3, arriving at $5x - 3 = 8$.
