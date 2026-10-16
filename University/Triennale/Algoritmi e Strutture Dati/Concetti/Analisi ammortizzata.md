---
title: Analisi ammortizzata
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - analisi-ammortizzata
---

# Analisi ammortizzata

> [!summary] In breve
> Si studia il costo totale di una **sequenza** di operazioni invece del caso peggiore di ognuna: le operazioni costose rare vengono "pagate" da quelle economiche frequenti.

**Metodo contabile** (*ciber-dollari*): ogni operazione paga una quota fissa; l'eccesso si accumula in "conti" e paga le operazioni costose. Se i conti non vanno mai in negativo, la quota è un limite ammortizzato.

Esempi nel libro:
- [[Array dinamico]]: 3 ciber-dollari per `add` bastano per i ridimensionamenti → $O(1)$ ammortizzato;
- [[Albero splay]]: $O(\log n)$ ammortizzato per operazione (con il rango $r(w) = \log n(w)$);
- [[Partizione union-find]] su sequenze: ogni elemento si sposta al più $\log n$ volte → $O(k + n\log n)$.

Ammortizzato ≠ medio: è una garanzia sul **totale** nel caso peggiore, senza probabilità.

## Collegamenti

- **Concetti correlati**: [[Array dinamico]] · [[Albero splay]] · [[Partizione union-find]] · [[Analisi del caso peggiore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Analisi ammortizzata degli array dinamici|Lezione 7 — Analisi ammortizzata degli array dinamici]]
