---
title: "ROW_NUMBER"
tags: [data-management, sql, window-functions, ranking]
source: "[[1-Introduction.pdf]]"
---

# ROW_NUMBER

> [!definition]
> `ROW_NUMBER()` assigns the integers 1, 2, 3, ... to rows according to the window order, restarting in every partition.

```sql
SELECT employee_id,
       department,
       salary,
       ROW_NUMBER() OVER (
           PARTITION BY department
           ORDER BY salary DESC, employee_id
       ) AS row_num
FROM Employee;
```

## Behavior

- Every row receives a different number inside its partition.
- Numbering restarts at 1 when the partition changes.
- Equal salaries do not receive the same number.
- A unique tie-breaker makes numbering deterministic.

## Ties

Without `employee_id` in the order, tied salaries have no defined internal sequence. The database must assign different row numbers, but repeated executions need not assign them to the same employees.

## Common uses

### Exactly one row per group

```sql
WITH numbered AS (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC, employee_id
           ) AS rn
    FROM Employee AS e
)
SELECT *
FROM numbered
WHERE rn = 1;
```

### Deduplication

Partition by the duplicate key, order by quality or recency, and keep `rn = 1`.

### Pagination

Row numbers can identify ranges, although keyset pagination may be more stable for changing, large datasets.

## Choosing another function

Use `RANK` or `DENSE_RANK` when ties should share a position. See [[RANK vs DENSE_RANK vs ROW_NUMBER]].

## Related notes

- [[Top-N per Group]]
- [[Window ORDER BY]]
- [[PARTITION BY]]

