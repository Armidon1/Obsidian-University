---
title: "Existential Queries in Databases"
tags: [data-management, query-patterns, sql, logic]
source: "[[1-Introduction.pdf]]"
---

# Existential Queries in Databases

> [!definition]
> An existential query asks whether **at least one** row satisfying a condition exists.

Natural-language signals include "there exists", "at least one", "some", and "has a".

## Relational algebra pattern

For cities having at least one school with a student who graduated with 100:

$$
\pi_{city}(\sigma_{mark=100}(Graduated)\bowtie_{school=scode}School)
$$

The qualifying graduation is a **witness** that proves the existential condition.

## SQL with a join

```sql
SELECT DISTINCT s.city
FROM School AS s
JOIN Graduated AS g
  ON g.school = s.scode
WHERE g.mark = 100;
```

`DISTINCT` is needed because multiple witnesses can repeat the same city.

## SQL with `EXISTS`

```sql
SELECT DISTINCT s.city
FROM School AS s
WHERE EXISTS (
    SELECT 1
    FROM Graduated AS g
    WHERE g.school = s.scode
      AND g.mark = 100
);
```

`EXISTS` tests whether the subquery returns at least one row. The selected expression `1` is conventional; row existence, not its projected value, determines the result.

## Join or `EXISTS`?

- Use a join when columns from the matching row are needed.
- Use `EXISTS` when only existence matters and duplicate multiplication would be distracting.
- A capable optimizer may produce similar physical plans for both.

## Related notes

- [[Queries Expressing Absence]]
- [[Universal Quantification in Databases]]
- [[SQL and Relational Algebra Correspondence]]

