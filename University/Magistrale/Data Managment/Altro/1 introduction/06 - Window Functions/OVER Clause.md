---
title: "OVER Clause"
tags: [data-management, sql, window-functions]
source: "[[1-Introduction.pdf]]"
---

# OVER Clause

> [!definition]
> `OVER(...)` marks an expression as a window function and defines the rows, ordering, and frame used by its calculation.

## Empty window specification

```sql
SUM(salary) OVER ()
```

All rows available to the query block form one partition. The grand total is attached to every row.

## Partitioned specification

```sql
SUM(salary) OVER (
    PARTITION BY department
)
```

The total is calculated independently per department. See [[PARTITION BY]].

## Ordered specification

```sql
ROW_NUMBER() OVER (
    PARTITION BY department
    ORDER BY salary DESC
)
```

The ordering controls row positions inside each partition. See [[Window ORDER BY]].

## Framed specification

```sql
SUM(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

This defines a running total. See [[Window Frames]].

## Named windows

SQL can name and reuse a specification:

```sql
SELECT employee_id,
       RANK() OVER w AS salary_rank,
       AVG(salary) OVER w AS ordered_average
FROM Employee
WINDOW w AS (
    PARTITION BY department
    ORDER BY salary DESC
);
```

Named windows reduce repetition, but confirm whether a frame is appropriate for every function sharing the definition.

## Related notes

- [[SQL Window Functions]]
- [[PARTITION BY]]
- [[Window ORDER BY]]
- [[Window Frames]]

