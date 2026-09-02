---
title: "LAG and LEAD"
tags: [data-management, sql, window-functions, navigation]
source: "[[1-Introduction.pdf]]"
---

# LAG and LEAD

> [!definition]
> `LAG` retrieves an expression from a preceding row in the window order. `LEAD` retrieves it from a following row.

```sql
SELECT employee_id,
       department,
       salary,
       LAG(salary) OVER (
           PARTITION BY department
           ORDER BY salary, employee_id
       ) AS previous_salary,
       LEAD(salary) OVER (
           PARTITION BY department
           ORDER BY salary, employee_id
       ) AS next_salary
FROM Employee;
```

## Boundaries

- The first row has no predecessor, so `LAG` returns `NULL` by default.
- The last row has no successor, so `LEAD` returns `NULL` by default.
- Navigation never crosses a partition boundary.

## Offset and default

```sql
LAG(value, 2, 0) OVER (...)
```

looks two rows backward and returns `0` if such a row does not exist.

## Change calculation

```sql
salary - LAG(salary) OVER (
    PARTITION BY employee_id
    ORDER BY effective_date
) AS salary_change
```

This pattern measures changes between consecutive salaries, prices, purchases, sensor readings, or dates.

## Ordering requirement

"Previous" has no meaning without an explicit order. Use a deterministic ordering key when timestamps can tie.

## Frame note

In PostgreSQL, `LAG` and `LEAD` navigate by partition position rather than by the aggregate frame. The window ordering and partition are the essential components.

## Related notes

- [[Window ORDER BY]]
- [[PARTITION BY]]
- [[Running Totals]]

