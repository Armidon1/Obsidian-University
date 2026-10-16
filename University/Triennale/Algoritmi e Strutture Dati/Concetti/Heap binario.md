---
title: Heap binario
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code-prioritarie
  - alberi
---

# Heap binario

> [!summary] In breve
> Un heap è un albero binario **completo** in cui ogni nodo ha chiave non minore di quella del genitore: il minimo è in radice e inserimenti/estrazioni costano $O(\log n)$.

- **Proprietà di ordinamento** (heap-order): $\text{key}(p) \ge \text{key}(\text{parent}(p))$.
- **Albero binario completo**: livelli pieni tranne l'ultimo, riempito da sinistra → altezza $\lfloor \log n \rfloor$.
- `insert`: si aggiunge nell'ultima posizione e si fa **up-heap** (scambi con il genitore finché serve).
- `removeMin`: si sposta l'ultimo elemento in radice e si fa **down-heap** (scambi con il figlio minore).
- Si memorizza in un [[Albero binario su array|array]]: figli di $j$ in $2j+1$, $2j+2$.

Da non confondere con la [[Allocazione nella memoria heap|memoria heap]].

## Collegamenti

- **Concetti correlati**: [[Coda prioritaria (ADT)]] · [[Costruzione bottom-up di uno heap]] · [[Heap sort]] · [[Albero binario su array]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Heap|Lezione 9 — Heap]]
