# JAMB Mathematics Notes: Fractions, Decimals, Approximations and Percentages

## What JAMB expects

This topic is Section I, Topic 2 of the JAMB Mathematics syllabus: Fractions, Decimals, Approximations and Percentages. It covers the following content items:

- (a) fractions and decimals;
- (b) significant figures;
- (c) decimal places;
- (d) percentage errors;
- (e) simple interest;
- (f) profit and loss percent;
- (g) ratio, proportion and rate;
- (h) shares and value added tax (VAT).

By the end of these notes, you should be able to:

1. perform basic operations ($\times, +, -, \div$) on fractions and decimals;
2. express to specified number of significant figures and decimal places;
3. calculate simple interest, profit and loss per cent; ratio proportion, rate and percentage error;
4. solve problems involving share and VAT.

**Note on the syllabus wording:** The syllabus asks you to perform basic operations printed as `(x,+,-,÷)on`. We will use standard mathematical spacing and the correct multiplication symbol ($\times$) in these notes. The syllabus also spells "valued added tax", which is a typing error for "value added tax" (VAT).

## Basic operations on fractions and decimals

**Objective i: perform basic operations ($\times, +, -, \div$) on fractions and decimals.**

Fractions and decimals are two ways of representing parts of a whole. In JAMB, you will often be asked to evaluate expressions that combine addition, subtraction, multiplication, and division. The golden rule for these operations is **BODMAS** (Brackets, Of, Division, Multiplication, Addition, Subtraction).

### Fractions

When working with fractions:
- Always convert **mixed fractions** (like $3\frac{1}{2}$) to **improper fractions** (like $\frac{7}{2}$) before multiplying or dividing.
- To add or subtract fractions, find the **Lowest Common Multiple (LCM)** of the denominators.
- To divide fractions, invert (flip) the fraction on the right and change the division sign to a multiplication sign.

**Example 1: Complex fractions**
Evaluate $\frac{3\frac{1}{2} - 1\frac{1}{4}}{2\frac{1}{3} \times 1\frac{2}{7}}$

1. **Numerator:** Convert to improper fractions: $3\frac{1}{2} = \frac{7}{2}$ and $1\frac{1}{4} = \frac{5}{4}$.
2. Subtract using the LCM of 2 and 4, which is 4:
   $$\frac{7}{2} - \frac{5}{4} = \frac{14 - 5}{4} = \frac{9}{4}$$
3. **Denominator:** Convert to improper fractions: $2\frac{1}{3} = \frac{7}{3}$ and $1\frac{2}{7} = \frac{9}{7}$.
4. Multiply: 
   $$\frac{7}{3} \times \frac{9}{7} = \frac{7 \times 9}{3 \times 7} = \frac{9}{3} = 3$$
5. **Final Division:** Divide the numerator by the denominator:
   $$\frac{9}{4} \div 3 = \frac{9}{4} \times \frac{1}{3} = \frac{3}{4}$$

### Decimals

When adding or subtracting decimals, strictly align the decimal points. When multiplying or dividing decimals, especially small ones like $0.0024$, the **JAMB shortcut** is to convert them to whole numbers multiplied by powers of 10 (standard form). This prevents you from miscounting zeroes.

**Example 2: Decimal multiplication and division**
Evaluate $\frac{0.0024 \times 0.06}{0.00012}$

1. Convert each decimal to a whole number multiplied by a power of 10:
   $0.0024 = 24 \times 10^{-4}$
   $0.06 = 6 \times 10^{-2}$
   $0.00012 = 12 \times 10^{-5}$
2. Substitute these into the expression:
   $$\frac{24 \times 10^{-4} \times 6 \times 10^{-2}}{12 \times 10^{-5}}$$
3. Group the whole numbers and the powers of 10:
   $$\frac{24 \times 6}{12} \times \frac{10^{-4} \times 10^{-2}}{10^{-5}}$$
4. Simplify:
   $2 \times 6 = 12$
   $10^{-6} \div 10^{-5} = 10^{-6 - (-5)} = 10^{-1}$
5. Result: $12 \times 10^{-1} = 1.2$.

**Example 3: Mixed fractions and decimals**
Evaluate $\frac{1}{2} + 0.75 - \frac{3}{4} \times 0.5$

1. It is usually easier to convert all decimals to fractions: $0.75 = \frac{3}{4}$ and $0.5 = \frac{1}{2}$.
2. The expression becomes: $\frac{1}{2} + \frac{3}{4} - \left(\frac{3}{4} \times \frac{1}{2}\right)$.
3. Use BODMAS (multiply first): $\frac{3}{4} \times \frac{1}{2} = \frac{3}{8}$.
4. Now add and subtract: $\frac{1}{2} + \frac{3}{4} - \frac{3}{8}$.
5. The LCM of 2, 4, and 8 is 8:
   $$\frac{4 + 6 - 3}{8} = \frac{7}{8}$$

**Common mistake:** Adding or subtracting before multiplying in a string of operations. Always apply BODMAS.

## Significant figures and decimal places

**Objective ii: express to specified number of significant figures and decimal places.**

Approximating numbers makes them easier to work with. You must know the difference between significant figures (s.f.) and decimal places (d.p.).

### Significant figures

Significant figures start counting from the **first non-zero digit** from the left.
- **Leading zeroes** (e.g., the zeroes in $0.004$) are **never** significant.
- **Zeroes between non-zero digits** (e.g., in $405$) are **always** significant.
- **Trailing zeroes** after a decimal point (e.g., $4.50$) are significant.

[IMAGE: A large number 0.040580 with arrows pointing to each digit to explain significant figures. The first two zeros (0.0) are labelled "Leading zeros (Not significant)". The digit 4 is labelled "1st significant figure". The zero between 4 and 5 is labelled "Zero between non-zero digits (Significant)". The digit 8 is labelled "4th significant figure". The final zero is labelled "Trailing zero after decimal point (Significant)". Clean flat textbook illustration, white background.]

### Decimal places

Decimal places simply count the digits **immediately after the decimal point**, regardless of whether they are zeroes or not.

### Rules for rounding
Look at the next digit after the one you want to stop at:
- If it is **5 or more**, round up (add 1 to your stopping digit).
- If it is **4 or less**, round down (leave your stopping digit as it is).

**Example 1: Approximating a large whole number**
Express 45,678 to 2 significant figures.
1. The 1st s.f. is 4. The 2nd s.f. is 5.
2. The next digit is 6, which is 5 or more, so we add 1 to 5 to make it 6.
3. Replace the remaining digits with zeroes (do not drop them, or you change the size of the number completely!).
4. Answer: 46,000.

**Example 2: Approximating a small decimal**
Express $0.007085$ to:
1. **3 decimal places:** Count 3 digits after the point (0, 0, 7). The next digit is 0, so we leave 7 as it is. Answer: $0.007$.
2. **3 significant figures:** The first non-zero digit is 7 (1st s.f.). Then 0 (2nd s.f.), then 8 (3rd s.f.). The next digit is 5, so we round the 8 up to 9. Answer: $0.00709$.

**Example 3: Calculation and rounding**
Evaluate $\frac{2.5 \times 0.04}{0.3}$ to 1 decimal place.
1. Multiply the numerator: $2.5 \times 0.04 = 0.100 = 0.1$.
2. Divide by the denominator: $\frac{0.1}{0.3} = \frac{1}{3}$.
3. As a decimal, $\frac{1}{3} = 0.3333...$
4. To 1 d.p., the first digit after the point is 3. The next digit is 3 (less than 5), so leave it. Answer: $0.3$.

## Percentages, ratios, rates and simple interest

**Objective iii: calculate simple interest, profit and loss per cent; ratio proportion, rate and percentage error.**

This section covers various real-life applications of fractions and percentages.

### Percentage errors

When a measurement is taken incorrectly, the error is the difference between the wrong (measured) value and the actual (correct) value.

$$ \text{Percentage Error} = \frac{| \text{Measured Value} - \text{Actual Value} |}{\text{Actual Value}} \times 100\% $$

**Common mistake:** Dividing by the wrong (measured) value instead of the correct (actual) value. The denominator must ALWAYS be the truth.

**Example 1: Measurement error**
A boy measured the length of a desk as 5.2 cm instead of the actual length of 5.0 cm. Calculate the percentage error.
1. Error = $5.2 - 5.0 = 0.2$ cm.
2. Actual Value = $5.0$ cm.
3. Percentage Error = $\frac{0.2}{5.0} \times 100 = \frac{2}{50} \times 100 = 4\%$.

**Example 2: Calculation error**
A girl evaluated $\frac{2}{5}$ instead of $\frac{5}{2}$. What is the percentage error in her calculation?
1. Actual value = $\frac{5}{2} = 2.5$.
2. Measured (wrong) value = $\frac{2}{5} = 0.4$.
3. Error = $2.5 - 0.4 = 2.1$.
4. Percentage Error = $\frac{2.1}{2.5} \times 100 = \frac{21}{25} \times 100 = 21 \times 4 = 84\%$.

### Simple interest

When money is borrowed or invested, interest is paid on it. Simple interest is calculated only on the original Principal ($P$), at a given Rate ($R$) in percentage per year, for a certain Time ($T$) in years.

$$ I = \frac{P \times R \times T}{100} $$
The total Amount ($A$) is the Principal plus the Interest: $A = P + I$.

**Example 1: Finding simple interest**
Find the simple interest on ₦150,000 for 3 years at 4% per annum.
1. $I = \frac{150000 \times 4 \times 3}{100}$.
2. $I = 1500 \times 12 = \text{₦}18,000$.

**Example 2: Finding time**
Find the time it takes for a sum of money to double itself at 5% simple interest per annum.
1. Let the Principal be $P$. If it doubles, the Amount $A = 2P$.
2. Interest $I = A - P = 2P - P = P$.
3. Using the formula: $P = \frac{P \times 5 \times T}{100}$.
4. Divide both sides by $P$: $1 = \frac{5T}{100}$.
5. $5T = 100$, so $T = 20$ years.

### Profit and loss percent

In trading, profit and loss are always calculated as a percentage of the **Cost Price (CP)**, never the Selling Price (SP).
- **Profit** = SP - CP (when SP > CP)
- **Loss** = CP - SP (when CP > SP)

$$ \text{Percentage Profit/Loss} = \frac{\text{Profit or Loss}}{\text{Cost Price}} \times 100\% $$

**Example 1: Finding profit percent**
A trader in Wuse Market bought a goat for ₦25,000 and sold it for ₦32,000. Calculate his profit percent.
1. Profit = $32,000 - 25,000 = \text{₦}7,000$.
2. % Profit = $\frac{7000}{25000} \times 100$.
3. % Profit = $\frac{700}{25} = 28\%$.

**Example 2: Finding Cost Price from Selling Price**
By selling an article for ₦4,500, a man makes a loss of 10%. Find the cost price.
1. A loss of 10% means the Selling Price is $100\% - 10\% = 90\%$ of the Cost Price.
2. $90\%$ of CP = ₦4,500.
3. $0.9 \times \text{CP} = 4500$.
4. $\text{CP} = \frac{4500}{0.9} = \frac{45000}{9} = \text{₦}5,000$.

### Ratio, proportion and rate

- **Ratio:** Compares quantities of the same kind. To share an amount in a given ratio, add the parts to find the total parts, then find the value of one part.
- **Rate:** Compares quantities of different kinds (e.g., km/h, litres/minute).
- **Proportion:** Can be direct (as one goes up, the other goes up) or inverse (as one goes up, the other goes down).

[IMAGE: Two side-by-side graphs illustrating proportion. On the left, a straight line passing through the origin on a Cartesian plane, labelled "Direct Proportion (y = kx)". On the right, a curve resembling a hyperbola in the first quadrant, labelled "Inverse Proportion (xy = k)". Clean flat textbook illustration, white background.]

**Example 1: Sharing in a ratio**
Ade, Bola and Cole share ₦1,200 in the ratio 2:3:5. How much does Bola receive?
1. Total ratio parts = $2 + 3 + 5 = 10$.
2. Bola's fraction of the total is $\frac{3}{10}$.
3. Bola's share = $\frac{3}{10} \times 1200 = \text{₦}360$.

**Example 2: Inverse proportion**
If 12 tailors can sew 360 dresses in 5 days, how many tailors are needed to sew 480 dresses in 4 days, assuming they all work at the same rate?
1. First, find the rate of one tailor. 12 tailors in 5 days is $12 \times 5 = 60$ tailor-days.
2. 60 tailor-days produce 360 dresses. Rate = $\frac{360}{60} = 6$ dresses per tailor per day.
3. For the new job: We need 480 dresses. At 6 dresses a day per tailor, this requires $\frac{480}{6} = 80$ tailor-days.
4. We only have 4 days to finish. Number of tailors needed = $\frac{80}{4} = 20$ tailors.

## Shares and value added tax (VAT)

**Objective iv: solve problems involving share and VAT.**

### Shares

When a company wants to raise money, it issues **shares**. When you buy shares, you own a tiny fraction of the company.
- **Nominal Value (Face Value):** The original price printed on the share certificate.
- **Market Value:** The current price the share is trading for on the stock exchange.
- **Dividend:** A share of the company's profit paid out to shareholders. **Crucial rule:** Dividend is ALWAYS calculated on the **Nominal Value**, not the market value.

**Example 1: Buying shares and earning dividends**
A man buys 5,000 shares of nominal value ₦2.00 at a market price of ₦2.50 each.
(i) Calculate the total cost of his shares.
(ii) If the company declares a dividend of 15%, calculate his total dividend.

1. **Total cost:** You buy shares at the Market Value.
   Cost = $5,000 \times 2.50 = \text{₦}12,500$.
2. **Total dividend:** Dividend is calculated on the Nominal Value.
   Total Nominal Value = $5,000 \times 2.00 = \text{₦}10,000$.
   Dividend = $15\%$ of ₦10,000 = $0.15 \times 10000 = \text{₦}1,500$.

### Value Added Tax (VAT)

VAT is a consumption tax placed on a product whenever value is added. In problems, VAT is usually given as a percentage that must be **added** to the basic price of the item.

**Example 2: Calculating VAT**
A refrigerator is priced at ₦150,000 exclusive of a 7.5% VAT. Calculate the total amount paid by a customer.
1. Find the VAT amount: $7.5\%$ of ₦150,000.
2. $\frac{7.5}{100} \times 150000 = 7.5 \times 1500 = \text{₦}11,250$.
3. Add the VAT to the original price: $150,000 + 11,250 = \text{₦}161,250$.

## Key terms

| Term | Meaning |
| --- | --- |
| BODMAS | Order of operations: Brackets, Of, Division, Multiplication, Addition, Subtraction |
| Significant figures | Digits that carry meaningful contributions to a number's precision, starting from the first non-zero digit |
| Decimal places | The number of digits immediately following the decimal point |
| Percentage error | The absolute error of a measurement expressed as a percentage of the true, actual value |
| Simple interest | Interest paid only on the original principal amount borrowed or invested |
| Nominal value | The original, face value of a company's share, used to calculate dividends |
| Market value | The current price at which a share is bought or sold |
| Dividend | A portion of a company's profit paid to its shareholders |
| VAT | Value Added Tax; a percentage tax added to the cost of goods and services |

## Exam tips and common mistakes

- **Common mistake in Percentage Error:** Using the wrong (measured) value as the denominator. The formula is $\frac{\text{Error}}{\text{Actual Value}} \times 100\%$.
- **Common mistake in Profit and Loss:** Calculating profit percent based on the selling price. It must always be calculated over the Cost Price (CP).
- **Common mistake in Shares:** Calculating dividend on the market price. Dividend is strictly a percentage of the **Nominal Value** of the shares.
- **Rounding trap:** When rounding large whole numbers to significant figures, do not drop the trailing zeroes before the decimal point! 45,678 to 2 s.f. is 46,000, not 46.
- **Time in Simple Interest:** The formula $I = \frac{PRT}{100}$ requires Time ($T$) to be in **years**. If given in months (e.g., 6 months), convert it to years ($\frac{6}{12} = 0.5$ years) before calculating.

## Quick summary

1. Simplify complex fractions by converting mixed fractions to improper fractions and applying BODMAS.
2. Multiply and divide small decimals safely by converting them to whole numbers multiplied by powers of 10.
3. Significant figures begin at the first non-zero digit. Leading zeroes are ignored.
4. Percentage error is the difference in measurement divided by the actual measurement, multiplied by 100.
5. Profit and loss percentages are always fractions of the Cost Price.
6. Simple interest is $I = \frac{PRT}{100}$, where T must be in years.
7. Dividends from shares are calculated using the nominal value, while the cost of purchasing shares is determined by the market value.
8. Value Added Tax (VAT) is calculated as a percentage and added to the exclusive price to find the total amount paid.

## Practice questions

**1. Simplify $\frac{3\frac{1}{2} + 2\frac{1}{3}}{1\frac{1}{4} - \frac{2}{3}}$**

- A. 5
- B. 7
- C. 10
- D. 14

**Answer: C.** The mistake behind the most tempting wrong option is failing to invert the denominator fraction when dividing.

1. Evaluate numerator: $3\frac{1}{2} + 2\frac{1}{3} = \frac{7}{2} + \frac{7}{3} = \frac{21 + 14}{6} = \frac{35}{6}$
2. Evaluate denominator: $1\frac{1}{4} - \frac{2}{3} = \frac{5}{4} - \frac{2}{3} = \frac{15 - 8}{12} = \frac{7}{12}$
3. Divide numerator by denominator: $\frac{35}{6} \div \frac{7}{12} = \frac{35}{6} \times \frac{12}{7}$
4. Simplify by cancelling out: $5 \times 2 = 10$.

**2. Evaluate $\frac{0.081 \times 0.005}{0.0027 \times 0.05}$**

- A. 30
- B. 3
- C. 0.3
- D. 0.03

**Answer: B.** The mistake behind the most tempting wrong option is miscounting decimal places when converting to standard form.

1. Convert all decimals to standard form: $81 \times 10^{-3}$, $5 \times 10^{-3}$, $27 \times 10^{-4}$, and $5 \times 10^{-2}$.
2. Substitute into expression: $\frac{81 \times 10^{-3} \times 5 \times 10^{-3}}{27 \times 10^{-4} \times 5 \times 10^{-2}}$
3. Group terms: $\frac{81 \times 5}{27 \times 5} \times \frac{10^{-6}}{10^{-6}}$
4. The powers of 10 cancel out. The 5s cancel out. $81 \div 27 = 3$.

**3. Evaluate $\frac{4.24 \times 0.02}{0.5}$ and express the answer to 2 significant figures.**

- A. 0.16
- B. 0.17
- C. 0.20
- D. 0.169

**Answer: B.** The mistake behind the most tempting wrong option is rounding down when the next digit is 5 or greater.

1. Multiply the numerator: $4.24 \times 0.02 = 0.0848$.
2. Divide by the denominator: $\frac{0.0848}{0.5} = 0.0848 \times 2 = 0.1696$.
3. Count 2 significant figures starting from the first non-zero digit (1, then 6).
4. The next digit is 9, so we round the 6 up to 7. Result is 0.17.

**4. A student measured the radius of a circle as 7.0 cm instead of 7.5 cm. Calculate the percentage error.**

- A. $6\frac{2}{3}\%$
- B. $7\frac{1}{7}\%$
- C. $5.0\%$
- D. $7.5\%$

**Answer: A.** The mistake behind the most tempting wrong option is dividing by the measured value (7.0 cm) instead of the actual value (7.5 cm).

1. Find the absolute error: $7.5 - 7.0 = 0.5$ cm.
2. Percentage Error = $\frac{\text{Error}}{\text{Actual}} \times 100 = \frac{0.5}{7.5} \times 100$.
3. Multiply top and bottom by 10 to clear decimals: $\frac{5}{75} \times 100 = \frac{1}{15} \times 100$.
4. Simplify: $\frac{100}{15} = \frac{20}{3} = 6\frac{2}{3}\%$.

**5. Find the principal which will earn ₦4,500 simple interest in 5 years at 3% per annum.**

- A. ₦30,000
- B. ₦45,000
- C. ₦35,000
- D. ₦25,000

**Answer: A.** The mistake behind the most tempting wrong option is confusing the formula or failing to rearrange $I = \frac{PRT}{100}$ correctly for Principal.

1. Use the rearranged formula: $P = \frac{100 \times I}{R \times T}$.
2. Substitute the values: $P = \frac{100 \times 4500}{3 \times 5}$.
3. Simplify the denominator: $3 \times 5 = 15$.
4. Calculate $P = \frac{450000}{15} = 30,000$.

**6. A man bought a television set for ₦80,000 and sold it for ₦64,000. Find his percentage loss.**

- A. 15%
- B. 20%
- C. 25%
- D. 30%

**Answer: B.** The mistake behind the most tempting wrong option is calculating the loss as a percentage of the selling price (₦64,000) instead of the cost price (₦80,000).

1. Calculate the loss: $80,000 - 64,000 = \text{₦}16,000$.
2. Set up the percentage loss fraction: $\frac{\text{Loss}}{\text{Cost Price}} \times 100$.
3. Substitute the values: $\frac{16000}{80000} \times 100$.
4. Simplify: $\frac{1}{5} \times 100 = 20\%$.

**7. Three boys, Ali, Bola, and Chukwu, shared a sum of money in the ratio 3:4:5. If Bola received ₦1,200, what was the total sum shared?**

- A. ₦4,800
- B. ₦3,600
- C. ₦2,400
- D. ₦6,000

**Answer: B.** The mistake behind the most tempting wrong option is assuming ₦1,200 is the total sum or finding only Chukwu's share.

1. Find the total number of parts in the ratio: $3 + 4 + 5 = 12$ parts.
2. Bola's share corresponds to 4 parts. So, 4 parts = ₦1,200.
3. Find the value of 1 part: $\frac{1200}{4} = \text{₦}300$.
4. Total sum = 12 parts = $12 \times 300 = \text{₦}3,600$.

**8. If 8 men can build a wall in 15 days, how many men would build the same wall in 10 days, assuming they work at the same rate?**

- A. 10
- B. 12
- C. 15
- D. 20

**Answer: B.** The mistake behind the most tempting wrong option is treating it as direct proportion instead of inverse proportion (more men take less time).

1. Find the total man-days required for the job: $8 \text{ men} \times 15 \text{ days} = 120 \text{ man-days}$.
2. Set up the inverse proportion for the new scenario: Let $x$ be the number of men.
3. $x \times 10 \text{ days} = 120 \text{ man-days}$.
4. $x = \frac{120}{10} = 12 \text{ men}$.

**9. A woman bought 2,000 ordinary shares of nominal value 50 kobo each at a market price of ₦1.50 per share. If a dividend of 20% was declared, find the total dividend received.**

- A. ₦200
- B. ₦600
- C. ₦100
- D. ₦3,000

**Answer: A.** The mistake behind the most tempting wrong option (B) is calculating the dividend based on the market price (₦1.50) instead of the nominal value (50 kobo).

1. Identify the nominal value of one share: 50 kobo = ₦0.50.
2. Calculate total nominal value: $2,000 \times 0.50 = \text{₦}1,000$.
3. Calculate the dividend (20% of nominal value): $\frac{20}{100} \times 1000$.
4. Total dividend = ₦200.

**10. The price of a laptop is ₦120,000 exclusive of 7.5% VAT. How much will a customer pay for the laptop?**

- A. ₦129,000
- B. ₦111,000
- C. ₦127,500
- D. ₦125,000

**Answer: A.** The mistake behind the most tempting wrong option is subtracting the VAT instead of adding it.

1. Calculate the VAT amount: $7.5\%$ of ₦120,000.
2. $\text{VAT} = \frac{7.5}{100} \times 120000 = 7.5 \times 1200 = \text{₦}9,000$.
3. Add the VAT to the exclusive price to get the total paid.
4. Total = $120,000 + 9,000 = \text{₦}129,000$.
