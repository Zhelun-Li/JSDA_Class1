# The Mathematical Principles of JSDA Class 1

## Purpose

Assuming the reader of this document has a solid technical background, I would recommend spending no more than 20 hours in total preparing for this exam and focusing the rest of your time on real work. By carefully studying the structure of the test and fully understanding the principles of entropy, a strategic test taker should be able to maximally exploit the information content of the questions in this exam.

<span style="color:red;">
"It remains that, from the same principles, I now demonstrate the frame of the System of the JSDA Class 1 exam." -- not by Isaac Newton
</span>

## Advice
Advice 1: Spend more than 80% of your study time on Derivatives Trading, Equity Operations, and Bond Operations.

Advice 2: The 5-choice questions are much more important than the True or False questions.

## Draft Outline

1. [Overview](#overview)
2. [Sensitivity](#sensitivity)
   1. [The random guesser](#random-guesser)
   2. [The informed guesser](#informed-guesser)
3. [Entropy](#entropy)
   1. [What is entropy? ](#What-is-entropy)
   2. [Coffee, wealth and pessimism ](#CWE)

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

<span style="color:red;"><strong>Advice 1: Spend more than 80% of your study time on Derivatives Trading, Equity Operations, and Bond Operations.</strong></span>

At this point, you may naturally have two questions:

- What about the other sections?
- What about Association Articles and Rules, since I just said that it is one of the most important sections?

Don't worry. I will teach you techniques for the other sections later. But first, let us look at why Association Articles and Rules is not as important as it seems. By investigating this, we will learn something important about the exam.

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

Now add these three distributions together. The exam has 440 total points, so the 70% passing line is 308 points. The exact probability that a pure random guesser passes is 8.23e-11, or about 0.00000000823%.

As one can clearly observe from the calculation above, passing the exam as a random guesser is astronomically unlikely. Overall, we can see that C15 is the most important question type, simply because choosing one answer out of five is difficult, which makes the expected relative score very low. At the same time, it is an all-or-nothing question type with a lot of weight. This explains the second question left open in Section 1. In part, Association Articles and Rules questions are not as important because they are TF and C25 questions, which are relatively favorable to a random guesser. We will soon see that this is not the only reason. Actual test takers are not random guessers, especially in sections such as Association Articles and Rules, where prior probability and common sense play an important role.
<!-- ![Exact random-guesser score distributions](images/random_guesser_question_type_distributions.png) -->

<a id="informed-guesser"></a>

### 2.2 The informed guesser

In Section 2.1, we worked out the special case of a random guesser. Now we proceed to develop a much more realistic model, in which the test taker is assumed to possess some information about the exam material. For those familiar with information theory, it is easy to see that we can intuitively represent the examinee's information using $p$, the rate at which the examinee is able to choose the right answer.

For starters, let us look at TF questions and assume that the examinee's probability of answering correctly is $p_{tf}$, instead of exactly $1/2$, which is the random-guesser case. Of course, we expect $p_{tf} \geq 1/2$. If not, intelligent examinees would simply invert their answers by choosing the opposite of what they believe to be right. In other words, it takes the same amount of information to be consistently wrong as it does to be consistently right. For any value of $p_{tf}$, we can work out the binomial distribution of the total number of TF questions answered correctly and hence derive the distribution of the TF score. Next, we evaluate the score distribution for C15 on the same plot. C15 is easy because it simply assigns a probability $p_{15}$ between `0.2` and `1` to choosing the correct answer.

C25 is harder to model. In practice, its five choices often behave like five TF statements bundled into one question. Let us assume that the examinee can judge each statement correctly with probability $p_{25}$: true statements are recognized as true, and false statements are recognized as false, each with probability $p_{25}$.

Each C25 question has 5 statements, of which 2 are true and 3 are false. Therefore, the expected number of statements the examinee believes to be true is roughly `2 * p_25 + 3 * (1 - p_25)`. This number may be smaller or larger than the 2 choices the examinee must submit. If fewer than 2 statements look true, the examinee selects those statements and randomly fills the remaining slot. If more than 2 statements look true, the examinee randomly selects 2 from the statements they believe are true. The plot of the expected score with respect to $p$ is shown below, where $p$ starts from the random-guess baseline.

<a id="fig-informed-guesser-sensitivity"></a>
![TF, C15, and C25 informed-guesser sensitivity](images/tf_c15_c25_informed_guesser_sensitivity.png)

*Figure 1. Expected score sensitivity for TF, C15, and C25 questions as examinee information increases.*

Now we can ask a more useful question: if $p$ improves by 1 percentage point, how many extra points should we expect? For each value of $p$, we calculate this as `expected_score(p + 0.01) - expected_score(p)`. The plot below shows the expected point gain only, which is the cleanest way to compare which question type is most sensitive to a small improvement in judgment. For TF and C15, it is easy to see that the sensitivity is flat, whereas C25 exhibits non-linear behavior. 

<a id="fig-question-type-point-sensitivity"></a>
![Question type point sensitivity](images/question_type_point_sensitivity.png)

*Figure 2. Expected point gain from a one-percentage-point improvement in judgment across question types.*

By now, I hope I have convinced the reader that both C15 and C25 carry more weight than TF. In terms of sensitivity, it is also more efficient to study them, especially C25, since it offers nonlinear improvement. To summarize:

<span style="color:red;"><strong>Advice 2:  5-choice questions are much more important than the True or False questions. </strong></span>

<a id="entropy"></a>

## 3. Entropy

In this chapter, I will first give you a lecture on what entropy is using real-world examples. You will understand why hot coffee tends to get cold, why things tend to break down instead of functioning, and why even equally talented people in fair societies inevitably create enormous wealth discrepancies over the long run.

Subsequently, we will see how to use entropy in the preparation of this test.

<a id="What-is-entropy"></a>
### 3.1 What is entropy?

Entropy can be defined in several ways: Boltzmann (statistical mechanics), Shannon (information theory), and Jaynes (Bayesian statistics). A knowledgeable reader will of course know that the three different approaches above are mutually equivalent and often borrow terms from one another. In this subsection, we will attempt to give a short description using the Boltzmann-like picture.

In one sentence, I wish to define entropy as "a measurement of disorder/randomness" and information as "a measurement of order with respect to disorder/randomness". To illustrate this, let us focus on the following example.

<a id="coinflip"></a>
#### 3.1.1  The coin flip
Let us say we play a game of coin-flipping: if it is heads (denoted by +), you receive one dollar. If it is tails (denoted by -), you pay one dollar. Are you scared to gamble under such conditions? Of course not. This is a fair game, and you know that on average, your expected payoff is $E = 0$. You are probably thinking something like this: "If I play a few games, I might get unlucky and lose some money. But as long as I play a huge number of games, I should be roughly winning half and roughly losing half." But why is that?

Let us examine the idea of "fairness": it means that on each flip, the outcome is independent and 50-50. If we play six games, the outcome could be represented by a string such as "+-++-+", where one wins four games and loses two. Now fairness demands that any such possible string is equally likely to happen. Otherwise, the game is rigged toward certain outcomes. Let us call such strings <span style="color:red">microstates</span>, micro in the sense that the string specifies all the flips exactly and therefore corresponds to only one outcome. On the contrary, when a person is in the state of "winning two dollars overall," we call this the <span style="color:red">macrostate</span>. Obviously, it is macro in the sense that there are multiple ways to win two dollars: "+-++-+", "++++--", "++--++", etc.

It is then obvious that macrostates correspond to one or more microstates, where the latter requires more information to specify. Recall the idea of fairness: all microstates must be equally likely in our coin flips. The question is: how much more likely is it for you to be net zero at the end of the sixth game than to be down 6 dollars?

To lose six dollars in a game of six coin flips, you must lose all six rounds. So the macrostate of "-6$" has only one microstate. But to be net zero, there are many more possibilities. As long as you win three games in total, you will be net zero. Now how many ways are there for you to win 3 games? The answer is 20. And since each microstate is equally likely to occur, we see that the macrostate of net zero is 20 times more likely than -6$. Denote the number of microstates in a macrostate as $\Omega$, and let $i, j$ be labels of a microstate. We then have:

$$\frac{P(0)}{P(-6)} = \frac{\sum_{i = 0}^{\Omega(0)} p(i)}{\sum_{j = 0}^{\Omega(-6)} p(j)} = \frac{\Omega(0)}{\Omega(-6)} = \frac{20}{1} = 20$$


We see that even though the game is fair, some macrostates are far more likely to occur because they are more "vague": they correspond to more microstates. And as we play more games, this phenomenon gets more exaggerated. Let us define the notional of the game, $N$, as the maximum money at stake. Let us compare how likely the game is to give an outcome near net zero for total numbers of 20, 400, and 2000 games. The results are shown below. We see that the distribution becomes far more concentrated around net zero. This is theoretically intuitive: as more games are played, the number of combinations of microstates near net zero grows much faster than the rest. The readers can investigate the mathematical details by themselves, derive the binomial distribution we used intensively in the last section, and conclude that the width of the distribution in the following plot shrinks polynomially, with exponent 1/2.

<a id="fig-coin-flip-payoff"></a>
![Normalized payoff distribution for 20, 400, and 2000 games](images/coin_flip_normalized_payoff.png)

*Figure 3. Normalized payoff distribution for 20, 400, and 2000 fair coin-flip games.*


To conclude, if you play more and more games, you will almost inevitably land somewhere near the net-zero center. And this "number of microstates" is what we call entropy. From the Boltzmann perspective, this is all just combinatorics. From Shannon's information theory perspective, a higher entropy means more randomness and less order. In the example given above, the macrostate of net zero is more random and chaotic because it can be any of many microstates. It has less order because -6$ means "------", which is very orderly, while net zero often means something like "+--+-++", which is not very neat, is it?

In other words, we propose that in the long term, things will NATURALLY and inevitably drift toward a state with higher entropy: more chaos, more randomness, and less order.


<a id="CWE"></a>
### 3.2 Coffee, wealth, and pessimism.

Entropy is a statistical property of large, complex systems, yet it governs many familiar processes. Why, for instance, does hot coffee cool in an air-conditioned room? The answer follows directly from the previous subsection. Imagine two rooms separated by a thin wall with a small aperture. Each room contains rapidly moving numbered balls, representing discrete units of thermal energy, and these balls can occasionally pass through the aperture. In the example below, Room A contains 3 balls and Room B contains 7. If the balls move randomly for a long time, how much more likely is it to observe an even split, with 5 balls in each room, than an extreme split, with all 10 balls in one room?

<a id="fig-thermal-exchange"></a>
![Thermal exchange between two connected rooms](images/thermal_exchange_two_rooms.svg)

*Figure 4. Random exchange of thermal-energy units between two connected rooms.*

This is the same combinatorial problem as the coin-flip example. A microstate specifies the location of every labelled ball, whereas a macrostate specifies only how many balls are on each side. The macrostate in which all 10 balls are on one side has only two microstates: all balls are on the left, or all balls are on the right. By contrast, there are 252 ways to place 5 balls on each side. For example, balls #1, #2, #3, #4, and #5 could be on the left, or balls #1, #4, #6, #8, and #9 could be on the left. Thus, the evenly divided macrostate is 126 times more likely than the extreme macrostate.

Since each ball is equally likely to be on the right or left in the fullness of time, it is essentially a coin flip. This is why [Figure 3](#fig-coin-flip-payoff) can also be read as a thermal-exchange diagram: the x-axis may be interpreted as the fraction of balls on the left side. As the number of balls increases from 20 to 2000, the distribution becomes sharply concentrated near an even split. A cup of hot coffee contains not 20 or 2000 atoms, but on the order of 2 × 10²⁵ atoms, while the surrounding air contains vastly more. The cooling of coffee is therefore not imposed by a separate rule of physics; it is a statistical consequence of overwhelmingly many more microstates in which thermal energy is dispersed into the surroundings than concentrated in the coffee. Energy can, in principle, flow in either direction, but for systems of this size the overwhelmingly probable outcome is that hot coffee loses heat to the room.

A naive reader at this point might think the examples above show that nature favours equality, since heat tends to spread evenly. But nothing could be further from the truth. Entropy does not favour equality itself; it favours the macrostate with the greatest number of possible microstates.

Consider a simple wealth experiment. Suppose 1,000 people each begin with $1,00 and repeatedly play rock-scissors-paper with one another at random. After each game, the loser pays the winner $1. Since everyone starts equally and the game is fair, one might expect wealth to remain roughly equal in the long run. But of course not. Over time, it is inevitable that a small number of people will hold a large share of the total wealth.

The reason is simple: perfect equality is an extremely specific state. Since money is not labelled, one dollar is the same as any other dollar, so there is only one allocation in which every person has exactly $1,00. Unequal distributions, however, can be arranged in vastly more ways. Person #1 could be rich, or person #84, or any combination of people, with many possible amounts assigned to each. At the opposite extreme, one person holding all the money is also highly specific and therefore unlikely. The most probable outcome lies somewhere between perfect equality and total concentration: unequal enough to allow many possible arrangements, but not so extreme that the arrangement becomes special again. This intermediate region is the maximum-entropy state. Thus, even when everyone begins equally and plays only fair games, most participants will eventually fall below the average, while a minority holds disproportionately more.

The simulation below illustrates the same mechanism with 1,000 participants. Each person begins with $100 and repeatedly plays a fair $1 game against a randomly chosen opponent. A person who reaches $0 cannot lose further money. Even under these symmetric rules, the initially equal distribution quickly spreads out and begins to resemble the Boltzmann-like exponential curve shown in red.

<a id="fig-wealth-rps-simulation"></a>
![Simulated wealth distribution under repeated fair games](images/wealth_rps_simulation.gif)

*Figure 5. Simulated wealth distribution for 1,000 people repeatedly playing fair $1 games over 1,000,000 rounds.*

A side note for curious readers: in the examples above, interchangeability matters enormously. Since entropy is a combinatorial idea in this picture we presented, the number of possible arrangements depends on whether the objects being counted are distinguishable. Dividing 10 labelled balls between two rooms is not the same problem as dividing 10 identical balls. The counting changes, and therefore the entropy changes. This is one reason elementary particles are so conceptually strange. A soccer ball, a mug, a molecule, or even an atom can in principle be labelled and tracked as an individual object. But an elementary particle cannot. Two electrons are not merely difficult to distinguish because our instruments are imperfect; they are identical in principle and cannot be labelled. This conclusion is supported by their observed statistical behaviour, among many other lines of evidence. If electrons could be labelled, even in principle, they would obey different statistical laws, and matter would have different thermodynamic properties.

Overall, the idea of increasing entropy teaches pessimism as an objective truth: in the long run, nothing in our universe escapes decay. Nature does not build high-speed railways, tall buildings, or bridges. If human beings build them and leave them alone, they will eventually collapse. This is not because physics specifically requires buildings to collapse, but because arranging atoms into a structure useful enough for human beings to live in is an extraordinarily specific state. There are vastly more ways for those atoms to be scattered, displaced, corroded, cracked, or otherwise arranged. All it takes is enough random processes over enough time.
Similarly, coffee cools, sand castles are washed away, wealth inequality intensifies, and the human body eventually ceases to function. Everything fails eventually. Not because some ancient prophet indoctrinated us with this idea of inevitable failure, but because success, as we define it, is usually highly specific. For a human being to remain alive, the heart, liver, lungs, brain, and countless other systems must keep functioning together. To have everything working at once is a narrow condition; to have at least one essential system fail allows many more possibilities. The same is true of a happy family: health, money, children, housing, work, affection, timing, luck. So many conditions must hold at once. As Leo Tolstoy famously wrote in what is now known as the Anna Karenina principle: “All happy families are alike; each unhappy family is unhappy in its own way.”

But beyond this pessimism, there are other lessons to draw. We should be grateful that human beings have come so far in finding ways to temporarily and locally reverse entropy’s increase on Earth. Futile as this may be in the longest run, we all benefit from the efforts of those who came before us: we do have hot coffee, air conditioners, bridges, and buildings. The point is therefore not to ask whether things will fail, because they certainly will, but to ask what we can do about it. It is not fruitful to sit in complete ignorance of this pessimism, nor to spend life mourning a lost golden age. Instead, if we acknowledge the intrinsic tendency of things to fail and still strive for a better world, we can exploit certain aspects of this pessimism. In the following chapters, I will show how this framework of thinking is particularly useful for the JSDA Class 1 exam, and perhaps for many other exams of a similar nature.

## Next Step
