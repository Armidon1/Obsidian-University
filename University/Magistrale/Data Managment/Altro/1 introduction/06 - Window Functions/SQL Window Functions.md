---
title: "SQL Window Functions"
tags: [data-management, sql, window-functions, definition]
source: "[[1-Introduction.pdf]]"
---

# SQL Window Functions

> [!definition]
> A window function calculates a value over rows related to the current row without collapsing the current row out of the result.

The general form is:

```sql
function(arguments) OVER (
    [PARTITION BY ...]
    [ORDER BY ...]
    [frame_clause]
)
```

## Mental model

For each current row:

1. identify its partition;
2. establish the logical order when required;
3. identify the applicable frame when relevant;
4. calculate the function;
5. attach the value to the current row.

## Main families

- Ranking: [[ROW_NUMBER]], [[RANK vs DENSE_RANK vs ROW_NUMBER]].
- Aggregate windows: [[Aggregate Window Functions]].
- Navigation: [[LAG and LEAD]].
- Distribution: `PERCENT_RANK`, `CUME_DIST`, `NTILE` where supported.

## Basic example

```sql
SELECT employee_id,
       department,
       salary,
       SUM(salary) OVER (
           PARTITION BY department
       ) AS department_total
FROM Employee;
```

Every employee remains visible. The department total repeats for rows in the same department.

## Evaluation position

Window functions are evaluated after `WHERE`, grouping, and `HAVING` in the same query block. Filtering a window result normally requires a subquery or CTE. See [[Logical Order of SQL Query Evaluation]].

## Core distinction

[[GROUP BY]] changes result granularity. A window function usually preserves the granularity available to its query block. See [[GROUP BY vs Window Functions]].

## Related notes

- [[OVER Clause]]
- [[PARTITION BY]]
- [[Window ORDER BY]]
- [[Window Frames]]

