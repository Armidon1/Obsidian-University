---
title: "Aggregate Window Functions"
tags: [data-management, sql, window-functions, aggregation]
source: "[[1-Introduction.pdf]]"
---

# Aggregate Window Functions

> [!definition]
> An aggregate window function computes an aggregate over a window while preserving the current result row.

Functions such as `SUM`, `AVG`, `COUNT`, `MIN`, and `MAX` become window functions when followed by [[OVER Clause|`OVER(...)`]].

## Grand total

```sql
SUM(salary) OVER () AS company_total
```

Every row receives the total across the query block.

## Partition total

```sql
SUM(salary) OVER (
    PARTITION BY department
) AS department_total
```

Every employee receives their department's total.

## Percentage of total

```sql
salary * 100.0 /
NULLIF(
    SUM(salary) OVER (PARTITION BY department),
    0
) AS department_percentage
```

`NULLIF` prevents division by zero.

## Running aggregate

```sql
SUM(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_amount
```

Adding order and a frame changes a full-partition total into a cumulative value.

## `NULL`

Aggregate windows inherit ordinary aggregate treatment of `NULL`: for example, `SUM(salary)` ignores `NULL` salaries. The detail row with a missing salary still remains visible.

## Related notes

- [[SQL Aggregate Functions]]
- [[GROUP BY vs Window Functions]]
- [[Running Totals]]
- [[Moving Averages]]

