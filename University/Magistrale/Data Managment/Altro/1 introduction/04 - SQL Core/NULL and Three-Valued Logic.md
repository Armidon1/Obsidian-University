---
title: "NULL and Three-Valued Logic"
tags: [data-management, sql, null, logic]
source: "[[1-Introduction.pdf]]"
---

# NULL and Three-Valued Logic

> [!definition]
> `NULL` represents a missing, unknown, or inapplicable value. SQL comparisons involving `NULL` generally produce `UNKNOWN`, creating three-valued logic: `TRUE`, `FALSE`, and `UNKNOWN`.

## Testing `NULL`

This is incorrect:

```sql
WHERE income = NULL
```

Use:

```sql
WHERE income IS NULL
```

or:

```sql
WHERE income IS NOT NULL
```

## Filtering behavior

`WHERE` retains only rows for which its condition is `TRUE`. Both `FALSE` and `UNKNOWN` are rejected. Therefore, `income > 20` does not retain rows with `NULL` income.

## `NOT IN` trap

If a `NOT IN` subquery returns a `NULL`, comparisons may become `UNKNOWN`:

```sql
WHERE scode NOT IN (SELECT school FROM Graduated)
```

For absence queries, `NOT EXISTS` is usually safer. See [[Queries Expressing Absence]].

## Null-safe equality in PostgreSQL

```sql
a IS NOT DISTINCT FROM b
```

treats two `NULL` values as equal and one `NULL` plus one non-`NULL` as different. This is useful when matching grouped `NULL` keys back to detail rows.

## Aggregates and windows

Most aggregate functions ignore `NULL` inputs, while `COUNT(*)` counts rows. `PARTITION BY` groups `NULL` partition keys together. See [[NULL and Aggregate Functions]] and [[PARTITION BY]].

> [!important]
> `NULL` is not zero, an empty string, or a special ordinary value. Its meaning and logic must be handled explicitly.

## Related notes

- [[COUNT in SQL]]
- [[NULL and Aggregate Functions]]
- [[Queries Expressing Absence]]

