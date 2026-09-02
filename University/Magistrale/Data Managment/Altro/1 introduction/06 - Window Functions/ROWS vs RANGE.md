---
title: "ROWS vs RANGE"
tags: [data-management, sql, window-functions, frames]
source: "[[1-Introduction.pdf]]"
---

# ROWS vs RANGE

> [!definition]
> `ROWS` defines frame boundaries by row positions. `RANGE` defines them through ordering values and peer groups.

Suppose ordered amounts are:

| row | date | amount |
|---:|---|---:|
| 1 | 2025-01-01 | 10 |
| 2 | 2025-01-01 | 20 |
| 3 | 2025-01-02 | 30 |

## `ROWS`

```sql
SUM(amount) OVER (
    ORDER BY date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

Processes physical row positions. The two rows sharing a date can receive successive totals, although their internal order is unstable unless another ordering key is added.

## `RANGE`

```sql
SUM(amount) OVER (
    ORDER BY date
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

`CURRENT ROW` includes peers with the same ordering value. Both `2025-01-01` rows can therefore receive the combined total 30.

## Practical rule

For a row-by-row running total, prefer:

```sql
ORDER BY date, transaction_id
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

Use `RANGE` when equal ordering values should intentionally move together as one logical level.

## DBMS details

Supported `RANGE` offsets and data types vary. Always check the target DBMS when using value-based preceding or following offsets.

## Related notes

- [[Window Frames]]
- [[Window ORDER BY]]
- [[Running Totals]]

