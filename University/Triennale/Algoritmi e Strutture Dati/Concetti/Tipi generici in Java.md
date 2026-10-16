---
title: Tipi generici in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - generics
---

# Tipi generici in Java

> [!summary] In breve
> I tipi generici (`class Pair<A,B>`) parametrizzano classi e metodi rispetto ai tipi degli elementi, con controllo a compile time e senza cast; non ammettono tipi primitivi.

```java
public class Pair<A,B> { A first; B second; }
Pair<String,Double> p = new Pair<>("x", 2.0);
public static <T> void reverse(T[] data) { ... }   // metodo generico
```

- Con i primitivi si usano le classi involucro (`Pair<Integer,…>`).
- *Type erasure*: a runtime il tipo parametro non esiste → non si può fare `new T[n]`; si usa `(T[]) new Object[n]` con un cast non controllato.
- Vincoli: `<K extends Comparable<K>>`.

## Collegamenti

- **Concetti correlati**: [[Classi involucro e auto-boxing]] · [[Comparatore]] · [[Tipo di dato astratto]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Programmazione mediante tipi generici|Lezione 2 — Programmazione mediante tipi generici]]
