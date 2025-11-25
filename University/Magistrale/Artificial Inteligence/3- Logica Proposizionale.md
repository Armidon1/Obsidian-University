# Artificial Intelligence

## A.Y. 2025/

## Prof. Fabio Patrizi


# Propositional Logic


### Motivating Example: the Wumpus World


### Wumpus World

initial state (^) [1,1] -> [2,1]


### Wumpus World

#### [1,1] -> [2,1] -> [1,1] -> [1,2] [1,1] -> [2,1] -> [2,2] -> [2,3]


### Wumpus World

- Agent cannot see pits or Wumpus
- Can only perceive breeze and stench
- Yet, it is able to infer position of pits and Wumpus indirectly
- How can the agent do so?
- Can we systematize the inference procedure?
- Yes, with logic!


### Propositional Logic

- Formalism for _representing_ the state of the world and _reasoning_ about it
- Based on _Propositions:_
    - Statements about the world which can be either _true_ or _false_
    - E.g.:
       - Proposition s1,2: "there is stench in cell [1,2]"
       - Proposition p3,3: "there is a pit in cell [3,3]"
       - Proposition b3,1: "there is breeze in cell [3,1]"
       - ...


### Building Blocks of Logical (Formal) Systems

Any Logical System must provide:

- Syntax: when does a string of characters is a _formula_ in the logic?
- Semantics: what is the _meaning_ of each formula?
- Inference system: how can we _infer_ new knowledge?
    - E.g.:
       - We know that: stench in [1,2], no Wumpus in [1,1], no Wumpus in[2,2]
       - Then we can infer: Wumpus in [1,3]


### Syntax of Propositional Logic

Propositional Alphabet:

- A (countable) set _P_ of _atomic propositions_ (or _atoms or variables_ )
    - s1,2, p3,3, wumpus_in_1_3,...
    - This is typically defined by the user (and is usually, but not always, finite)
- Logical _connectives_ :
    - ¬ negation (not)
    - ∧ conjunction (and)
    - ∨ disjunction (or)
    - ⊃ implication, also written as → (if then)
    - ↔ (material) equivalence (if and and only if, iff)
- Parenthesis symbols:
    - "(" and ")"


### Syntax of Propositional Logic

_Formulas_ of Propositional Logic are sequences of symbols from alphabet

Not all sequences are Propositional Logic formulas

The set of formulas is defined _inductively_


### Formulas of Propositional Logic

- Every proposition p∈ _P_ is a propositional formula (called _atomic formula_ )
- If φ and ψ are propositional formulas then the following are propositional
    formulas:
       - ¬ψ
       - φ ∧ ψ
       - φ ∨ ψ
       - φ ⊃ ψ
       - φ ↔ ψ
       - (φ)
- Nothing else is a propositional formula*

*can be omitted by saying that the set of formulas is define inductively


### Formulas of Propositional Logic

These are (propositional) formulas:

- s1,2 - _there is stench in [1,2]_ (^)

- s1,2∧p3,3 - _there is stench in [1,2] and a pit in [3,3]_
- s1,2∨p3,3 - _there is stench in [1,2] or a pit in [3,3]_
- b2,1⊃p1,1∨p2,2∨p3,2 - _if breeze in [2,1] then pit in [1,1] or [2,2] or [3,2]_
-

These are not formulas (just sequences of propositional symbols):

- ∧p
- (qp∧¬r∨∧(pp


### Operator Precedence

How do we read formula φ ∧ ψ ⊃ γ?

- (φ ∧ ψ) ⊃ γ (φ and ψ (together) imply γ)?
- φ ∧ (ψ ⊃ γ) (φ and ψ implies γ)?

Solved using operator precedence:

1. ¬
2. ∧
3. ∨
4. ⊃
5. ↔

Thus φ ∧ ψ ⊃ γ is to be read as: (φ ∧ ψ) ⊃ γ, because ∧ has higher precedence than ⊃


### Semantics of Propositional Logic

Semantics defines when a formula is true or false, depending on _whether the_

_propositional symbols it contains are true or false_

In order to assign a truth value to a formula, we need to know the truth value of its

symbols

E.g., whether formula P∧Q is true depends on truth value of P and Q


### Propositional Interpretations

A (propositional) _interpretation_ is a function _I_ assigning T (true) or F (false) to every
propositional symbol, i.e., _I_ : _P_ →{T,F}

Example: _I_ (s1,2)=; _I_ (b2,2)=F; _I_ (b1,2)=T

We represent an interpretation _I_ as a set _I_ ⊆ _P_ under the convention that:

```
I (p)=T if and only if p∈ I
```
Example:

I={s1,2,b1,2} represents interpretation I above

Propositional interpretations are sometimes called _propositional models_


### Semantics of Propositional Logic

We define when a formula φ is true under an interpretation _I_ (written _I_ ⊧ φ)
inductively as follows:

- if φ is an atom, then _I_ ⊨ φ iff φ∈ _I_
- if φ=¬ψ then iff _I_ ⊭φ
- if φ=ψ∧γ then _I_ ⊨ φ iff _I_ ⊨ ψ and _I_ ⊨ γ
- if φ=ψ∨γ then _I_ ⊨ φ iff _I_ ⊨ ψ or _I_ ⊨ γ
- if φ=ψ⊃γ then _I_ ⊨ φ iff _I_ ⊭ ψ or _I_ ⊨ γ
- if φ=ψ↔γ then _I_ ⊨ φ iff _I_ ⊨ ψ⊃γ and _I_ ⊨ γ⊃ψ
- if φ=(ψ) then _I_ ⊨ φ iff _I_ ⊨ ψ

When _I_ ⊨ φ we also say that _I satisfies_ φ and call _I_ a _model_ of φ


### Truth Tables

The semantics of propositional formulas can also be defined using truth tables

```
ψ γ ¬ψ ψ∧γ ψ∨γ ψ⊃γ ψ↔γ (ψ)
```
```
F F T F F T T F
F T T F T T F F
T F F F T F F T
T T F T T T T T
```

### Semantics of Propositional Logic

For _I_ ={p}, does _I_ ⊨ (p∧q)∨(r⊃s)?

Let's apply the rules above:

- _I_ ⊨ (p∧q)∨(r⊃s) iff _I_ ⊨ (p∧q) or _I_ ⊨ (r⊃s)
- _I_ ⊨(p∧q) iff _I_ ⊨ p and _I_ ⊨ q
- _I_ ⊨ p iff p∈ _I_ , thus **_I_** ⊨ **p**
- _I_ ⊨ q iff q∈ _I_ , thus **_I_** ⊭ **q**
- since _I_ ⊭q, we have that **_I_** ⊭ **(p** ∧ **q)**
- _I_ ⊨ (r⊃s) iff _I_ ⊭ r or _I_ ⊨ s
- _I_ ⊭r iff r∉I, thus **_I_** ⊭ **r** and hence **_I_** ⊨ **(r** ⊃ **s)**
- since _I_ ⊨ (r⊃s) we have that **_I_** ⊨ **(p** ∧ **q)** ∨ **(r** ⊃ **s)**


### Algorithm for Checking I ⊨ φ

Boolean check( _I,_ φ){ // Returns true iff _I_ ⊨ φ

```
if φ is an atom then return true if φ∈ I, false otherwise
if φ=¬ψ then return (!check( I, ψ))
if φ=ψ∧γ then return (check( I, ψ) && check( I, γ))
if φ=ψ∨γ then return (check( I, ψ) || check( I, γ))
if φ=ψ⊃γ then return ((not check( I, ψ)) || check( I, γ))
if φ=ψ↔γ then return (check( I, ψ⊃γ) && check( I, γ⊃ψ))
if φ=(ψ) then return check( I, ψ)
```
}


### Useful Equivalences

The following semantic equivalences are easy to verify:

- ψ⊃γ has the same meaning as ¬ψ∨γ
- ψ⊃γ has the same meaning as ¬γ⊃¬ψ
- ¬(ψ∨γ) has the same meaning as ¬ψ∧¬γ
- ¬(ψ∧γ) has the same meaning as ¬ψ∨¬γ
- ψ⊃¬γ has the same meaning as ψ⊃¬γ


### Knowledge Bases

A set 𝚪 of propositional formulas is also called a _Knowledge Base_ (because it

provides an agent with knowledge about some world)

A KB 𝚪 can be used to reason about the world


### Wumpus World Knowledge Base

Let's build a simple Knowledge Base 𝚪 formalizing valid maps in Wumpus World

Start with Atomic Propositions (omit gold for simplicity):

px,y - pit in x,y

wx,y- Wumpus in x,y

bx,y - breeze in x,y

sx,y - stench in x,y

lx,y - agent in in x,y

for x,y ∈ {1,2,3,4}


### Wumpus World Knowledge Base

Then, add formulas describing constraints on maps

1. Wumpus is in **exactly** one square:

## ∨wx,y for x,y ∈ {1,2,3,4} (this says in at least one square )

```
¬(wx,y∧wx',y') for (x,y)≠(x',y') (all these together say in at most one square )
```
Observe:

## ∨wx,y for x,y ∈ {1,2,3,4} shortcut for:

```
w1,1∨w1,2∨w1,3∨w1,4∨w2,1∨...∨w2,4∨w3,1∨...∨w3,4∨w4,1∨...∨w4,4 (same for
```
## ∧)


### Wumpus World Knowledge Base

2. Square [x,y] has stench iff Wumpus in [x+1,y] or [x,y+1] or [x-1,y] or [x,y-1]

(for squares out of bounds proposition is dropped):

```
sx,y ↔ wx+1,y∨wx,y+1∨wx-1,y∨wx,y-1
```

### Wumpus World Knowledge Base

3. Square (x,y) has breeze iff pit in [x+1,y] or [x,y+1] or [x-1,y] or [x,y-1]

(for squares out of bounds proposition is dropped):

```
bx,y ↔ px+1,y∨px,y+1∨px-1,y∨px,y-1
```
4. No pit in [1,1]: ¬p1,1


### Logical Inference in Wumpus World

Every interpretation corresponds to a map

configuration (and viceversa). For map in figure:

{l1,1,b2,1,p3,1,b4,1,s1,2,b3,2,b2,3,s2,3,p3,3,b4,3,s1,4,b3,4,p4,4}

But interpretations model also maps inconsistent

with KB

Only the interpretations that satisfy **all** formulas in

KB are relevant!


### Logical Inference in Wumpus World

The interpretation associated with this map

satisfies all formulas in KB

{l1,1,b2,1,p3,1,b4,1,s1,2,b3,2,b2,3,s2,3,p3,3,b4,3,s1,4,b3,4,p4,4}


### Logical Inference in Wumpus World

The interpretation associated with this map

**does not** satisfy all formulas in KB

{l1,1,b2,1,p3,1,b4,1,s1,2,b3,2, **b2,2** ,b2,3,s2,3,p3,3,b4,3,s1,4,b3,4,p4,4}

The following formula is not satisfied:

```
b2,2 ↔ p3,2∨p2,3∨p1,2∨p2,1
```

### Logical Inference in Wumpus World

As the agent perceives features,some maps

(possibly all) are ruled out

This map cannot have a pit in [1,2], as the formula

```
b1,1 ↔ p1,2∨p2,1
```
would not be satisfied: agent knows ¬b1,1

thus both p1,2 and p2,1 must be false

#### ????

#### ???

#### ????

#### ?

#### ??


### Logical Inference in Wumpus World

Before moving, agent checks, e.g., if pit can be in [1,2]

How?

- Consider observations collected so far:
    Obs={¬b1,1, ¬p1,1, ¬w1,1, ¬s1,1, b1,2, ¬s1,2¬p1,2, ¬w1,2}
- Check whether there exists a model of **all**
    formulas in 𝚪 ∪ Obs ∪ {p2,1}

If one such model exists, there exists a valid map

with breeze in [2,1], agent in [1,1] and pit in [1,2]

(thus moving to [1,2] is unsafe)

#### ????

#### ???

#### ????

#### ?

#### ??


### Propositional Satisfiability

The problem of checking whether there exists an interpretation _I_ that satisfies a
propositional formula φ is called

```
Propositional Satisfiability Problem (SAT)
```
This is among the most (if not **the** most) studied problems in AI (and CS)

It allows for checking whether a world _I_ that satisfies certain properties is possible

Observation: checking whether _I_ ⊨ φ 1 and _I_ ⊨ φ 2 ,..., and _I_ ⊨ φn is equivalent to

checking whether _I_ ⊨ φ 1 ∧ φ 2 ∧...∧ φn (not applicable if n=∞)


### Satisfiable Formulas

A propositional formula φ is said to be _satisfiable_ if there exists an interpretation _I_
such that _I_ ⊨ φ

If φ doesn't have any model, it is said to be _unsatisfiable_

Examples:

- formula ¬(a∨b)→c is satisfiable: e.g., _I_ ={c}
- formula a∧(a→b)∧(b→¬a) is unsatisfiable


### Checking Satisfiability with Truth Tables

One naïve way to check a formula for satisfiability consists in constructing the truth
table of the formula

The truth table lists all the interpretations of the propositions occurring in the
formula and associates them with the truth value of the formula

To check satisfiability, we can check whether some interpretation exists which
satisfies the formula


### Checking Satisfiability with Truth Tables

Example: for ¬(a∨b)→c

All interpretations but the

first one are models

```
a b c (a ∨ b) ¬(a ∨ b) ¬(a ∨ b)
→c
F F F F T F
F F T F T T
F T F T F T
F T T T F T
T F F T F T
T F T T F T
T T F T F T
T T T T F T
```

### Checking Satisfiability with Truth Tables

Example: for a∧(a→b)∧(b→¬a)

No interpretation is a model

```
a b ¬a (a→b) (b→¬a) a ∧ (a→b) ∧
(b→¬a)
F F T T T F
F T T T T F
T F F F T F
T T F T F F
```

### Checking Satisfiability with Truth Tables

Checking satisfiability with truth tables is not the smartest approach

Requires listing all 2|P| interpretations (P: propositions occurring in formula)

We shall see better approaches


### Valid Formulas

A propositional formula φ is said to be _valid_ if _I_ ⊨ φ for all interpretations _I_

Examples:

- (a→b)∨(b→¬a) is valid
- (a→b) is satisfiable but not valid


### Checking Validity with Truth Tables

To check validity, we can check whether all interpretations satisfy the formula

Also for this, better approaches exist

Example: (a→b)∨(b→¬a)

```
a b (a→b) (b→¬a) (a→b) ∨ (b→¬a)
F F T T T
F T T T T
T F F T T
T T T F T
```

### Checking Validity with Truth Tables

Example: (a→b)

```
a b (a→b)
F F T
F T T
T F F
T T T
```

### Satisfiability, Unsatisfiability, Validity

By the definitions of satisfiability, unsatisfiability and validity, we have that:

- if φ is valid then it is satisfiable
- if φ is unsatisfiable then it is not valid
- φ is satisfiable iff ¬φ is not valid
- φ is valid iff ¬φ is unsatisfiable
- φ is not valid iff ¬φ satisfiable
- φ is unsatisfiable iff ¬φ is valid

Proving the above is a simple exercise


### Valid, Satisfiable and Unsatisfiable

```
Satisfiable
```
```
Unsatisfiable
```
```
Valid
```
```
Not valid
```
#### ↔

#### ↔

#### ↔


### Satisfiable, Unsatisfiable and Valid Knowledge Bases

All previous notions can be lifted to KBs

An interpretation _I_ is a _model_ of (or _satisfies_ ) a KB 𝚪 = {φ 1 ,...,φn}, written _I_ ⊨ 𝚪, if

_I_ ⊨ φ 1 ,..., _I_ ⊨ φn (which is equivalent to _I_ ⊨ φ 1 ∧...∧φn – only for finite KBs!)

A KB 𝚪 = {φ 1 ,...,φn} is:

- _satisfiable_ if there exists an interpretation _I_ such that _I_ ⊨ 𝚪
- _unsatisfiable_ if there exists no interpretation _I_ such that _I_ ⊨ 𝚪
- _valid_ if _I_ ⊨ 𝚪, for all interpretations _I_

Observation: all definitions apply also to infinite KBs


### Using Satisfiability in Wumpus World

Let's check whether there _can_ be a pit in [1,2]

- Assume observations collected so far:
    Obs={¬b1,1,¬p1,1,¬w1,1,¬s1,1,b1,2,¬s1,2,¬p1,2,¬w1,2}
- Check whether there exists a model of **all**
    formulas in 𝚪 ∪ Obs ∪ {p1,2}

For simplicity, we consider only formulas from 𝚪

mentioning squares [1,1], [1,2] or [2,1] (the only

ones affected by observations)

#### ????

#### ???

#### ????

#### ?

#### ??


### Using Satisfiability in Wumpus World

Is this set of formulas satisfiable?

w1,1∨w1,2∨w2,1∨w2,2

¬(w1,1∧w1,2); ¬(w1,1∧w2,1); ¬(w2,1∧w1,2)

s1,1 ↔ w2,1∨w1,2 ; s1,2 ↔ w1,1∨w2,2∨w1,3 ; s2,1 ↔ w1,1∨w2,2∨w3,1

b1,1 ↔ p2,1∨p1,2 ; b1,2 ↔ p1,1∨p2,2∨p1,3 ; b2,1 ↔ p1,1∨p2,2∨p3,1

```
¬b1,1,¬p1,1,¬w1,1,¬s1,1,b1,2,¬s1,2,¬p1,2,¬w1,2
```
p1,2

```
Wumpus KB
```
```
Collected Observations
```
```
Formula of interest
```

### Using Satisfiability in Wumpus World

Assume _I_ is an interpretation satisfying all the formulas above

Then, in particular:

1. _I_ ⊨ p1,2
2. _I_ ⊨ b1,1 ↔ p2,1∨p1,2

By 1., it follows that p2,1∈ _I_

By 2. and p2,1∈ _I_ , it follows that b1,1∈ _I_

But if b1,1∈ _I_ then _I_ ⊭¬b1,1

Therefore no _I_ satisfying all formulas above may exist, thus **no pit can be in [1,2]**


### Using Satisfiability in Wumpus World

We can also check whether Wumpus (instead of pit) can be in [1,2]:

w1,1∨w1,2∨w2,1∨w2,2

¬(w1,1∧w1,2); ¬(w1,1∧w2,1); ¬(w2,1∧w1,2)

s1,1 ↔ w2,1∨w1,2 ; s1,2 ↔ w1,1∨w2,2∨w1,3 ; s2,1 ↔ w1,1∨w2,2∨w3,1

b1,1 ↔ p2,1∨p1,2 ; b1,2 ↔ p1,1∨p2,2∨p1,3 ; b2,1 ↔ p1,1∨p2,2∨p3,1

```
¬b1,1,¬p1,1,¬w1,1,¬s1,1,b1,2,¬s1,2,¬p1,2,¬w1,2
```
w1,2

```
Wumpus KB
```
```
Collected Observations
```
```
Formula of interest
```

### Propositional Satisfiability

Whenever we want to check whether some (propositional) property is _possible_ , we

need to check for _satisfiability_

We want to automatize this procedure

Algorithms for satisfiability check (Later on)


### Exercise

Check whether the following formulas are valid, satisfiable, or unsatisfiable


### (Propositional) Logical Implication

We might also be interested in checking whether **_all models_** _that satisfy KB_ 𝚪 _and_

_observations have a Wumpus in [1,3], i.e., whether we_ **_are sure_** _Wumpus is there_

Formula φ _logically implies_ ψ (φ⊨ψ), if for every _I_ s.t. _I_ ⊨ φ, it is the case that _I_ ⊨ ψ

Corresponds to requiring that the set of models of ψ includes that of φ

(Notice we are _overloading_ ⊨ for satisfaction and logical implication)

Can be lifted to KBs: 𝚪 ⊨ ψ, if for every _I_ s.t. _I_ ⊨ 𝚪, it is the case that _I_ ⊨ φ

Notice that ∅ ⊨ φ, simply written as ⊨ φ, is equivalent to saying that _φ is valid_


### Logical Implication

Which ones of the following implications hold?


### Logical Implication

Is there a Wumpus in [1,3]?

Wumpus-world KB: 𝚪

Observations:

_O_ ={¬b1,1;¬p1,1;¬w1,1;¬s1,1;b2,1;¬s2,1;¬w2,1; ... **¬w2,2;s1,2;s2,3** }

Formula of interest: w1,3 (Wumpus in [1,3])

Does 𝚪∪ _O_ ⊨ w1,3?

#### ??

#### ?

#### ?

#### ?

#### ??

#### ?

#### ?

#### ?

#### ?

#### ?


### Logical Equivalence

We can also be interested in checking whether two formulas (or KBs) have the
_same meaning_.

φ and ψ are _logically equivalent_ (φ☰ψ) if every interpretation _I_ is s.t. _I_ ⊨ φ iff _I_ ⊨ ψ

Corresponds to requiring that φ and ψ have _exactly the same models_ and is
equivalent to: φ ⊨ ψ _and_ ψ ⊨ φ


### Logical Implication and Equivalence on KBs

Logical implication and logical equivalence can be lifted to KBs 𝚪 and 𝚪'

𝚪 ⊨ 𝚪', if for every _I_ s.t. _I_ ⊨ 𝚪, it is the case that _I_ ⊨ 𝚪'

(The set of models of 𝚪' includes that of 𝚪)

𝚪 ☰ 𝚪', if _I_ ⊨ 𝚪 and _I_ ⊨ 𝚪'

(The set of models of 𝚪 and 𝚪' match )


### Properties of Propositional Logical Implication

Reflexivity: if φ∈𝚪 then 𝚪 ⊨ φ

Ex falso (sequitur) quodlibet: if 𝚪 is unsatisfiable then 𝚪⊨φ for every φ

Monotonicity: if 𝚪⊨φ then 𝚪∪𝚪'⊨φ

Cut: if 𝚪 ⊨ φ and 𝚪'∪{φ} ⊨ φ' then 𝚪∪𝚪' ⊨ φ'

Compactness: if 𝚪 ⊨ φ then there is a finite 𝚪'⊆ 𝚪 s.t. 𝚪' ⊨ φ

Deduction Theorem: if 𝚪∪{φ} ⊨ φ' then 𝚪 ⊨ φ→φ'

Deduction Principle: 𝚪∪{φ} ⊨ φ' iff 𝚪 ⊨ φ→φ'

**Refutation Principle:** 𝚪 ⊨ **φ iff** 𝚪∪ **{¬φ} is unsatisfiable**


