---
title: "WHERE vs HAVING"
tags: [data-management, sql, grouping, filtering]
source: "[[1-Introduction.pdf]]"
---

# WHERE vs HAVING

> [!definition]
> `WHERE` filters detail rows before grouping. `HAVING` filters completed groups after aggregation.

| `WHERE` | `HAVING` |
|---|---|
| Operates on input rows | Operates on groups |
| Evaluated before `GROUP BY` | Evaluated after grouping |
| Determines which rows contribute | Determines which summaries survive |
| Normally cannot use group aggregates | Commonly uses aggregate expressions |

## Combined example

Find fathers whose children younger than 30 have an average income above 20:

```sql
SELECT f.father, AVG(p.income) AS average_income
FROM Person AS p
JOIN Paternity AS f
  ON f.child = p.name
WHERE p.age < 30
GROUP BY f.father
HAVING AVG(p.income) > 20;
```

Interpretation:

1. `WHERE` removes children aged 30 or above.
2. Remaining children are grouped by father.
3. `AVG` is computed inside each group.
4. `HAVING` removes groups whose average is not above 20.

## Performance and meaning

A non-aggregate condition that logically belongs to individual rows should usually be in `WHERE`. This reduces rows before grouping and states the intended semantics directly.

## Common mistake

Moving `age < 30` into `HAVING` does not simply delay the same filter. It is either invalid, because `age` has several group values, or it asks a different group-level question.

## Related notes

- [[GROUP BY]]
- [[Logical Order of SQL Query Evaluation]]
- [[SQL Query Granularity]]

