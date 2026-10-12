---
title: Identificatore ER
tags:
  - basi-di-dati
  - concetto
  - modello-er
  - vincoli
---

# Identificatore ER

> [!summary] In breve
> Insieme di attributi (1,1) e/o ruoli (1,1) che distingue le istanze di un'entità (interno o esterno) o di una relazione; essenziale se minimale.

- **Interno**: pallino annerito o linea che unisce gli attributi.
- **Esterno**: include ruoli di relazioni → entità **debole** (Studente: Matricola + Università).
- Ogni relazione ha l'identificatore **implicito** (tutti i ruoli), non indicato.
- Derivati: un ruolo con massima 1 identifica la relazione; un ruolo che identifica l'entità implica che gli altri ruoli identificano la relazione.
- Nella progettazione logica uno diventa l'[[Identificatore Principale]].

## Collegamenti

- **Concetti correlati**: [[Superchiave e Chiave]] · [[Identificatore Principale]] · [[Vincoli di Cardinalità]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Vincoli di identificazione di entità|Lezione 5 — Vincoli di identificazione di entità]]
> - [[05 - BD - Progettazione Concettuale#Vincoli di identificazione di relazione|Lezione 5 — Vincoli di identificazione di relazione]]
> - [[05 - BD - Progettazione Concettuale#Vincoli derivati di identificazione di relazione|Lezione 5 — Vincoli derivati di identificazione di relazione]]
