---
title: Ricorsione
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
---

# Ricorsione

> [!summary] In breve
> Un metodo è ricorsivo se invoca se stesso su un'istanza più piccola, fino a uno o più **casi base** risolti direttamente.

- Ogni chiamata ha il proprio frame nella [[Pila dei metodi di Java|pila delle invocazioni]]: più istanze coesistono.
- Senza caso base (o se non lo si raggiunge) si ha ricorsione infinita → `StackOverflowError`.
- Analisi: si somma il lavoro di ogni chiamata (escluse le sotto-chiamate), aiutandosi con l'albero/traccia di ricorsione.

```java
public static int factorial(int n) {
  if (n == 0) return 1;            // caso base
  return n * factorial(n - 1);     // passo ricorsivo
}
```

## Collegamenti

- **Concetti correlati**: [[Ricorsione lineare, binaria e multipla]] · [[Ricorsione in coda]] · [[Pila dei metodi di Java]] · [[Dividi-e-conquista]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Introduzione|Lezione 5 — Introduzione]]
