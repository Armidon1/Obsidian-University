---
title: "RANK vs DENSE_RANK vs ROW_NUMBER"
tags: [data-management, sql, window-functions, ranking]
source: "[[1-Introduction.pdf]]"
---

# RANK vs DENSE_RANK vs ROW_NUMBER

> [!definition]
> These functions assign positions to ordered rows but use different rules for ties.

For salaries `5000, 5000, 4500, 4000`:

| Salary | `ROW_NUMBER()` | `RANK()` | `DENSE_RANK()` |
|---:|---:|---:|---:|
| 5000 | 1 | 1 | 1 |
| 5000 | 2 | 1 | 1 |
| 4500 | 3 | 3 | 2 |
| 4000 | 4 | 4 | 3 |

## Rules

- `ROW_NUMBER`: every row gets a unique sequential number.
- `RANK`: peers share a rank; later ranks leave gaps.
- `DENSE_RANK`: peers share a rank; later ranks have no gaps.

## Query

```sql
SELECT employee_id,
       salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_number,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM Employee;
```

## Choosing correctly

- Choose `ROW_NUMBER` when exactly one row must occupy each position.
- Choose `RANK` for competition ranking: two first places make the next place third.
- Choose `DENSE_RANK` to number distinct ordered values consecutively.

## Tie-breaker warning

Peer groups are defined by the complete [[Window ORDER BY]]. Adding a unique `employee_id` to `RANK()` makes tied salaries no longer peers. Add tie-breakers to `ROW_NUMBER` for determinism; do not add them to ranking functions unless breaking ties is intended.

## Related notes

- [[ROW_NUMBER]]
- [[Top-N per Group]]
- [[Finding Minimum or Maximum Rows per Group]]

