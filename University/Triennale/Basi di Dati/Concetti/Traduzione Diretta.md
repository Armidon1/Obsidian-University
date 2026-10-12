---
title: Traduzione Diretta
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Traduzione Diretta

> [!summary] In breve
> Procedura quasi automatica che traduce lo schema ER ristrutturato in tabelle: ogni entità e ogni ER-relazione non accorpata diventa una relazione, con chiavi, foreign key e inclusioni.

- **Entità** → relazione con i suoi attributi (`*` se (0,1)); le ER-relazioni del suo identificatore principale esterno vengono **accorpate**.
- **ER-relazione** non accorpata → relazione con le chiavi delle entità (nome del ruolo) + attributi; foreign key di ruolo.
- Cardinalità minima 1 → **inclusione** (foreign key se verso una chiave); massima 1 → **chiave**.
- Identificatore esterno non principale → vincolo **di join**.

```
Partecipa(Cognome, DataN, Progetto, OreSett)
    foreign key: Partecipa[Cognome,DataN] ⊆ Impiegato[Cognome,DataN]
```

## Collegamenti

- **Concetti correlati**: [[Ristrutturazione dello Schema ER]] · [[Foreign Key]] · [[Ristrutturazione dello Schema Logico]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#6.3 Traduzione diretta nel modello relazionale|Lezione 6 — 6.3 Traduzione diretta nel modello relazionale]]
> - [[06 - BD - Progettazione Logica#(1) Traduzione delle entità|Lezione 6 — (1) Traduzione delle entità]]
> - [[06 - BD - Progettazione Logica#(2) Traduzione delle ER-relazioni|Lezione 6 — (2) Traduzione delle ER-relazioni]]
> - [[06 - BD - Progettazione Logica#(3) e (4) Vincoli e carico applicativo|Lezione 6 — (3) e (4) Vincoli e carico applicativo]]
