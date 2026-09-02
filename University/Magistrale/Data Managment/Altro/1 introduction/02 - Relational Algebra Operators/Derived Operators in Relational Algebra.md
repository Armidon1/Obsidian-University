---
title: "Derived Operators in Relational Algebra"
tags: [data-management, relational-algebra, definition]
source: "[[1-Introduction.pdf]]"
---

# Derived Operators in Relational Algebra

> [!definition]
> A derived operator is an operator definable through a composition of more basic relational algebra operations.

Derived operators improve readability without necessarily increasing expressive power.

## Main examples

### Intersection

$$
R\cap S=R-(R-S)
$$

See [[Intersection in Relational Algebra]].

### Theta join

$$
R\bowtie_{\Theta}S=\sigma_{\Theta}(R\times S)
$$

See [[Theta Join]].

### Natural join

A natural join is an equijoin on all common attributes followed by a projection that removes duplicate common columns. See [[Natural Join]].

## Expressive power versus convenience

Adding a notation such as join does not automatically let the algebra express a query that was previously impossible. It packages a frequent pattern into one meaningful operator.

This distinction appears again in SQL. Window functions make many analytical queries direct and readable, although some can be emulated using grouping, self-joins, and subqueries. See [[GROUP BY vs Window Functions]].

## Why derived operators matter to a DBMS

At the logical level, a join can be expanded into product and selection. At the physical level, the DBMS treats join as an important operator with specialized algorithms. Logical equivalence does not prescribe physical execution.

## Related notes

- [[Relational Algebra]]
- [[Intersection in Relational Algebra]]
- [[Theta Join]]
- [[Natural Join]]

