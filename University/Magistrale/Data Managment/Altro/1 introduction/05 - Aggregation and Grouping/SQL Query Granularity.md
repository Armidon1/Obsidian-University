---
title: "SQL Query Granularity"
tags: [data-management, sql, grouping, window-functions]
source: "[[1-Introduction.pdf]]"
---

# SQL Query Granularity

> [!definition]
> Query granularity is what one row of a result represents.

Examples include:

- one row per employee;
- one row per transaction;
- one row per department;
- one row per department and month.

## Why granularity matters

Selected columns must be meaningful at the current granularity. If a grouped query produces one row per department, an arbitrary employee name has no single value for that row.

```sql
SELECT department, SUM(salary)
FROM Employee
GROUP BY department;
```

This result has department granularity.

## Granularity-changing operations

- [[GROUP BY]] collapses detail rows into groups.
- `DISTINCT` can collapse duplicate projected rows.
- joins may multiply rows when one record matches several records.
- aggregation without grouping produces one global row.

## Granularity-preserving analytics

```sql
SELECT e.*,
       SUM(salary) OVER (
           PARTITION BY department
       ) AS department_total
FROM Employee AS e;
```

This keeps employee granularity while adding department-level information. See [[GROUP BY vs Window Functions]].

## Diagnostic questions

Before writing a query, ask:

1. What should one output row represent?
2. Which table already has that granularity?
3. Can a join duplicate those rows?
4. Should groups replace detail rows or annotate them?
5. How should ties and missing matches behave?

## Related notes

- [[Homogeneous Target List]]
- [[GROUP BY]]
- [[SQL Window Functions]]

