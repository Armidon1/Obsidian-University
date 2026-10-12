---
title: Identificatore Principale
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Identificatore Principale

> [!summary] In breve
> L'identificatore scelto per ogni entità e relazione, che diventerà la chiave primaria; deve essere essenziale e senza cicli di identificazione esterna.

- Criteri: essenziale, semplice, usato spesso, preferibilmente interno; tra gli esterni quelli da ISA.
- Se manca, si introduce un **codice**.
- **Cicli** nel grafo degli identificatori principali esterni (es. Rettore ↔ Università) vanno spezzati.
- Più identificatori: il principale si indica con un cerchio attorno al pallino.

## Collegamenti

- **Concetti correlati**: [[Identificatore ER]] · [[Chiave Primaria]] · [[Traduzione Diretta]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#Attività 5, identificatori principali|Lezione 6 — Attività 5, identificatori principali]]
