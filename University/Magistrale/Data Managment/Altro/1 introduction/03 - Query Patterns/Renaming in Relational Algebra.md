---
title: "Renaming in Relational Algebra"
tags: [data-management, relational-algebra, operator, self-join]
source: "[[1-Introduction.pdf]]"
---

# Renaming in Relational Algebra

> [!definition]
> Renaming assigns new relation or attribute names so that expressions remain unambiguous and schemas become compatible.

A common notation is $\rho$:

$$
\rho_{G_1(gcode_1,mark_1,school_1)}(Graduated)
$$

The course notation also allows attribute renaming within projection:

$$
\pi_{N\leftarrow Name,\;A\leftarrow Age}(Employee)
$$

## Why renaming is necessary

### Self-joins

Comparing a relation with itself requires two logical roles. To test whether a student has a greater mark than another student in the same school, use `G1` and `G2` rather than two indistinguishable references to `Graduated`.

### Attribute compatibility

Before union or difference, corresponding attributes may need aligned names. For example, rename `school` to `scode` before subtracting it from a projection of `School`.

### Readability

Short aliases expose each table's role:

```sql
SELECT g1.gcode
FROM Graduated AS g1
JOIN Graduated AS g2
  ON g1.school = g2.school
 AND g1.mark > g2.mark;
```

## SQL distinction

SQL table aliases rename a table reference for the current query. Column aliases rename output expressions. They do not normally change stored schema names.

## Related notes

- [[SQL Aliases and Attribute Qualification]]
- [[Finding Minimum or Maximum Rows per Group]]
- [[Projection in Relational Algebra]]

