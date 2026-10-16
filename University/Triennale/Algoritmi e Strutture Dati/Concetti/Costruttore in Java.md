---
title: Costruttore in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - oggetti
---

# Costruttore in Java

> [!summary] In breve
> Un costruttore è un metodo speciale con lo stesso nome della classe e senza tipo di ritorno, invocato da `new` per inizializzare lo stato del nuovo oggetto.

- Se non ne viene definito nessuno, Java fornisce un costruttore di default senza parametri.
- Si possono avere più costruttori (**sovraccarico**, *overloading*) con firme diverse.
- `this(...)` invoca un altro costruttore della stessa classe; `super(...)` quello della superclasse (deve essere la prima istruzione).
- I campi non inizializzati valgono 0, `false` o `null`.

## Collegamenti

- **Concetti correlati**: [[Variabile riferimento]] · [[Ereditarietà in Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Definire costruttori|Lezione 1 — Definire costruttori]]
