---
title: Allocazione nella memoria heap
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - jvm
  - memoria
---

# Allocazione nella memoria heap

> [!summary] In breve
> Gli oggetti creati con `new` vanno nella memoria heap; la memoria libera è tenuta in una free list di buchi, e la politica di scelta (best/first/next/worst-fit) influenza la frammentazione esterna.

| Politica | Scelta | Effetto |
|---|---|---|
| best-fit | buco più vicino alla richiesta | lascia avanzi minuscoli: frammentazione peggiore |
| first-fit | primo buco sufficiente | veloce, frammenta l'inizio della lista |
| next-fit | primo sufficiente dall'ultima posizione | frammentazione distribuita |
| worst-fit | buco più grande | avanzi grandi |

- **Frammentazione interna**: spazio inutilizzato dentro un blocco assegnato.
- **Frammentazione esterna**: memoria libera sparsa tra blocchi in uso.
- Pila e heap crescono una verso l'altra nella memoria della JVM. Vedi anche [[Frammentazione]] e [[Allocazione Contigua]] (SO).

## Collegamenti

- **Concetti correlati**: [[Garbage collection mark-sweep]] · [[Pila dei metodi di Java]] · [[Frammentazione]] · [[Allocazione Contigua]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Riservare spazio nella memoria heap|Lezione 15 — Riservare spazio nella memoria heap]]
