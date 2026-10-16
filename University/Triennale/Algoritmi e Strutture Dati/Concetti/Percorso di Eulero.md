---
title: Percorso di Eulero
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
  - algoritmi
  - design-pattern
---

# Percorso di Eulero

> [!summary] In breve
> Il percorso di Eulero gira attorno all'albero visitando ogni nodo "da sinistra" (prima dei figli), "da sotto" (tra i figli, binari) e "da destra" (dopo): unifica pre-ordine, simmetrico e post-ordine in $O(n)$.

- Si implementa con lo [[Schema template method|schema template method]]: un metodo generico chiama gli hook `previsit`, `invisit`, `postvisit`.
- Esempi: stampa con parentesi di un'espressione, calcolo del valore di un'espressione, disegno di un albero (coordinate $x$ = ordine simmetrico, $y$ = profondità).

## Collegamenti

- **Concetti correlati**: [[Attraversamenti di un albero]] · [[Schema template method]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Percorso di Eulero|Lezione 8 — Percorso di Eulero]]
