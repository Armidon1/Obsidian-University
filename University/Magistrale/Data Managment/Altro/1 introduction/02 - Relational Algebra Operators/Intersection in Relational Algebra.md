---
title: "Intersection in Relational Algebra"
tags: [data-management, relational-algebra, derived-operator]
source: "[[1-Introduction.pdf]]"
---

# Intersection in Relational Algebra

> [!definition]
> Intersection returns tuples that occur in both union-compatible relations.

$$
R\cap S=\{t\mid t\in R\land t\in S\}
$$

## Derivation from difference

Intersection is a derived operation because:

$$
R\cap S=R-(R-S)=S-(S-R)
$$

The inner difference finds tuples unique to one side. Removing them leaves the common tuples.

## Derivation from equijoin

For $R(A_1,\ldots,A_k)$ and $S(B_1,\ldots,B_k)$:

$$
R\cap S=\pi_{R.A_1,\ldots,R.A_k}(R\bowtie_{R.A_1=S.B_1\land\cdots\land R.A_k=S.B_k}S)
$$

All corresponding components must match. Projection keeps one copy of the tuple.

## SQL

```sql
SELECT code, name, age FROM Employee
INTERSECT
SELECT code, name, age FROM Director;
```

The exact support for `INTERSECT ALL` is DBMS-specific. Standard `INTERSECT` follows set semantics.

## Related notes

- [[Difference in Relational Algebra]]
- [[Equijoin]]
- [[Derived Operators in Relational Algebra]]

