---
title: "SQL and Relational Algebra Correspondence"
tags: [data-management, sql, relational-algebra]
source: "[[1-Introduction.pdf]]"
---

# SQL and Relational Algebra Correspondence

> [!definition]
> The core of a SQL `SELECT` query can be interpreted through relational algebra: `FROM` forms tuple combinations, `WHERE` selects rows, and `SELECT DISTINCT` projects attributes.

| SQL clause | Relational algebra role |
|---|---|
| `FROM R1, ..., Rk` | $R_1\times\cdots\times R_k$ |
| `WHERE gamma` | $\sigma_{\gamma}$ |
| `SELECT DISTINCT A1, ..., Am` | $\pi_{A_1,\ldots,A_m}$ |

Thus:

```sql
SELECT DISTINCT e.name
FROM Employee AS e, Department AS d
WHERE e.department = d.code
  AND d.city = 'Rome';
```

corresponds to:

$$
\pi_{e.name}(\sigma_{e.department=d.code\land d.city="Rome"}(Employee\times Department))
$$

## Semantic, not physical, interpretation

The formula explains the result. A DBMS is not required to build the full Cartesian product. Its optimizer can push filters downward and select an efficient join algorithm.

## Duplicate semantics

Classical algebra uses sets. Basic SQL uses bags. `DISTINCT` is included in the correspondence because it removes duplicates. See [[Set Semantics vs Bag Semantics]].

## Modern SQL extends the core

SQL additionally includes:

- grouping and aggregate functions;
- outer joins;
- subqueries and common table expressions;
- recursive queries;
- ordering and limiting;
- [[SQL Window Functions]].

These constructs require an extended algebra or additional semantic rules.

## Related notes

- [[Relational Algebra]]
- [[Logical Order of SQL Query Evaluation]]
- [[SQL Aliases and Attribute Qualification]]

