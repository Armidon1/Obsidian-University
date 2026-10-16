---
title: Albero binario
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
---

# Albero binario

> [!summary] In breve
> Albero ordinato in cui ogni nodo ha al più due figli, detti sinistro e destro; è **proprio** se ogni nodo interno ne ha esattamente due.

- Definizione ricorsiva: vuoto, oppure radice con sottoalbero sinistro e destro (binari).
- Metodi aggiuntivi: `left(p)`, `right(p)`, `sibling(p)`.
- Esempi: **alberi di decisione** (domande sì/no), **alberi di espressione** (operatori nei nodi interni, operandi nelle foglie).
- Implementazioni: [[Albero binario su array|su array]] o concatenata (`LinkedBinaryTree`: nodo con elemento, genitore, sinistro, destro; tutte le operazioni $O(1)$).

## Collegamenti

- **Concetti correlati**: [[Proprietà degli alberi binari]] · [[Albero binario su array]] · [[Albero di ricerca binario]] · [[Attraversamenti di un albero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Alberi binari|Lezione 8 — Alberi binari]]
