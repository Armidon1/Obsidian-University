---
title: Attraversamenti di un albero
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
  - algoritmi
---

# Attraversamenti di un albero

> [!summary] In breve
> Un attraversamento visita tutti i nodi: in pre-ordine (prima il nodo, poi i figli), post-ordine (prima i figli), in ampiezza (per livelli, con una coda) e, per gli alberi binari, in ordine simmetrico (sinistro, nodo, destro).

| Visita | Ordine | Uso tipico |
|---|---|---|
| pre-ordine | nodo, figli | indice di un documento |
| post-ordine | figli, nodo | spazio su disco di una cartella, valutazione di espressioni |
| ampiezza (BFS) | livello per livello, con una [[Coda (ADT)|coda]] | giochi, alberi di decisione |
| simmetrico (inorder) | sinistro, nodo, destro | chiavi in ordine in un [[Albero di ricerca binario|BST]], stampa di espressioni |

Tutte $O(n)$. Generalizzazione: il [[Percorso di Eulero|percorso di Eulero]].

## Collegamenti

- **Concetti correlati**: [[Percorso di Eulero]] · [[Albero (ADT)]] · [[Attraversamento in ampiezza (BFS)]] · [[Iteratore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Algoritmi di attraversamento di alberi|Lezione 8 — Algoritmi di attraversamento di alberi]]
