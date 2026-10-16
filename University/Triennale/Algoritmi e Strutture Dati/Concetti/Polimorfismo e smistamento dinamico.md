---
title: Polimorfismo e smistamento dinamico
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - oop
  - java
---

# Polimorfismo e smistamento dinamico

> [!summary] In breve
> Una variabile di un supertipo può riferire oggetti di qualunque sottotipo; il metodo eseguito è scelto **a runtime** in base al tipo effettivo dell'oggetto (dynamic dispatch).

```java
Progression p = new FibonacciProgression();
p.nextValue();   // esegue la versione di FibonacciProgression
```

- **Tipo statico** (della variabile): decide quali metodi si possono chiamare (controllo del compilatore).
- **Tipo dinamico** (dell'oggetto): decide quale implementazione viene eseguita.
- Sovraccarico (*overloading*, risolto a compile time) ≠ ridefinizione (*overriding*, risolta a runtime).
- In C++/C si realizza con le [[Vtable]].

## Collegamenti

- **Concetti correlati**: [[Ereditarietà in Java]] · [[Interfacce e classi astratte]] · [[Cast in Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Polimorfismo e smistamento dinamico|Lezione 2 — Polimorfismo e smistamento dinamico]]
