---
title: "Equijoin"
tags: [data-management, relational-algebra, join]
source: "[[1-Introduction.pdf]]"
---

# Equijoin

> [!definition]
> An equijoin is a [[Theta Join]] whose join condition consists of equality comparisons.

Example:

$$
Employee\bowtie_{Employee.department=Department.code}Department
$$

## SQL

```sql
SELECT e.name, d.code, d.chair
FROM Employee AS e
JOIN Department AS d
  ON e.department = d.code;
```

The result normally retains both join columns unless a projection removes one.

## Equijoin versus natural join

| Equijoin | [[Natural Join]] |
|---|---|
| Join columns are stated explicitly | All same-named attributes are matched automatically |
| May compare differently named columns | Requires common attribute names |
| Usually retains both compared columns | Keeps one copy of common columns |
| Meaning is stable when unrelated columns are added | Meaning can change when schemas gain same-named columns |

## Intersection connection

For union-compatible relations, intersection can be expressed by equijoining all corresponding attributes and projecting one copy. See [[Intersection in Relational Algebra]].

## Common mistake

Joining only on a person's name may be insufficient if names are not globally unique. Use every attribute needed to identify the intended match, such as both name and department, or preferably a stable key.

## Related notes

- [[Theta Join]]
- [[Natural Join]]
- [[SQL Aliases and Attribute Qualification]]

