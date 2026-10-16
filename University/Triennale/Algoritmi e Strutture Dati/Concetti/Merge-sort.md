---
title: Merge-sort
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - dividi-e-conquista
---

# Merge-sort

> [!summary] In breve
> Merge-sort divide la sequenza a metà, ordina ricorsivamente le due metà e le fonde: $O(n\log n)$ in ogni caso, stabile se la fusione preferisce la prima metà a parità, ma non sul posto.

```java
public static <K> void mergeSort(K[] S, Comparator<K> comp) {
  int n = S.length;
  if (n < 2) return;
  int mid = n / 2;
  K[] S1 = Arrays.copyOfRange(S, 0, mid);
  K[] S2 = Arrays.copyOfRange(S, mid, n);
  mergeSort(S1, comp);
  mergeSort(S2, comp);
  merge(S1, S2, S, comp);            // O(n1 + n2)
}
```

- Albero di ricorsione di altezza $\lceil \log n \rceil$, costo $O(n)$ per livello.
- $t(n) = 2t(n/2) + cn = O(n\log n)$.
- Varianti: su code/liste concatenate, **bottom-up** non ricorsiva (fusioni di blocchi lunghi 1, 2, 4, … con un array ausiliario), [[Merge-sort a più vie|a più vie]] per la memoria esterna.

## Collegamenti

- **Concetti correlati**: [[Dividi-e-conquista]] · [[Equazione di ricorrenza]] · [[Quick-sort]] · [[Merge-sort a più vie]] · [[Ordinamento stabile]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Ordinamento mediante la strategia dividi-e-conquista|Lezione 12 — Ordinamento mediante la strategia dividi-e-conquista]]
