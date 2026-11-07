# JAMB Mathematics Notes: Probability

## What JAMB expects

This topic is Section V, Topic 5 of the JAMB Mathematics syllabus: Probability. It covers:

- **a.** experimental probability (tossing of coin, throwing of a dice etc);
- **b.** Addition and multiplication of probabilities (mutual and independent cases).

By the end of these notes, you should be able to:

1. solve simple problems in probability (including addition and multiplication).

**Note on the syllabus wording:** The syllabus asks for the "throwing of a dice" and "mutual and independent cases". The word "dice" is technically the plural of "die", and "mutual" means "mutually exclusive". In these notes, we use the standard mathematical English—one **die**, two **dice**, and **mutually exclusive** events—but the underlying concepts and mathematical operations are exactly what JAMB expects. 

## Basic concepts in probability

Probability is the measure of the likelihood or chance that a specific event will happen. 

- An **experiment** or **trial** is an action where the result is uncertain (like tossing a coin or picking a number).
- An **outcome** is a single possible result of an experiment.
- A **sample space ($S$)** is the complete set of all possible outcomes.
- An **event ($E$)** is a specific outcome or a collection of outcomes you are interested in.

The probability of an event, written as $P(E)$ or $Pr(E)$, is calculated using the formula:
$$P(E) = \frac{\text{Number of required outcomes}}{\text{Total number of possible outcomes}} = \frac{n(E)}{n(S)}$$

Probability is measured on a scale from $0$ to $1$:
- If an event is **impossible**, its probability is $0$.
- If an event is **certain**, its probability is $1$.
- The sum of the probability of an event happening and the probability of it not happening is always $1$: $P(E) + P(E') = 1$.

## Experimental probability (tossing of coin, throwing of a dice etc)

JAMB uses the term "experimental probability" to refer to two things: problems involving physical random generators (like coins and dice) based on theoretical sample spaces, and true experimental situations where data is collected through trials and recorded as frequencies.

### Tossing coins

A fair coin has two sides: a Head (H) and a Tail (T). 
- **One coin:** The sample space is $S = \{H, T\}$. There are 2 possible outcomes. The probability of getting a Head is $\frac{1}{2}$.
- **Two coins:** The sample space is $S = \{HH, HT, TH, TT\}$. Notice that (Head, Tail) and (Tail, Head) are two distinct outcomes. There are $2 \times 2 = 4$ possible outcomes.
- **Three coins:** The sample space is $S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$. There are $2 \times 2 \times 2 = 8$ possible outcomes.

**Worked Example 1**
Three fair coins are tossed together. Find the probability of obtaining at least two heads.

**Working:**

1. List the sample space: $S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$.
2. The total number of possible outcomes is $n(S) = 8$.
3. Identify the required outcomes. "At least two heads" means exactly $2$ heads or exactly $3$ heads. The set of such outcomes is $\{HHH, HHT, HTH, THH\}$.
4. The number of required outcomes is $4$.
5. $P(\text{at least two heads}) = \frac{4}{8} = \frac{1}{2}$.

### Throwing a die or dice

A standard fair die is a cube with six numbered faces: 1, 2, 3, 4, 5, and 6.
- **One die:** The sample space is $S = \{1, 2, 3, 4, 5, 6\}$. There are 6 possible outcomes. 
- **Two dice:** When throwing two dice, each die has 6 outcomes, so the total number of combinations is $6 \times 6 = 36$. The best way to visualize this is using a $6 \times 6$ grid or table.

[IMAGE: A 6 by 6 grid showing the sample space of throwing two dice. The top row has column headers 1 to 6 representing the first die, and the left column has row headers 1 to 6 representing the second die. Inside the grid are 36 cells showing pairs of numbers like (1,1), (1,2), up to (6,6). The diagonal cells (1,1) to (6,6) are highlighted softly. Style: clean flat textbook illustration, white background.]

**Worked Example 2**
Two fair dice are thrown simultaneously. What is the probability that the sum of the scores is a multiple of 4?

**Working:**

1. The total number of possible outcomes for two dice is $36$.
2. The possible sums range from 2 (which is $1+1$) to 12 (which is $6+6$). The multiples of 4 in this range are 4, 8, and 12.
3. List the specific pairs from the 36 outcomes that give these sums:
   - Sum of 4: $(1,3), (2,2), (3,1)$ $\rightarrow$ 3 outcomes
   - Sum of 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$ $\rightarrow$ 5 outcomes
   - Sum of 12: $(6,6)$ $\rightarrow$ 1 outcome
4. The total number of required outcomes is $3 + 5 + 1 = 9$.
5. $P(\text{sum is a multiple of 4}) = \frac{9}{36} = \frac{1}{4}$.

### Drawing playing cards
Though not explicitly named in this syllabus item, playing cards are a standard probability tool in JAMB. A standard pack has **52 cards**, divided into 4 suits of 13 cards each: Hearts (red), Diamonds (red), Clubs (black), and Spades (black). Each suit contains numbers 2 to 10, a Jack, a Queen, a King, and an Ace.

### True experimental probability (Relative frequency)

Sometimes, the probability is derived from an actual experiment or historical data. Here, $P(E) = \frac{\text{Frequency of the event}}{\text{Total number of trials}}$.

**Worked Example 3**
A die is tossed 50 times. The outcomes are recorded as follows:

| Score | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Freq | 8 | 10| 7 | 9 | 12| 4 |

What is the experimental probability of obtaining a prime number?

**Working:**

1. The total number of trials is $50$.
2. The prime numbers on a regular die are 2, 3, and 5.
3. Look up their frequencies in the table: 
   - Frequency of 2 = $10$
   - Frequency of 3 = $7$
   - Frequency of 5 = $12$
4. Total frequency for prime numbers = $10 + 7 + 12 = 29$.
5. The experimental probability is $\frac{29}{50}$.

## Addition and multiplication of probabilities (mutual and independent cases)

In complex probability problems, we often combine two or more simple events using "OR" or "AND". 

### Addition of probabilities (Mutually exclusive events)

Events are **mutually exclusive** if they cannot happen at the same time. For example, if you pick a single ball from a bag, it cannot be both completely red and completely blue. Similarly, on a single throw of a die, you cannot roll a 3 and a 4 simultaneously. 

The rule for mutually exclusive events uses the word **OR**:
$$P(A \text{ or } B) = P(A \cup B) = P(A) + P(B)$$

**Non-mutually exclusive events**
If two events *can* happen at the same time (they overlap), they are non-mutually exclusive. For example, drawing a card that is red OR a King (because there are red Kings). To avoid counting the overlap twice, we subtract it:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Worked Example 4**
An integer is chosen at random from 1 to 25 inclusive. What is the probability that it is a multiple of 3 or a multiple of 4?

**Working:**

1. The total possible outcomes is $n(S) = 25$.
2. Find the multiples of 3 (Event A): $\{3, 6, 9, 12, 15, 18, 21, 24\}$. There are $8$ outcomes, so $P(A) = \frac{8}{25}$.
3. Find the multiples of 4 (Event B): $\{4, 8, 12, 16, 20, 24\}$. There are $6$ outcomes, so $P(B) = \frac{6}{25}$.
4. Check for an overlap (numbers that are multiples of both 3 and 4, which means multiples of 12): $\{12, 24\}$. There are $2$ outcomes, so $P(A \cap B) = \frac{2}{25}$.
5. Use the non-mutually exclusive Addition Rule:
   
   $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
   
   $P(A \cup B) = \frac{8}{25} + \frac{6}{25} - \frac{2}{25} = \frac{12}{25}$.

### Multiplication of probabilities (Independent events)

Events are **independent** if the outcome of one event does not affect the outcome of the other. For example, tossing a coin and throwing a die are independent. What happens on the coin has no effect on the die. 

The rule for independent events uses the word **AND**:
$$P(A \text{ and } B) = P(A \cap B) = P(A) \times P(B)$$

**Worked Example 5**
The probability that Ade passes a mathematics exam is $\frac{2}{3}$ and the probability that Femi passes is $\frac{3}{4}$. If they both write the exam, find the probability that exactly one of them passes.

**Working:**

1. Find the probability of passing and failing for each student:
   - $P(\text{Ade passes}) = \frac{2}{3} \Rightarrow P(\text{Ade fails}) = 1 - \frac{2}{3} = \frac{1}{3}$.
   - $P(\text{Femi passes}) = \frac{3}{4} \Rightarrow P(\text{Femi fails}) = 1 - \frac{3}{4} = \frac{1}{4}$.
2. "Exactly one passes" means either (Ade passes AND Femi fails) OR (Ade fails AND Femi passes).
3. Find the probability of the first scenario (Ade passes AND Femi fails):
   
   $\frac{2}{3} \times \frac{1}{4} = \frac{2}{12}$
4. Find the probability of the second scenario (Ade fails AND Femi passes):
   
   $\frac{1}{3} \times \frac{3}{4} = \frac{3}{12}$
5. Since these two scenarios are mutually exclusive, add them together:
   
   $\frac{2}{12} + \frac{3}{12} = \frac{5}{12}$.

### Dependent cases (Selection without replacement)

Sometimes, picking an item and *not putting it back* changes the total for the next pick. The events become dependent, but you still use multiplication for "AND" scenarios. You simply adjust the second probability to account for the item that has been removed. 

[IMAGE: A probability tree diagram showing two successive draws from a bag of 5 red and 3 black balls without replacement. The first set of branches shows Red (5/8) and Black (3/8). From Red, two branches show Red (4/7) and Black (3/7). From Black, two branches show Red (5/7) and Black (2/7). The final outcomes R,R; R,B; B,R; B,B are listed on the right. Style: clean flat textbook illustration, white background.]

**Worked Example 6**
A bag contains 5 red balls and 3 black balls. Two balls are picked one after the other without replacement. Find the probability that both are of the same colour.

**Working:**

1. The initial total number of balls is $5 + 3 = 8$.
2. "Same colour" means either (Red AND Red) OR (Black AND Black).
3. Calculate the probability for (Red AND Red):
   - First pick is red: $\frac{5}{8}$.
   - Second pick is red: Since one red ball is gone, there are 4 red balls left out of 7 total balls. The probability is $\frac{4}{7}$.
   - $P(\text{Red, Red}) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$.
4. Calculate the probability for (Black AND Black):
   - First pick is black: $\frac{3}{8}$.
   - Second pick is black: Since one black ball is gone, there are 2 black balls left out of 7 total balls. The probability is $\frac{2}{7}$.
   - $P(\text{Black, Black}) = \frac{3}{8} \times \frac{2}{7} = \frac{6}{56}$.
5. Add the probabilities of the two mutually exclusive paths:
   
   $P(\text{Same colour}) = \frac{20}{56} + \frac{6}{56} = \frac{26}{56} = \frac{13}{28}$.

## Solving simple problems in probability

JAMB will often mix probability with other topics, particularly Set Theory and Permutations and Combinations. The key is to logically find out exactly how many items fit the description before you divide by the total. 

### Probability with Venn diagrams

**Worked Example 7**
In a class of 45 students, 28 study Economics, 22 study Government and 6 study neither. If a student is chosen at random, find the probability that the student studies Government only.

**Working:**

1. Let the universal set total be $45$. The number of students who study at least one subject is $45 - 6 = 39$.
2. Let $x$ be the number of students who study both subjects. Using the set formula $n(E) + n(G) - n(E \cap G) = n(E \cup G)$:
   
   $28 + 22 - x = 39$
   
   $50 - x = 39 \Rightarrow x = 11$.
3. The number of students studying both is $11$.
4. The number of students studying Government ONLY is the total for Government minus those who study both: $22 - 11 = 11$.
5. The probability that a randomly chosen student studies Government only is $\frac{\text{Government only}}{\text{Total class}} = \frac{11}{45}$.

### Using Combinations for Probability

For probability problems involving selections of larger groups, you may need to use Permutation and Combination (covered in `E4-permutation-and-combination.md`).

**Worked Example 8**
A committee of 3 is to be selected from 4 men and 5 women. What is the probability that the committee consists of exactly 2 men and 1 woman?

**Working:**

1. The total number of people is $4 + 5 = 9$.
2. The total possible ways to select 3 people from 9 is using combinations (since order does not matter): $^{9}C_3$.
   
   $^{9}C_3 = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$.
3. The required event is choosing 2 men (from 4) AND 1 woman (from 5).
   - Ways to choose the men: $^{4}C_2 = \frac{4 \times 3}{2 \times 1} = 6$.
   - Ways to choose the woman: $^{5}C_1 = 5$.
   - Total required outcomes (using the multiplication principle): $6 \times 5 = 30$.
4. The probability is $\frac{\text{Required outcomes}}{\text{Total outcomes}} = \frac{30}{84}$.
5. Simplify the fraction by dividing top and bottom by 6: $\frac{5}{14}$.

### The "At least" shortcut

JAMB frequently asks for the probability of "at least one" outcome. Instead of calculating and adding multiple scenarios, you can use a powerful shortcut.

**Worked Example 9**
A fair coin is tossed 4 times. What is the probability of obtaining at least one head?

**Working:**

1. The total number of possible outcomes for 4 coins is $2 \times 2 \times 2 \times 2 = 16$.
2. "At least one head" means 1, 2, 3, or 4 heads. It is much faster to find the probability of the only opposite event: getting NO heads (which means all tails).
3. The only outcome with all tails is $(T, T, T, T)$. There is exactly $1$ such outcome.
4. $P(\text{no heads}) = \frac{1}{16}$.
5. Because the sum of all probabilities is 1:
   
   $P(\text{at least one head}) = 1 - P(\text{no heads})$
   
   $P(\text{at least one head}) = 1 - \frac{1}{16} = \frac{15}{16}$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Experiment / Trial** | An action or process that yields an uncertain outcome. |
| **Outcome** | A single possible result of an experiment. |
| **Sample Space** | The complete set of all possible outcomes for an experiment. |
| **Event** | A set of outcomes that you are interested in. |
| **Mutually Exclusive** | Events that cannot occur at the same time. Connected by "OR" (Addition). |
| **Independent Events** | Events where the outcome of one does not affect the outcome of the other. Connected by "AND" (Multiplication). |
| **Dependent Events** | Events where the outcome of the first affects the probabilities in the second (e.g., selection without replacement). |

## Exam tips and common mistakes

- **Adding instead of multiplying (and vice versa):** A very common JAMB trap. Remember: OR implies Addition ($+$), and AND implies Multiplication ($\times$).
- **Forgetting to reduce the total in "without replacement" problems:** If you pick a ball and don't replace it, the total number of balls decreases by $1$ for the next pick. Do not use the original denominator.
- **Ignoring overlap in non-mutually exclusive events:** When finding $P(A \text{ or } B)$, you must subtract $P(A \text{ and } B)$ if the events can happen at the same time (like picking a card that is both red and a Queen).
- **Assuming coin toss order doesn't matter:** (Head, Tail) and (Tail, Head) are two completely different outcomes when two coins are tossed. Always list the sample space carefully.
- **Not simplifying fractions:** JAMB always leaves options in their lowest terms. If you calculate $\frac{20}{56}$, look for its simplified form ($\frac{5}{14}$) in the options.

## Quick summary

1. The basic formula for probability is $P(E) = \frac{\text{Number of required outcomes}}{\text{Total possible outcomes}}$.
2. Experimental probability can mean a physical test (like throwing a die) or calculating probabilities from a given frequency table.
3. The sample space for one coin is $2$, two coins is $4$, and three coins is $8$. 
4. The sample space for one die is $6$, and for two dice is $36$.
5. For mutually exclusive events, use the Addition Rule: $P(A \text{ or } B) = P(A) + P(B)$.
6. For independent events, use the Multiplication Rule: $P(A \text{ and } B) = P(A) \times P(B)$.
7. In word problems with Set Theory, solve the Venn diagram or set formula first to find the exact number of people before dividing by the total.
8. The probability of an event NOT happening is $1 - P(\text{event happening})$.

## Practice questions

**1. A fair die is tossed once. What is the probability of obtaining a number strictly greater than 4?**

- A. $\frac{1}{6}$
- B. $\frac{1}{3}$
- C. $\frac{1}{2}$
- D. $\frac{2}{3}$

**Answer: B.** 

1. The sample space for a fair die is $S = \{1, 2, 3, 4, 5, 6\}$. Total outcomes = $6$.
2. The numbers strictly greater than 4 are $5$ and $6$. The number of required outcomes is $2$.
3. Probability = $\frac{2}{6}$.
4. Simplify the fraction: $\frac{2}{6} = \frac{1}{3}$. The common mistake leading to Option C is assuming "4 or greater", which gives 3 outcomes ($4, 5, 6$) and a probability of $\frac{1}{2}$. The word "strictly" means 4 is not included.

**2. A standard die is rolled 60 times. The number 3 appears 12 times. What is the experimental probability of rolling a 3?**

- A. $\frac{1}{6}$
- B. $\frac{1}{5}$
- C. $\frac{1}{4}$
- D. $\frac{1}{3}$

**Answer: B.** 

1. The total number of trials (rolls) is $60$.
2. The frequency of rolling a 3 is $12$.
3. Experimental probability = $\frac{\text{Frequency}}{\text{Total trials}} = \frac{12}{60}$.
4. Simplify to get $\frac{1}{5}$. The mistake behind the tempting Option A ($\frac{1}{6}$) is calculating the *theoretical* probability of rolling a 3 on a fair die, instead of the *experimental* probability based on the provided trial data.

**3. A bag contains 4 red, 5 green and 6 blue balls. If a ball is picked at random, what is the probability that it is NOT green?**

- A. $\frac{1}{3}$
- B. $\frac{4}{15}$
- C. $\frac{2}{5}$
- D. $\frac{2}{3}$

**Answer: D.** 

1. Find the total number of balls = $4 + 5 + 6 = 15$.
2. If the ball is not green, it must be either red or blue.
3. The number of red and blue balls = $4 + 6 = 10$.
4. Probability = $\frac{10}{15}$.
5. Simplify the fraction by dividing top and bottom by 5 to get $\frac{2}{3}$. A student might choose Option A ($\frac{1}{3}$) if they calculate the probability of picking a green ball ($\frac{5}{15}$) and forget to find the probability of NOT green.

**4. Two fair coins are tossed together. Find the probability of obtaining exactly one head.**

- A. $\frac{1}{4}$
- B. $\frac{1}{3}$
- C. $\frac{1}{2}$
- D. $\frac{3}{4}$

**Answer: C.** 

1. List the sample space: $S = \{HH, HT, TH, TT\}$. The total number of outcomes is $4$.
2. The outcomes with *exactly* one head are $HT$ and $TH$. The number of required outcomes is $2$.
3. Probability = $\frac{2}{4}$.
4. Simplify to get $\frac{1}{2}$. Thinking that $\{HT, TH\}$ represents just one combined outcome is a common error that leads to the incorrect Option A ($\frac{1}{4}$). The order of the coins always matters.

**5. A number is chosen at random from the integers 1 to 20 inclusive. Find the probability that it is a multiple of 3 or 4.**

- A. $\frac{1}{4}$
- B. $\frac{3}{10}$
- C. $\frac{1}{2}$
- D. $\frac{11}{20}$

**Answer: C.** 

1. Multiples of 3 between 1 and 20 are $\{3, 6, 9, 12, 15, 18\}$, which gives $6$ numbers.
2. Multiples of 4 between 1 and 20 are $\{4, 8, 12, 16, 20\}$, which gives $5$ numbers.
3. Find the overlap (numbers that are multiples of both 3 and 4). The only one is $12$, which gives $1$ number.
4. Use the formula for non-mutually exclusive events: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
5. $P(A \cup B) = \frac{6}{20} + \frac{5}{20} - \frac{1}{20} = \frac{10}{20} = \frac{1}{2}$. If you forget to subtract the overlapping 12, you will simply add 6 and 5 to get $\frac{11}{20}$, which is the incorrect Option D.

**6. In a class of 40 students, 25 play football, 15 play basketball, and 10 play neither. If a student is picked at random, what is the probability that they play BOTH sports?**

- A. $\frac{1}{8}$
- B. $\frac{1}{4}$
- C. $\frac{3}{8}$
- D. $\frac{5}{8}$

**Answer: B.** 

1. Find the number of students playing at least one sport by subtracting those who play neither: $40 - 10 = 30$.
2. Let $x$ be the number playing both. Using sets: $n(F) + n(B) - x = n(F \cup B)$.
3. Substitute the values: $25 + 15 - x = 30$.
4. $40 - x = 30 \Rightarrow x = 10$.
5. The probability that a student plays both is $\frac{10}{40}$.
6. Simplify to get $\frac{1}{4}$. Option A ($\frac{1}{8} = \frac{5}{40}$) is the probability of playing basketball only ($30 - 25 = 5$ students), which is not the same as playing both.

**7. Two fair dice are thrown simultaneously. What is the probability that the sum of the scores is a prime number?**

- A. $\frac{7}{36}$
- B. $\frac{1}{3}$
- C. $\frac{5}{12}$
- D. $\frac{1}{2}$

**Answer: C.** 

1. The total possible outcomes for two dice is $36$.
2. The possible sums range from 2 to 12. The prime sums in this range are 2, 3, 5, 7, and 11.
3. Count how many combinations give these sums: Sum 2 gives 1 pair; Sum 3 gives 2 pairs; Sum 5 gives 4 pairs; Sum 7 gives 6 pairs; Sum 11 gives 2 pairs.
4. Total required outcomes = $1 + 2 + 4 + 6 + 2 = 15$.
5. Probability = $\frac{15}{36}$.
6. Divide top and bottom by 3 to simplify: $\frac{5}{12}$. A common mistake is forgetting that 2 is a prime number or incorrectly including 9, which throws the count off. The wrong options come from miscounting the pairs for each sum; for example, $\frac{1}{3} = \frac{12}{36}$ is what you get if you count 12 pairs instead of 15.

**8. The probability that Ade passes the JAMB exam is 0.6 and the probability that Bola passes is 0.8. What is the probability that ONLY ONE of them passes?**

- A. 0.14
- B. 0.44
- C. 0.48
- D. 0.92

**Answer: B.** 

1. Find their individual probabilities of failing: $P(\text{Ade fails}) = 1 - 0.6 = 0.4$, and $P(\text{Bola fails}) = 1 - 0.8 = 0.2$.
2. "Only one passes" means either (Ade passes AND Bola fails) OR (Ade fails AND Bola passes).
3. First path (Ade passes and Bola fails): $0.6 \times 0.2 = 0.12$.
4. Second path (Ade fails and Bola passes): $0.4 \times 0.8 = 0.32$.
5. Add the mutually exclusive paths: $0.12 + 0.32 = 0.44$. Option C (0.48) is a common error resulting from finding the probability that they BOTH pass ($0.6 \times 0.8$) instead of exactly one.

**9. A box contains 3 black pens and 5 blue pens. Two pens are picked one after the other WITHOUT replacement. Find the probability that both are blue.**

- A. $\frac{3}{28}$
- B. $\frac{15}{56}$
- C. $\frac{5}{14}$
- D. $\frac{25}{64}$

**Answer: C.** 

1. The initial total number of pens is $3 + 5 = 8$.
2. The probability the first pen is blue is $\frac{5}{8}$.
3. Because the first blue pen is not replaced, only 4 blue pens remain, out of a new total of 7 pens.
4. The probability the second pen is blue is $\frac{4}{7}$.
5. Multiply the probabilities (AND rule): $\frac{5}{8} \times \frac{4}{7} = \frac{20}{56}$.
6. Simplify by dividing top and bottom by 4 to get $\frac{5}{14}$. Option D ($\frac{25}{64}$) is the common mistake of computing the probability WITH replacement ($\frac{5}{8} \times \frac{5}{8}$).

**10. Bag A contains 2 red and 4 green marbles. Bag B contains 3 red and 5 green marbles. A marble is drawn from each bag. What is the probability that they are of DIFFERENT colours?**

- A. $\frac{1}{8}$
- B. $\frac{5}{12}$
- C. $\frac{11}{24}$
- D. $\frac{13}{24}$

**Answer: C.** 

1. Determine the individual probabilities for each bag. For Bag A (6 marbles): $P(Red_A) = \frac{2}{6}$ and $P(Green_A) = \frac{4}{6}$. For Bag B (8 marbles): $P(Red_B) = \frac{3}{8}$ and $P(Green_B) = \frac{5}{8}$.
2. "Different colours" means picking (Red from A AND Green from B) OR (Green from A AND Red from B).
3. Calculate the first path ($Red_A$ and $Green_B$): $\frac{2}{6} \times \frac{5}{8} = \frac{10}{48}$.
4. Calculate the second path ($Green_A$ and $Red_B$): $\frac{4}{6} \times \frac{3}{8} = \frac{12}{48}$.
5. Add the mutually exclusive paths: $\frac{10}{48} + \frac{12}{48} = \frac{22}{48}$.
6. Simplify the fraction by dividing by 2 to get $\frac{11}{24}$. A very tempting wrong answer is Option D ($\frac{13}{24}$), which is the probability that they are the SAME colour ($\frac{6}{48} + \frac{20}{48} = \frac{26}{48} = \frac{13}{24}$).
