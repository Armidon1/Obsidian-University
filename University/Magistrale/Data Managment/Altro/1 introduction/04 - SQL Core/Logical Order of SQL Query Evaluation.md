---
title: "Logical Order of SQL Query Evaluation"
tags: [data-management, sql, query-processing]
source: "[[1-Introduction.pdf]]"
---

# Logical Order of SQL Query Evaluation

> [!definition]
> SQL's logical evaluation order describes how the meaning of a query is constructed. It differs from both the written clause order and the physical execution plan.

## Useful logical order

1. `FROM` and joins
2. `WHERE`
3. `GROUP BY`
4. aggregate evaluation
5. `HAVING`
6. window functions
7. `SELECT`
8. `DISTINCT`
9. outer `ORDER BY`
10. `LIMIT` / `OFFSET`

## Why this matters

### `WHERE` precedes grouping

`WHERE` decides which detail rows can contribute to groups. See [[WHERE vs HAVING]].

### Window functions follow `WHERE`

This is normally invalid:

```sql
SELECT e.*,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM Employee AS e
WHERE rn <= 10;
```

The alias and window result do not yet exist when `WHERE` is evaluated. Use another query level:

```sql
WITH ranked AS (
    SELECT e.*,
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM Employee AS e
)
SELECT *
FROM ranked
WHERE rn <= 10;
```

### Outer ordering is last

The [[Window ORDER BY]] controls a calculation, while the outer `ORDER BY` controls presentation.

## Physical execution

The optimizer may reorder joins, use indexes, or transform subqueries as long as it preserves the logical result. Logical order is a reasoning model, not a trace of runtime steps.

## Related notes

- [[SQL and Relational Algebra Correspondence]]
- [[WHERE vs HAVING]]
- [[SQL Window Functions]]

