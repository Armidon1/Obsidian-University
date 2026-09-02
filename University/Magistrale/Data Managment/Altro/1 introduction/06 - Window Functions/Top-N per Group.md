---
title: "Top-N per Group"
tags: [data-management, sql, window-functions, ranking]
source: "[[1-Introduction.pdf]]"
---

# Top-N per Group

> [!definition]
> A top-N-per-group query returns the highest or lowest $N$ rows or value levels independently inside each group.

## Exactly N rows per department

```sql
WITH ranked AS (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC, employee_id
           ) AS rn
    FROM Employee AS e
)
SELECT *
FROM ranked
WHERE rn <= 3;
```

`ROW_NUMBER` returns at most three rows per department and resolves ties through `employee_id`.

## Include all ties at the boundary

```sql
WITH ranked AS (
    SELECT e.*,
           DENSE_RANK() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS salary_level
    FROM Employee AS e
)
SELECT *
FROM ranked
WHERE salary_level <= 3;
```

This returns all employees belonging to the three highest distinct salary levels, possibly more than three rows.

## `RANK` alternative

`RANK <= 3` uses competition positions. A large tie at rank 1 can make the next rank larger than 3, so fewer than three distinct levels may appear.

## Why an outer query is required

Window functions are evaluated after `WHERE` in their query block. The CTE first computes the rank; the outer query can then filter it. See [[Logical Order of SQL Query Evaluation]].

## Selection question

Decide whether "top 3" means:

- exactly three rows;
- all rows tied within the first three positions;
- the three highest distinct values.

That decision determines the ranking function.

## Related notes

- [[ROW_NUMBER]]
- [[RANK vs DENSE_RANK vs ROW_NUMBER]]
- [[Finding Minimum or Maximum Rows per Group]]

