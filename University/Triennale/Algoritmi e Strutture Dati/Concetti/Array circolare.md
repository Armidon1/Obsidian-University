---
title: Array circolare
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code
  - array
---

# Array circolare

> [!summary] In breve
> Per una coda su array si fa "girare" l'indice con il modulo: il primo elemento è in `f` e il prossimo posto libero in `(f + sz) % N`, così `dequeue` non richiede spostamenti.

```java
public void enqueue(E e) {
  if (sz == data.length) throw new IllegalStateException("Queue is full");
  int avail = (f + sz) % data.length;
  data[avail] = e; sz++;
}
public E dequeue() {
  if (isEmpty()) return null;
  E answer = data[f]; data[f] = null;
  f = (f + 1) % data.length; sz--;
  return answer;
}
```

Senza il modulo, dopo molti `dequeue` la coda "scivolerebbe" fuori dall'array pur avendo spazio libero all'inizio.

## Collegamenti

- **Concetti correlati**: [[Coda (ADT)]] · [[Lista concatenata circolare]] · [[Array dinamico]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#L'uso di un array circolare|Lezione 6 — L'uso di un array circolare]]
