---
title: Vincoli di Cardinalità
tags:
  - basi-di-dati
  - concetto
  - modello-er
  - vincoli
---

# Vincoli di Cardinalità

> [!summary] In breve
> Coppia (min, max) su un ruolo: ogni istanza dell'entità partecipa almeno min e al più max volte alla relazione in quel ruolo.

| | Significato |
|---|---|
| min 0 / 1 | partecipazione opzionale / obbligatoria |
| max 1 / n | al più una / un numero qualsiasi |
| assente | (0,n) |

- Uno a uno, uno a molti, molti a molti (cardinalità massime).
- Con ISA tra relazioni: la **massima** si propaga dal padre alla figlia, la **minima** dalla figlia al padre; si prende $(\max x_i, \min y_i)$.
- Se dopo la propagazione min > max, l'entità non può avere istanze.
- In logica: min 1 → inclusione/foreign key; max 1 → chiave.

## Collegamenti

- **Concetti correlati**: [[Relazione ER]] · [[Identificatore ER]] · [[Traduzione Diretta]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Vincoli di cardinalità sulle relazioni|Lezione 5 — Vincoli di cardinalità sulle relazioni]]
> - [[05 - BD - Progettazione Concettuale#Cardinalità ed ereditarietà su relazioni|Lezione 5 — Cardinalità ed ereditarietà su relazioni]]
