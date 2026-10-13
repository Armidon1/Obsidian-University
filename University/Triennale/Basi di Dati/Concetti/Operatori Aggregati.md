---
title: Operatori Aggregati
tags:
  - basi-di-dati
  - concetto
  - sql
---

# Operatori Aggregati

> [!summary] In breve
> Funzioni che calcolano un valore da un insieme di tuple: count, sum, avg, max, min. Ignorano i NULL e richiedono una target list omogenea.

| Espressione | Conta |
|---|---|
| `count(*)` | le tuple |
| `count(A)` | i valori non nulli di A |
| `count(distinct A)` | i valori distinti non nulli |

- `avg` di 30, NULL, 36, 36 = $102/3 = 34$.
- `select nome, max(reddito)` è **irragionevole** (target list disomogenea).
- Gli aggregati non vanno nella `where`: per il massimo si usa una sottoquery.

## Collegamenti

- **Concetti correlati**: [[Group By e Having]] · [[Valore Nullo]] · [[Select SQL]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[SQL Aggregate Functions]] · [[COUNT in SQL]] · [[SQL Window Functions]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Operatori aggregati|Lezione 3 — Operatori aggregati]]
> - [[03 - BD - SQL#Esercizio 11, annidamento e funzioni|Lezione 3 — Esercizio 11, annidamento e funzioni]]
