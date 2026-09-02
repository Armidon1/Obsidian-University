---
title: "GROUP BY"
tags: [data-management, sql, grouping]
source: "[[1-Introduction.pdf]]"
---

# GROUP BY

> [!definition]
> `GROUP BY` partitions the rows surviving `FROM` and `WHERE` according to grouping expressions and produces one output row per group.

## Example

```sql
SELECT father, COUNT(*) AS num_children
FROM Paternity
GROUP BY father;
```

The input has one row per parent-child fact. The output has one row per father. This is a change in [[SQL Query Granularity]].

## Conceptual evaluation

1. Build source rows with `FROM` and joins.
2. Filter detail rows with `WHERE`.
3. Place rows sharing grouping values into one group.
4. Evaluate aggregates per group.
5. Emit one row per group.

## Multiple grouping columns

```sql
SELECT department, job_title, AVG(salary)
FROM Employee
GROUP BY department, job_title;
```

Each distinct `(department, job_title)` pair defines a group.

## `NULL` grouping keys

Rows with `NULL` in the same grouping position are placed in one group. This does not mean that ordinary equality with `NULL` returns true; grouping uses its own not-distinct notion.

## Target-list rule

Every selected expression must have one value per group. It should be grouped, aggregated, or accepted as functionally determined. See [[Homogeneous Target List]].

## Difference from partitioning

`GROUP BY` collapses each group. `PARTITION BY` inside a window function preserves every row. See [[GROUP BY vs Window Functions]].

## Related notes

- [[SQL Aggregate Functions]]
- [[WHERE vs HAVING]]
- [[SQL Query Granularity]]

