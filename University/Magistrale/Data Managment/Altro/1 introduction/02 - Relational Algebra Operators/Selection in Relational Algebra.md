---
title: "Selection in Relational Algebra"
tags: [data-management, relational-algebra, operator]
source: "[[1-Introduction.pdf]]"
---

# Selection in Relational Algebra

> [!definition]
> Selection is a unary relational operator that retains the tuples satisfying a condition while preserving the relation's attributes.

The notation is:

$$
\sigma_{\Theta}(R)=\{t\in R\mid \Theta(t)\}
$$

where $\Theta$ is evaluated independently for every tuple.

## Conditions

Atomic conditions compare constants, attributes, or positional components using $=, \neq, <, >, \leq, \geq$. More complex conditions use:

- conjunction $\land$;
- disjunction $\lor$;
- negation $\neg$.

Examples:

$$
\sigma_{Salary>50}(Employee)
$$

$$
\sigma_{Branch="Aptos"\land Balance<1000}(Savings)
$$

Ordered comparisons require a meaningful order on the attribute domain. Equality can be used even when no total order exists.

## Properties

Selection changes cardinality but not arity. It is commutative when selections are composed:

$$
\sigma_A(\sigma_B(R))=\sigma_B(\sigma_A(R))=\sigma_{A\land B}(R)
$$

This law helps an optimizer push selective predicates close to base relations before expensive joins.

## SQL counterpart

The basic counterpart is `WHERE`:

```sql
SELECT *
FROM Employee
WHERE salary > 50;
```

Classical algebra uses two-valued logic. SQL uses three-valued logic when `NULL` is involved; see [[NULL and Three-Valued Logic]].

## Common mistakes

- Confusing selection of **rows** with [[Projection in Relational Algebra]], which selects columns.
- Applying a condition to an attribute that does not exist in the current expression.
- Assuming comparisons with `NULL` behave like ordinary equality in SQL.

## Related notes

- [[Projection in Relational Algebra]]
- [[Theta Join]]
- [[SQL and Relational Algebra Correspondence]]

