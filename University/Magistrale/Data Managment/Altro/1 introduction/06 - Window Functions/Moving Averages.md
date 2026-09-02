---
title: "Moving Averages"
tags: [data-management, sql, window-functions, analytics]
source: "[[1-Introduction.pdf]]"
---

# Moving Averages

> [!definition]
> A moving average calculates an average over a frame that moves with the current row.

## Last three rows

```sql
SELECT sale_time,
       sale_id,
       amount,
       AVG(amount) OVER (
           ORDER BY sale_time, sale_id
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS moving_average_3_rows
FROM Sale;
```

The frame contains the current row and at most two previous rows.

## Beginning of the partition

The first row is averaged over one value and the second over two values. SQL does not wait until the frame is "full". If a full three-row window is required, combine the average with:

```sql
COUNT(*) OVER (
    ORDER BY sale_time, sale_id
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

and filter from an outer query when the count is 3.

## Row-based versus time-based windows

`ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` means seven observations, not seven days. If observation frequency varies, a value-based time interval may be more appropriate, using a supported `RANGE` interval frame or a self-join.

## Partitioned moving average

```sql
AVG(amount) OVER (
    PARTITION BY product_id
    ORDER BY sale_time, sale_id
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

restarts independently for each product.

## Related notes

- [[Window Frames]]
- [[ROWS vs RANGE]]
- [[Running Totals]]

