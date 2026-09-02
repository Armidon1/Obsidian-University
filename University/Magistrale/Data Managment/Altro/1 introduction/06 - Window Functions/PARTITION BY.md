---
title: "PARTITION BY"
tags: [data-management, sql, window-functions, partitioning]
source: "[[1-Introduction.pdf]]"
---

# PARTITION BY

> [!definition]
> `PARTITION BY` divides the rows available to a window function into independent groups without collapsing them.

```sql
SUM(salary) OVER (
    PARTITION BY department
)
```

For every employee, this sums salaries of employees in the same department.

## If partitioning is omitted

```sql
SUM(salary) OVER ()
```

All available rows belong to one partition.

## Multiple expressions

```sql
AVG(amount) OVER (
    PARTITION BY customer_id, currency
)
```

Each distinct `(customer_id, currency)` combination defines a partition.

## `NULL` keys

Rows whose partition expressions are all not distinct, including rows sharing `NULL`, belong to the same partition. An employee with `NULL department` is not excluded automatically.

## Partition versus frame

The partition defines the maximum set in which a window function operates. An ordered [[Window Frames|frame]] may select only part of that partition for the current row.

## Partition versus grouping

Both identify groups, but their output behavior differs:

- [[GROUP BY]] emits one row per group.
- `PARTITION BY` retains every row and restarts the window calculation at group boundaries.

## Typical uses

- ranks per department;
- previous transaction per account;
- running total per customer;
- group total beside detail rows.

## Related notes

- [[OVER Clause]]
- [[GROUP BY vs Window Functions]]
- [[Aggregate Window Functions]]

