---
title: Schema template method
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - design-pattern
  - oop
---

# Schema template method

> [!summary] In breve
> Una superclasse definisce lo scheletro di un algoritmo e delega alcuni passi a metodi "aggancio" (hook) che le sottoclassi ridefiniscono.

- Il codice comune sta una sola volta nella superclasse; le varianti nelle sottoclassi.
- Esempi nel libro:
  - `AbstractProgression.nextValue()` chiama `advance()` ridefinito dalle sottoclassi;
  - `TreeMap` chiama `rebalanceInsert`, `rebalanceDelete`, `rebalanceAccess`, vuoti, ridefiniti da `AVLTreeMap`, `SplayTreeMap`, `RBTreeMap`.

## Collegamenti

- **Concetti correlati**: [[Interfacce e classi astratte]] · [[Albero AVL]] · [[Albero splay]] · [[Albero rosso-nero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Classi astratte|Lezione 2 — Classi astratte]]
