---
title: "Difference in Relational Algebra"
tags: [data-management, relational-algebra, operator, negation]
source: "[[1-Introduction.pdf]]"
---

# Difference in Relational Algebra

> [!definition]
> Difference returns tuples in the first relation that do not occur in the second relation.

$$
R-S=\{t\mid t\in R\land t\notin S\}
$$

The operands must be union-compatible.

## Direction matters

Difference is not commutative:

$$
R-S\neq S-R
$$

If an employee is not a director, that tuple belongs to `Employee - Director`. A director who is not an employee represented in the first relation belongs to the reverse difference.

## Negation pattern

Difference is central to queries containing "no", "not", or "without":

$$
AllCandidates - CandidatesWithForbiddenWitness
$$

Example: schools where no student graduated with 100:

$$
\pi_{scode}(School)-\rho_{scode\leftarrow school}(\pi_{school}(\sigma_{mark=100}(Graduated)))
$$

This includes schools with no graduates, because they are in the candidate set but not in the forbidden set.

## SQL counterparts

SQL may express difference using:

- `EXCEPT`;
- `NOT EXISTS`;
- an anti-join pattern;
- sometimes `NOT IN`, with care around `NULL`.

See [[Queries Expressing Absence]] and [[NULL and Three-Valued Logic]].

## Related notes

- [[Intersection in Relational Algebra]]
- [[Universal Quantification in Databases]]
- [[Queries Expressing Absence]]

