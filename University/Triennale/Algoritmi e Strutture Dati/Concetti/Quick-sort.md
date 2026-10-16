---
title: Quick-sort
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - dividi-e-conquista
---

# Quick-sort

> [!summary] In breve
> Quick-sort sceglie un pivot, divide in minori, uguali e maggiori, e ordina ricorsivamente: $O(n^2)$ nel caso peggiore ma $O(n\log n)$ atteso con pivot casuale; sul posto, non stabile, molto veloce in pratica.

- **Caso peggiore**: pivot sempre estremo (es. ultimo elemento su input già ordinato) → altezza $n - 1$, $O(n^2)$.
- **Pivot casuale**: ogni elemento partecipa in media a $O(\log n)$ confronti → $O(n\log n)$ atteso su **ogni** input.
- **Sul posto**: due indici `left`/`right` scambiano le coppie fuori posto, poi il pivot va nella posizione finale.
- Pratica: **mediana di tre** come pivot, **ibrido** con insertion-sort sotto ~50 elementi, pila esplicita impilando prima il sotto-problema più grande (profondità $O(\log n)$).

## Collegamenti

- **Concetti correlati**: [[Merge-sort]] · [[Dividi-e-conquista]] · [[Quick-select probabilistico]] · [[Ordinamento per inserimento]] · [[Heap sort]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Ordinamento quick-sort|Lezione 12 — Ordinamento quick-sort]]
