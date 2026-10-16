---
title: Garbage collection mark-sweep
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - jvm
  - memoria
  - grafi
---

# Garbage collection mark-sweep

> [!summary] In breve
> La garbage collection libera gli oggetti non più raggiungibili dalle radici (variabili nelle pile dei thread): la fase mark li marca con un DFS sul grafo dei riferimenti, la fase sweep libera i non marcati.

1. Si sospende l'esecuzione e si azzerano i bit di marcatura.
2. **Mark**: DFS orientato da ogni oggetto radice; si marcano gli oggetti **vivi**.
3. **Sweep**: si scandisce lo heap, si liberano i non marcati e si può compattare la memoria.

- Tempo: proporzionale agli oggetti vivi e ai loro riferimenti + dimensione dello heap.
- Il DFS va fatto **sul posto** (memoria scarsa): si invertono temporaneamente i riferimenti per ricordare il cammino di ritorno, ripristinandoli al ritorno.

## Collegamenti

- **Concetti correlati**: [[Attraversamento in profondità (DFS)]] · [[Allocazione nella memoria heap]] · [[Pila dei metodi di Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Garbage collection|Lezione 15 — Garbage collection]]
