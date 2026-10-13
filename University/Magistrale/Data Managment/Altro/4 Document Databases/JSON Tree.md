---
title: JSON Tree
tags:
  - data-management
  - concept
  - json
  - data-models
---

# JSON Tree

> [!summary] In short
> The tree representation $\varphi$ of a JSON value: objects become nodes with **key-labeled** edges, arrays nodes with **position-labeled** edges, atomic values leaves.

- JSON values: numbers, strings, `true`/`false`, `null`, objects $\{s_1:v_1,\ldots,s_n:v_n\}$ with **distinct keys**, arrays $[v_1,\ldots,v_n]$.
- $\varphi(\{s_1:v_1,\ldots\})$: root with edges $s_i$ to $\varphi(v_i)$; $\varphi([v_1,\ldots])$: root with edges $i$ to $\varphi(v_i)$.
- Example: `{"name": {"first": "John"}, "hobbies": ["yoga"]}` → paths `name.first` → "John", `hobbies.1` → "yoga" (MongoDB dot notation).

## Links

- **Related concepts**: [[Document Database]] · [[BSON]]
- **Base triennale (Basi di Dati)**: [[JSON]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#JSON formalization (simplified)|Lecture 4 — JSON formalization (simplified)]]
> - [[04 - DM - Document Databases#JSON trees|Lecture 4 — JSON trees]]
