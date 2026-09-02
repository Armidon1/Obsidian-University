---
title: "Set Semantics vs Bag Semantics"
tags: [data-management, sql, relational-model, duplicates]
source: "[[1-Introduction.pdf]]"
---

# Set Semantics vs Bag Semantics

> [!definition]
> Under **set semantics**, each distinct tuple occurs at most once. Under **bag** or **multiset semantics**, the same tuple may occur multiple times.

## Relational algebra

Classical [[Relational Algebra]] uses sets. Consequently:

- a projection eliminates duplicate tuples;
- union returns each tuple once;
- relation cardinality counts distinct tuples;
- row order has no semantic meaning.

## SQL

SQL normally uses bag semantics. Therefore:

```sql
SELECT name, city
FROM Person;
```

may return the same `(name, city)` pair more than once. To request duplicate elimination:

```sql
SELECT DISTINCT name, city
FROM Person;
```

`SELECT DISTINCT` is the closest basic SQL counterpart to set-based projection.

## Set operators in SQL

SQL distinguishes:

- `UNION`, which removes duplicates;
- `UNION ALL`, which preserves them;
- similarly, some systems provide `INTERSECT ALL` and `EXCEPT ALL`.

Bag semantics often avoids the cost of duplicate elimination and preserves multiplicities that may carry useful information. It also means that translating relational algebra into SQL sometimes requires an explicit `DISTINCT`.

## Common misconception

Duplicate-looking rows are not necessarily duplicate base records: unselected key columns may differ. A projection can make distinct input rows appear identical.

> [!warning]
> Neither set nor bag semantics gives rows an intrinsic order. Only an outer `ORDER BY` makes presentation order part of the SQL request.

## Related notes

- [[Relational Data Model]]
- [[Projection in Relational Algebra]]
- [[Union in Relational Algebra]]
- [[SQL Query Granularity]]

