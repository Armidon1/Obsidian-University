---
title: "Homogeneous Target List"
tags: [data-management, sql, grouping, correctness]
source: "[[1-Introduction.pdf]]"
---

# Homogeneous Target List

> [!definition]
> In an aggregate or grouped query, every selected expression must have one well-defined value at the result's current granularity.

## Ambiguous query

```sql
SELECT age, income
FROM Person
GROUP BY age;
```

One age group may contain several incomes. The query does not specify which income should represent the group.

## Well-defined query

```sql
SELECT age, AVG(income) AS average_income
FROM Person
GROUP BY age;
```

`age` identifies the group, and the average has one value for that group.

## Global aggregation

This is similarly ambiguous:

```sql
SELECT name, MAX(income)
FROM Person;
```

`MAX(income)` has one global value, while `name` may have many. To retrieve the person associated with the maximum, use [[Finding Minimum or Maximum Rows per Group]].

## Functional dependencies

Some DBMSs accept an ungrouped column when it is functionally determined by grouped key columns. For example, grouping by a declared primary key determines every column of that row. Exact recognition rules depend on the DBMS.

## Permissive behavior

Some systems or configurations may return an arbitrary group value instead of rejecting an ambiguous query. Such results should not be relied upon because they obscure intent and can be non-deterministic.

## Related notes

- [[GROUP BY]]
- [[SQL Query Granularity]]
- [[GROUP BY vs Window Functions]]

