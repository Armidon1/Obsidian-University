---
title: Chiave Primaria
tags:
  - basi-di-dati
  - concetto
  - vincoli
  - sql
---

# Chiave Primaria

> [!summary] In breve
> La chiave scelta per identificare le tuple, su cui non sono ammessi valori nulli; una sola per relazione, attributi sottolineati.

- $K$ chiave + nessun NULL ⇒ $t_1[K] \neq t_2[K]$ per tuple diverse.
- SQL: `primary key` (implica `not null`); è il progettista a garantire la minimalità.
- Viene dall'**identificatore principale** nella progettazione logica.

## Collegamenti

- **Concetti correlati**: [[Superchiave e Chiave]] · [[Foreign Key]] · [[Identificatore Principale]] · [[Create Table]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Surrogate Key]] · [[Database Index]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Chiave primaria|Lezione 2 — Chiave primaria]]
> - [[03 - BD - SQL#Vincoli in SQL|Lezione 3 — Vincoli in SQL]]
