---
title: "Codd's Theorem"
tags: [data-management, relational-model, theorem]
source: "[[1-Introduction.pdf]]"
---

# Codd's Theorem

> [!definition]
> Codd's theorem states that relational algebra and safe relational calculus are essentially equivalent in expressive power.

## Meaning of expressive power

Two query languages have the same expressive power when every query expressible in one can also be expressed in the other, even if the expressions look very different.

- [[Relational Algebra]] gives an operator-based, procedural description.
- [[Relational Calculus]] gives a logical, declarative description.

The theorem does **not** say that the two languages have the same syntax, that their expressions are equally convenient, or that equivalent queries have the same execution cost.

## Why safety is required

An unrestricted calculus formula may refer to values outside the active database domain and could define an infinite result. The equivalence concerns safe or domain-independent calculus queries, whose results are determined by the finite database content.

## Practical significance

The theorem helps separate three layers:

1. **Meaning** - the declarative property the result must satisfy.
2. **Logical plan** - an algebraic expression that computes the result.
3. **Physical plan** - concrete algorithms chosen by the DBMS.

A user may express a query declaratively in SQL, while the DBMS constructs an internal algebraic plan and chooses physical operators to evaluate it.

> [!important]
> Equivalent expressive power does not imply equivalent performance. Two correct formulations can lead to very different plans unless the optimizer recognizes their equivalence.

## Related notes

- [[Relational Algebra]]
- [[Relational Calculus]]
- [[SQL and Relational Algebra Correspondence]]

