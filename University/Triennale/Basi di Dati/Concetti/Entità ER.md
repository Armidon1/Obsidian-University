---
title: Entità ER
tags:
  - basi-di-dati
  - concetto
  - modello-er
---

# Entità ER

> [!summary] In breve
> Classe di oggetti di interesse con esistenza autonoma e proprietà comuni; i suoi attributi sono funzioni totali (salvo cardinalità diverse).

- Istanza di entità = l'**oggetto** stesso (object identifier), non un valore.
- Attributo: proprietà **locale**, funzione totale $A : \text{istanze}(I,E) \to D$.
- Cardinalità sugli attributi: (0,1) opzionale, (x,n) multivalore; senza indicazione (1,1).
- Attributo **composto**: dominio di tipo record.
- Stesso nome di attributo su più entità = un'unica funzione.

## Collegamenti

- **Concetti correlati**: [[Relazione ER]] · [[Identificatore ER]] · [[Entità vs Attributo vs Relazione]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Entità|Lezione 5 — Entità]]
> - [[05 - BD - Progettazione Concettuale#Attributi di entità|Lezione 5 — Attributi di entità]]
> - [[05 - BD - Progettazione Concettuale#Vincoli di cardinalità sugli attributi|Lezione 5 — Vincoli di cardinalità sugli attributi]]
