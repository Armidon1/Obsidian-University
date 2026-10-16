---
title: Copia superficiale e copia profonda
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - oggetti
---

# Copia superficiale e copia profonda

> [!summary] In breve
> Una copia superficiale (shallow) duplica i riferimenti e condivide gli oggetti interni; una copia profonda (deep) duplica anche gli oggetti riferiti.

- `clone()` di `Object` fa una copia **superficiale** campo per campo.
- Per un array `int[]` la copia superficiale basta; per `Person[]` copia solo i riferimenti alle persone.
- Per una lista concatenata, la clonazione corretta crea **nuovi nodi** (altrimenti le due liste condividerebbero la catena).
- Implementare `Cloneable` e ridefinire `clone()`.

## Collegamenti

- **Concetti correlati**: [[Metodo equals]] · [[Variabile riferimento]] · [[Lista semplicemente concatenata]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Clonare strutture dati|Lezione 3 — Clonare strutture dati]]
