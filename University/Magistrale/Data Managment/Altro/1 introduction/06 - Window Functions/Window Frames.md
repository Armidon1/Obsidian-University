---
title: "Window Frames"
tags: [data-management, sql, window-functions, frames]
source: "[[1-Introduction.pdf]]"
---

# Window Frames

> [!definition]
> A window frame selects the portion of an ordered partition that contributes to a framed window calculation for the current row.

## Common boundaries

- `UNBOUNDED PRECEDING` - beginning of the partition;
- `n PRECEDING` - a position or value before the current row;
- `CURRENT ROW`;
- `n FOLLOWING`;
- `UNBOUNDED FOLLOWING` - end of the partition.

## Running frame

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

Includes all ordered rows from partition start through the current row.

## Moving frame

```sql
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
```

Includes at most three rows: the current row and two preceding rows.

## Full-partition frame

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
```

Includes the entire partition even when `ORDER BY` is present.

## Partition versus frame

The partition is the complete independent group. The frame is a current-row-dependent subset inside it. Frames are especially important for aggregate windows; ranking and navigation functions have their own positional semantics.

## Default-frame warning

With a window `ORDER BY`, the default frame may end at the current row or its peer group. Duplicate ordering values can therefore make results appear to jump. Write the frame explicitly when correctness depends on cumulative or moving behavior.

## Related notes

- [[ROWS vs RANGE]]
- [[Running Totals]]
- [[Moving Averages]]

