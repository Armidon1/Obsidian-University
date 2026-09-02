---
title: "Union in Relational Algebra"
tags: [data-management, relational-algebra, operator, set-operations]
source: "[[1-Introduction.pdf]]"
---

# Union in Relational Algebra

> [!definition]
> Union returns every tuple that belongs to at least one of two union-compatible relations.

$$
R\cup S=\{t\mid t\in R\lor t\in S\}
$$

## Union compatibility

The operands must have:

- the same arity;
- compatible corresponding domains or SQL types;
- aligned attribute meanings, with renaming when necessary.

Under classical set semantics, a tuple appearing in both inputs occurs once in the result.

## Example

If `Employee` and `Director` share schema `(Code, Name, Age)`, `Employee ∪ Director` contains everyone appearing in either relation. A person represented by the same complete tuple in both relations appears once.

## Properties

Union is:

- commutative: $R\cup S=S\cup R$;
- associative: $(R\cup S)\cup T=R\cup(S\cup T)$;
- idempotent: $R\cup R=R$.

## SQL

```sql
SELECT code, name, age FROM Employee
UNION
SELECT code, name, age FROM Director;
```

`UNION` removes duplicates; `UNION ALL` preserves them and follows bag semantics. See [[Set Semantics vs Bag Semantics]].

> [!warning]
> Equal arity is not enough conceptually. Combining `Employee(age, salary)` with `Building(floors, cost)` may be type-compatible but semantically meaningless.

## Related notes

- [[Difference in Relational Algebra]]
- [[Intersection in Relational Algebra]]
- [[Set Semantics vs Bag Semantics]]

