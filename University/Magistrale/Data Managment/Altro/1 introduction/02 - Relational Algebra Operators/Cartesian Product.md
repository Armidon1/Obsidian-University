---
title: "Cartesian Product"
tags: [data-management, relational-algebra, operator]
source: "[[1-Introduction.pdf]]"
---

# Cartesian Product

> [!definition]
> The Cartesian product combines every tuple of one relation with every tuple of another relation.

For an $m$-ary relation $R$ and an $n$-ary relation $S$:

$$
R\times S=\{(a_1,\ldots,a_m,b_1,\ldots,b_n)\mid (a_1,\ldots,a_m)\in R\land(b_1,\ldots,b_n)\in S\}
$$

The result has arity $m+n$ and cardinality:

$$
|R\times S|=|R|\cdot|S|
$$

## Example

If `Employee` contains three rows and `Department` contains two rows, their product contains six rows. Each employee is paired with each department, including pairs that are not logically related.

## Role in joins

The product provides candidate pairs. A [[Theta Join]] filters those pairs:

$$
R\bowtie_{\Theta}S=\sigma_{\Theta}(R\times S)
$$

This equation defines join semantics, but a DBMS does not need to materialize the full product. It can use a hash join, merge join, or nested-loop algorithm to generate only useful matches.

## Attribute ambiguity

If both relations contain an attribute called `code`, qualify it as `R.code` and `S.code`, or use [[Renaming in Relational Algebra]]. Without disambiguation, later conditions and projections may be unclear.

## Common mistake

An accidental Cartesian product in SQL occurs when tables are combined without a correct join condition:

```sql
SELECT *
FROM Employee, Department;
```

Modern SQL makes intentional products explicit with `CROSS JOIN`.

## Related notes

- [[Theta Join]]
- [[Equijoin]]
- [[Natural Join]]

