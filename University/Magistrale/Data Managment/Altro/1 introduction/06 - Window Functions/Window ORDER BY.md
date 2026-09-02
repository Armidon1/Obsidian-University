---
title: "Window ORDER BY"
tags: [data-management, sql, window-functions, ordering]
source: "[[1-Introduction.pdf]]"
---

# Window ORDER BY

> [!definition]
> The `ORDER BY` inside `OVER(...)` defines the logical sequence used by a window function within each partition.

```sql
ROW_NUMBER() OVER (
    PARTITION BY department
    ORDER BY salary DESC, employee_id
)
```

## Different from final ordering

```sql
SELECT employee_id,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM Employee
ORDER BY employee_id;
```

Employees are numbered by descending salary but displayed by `employee_id`. The inner order controls calculation; the outer order controls presentation.

## Determinism

If two rows have the same ordering values, they are peers. `ROW_NUMBER` still assigns different numbers, but their relative order is unspecified unless a unique tie-breaker is added.

```sql
ORDER BY salary DESC, employee_id
```

creates a deterministic total order when `employee_id` is unique.

## Ties and ranking

For `RANK` and `DENSE_RANK`, peer status is defined by the complete ordering key. Adding `employee_id` breaks salary ties, which may be undesirable. See [[RANK vs DENSE_RANK vs ROW_NUMBER]].

## Ordered aggregates

Adding window ordering to an aggregate often changes a full-partition total into a cumulative calculation depending on the frame. See [[Running Totals]] and [[ROWS vs RANGE]].

## Related notes

- [[OVER Clause]]
- [[ROW_NUMBER]]
- [[Window Frames]]

