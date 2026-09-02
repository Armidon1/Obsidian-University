---
title: "Relational Data Model"
tags: [data-management, relational-model, definition]
source: "[[1-Introduction.pdf]]"
---

# Relational Data Model

> [!definition]
> The relational data model represents data as **relations**. Mathematically, a relation is a subset of a Cartesian product of domains.

Given domains $D_1, D_2, \ldots, D_k$, a $k$-ary relation $R$ satisfies:

$$
R \subseteq D_1 \times D_2 \times \cdots \times D_k
$$

Each element $(a_1,\ldots,a_k)$ is a **tuple**. A relation can be visualized as a table, where tuples are rows and attributes are columns, but the mathematical definition is more precise than the visual metaphor.

## Core vocabulary

| Concept | Meaning |
|---|---|
| Relation schema | Relation name and attributes, e.g. `Account(branch, number, customer, balance)` |
| Relation instance | The tuples currently belonging to that relation |
| Attribute | A named tuple component |
| Domain | The admissible values and interpretation of an attribute |
| Arity | Number of attributes |
| Cardinality | Number of tuples in an instance |

## Important properties

A mathematical relation:

- contains no duplicate tuples;
- has no intrinsic row order;
- treats attribute values according to their domains;
- is manipulated through operations that return new relations.

The last property gives [[Relational Algebra]] its closure: operators can be composed because every result is again a relation.

> [!warning] Relation versus SQL table
> SQL tables commonly use bag semantics, may contain `NULL`, and can contain duplicates. SQL output is unordered unless an outer `ORDER BY` is present. See [[Set Semantics vs Bag Semantics]] and [[NULL and Three-Valued Logic]].

## Example

| branch_name | account_no | customer_name | balance |
|---|---|---|---:|
| Orsay | 10991-06284 | Abiteboul | 3567.53 |
| Hawthorne | 10992-35671 | Hull | 11245.75 |

The schema describes the meaning and structure of the table. The two displayed rows form one possible instance of that schema.

## Related notes

- [[Relational Algebra]]
- [[Relational Calculus]]
- [[Set Semantics vs Bag Semantics]]
- [[SQL and Relational Algebra Correspondence]]

