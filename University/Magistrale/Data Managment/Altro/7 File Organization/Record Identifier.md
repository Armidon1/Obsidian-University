---
title: Record Identifier
aliases:
  - RID
  - Slotted page
tags:
  - data-management
  - concept
  - file-organization
  - storage
---

# Record Identifier

> [!summary] In short
> A record is identified by $rid=\langle page\ id, slot\ number\rangle$; a slot directory at the end of the page maps slots to offsets so records can move inside the page without changing their rid.

- Fixed-length records: **packed** (deletion moves records → rids change) or **unpacked** with a bit array.
- Variable-length records: slot directory; deleted slot = −1; moving to another page leaves a forwarding address $(j,h)$.
- Field formats: separators or **offset array** (direct access, NULL = two equal offsets).
- Records larger than a page are **spanned** (fragments), BLOBs occupy page sequences.

## Links

- **Related concepts**: [[Heap File]] · [[Database Index]]
- **Base triennale (Basi di Dati)**: [[Valore Nullo]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Pages and records|Lecture 7 — Pages and records]]
> - [[07 - DM - File Organization and Indexing#Pages with variable-length records|Lecture 7 — Pages with variable-length records]]
> - [[07 - DM - File Organization and Indexing#Format of records|Lecture 7 — Format of records]]
