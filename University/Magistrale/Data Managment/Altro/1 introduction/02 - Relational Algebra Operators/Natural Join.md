---
title: "Natural Join"
tags: [data-management, relational-algebra, join]
source: "[[1-Introduction.pdf]]"
---

# Natural Join

> [!definition]
> A natural join matches tuples on every attribute name shared by the two input schemas and keeps one copy of each common attribute.

If $A_1,\ldots,A_k$ are common to $R$ and $S$:

$$
R\bowtie S=\pi_{\text{all attributes, one copy of each }A_i}(\sigma_{R.A_1=S.A_1\land\cdots\land R.A_k=S.A_k}(R\times S))
$$

## Example

`Enrolls(student, course, term)` and `Teaches(faculty, course, term)` share `course` and `term`. Their natural join matches on both and produces `(student, course, term, faculty)`.

## SQL

```sql
SELECT *
FROM Enrolls
NATURAL JOIN Teaches;
```

An explicit alternative is clearer:

```sql
SELECT e.student, e.course, e.term, t.faculty
FROM Enrolls AS e
JOIN Teaches AS t
  ON e.course = t.course
 AND e.term = t.term;
```

## Schema sensitivity

If both tables later gain an unrelated column called `status`, the natural join silently starts matching on it as well. This can remove valid rows and change query meaning.

> [!warning]
> Natural join is concise for formal reasoning but can be fragile in evolving production schemas. Prefer explicit join conditions when long-term clarity matters.

## Related notes

- [[Equijoin]]
- [[Theta Join]]
- [[SQL Aliases and Attribute Qualification]]

