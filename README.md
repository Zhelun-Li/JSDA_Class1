# The Mathematical Principles of JSDA Class 1

## Purpose

Assuming the reader of this document has a solid technical background, I would recommend spending no more than 20 hours in total preparing for this exam and focusing the rest of your time on real work. By carefully studying the structure of the test and fully understanding the principles of entropy, a strategic test taker should be able to maximally exploit the information content of questions in any exam.

<span style="color:red;">
"It remains that, from the same principles, I now demonstrate the frame of the System of the JSDA Class 1 exam." -- not by Isaac Newton
</span>

## Draft Outline

1. [Overview](#overview)
2. [Sensitivity](#sensitivity)
   1. [The random guesser](#random-guesser)
   2. [The informed guesser](#informed-guesser)
3. [Entropy](#entropy)

<a id="overview"></a>

## 1. Overview

Question type notation:

- TF = True or False
- C15 = Choose 1 from 5
- C25 = Choose 2 from 5

<table>
  <thead>
    <tr>
      <th>Section (Japanese)</th>
      <th>Section (English)</th>
      <th>TF</th>
      <th>C15</th>
      <th>C25</th>
      <th>Total Points</th>
      <th>Share of Total</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>金融商品取引法及び関係法令</td><td>Financial Instruments and Exchange Act and Related Laws</td><td>7 questions / 14 points</td><td>0 questions / 0 points</td><td>2 questions / 20 points</td><td>34</td><td>7.7%</td></tr>
    <tr><td>金融商品の勧誘・販売に関係する法律</td><td>Laws Related to the Solicitation and Sale of Financial Products</td><td>3 questions / 6 points</td><td>0 questions / 0 points</td><td>0 questions / 0 points</td><td>6</td><td>1.4%</td></tr>
    <tr><td>協会定款・諸規則</td><td>Association Articles and Rules</td><td>7 questions / 14 points</td><td>0 questions / 0 points</td><td>3 questions / 30 points</td><td>44</td><td>10.0%</td></tr>
    <tr><td>取引所定款・諸規則</td><td>Exchange Articles and Rules</td><td>6 questions / 12 points</td><td>0 questions / 0 points</td><td>0 questions / 0 points</td><td>12</td><td>2.7%</td></tr>
    <tr><td>株式業務</td><td>Equity Operations</td><td>6 questions / 12 points</td><td>3 questions / 30 points</td><td>1 question / 10 points</td><td>52</td><td>11.8%</td></tr>
    <tr><td>債券業務</td><td>Bond Operations</td><td>5 questions / 10 points</td><td>3 questions / 30 points</td><td>0 questions / 0 points</td><td>40</td><td>9.1%</td></tr>
    <tr><td>投資信託及び投資法人に関する業務</td><td>Investment Trust and Investment Corporation Operations</td><td>7 questions / 14 points</td><td>2 questions / 20 points</td><td>0 questions / 0 points</td><td>34</td><td>7.7%</td></tr>
    <tr><td>付随業務</td><td>Ancillary Operations</td><td>0 questions / 0 points</td><td>0 questions / 0 points</td><td>1 question / 10 points</td><td>10</td><td>2.3%</td></tr>
    <tr><td>株式会社法概論</td><td>Introduction to Corporate Law</td><td>5 questions / 10 points</td><td>0 questions / 0 points</td><td>1 question / 10 points</td><td>20</td><td>4.5%</td></tr>
    <tr><td>経済・金融・財政の常識</td><td>General Knowledge of Economics, Finance, and Public Finance</td><td>0 questions / 0 points</td><td>0 questions / 0 points</td><td>2 questions / 20 points</td><td>20</td><td>4.5%</td></tr>
    <tr><td>財務諸表と企業分析</td><td>Financial Statements and Corporate Analysis</td><td>5 questions / 10 points</td><td>1 question / 10 points</td><td>0 questions / 0 points</td><td>20</td><td>4.5%</td></tr>
    <tr><td>証券税制</td><td>Securities Taxation</td><td>6 questions / 12 points</td><td>1 question / 10 points</td><td>0 questions / 0 points</td><td>22</td><td>5.0%</td></tr>
    <tr><td>証券市場の基礎知識</td><td>Basic Knowledge of Securities Markets</td><td>1 question / 2 points</td><td>1 question / 10 points</td><td>0 questions / 0 points</td><td>12</td><td>2.7%</td></tr>
    <tr><td>セールス業務</td><td>Sales Operations</td><td>4 questions / 8 points</td><td>0 questions / 0 points</td><td>0 questions / 0 points</td><td>8</td><td>1.8%</td></tr>
    <tr><td>デリバティブ取引</td><td>Derivatives Trading</td><td>8 questions / 16 points</td><td>4 questions / 40 points</td><td>5 questions / 50 points</td><td>106</td><td>24.1%</td></tr>
  </tbody>
  <tfoot>
    <tr><td><strong>Total</strong></td><td><strong>All Sections</strong></td><td><strong>70 questions / 140 points</strong></td><td><strong>15 questions / 150 points</strong></td><td><strong>15 questions / 150 points</strong></td><td><strong>440</strong></td><td><strong>100.0%</strong></td></tr>
  </tfoot>
</table>


Now, after looking at the table, one conclusion becomes immediately clear: Derivatives Trading, Equity Operations, Bond Operations, and Association Articles and Rules are the four most important sections.
<span style="color:red;"><strong>Advice 1.1: Spend more than 80% of your study time on Derivatives Trading, Equity Operations, and Bond Operations.</strong></span>
At this point, you may naturally have two questions:

- What about the other sections?
- What about Association Articles and Rules, since I just said that it is one of the most important sections?

Don't worry. I will teach you the techniques for the other sections later. But first, let us look at why Association Articles and Rules is not as important as it seems. By investigating this, we will learn something important about the exam.

<a id="sensitivity"></a>

## 2. Sensitivity

<a id="random-guesser"></a>

### 2.1 The random guesser

First, let us study the expected result for someone who attempts the exam with no knowledge, or information, at all. Given this lack of information, a truly rational Bayesian test taker would inevitably become a random guesser, since all choices must be treated as equally likely.

For TF questions, random guessing gives a `1/2` chance of being correct. For C15 questions, random guessing gives a `1/5` chance. C25 is more interesting. Since we choose 2 answers from 5, there are `C(5, 2) = 10` possible pairs. One pair is fully correct and gives 10 points. Six pairs contain exactly one correct answer and give 5 points. The remaining three pairs give 0 points.

So, using the question counts from the overview table:

- TF score follows `2 * Binomial(70, 1/2)`
- C15 score follows `10 * Binomial(15, 1/5)`
- C25 score follows a 15-question partial-credit distribution with `P(0 points) = 3/10`, `P(5 points) = 6/10`, and `P(10 points) = 1/10`


| Question Type | Maximum Points | Expected Score +/- Std | Relative Score +/- Std |
| --- | ---: | ---: | ---: |
| TF | 140 | 70.00 +/- 8.37 | 50.00% +/- 5.98% |
| C15 | 150 | 30.00 +/- 15.49 | 20.00% +/- 10.33% |
| C25 | 150 | 60.00 +/- 11.62 | 40.00% +/- 7.75% |
| **Total** | **440** | **160.00 +/- 21.10** | **36.36% +/- 4.79%** |

Now add these three distributions together. The exam has 440 total points, so the 70% passing line is 308 points. The exact probability that a pure random guesser passes is:

<span style="color:red;"><strong>Probability of passing by pure random guessing: 8.23e-11, or about 0.00000000823%.</strong></span>

As one can clearly observe from the calculation above, passing the exam as a random guesser is astronomically unlikely. Overall, we can see that C15 is the most important question type, simply because choosing one answer out of five is difficult, which makes the expected relative score very low. At the same time, it is an all-or-nothing question type with a lot of weight. This explains the second question left open in Section 1. In part, Association Articles and Rules questions are not as important because they are TF and C25 questions, which are relatively favorable to a random guesser. And we will soon see that this is not the only reason. Actual test takers are not random guessers, especially in sections such as Association Articles and Rules, where prior probability and common sense play an important role.
<!-- ![Exact random-guesser score distributions](images/random_guesser_question_type_distributions.png) -->

<a id="informed-guesser"></a>

### 2.2 The informed guesser

In Section 2.1, we worked out the special case of a random guesser. Now we proceed to develop a much more realistic model, in which the test taker is assumed to possess some information about the exam material. For those familiar with information theory, it is easy to see that we can intuitively represent the examinee's information using $p$, the rate at which the examinee is capable of choosing the right answer.

For starters, let us look at TF questions and assume that the examinee's probability of answering correctly is $p_{tf}$, instead of exactly $1/2$, which is the random-guesser case. Of course, we expect $p_{tf} \geq 1/2$. If not, intelligent examinees would simply invert their answers by choosing the opposite of what they believe to be right. In other words, it takes the same amount of information to be consistently wrong as it does to be consistently right. For any value of $p_{tf}$, we can work out the binomial distribution of the total number of TF questions answered correctly and hence derive the distribution of the TF score. Next, we evaluate the score distribution for C15 on the same plot. C15 is easy because it simply assigns a probability $p_{15}$ between `0.2` and `1` to choosing the correct answer.

C25 is harder to model. In practice, its five choices often behave like five TF statements bundled into one question. Let us assume that the examinee can judge each statement correctly with probability $p_{25}$: true statements are recognized as true, and false statements are recognized as false, each with probability $p_{25}$.

Each C25 question has 5 statements, of which 2 are true and 3 are false. Therefore, the expected number of statements the examinee believes to be true is roughly `2 * p_25 + 3 * (1 - p_25)`. This number may be smaller or larger than the 2 choices the examinee must submit. If fewer than 2 statements look true, the examinee selects those statements and randomly fills the remaining slot. If more than 2 statements look true, the examinee randomly selects 2 from the statements they believe are true.

![TF, C15, and C25 informed-guesser sensitivity](images/tf_c15_c25_informed_guesser_sensitivity.png)

Now we can ask a more useful question: if $p$ improves by 1 percentage point, how many extra points should we expect? For each value of $p$, we calculate this as `expected_score(p + 0.01) - expected_score(p)`. The plot below shows the expected point gain only, which is the cleanest way to compare which question type is most sensitive to a small improvement in judgment.

![Question type point sensitivity](images/question_type_point_sensitivity.png)

<a id="entropy"></a>

## 3. Entropy

## Next Step
