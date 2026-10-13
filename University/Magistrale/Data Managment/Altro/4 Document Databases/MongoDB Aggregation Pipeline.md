---
title: MongoDB Aggregation Pipeline
aliases:
  - Aggregation pipeline
tags:
  - data-management
  - concept
  - mongodb
  - query-languages
---

# MongoDB Aggregation Pipeline

> [!summary] In short
> MongoDB computes aggregates with `db.coll.aggregate([stage1, …, stageN])`: each stage (`$match`, `$group`, `$lookup`, …) takes the output of the previous one.

```javascript
db.orders.aggregate([
  { $match: { status: "A" } },                                   // WHERE
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } }    // GROUP BY + SUM
])
db.people.aggregate([{ $lookup: { from: "places", localField: "city",
                                  foreignField: "cityName", as: "city_details" } }])
```

- `$lookup` ≈ left outer join that **nests** matches in an array.

## Links

- **Related concepts**: [[Document Database]] · [[BSON]]
- **Base triennale (Basi di Dati)**: [[Group By e Having]] · [[Join Esterno]] · [[07 - BD - NoSQL#Il join con $lookup|Il join con $lookup]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Aggregation pipeline|Lecture 4 — Aggregation pipeline]]
> - [[04 - DM - Document Databases#Aggregation as a means for joins|Lecture 4 — Aggregation as a means for joins]]
