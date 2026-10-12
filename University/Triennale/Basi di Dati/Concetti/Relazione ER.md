---
title: Relazione ER
tags:
  - basi-di-dati
  - concetto
  - modello-er
---

# Relazione ER

> [!summary] In breve
> Legame tra due o più entità; le sue istanze sono tuple etichettate e, essendo un insieme, non possono ripetersi sulle stesse istanze di entità.

$$\text{istanze}(I, R) \subseteq \text{istanze}(I, E_1) \times \dots \times \text{istanze}(I, E_n)$$
- Grado = numero di ruoli (binaria, n-aria).
- Gli **attributi di relazione** descrivono il legame ma **non distinguono** istanze: forniture ripetute in date diverse richiedono la [[Reificazione]].
- Non confondere con la relazione (tabella) del modello relazionale.

## Collegamenti

- **Concetti correlati**: [[Entità ER]] · [[Ruolo ER]] · [[Vincoli di Cardinalità]] · [[Reificazione]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Relazioni|Lezione 5 — Relazioni]]
> - [[05 - BD - Progettazione Concettuale#Attributi di relazione|Lezione 5 — Attributi di relazione]]
