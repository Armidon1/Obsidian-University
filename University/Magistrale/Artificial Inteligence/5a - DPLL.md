# Davis–Putnam–Logemann–Loveland (DPLL) procedure for satisfiability

```
Luciano Serafini – Maurizio Lenzerini
```
```
FBK-IRST, Trento, Italy – Sapienza Universit`a di Roma
```
```
Revised and adapted by F. Patrizi
```

# Decision procedures - automated reasoning

Automated reasoning is the discipline that aims at solving basic decision problems in logic, the
main of which are:

## Four types of decision problems

```
Model Checking(I,φ):I
```
```
?
|=φDoes the intepretationIsatisfyφ, or equivalently, isIa
model ofφ?
```
```
Satisfiability(φ):
```
```
?
∃I.I |=φIs there a model ofφ?
```
```
Validity(φ):
```
```
?
|=φIs every interpretation forφa model ofφ?
```
```
Logical implication(Γ,φ):Γ
```
```
?
|=φIs every model of the set of formulasΓa model ofφas
well?
```
```
Logical inference(Γ,φ):Γ
```
```
?
⊢ΣφIs there a proof ofφinΣfromΓ?
```

# Model Checking

## Model checking decision procedure

A model checking decision procedure,MCDPis an algorithm that checks if a formulaφis
satisfied by an interpretationI. Namely

```
MCDP(φ,I) =true if and only if I |=φ
MCDP(φ,I) =false if and only if I ̸|=φ
```
## Observation

The procedure of model checking returns for all inputs either true or false since for every
intepretationIand for every formulaφ, we have that eitherI |=φorI ̸|=φ.

## Observation

We have already seen a naive algorithm for model checking in propositional logic.


# Satisfiability

## Satisfiability decision procedure

A satisfiability decision procedureSDPis an algorithm that takes in input a formulaφand checks
ifφis satisfiable. Namely

```
SDP(φ) =Satisfiable if and only if I |=φfor someI
SDP(φ) =Unsatisfiable if and only if I ̸|=φfor allI
```
WhenSDP(φ) =satisfiable, SDP can in addition return a modelI(or, one of the models) of the
formulaφ.


# Validity

## Validity decision procedure

A decision procedure for Validity VDC, is an algorithm that checks whether a formula is valid.
VDP can be based on a satisfiability decision procedure by exploiting the equivalence

```
φis valid if and only if¬φis not satisfiable
```
```
V DP(φ) =true if and only if SDP(¬φ) =Unsatisfiable
V DP(φ) =false if and only if SDP(¬φ) =Satisfiable
```
WhenSDP(¬φ)returnsSatisfiable, it may in addition returns an interpretationI, andIis called
a counter-model forφ, in the sense that is an intepretation that falsifiesφ.


# Logical implication

## Logical implication decision procedure

A decision procedure for logical consequence (or implication) LCDP is an algorithm that checks
whether a formulaφis a logical consequence of a finite set of formulasΓ ={γ 1 ,...,γn}. LCDP
can be implemented on the basis of satisfiability decision procedure by exploiting the property

```
Γ|=φif and only ifΓ∪{¬φ}is unsatisfiable
```
```
LCDP(Γ,φ) =true if and only if SDP(γ 1 ∧···∧γn∧¬φ) =Unatisfiable
LCDP(Γ,φ) =false if and only if SDP(γ 1 ∧···∧γn∧¬φ) =Satisfiable
```
WhenSDP(γ 1 ∧···∧γn∧¬φ)returnsSatisfiable, it may in addition returns an interpretationI,
andIis a model forΓand a counter-model forφ, i.e., a model ofΓthat falsifiesφ.


# Proof of the previous property

## Theorem

Γ|=φif and only ifΓ∪{¬φ}is unsatisfiable.

## Proof.

```
⇒IfΓ|=φ, then every model ofΓsatisfiesφ, and therefore we cannot find a model ofΓwhere
¬φis true. It follows thatΓ∪{¬φ}is unsatisfiable.
⇐IfΓ∪{¬φ}is unsatisfiable, then either(a) Γitself is unsatisfiable, or(b) Γhas at least one
model, but¬φis false in every model ofΓ. If(a)is the case, thenΓlogically implies
everything, and thereforeΓ|=φ. If(b)is the case, the set of models ofΓis nonempty, andφ
is true in all such model. So, we have shown thatΓ|=φholds in all cases.
```

# Davis–Putnam–Logemann–Loveland (DPLL) procedure for satisfiability

DPLL SAT procedure:

```
Introduced in 1961 by Martin Davis, George Logemann and Donald W. Loveland;
Refinement of the earlier Davis–Putnam procedure, which is a resolution-based procedure
developed by Davis and Hilary Putnam in 1960;
After more than 60 years the DPLL procedure still forms the basis for most efficient complete
SAT solvers.
```
Original references:

```
Martin Davis, Hilary Putnam: A Computing Procedure for Quantification Theory. J. ACM
7(3): 201-215 (1960)
Martin Davis, George Logemann, Donald W. Loveland: A machine program for
theorem-proving. Commun. ACM 5(7): 394-397 (1962)
```

# Conjunctive Normal form

## Definition

```
A literal is either a propositional variable or the negation of a propositional variable.
```
```
p, ¬q
```
```
A clause is a disjunction of literals.
(a∨¬b∨c)
```
```
A formula is in conjunctive normal form, if it is a conjunction of clauses.
```
```
(p∨¬q∨r)∧(q∨r)∧(¬p∨¬q)∧r
```

# Conjunctive Normal form

## Conjunctive Normal form

A formula in conjunctive normal form has the following shape:

```
(l 11 ∨···∨l 1 n 1 )∧...∧(lm 1 ∨···∨lmnm)
```
equivalently written as
^m

```
i=
```
(^) nj
_
j=
lij

### !

wherelijis thej-th literal of thei-th clause composingφ

## Example

```
(p∨¬q)∧(r∨p∨¬r)∧(p∨p) p∨q
p∧q, p∧¬q∧(r∨s)
```

# Equi-satisfiable formulas

Two formulasφandφ′are equi.satisfiable iff:

```
φis satisfiable if and only ifφ′is satisfiable
```
```
If two formulas are equi-satisfiable, are they equivalent? No!
Example: Any satisfiable formula (e.g.,p) is equi-satisfiable with⊤, but clearly,p≡⊤is not
valid!
Another example: Introducing names leads to equi-satisfiable formulas. E.g. the formula
a∧bis equi-satisfiable of the formula(n≡a∧b)∧n, but it is not true that
```
```
(a∧b)≡(n∧(a∧b≡n))
```
```
Equi-satisfiability is a weaker notion than equivalence. But useful if all we want to do is
determine satisfiability.
```

# Tseitin’s transformation

## Tseitin’s transformation ...

... converts any propositional formulaφinto an equi-satisfiable formulaφ′in CNF with only a
linear increase in size.

Key ideas:

```
give a “name” to every subformula (except for literals), and use this name as a fresh
propositional letter “representing” the subformula
for every formulaψof the formp 1 ≡(p 2 ◦p 3 )(where◦is a connective), there is a CNF
formulaCNF(ψ)that is equivalent toψ
transform the original formulaψinto a conjunction of manyCNF(ψi)obtained fromψ, one
for each subformula ofψ
```
```
∗Gregory S. Tseitin - On the complexity of proof in prepositional calculus, Leningrad, 1968.
```

# Tseitin’s transformation

Ifψis any formula, then for every subformulaφofψ, we define its namenφas follows:

```
nφis simplyφifφis a literal;
nφis a new propositional letter ifφis not a literal.
```
The Tseitin’s transformationT(ψ)ofψis the conjunction of

```
nψ
CNF(q≡¬nφ)for every non-literal subformula of the form¬φhaving nameq
CNF(q≡(nφ 1 ◦nφ 2 ))for every subformula of the formφ 1 ◦φ 2 having nameq, where
◦∈{∨,∧,→,≡}.
```

# Tseitin’s transformation

We still need to understand whatCNFdoes. We proceed to analyze all cases.

```
CNF(q≡¬p) = (¬q∨¬p)∧(p∨q)
CNF(q≡(p∧r)) = (q∨¬p∨¬r)∧(¬q∨p)∧(¬q∨r)
CNF(q≡(p∨r)) = (¬q∨p∨r)∧(q∨¬p)∧(q∨¬r)
CNF(q≡(p→r)) = (¬q∨¬p∨r)∧(p∨q)∧(¬r∨q)
CNF(q≡(p≡r)) = (q∨p∨r)∧(q∨¬p∨¬r)∧(¬q∨p¬r)∧(¬q∨¬p∨r)
```

# Tseitin’s transformation

## Theorem

For every formulaψ,T(ψ)is satisfiable if and only ifψis. Moreover,T(ψ)is 3-CNF formula
whose size is linear with respect to the size ofψ.


# Tseitin’s transformation - Example

Letψbe the formula(p∨q)→(p∧¬r)

(^1) For each non-literal subformula, introduce new letters:
x 1 forψ,x 2 forp∨q,x 3 forp∧¬r
(^2) Stipulate equivalences and convert them to CNF:
CNF(x 1 ≡(x 2 →x 3 )) ⇒ φ 1 : (¬x 1 ∨¬x 2 ∨x 3 )∧(x 2 ∨x 1 )∧
(¬x 3 ∨x 1 )
CNF(x 2 ≡(p∨q)) ⇒ φ 2 : (¬x 2 ∨p∨q)∧(¬p∨x 2 )∧
(¬q∨x 2 )
CNF(x 3 ≡(p∧¬r)) ⇒ φ 3 : (¬x 3 ∨p)∧(¬x 3 ∨¬r)∧
(¬p∨r∨x 3 )
(^3) The formulaT(ψ)is:
x 1 ∧φ 1 ∧φ 2 ∧φ 3


# Properties of∧and∨

```
Commutativity of∧: φ∧ψ ≡ ψ∧φ
Commutativity of∨: φ∨ψ ≡ ψ∨φ
Absorption of∧: φ∧φ ≡ φ
Absorption of∨: φ∨φ ≡ φ
```

# Properties of clauses

## Order of literals does not matter

If a clauseCis obtained by reordering the literals of a clauseC′thenCandC′are equivalent.
E.g.,(p∨q∨r∨¬r)≡(¬r∨q∨p∨r)

## Multiple literals can be merged

If a clause contains more than one occurrence of the same literal, then it is equivalent to the clause
obtained by deleting all but one such occurrences. E.g.,(p∨q∨r∨q∨¬r)≡(p∨q∨r∨¬r)

## Clauses as set of literals

It follows from these propertiesthat we can represent a clause as a set of literals, by leaving
disjunction implicit and by ignoring replication and order of literals

```
(p∨q∨r∨¬r) is represented by the set {p,q,r,¬r}
```

# Properties of formulas in CNF

## Order of clauses does not matter

If a CNF formulaφis obtained by reordering the clauses of a CNF formulaφ′thenφandφ′are
equivalent. E.g.,
(a∨b)∧(c∨¬b)∧(¬b)≡(c∨¬b)∧(¬b)∧(a∨b)

## Multiple clauses can be merged

If a CNF formula contains more than one occurrence of the same clause, then it is equivalent to
the formula obtained by deleting all but one such occurrences. E.g.,
(a∨b)∧(c∨¬b)∧(a∨b)≡(a∨b)∧(c∨¬b)

## A CNF formula can be seen as a set of clauses

It follows from the properties of clauses and CNF formulas that we can represent a CNF formula
as a set of sets of literals. E.g.,(¬b)∧(b∨a∨b)∧(c∨¬b)∧(¬b)
is represented by {{a,b},{c,¬b},{¬b}}


# Satisfiability of a set of clauses

```
Letψ={C 1 ,...,Cn}
▶I |=ψif and only ifI |=Cifor alli= 1..n;
▶I |=Ciif and only if for somel∈C,I |=l
To check if an intepretationIsatisfiesψwe do not necessarily need to know the truth values
thatIassigns to all the literals appearing inψ.
For instance, ifI(p) =trueandI(q) =false, we can say thatI |={{p,q,¬r},{¬q,s,q}},
without considering the evaluations ofI(r)andI(s).
```
## Partial interpretation

A partial intepretation is a partial function that associates to some propositional variables of the
alphabetPa truth value (either true or false) and can be undefined for the others.


# Partial interpretations

```
Partial interpretations can be used to construct models for a set of clausesψ={C 1 ,...,Cn}
incrementally
Under a partial interpretationI, literals and clauses can be true, false or undefined; a clause
C
▶is true underIif at least one of its literals is true;
▶is false (or “conflicting”) underIif all its literals are false
▶is undefined (or “unresolved”) underI, otherwise.
The algorithms that exploit partial intepretations usually start with an empty interpretation
(where the truth values of all propositional letters are undefined) and try to extend it step by
step to the various variables occurring in{C 1 ,...,Cn}.
```

# Simplification

```
Ifλis a literal of the formp, then¬λdenotes¬p.
Ifλis a literal of the form¬p, then¬λdenotesp.
```
## Simplification of a formula by a literal

For any CNF formulaφand a literalλ,φ|λstands for the formula obtained fromφby

```
removing all clauses containing the literalλ, and
removing the literals¬λin all remaining clauses
```
## Example

For instance,
{{p,q,¬r},{¬p,¬r}}|¬p={{q,¬r}}


# Unit propagation

## Unit clause

A unit clause is a clause containing a single literal.

If the CNF formulaφcontains a unit clause{λ}, then to satisfyφthe literalλmust be evaluated
to True. As a consequenceφcan be simplified using the procedureUnitPropagation, that is
invoked onφand a partial intepretationI, and returns a CNF formula and a partial interpretation.

## Unit propagation

```
UnitPropagation(φ,I)
whileφcontains a unit clause{λ}
ifλ=p, thenI(p) :=true;
ifλ=¬p, thenI(p) :=false
φ:=φ|λ;
end;
return(φ,I)
```

# The DPLL procedure

## Example

```
UnitPropagation({{p},{¬p,¬q},{¬q,r}},∅)
```
```
{{p},{¬p,¬q},{¬q,r}}
{{p},{¬p,¬q},{¬q,r}}|p={{¬q},{¬q,r}} I(p) =true
{{¬q},{¬q,r}}
{{¬q},{¬q,r}}|¬q={} I(q) =false
```
the procedure returns ({},I)


# The DPLL procedure

## Remark

In some cases, unit propagation applied toφis enough to decide satisfiability ofφ, for example
when it terminates with one of the following two results:

```
({},I)(as in the example above), in which case the initial formula is satisfiable, and a
satisfying interpretation can be easily extracted fromI;
(φ,I), where{}∈φ, in which case the original formula is unsatisfiable.
```
There are cases whereUnitPropagationdoes terminate with any of the cases above, i.e., when
there is no unit clauses to consider, the CNF is nonempty, and it does not contain empty clauses.

Example:{{p,q},{¬q,r}}


# The DPLL procedure

## The Davis-Putnam-Logemann-Loveland procedure

To check the CNF formulaφfor satisfiability, the procedure is invoked byDPLL(φ,∅).

```
DPLL(φ,I′)
(ψ,I):=UnitPropagation(φ,I′);
ifψcontains{}
thenreturn({{}},∅)
elseifψ={}thenreturn({},I)
elseselect a literalλ∈C∈ψ;
ifDPLL(ψ∪{{λ}},I)= ({},I′′)
thenreturn({},I′′)
elsereturnDPLL(ψ∪{{¬λ}},I)
```
```
UnitPropagationrealizes the “unit propagation rule”
The last “if then else” realizes the “splitting rule”
```

# Properties of the DPLL procedure

We first discuss the properties ofUnitPropagation. By observing that every execution of the
instructions inside thewhileloop eliminates one clause from the formula and possibly a set of
literals from the other clauses of the input formula, we can easily conclude the following.

## Theorem

For anyφ,I,UnitPropagation(φ,I) terminates, and runs in polynomial time with respect to
the size ofφ.


# Derivation tree

The computation done byDPLL(φ,∅) can be described by a binary tree, in which every path
from the root to a splitting node, or from a splitting node to another splitting node, or from a
splitting node to a leaf is the sequence of operations of unit propagation.

```
unit propagation
```
```
splitting rule
```
```
splitting rule
```
```
splitting rule
```
```
unit propagation
```

# Properties of the DPLL procedure

Since the length of every path from the root to a leaf is bound ton, wherenis the number of
variables inφ, we have that the size of the binary tree is at most 2 n. From this observation the
following theorem on the worst-case time complexity follows.

## Theorem

For anyφ,DPLL(φ,∅) terminates, and its time complexity isO(2m), wheremis the size ofφ.


# Properties of the DPLL procedure

The following theorem sanctions the correctness ofDPLL.

## Theorem

For anyφ,DPLL(φ,∅)returns

```
({},I)ifφis satisfiable, and
({{}},∅)ifφis unsatisfiable.
```
Note that whenDPLL(φ,∅)returns({},I),Iis a model ofφ.


# Horn clauses

## Definition

A clause is a Horn clause if it has at most one positive literal. A Horn formula is a formula in CNF
all of whose clauses are Horn clauses.

## Theorem

A Horn formulaφis satisfiable if and only ifUnitPropagation(φ,∅) returns(ψ,I), withψ
different from{{}}.

## Theorem

Satisfiability of Horn formulas can be solved in polynomial time.

We leave as an exercise the proof of the above theorems.


