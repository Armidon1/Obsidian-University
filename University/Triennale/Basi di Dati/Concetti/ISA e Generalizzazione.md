---
title: ISA e Generalizzazione
tags:
  - basi-di-dati
  - concetto
  - modello-er
---

# ISA e Generalizzazione

> [!summary] In breve
> ISA dice che una sottoentità è un sottoinsieme dell'entità padre ed eredita le sue proprietà; una generalizzazione divide il padre in sottoentità disgiunte, completa se le coprono tutte.

- ISA: $\text{istanze}(E_1) \subseteq \text{istanze}(E_2)$, riflessiva e transitiva; **un solo padre** per entità.
- Generalizzazione: figlie disgiunte; **completa** (freccia annerita) se ne sono una partizione.
- Ereditarietà di attributi, relazioni e cardinalità.
- Entità **disgiunte**: discendenti di figlie diverse di una generalizzazione (le radici sono figlie di TOP).
- ISA tra relazioni: stessi ruoli e entità in ISA ruolo per ruolo.

## Collegamenti

- **Concetti correlati**: [[Entità ER]] · [[Eliminazione delle ISA]] · [[Vincoli di Cardinalità]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[RDFS Knowledge Graph]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#La relazione ISA tra entità|Lezione 5 — La relazione ISA tra entità]]
> - [[05 - BD - Progettazione Concettuale#Generalizzazioni|Lezione 5 — Generalizzazioni]]
> - [[05 - BD - Progettazione Concettuale#Grafo delle gerarchie ed entità disgiunte|Lezione 5 — Grafo delle gerarchie ed entità disgiunte]]
> - [[05 - BD - Progettazione Concettuale#ISA e generalizzazioni tra relazioni|Lezione 5 — ISA e generalizzazioni tra relazioni]]
