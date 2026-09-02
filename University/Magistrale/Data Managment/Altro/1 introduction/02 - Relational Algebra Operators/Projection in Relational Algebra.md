---
title: "Projection in Relational Algebra"
tags: [data-management, relational-algebra, operator]
source: "[[1-Introduction.pdf]]"
---

# Projection in Relational Algebra

> [!definition]
> Projection is a unary operator that selects, reorders, and optionally renames attributes. Under set semantics it also eliminates duplicate result tuples.

The notation is:

$$
\pi_{A_1,\ldots,A_m}(R)
$$

## Example

For `Employee(Code, Name, Site, Salary)`:

$$
\pi_{Name,Site}(Employee)
$$

keeps only `Name` and `Site`. If two employees have the same pair of values, the result contains that tuple once.

Projection can reorder attributes:

$$
\pi_{Site,Name}(Employee)
$$

and can rename them:

$$
\pi_{N\leftarrow Name,\;S\leftarrow Site}(Employee)
$$

## Positional notation

If $R(A,B,C,D)$, then:

$$
\pi_{C,A}(R)=\pi_{3,1}(R)
$$

Named attributes are generally safer because schema reordering does not change their meaning.

## Properties

Projection changes arity and may reduce cardinality. Nested projections can often be simplified when the outer attribute set is contained in the inner one:

$$
\pi_A(\pi_{A,B}(R))=\pi_A(R)
$$

## SQL counterpart

```sql
SELECT DISTINCT name, site
FROM Employee;
```

`DISTINCT` is needed to reproduce algebraic set semantics. Without it, SQL preserves duplicate projected rows.

> [!tip]
> Selection answers "which tuples?" Projection answers "which attributes?" A typical query applies both: $\pi_{Name}(\sigma_{Salary>50}(Employee))$.

## Related notes

- [[Selection in Relational Algebra]]
- [[Set Semantics vs Bag Semantics]]
- [[Renaming in Relational Algebra]]

