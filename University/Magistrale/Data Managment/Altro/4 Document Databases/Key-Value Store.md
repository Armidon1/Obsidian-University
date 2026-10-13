---
title: Key-Value Store
tags:
  - data-management
  - concept
  - nosql
---

# Key-Value Store

> [!summary] In short
> Aggregate store where the value is an **opaque blob** accessed only by **primary key**: a large distributed hash map.

- Very fast lookups; the application must interpret the value.
- Some add structure: Redis (lists, sets), Riak (buckets).
- Tools: Riak, Redis, Memcached DB, Berkeley DB, Amazon DynamoDB, Project Voldemort.

## Links

- **Related concepts**: [[Aggregate Data Model]] · [[Document Database]] · [[Column-Family Store]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Key-value data model|Lecture 4 — Key-value data model]]
> - [[04 - DM - Document Databases#Key-value vs document databases|Lecture 4 — Key-value vs document databases]]
