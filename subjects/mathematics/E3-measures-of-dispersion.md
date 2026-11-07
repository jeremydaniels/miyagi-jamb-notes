# JAMB Mathematics Notes: Measures of Dispersion

## What JAMB expects

This file covers Section V, Topic 3 of the JAMB Mathematics syllabus: Measures of Dispersion. It has one content item and one objective:

- **only** range, mean deviation, variance and standard deviation.

By the end of these notes, you should be able to:
- **only** calculate the range, mean deviation, variance and standard deviation of ungrouped and grouped data.

*(Note on the syllabus wording: The syllabus uses the single word "only" for both the content item identifier and the objective identifier in this topic. To meet JAMB's requirements, we will explore the core concepts first, and then learn how to calculate each measure for both grouped and ungrouped data.)*

## Concepts of dispersion: range, mean deviation, variance and standard deviation

In statistics, "measures of location" or central tendency (like the mean, median, and mode) tell us where the centre of a dataset lies. However, the centre alone does not give us the full picture. We also need to know how scattered or spread out the data values are around that centre. **Measures of dispersion** (or spread) provide this missing information.

To understand why this is important, consider the test scores of two students, Amina and Bola, in five subjects:
- **Amina's scores:** $50, 50, 50, 50, 50$
- **Bola's scores:** $10, 20, 50, 80, 90$

If we calculate the mean for both students:
- Amina's mean $= \frac{50+50+50+50+50}{5} = 50$
- Bola's mean $= \frac{10+20+50+80+90}{5} = \frac{250}{5} = 50$

Both students have the exact same mean score of $50$. However, Amina is extremely consistent (her scores are identical), meaning there is **zero dispersion** in her data. Bola is very inconsistent; her scores are widely spread out from the mean, meaning there is **large dispersion** in her data. Measures of dispersion allow us to quantify this spread mathematically.

[IMAGE: Two bell-shaped curves on the same horizontal axis. One curve is tall and narrow (blue), indicating data closely packed together. The other curve is short and wide (red), indicating data spread far apart. A vertical dashed line passes through the exact centre of both curves. Labels to add later: "Small dispersion (data clustered around mean)", "Large dispersion (data spread out widely)", "Mean". Clean flat textbook style, white background.]

The four main measures of dispersion tested in the JAMB exam are:
1. **Range:** The total distance from the lowest value to the highest value.
2. **Mean Deviation:** The average absolute distance of each data point from the mean.
3. **Variance:** The average of the squared distances of each data point from the mean.
4. **Standard Deviation:** The square root of the variance, which brings the units back to the original form.

## Calculating range, mean deviation, variance and standard deviation

In this section, we will learn how to calculate all four measures for both **ungrouped data** (simple lists of numbers or frequency tables without classes) and **grouped data** (data organized into class intervals like $10 - 14$).

*(Note: Calculating measures of dispersion requires finding the mean first. If you need a refresher on calculating the mean, please refer to `E2-measures-of-location.md`.)*

### 1. The Range

The **range** is the simplest and quickest measure of dispersion to calculate. It only considers the two extreme ends of the data distribution.

#### Range of Ungrouped Data
For a simple set of numbers, the range is the difference between the highest value and the lowest value.
$$Range = \text{Highest value} - \text{Lowest value}$$

**Worked Example 1: Range of ungrouped data**
Find the range of the following set of ages (in years): $12, 5, 8, 17, 20, 9$.

**Step-by-step Solution:**
1. Identify the highest value in the set: $20$.
2. Identify the lowest value in the set: $5$.
3. Subtract the lowest value from the highest value: $20 - 5 = 15$.
4. The range is $15$ years.

#### Range of Grouped Data
For continuous data grouped into class intervals, we cannot see the exact highest and lowest individual values. Instead, we use the class limits.

**Textbook variation:** When finding the range of grouped data, standard Nigerian textbooks and examining bodies like JAMB and WAEC define the range as the difference between the **Upper Class Boundary (UCB)** of the highest class and the **Lower Class Boundary (LCB)** of the lowest class. However, some older books simply subtract the lowest class limit from the highest class limit. Always calculate using boundaries first. If your answer is not in the options, try the limits method.

$$Range = UCB_{\text{highest}} - LCB_{\text{lowest}}$$

**Worked Example 2: Range of grouped data**
Calculate the range of the following grouped frequency distribution:

| Class | 1 - 5 | 6 - 10 | 11 - 15 | 16 - 20 |
|-------|-------|--------|---------|---------|
| **Frequency**| 1 | 4 | 3 | 2 |

**Step-by-step Solution:**
1. Identify the lowest class: $1 - 5$.
2. Find its Lower Class Boundary. Since the gap between classes is $1$ (e.g., from $5$ to $6$), we divide the gap by $2$ to get $0.5$. Subtract $0.5$ from the lower limit: $1 - 0.5 = 0.5$.
3. Identify the highest class: $16 - 20$.
4. Find its Upper Class Boundary. Add $0.5$ to the upper limit: $20 + 0.5 = 20.5$.
5. Calculate the range by subtracting the lowest boundary from the highest boundary: $20.5 - 0.5 = 20.0$.
6. The range is $20.0$. *(Note: If the boundary method was not in the options, the limit method would give $20 - 1 = 19$.)*

---

### 2. Mean Deviation

The **mean deviation** (also called the mean absolute deviation) measures the average distance of each data point from the mean. 

If we simply subtracted the mean from each number and added them up, the positive and negative distances would cancel each other out and equal zero! To fix this, we ignore whether the distance is positive or negative by taking the **absolute value**, which is denoted by two vertical bars $| \dots |$.

#### Mean Deviation of Ungrouped Data (Without Frequencies)
$$MD = \frac{\sum |x - \bar{x}|}{n}$$
where:
- $x$ is each individual data value.
- $\bar{x}$ is the mean of the data.
- $n$ is the total number of values.
- $|x - \bar{x}|$ is the absolute difference between the value and the mean (all negative signs are turned into positives).

**Worked Example 3: Mean deviation of simple numbers**
Find the mean deviation of the numbers: $6, 8, 10, 12, 14$.

**Step-by-step Solution:**
1. Calculate the mean ($\bar{x}$): 
   $$\bar{x} = \frac{6 + 8 + 10 + 12 + 14}{5} = \frac{50}{5} = 10$$
2. Find the deviation of each number from the mean ($x - \bar{x}$):
   - $6 - 10 = -4$
   - $8 - 10 = -2$
   - $10 - 10 = 0$
   - $12 - 10 = 2$
   - $14 - 10 = 4$
3. Take the absolute values $|x - \bar{x}|$ by dropping the negative signs:
   - $4, 2, 0, 2, 4$
4. Sum the absolute values: $\sum |x - \bar{x}| = 4 + 2 + 0 + 2 + 4 = 12$.
5. Divide by $n$ (which is $5$) to find the Mean Deviation:
   $$MD = \frac{12}{5} = 2.4$$

**Common Mistake:** Forgetting to drop the negative signs! If you do not take the absolute value, the sum of deviations $(x - \bar{x})$ will always be exactly zero, which is useless for measuring spread.

#### Mean Deviation of Ungrouped Frequency Data
When data is presented in a frequency table, we must multiply each absolute deviation by its corresponding frequency.
$$MD = \frac{\sum f|x - \bar{x}|}{\sum f}$$

**Worked Example 4: Mean deviation with frequencies**
Calculate the mean deviation of the following distribution:

| Score ($x$) | 2 | 4 | 6 | 8 |
|---|---|---|---|---|
| Frequency ($f$) | 2 | 3 | 3 | 2 |

**Step-by-step Solution:**
1. Find the total frequency: $\sum f = 2 + 3 + 3 + 2 = 10$.
2. Calculate the mean ($\bar{x}$):
   - $\sum fx = (2 \times 2) + (4 \times 3) + (6 \times 3) + (8 \times 2) = 4 + 12 + 18 + 16 = 50$
   - $\bar{x} = \frac{\sum fx}{\sum f} = \frac{50}{10} = 5.0$
3. Find the absolute deviations $|x - 5.0|$ for each score $x$:
   - For $x=2$: $|2 - 5| = 3$
   - For $x=4$: $|4 - 5| = 1$
   - For $x=6$: $|6 - 5| = 1$
   - For $x=8$: $|8 - 5| = 3$
4. Multiply each absolute deviation by its frequency ($f|x - \bar{x}|$):
   - Frequency $2 \times$ deviation $3 = 6$
   - Frequency $3 \times$ deviation $1 = 3$
   - Frequency $3 \times$ deviation $1 = 3$
   - Frequency $2 \times$ deviation $3 = 6$
5. Sum these products: $\sum f|x - \bar{x}| = 6 + 3 + 3 + 6 = 18$.
6. Divide by the total frequency:
   $$MD = \frac{18}{10} = 1.8$$

#### Mean Deviation of Grouped Data
For grouped data, the process is exactly the same as for frequency data, but **$x$ represents the class mark (midpoint)** of each class.
- $x = \frac{\text{Lower Class Limit} + \text{Upper Class Limit}}{2}$

**Worked Example 5: Mean deviation of grouped data**
Calculate the mean deviation of the data below:

| Class | 10 - 14 | 15 - 19 | 20 - 24 |
|---|---|---|---|
| **Frequency ($f$)**| 2 | 3 | 5 |

**Step-by-step Solution:**
1. Find the midpoints ($x$) of each class:
   - $10 - 14$: $\frac{10+14}{2} = 12$
   - $15 - 19$: $\frac{15+19}{2} = 17$
   - $20 - 24$: $\frac{20+24}{2} = 22$
2. Total frequency $\sum f = 2 + 3 + 5 = 10$.
3. Calculate the mean ($\bar{x}$):
   - $fx$: $(2 \times 12) = 24$, $(3 \times 17) = 51$, $(5 \times 22) = 110$.
   - $\sum fx = 24 + 51 + 110 = 185$.
   - $\bar{x} = \frac{185}{10} = 18.5$.
4. Find the absolute deviations $|x - 18.5|$ for each midpoint:
   - $|12 - 18.5| = 6.5$
   - $|17 - 18.5| = 1.5$
   - $|22 - 18.5| = 3.5$
5. Multiply each deviation by its frequency ($f|x - \bar{x}|$):
   - $2 \times 6.5 = 13.0$
   - $3 \times 1.5 = 4.5$
   - $5 \times 3.5 = 17.5$
6. Sum these products: $13.0 + 4.5 + 17.5 = 35.0$.
7. Divide by $\sum f$: $MD = \frac{35.0}{10} = 3.5$.

---

### 3. Variance

The **variance** (often written as $Var$, $s^2$, or $\sigma^2$) is another way to mathematically remove negative signs when measuring spread. Instead of taking the absolute value, we **square** the deviations. 

**Textbook variation:** There are two types of variance in advanced statistics: population variance (where you divide by $n$) and sample variance (where you divide by $n-1$). In JAMB and WAEC exams, unless a question specifically asks for "sample variance" (which is extremely rare), you must **always divide by $n$ (or $\sum f$)**.

#### Variance of Ungrouped Data
**Definition Formula:**
$$Variance = \frac{\sum (x - \bar{x})^2}{n}$$

**Worked Example 6: Variance of simple numbers**
Find the variance of the numbers: $2, 4, 6, 8, 10$.

**Step-by-step Solution:**
1. Find the mean ($\bar{x}$) $= \frac{2+4+6+8+10}{5} = \frac{30}{5} = 6$.
2. Find the deviations from the mean ($x - 6$): $-4, -2, 0, 2, 4$.
3. Square each deviation $(x - 6)^2$: 
   - $(-4)^2 = 16$
   - $(-2)^2 = 4$
   - $(0)^2 = 0$
   - $(2)^2 = 4$
   - $(4)^2 = 16$
4. Sum the squared deviations: $16 + 4 + 0 + 4 + 16 = 40$.
5. Divide by $n$ to find the variance: $Variance = \frac{40}{5} = 8$.

#### Variance of Frequency and Grouped Data
For frequency tables (both ungrouped and grouped), we incorporate the frequency $f$. Because means are often decimal numbers, squaring deviations can become very messy. To avoid this, we strongly recommend using the **shortcut formula** for JAMB.

**Definition Formula:**
$$Variance = \frac{\sum f(x - \bar{x})^2}{\sum f}$$

**Shortcut Formula (highly recommended for JAMB):**
$$Variance = \frac{\sum fx^2}{\sum f} - \bar{x}^2$$

*(Note: $fx^2$ means $f \times (x^2)$, which is the frequency multiplied by the square of $x$. Do NOT calculate $(fx)^2$. Calculate $x^2$ first, then multiply by $f$.)*

**Worked Example 7: Variance using the shortcut formula**
Calculate the variance of the following grouped data:

| Class | 1 - 5 | 6 - 10 | 11 - 15 |
|-------|-------|--------|---------|
| **Freq ($f$)**| 3 | 4 | 3 |

**Step-by-step Solution:**
1. Find the midpoints ($x$) of each class:
   - $1 - 5$: $\frac{1+5}{2} = 3$
   - $6 - 10$: $\frac{6+10}{2} = 8$
   - $11 - 15$: $\frac{11+15}{2} = 13$
2. Set up a table to find $\sum f$, $\sum fx$, and $\sum fx^2$:

| Midpoint ($x$) | Freq ($f$) | $x^2$ | $fx$ (for mean) | $fx^2$ (for variance)|
|---|---|---|---|---|
| 3 | 3 | $3^2 = 9$ | $3 \times 3 = 9$ | $3 \times 9 = 27$ |
| 8 | 4 | $8^2 = 64$ | $4 \times 8 = 32$ | $4 \times 64 = 256$ |
| 13 | 3 | $13^2 = 169$ | $3 \times 13 = 39$ | $3 \times 169 = 507$ |
| **Sum** | **$\sum f = 10$**| | **$\sum fx = 80$** | **$\sum fx^2 = 790$** |

3. Calculate the mean ($\bar{x}$):
   $$\bar{x} = \frac{\sum fx}{\sum f} = \frac{80}{10} = 8$$
4. Apply the variance shortcut formula:
   $$Variance = \frac{\sum fx^2}{\sum f} - \bar{x}^2$$
   $$Variance = \frac{790}{10} - (8)^2$$
   $$Variance = 79 - 64 = 15$$
5. The variance is $15$. Notice how this method avoided subtracting means from every number!

---

### 4. Standard Deviation

The **standard deviation** (often written as $s$, $SD$, or $\sigma$) is simply the **positive square root of the variance**. 

Because variance involves squaring the data, its final units are squared (e.g., if the data represents masses in $kg$, the variance is in $kg^2$). Taking the square root brings the units back to their original, real-world form ($kg$), making standard deviation the most practically useful measure of spread.

$$SD = \sqrt{Variance}$$

**Worked Example 8: Standard deviation of grouped data**
What is the standard deviation of the grouped data from Worked Example 7?

**Step-by-step Solution:**
1. We already calculated the Variance = $15$.
2. To find the standard deviation, simply take the square root: $SD = \sqrt{15}$.
3. Using the square root table (provided in the exam) or leaving it in decimal form: $SD \approx 3.87$.

### Properties of Variance and Standard Deviation
JAMB frequently tests your understanding of how altering a dataset mathematically affects its spread, without requiring you to do long calculations.

1. **Adding or subtracting a constant:** If you add or subtract a constant $k$ from every number in a dataset, the entire dataset just shifts up or down. The numbers remain exactly as spread out from each other as they were before.
   - **New SD = Old SD** (No change)
   - **New Variance = Old Variance** (No change)
   - *Example:* The SD of the set $\{2, 4, 6\}$ is $2$. If we add $10$ to each number to get $\{12, 14, 16\}$, the SD is still exactly $2$.
2. **Multiplying or dividing by a constant:** If you multiply every number in a dataset by a constant $k$, the spread stretches by that factor.
   - **New SD = $k \times \text{Old SD}$**
   - **New Variance = $k^2 \times \text{Old Variance}$**
   - *Example:* If the SD of a dataset is $5$ and its variance is $25$. If every number is multiplied by $3$, the new SD is $5 \times 3 = 15$. The new variance is $(15)^2 = 225$ (which is $3^2 \times 25$).

**Worked Example 9: Properties of Dispersion**
The standard deviation of a set of numbers is $4$. If $5$ is added to each number, and then each number is multiplied by $3$, what is the new standard deviation and variance?

**Step-by-step Solution:**
1. Adding $5$ to each number does not affect the spread. The SD remains $4$.
2. Multiplying each number by $3$ scales the standard deviation by $3$.
3. New Standard Deviation = $4 \times 3 = 12$.
4. New Variance = $(\text{New SD})^2 = 12^2 = 144$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Dispersion** | The extent to which data values are spread out around the centre of the distribution. |
| **Range** | The difference between the highest value (or boundary) and the lowest value (or boundary). |
| **Mean Deviation** | The average of the absolute differences between each data point and the mean. Also called Mean Absolute Deviation. |
| **Variance** | The average of the squared differences between each data point and the mean. |
| **Standard Deviation** | The square root of the variance, restoring the data to its original units. |
| **Class Boundary** | The true upper and lower limits of a class, found by closing the gap between consecutive classes. |
| **Class Mark (Midpoint)** | The exact middle of a class, calculated as $\frac{\text{Lower limit} + \text{Upper limit}}{2}$. |

## Exam tips and common mistakes

- **Shortcut Formula for Variance:** Always use $Var = \frac{\sum fx^2}{\sum f} - \bar{x}^2$ for frequency data in the exam. It requires fewer columns and eliminates messy decimal subtractions.
- **$fx^2$ mistake:** Remember that $fx^2$ means $f \times (x \times x)$. A massive and common mistake is squaring $fx$ to get $(fx)^2$. Do not do this! Calculate $x^2$ first, then multiply by $f$.
- **Absolute values in Mean Deviation:** Always drop the negative signs. If you add the deviations $(x - \bar{x})$ without dropping the signs, your sum will be exactly zero.
- **Rounding errors:** If your mean is a long repeating decimal (e.g., $3.333...$), do not round it off to $3.3$ when calculating variance by definition, as squaring a rounded number creates huge errors. The shortcut formula avoids this problem entirely.
- **Forgetting the square root:** When a JAMB question asks for the standard deviation, they almost always put the variance as one of the options (usually Option C or D). Many students calculate the variance and immediately select that option. Always take the final square root!
- **Grouped Data Range:** Remember to use class boundaries for the range of grouped data. Only use class limits if the boundary-based answer is absolutely missing from the options.

## Quick summary

1. Measures of dispersion describe how spread out data is; they include range, mean deviation, variance, and standard deviation.
2. The **range** is the highest value minus the lowest value. For grouped continuous data, use class boundaries.
3. The **mean deviation** is the average of the absolute deviations from the mean: $MD = \frac{\sum f|x - \bar{x}|}{\sum f}$.
4. The **variance** is the average of the squared deviations from the mean: $Var = \frac{\sum fx^2}{\sum f} - \bar{x}^2$.
5. The **standard deviation** is the square root of the variance.
6. Adding or subtracting a constant to all values in a dataset does not change the variance or standard deviation.
7. Multiplying all values by a constant $k$ multiplies the standard deviation by $k$ and the variance by $k^2$.

## Practice questions

**1. Find the range of the following set of numbers: 12, 15, 9, 21, 14, 8, 17, 10.**

- A. 12
- B. 13
- C. 21
- D. 29

**Answer: B.** Here are the steps to find the solution:
1. Identify the maximum value in the set: $21$.
2. Identify the minimum value in the set: $8$.
3. Calculate range: $21 - 8 = 13$.
4. Option A is a distractor for students who carelessly identify the lowest value as $9$ instead of $8$.

**2. Calculate the range of the distribution with classes: 10-14, 15-19, 20-24, 25-29, 30-34.**

- A. 24
- B. 25
- C. 34
- D. 35

**Answer: B.** The step-by-step working is:
1. Find the Upper Class Boundary of the highest class ($30 - 34$). The gap to the next imaginary class ($35 - 39$) is $1$, so add $0.5$: $34 + 0.5 = 34.5$.
2. Find the Lower Class Boundary of the lowest class ($10 - 14$): $10 - 0.5 = 9.5$.
3. Calculate range: $34.5 - 9.5 = 25.0$.
4. Option A is the main distractor, obtained by improperly subtracting the strict class limits: $34 - 10 = 24$.

**3. What is the mean deviation of the numbers 3, 5, 8, 10, 14?**

- A. 0.0
- B. 3.2
- C. 4.0
- D. 16.0

**Answer: B.** The correct procedure is:
1. Determine the mean $\bar{x} = \frac{3+5+8+10+14}{5} = \frac{40}{5} = 8$.
2. Find the absolute deviations $|x - 8|$ for each value:
   $|3-8|=5$, $|5-8|=3$, $|8-8|=0$, $|10-8|=2$, $|14-8|=6$.
3. Sum the absolute deviations: $5 + 3 + 0 + 2 + 6 = 16$.
4. Divide by $n=5$ to find the mean deviation: $MD = \frac{16}{5} = 3.2$.
5. Option A is the distractor if the negative signs are not dropped before summing, which mathematically forces the sum to $0.0$. Option D forgets to divide by $n$.

**4. Find the mean deviation of the following frequency distribution:**
|$x$| 2 | 4 | 6 | 8 |
|---|---|---|---|---|
|$f$| 3 | 4 | 2 | 1 |

- A. 1.48
- B. 1.80
- C. 2.00
- D. 14.80

**Answer: A.** The full working is:
1. Find the sum of frequencies: $\sum f = 3 + 4 + 2 + 1 = 10$.
2. Calculate $\sum fx = (2\times3) + (4\times4) + (6\times2) + (8\times1) = 6 + 16 + 12 + 8 = 42$.
3. Calculate the mean: $\bar{x} = \frac{42}{10} = 4.2$.
4. Find the absolute deviations $|x - 4.2|$ for each $x$: $2.2, 0.2, 1.8, 3.8$.
5. Multiply each by its frequency $f|x - 4.2|$: 
   $3 \times 2.2 = 6.6$
   $4 \times 0.2 = 0.8$
   $2 \times 1.8 = 3.6$
   $1 \times 3.8 = 3.8$
6. Sum the results: $6.6 + 0.8 + 3.6 + 3.8 = 14.8$.
7. Divide by $\sum f$: $MD = \frac{14.8}{10} = 1.48$.
8. Option D is the distractor for students who forget to divide the total by $\sum f$.

**5. Calculate the variance of the numbers 4, 7, 5, 9, 10.**

- A. 2.28
- B. 5.20
- C. 6.50
- D. 26.00

**Answer: B.** Follow these steps:
1. Calculate the mean: $\bar{x} = \frac{4+7+5+9+10}{5} = \frac{35}{5} = 7$.
2. Find the deviations $(x - 7)$: $-3, 0, -2, 2, 3$.
3. Find the squared deviations $(x - 7)^2$: $9, 0, 4, 4, 9$.
4. Sum the squared deviations: $9 + 0 + 4 + 4 + 9 = 26$.
5. Divide by $n$ to find variance = $\frac{26}{5} = 5.20$.
6. Option A is the distractor for students who confuse variance with standard deviation (since $\sqrt{5.20} \approx 2.28$). Option D forgets to divide by $n$.

**6. The variance of a frequency distribution is given by the table below. Find its value.**
|$x$| 10 | 20 | 30 |
|---|----|----|----|
|$f$| 2 | 5 | 3 |

- A. 7.0
- B. 49.0
- C. 67.7
- D. 490.0

**Answer: B.** The step-by-step working is:
1. Find the total frequency: $\sum f = 2 + 5 + 3 = 10$.
2. Calculate $fx$: $20, 100, 90 \implies \sum fx = 210$.
3. Find the mean: $\bar{x} = \frac{210}{10} = 21$.
4. Calculate $x^2$: $10^2=100$, $20^2=400$, $30^2=900$.
5. Calculate $fx^2$: $2(100)=200$, $5(400)=2000$, $3(900)=2700$.
6. Sum the values: $\sum fx^2 = 200 + 2000 + 2700 = 4900$.
7. Apply the shortcut formula $Var = \frac{\sum fx^2}{\sum f} - \bar{x}^2 = \frac{4900}{10} - (21)^2 = 490 - 441 = 49.0$.
8. Option D is the distractor where the student forgets to subtract the mean squared. Option A is the standard deviation.

**7. Find the standard deviation of 1, 2, 3, 4, 5, 6, 7.**

- A. 2.00
- B. 2.65
- C. 4.00
- D. 16.00

**Answer: A.** The correct steps are:
1. Find the mean: $\bar{x} = \frac{28}{7} = 4$.
2. Find the squared deviations $(x - 4)^2$: $(-3)^2, (-2)^2, (-1)^2, 0^2, 1^2, 2^2, 3^2 \implies 9, 4, 1, 0, 1, 4, 9$.
3. Sum the squared deviations = $28$.
4. Calculate variance = $\frac{28}{7} = 4.0$.
5. Take the square root to find Standard Deviation = $\sqrt{4} = 2.00$.
6. Option C is the main distractor; many students calculate the variance correctly and forget the final square root step!

**8. Calculate the standard deviation of the following grouped data:**
| Class | 0-4 | 5-9 | 10-14 |
|---|---|---|---|
| Frequency | 2 | 5 | 3 |

- A. 3.50
- B. 3.87
- C. 7.50
- D. 12.25

**Answer: A.** The full working is:
1. Find class midpoints $x$: $2, 7, 12$.
2. Sum the frequencies: $\sum f = 2+5+3 = 10$.
3. Calculate $fx$: $2(2)=4, 5(7)=35, 3(12)=36 \implies \sum fx = 75$. 
4. Calculate Mean: $\frac{75}{10} = 7.5$.
5. Calculate $x^2$: $2^2=4, 7^2=49, 12^2=144$.
6. Calculate $fx^2$: $2(4)=8$, $5(49)=245$, $3(144)=432 \implies \sum fx^2 = 685$.
7. Calculate Variance = $\frac{\sum fx^2}{\sum f} - \bar{x}^2 = \frac{685}{10} - (7.5)^2 = 68.5 - 56.25 = 12.25$.
8. Find Standard Deviation = $\sqrt{12.25} = 3.50$.
9. Option D is the distractor for students who stop at the variance and fail to take the square root.

**9. Which of the following measures of dispersion is based on all items in a distribution and mathematically ignores the negative signs of deviations without squaring?**

- A. Range
- B. Mean Deviation
- C. Variance
- D. Standard Deviation

**Answer: B.** Here is the explanation distinguishing the methods:
1. The Range relies only on the two extreme items ($Max - Min$), not all items.
2. The Variance squares the deviations $\frac{\sum(x - \bar{x})^2}{n}$, which removes negative signs but alters the mathematical degree of the units.
3. The Mean Deviation uses the absolute value operation $\frac{\sum|x - \bar{x}|}{n}$ specifically to ignore negative signs without squaring them.
4. Option C is a tempting distractor because squaring also technically removes negative signs, but it alters the magnitude into squared units, unlike the absolute value method.

**10. If the standard deviation of a set of numbers is 5, what is the new variance if each number is multiplied by 2?**

- A. 10
- B. 25
- C. 50
- D. 100

**Answer: D.** Follow the mathematical principles for linear transformations of spread:
1. Identify the original standard deviation: $SD = 5$.
2. Calculate the original variance: $Var = 5^2 = 25$.
3. Recall that when every number is multiplied by a constant $k$, the new variance becomes $k^2 \times \text{Old Variance}$.
4. Calculate new variance = $2^2 \times 25 = 4 \times 25 = 100$.
5. Alternatively, calculate the new SD ($5 \times 2 = 10$) and square it ($10^2 = 100$).
6. Option A is the distractor for the new standard deviation, not the new variance! Option C incorrectly multiplies the variance by just $2$ instead of $2^2$.
