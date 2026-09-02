---
title: "Universal Quantification in Databases"
tags: [data-management, query-patterns, sql, logic]
source: "[[1-Introduction.pdf]]"
---

# Universal Quantification in Databases

> [!definition]
> A universal query requires a property to hold for **every** relevant object.

SQL has no general `FOR ALL` clause, so universal conditions are commonly rewritten through double negation:

$$
\forall x\;P(x)\equiv\neg\exists x\;\neg P(x)
$$

In words:

> Every school is good if there does not exist a bad school.

## Example

Find cities where every school has at least one student who graduated with 100:

```sql
SELECT DISTINCT candidate.city
FROM School AS candidate
WHERE NOT EXISTS (
    SELECT 1
    FROM School AS s
    WHERE s.city = candidate.city
      AND NOT EXISTS (
          SELECT 1
          FROM Graduated AS g
          WHERE g.school = s.scode
            AND g.mark = 100
      )
);
```

Read from the inside outward:

1. look for a qualifying graduate for one school;
2. identify a school for which no such graduate exists;
3. retain cities for which no bad school exists.

## Relational algebra pattern

1. Compute all candidates.
2. Compute elements violating the property.
3. Map violations back to candidate groups.
4. Subtract bad groups from all groups.

This uses [[Difference in Relational Algebra]] and the absence pattern from [[Queries Expressing Absence]].

## Vacuous truth

A universal statement over an empty set is logically true. Database questions often define candidates through an existing relation, such as `School`, so only cities with at least one school are considered. Always decide whether empty groups should count.

## Related notes

- [[Existential Queries in Databases]]
- [[Queries Expressing Absence]]
- [[Relational Calculus]]

