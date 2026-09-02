---
title: "Relational Algebra"
tags: [data-management, relational-algebra, definition]
source: "[[1-Introduction.pdf]]"
---

# Relational Algebra

> [!definition]
> Relational algebra is a formal, procedural query language in which expressions transform one or more relations into another relation.

The word **procedural** means that an expression describes a composition of operations. It does not mean that a DBMS must execute those operations in the written order: equivalent expressions can be optimized into different physical plans.

## Closure

Every relational operator returns a relation. Therefore, an operator result can become the input of another operator:

$$
\pi_{Name}(\sigma_{Salary>50}(Employee))
$$

This expression first selects employees with salary above 50 and then projects their names.

## Five basic operations

The core presented in the course contains:

1. [[Union in Relational Algebra]];
2. [[Difference in Relational Algebra]];
3. [[Cartesian Product]];
4. [[Projection in Relational Algebra]];
5. [[Selection in Relational Algebra]].

Other operations, such as [[Intersection in Relational Algebra]], [[Theta Join]], and [[Natural Join]], can be derived from this core. See [[Derived Operators in Relational Algebra]].

## Expression grammar

A simplified grammar is:

$$
E ::= R \mid (E_1 \cup E_2) \mid (E_1-E_2) \mid (E_1 \times E_2) \mid \pi_X(E) \mid \sigma_{\Theta}(E)
$$

where $X$ is an attribute list and $\Theta$ is a condition.

## Why it matters

Relational algebra provides:

- precise query semantics;
- a bridge between user-level SQL and internal query plans;
- equivalence laws used in query optimization;
- a method for reasoning about difficult queries involving joins, negation, and universal conditions.

> [!example] Equivalent strategies
> A selection can often be moved closer to an input relation before a join. The result remains equivalent, but fewer tuples may need to be joined. This is the kind of transformation exploited by an optimizer.

## Related notes

- [[Relational Data Model]]
- [[Relational Calculus]]
- [[Codd's Theorem]]
- [[SQL and Relational Algebra Correspondence]]

