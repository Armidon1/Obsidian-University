---
title: "Relational Calculus"
tags: [data-management, relational-calculus, definition]
source: "[[1-Introduction.pdf]]"
---

# Relational Calculus

> [!definition]
> Relational calculus is a declarative formalism in which a query describes the logical properties that result tuples must satisfy.

Instead of prescribing a sequence of operators, relational calculus uses formulas inspired by first-order logic. A query conceptually says:

> Return every tuple $t$ for which property $P(t)$ is true.

## Declarative perspective

In [[Relational Algebra]], the expression emphasizes *how relations are combined*. In relational calculus, the formula emphasizes *what must be true of the answer*.

For example, the request "find employees with salary above 50" can be viewed as the set of employees $e$ satisfying:

$$
Employee(e) \land e.salary > 50
$$

## Variables and quantification

First-order logic provides:

- existential quantification, $\exists$, corresponding to phrases such as "there exists" or "at least one";
- universal quantification, $\forall$, corresponding to "for every";
- conjunction, disjunction, and negation.

These ideas reappear in practical SQL through `EXISTS`, `NOT EXISTS`, joins, and subqueries. See [[Existential Queries in Databases]] and [[Universal Quantification in Databases]].

## Safety

Unrestricted logical formulas could describe infinite sets unrelated to the finite database. Practical relational calculus therefore uses a safety or domain-independence condition so that query results depend only on relevant database values and remain finite.

## Relationship to other languages

[[Codd's Theorem]] states that relational algebra and safe relational calculus are essentially equivalent in expressive power. SQL inherits declarative ideas from calculus while also exposing constructs that resemble relational algebra.

## Related notes

- [[Relational Algebra]]
- [[Codd's Theorem]]
- [[Existential Queries in Databases]]
- [[Universal Quantification in Databases]]

