# Reasoning in propositional logic theories: logical puzzles and exercises

## Slides by Chiara Ghidini and Maurizio Lenzerini

## Adapted by Giuseppe De Giacomo, Francesco Fuggitti, Fabio Patrizi


# Cards

## Consider a deck of cards where each card has a letter in one face and one number on the other. One such

## deck is said to be “balanced” if any card that has a vowel in one face has an even number on the other

## side. LetMbe a deck of 4 cards of each of which we are shown a face, as follows:

## card position 1 2 3 4

## writing on card face A 6 K 7

## What is the minimum number of cards to turn over to verify thatMis a balanced deck?


# Cards: solution

## Consider a deck of cards where each card has a letter in one face and one number on the other. One such

## deck is said to be “balanced” if any card that has a vowel in one face has an even number on the other

## side. LetMbe a deck of 4 cards of each of which we are shown a face, as follows:

## card position 1 2 3 4

## writing on card face A 6 K 7

## What is the minimum number of cards to turn over to verify thatMis a balanced deck?

## Solution:

## Formalize the rules capturing that a deck is balanced using a propositional theoryFso that each deck is

## an interpretation; then determine the minimum number of letters propositional whose truth value must be

## determined for verify thatMis aFpattern.


## Propositional letters:v 1 , v 2 , v 3 , v 4 (vocali), andp 1 , p 2 , p 3 , p 4 (pari)

## Axioms ofFand facts:{v 1 →p 1 , v 2 →p 2 , v 3 →p 3 , v 4 →p 4 }∪{v 1 , p 2 ,¬v 3 ,¬p 4 }

## Mas an intepretation:M(v 1 ) =M(p 2 ) =True, M(v 3 ) =M(p 4 ) =False

## Task: determine the minimum number of letters you have to verify in order to check whetherMcan be

## extended to a model ofF

## i card vi pi vi→pi

## 1 A True??

## 2 6? True True

## 3 K False? True

## 4 7? False?

## To complete the truth table we should know the value ofp 1 andv 4. Hence,d we have to turn two cards:

## card 1 and card 4.


# Three perfect logicians at the pub

## A perfect logician answers perfectly to every “boolean question”Q, with

## “yes” (if her/his knowledge impliesQtrue)

## “no” (if her/his knowledge impliesQfalse)

## “I do not know” (if her/his knowledge implies neitherQtrue, norQfalse)

## as possible answers.

## Three perfect logicians who have never met with each other enter into a pub and sit at the only table with

## free seats (exactly three seats). The waiter goes to the table and, since he is very busy, while cleaning the

## table, decides to ask collectively the following question: “Everybody at this table wants a beer?” The three

## logicians answer one by one, and after hearing the answers, the waiter brings exactly one beer at the table.

## The question for you is: Is the waiter a perfect logician?


# Three perfect logicians at the pub: solution

## Three perfect logicians who have never met with each other enter into a pub and sit at the only table with

## free seats (exactly three seats). The waiter goes to the table and, since he is very busy, while cleaning the

## table, decides to ask collectively the following question: “Everybody at this table wants a beer?” The three

## logicians answer one by one, and after hearing the answers, the waiter brings exactly one beer at the table.

## Is the waiter a perfect logician?

## We formalize the puzzle in terms of a theory (set of axioms) representing the knowledge of the waiter. The

## alphabet of the theory is simply constituted by the propositional lettersb 1 , b 2 , b 3 , b 4 , wherebimeans that

## logicianiwants a beer.

## The initial theoryK 0 is empty, because the waiter knows nothing.

## After the answer by logiciani(i= 1, 2 , 3 ) the theory changes and the new theory will be denoted by

## Ki. Thus,K 3 is the final theory.

## The waiter is a perfect logician if and only if, no matter what the three answers are,

## K 3 |= (b 1 ∧¬b 2 ∧¬b 3 )∨(¬b 1 ∧b 2 ∧¬b 3 )∨(¬b 1 ∧¬b 2 ∧b 3 )


# Three perfect logicians at the pub: solution

## InitiallyK 0 ={}; answers of the 1st logician:

## “yes”⇝impossible (logician 1 doesn’t know about the others)

## “no”⇝all future answers will be “no”,K 1 =K 2 =K 3 ={¬b 1 }possibile outcomes are 0, 1 or 2

## beers and the waiter should ask for more information

## “I do not know”⇝K 1 ={b 1 }; answers of the 2nd logician:

## ▶“yes”⇝impossible (logician 2 doesn’t know about logician 3)

## ▶“no” the third answer will be “no”,⇝K 2 =K 3 ={b 1 ,¬b 2 }, possibile outcomes are 1 or 2

## beers and the waiter should ask for more information

## ▶“I do not know”⇝K 2 ={b 1 , b 2 }, answers of the 3rd logician

```
⋆“yes”⇝K 3 ={b 1 , b 2 , b 3 }, the waiter should bring 3 beers
⋆“no”⇝K 3 ={b 1 , b 2 ,¬b 3 }, the waiter should bring 2 beers
⋆“I do not know”⇝impossible (logician 3 knows everything)
```
## Conclusion: the waiter is not a perfect logician, because in all cases

## K 3 ̸|= (b 1 ∧¬b 2 ∧¬b 3 )∨(¬b 1 ∧b 2 ∧¬b 3 )∨(¬b 1 ∧¬b 2 ∧b 3 )


# The 3 doors

## Problem

Kyle, Neal, and Grant find themselves trapped in a dark and cold dungeon. After a quick search the boys find three doors,
the first one red, the second one blue, and the third one green.
Behind one of the doors is a path to freedom. Behind the other two doors, however, is an evil fire-breathing dragon.
Opening a door to the dragon means certain death. On each door there is an inscription:

```
freedom freedom
```
```
this door
```
```
is behind
```
```
the blue door
```
```
freedom
```
```
is not behind is not behind
```
```
this door
```
Given the fact that at LEAST ONE of the three statements on the three doors is true and at LEAST ONE of them is
false, which door would lead the boys to safety?


# The 3 doors: solution

## Language

```
r:”freedom is behind the red door”
b:”freedom is behind the blue door”
g:”freedom is behind the green door”
```
## Axioms

(^1) ”behind one of the door is a path to freedom, behind the other two doors is an evil dragon”
(r∧¬b∧¬g)∨(¬r∧b∧¬g)∨(¬r∧¬b∧g)
(^2) ”at least one of the three statements is true”
r∨¬b
(^3) ”at least one of the three statements is false”
¬r∨b


# The 3 doors: solution

## Axioms

(^1) (r∧¬b∧¬g)∨(¬r∧b∧¬g)∨(¬r∧¬b∧g)
(^2) r∨¬b
(^3) ¬r∨b

## Solution

```
r b g 1 2 3 2 ∧ 3 1 ∧ 2 ∧ 3
False False False False True True True False
False False True True True True True True
False True False True False True False False
False True True False False True False False
True False False True True False False False
True False True False True False False False
True True False False True True True False
True True True False True True True False
```
```
Since{ 1 , 2 , 3 }|=g, freedom is behind thegreen door!
```

# Graph coloring

## Problem

## Provide the formalization in propositional logic of the graph coloring problem.

## Graph coloring problem: given a non-oriented graph withn > 0 nodes, check whether the

## graph isk-colorable, i.e., whether we can associate one of thek > 0 colors to each of its

## nodes in such a way that no pair of adjacent nodes have the same color.


# Graph coloring

## Problem

## Provide the formalization in propositional logic of the graph coloring problem.

## Graph coloring problem: given a non-oriented graphGwithn > 0 nodes, check whether the

## graph isk-colorable, i.e., whether we can associate one of thek > 0 colors to each of its

## nodes in such a way that no pair of adjacent nodes have the same color.

## Solution:

## Formalize the problem in terms of a propositional theoryTGwhose axioms are satisfied if and only

## if the graphGis colorable.


# Graph coloring: propositional formalization

## Language of theoryTG

```
For each 1 ≤i≤nand 1 ≤c≤k, coloricis a proposition, which intuitively means that”thei-th node ofGhas
theccolor”
For each 1 ≤i̸=j≤n, edgeijis a proposition, which intuitively means that”thei-th node is connected inG
with thej-th node”.
```
## Axioms of theoryTG

```
for each 1 ≤i≤n,
```
```
Wk
c=1coloric
”each node has at least one color”
for each 1 ≤i≤nand 1 ≤c̸=c′≤k, coloric→¬coloric′
”every node has at most 1 color”
for each 1 ≤i, j≤nand 1 ≤c≤k, edgeij→¬(coloric∧colorjc)
”adjacent nodes do not have the same color”
facts,
```
### V

```
edgeij
”all given edges are true”
```
It can be shown that every solution to the graph coloring problem forGcorresponds to a model ofTG, and, conversely,
every model ofTGcorresponds to a solution of the graph coloring problem forG.


# Sudoku

## Problem

Provide a formalization of the Sudoku game. Sudoku is a placement puzzle. The aim of the puzzle is to enter a numeral

from 1 through 9 in each cell of a grid, here a 9 × 9 grid made up of 3 × 3 subgrids (called ”regions”), starting with

various numerals given in some cells (the ”givens”). Each row, column and region must contain only one instance of each

numeral. Its grid layout is like the one shown in the following schema


# Sudoku: solution

## Problem

Provide a formalization of the Sudoku game. Sudoku is a placement puzzle. The aim of the puzzle is to enter a numeral

from 1 through 9 in each cell of a grid, here a 9 × 9 grid made up of 3 × 3 subgrids (called ”regions”), starting with

various numerals given in some cells (the ”givens”). Each row, column and region must contain only one instance of each

numeral. Its grid layout is like the one shown in the following schema

We provide a formalization of the Sudoku game as a propositional theory, so that any truth assignment to the

propositional variables that satisfy the axioms of the theory is a solution for the puzzle, and, conversely, every solution for

the puzzle corresponds to a truth assignment to the propositional variables that satisfy the axioms of the theory.


# Sudoku: solution

## Language of theoryTS

For 1 ≤n, r, c≤ 9 ,define the proposition
in(n, r, c)

which means that the numbernhas been inserted in the cross between rowrand columnc.


# Sudoku: solution

## Axioms of theoryTS

(^1) ”Every number from 1 to 9 appears in every row”
^^9
n=
(^9)
^
r=
(^9)
_
c=
in(n, r, c)

### !!

(^2) ”Every number from 1 to 9 appears in every column”
^^9
n=

### ^^9

```
c=
```
### _^9

```
r=
```
```
in(n, r, c)
```
### !!

```
3 ”Every numbers from 1 to 9 appears in every region (sub-grid)”
```
```
for any 0 ≤k, h≤ 2
```
### ^^9

```
n=
```
(^3)
_
r=
(^3)
_
c=
in(n, 3 ∗k+r, 3 ∗h+c)

### !!

(^4) ”No cell can contain more than one number”
for any 1 ≤n, n′, c, r≤ 9 andn̸=n′ in(n, r, c)→¬in(n′, r, c)
(^5) ”the givens”represented by appropriatein(n, r, c)


