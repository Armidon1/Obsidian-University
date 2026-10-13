---
title: Reificazione
tags:
  - basi-di-dati
  - concetto
  - progettazione-concettuale
  - modello-er
---

# Reificazione

> [!summary] In breve
> Trasformazione che preserva l'equivalenza trasformando in entità un attributo (semplice, composto o multivalore) o una relazione.

| Caso | Trasformazione |
|---|---|
| a | attributo → relazione verso un'entità-dominio (1,n) |
| b | attributo composto → entità con i campi |
| c1 | relazione → entità con N relazioni binarie (1,1) |
| c2 | relazione → entità (1,1) in una nuova relazione con le N entità |
| d, e | attributo di relazione → relazione/entità |

Le relazioni in ISA con quella reificata vanno trasformate anch'esse. Serve, ad esempio, per contratti ripetuti tra lo stesso giocatore e la stessa squadra.

## Collegamenti

- **Concetti correlati**: [[Relazione ER]] · [[Eventi e Storicizzazione]] · [[Ristrutturazione dello Schema ER]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[RDF Reification]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Trasformazioni dello schema|Lezione 5 — Trasformazioni dello schema]]
> - [[05 - BD - Progettazione Concettuale#Trasformazioni, caso c (relazione in entità)|Lezione 5 — Trasformazioni, caso c (relazione in entità)]]
> - [[06 - BD - Progettazione Logica#Attività 2, attributi multivalore|Lezione 6 — Attività 2, attributi multivalore]]
