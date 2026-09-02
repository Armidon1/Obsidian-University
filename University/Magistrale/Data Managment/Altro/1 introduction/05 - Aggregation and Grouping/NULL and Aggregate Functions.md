---
title: "NULL and Aggregate Functions"
tags: [data-management, sql, aggregation, null]
source: "[[1-Introduction.pdf]]"
---

# NULL and Aggregate Functions

> [!definition]
> Most SQL aggregate functions ignore `NULL` input values rather than treating them as zero.

For incomes `30, NULL, 36, 36`:

```sql
SELECT AVG(income)
FROM Person;
```

returns:

$$
(30+36+36)/3=34
$$

The denominator is 3 because only non-`NULL` incomes contribute.

## Behavior summary

| Aggregate | Treatment of `NULL` |
|---|---|
| `COUNT(*)` | Counts the row |
| `COUNT(expr)` | Ignores `NULL` expression values |
| `SUM(expr)` | Ignores `NULL` values |
| `AVG(expr)` | Ignores `NULL` values in numerator and denominator |
| `MIN(expr)`, `MAX(expr)` | Ignore `NULL` values |

If no non-`NULL` value exists, `SUM`, `AVG`, `MIN`, and `MAX` normally return `NULL`; `COUNT(expr)` returns `0`.

## Why `COALESCE` changes meaning

```sql
AVG(COALESCE(income, 0))
```

treats missing incomes as zero. This is not merely formatting: it changes both the numerator and denominator. Use it only if zero is the intended replacement.

To replace only the final missing aggregate result:

```sql
COALESCE(AVG(income), 0)
```

## Outer joins

After a left join, `COUNT(*)` counts the preserved row even without a match, while `COUNT(matched_table.id)` counts actual matches. This difference is a common source of mistakes.

## Related notes

- [[NULL and Three-Valued Logic]]
- [[COUNT in SQL]]
- [[SQL Aggregate Functions]]

