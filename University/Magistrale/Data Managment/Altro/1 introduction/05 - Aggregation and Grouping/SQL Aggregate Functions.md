---
title: "SQL Aggregate Functions"
tags: [data-management, sql, aggregation]
source: "[[1-Introduction.pdf]]"
---

# SQL Aggregate Functions

> [!definition]
> An aggregate function maps a collection of input rows or values to one summary value.

Common aggregate functions are:

- `COUNT` - number of rows or non-`NULL` values;
- `SUM` - total of non-`NULL` numeric values;
- `AVG` - arithmetic mean of non-`NULL` numeric values;
- `MIN` - least non-`NULL` value;
- `MAX` - greatest non-`NULL` value.

## Global aggregation

Without `GROUP BY`, all rows surviving `FROM` and `WHERE` form one group:

```sql
SELECT MIN(age), AVG(income)
FROM Person
WHERE age >= 18;
```

The result contains one row.

## Grouped aggregation

```sql
SELECT age, AVG(income)
FROM Person
GROUP BY age;
```

The result contains one row per distinct age group. See [[GROUP BY]].

## `DISTINCT` inside an aggregate

```sql
COUNT(DISTINCT income)
```

removes duplicate non-`NULL` values before counting. This is different from placing `DISTINCT` after `SELECT`, which removes duplicate final rows.

## Aggregate versus row retrieval

`MAX(income)` returns the largest income, not the person earning it. Retrieving associated rows requires a subquery, join, or window function. See [[Finding Minimum or Maximum Rows per Group]].

## Aggregate functions as windows

The same functions can preserve detail rows when followed by `OVER(...)`:

```sql
SUM(salary) OVER (PARTITION BY department)
```

See [[Aggregate Window Functions]].

## Related notes

- [[COUNT in SQL]]
- [[NULL and Aggregate Functions]]
- [[GROUP BY]]

