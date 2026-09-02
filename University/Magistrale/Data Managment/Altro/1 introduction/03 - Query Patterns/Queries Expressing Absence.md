---
title: "Queries Expressing Absence"
tags: [data-management, query-patterns, sql, negation]
source: "[[1-Introduction.pdf]]"
---

# Queries Expressing Absence

> [!definition]
> An absence query asks for candidates for which no matching row satisfies a forbidden condition.

Common phrases include "no", "none", "without", "never", and "does not have".

## Relational algebra

The standard pattern is:

$$
AllCandidates-CandidatesWithForbiddenWitness
$$

For schools with no mark-100 graduate:

$$
\pi_{scode}(School)-\rho_{scode\leftarrow school}(\pi_{school}(\sigma_{mark=100}(Graduated)))
$$

See [[Difference in Relational Algebra]].

## Preferred SQL pattern

```sql
SELECT s.scode
FROM School AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM Graduated AS g
    WHERE g.school = s.scode
      AND g.mark = 100
);
```

For each school, the correlated subquery searches for a forbidden witness. `NOT EXISTS` retains the school when none is found.

## Why `NOT IN` is risky

```sql
WHERE scode NOT IN (SELECT school FROM Graduated)
```

If the subquery returns `NULL`, comparisons can become `UNKNOWN`, potentially eliminating every candidate. `NOT EXISTS` is usually clearer and safer. See [[NULL and Three-Valued Logic]].

## Outer-join alternative

```sql
SELECT s.scode
FROM School AS s
LEFT JOIN Graduated AS g
  ON g.school = s.scode
 AND g.mark = 100
WHERE g.school IS NULL;
```

This anti-join pattern works when the tested joined column cannot itself be `NULL` in a real match.

## Related notes

- [[Existential Queries in Databases]]
- [[Universal Quantification in Databases]]
- [[Difference in Relational Algebra]]

