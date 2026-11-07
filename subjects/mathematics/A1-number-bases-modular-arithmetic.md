# JAMB Mathematics Notes: Number bases/Modular Arithmetic

## What JAMB expects

This file covers Section I, Topic 1 of the JAMB Mathematics syllabus: Number bases/Modular Arithmetic. It covers the following content items:
- **(a)** operations in different number bases from $2$ to $10$;
- **(b)** conversion from one base to another including fractional parts;
- **(c)** modular arithmetic.

By the end of these notes, you should be able to:
1. perform four basic operations $(\times, +, -, \div)$;
2. convert one base to another;
3. perform operations in modulo arithmetic.

**Note on the syllabus wording:** In the original syllabus, the letter "x" is printed in place of the standard multiplication sign ($\times$) for the basic operations, and the division symbol is printed as $\div$. We use the correct mathematical symbols in these notes.

## Conversion between number bases

**Content (b): conversion from one base to another including fractional parts.**
**Objective ii: convert one base to another.**

A number base is a system of counting that uses a specific number of digits. The base we use in everyday life is base $10$ (the decimal system), which uses ten digits: $0, 1, 2, 3, 4, 5, 6, 7, 8$ and $9$. 
Other systems use different numbers of digits. For example, base $2$ (binary) uses only two digits: $0$ and $1$. Base $5$ uses five digits: $0, 1, 2, 3$ and $4$. **You can never have a digit that is equal to or greater than the base itself.**

### 1. Converting from any base to base 10
To convert a number from any base to base $10$, we expand the number using the place value of each digit. The place values are powers of the base. For the whole number part, the powers start at $0$ from the rightmost digit and increase to the left. 

**Worked Example 1: Convert $124_5$ to base 10.**
1. Write out the number and assign powers of the base ($5$) from right to left, starting at $0$.
   $$1 \times 5^2 + 2 \times 5^1 + 4 \times 5^0$$
2. Expand the powers: $5^2 = 25$, $5^1 = 5$, and remember that any non-zero number to the power of $0$ is $1$ ($5^0 = 1$).
   $$1(25) + 2(5) + 4(1)$$
3. Multiply and add the results.
   $$25 + 10 + 4 = 39_{10}$$

#### Fractional parts in other bases
When a number has a decimal point (a fractional part), the powers of the base continue to the right of the point, but they become negative: $-1, -2, -3,$ etc. 

[IMAGE: A diagram showing the place values of a base-2 number: 1101.11. Above each digit is its place value power: 2^3, 2^2, 2^1, 2^0, then a decimal point, then 2^-1, 2^-2. Below each digit is its base-10 value: 8, 4, 2, 1, point, 0.5, 0.25. Clean flat textbook style, white background.]

**Worked Example 2: Convert $1101.11_2$ to base 10.**
1. Assign powers. For digits to the left of the point, start from $0$ and increase to the left. For digits to the right, start from $-1$ and decrease to the right.
   $$1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 1 \times 2^{-2}$$
2. Expand the powers.
   $$8 + 4 + 0 + 1 + \frac{1}{2} + \frac{1}{4}$$
3. Convert the fractions to decimals (or common fractions) and sum them up.
   $$13 + 0.5 + 0.25 = 13.75_{10}$$

### 2. Converting from base 10 to another base
To convert a whole number from base $10$ to another base, we use the **successive division** method. We divide the number repeatedly by the new base and write down the remainders, until the quotient becomes $0$.

**Worked Example 3: Convert $45_{10}$ to base 8.**
1. Set up a successive division table, dividing by the new base ($8$) and recording the remainders.
   $$45 \div 8 = 5 \text{ remainder } 5$$
   $$5 \div 8 = 0 \text{ remainder } 5$$
2. Read the remainders **upwards** (from the last division to the first).
3. The result is $55_8$.

[IMAGE: A successive division table converting 45 to base 8. It shows three columns: the divisor (8) on the left, the quotients down the middle (45, then 5, then 0), and the remainders on the right (5, 5). A bold arrow points upwards from the bottom remainder to the top, labelled "Read upwards". Clean flat textbook style, white background.]

#### Converting base 10 fractional parts
To convert a base $10$ fraction to another base, use **successive multiplication**. Multiply the fractional part by the new base, record the integer (whole number) part, and repeat the process with the new fractional part.

**Worked Example 4: Convert $45.75_{10}$ to base 2.**
1. Split the number into the whole number part ($45$) and the fractional part ($0.75$).
2. Convert the whole number ($45$) to base $2$ by successive division.
   $45 \div 2 = 22$ remainder $1$
   $22 \div 2 = 11$ remainder $0$
   $11 \div 2 = 5$ remainder $1$
   $5 \div 2 = 2$ remainder $1$
   $2 \div 2 = 1$ remainder $0$
   $1 \div 2 = 0$ remainder $1$
   Read upwards: $45_{10} = 101101_2$.
3. Convert the fractional part ($0.75$) to base $2$ by successive multiplication.
   $0.75 \times 2 = 1.50 \rightarrow$ record whole number **$1$**
   Take the new fractional part ($0.50$) and multiply by $2$.
   $0.50 \times 2 = 1.00 \rightarrow$ record whole number **$1$**
   The fractional part is now $0$, so we stop. 
   For fractions, read the recorded whole numbers **downwards** (from first to last): $0.75_{10} = 0.11_2$.
4. Combine the two parts.
   $$45.75_{10} = 101101.11_2$$

### 3. Converting between two non-base-10 bases
To convert a number from one base to another (when neither is base $10$), you must use a two-step process:
- **Step 1:** Convert the number to base $10$.
- **Step 2:** Convert the result from base $10$ to the new base.

**Worked Example 5: Convert $342_5$ to base 6.**
1. **Convert to base $10$:**
   $$3 \times 5^2 + 4 \times 5^1 + 2 \times 5^0$$
   $$3(25) + 4(5) + 2(1) = 75 + 20 + 2 = 97_{10}$$
2. **Convert $97_{10}$ to base $6$:**
   $97 \div 6 = 16$ remainder $1$
   $16 \div 6 = 2$ remainder $4$
   $2 \div 6 = 0$ remainder $2$
   Read upwards: $241_6$.
3. The result is $241_6$.

### 4. Solving equations involving number bases
JAMB often sets equations where the base itself is an unknown variable $x$. Always convert both sides of the equation to base $10$ and solve for $x$.

**Worked Example 6: Find $x$ if $42_x = 26_8$.**
1. Convert both sides to base $10$.
   $$4 \times x^1 + 2 \times x^0 = 2 \times 8^1 + 6 \times 8^0$$
2. Simplify the terms.
   $$4x + 2(1) = 2(8) + 6(1)$$
   $$4x + 2 = 16 + 6$$
   $$4x + 2 = 22$$
3. Solve for $x$.
   $$4x = 20$$
   $$x = 5$$

> **Common mistakes in conversion:** 
> - Reading remainders downwards instead of upwards when converting whole numbers from base 10 (wrong: for $35_{10}$ the remainders, read downwards, give $110001_2$; correct: read upwards to get $100011_2$).
> - Forgetting that any number to the power of $0$ is $1$, not $0$. (e.g., $4 \times 5^0$ is $4 \times 1 = 4$, not $4 \times 0 = 0$).

## Operations in different number bases

**Content (a): operations in different number bases from 2 to 10.**
**Objective i: perform four basic operations ($\times, +, -, \div$).**

You can perform arithmetic directly in any base. The golden rule is: **you carry over or borrow in bundles of the base you are working in.** For example, in base $10$, you carry over tens. In base $5$, you carry over fives. 

### 1. Addition
When adding, if the sum in a column equals or exceeds the base, divide it by the base. Write down the remainder and carry over the quotient to the next column.

**Worked Example 7: Evaluate $341_5 + 124_5$.**
1. Set it up in columns:
   $$ \begin{array}{r@{\quad}l} 341 \\ + 124 \\ \hline \end{array} $$
2. Right column: $1 + 4 = 5$. Since $5 \div 5 = 1$ remainder $0$, write $0$ and carry $1$.
3. Middle column: $4 + 2 + 1 \text{ (carry)} = 7$. Since $7 \div 5 = 1$ remainder $2$, write $2$ and carry $1$.
4. Left column: $3 + 1 + 1 \text{ (carry)} = 5$. Since $5 \div 5 = 1$ remainder $0$, write $0$ and carry $1$. Bring down the $1$.
5. The result is $1020_5$.

**Worked Example 8: Evaluate $1011_2 + 1101_2$.**
1. Set it up:
   $$ \begin{array}{r@{\quad}l} 1011 \\ + 1101 \\ \hline \end{array} $$
2. Column 1 (right): $1 + 1 = 2$. In base $2$, $2 = 10_2$. Write $0$, carry $1$.
3. Column 2: $1 + 0 + 1 \text{ (carry)} = 2$. Write $0$, carry $1$.
4. Column 3: $0 + 1 + 1 \text{ (carry)} = 2$. Write $0$, carry $1$.
5. Column 4 (left): $1 + 1 + 1 \text{ (carry)} = 3$. In base $2$, $3 \div 2 = 1$ remainder $1$. Write $1$, carry $1$. Bring down the final $1$.
6. The result is $11000_2$.

### 2. Subtraction
When subtracting, if a top digit is smaller than the bottom digit, you must borrow $1$ from the next column to the left. **The $1$ you borrow is worth the value of the base.** 

**Worked Example 9: Evaluate $1211_5 - 432_5$.**
1. Set it up:
   $$ \begin{array}{r@{\quad}l} 1211 \\ - 0432 \\ \hline \end{array} $$
2. Column 1 (right): $1 - 2$. Cannot subtract. Borrow $1$ from the next column (the $1$ becomes $0$). The borrowed $1$ is worth $5$. $5 + 1 = 6$. Now, $6 - 2 = 4$.
3. Column 2: Now $0 - 3$. Cannot subtract. Borrow $1$ from the next column (the $2$ becomes $1$). The borrowed $1$ is worth $5$. $5 + 0 = 5$. Now, $5 - 3 = 2$.
4. Column 3: Now $1 - 4$. Cannot subtract. Borrow $1$ from the left column (the $1$ becomes $0$). The borrowed $1$ is worth $5$. $5 + 1 = 6$. Now, $6 - 4 = 2$.
5. The result is $224_5$.

### 3. Multiplication
Multiply as you would in base $10$, but convert every product to the given base before writing it down.

**Worked Example 10: Evaluate $23_4 \times 12_4$.**
1. Multiply by the $2$:
   $2 \times 3 = 6$. In base $4$, $6 \div 4 = 1$ remainder $2$. Write $2$, carry $1$.
   $2 \times 2 = 4$. Add the carried $1$ to get $5$. In base $4$, $5 = 11_4$.
   First row is $112_4$.
2. Multiply by the $1$:
   $1 \times 3 = 3$.
   $1 \times 2 = 2$.
   Second row is $230_4$ (remember to shift one space to the left, adding a zero).
3. Add the rows in base $4$:
   $$ \begin{array}{r@{\quad}l} 112 \\ + 230 \\ \hline \end{array} $$
   $2 + 0 = 2$.
   $1 + 3 = 4$. In base $4$, this is $10_4$. Write $0$, carry $1$.
   $1 + 2 + 1 \text{ (carry)} = 4 = 10_4$.
4. The result is $1002_4$.

### 4. Division
Long division directly in other bases can be very tricky and prone to errors. **The JAMB shortcut (and the safest method) is to convert both numbers to base 10, do the division in base 10, and convert the answer back to the required base.**

**Worked Example 11: Evaluate $331_5 \div 12_5$.**
1. Convert both to base $10$.
   $331_5 = 3(25) + 3(5) + 1(1) = 75 + 15 + 1 = 91_{10}$
   $12_5 = 1(5) + 2(1) = 7_{10}$
2. Perform the division in base $10$.
   $$91 \div 7 = 13_{10}$$
3. Convert $13_{10}$ back to base $5$.
   $13 \div 5 = 2$ remainder $3$
   $2 \div 5 = 0$ remainder $2$
   Read upwards: $23_5$.
4. The result is $23_5$.

> **Common mistakes in operations:** 
> - Forgetting the base you are in! During subtraction, students often borrow "10" instead of borrowing the value of the base. For example, borrowing in base 5 gives you 5, not 10.
> - Leaving a digit equal to the base in your final answer (e.g., writing $4$ in base 4. It should be $10_4$).

## Modular arithmetic

**Content (c): modular arithmetic.**
**Objective iii: perform operations in modulo arithmetic.**

Modular arithmetic is sometimes called "clock arithmetic". If you look at a traditional $12$-hour clock, after $12$ o'clock comes $1$ o'clock. The numbers "wrap around" a certain value called the **modulo** (or **mod** for short). In traditional Nigerian settings, markets often operate on cycles. For example, in Igbo culture, there are four market days (Eke, Orie, Afor, Nkwo) forming a $4$-day cycle. This is a real-world example of modulo $4$ arithmetic.

When you divide a number by the modulo, **the remainder is the answer.**
For example, $17 \pmod 5$: $17 \div 5 = 3$ remainder $2$. Therefore, $17 \equiv 2 \pmod 5$. 

[IMAGE: A circular clock face used for modulo 7 arithmetic. The numbers 0, 1, 2, 3, 4, 5, and 6 are arranged evenly around the circle like hours on a clock, with 0 at the top. Arrows outside the circle point clockwise to show addition. Clean flat textbook style, white background.]

### 1. Addition and Subtraction
Perform the operation normally, then find the remainder when divided by the modulo.

**Worked Example 12: Evaluate $15 + 18 \pmod 7$.**
1. Add the numbers normally.
   $$15 + 18 = 33$$
2. Divide by $7$ to find the remainder.
   $$33 \div 7 = 4 \text{ remainder } 5$$
3. The result is $5 \pmod 7$.

**Worked Example 13: Evaluate $(15 - 28) \pmod 6$.**
1. Subtract normally.
   $$15 - 28 = -13$$
2. In modulo arithmetic, we do not leave answers as negative numbers. To find the equivalent positive remainder, keep adding the modulo ($6$) until the number becomes positive.
   $$-13 + 6 = -7$$
   $$-7 + 6 = -1$$
   $$-1 + 6 = 5$$
3. The result is $5 \pmod 6$.

### 2. Multiplication
Multiply the numbers normally and find the remainder.

**Worked Example 14: Evaluate $4 \times 5 \pmod 6$.**
1. Multiply normally.
   $$4 \times 5 = 20$$
2. Divide by $6$ to find the remainder.
   $$20 \div 6 = 3 \text{ remainder } 2$$
3. The result is $2 \pmod 6$.

### 3. Solving equations in modulo arithmetic
Equations in modular arithmetic are called **linear congruences**. To solve an equation like $ax \equiv b \pmod m$, you need to find a value of $x$ such that when $ax$ is divided by $m$, the remainder is $b$. The fastest method for JAMB is to test the possible remainders ($0$ to $m-1$), or add multiples of the modulo to $b$ until you find a number cleanly divisible by $a$.

**Worked Example 15: Find the value of $x$ if $2x \equiv 4 \pmod 7$.**
1. This equation means $2x$ leaves a remainder of $4$ when divided by $7$.
2. We can add multiples of the modulo ($7$) to the remainder ($4$) until we get a number that divides perfectly by $2$.
   $4 + 7(0) = 4$. (divisible by $2$)
3. So, $2x = 4 \Rightarrow x = 2$.
   *(Check: $2 \times 2 = 4 \equiv 4 \pmod 7$. Correct.)*

**Worked Example 16: Solve $2x + 4 \equiv 1 \pmod 5$.**
1. Isolate the $x$ term.
   $$2x \equiv 1 - 4 \pmod 5$$
   $$2x \equiv -3 \pmod 5$$
2. Convert the negative number to a positive modulo equivalent by adding the modulo ($5$).
   $$-3 + 5 = 2$$
   So, $2x \equiv 2 \pmod 5$.
3. Divide by $2$.
   $$x = 1$$
   *(Check: $2(1) + 4 = 6$. $6 \pmod 5 = 1$. Correct.)*

## Key terms

| Term | Meaning |
| --- | --- |
| Number Base | A counting system that uses a specific number of digits (e.g., base $2$ uses $0,1$; base $10$ uses $0-9$). |
| Binary | Another name for base $2$. |
| Place Value | The value of a digit based on its position, calculated as a power of the base. |
| Successive Division | A method used to convert a base $10$ integer to another base by dividing repeatedly. |
| Modulo | The divisor in modular arithmetic; the number at which counting wraps around back to zero. |
| Linear Congruence | An equation in modular arithmetic, generally in the form $ax \equiv b \pmod m$. |

## Exam tips and common mistakes

- **Always verify the base:** Ensure that all digits in a number are smaller than the base. If you write $142_4$, it is wrong because the digit "$4$" cannot exist in base $4$.
- **Borrowing means borrowing the base:** In base $n$ subtraction, borrowing $1$ from the next column gives you $n$, not $10$.
- **Use the base 10 shortcut for division:** Division in other bases is hard. Convert to base $10$, divide, and convert back.
- **Negative modulo answers:** If you get a negative result in modular arithmetic, add the modulo value repeatedly until it becomes positive.
- **Solving equations with unknown bases:** If given an equation like $32_x = 26_8$, always convert both sides to base $10$ first to form a simple algebra equation.

## Quick summary

1. A number base is a system using a specific number of digits; base $10$ is the standard system.
2. To convert from any base to base $10$, expand the number using powers of the base starting from $0$ on the right (and negative powers for fractional parts).
3. To convert from base $10$ to another base, use successive division for whole numbers (read remainders upwards) and successive multiplication for fractions (read integers downwards).
4. For operations (addition, subtraction, multiplication) in other bases, perform the operation and convert sums/products to the specific base. Borrowing equals the value of the base.
5. For division in non-10 bases, convert both numbers to base $10$, divide them, and convert the quotient back to the required base.
6. Modular arithmetic deals with remainders. The modulo acts as a wrap-around point (like a clock).
7. Negative numbers in modulo arithmetic are resolved by adding the modulo until the result is a positive number within the correct range.

## Practice questions

**1. Convert $124_5$ to base 10.**

- A. $39_{10}$
- B. $41_{10}$
- C. $34_{10}$
- D. $29_{10}$

**Answer: A.**
1. Expand using powers of $5$: $1 \times 5^2 + 2 \times 5^1 + 4 \times 5^0$.
2. Substitute the values: $1(25) + 2(5) + 4(1)$.
3. Add them together: $25 + 10 + 4 = 39_{10}$.
*(Mistake behind D: leaving out the middle term $2 \times 5^1$ gives $25 + 4 = 29$. Treating $5^0$ as $0$ instead of $1$ would give $25 + 10 + 0 = 35$, which is not one of the options.)*

**2. Convert $35_{10}$ to base 2.**

- A. $110011_2$
- B. $100011_2$
- C. $101011_2$
- D. $100101_2$

**Answer: B.**
1. Successively divide $35$ by $2$:
   $35 \div 2 = 17$ R $1$
   $17 \div 2 = 8$ R $1$
   $8 \div 2 = 4$ R $0$
   $4 \div 2 = 2$ R $0$
   $2 \div 2 = 1$ R $0$
   $1 \div 2 = 0$ R $1$
2. Read the remainders upwards: $100011_2$.
*(Mistake behind A: misdividing $17 \div 2$ or recording remainders poorly).*

**3. Convert $10.101_2$ to base 10.**

- A. $2.625_{10}$
- B. $2.5_{10}$
- C. $2.125_{10}$
- D. $2.375_{10}$

**Answer: A.**
1. Split into whole and fractional parts. Whole part: $1 \times 2^1 + 0 \times 2^0 = 2$.
2. Fractional part: $1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3}$.
3. Evaluate: $\frac{1}{2} + 0 + \frac{1}{8} = 0.5 + 0.125 = 0.625$.
4. Combine: $2 + 0.625 = 2.625_{10}$.

**4. Add $1011_2$ and $1101_2$.**

- A. $11010_2$
- B. $11100_2$
- C. $11000_2$
- D. $10100_2$

**Answer: C.**
1. Right column: $1 + 1 = 2 \rightarrow 10_2$. Write $0$, carry $1$.
2. Next column: $1 + 0 + 1 \text{ (carry)} = 2 \rightarrow 10_2$. Write $0$, carry $1$.
3. Next column: $0 + 1 + 1 \text{ (carry)} = 2 \rightarrow 10_2$. Write $0$, carry $1$.
4. Left column: $1 + 1 + 1 \text{ (carry)} = 3 \rightarrow 11_2$. Write $11$.
5. Final answer: $11000_2$.

**5. Subtract $432_5$ from $1211_5$.**

- A. $224_5$
- B. $234_5$
- C. $214_5$
- D. $124_5$

**Answer: A.**
1. Align the numbers: $1211_5 - 0432_5$.
2. $1 - 2$: Borrow $1$ (worth $5$) from the next digit. $5 + 1 = 6$. $6 - 2 = 4$.
3. Next digit is now $0$. $0 - 3$: Borrow $1$ (worth $5$). $5 + 0 = 5$. $5 - 3 = 2$.
4. Next digit is now $1$. $1 - 4$: Borrow $1$ (worth $5$). $5 + 1 = 6$. $6 - 4 = 2$.
5. Next digit is now $0$. Result: $224_5$.
*(Mistake behind B: after borrowing in the units column, forgetting to reduce the next digit by $1$. This gives $234_5$ instead of $224_5$.)*

**6. Evaluate $34_6 \times 25_6$.**

- A. $1432_6$
- B. $1412_6$
- C. $1322_6$
- D. $1422_6$

**Answer: D.**
1. Multiply $5 \times 34_6$: $5 \times 4 = 20 = 32_6$ (write $2$, carry $3$). $5 \times 3 = 15 + 3 = 18 = 30_6$ (write $0$, carry $3$). Row 1 is $302_6$.
2. Multiply $2 \times 34_6$: $2 \times 4 = 8 = 12_6$ (write $2$, carry $1$). $2 \times 3 = 6 + 1 = 7 = 11_6$ (write $1$, carry $1$). Row 2 is $1120_6$ (shifted).
3. Add rows: $302_6 + 1120_6$. $2+0=2$. $0+2=2$. $3+1=4$. $1+0=1$.
4. Result: $1422_6$.

**7. Divide $10010_2$ by $11_2$.**

- A. $101_2$
- B. $110_2$
- C. $111_2$
- D. $100_2$

**Answer: B.**
1. Convert to base $10$: $10010_2 = 16 + 2 = 18_{10}$.
2. Convert divisor: $11_2 = 2 + 1 = 3_{10}$.
3. Divide in base $10$: $18 \div 3 = 6_{10}$.
4. Convert $6_{10}$ back to base $2$: $6 \div 2 = 3$ R $0$; $3 \div 2 = 1$ R $1$; $1 \div 2 = 0$ R $1$. Read upwards: $110_2$.

**8. If $42_x = 26_8$, find the value of $x$.**

- A. $4$
- B. $5$
- C. $6$
- D. $7$

**Answer: B.**
1. Convert both sides to base $10$: $4(x) + 2(1) = 2(8) + 6(1)$.
2. Simplify: $4x + 2 = 16 + 6$.
3. Combine constants: $4x + 2 = 22$.
4. Solve: $4x = 20 \Rightarrow x = 5$.
*(Mistake behind C: accidentally adding 2 to 22 instead of subtracting, leading to $4x = 24 \Rightarrow x=6$).*

**9. Evaluate $(15 - 28) \pmod 6$.**

- A. $1$
- B. $3$
- C. $4$
- D. $5$

**Answer: D.**
1. Perform the subtraction: $15 - 28 = -13$.
2. To convert a negative number to a valid positive modulo remainder, add the modulo ($6$) repeatedly.
3. $-13 + 6 = -7$; $-7 + 6 = -1$; $-1 + 6 = 5$.
4. Result is $5 \pmod 6$.

**10. Find the value of $x$ if $3x \equiv 4 \pmod 7$.**

- A. $4$
- B. $5$
- C. $6$
- D. $2$

**Answer: C.**
1. The equation implies $3x$ is a number that leaves a remainder of $4$ when divided by $7$.
2. Add multiples of $7$ to $4$ until you find a number divisible by $3$:
   $4 + 7(0) = 4$ (No)
   $4 + 7(1) = 11$ (No)
   $4 + 7(2) = 18$ (Yes, $18 \div 3 = 6$).
3. So, $3x = 18 \Rightarrow x = 6$.
*(Alternatively, test options: $3(6) = 18 \Rightarrow 18 \div 7 = 2 \text{ remainder } 4$. Correct).*
