---
title: Heap File
tags:
  - data-management
  - concept
  - file-organization
---

# Heap File

> [!summary] In short
> File organization with records in no particular order; cheap insertion and scan, but every search is a full scan.

| Operation | Pages |
|---|---|
| Scan, equality, range | $B$ (equality on key: $B/2$ on average) |
| Insertion | 2 (read + write last page) |
| Deletion by rid | 2 |

- Free space tracked by two linked lists (full / with space) or by a **directory** (search cost linear in the directory size).

## Links

- **Related concepts**: [[Hashed File]] · [[Cost Model for File Organizations]] · [[Record Identifier]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Heap file|Lecture 7 — Heap file]]
> - [[07 - DM - File Organization and Indexing#Heap file costs|Lecture 7 — Heap file costs]]
