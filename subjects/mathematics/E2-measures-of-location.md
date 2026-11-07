# JAMB Mathematics Notes: Measures of Location

## What JAMB expects

This topic is Section V, Topic 2 of the JAMB Mathematics syllabus: Measures of Location. It covers the calculation and interpretation of statistical averages for different types of data, as well as the graphical representation of running totals to find specific positions in a dataset.

The syllabus covers:
- **a.** mean, mode and median of ungrouped and grouped data – (simple cases only);
- **b.** cumulative frequency.

By the end of these notes, you should be able to:
1. calculate the mean, mode and median of ungrouped and grouped data (simple cases only);
2. use Ogive to find the median, quartiles and percentiles.

**Note on the syllabus wording:** "Ogive" is the standard statistical term for a cumulative frequency curve. Measures of location are often called "measures of central tendency" or simply "averages" in many recommended textbooks.

## Mean, mode and median of ungrouped and grouped data

In statistics, after collecting data (such as the ages of students in a class or the prices of yams in a market), we often need a single value that represents the entire dataset. These representative values are called **measures of location** or **measures of central tendency**, because they tell us where the "centre" or "typical" value of the data is located. 

The three most common measures are the **Mean**, the **Median**, and the **Mode**.

### 1. The Mean (Arithmetic Mean)
The mean is what we normally call the "average" in everyday life. It takes every single value into account. It is calculated by adding all the values together and dividing by the total number of values. 
- **Advantage:** It uses all the data available, making it mathematically useful for further statistical calculations (like standard deviation).
- **Disadvantage:** It is easily affected by extreme values (called outliers). For example, in a group of five people, four earn ₦1,000, ₦1,200, ₦1,100 and ₦900, and one earns ₦50,000, the mean will be heavily pulled up by the ₦50,000, giving a false impression of the typical earnings.

### 2. The Median
The median is the literal middle value when the data is arranged in order of size (either from smallest to largest or largest to smallest). It cuts the dataset exactly in half.
- **Advantage:** It is not affected by extreme values (outliers). In the salary example above, the median would still accurately reflect the typical ₦1,100 earnings regardless of the one massive ₦50,000 salary.
- **Disadvantage:** It does not use the exact value of every piece of data, only their order and position.

### 3. The Mode
The mode is the most frequently occurring value in a dataset. It is the "most popular" item.
- **Advantage:** It is the only average that can be used for non-numerical (categorical) data. For example, if a shoe seller in Balogun Market wants to know which shoe size to stock the most, they look for the modal shoe size.
- **Disadvantage:** A dataset might not have a mode at all (if all values appear only once), or it might have more than one mode (bimodal or multimodal), which can make it less useful as a single representative value.

### Data Types: Ungrouped vs Grouped
To calculate these measures, the method depends on how the data is presented to you:
- **Ungrouped data:** A simple raw list of numbers (e.g., $4, 7, 2, 8, 4$).
- **Grouped discrete data:** A frequency table where each specific value is listed alongside how many times it appears (e.g., a table showing the scores out of 10 and the number of students who got each score).
- **Grouped continuous data:** A frequency table where data is grouped into class intervals or ranges (e.g., ages $10-14$, $15-19$, $20-24$).

## How to calculate the mean, mode and median of ungrouped and grouped data

### A. Calculating for Ungrouped Data

#### 1. Mean of Ungrouped Data
To find the mean (often denoted as $\bar{x}$, read as "$x$-bar"), sum all the values ($\sum x$) and divide by the total number of items ($N$ or $n$).
$$ \bar{x} = \frac{\sum x}{N} $$

**Worked Example 1:**
Find the mean of the following mathematics scores: $45, 60, 55, 70, 80$.

1. Add the scores: $\sum x = 45 + 60 + 55 + 70 + 80 = 310$.
2. Count the number of scores: $N = 5$.
3. Divide the sum by $N$: $\bar{x} = \frac{310}{5} = 62$.

**The mean score is $62$.**

**Worked Example 2 (Unknown Value):**
The mean of $5, 8, x, 12$, and $15$ is $10$. Find the value of $x$.

1. Write the formula with the given numbers: $\frac{5 + 8 + x + 12 + 15}{5} = 10$.
2. Simplify the numerator: $\frac{40 + x}{5} = 10$.
3. Cross-multiply: $40 + x = 50$.
4. Solve for $x$: $x = 50 - 40 = 10$.

**The value of $x$ is $10$.**

#### 2. Median of Ungrouped Data
To find the median:
1. **Sort** the numbers in ascending (or descending) order. Do not skip this step!
2. Find the middle position, which is the $\frac{N + 1}{2}$-th term.
3. If $N$ is odd, the median is the single middle number.
4. If $N$ is even, the median is the average (mean) of the two middle numbers.

**Worked Example 3 (Odd $N$):**
Find the median of the ages: $14, 12, 16, 13, 15, 17, 11$.

1. Sort the ages: $11, 12, 13, 14, 15, 16, 17$.
2. Count the items: $N = 7$ (odd).
3. Find the middle position: $\frac{7 + 1}{2} = \frac{8}{2} = 4$th position.
4. The 4th number is $14$. 

**The median age is $14$.**

**Worked Example 4 (Even $N$):**
Find the median of the prices: ₦450, ₦230, ₦670, ₦120, ₦340, ₦890, ₦560, ₦780.

1. Sort the prices: $120, 230, 340, 450, 560, 670, 780, 890$.
2. Count the items: $N = 8$ (even).
3. The middle numbers are the 4th and 5th items ($450$ and $560$).
4. Calculate their average: $\frac{450 + 560}{2} = \frac{1010}{2} = 505$.

**The median price is ₦505.**

#### 3. Mode of Ungrouped Data
Simply count how many times each number appears. The mode is the number with the highest frequency.

**Worked Example 5:**
Find the mode of $2, 5, 2, 4, 3, 5, 2, 6, 3, 2, 5, 5, 5$.

1. Count the frequencies: 
   - $2$ appears $4$ times.
   - $3$ appears $2$ times.
   - $4$ appears $1$ time.
   - $5$ appears $5$ times.
   - $6$ appears $1$ time.
2. The highest frequency is $5$, which belongs to the number $5$.

**The mode is $5$.**

### B. Calculating for Grouped Discrete Data (Frequency Tables)

When data contains many repeated values, it is summarised in a frequency table. The data values are denoted by $x$, and their frequencies by $f$.

#### 1. Mean of Grouped Discrete Data
The formula is adapted to account for the frequencies:
$$ \bar{x} = \frac{\sum fx}{\sum f} $$
Where:
- $\sum fx$ is the sum of the product of each value and its frequency.
- $\sum f$ is the total frequency (total number of items, $N$).

**Worked Example 6:**
The number of children per family in a small estate is given below. Find the mean.

| No. of children ($x$) | 0 | 1 | 2 | 3 | 4 | 5 |
|-------------------|---|---|---|---|---|---|
| Frequency ($f$) | 3 | 7 | 12 | 10 | 6 | 2 |

1. Create an $fx$ row (or column) by multiplying $x$ and $f$:
   - $0 \times 3 = 0$
   - $1 \times 7 = 7$
   - $2 \times 12 = 24$
   - $3 \times 10 = 30$
   - $4 \times 6 = 24$
   - $5 \times 2 = 10$
2. Find $\sum f = 3 + 7 + 12 + 10 + 6 + 2 = 40$.
3. Find $\sum fx = 0 + 7 + 24 + 30 + 24 + 10 = 95$.
4. Calculate the mean: $\bar{x} = \frac{95}{40} = 2.375$.

**The mean number of children is $2.375$.**

#### 2. Median of Grouped Discrete Data
To find the median from a frequency table, we use **cumulative frequency** to track positions.

1. Find the total frequency, $N = \sum f$.
2. The median is located at the $\frac{N + 1}{2}$-th position.
3. Build a cumulative frequency row and find which value of $x$ contains this position.

**Worked Example 7:**
Using the same data from Example 6, find the median.

1. Total frequency $N = 40$.
2. The median is the average of the 20th and 21st positions (since $\frac{40+1}{2} = 20.5$).
3. Write out the cumulative frequencies ($CF$):
   - $x = 0 \implies CF = 3$ (Positions 1 to 3)
   - $x = 1 \implies CF = 3 + 7 = 10$ (Positions 4 to 10)
   - $x = 2 \implies CF = 10 + 12 = 22$ (Positions 11 to 22)
4. Since the 20th and 21st positions both fall in the group that ends at position 22, the median value is $2$.

**The median is $2$.**

#### 3. Mode of Grouped Discrete Data
Simply look at the frequency row. The mode is the $x$ value that corresponds to the highest frequency.

**Worked Example 8:**
Using the same data from Example 6, the highest frequency is $12$. The $x$ value for this frequency is $2$. 

**The mode is $2$.**

### C. Calculating for Grouped Continuous Data (Class Intervals)

When data is highly varied (like weights, heights, or exam marks out of 100), it is grouped into classes or intervals, such as $10-14$, $15-19$, $20-24$. 

**Crucial Definitions:**
- **Class Limits:** The written numbers defining the class (e.g., $10$ is the lower limit, $14$ is the upper limit).
- **Class Boundaries:** The true unbroken limits that close the gaps between classes. If classes are $10-14$ and $15-19$, the gap is $1$ unit. Half of this gap ($0.5$) is subtracted from lower limits and added to upper limits. The boundaries for $10-14$ become $9.5 - 14.5$.
- **Class Width ($c$ or $w$):** The difference between the upper and lower **boundaries** (not limits). For $10-14$, the width is $14.5 - 9.5 = 5$.
- **Class Mark or Mid-point ($x$):** The exact middle of the class, used to represent all values in that class. $x = \frac{\text{lower limit} + \text{upper limit}}{2}$.

#### 1. Mean of Continuous Data
Since the exact raw values are lost in intervals, we assume every value in a class is exactly equal to its class mid-point ($x$). Then we apply the standard grouped formula: $\bar{x} = \frac{\sum fx}{\sum f}$.

**Shortcut for JAMB: The Assumed Mean Method**
When numbers are large, multiplying $f$ and $x$ manually wastes time. You can choose a mid-point near the middle of the table as an "Assumed Mean" ($A$).
Formula:
$$ \bar{x} = A + \frac{\sum fd}{\sum f} $$
Where $d = x - A$ (the deviation of each mid-point from the assumed mean).

**Worked Example 9:**
Calculate the mean of the following marks using both the direct method and assumed mean method.

| Marks | 10-19 | 20-29 | 30-39 | 40-49 | 50-59 |
|---|---|---|---|---|---|
| Frequency ($f$) | 5 | 8 | 12 | 10 | 5 |

**Method 1 (Direct):**
1. Find mid-points ($x$): $14.5, 24.5, 34.5, 44.5, 54.5$.
2. Calculate $fx$:
   - $5 \times 14.5 = 72.5$
   - $8 \times 24.5 = 196.0$
   - $12 \times 34.5 = 414.0$
   - $10 \times 44.5 = 445.0$
   - $5 \times 54.5 = 272.5$
3. $\sum fx = 72.5 + 196 + 414 + 445 + 272.5 = 1400$.
4. $\sum f = 40$.
5. Mean $\bar{x} = \frac{1400}{40} = 35.0$.

**Method 2 (Assumed Mean):**
Let Assumed Mean $A = 34.5$ (the middle mid-point).
1. Calculate deviations $d = x - 34.5$: $-20, -10, 0, 10, 20$.
2. Calculate $fd$:
   - $5 \times (-20) = -100$
   - $8 \times (-10) = -80$
   - $12 \times 0 = 0$
   - $10 \times 10 = 100$
   - $5 \times 20 = 100$
3. Sum the deviations: $\sum fd = -100 - 80 + 0 + 100 + 100 = 20$.
4. Apply formula: $\bar{x} = 34.5 + \frac{20}{40} = 34.5 + 0.5 = 35.0$.

*Notice how the assumed mean method involves much simpler mental arithmetic!*

#### 2. Median of Continuous Data
Since we don't have individual values, we use interpolation to find the exact point within the median class.
$$ \text{Median} = L_1 + \left( \frac{\frac{N}{2} - F_c}{f_m} \right) c $$
Where:
- $L_1$ = lower **class boundary** of the median class.
- $N$ = total frequency ($\sum f$).
- $F_c$ = cumulative frequency *before* the median class.
- $f_m$ = frequency of the median class itself.
- $c$ = class width (upper boundary - lower boundary).

**Worked Example 10:**
Find the median from the following distribution.

| Class Limits | 10-14 | 15-19 | 20-24 | 25-29 | 30-34 |
|---|---|---|---|---|---|
| Frequency ($f$) | 4 | 8 | 14 | 10 | 4 |

1. Prepare Cumulative Frequencies ($CF$): $4, 12, 26, 36, 40$. Total $N = 40$.
2. Find the median position: $\frac{N}{2} = \frac{40}{2} = 20$.
3. The 20th item falls in the $20-24$ class (since CF goes from 12 up to 26 here). **Median class = 20-24.**
4. Identify variables:
   - $L_1 = 19.5$ (Boundary for 20 is $20 - 0.5 = 19.5$).
   - $F_c = 12$ (CF of the class before).
   - $f_m = 14$ (Frequency of the median class).
   - $c = 5$ (Width: $24.5 - 19.5 = 5$).
5. Apply formula:
   $$ \text{Median} = 19.5 + \left( \frac{20 - 12}{14} \right) \times 5 $$
   $$ \text{Median} = 19.5 + \left( \frac{8}{14} \right) \times 5 = 19.5 + \frac{40}{14} = 19.5 + 2.857 = 22.36 $$

#### 3. Mode of Continuous Data
The modal class is the class with the highest frequency. We use interpolation to estimate the mode within that class.
$$ \text{Mode} = L_1 + \left( \frac{d_1}{d_1 + d_2} \right) c $$
Where:
- $L_1$ = lower **class boundary** of the modal class.
- $d_1 = f_m - f_{m-1}$ (frequency of modal class minus frequency of the previous class).
- $d_2 = f_m - f_{m+1}$ (frequency of modal class minus frequency of the next class).
- $c$ = class width.

*(Note: Textbook variation - Some texts write the formula as $L_1 + \left( \frac{f_m - f_{m-1}}{2f_m - f_{m-1} - f_{m+1}} \right) c$. This is mathematically identical.)*

**Worked Example 11:**
Using the same data from Example 10, find the mode.

1. The highest frequency is $14$, so the modal class is $20-24$.
2. Identify variables:
   - $L_1 = 19.5$.
   - $d_1 = 14 - 8 = 6$ (Modal freq minus previous freq).
   - $d_2 = 14 - 10 = 4$ (Modal freq minus next freq).
   - $c = 5$.
3. Apply formula:
   $$ \text{Mode} = 19.5 + \left( \frac{6}{6 + 4} \right) \times 5 = 19.5 + \left( \frac{6}{10} \right) \times 5 = 19.5 + 3 = 22.5 $$

## Cumulative frequency

A **cumulative frequency** is simply the running total of frequencies as you move through a dataset. It tells you how many data points are "less than or equal to" a certain upper boundary. 

Cumulative frequency tables are essential for locating the median in grouped data (as seen above) and are the absolute foundation for drawing an Ogive curve.

To build a cumulative frequency table for continuous data:
1. List the upper class boundaries for each class.
2. The cumulative frequency for the first class is just its frequency.
3. For the next class, add its frequency to the previous cumulative total.
4. The final cumulative frequency must exactly equal the total number of items, $N$.

**Example Cumulative Frequency Table:**

| Class Limit | Upper Boundary ($x$) | Frequency ($f$) | Cumulative Frequency ($CF$) |
|---|---|---|---|
| 10 - 14 | 14.5 | 4 | 4 |
| 15 - 19 | 19.5 | 8 | 4 + 8 = 12 |
| 20 - 24 | 24.5 | 14 | 12 + 14 = 26 |
| 25 - 29 | 29.5 | 10 | 26 + 10 = 36 |
| 30 - 34 | 34.5 | 4 | 36 + 4 = 40 |

Notice how we emphasize the **Upper Boundary**. When we ask, "How many students scored 14 or less?", we are actually looking at all scores up to the very edge of the class boundary, which is 14.5.

## How to use an Ogive to find the median, quartiles and percentiles

An **Ogive** (pronounced "oh-jive") is a smooth curve that graphically represents the cumulative frequency distribution. It allows us to estimate position-based measures like the median, quartiles, and percentiles without using complex formulas.

### 1. Constructing the Ogive
To draw an Ogive:
1. Create a cumulative frequency table, explicitly noting the **upper class boundaries**.
2. Add a starting class with a frequency of $0$. This ensures the curve starts touching the horizontal axis ($y = 0$). The upper boundary of this phantom class is the lower boundary of your actual first class.
3. Draw axes on graph paper. The **horizontal axis ($x$-axis)** represents the upper class boundaries. The **vertical axis ($y$-axis)** represents the cumulative frequencies.
4. Plot the points as coordinates: $(\text{Upper Boundary}, \text{Cumulative Frequency})$.
5. Connect the points with a freehand, smooth, S-shaped curve (do not use a ruler to join the dots).

### 2. Reading position measures from the Ogive
Because the Ogive represents cumulative totals from $0$ to $N$, we can find specific fractions of the dataset by checking the $y$-axis and reading over to the curve, then down to the $x$-axis.

- **Median ($Q_2$ or $P_{50}$):** The value that divides the data into two equal parts. Find position $\frac{N}{2}$ on the $y$-axis.
- **Lower Quartile ($Q_1$):** The value below which 25% of the data lies. Find position $\frac{N}{4}$ on the $y$-axis.
- **Upper Quartile ($Q_3$):** The value below which 75% of the data lies. Find position $\frac{3N}{4}$ on the $y$-axis.
- **Percentiles ($P_k$):** The value below which $k\%$ of the data lies. Find position $\frac{k \times N}{100}$ on the $y$-axis.

*(Note: Once you find $Q_1$ and $Q_3$, you might be asked for the **Interquartile Range** ($Q_3 - Q_1$) or the **Semi-interquartile Range** $\frac{Q_3 - Q_1}{2}$.)*

**Worked Example 12:**
The weights (in kg) of 100 yams harvested from a farm are grouped below.
| Weight (kg) | 40-49 | 50-59 | 60-69 | 70-79 | 80-89 | 90-99 |
|---|---|---|---|---|---|---|
| Frequency | 5 | 15 | 40 | 25 | 10 | 5 |

First, we generate the cumulative frequencies and upper boundaries. We include a starting boundary of 39.5 with a CF of 0.
| Upper Boundary ($x$) | Cum. Freq ($y$) |
|---|---|
| 39.5 | 0 |
| 49.5 | 5 |
| 59.5 | 20 |
| 69.5 | 60 |
| 79.5 | 85 |
| 89.5 | 95 |
| 99.5 | 100 |

[IMAGE: A cumulative frequency curve (Ogive) plotted on a graph. The horizontal x-axis is labelled "Weight (kg)" with upper class boundary marks: 39.5, 49.5, 59.5, 69.5, 79.5, 89.5, 99.5. The vertical y-axis is labelled "Cumulative Frequency" from 0 to 100 in steps of 10. The curve starts smoothly at (39.5, 0), rises smoothly through (49.5, 5), (59.5, 20), (69.5, 60), (79.5, 85), (89.5, 95) and ends at (99.5, 100). Dashed lines show the Median (from 50 on the y-axis horizontally to the curve, then vertically down to 67.0 on the x-axis), Lower Quartile Q1 (from 25 on the y-axis to 60.75 on the x-axis), and Upper Quartile Q3 (from 75 on the y-axis to 75.5 on the x-axis). Clean flat textbook style, white background.]

**Interpreting the Ogive:**
1. **Median ($N = 100$):** Look for position $\frac{100}{2} = 50$ on the $y$-axis. Draw a horizontal line to the curve, then a vertical line straight down. It lands at approximately **$67.0$ kg**.
2. **Lower Quartile ($Q_1$):** Look for position $\frac{100}{4} = 25$ on the $y$-axis. The line drops down to **$60.75$ kg**.
3. **80th Percentile ($P_{80}$):** Look for position $\frac{80 \times 100}{100} = 80$ on the $y$-axis. The line drops down to approximately **$77.5$ kg**.

### 3. Estimating missing frequencies or values (Linear Interpolation)
Sometimes JAMB gives you two points on a cumulative frequency curve and assumes the line is straight between them to test your understanding of proportions (interpolation).

**Worked Example 13:**
An Ogive passes through the points $(49.5, 20)$ and $(59.5, 60)$. What is the estimated upper boundary for a cumulative frequency of $50$?

Using the gradient (slope) method between the two points:
- Point 1: $(49.5, 20)$
- Point 2: $(59.5, 60)$
- Target Point: $(x, 50)$

1. Find the slope $m$ between Point 1 and Point 2: $m = \frac{60 - 20}{59.5 - 49.5} = \frac{40}{10} = 4$.
2. The slope between Point 1 and the Target Point must be the same: $4 = \frac{50 - 20}{x - 49.5}$.
3. Equate and simplify: $4 = \frac{30}{x - 49.5}$.
4. Solve: $4(x - 49.5) = 30 \implies x - 49.5 = 7.5$.
5. Final value: $x = 49.5 + 7.5 = 57.0$.

**The estimated boundary is $57.0$.**

## Key terms

| Term | Meaning |
|---|---|
| **Mean** | The arithmetic average, calculated by dividing the sum of values by the total count ($\frac{\sum x}{N}$ or $\frac{\sum fx}{\sum f}$). |
| **Median** | The middle value of a sorted dataset, separating the lower half from the upper half. |
| **Mode** | The data value or class interval that appears most frequently. |
| **Class Limit** | The stated minimum and maximum values for a grouped interval (e.g., $10$ to $14$). |
| **Class Boundary** | The true unbroken edges of a class (e.g., $9.5$ to $14.5$) that leave no gaps between intervals. |
| **Class Mark ($x$)** | The mid-point of a class interval, used to represent the entire class when finding the mean. |
| **Cumulative Frequency ($CF$)** | The running total of frequencies up to the upper boundary of a specific class. |
| **Ogive** | A smooth S-shaped curve plotting cumulative frequencies against upper class boundaries. |
| **Quartiles** | Values that divide the ordered data into four equal parts: $Q_1$ (lower), $Q_2$ (median), and $Q_3$ (upper). |
| **Percentiles** | Values that divide the ordered data into 100 equal parts. |

## Exam tips and common mistakes

- **Forgetting to sort data:** Before finding the median of ungrouped data, you *must* arrange the numbers in ascending or descending order. This is the #1 mistake students make.
- **Even number medians:** If an ungrouped list has an even number of items, the median is the average of the two middle numbers, not just picking one of them.
- **Class limits vs boundaries:** When calculating median or mode for continuous data, always use the lower class **boundary** for $L_1$, never the class limit! (e.g., if the limit is $10-14$, $L_1$ is $9.5$).
- **Miscalculating class width ($c$):** The class width for $10-14$ is $14.5 - 9.5 = 5$, NOT $14 - 10 = 4$. Count on your fingers if you are unsure: 10, 11, 12, 13, 14 (that is 5 numbers).
- **Ogive coordinates:** Always plot the cumulative frequency against the **upper class boundary**, never against the class mid-point or lower boundary.

## Quick summary

1. Measures of location (central tendency) summarise datasets into a single representative value: Mean, Median, or Mode.
2. The **mean** uses all data points ($\bar{x} = \frac{\sum fx}{\sum f}$) but is sensitive to outliers. The assumed mean method ($\bar{x} = A + \frac{\sum fd}{\sum f}$) simplifies calculations by hand.
3. The **median** is the middle value of sorted data. For continuous grouped data, it is estimated using $\text{Median} = L_1 + \left( \frac{\frac{N}{2} - F_c}{f_m} \right) c$.
4. The **mode** is the most frequent value. For continuous data, it is found inside the modal class using $\text{Mode} = L_1 + \left( \frac{d_1}{d_1 + d_2} \right) c$.
5. **Class boundaries** close the gaps between limits. The gap is usually $1$, so we subtract $0.5$ from the lower limit and add $0.5$ to the upper limit.
6. **Cumulative frequency** is a running total, used to locate positions.
7. An **Ogive** is a cumulative frequency curve. Positions are read on the $y$-axis: Median at $\frac{N}{2}$, Lower Quartile at $\frac{N}{4}$, Upper Quartile at $\frac{3N}{4}$, and the $k$-th Percentile at $\frac{kN}{100}$.

## Practice questions

**1. Find the mean of the numbers: 5, 8, 12, 15, 20.**

- A. 10.0
- B. 12.0
- C. 12.5
- D. 15.0

**Answer: B.**
1. Sum all the given numbers: $\sum x = 5 + 8 + 12 + 15 + 20 = 60$.
2. Divide the sum by the total count ($N = 5$): $\bar{x} = \frac{60}{5} = 12.0$.
3. Option C ($12.5$) is a mistake of finding the average of the lowest and highest values, $\frac{5 + 20}{2}$, instead of the mean of all the numbers.

**2. What is the median of the following set of numbers: 45, 23, 67, 12, 34, 89, 56, 78?**

- A. 45.0
- B. 50.5
- C. 56.0
- D. 101.0

**Answer: B.**
1. Sort the numbers in ascending order: $12, 23, 34, 45, 56, 67, 78, 89$.
2. Since there are $8$ numbers (an even amount), the median is the average of the 4th and 5th items.
3. Calculate the average: $\frac{45 + 56}{2} = \frac{101}{2} = 50.5$.
4. Option A ($45.0$) is the mistake of picking just the 4th item instead of averaging it with the 5th.

**3. The mean of the numbers 15, 21, $x$, 18, 25, 17 is 20. Find the value of $x$.**

- A. 21
- B. 22
- C. 24
- D. 26

**Answer: C.**
1. Set up the mean equation using $\bar{x} = \frac{\sum x}{N}$: $\frac{15 + 21 + x + 18 + 25 + 17}{6} = 20$.
2. Simplify the numerator: $\frac{96 + x}{6} = 20$.
3. Cross-multiply to remove the fraction: $96 + x = 120$.
4. Solve for $x$: $x = 120 - 96 = 24$.
5. Option D ($26$) is a common arithmetic mistake made during subtraction.

**4. Find the mode of the dataset: 7, 9, 7, 4, 3, 9, 2, 7, 9, 7, 5, 4.**

- A. 4
- B. 5
- C. 7
- D. 9

**Answer: C.**
1. Count the frequency of each number: $7$ appears $4$ times, $9$ appears $3$ times, $4$ appears $2$ times, while the others appear once.
2. Identify the highest frequency: the number $7$ has the highest frequency ($4$).
3. Therefore, the mode is $7$. 
4. The most tempting wrong option is D ($9$), a mistake made by selecting the highest numerical value instead of the value with the highest frequency.

**5. A frequency distribution is given as follows: $x = \{0, 1, 2, 3, 4, 5\}$ with frequencies $f = \{3, 7, 12, 10, 6, 2\}$. Find the mean.**

- A. 2.15
- B. 2.375
- C. 2.50
- D. 3.00

**Answer: B.**
1. Calculate the total frequency $\sum f = 3 + 7 + 12 + 10 + 6 + 2 = 40$.
2. Calculate each product $fx$: $(0 \times 3)=0$, $(1 \times 7)=7$, $(2 \times 12)=24$, $(3 \times 10)=30$, $(4 \times 6)=24$, $(5 \times 2)=10$.
3. Sum the products: $\sum fx = 0 + 7 + 24 + 30 + 24 + 10 = 95$.
4. Calculate the mean: $\bar{x} = \frac{95}{40} = 2.375$.
5. Option C ($2.50$) is the mistake of just finding the middle of the $x$ values without weighting them by their frequencies.

**6. Using the same distribution from question 5 ($x = \{0, 1, 2, 3, 4, 5\}$ and $f = \{3, 7, 12, 10, 6, 2\}$), what is the median?**

- A. 1
- B. 2
- C. 3
- D. 4

**Answer: B.**
1. Calculate the cumulative frequencies: $3, 10, 22, 32, 38, 40$.
2. Identify the total frequency $N = 40$. The median falls between the 20th and 21st positions (since $\frac{40+1}{2} = 20.5$).
3. Looking at the cumulative frequencies, both the 20th and 21st positions fall into the class ending at $22$, which corresponds to $x = 2$.
4. The median is therefore $2$. Option C ($3$) is a mistake of picking the middle category blindly.

**7. For a distribution with classes 10-14, 15-19, 20-24, 25-29, 30-34 having frequencies 4, 8, 14, 10, and 4 respectively, determine the mode.**

- A. 21.5
- B. 22.0
- C. 22.5
- D. 23.0

**Answer: C.**
1. Identify the modal class: the class $20-24$ has the highest frequency ($14$).
2. Identify variables for the formula: lower boundary $L_1 = 19.5$, class width $c = 24.5 - 19.5 = 5$.
3. Find differences in frequency: $d_1 = 14 - 8 = 6$ (freq minus previous), $d_2 = 14 - 10 = 4$ (freq minus next).
4. Apply the mode formula: $\text{Mode} = 19.5 + \left(\frac{6}{6 + 4}\right) \times 5 = 19.5 + \left(\frac{6}{10}\right) \times 5$.
5. Solve: $19.5 + 3.0 = 22.5$.
6. Option B ($22.0$) is a mistake of using the mid-point of the modal class instead of interpolating.

**8. Using the data from question 7, calculate the median.**

- A. 22.00
- B. 22.36
- C. 22.50
- D. 23.15

**Answer: B.**
1. Calculate total frequency $\sum f = 40$. The median position is $\frac{40}{2} = 20$.
2. The cumulative frequencies are $4, 12, 26, 36, 40$. The 20th item falls in the $20-24$ class.
3. Identify variables: lower boundary $L_1 = 19.5$, cumulative frequency before $F_c = 12$, frequency of median class $f_m = 14$, class width $c = 5$.
4. Apply median formula: $\text{Median} = 19.5 + \left(\frac{20 - 12}{14}\right) \times 5 = 19.5 + \left(\frac{8}{14}\right) \times 5$.
5. Evaluate: $19.5 + \frac{40}{14} = 19.5 + 2.857 \approx 22.36$. 
6. Option C ($22.50$) is the mistake of calculating and selecting the mode instead of the median.

**9. The cumulative frequency curve of the marks of 200 students passes through the points $(49.5, 120)$ and $(59.5, 160)$. Assuming the curve is a straight line between these points, what is the estimated upper quartile mark?**

- A. 54.5
- B. 55.0
- C. 57.0
- D. 59.5

**Answer: C.**
1. The upper quartile ($Q_3$) corresponds to the $\frac{3N}{4} = \frac{3 \times 200}{4} = 150$th position on the $y$-axis.
2. We interpolate linearly between $(49.5, 120)$ and $(59.5, 160)$ to find $x$ when $y = 150$.
3. Find the gradient $m = \frac{160 - 120}{59.5 - 49.5} = \frac{40}{10} = 4$.
4. Apply the line equation $y - y_1 = m(x - x_1)$: $150 - 120 = 4(x - 49.5)$.
5. Solve for $x$: $30 = 4(x - 49.5) \implies x - 49.5 = 7.5$, so $x = 49.5 + 7.5 = 57.0$.
6. Option A ($54.5$) is the mistake of finding the simple mid-point of the class boundaries instead of properly interpolating.

**10. Which of the following is TRUE regarding the construction of an Ogive?**

- A. It is plotted using class mid-points against class frequencies.
- B. It is plotted using upper class boundaries against cumulative frequencies.
- C. It is plotted using lower class boundaries against cumulative frequencies.
- D. It is a bar chart showing the running totals of the data.

**Answer: B.**
1. An Ogive is a smooth curve representing the cumulative frequency distribution.
2. The upper class boundaries (the $x$ values) are plotted on the horizontal axis.
3. The cumulative frequencies (the $CF$ values) are plotted on the vertical axis.
4. This produces points in the coordinate form $(x, CF)$, confirming option B is correct. 
5. Option C is a common mistake; plotting against lower boundaries shifts the curve incorrectly on the graph.
