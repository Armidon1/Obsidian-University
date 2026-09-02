---
title: "GROUP BY vs Window Functions"
tags: [data-management, sql, grouping, window-functions]
source: "[[1-Introduction.pdf]]"
---

# GROUP BY vs Window Functions

> [!definition]
> `GROUP BY` produces one row per group. A window function computes over related rows while retaining each current row.

## Grouped total

```sql
SELECT department,
       SUM(salary) AS department_total
FROM Employee
GROUP BY department;
```

One result row represents one department.

## Windowed total

```sql
SELECT employee_id,
       department,
       salary,
       SUM(salary) OVER (
           PARTITION BY department
       ) AS department_total
FROM Employee;
```

One result row still represents one employee.

| `GROUP BY` | Window function |
|---|---|
| Collapses a group | Preserves rows |
| Changes granularity | Annotates current granularity |
| Group columns belong in the target list | Detail columns remain selectable |
| Designed for summaries | Designed for analytics and comparisons |

## Why detail columns fail with grouping

```sql
SELECT name, department, salary, SUM(salary)
FROM Employee
GROUP BY department;
```

The query is ambiguous because a department contains multiple names and salaries. See [[Homogeneous Target List]].

## Can windows be emulated?

A grouped subquery can be joined back to detail rows:

```sql
SELECT e.*, d.department_total
FROM Employee AS e
JOIN (
    SELECT department, SUM(salary) AS department_total
    FROM Employee
    GROUP BY department
) AS d
  ON e.department IS NOT DISTINCT FROM d.department;
```

The window formulation is usually clearer and supports ranking, navigation, and framed calculations directly.

## Related notes

- [[SQL Query Granularity]]
- [[GROUP BY]]
- [[Aggregate Window Functions]]

