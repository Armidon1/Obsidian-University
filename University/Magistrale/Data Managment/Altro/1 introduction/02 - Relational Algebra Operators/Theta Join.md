---
title: "Theta Join"
tags: [data-management, relational-algebra, join]
source: "[[1-Introduction.pdf]]"
---

# Theta Join

> [!definition]
> A theta join combines tuples from two relations and retains only pairs satisfying a condition $\Theta$.

$$
R\bowtie_{\Theta}S=\sigma_{\Theta}(R\times S)
$$

The condition may use equality, inequality, ordering comparisons, and Boolean connectives.

## Example

Let `Faculty(name, department, salary)` and `ChairSalary(department, salary)`. Faculty members earning more than their department chair are found using:

$$
Faculty\bowtie_{Faculty.department=ChairSalary.department\land Faculty.salary>ChairSalary.salary}ChairSalary
$$

The comparison on salary makes this a theta join but not an [[Equijoin]].

## SQL

```sql
SELECT f.name
FROM Faculty AS f
JOIN ChairSalary AS c
  ON f.department = c.department
 AND f.salary > c.salary;
```

## Why qualification matters

When both relations have `salary` or `department`, write `f.salary` and `c.salary`. Qualification identifies the exact operand of each comparison. See [[SQL Aliases and Attribute Qualification]].

## Physical execution

The algebraic definition uses [[Cartesian Product]] followed by [[Selection in Relational Algebra]]. A DBMS can implement the result with a specialized join algorithm without constructing all pairs.

## Related notes

- [[Equijoin]]
- [[Natural Join]]
- [[Cartesian Product]]

