---
title: Metodo greedy
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - progettazione-algoritmi
  - greedy
---

# Metodo greedy

> [!summary] In breve
> Schema per problemi di ottimizzazione: a ogni passo si fa la scelta localmente migliore senza tornare indietro; dà l'ottimo se il problema ha la proprietà di scelta greedy.

- Non sempre ottimo (es. il resto con monete di taglio strano), ma lo è in molti casi classici:

| Problema | Algoritmo greedy | Scelta locale |
|---|---|---|
| compressione | [[Codifica di Huffman|Huffman]] | fondi i due alberi meno frequenti |
| percorsi minimi | [[Algoritmo di Dijkstra|Dijkstra]] | vertice esterno più vicino |
| MST | [[Algoritmo di Prim-Jarník|Prim-Jarník]], [[Algoritmo di Kruskal|Kruskal]] | lato più leggero sicuro |

La correttezza va dimostrata (es. con la proprietà del taglio per gli MST).

## Collegamenti

- **Concetti correlati**: [[Codifica di Huffman]] · [[Algoritmo di Dijkstra]] · [[Albero ricoprente minimo (MST)]] · [[Programmazione dinamica]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Il metodo greedy|Lezione 13 — Il metodo greedy]]
