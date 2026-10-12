---
title: DDL e DML
tags:
  - basi-di-dati
  - concetto
  - sql
---

# DDL e DML

> [!summary] In breve
> Il DDL definisce lo schema (create, alter, drop); il DML manipola i dati (select, insert, delete, update).

| DDL | DML |
|---|---|
| `create schema/table/domain/index/view` | `select` |
| `alter table ... add/drop` | `insert into ... values / select` |
| `drop table ... restrict/cascade` | `delete from ... [where]` (senza where = tutto) |
| | `update ... set ... [where]` |

`insert` senza lista di attributi segue l'ordine della `create table`; gli attributi omessi ricevono il default o NULL.

## Collegamenti

- **Concetti correlati**: [[SQL]] · [[Create Table]] · [[Select SQL]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Linguaggi per basi di dati|Lezione 2 — Linguaggi per basi di dati]]
> - [[03 - BD - SQL#3.3 Manipolazione dei dati|Lezione 3 — 3.3 Manipolazione dei dati]]
> - [[03 - BD - SQL#Modifiche degli schemi, alter table|Lezione 3 — Modifiche degli schemi, alter table]]
