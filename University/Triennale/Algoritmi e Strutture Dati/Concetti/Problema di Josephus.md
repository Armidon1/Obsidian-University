---
title: Problema di Josephus
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code
  - applicazioni
---

# Problema di Josephus

> [!summary] In breve
> $n$ persone in cerchio, si elimina ogni $k$-esima finché ne resta una: con una coda circolare si ruota $k-1$ volte e si estrae, in $O(nk)$.

```java
public static <E> E Josephus(CircularQueue<E> queue, int k) {
  if (queue.isEmpty()) return null;
  while (queue.size() > 1) {
    for (int i = 0; i < k - 1; i++) queue.rotate();
    queue.dequeue();                       // eliminato
  }
  return queue.dequeue();                  // vincitore
}
```

## Collegamenti

- **Concetti correlati**: [[Lista concatenata circolare]] · [[Coda (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Il problema di Josephus|Lezione 6 — Il problema di Josephus]]
