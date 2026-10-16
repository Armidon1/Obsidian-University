---
title: Lista doppiamente concatenata
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - strutture-dati
---

# Lista doppiamente concatenata

> [!summary] In breve
> Ogni nodo ha riferimenti al precedente e al successivo; con le sentinelle `header` e `trailer` inserimenti e rimozioni in qualunque punto noto costano $O(1)$.

```text
header ⇄ [A] ⇄ [B] ⇄ [C] ⇄ trailer
```

- Le **sentinelle** (nodi senza elemento) eliminano i casi speciali per lista vuota, testa e coda.
- `addBetween(e, pred, succ)` e `remove(node)` sono $O(1)$.
- Base di [[Coda doppia (deque)|deque]] e [[Lista posizionale|liste posizionali]].

## Collegamenti

- **Concetti correlati**: [[Lista semplicemente concatenata]] · [[Lista posizionale]] · [[Coda doppia (deque)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Liste doppiamente concatenate|Lezione 3 — Liste doppiamente concatenate]]
