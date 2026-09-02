---
title: "SQL Aliases and Attribute Qualification"
tags: [data-management, sql, naming]
source: "[[1-Introduction.pdf]]"
---

# SQL Aliases and Attribute Qualification

> [!definition]
> A table alias gives one table reference a temporary name. Attribute qualification identifies a column through that reference, such as `e.department`.

## Table aliases

```sql
SELECT e.name
FROM Employee AS e;
```

Aliases are especially important in joins:

```sql
SELECT e.name, d.chair
FROM Employee AS e
JOIN Department AS d
  ON e.department = d.code;
```

## Self-joins

The same base table can appear in different roles:

```sql
SELECT g1.gcode
FROM Graduated AS g1
JOIN Graduated AS g2
  ON g1.school = g2.school
 AND g1.mark > g2.mark;
```

Without `g1` and `g2`, the comparison would be ambiguous. This is the SQL counterpart of [[Renaming in Relational Algebra]].

## Column aliases

```sql
SELECT AVG(income) AS average_income
FROM Person;
```

A column alias names an output expression. Because of [[Logical Order of SQL Query Evaluation]], an alias is not generally available in `WHERE` of the same query block, although it can often be used in the outer `ORDER BY`.

## Good practice

- Use short but meaningful aliases.
- Qualify columns when multiple inputs contain the same name.
- Prefer stable keys over names when defining joins.
- Do not reuse one alias for conceptually different roles.

## Related notes

- [[Theta Join]]
- [[Equijoin]]
- [[Renaming in Relational Algebra]]

