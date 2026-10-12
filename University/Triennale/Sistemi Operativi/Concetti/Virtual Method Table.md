---
title: Virtual Method Table
tags:
  - sistemi-operativi
  - concetto
  - linguaggio-c
  - oop
  - polimorfismo
---

# Virtual Method Table

> [!summary] In breve
> Il late binding si implementa con un puntatore, in ogni oggetto, a una tabella di puntatori a funzione condivisa da tutti gli oggetti della stessa classe.

- In C++ solo i metodi `virtual` sono soggetti a override (in Java tutti quelli non `static`).
- Ogni istanza ha un puntatore alla **VMT** della propria classe; la VMT contiene i puntatori ai metodi (incluso il **destructor**).
- Chiamata virtuale: `obj->ops->print_fn(obj)`.
- In C: `struct Ops { void (*print_fn)(A*); void (*dtor_fn)(A*); }`, un'istanza globale per classe, e un wrapper `A_print(a)` che fa il dispatch.
- Un **driver** è una classe virtuale: una tabella di operazioni (`open`, `read`, `write`, `ioctl`…) che ogni driver implementa a modo suo.

## Collegamenti

- **Concetti correlati**: [[Puntatori a Funzione]] · [[Ereditarietà in C]] · [[Lista Generica in C]] · [[Driver e Block Device]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[03 - SO - Programmazione OOP in C#Polimorfismo (late binding)|Lezione 3 — Polimorfismo (late binding)]]
> - [[03 - SO - Programmazione OOP in C#Come è implementato: la Virtual Method Table|Lezione 3 — Come è implementato: la Virtual Method Table]]
> - [[03 - SO - Programmazione OOP in C#Lista polimorfica|Lezione 3 — Lista polimorfica]]
