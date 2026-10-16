---
title: Metodo equals
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - oggetti
---

# Metodo equals

> [!summary] In breve
> `a == b` confronta i riferimenti (identità); `a.equals(b)` confronta il contenuto (equivalenza), purché la classe lo ridefinisca rispettando riflessività, simmetria, transitività e `x.equals(null) == false`.

- `Object.equals` di default equivale a `==`.
- Per gli array: `Arrays.equals(a, b)` (elementi) e `Arrays.deepEquals` (multidimensionali).
- Chi ridefinisce `equals` deve ridefinire anche `hashCode` in modo coerente (oggetti uguali → stesso hash), altrimenti le [[Tabella hash|tabelle hash]] non funzionano.

## Collegamenti

- **Concetti correlati**: [[Funzione di hash]] · [[Copia superficiale e copia profonda]] · [[Classi involucro e auto-boxing]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Verifica di equivalenza|Lezione 3 — Verifica di equivalenza]]
