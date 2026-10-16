---
title: Ordinamento per inserimento
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - array
---

# Ordinamento per inserimento

> [!summary] In breve
> Insertion-sort inserisce ogni elemento al suo posto nella parte già ordinata spostando a destra i maggiori: $O(n^2)$ nel caso peggiore, $O(n + m)$ con $m$ inversioni, ottimo per input piccoli o quasi ordinati.

```java
for (int k = 1; k < n; k++) {
  char cur = data[k];
  int j = k;
  while (j > 0 && data[j-1] > cur) { data[j] = data[j-1]; j--; }
  data[j] = cur;
}
```

| Caso | Tempo |
|---|---|
| già ordinato | $O(n)$ |
| ordinato al contrario | $O(n^2)$ |
| generale | $O(n + m)$, $m$ = numero di inversioni |

Stabile e sul posto; usato negli ordinamenti ibridi sotto una soglia (circa 50 elementi).

## Collegamenti

- **Concetti correlati**: [[Quick-sort]] · [[Merge-sort]] · [[Ordinamento stabile]] · [[Ordinamento con coda prioritaria]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Ordinare un array|Lezione 3 — Ordinare un array]]
