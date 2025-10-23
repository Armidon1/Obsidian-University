## Artificial Intelligence

## &

## Machine Learning

### A.Y. 2025/

### Prof. Fabio Patrizi


# Propositional Tableaux


#### How to Check Satisfiability

How to check whether there exists an interpretation 𝐼 s.t. 𝐼 ⊧ 𝜑?

We have seen Truth Tables: for complex formulas, approach is infeasible

We'll see two more approaches

Today: Tableaux method

Easy to understand, easy to implement


#### Tableaux

A Tableau is a tree-like structure, where:

- The root is the formula 𝜑 we want to check for satisfiability
- Internal nodes contain formulas over propositions of 𝜑
- Leaves are labelled with X or O

The tableau is constructed incrementally

Once construction is complete:

```
φ is satisfiable iff there exists some leaf labelled with O
equivalently, φ is unsatisfiable iff all leaves are labelled with X
```

#### Expansion rules

##### 𝜑⋀𝜓

##### 𝜑

##### 𝜓

```
𝛼-rules (or deterministic rules)
```
```
𝛽-rules (or splitting rules)
```
##### ¬(𝜑∨𝜓)

##### ¬𝜑

##### ¬𝜓

##### ¬(𝜑⊃𝜓)

##### 𝜑

##### ¬𝜓

##### 𝜑∨𝜓

##### 𝜑 𝜓

##### ¬(𝜑⋀𝜓)

##### ¬𝜑 ¬𝜓

##### 𝜑⊃𝜓

##### ¬𝜑 𝜓

##### ¬¬𝜑

##### 𝜑

##### 𝜑↔𝜓

##### 𝜑 ¬𝜑

##### 𝜓 ¬𝜓

##### ¬(𝜑↔𝜓)

##### ¬𝜑 𝜑

##### 𝜓 ¬𝜓


#### Tableaux Construction Algorithm

Tableaux is constructed proceeding top-down

Start with root labelled with formula to check

At every step one node is expanded (nodes can be expanded only once)

Expansion order is arbitrary (but may affect size of Tableau)

If a path (called _branch_ ) contains contradictory formulas, e.g., p and ¬p, add leaf with X

Once all nodes along a branch have been expanded, if it contains no contradiction then
add leaf with O

Construction is complete when every leaf has O or X


#### Example

```
¬(q∨p⊃p∨q)
```
```
q∨p
¬(p∨q)
```
```
(𝛼-rule)
```
```
(𝛼-rule)
```
```
q p
```
```
(𝛽-rule)
```
```
X X
```
```
¬q
¬p
```
```
(contradiction: q,¬q)^ (contradiction: p,¬p)^
```
All leaves contain X:
unsatisfiable


#### Example

Some leaf contains O:
satisfiable


#### Termination

It is immediate to see that the _tableau construction eventually terminates_ :

Applying the expansion rule reduces the size of the formulas involved

Thus, iterative applications of the rules eventually end up in formulas that cannot
be expanded anymore


#### Open and Closed Tableau

A root-leaf path, also called _branch_ , is said to be:

- _closed_ if it contains a formula and its negation
_- open_ otherwise

A tableau is _closed_ if all its branches are closed, _open_ otherwise


#### Soundness and Completeness

If a tableau for 𝜑 is open then 𝜑 is satisfiable (soundness)

If 𝜑 is satisfiable, every tableau for 𝜑 is open (completeness)

Thus:

```
𝜑 is satisfiable iff some tableau for 𝜑 is open
```
(Observe: a tableau for 𝜑 is open iff all the tableaux for 𝜑 are open)


#### Intuition

Every branch of a tableaux contains, overall, a set of formulas

If an interpretation 𝐼 satisfies all the formulas in a branch, then 𝐼 ⊧ 𝜑

By the construction of the tableau, also the converse holds:
if 𝐼 ⊧ 𝜑 then 𝐼 satisfies all the formulas occurring in some branch of the tableau

Thus,

```
𝐼 ⊧ 𝜑 iff 𝐼 satisfies all the formulas in some branch of the tableau
```

#### Complexity

Worst-case complexity is O(2n), for n the size of the formula

This corresponds to the # of branches produced by the algorithm

(Each branch is of linear size wrt size of the formula)


#### Models from Tableau

- Select one open branch
- Assign true to every proposition occurring in some
    _positive literal_ (e.g., P) from that branch
- Assign false to every proposition occurring in some
    _negative literal_ (e.g., ¬Q) from that branch
- Assign any value to propositions not mentioned in
    branch
- The resulting set is a model of 𝜑

E.g.: 𝐼={P} is a model


#### Satisfiability, Validity and Logical Implication

Recall the Refutation Principle:

```
𝚪 ⊧ 𝜑 iff 𝚪∪{¬𝜑} is unsatisfiable
```
If 𝚪={𝜑 1 ,...,𝜑m} is finite, this is equivalent to:

```
𝚪 ⊧ 𝜑 iff 𝜑 1 ⋀...⋀𝜑m⋀¬𝜑 is unsatisfiable
```
We can check whether 𝚪 ⊧ 𝜑 by checking whether 𝜑 1 ⋀...⋀𝜑m⋀¬𝜑 is unsatisfiable

Can use any algorithm for satisfiability, including Tableaux

Special case 𝚪=∅: ⊧ 𝜑 (𝜑 is valid) iff ¬𝜑 is unsatisfiable


