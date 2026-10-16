---
title: Ricerca binaria
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
  - ricerca
---

# Ricerca binaria

> [!summary] In breve
> In un array ordinato si confronta il valore cercato con l'elemento centrale e si continua in una sola metà: $O(\log n)$.

```java
public static boolean binarySearch(int[] data, int target, int low, int high) {
  if (low > high) return false;
  int mid = (low + high) / 2;
  if (target == data[mid]) return true;
  else if (target < data[mid]) return binarySearch(data, target, low, mid - 1);
  else return binarySearch(data, target, mid + 1, high);
}
```

Ogni chiamata dimezza l'intervallo: al più $\lfloor \log n \rfloor + 1$ chiamate. È un esempio di **prune-and-search**. È anche alla base delle mappe ordinate su tabella ordinata.

## Collegamenti

- **Concetti correlati**: [[Ricorsione]] · [[Mappa ordinata]] · [[Quick-select probabilistico]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Ricerca binaria|Lezione 5 — Ricerca binaria]]
