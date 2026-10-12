---
title: Selezione e Proiezione
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
---

# Selezione e Proiezione

> [!summary] In breve
> La selezione tiene le righe che soddisfano una condizione (decomposizione orizzontale), la proiezione tiene alcune colonne (decomposizione verticale).

$$\text{PROJ}_{\text{Matricola}, \text{Cognome}}(\text{SEL}_{\text{Stipendio} > 50}(\text{Impiegato}))$$

- La selezione mantiene lo schema; la condizione può confrontare due attributi.
- La proiezione ha **al più** tante tuple quante l'operando (duplicati eliminati); esattamente tante se proietta su una superchiave.
- In SQL: `select lista from R where cond` (con `distinct` per eliminare i duplicati).

## Collegamenti

- **Concetti correlati**: [[Algebra Relazionale]] · [[Select SQL]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Selezione|Lezione 2 — Selezione]]
> - [[02 - BD - Modello Relazionale#Proiezione|Lezione 2 — Proiezione]]
> - [[03 - BD - SQL#Proiezione e duplicati|Lezione 3 — Proiezione e duplicati]]
