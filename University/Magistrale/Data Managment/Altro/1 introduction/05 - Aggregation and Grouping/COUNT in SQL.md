---
title: "COUNT in SQL"
tags: [data-management, sql, aggregation, count]
source: "[[1-Introduction.pdf]]"
---

# COUNT in SQL

> [!definition]
> `COUNT` returns a number describing rows or non-`NULL` expression values.

## Three forms

### Count rows

```sql
COUNT(*)
```

Counts every row, even when some or all columns contain `NULL`.

### Count non-null values

```sql
COUNT(income)
```

Counts rows whose `income` is not `NULL`. Duplicate incomes count separately.

### Count distinct non-null values

```sql
COUNT(DISTINCT income)
```

Counts different non-`NULL` incomes.

## Example

For incomes `21, NULL, 21, 35`:

| Expression | Result |
|---|---:|
| `COUNT(*)` | 4 |
| `COUNT(income)` | 3 |
| `COUNT(DISTINCT income)` | 2 |

## Conditional counting

In PostgreSQL:

```sql
COUNT(*) FILTER (WHERE mark = 100)
```

counts only rows satisfying the filter. A portable alternative is:

```sql
SUM(CASE WHEN mark = 100 THEN 1 ELSE 0 END)
```

## Empty input

`COUNT` returns `0` for an empty input, unlike `SUM`, `AVG`, `MIN`, and `MAX`, which generally return `NULL`.

> [!tip]
> To count entities, start with `COUNT(*)`. Use `COUNT(column)` only when ignoring missing values is part of the intended question.

## Related notes

- [[SQL Aggregate Functions]]
- [[NULL and Aggregate Functions]]
- [[NULL and Three-Valued Logic]]

