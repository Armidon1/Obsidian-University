---
title: Entità vs Attributo vs Relazione
tags:
  - basi-di-dati
  - concetto
  - modello-er
  - progettazione-concettuale
---

# Entità vs Attributo vs Relazione

> [!summary] In breve
> Criteri pragmatici per scegliere il costrutto: entità se ha esistenza autonoma e proprietà proprie, attributo se è una proprietà locale, relazione se è una tupla di altri oggetti.

| Il concetto… | Costrutto |
|---|---|
| ha proprietà e esistenza autonoma | entità |
| è proprietà locale senza proprietà | attributo |
| correla altri concetti | relazione |
| è un caso particolare | ISA / generalizzazione |

- Errore tipico: `Città` come attributo perde il legame con l'entità Città.
- Le scelte possono cambiare in analisi (se interessa la regione, Città diventa entità).

## Collegamenti

- **Concetti correlati**: [[Entità ER]] · [[Relazione ER]] · [[Metodologia di Progettazione Concettuale]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Scelta tra entità e attributo|Lezione 5 — Scelta tra entità e attributo]]
> - [[05 - BD - Progettazione Concettuale#Scelta tra entità e relazione|Lezione 5 — Scelta tra entità e relazione]]
> - [[05 - BD - Progettazione Concettuale#Esercizi 7, 8 e 9 — Impiegati, dipartimenti, progetti|Lezione 5 — Esercizi 7, 8 e 9 — Impiegati, dipartimenti, progetti]]
