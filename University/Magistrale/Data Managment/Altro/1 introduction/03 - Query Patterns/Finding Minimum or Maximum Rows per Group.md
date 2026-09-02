---
title: "Finding Minimum or Maximum Rows per Group"
tags: [data-management, query-patterns, sql, grouping]
source: "[[1-Introduction.pdf]]"
---

# Finding Minimum or Maximum Rows per Group

> [!definition]
> An extreme-row query asks for the complete row or identifier associated with the minimum or maximum value inside each group.

This differs from merely calculating `MIN(value)` or `MAX(value)`, which returns the extreme value but not the row containing it.

## Correlated subquery

```sql
SELECT g1.school, g1.gcode, g1.mark
FROM Graduated AS g1
WHERE g1.mark = (
    SELECT MIN(g2.mark)
    FROM Graduated AS g2
    WHERE g2.school = g1.school
);
```

Ties are preserved because every row equal to the minimum qualifies.

## Relational algebra idea

A row is not minimal if another row in the same school has a smaller mark. Self-join two renamed copies, select `g1.mark > g2.mark`, project the non-minimal rows, then subtract them from all rows.

See [[Renaming in Relational Algebra]] and [[Difference in Relational Algebra]].

## Window-function solution

```sql
WITH ranked AS (
    SELECT g.*,
           RANK() OVER (
               PARTITION BY school
               ORDER BY mark ASC
           ) AS rnk
    FROM Graduated AS g
)
SELECT school, gcode, mark
FROM ranked
WHERE rnk = 1;
```

Use `RANK` to preserve ties. `ROW_NUMBER` would select exactly one row per school and requires a deterministic tie-breaker.

## Choosing a method

- Correlated aggregate: clear and compact.
- Join to grouped minima: useful when the grouped summary is reused.
- Window function: ideal when ranks or other row-level analytics are also needed.

## Related notes

- [[RANK vs DENSE_RANK vs ROW_NUMBER]]
- [[Top-N per Group]]
- [[SQL Query Granularity]]

