## First order logic

```
Introduction, syntax and semantics
```
```
Luciano Serafini – Maurizio Lenzerini
```
FBK-IRST, Trento, Italy – Sapienza Universit`a di Roma

```
Revised and adapted by F. Patrizi
```

## Expressivity of propositional logic - I

### Question

Try to express in Propositional Logic the following statements:
Mary is a person
John is a person
Mary is mortal
Mary and John are siblings

### A solution

Through atomic propositions:
Mary-is-a-person
John-is-a-person
Mary-is-mortal
Mary-and-John-are-siblings


## Problem with previous solution

Mary-is-a-person
John-is-a-person
Mary-is-mortal
Mary-and-John-are-siblings
How do we linkMaryof the first sentence toMaryof the third sentence? Same withJohn. How
do we linkMaryandMary-and-John?


## Expressivity of propositional logic - II

### Question

Try to express in Propositional Logic the following statements:
All persons are mortal;
There is a person who is a spy.

### A solution

We can give all people a name and express this fact through atomic propositions:
Mary-is-mortal∧John-is-mortal∧Chris-is-mortal∧...∧Michael-is-mortal
Mary-is-a-spy∨John-is-a-spy∨Chris-is-a-spy∨...∨Michael-is-a-spy


## Problem with previous solution

Mary-is-mortal∧John-is-mortal∧Chris-is-mortal∧...∧Michael-is-mortal
Mary-is-a-spy∨John-is-a-spy∨Chris-is-a-spy∨...∨Michael-is-a-spy
The representation is not compact and generalization patterns are difficult to express.
What if we do not know all the people in our “universe”? How can we express the statement
independently from the people in our “universe”?


## Expressivity of propositional logic - III

### Question

Try to express in Propositional Logic the following statements:
Every natural number is either even or odd

### A solution

We can use two families of propositionseveniandoddifor everyi≥ 1 , and use the set of formulas

```
{oddi∨eveni|i≥ 1 }
```

## Problem with previous solution

```
{oddi∨eveni|i≥ 1 }
```
What happens if we want to state this in one single formula? To do this we would need to write
an infinite formula like:
(odd 1 ∨even 1 )∧(odd 2 ∨even 2 )∧...

and this cannot be done in propositional logic.


## Expressivity of propositional logic -IV

### Question

Express the statements:
the father of Luca is Italian

### Solution (Partial)

```
mario-is-father-of-luca→mario-is-italian
michele-is-father-of-luca→michele-is-italian
...
```

## Problem with previous solution

mario-is-father-of-luca→mario-is-italian
michele-is-father-of-luca→michele-is-italian
...
This statement strictly depend from a fixed set of people. What happens if we want to make this
statement independently of the set of persons we have in our universe?


## Why first order logic?

Because it provides a way of representing information like the following one:

(^1) Mary is a person;
(^2) John is a person;
(^3) Mary is mortal;
(^4) Mary and John are siblings
(^5) Every person is mortal;
(^6) There is a person who is a spy;
(^7) Every natural number is either even or odd;
(^8) The father of Luca is Italian
and also to infer the third one from the first one and the fifth one.


## First order logic

While propositional logic assumes that the world to be formalized is constituted by facts
corresponding to propositions, first-order logic (like natural language) assumes that the world is
constituted by:
Individual objectes, denoted by Constants: mary, john, 1, 2, 3, red, blue, world war 1, world
war 2, 18th Century...
Functional means to refer to objects, denoted by Functions: the father of, the best friend, the
third inning of,...
Properties and relations, denoted by Predicates: Mortal, Prime, IsBrotherOf, Bigger than,
Inside, IsPartOf, HasColor, Owns,...

In the following, we define first-order logic with equality.


## Constants and Predicates

```
Mary is a person
John is a person
Mary is mortal
Mary and John are siblings
```
In FOL it is possible to build an atomic propositions by applying a predicate to constants
Person(mary)
Person(john)
Mortal(mary)
Siblings(mary,john)


## Quantifiers and variables

```
Every person is mortal;
There is a person who is a spy;
Every natural number is either even or odd;
```
In FOL it is possible to build propositions by applying universal (existential) quantifiers to
variables. This allows to quantify to arbitrary objects of the universe.
∀x.Person(x)→Mortal(x)
∃x.Person(x)∧Spy(x)
∀x.(Odd(x)∨Even(x))


## Functions

```
The father of Luca is Italian.
```
In FOL it is possible to build propositions by applying a function to a constant, and then a
predicate to the resulting object.
Italian(fatherOf(Luca))


## Syntax of FOL

The alphabet of FOL is composed of two sets of symbols:

### Logical symbols

```
the logical constants⊥(false) and⊤(true)
propositional logical connectives∧,∨,→,¬,↔
the quantifiers∀,∃
a denumerable set of variable symbolsx 1 ,x 2 ,...
the equality predicate symbol=(optional)
```
### Non logical symbols⟨c 1 ,c 2 ,...,f 1 ,f 2 ,...,P 1 ,P 2 ,...⟩

```
a denumerable setc 1 ,c 2 ,...of constants
a denumerable setf 1 ,f 2 ,...of function symbols each of which is associated with its arity
≥ 1 (i.e., number of arguments)
a denumerable setP 1 ,P 2 ,...of predicate (or relational) symbols each of which is associated
with its arity≥ 0 (i.e., number of arguments)
```

## Non logical symbols - Example

Non logical symbols depend on the domain we want to model. They should have an intended
meaning in such a domain.

### Example (Domain of arithmetics)

```
symbol type arity intended meaning
0 constant 0 ∗ the smallest natural number
succ(·) function 1 the function that given a number returns its successor
+(·,·) function 2 the function that given two numbers returns the number cor-
responding to the sum of the two
<(·,·) predicate 2 the “less than” relation between natural numbers
```
∗A constant can be considered as a function with arity equal to 0


## Non logical symbols - Example

### Example (Domain of arithmetics - extended)

The basic language of arithmetics can be extended with further symbols e.g:
symbols type arity intended meaning
0 constant 0 the smallest natural number
succ(·) function 1 the function that given a number returns its successor
+(·,·) function 2 the function that given two numbers returns the number cor-
responding to the sum of the two
∗(·,·) function 2 the function that given two numbers returns the number cor-
responding to the product of the two
<(·,·) predicate 2 the “less than” predicate between natural numbers
≤(·,·) predicate 2 the “less than or equal to” predicate between natural numbers


## Non logical symbols - Example

### Example (Domain of strings)

```
symbols type arity intended meaning
ε constant 0 the empty string
“a”,“b”, constants 0 the strings containing one single character of the latin alphabet
concat(·,·) function 2 the function that given two strings returns the string which is
the concatenation of the two
subst(·,·,·) function 3 the function that replaces all the occurrence of a string with
another string in a third one
< predicate 2 alphabetic order on the strings
substring(·,·) predicate 2 the relation that states if a string is contained in another string
```

## Terms and formulas of FOL

In the following, we writeg/nto indicate that the function or predicate symbolghas arityn.

### Terms

```
every constantcand every variablexis a term;
ift 1 ,...,tnare terms andf/nis a function symbol, thenf(t 1 ,...,tn)is a term.
```
### Well formed formulas

```
ift 1 andt 2 are terms thent 1 =t 2 is a formula;
Ift 1 ,...,tnare terms andP/nis a predicate symbol, thenP(t 1 ,...,tn)is a formula (if
n= 0, then the formula is written simply asP);
ifAandBare formulas then⊥,⊤,A∧B,A→B,A∨B,¬A,A↔B,(A)are formulas;
ifAis a formula andxa variable, then∀x.Aand∃x.Aare formulas (also written simply as
∀xAand∃xA).
```

## Examples of terms and formulas

In the following examples we use the function symbolsf 1 / 2 ,f 2 / 3 ,g/ 2 ,h/ 3 , the variablesx,y,z,
the constantsa,b,cand the predicate symbolsP/ 1 ,A/ 1 ,B/ 1 ,Q/ 2.

### Example (terms)

```
x
c
f 1 (x,c)
f 2 (g(x,y),h(x,y,z),y)
```
### Example (formulas)

```
f 1 (a,b) =c
P(c)
∃x(A(x)∨B(y))
P(x)→∃y.Q(x,y)
```

## Semantics of FOL

### FOL interpretation

A first order interpretation for the alphabet⟨c 1 ,c 2 ,...,f 1 ,f 2 ,...,P 1 ,P 2 ,...⟩is a pair⟨∆,I⟩
where
∆is a non empty set called interpretation domain
Iis a function, called interpretation function such that
▶I(ci)∈∆ for each constantci
▶I(fi) : ∆n→∆ for each function symbolfi/n
▶I(Pi)⊆∆n for each predicate symbolPi/n

In other words,Iassociates to each constant an element of the domain∆, to each function
symbolfi/na totaln-ary function on the domain∆, and to each predicate symbolPiann-ary
relation on the domain∆.

In the following, we sometime usecI,fIandPIinstead ofI(c),I(f)andI(P), respectively.


## Example of interpretation

### Example (of interpretation)

```
Symbols Constants:alice,bob,carol,robert
Function symbol:mother-of/ 1
Predicate symbol:friends/ 2
```
```
Domain ∆ ={ 1 , 2 , 3 , 4 ,.. .}
Interpretation I(alice) = 1,I(bob) = 2,I(carol) = 3,
I(robert) = 2
```
```
I(mother-of) =M
```
```
M(1) = 3
M(2) = 1
M(3) = 4
M(n) =n+ 1forn≥ 4
I(friends) =F=
```
```



```
```
⟨ 1 , 2 ⟩, ⟨ 2 , 1 ⟩, ⟨ 3 , 4 ⟩,
⟨ 4 , 3 ⟩, ⟨ 4 , 2 ⟩, ⟨ 2 , 4 ⟩,
⟨ 4 , 1 ⟩, ⟨ 1 , 4 ⟩, ⟨ 4 , 4 ⟩
```
```



```

## Example (cont’d)

# 6

# Alice Bob Carol Robert

# 4

# M

# M

# Syntax

# Semantics

# M

# 2

# 1

# M

# 3

# F

# F F F

# F

# Mother Friend

# 5


## Interpretation of terms

### Definition (Assignment)

An assignmentαforIis a function from the set of variables to∆.

Ifαis an assignment forI, thenα[x/d]denotes the assignment forIthat coincides withαon all
the variables butx, which is associated tod.

### Definition (Interpretation of terms)

The interpretation of a termtw.r.t. the assignmentα, in symbolstI,αis recursively defined as
follows (wherexis a variable,ca constant andf/na function symbol):

```
xI,α = α(x)
cI,α = I(c)
f(t 1 ,...,tn)I,α = I(f)(tI 1 ,α,...,tIn,α)
```

## FOL Satisfaction of formulas

### Definition (Satisfaction of a formula byIw.r.t.α)

The following rules establish when an interpretationIsatisfies a formulaφw.r.t. the assignment
α(written as(I,α)|=φ):
(I,α)|=⊤ and (I,α)̸|=⊥
(I,α)|=t 1 =t 2 if tI 1 ,αis the same astI 2 ,α
(I,α)|=P(t 1 ,...,tn) if ⟨tI 1 ,α,...,tIn,α⟩∈I(P)
(I,α)|=φ∧ψ if (I,α)|=φand(I,α)|=ψ
(I,α)|=φ∨ψ if (I,α)|=φor(I,α)|=ψ
(I,α)|=φ→ψ if (I,α)̸|=φor(I,α)|=ψ
(I,α)|=¬φ if (I,α)̸|=φ
(I,α)|=φ↔ψ if (I,α)|=φif and only if (I,α)|=ψ
(I,α)|= (φ) if (I,α)|=φ
(I,α)|=∃xφ if (I,α[x/d])|=φfor somed∈∆
(I,α)|=∀xφ if (I,α[x/d])|=φfor alld∈∆


## Example (cont’d)

### Exercise

Letαbe such thatα(x) = 2, and letIbe the interpretation defined few slides ago. Check
whether the following are true:

(^1) (I,α)|=Alice=Bob
(^2) (I,α)|=Robert=Bob∧friends(Carol,mother(Carol))
(^3) (I,α[x/2])|=¬(x=Bob)
(^4) (I,α)|=∃x¬friends(x,mother(x))
(^5) (I,α)|=∀x∃y friends(x,y)
(^6) (I,α)|=∀x∃y¬friends(x,y)
(^7) (I,α)|=∀x∀y friends(x,y)→friends(y,x)


## Free variables

A free occurrence of a variablexis an occurrence ofxwhich is not bound to a (universal or
existential) quantifier.

### Definition (Inductive definition of free occurrence)

```
any occurrence ofxintkis free inP(t 1 ,...,tk,...,tn)
any free occurrence ofxinφor inψis also free inφ∧ψ,ψ∨φ,ψ→φ,ψ↔φand¬φ
any free occurrence ofxinφ, is free in∀y.φand∃y.φifyis distinct fromx.
```
Free variables represent individuals which must be instantiated to make the formula a meaningful
proposition.

### Definition (Free variable)

A variablexis free inφ(denote byφ(x)) if there is at least a free occurrence ofxinφ.


## Free variables - examples

### Intuitively..

Free variables represents individuals which must be instantiated to make the formula a meaningful
proposition.
friends(Alice,x) xfree
∀x(friends(Alice,x)∧friends(Bob,x)) xnot free
(∀xfriends(Alice,x))∧friends(Bob,x) xfree
∀y.friends(Bob,y) no free variables
sum(x,3) = 12 xfree
∃x.(sum(x,3) = 12) no free variables
∃x.(sum(x,y) = 12) yfree


## Open and closed formulas

### Definition (Ground/Closed/Open Formula)

A formulaφis ground if it does not contain any variable.
A formula is open if it contains at least one free variable, closed otherwise.
Obviously, all ground formulas are closed.

It is not difficult to see that when we interpret a closed formula in an interpretation, we do not
actually need any assignment. Indeed, it can be shown that ifα 1 andα 2 coincide on the variables
that are free inφ, then(I,α 1 )|=φif and only if(I,α 2 )|=φ. For this reason, in the following,
wheneverφis a closed formula, we write
I |=φ

to mean thatIsatisfiesφ(independently from any assignment).


## An example of representation in FOL

### Example (Language)

```
constants functions/arity Predicate/arity
Aldo
Bruno
Carlo
Math
DataBase
0, 1,... , 10
```
```
mark/2
best-friend/1
```
```
attend/2
friend/2
student/1
course/1
less-than/2
```
### Example (Terms)

```
Intended meaning
an individual named Aldo
the mark 1
Bruno’s best friend
anything
Bruno’s mark in Math
somebody’s mark in DataBase
Bruno’s best friend mark in Math
```
```
term
Aldo
1
best-friend(Bruno)
x
mark(Bruno,Math)
mark(x,DataBase)
mark(best-friend(Bruno),Math)
```

## An example of representation in FOL (cont’d)

### Example (Formulas)

```
Intended meaning
Aldo and Bruno are the same personCarlo is a person and Math is a course
Aldo attends MathCourses are attended only by students
every course is attended by somebodyevery student attends something
there is a student who attends all the coursesevery course has at least two attenders
Aldo’s best friend attend all the coursesattended by Aldo
Aldo and his best friend have the same markin Math
A student can attend at most two courses
```
```
Formula
Aldoperson=(BrunoCarlo)∧course(Math)
attend∀x∀y(attend(Aldo, Math(x, y)→)course(y)→student(x))
∀∀xx((coursestudent(x()x)→ ∃→ ∃y attendy attend(y, x(x, y))))
∃∀xx((studentcourse(x(x))→ ∃∧∀yy(∃coursez(attend(y)(y, x→attend)∧attend(x, y()))z, x)∧¬y=z))
∀x(attend(Aldo, x)→attend(best-friend(Aldo), x))
mark(best-friend(Aldo), Math) =mark(Aldo, Math)
∀x(∀yy=∀zz∀∨w(zattend=w∨(yx, y=)w∧))attend(x, z)∧attend(x, w)→
```

## Common Mistakes

```
Use of∧with∀
∀x(WorksAt(FBK,x)∧Smart(x))means “Everyone works at FBK and everyone is smart”
“Everyone working at FBK is smart” is formalized as∀x(WorksAt(FBK,x)→Smart(x))
Use of→with∃
∃x(WorksAt(FBK,x)→Smart(x))mans “There is a person so that if (s)he works at
FBK then (s)he is smart” and this is true as soon as there is at last anxwho does not work
at FBK
“There is an FBK-working smart person” is formalized as
∃x(WorksAt(FBK,x)∧Smart(x))
```

## Representing variations quantifiers in FOL

### Example

Represent the statement “at least 2 students attend the KR course”
∃x 1 ∃x 2 (attend(x 1 ,KR)∧attend(x 2 ,KR))
The above representation is not enough, asx 1 andx 2 are variable and they could denote the same individual, we have to
guarantee the fact thatx 1 andx 2 denote different person. The correct formalization is:
∃x 1 ∃x 2 (attend(x 1 ,KR)∧attend(x 2 ,KR)∧x 1 ̸=x 2 )

### At leastn...

```
∃x 1 ...xn
```
#### 

#### 

```
^n
i=1
```
```
φ(xi)∧
```
```
^n
i̸=j=1
```
```
xi̸=xj
```
#### 

#### 


## Representing variations of quantifiers in FOL

### Example

Represent the statement “at most 2 students attend the KR course”

```
∀x 1 ∀x 2 ∀x 3 (attend(x 1 ,KR)∧attend(x 2 ,KR)∧attend(x 3 ,KR)→
x 1 =x 2 ∨x 2 =x 3 ∨x 1 =x 3 )
```
### At mostn...

```
∀x 1 ...xn+1
```
#### 

#### 

```
n^+1
i=1
```
```
φ(xi)→
```
```
n_+1
```
```
i̸=j=1
```
```
xi=xj
```
#### 

#### 


## Models, satisfiability and validity

In the following, ifΓis a set of formulas, then(I,α)|= Γmeans that(I,α)|=gfor allg∈Γ.

### Definition (Model, satisfiability and validity)

An interpretationIis a model ofφunder the assignmentα, if(I,α)|=φ.
A formulaφis satisfiable if there is someIand some assignmentαsuch that(I,α)|=φ.
A formulaφis unsatisfiable if it is not satisfiable.
A formulaφis valid if for everyIand every assignmentα, we have(I,α)|=φ.

### Definition (Logical implication)

A formulaφis logical implied by a set of formulasΓ, in symbolsΓ|=φ, if for all interpretationsI
and for all assignmentα, if(I,α)|= Γthen(I,α)|=φ.


## Models, satisfiability and validity for closed formulas

### Definition (Model, satisfiability and validity for closed formulas)

An interpretationIis a model of a closed formulaφifI |=φ.
A closed formulaφis satisfiable if there is someIsuch thatI |=φ.
A clsed formulaφis unsatisfiable if it is not satisfiable.
A closed formulaφis valid if for everyIwe haveI |=φ.

### Definition (Logical implication)

A closed formulaφis logically implied by a set of closed formulasΓ, in symbolsΓ|=φ, if for all
interpretationsI, ifI |= ΓthenI |=φ.

The notions of theory, set of axioms of a theory, and finitely axiomatizable theory in first-order
logic is a straightforward generalization of the corresponding notions in propositional logic.


## Properties of first-order logical implication

### Proposition

IfΓandΣare two sets of closed formulas formulas, andAandBtwo closed formulas, then the
following properties hold:
Reflexivity IfA∈Γ, thenΓ|=A
Ex falso sequitur quodlibet IfΓis unsatisfiable, thenΓ|=Afor allA
Monotonicity IfΓ|=AthenΓ∪Σ|=A
Cut IfΓ|=AandΣ∪{A}|=BthenΓ∪Σ|=B
Compactness IfΓ|=A, then there is a finite subsetΓ 0 ⊆Γ, such thatΓ 0 |=A
Deduction theorem IfΓ∪{A}|=BthenΓ|=A→B
Deduction principleΓ∪{A}|=Bif and only ifΓ|=A→B
Refutation principleΓ|=Aif and only ifΓ∪{¬A}is unsatisfiable


## Computational properties of first-order logic

### Theorem

Checking if a formula in first-order logic is valid is an undecidable problem (although
semi-decidable: there is algorithm that terminates and answer “yes” if the formula is valid). The
same holds for checking satisfiability and checking logical implication.

The proof is by reduction from the halting problem, that is the problem of checking if a given
Turing machine halts for a given input. The basic idea is that the Turing maching and the input
can be formalized by a first-order logic that is valid if and only if the machine halts for the input.

What about the evaluation of a formula in an interpretation? Note that this question is
meaningful only if the interpretation can be represented as a finite structure. Actually, it can be
shown that evaluating a formula in a finite interpretation is a PSPACE-complete problem.


## Excercises

Tell whether these formulas are valid, satisfiable, or unsatisfiable
∀xP(x)
∀xP(x)→∃yP(y)
∀x∀y(P(x)→P(y))
P(x)→∃yP(y)
P(x)∨¬P(y)
P(x)∧¬P(y)
P(x)→∀xP(x)
∀x∃yQ(x,y)→∃y∀xQ(x,y)
x=x
∀xP(x)↔∀y.P(y)
x=y→∀x.P(x)↔∀yP(y)
x=y→(P(x)↔P(y))
P(x)↔P(y)→x=y


## Solution

```
∀xP(x) Satisfiable
∀xP(x)→∃yP(y) Valid
∀x∀y(P(x)→P(y)) Satisfiable
P(x)→∃yP(y) Valid
P(x)∨¬P(y) Satisfiable
P(x)∧¬P(y) Satisfiable
P(x)→∀xP(x) Satisfiable
∀x∃yQ(x,y)→∃y∀xQ(x,y) Satisfiable
x=x Valid
∀xP(x)↔∀yP(y) Valid
x=y→∀xP(x)↔∀yP(y) Valid
x=y→(P(x)↔P(y)) Valid
P(x)↔P(y)→x=y Satisfiable
```

## Properties of quantifiers

### Proposition

The following formulas are valid
∀x(φ(x)∧ψ(x))≡∀xφ(x)∧∀xψ(x)
∃x(φ(x)∨ψ(x))≡∃xφ(x)∨∃xψ(x)
∀xφ(x)≡¬∃x¬φ(x)
∀x∃xφ(x)≡∃xφ(x)
∃x∀xφ(x)≡∀xφ(x)

### Proposition

The following formulas are not valid
∀x(φ(x)∨ψ(x))≡∀xφ(x)∨∀xψ(x)
∃x(φ(x)∧ψ(x))≡∃xφ(x)∧∃xψ(x)
∀xφ(x)≡∃xφ(x)
∀x∃yφ(x,y)≡∃y∀xφ(x,y)


## Expressing properties in FOL

What is the meaning of the following FOL formulas?

(^1) ∃x(bought(Frank,x)∧dvd(x))
(^2) ∃x bought(Frank,x)
(^3) ∀x(bought(Frank,x)→bought(Susan,x))
(^4) (∀x bought(Frank,x))→(∀x bought(Susan,x))
(^5) ∀x∃y bought(x,y)
(^6) ∃x∀y bought(x,y)
(^1) ”Frank bought a dvd.”
(^2) ”Frank bought something.”
(^3) ”Susan bought everything that Frank bought.”
(^4) ”If Frank bought everything, so did Susan.”
(^5) ”Everyone bought something.”
(^6) ”Someone bought everything.”


## Expressing properties in FOL

Define an appropriate language and formalize the following sentences using FOL formulas.

(^1) All Students are smart.
(^2) There exists a student.
(^3) There exists a smart student.
(^4) Every student loves some student.
(^5) Every student loves some other student.
(^6) There is a student who is loved by every other student.
(^7) Bill is a student.
(^8) Bill takes either Analysis or Geometry (but not both).
(^9) Bill takes Analysis and Geometry.
(^10) Bill doesn’t take Analysis.
(^11) No students love Bill.


## Expressing properties in FOL

(^1) ∀x(Student(x)→Smart(x))
(^2) ∃x Student(x)
(^3) ∃x(Student(x)∧Smart(x))
(^4) ∀x(Student(x)→∃y(Student(y)∧Loves(x,y)))
(^5) ∀x(Student(x)→∃y(Student(y)∧¬(x=y)∧Loves(x,y)))
(^6) ∃x(Student(x)∧∀y(Student(y)∧¬(x=y)→Loves(y,x)))
(^7) Student(Bill)
(^8) Takes(Bill,Analysis)↔¬Takes(Bill,Geometry)
(^9) Takes(Bill,Analysis)∧Takes(Bill,Geometry)
(^10) ¬Takes(Bill,Analysis)
(^11) ¬∃x(Student(x)∧Loves(x,Bill))


## Expressing properties in FOL

For each property write a formula expressing the property, and for each formula write the property
it formalises.
Every Man is Mortal
∀x(Man(x)→Mortal(x))
Every Dog has a Tail
∀x(Dog(x)→∃y(PartOf(x,y)∧Tail(y)))
There are two dogs
∃x∃y(Dog(x)∧Dog(y)∧x̸=y)
Not every dog is white
¬∀x(Dog(x)→White(x))
∃x.Dog(x)∧∃y.Dog(y)
There is a dog
∀x∀y(Dog(x)∧Dog(y)→x=y)
There is at most one dog


