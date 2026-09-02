---
title: "Running Totals"
tags: [data-management, sql, window-functions, analytics]
source: "[[1-Introduction.pdf]]"
---

# Running Totals

> [!definition]
> A running total is the sum from the beginning of an ordered partition through the current row.

```sql
SELECT account_id,
       transaction_time,
       transaction_id,
       amount,
       SUM(amount) OVER (
           PARTITION BY account_id
           ORDER BY transaction_time, transaction_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM Transaction;
```

## Components

- `PARTITION BY account_id` restarts the balance for each account.
- `ORDER BY transaction_time, transaction_id` defines transaction sequence.
- The `ROWS` frame includes all earlier rows and the current row.

## Why the tie-breaker matters

Timestamps may repeat. Without `transaction_id`, equal-time rows have no deterministic internal order. A row-by-row cumulative total can then be unstable.

## `ROWS` versus `RANGE`

With `RANGE ... CURRENT ROW`, all peers sharing the current ordering value may be included together. This can make the total jump by several rows. See [[ROWS vs RANGE]].

## Starting balance

```sql
opening_balance +
SUM(amount) OVER (...) AS balance_after_transaction
```

If `opening_balance` is stored once per account, ensure a join does not accidentally duplicate it before the window calculation.

## Reverse total

For a remaining total from the current row to partition end:

```sql
SUM(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
)
```

## Related notes

- [[Aggregate Window Functions]]
- [[Window Frames]]
- [[Moving Averages]]

