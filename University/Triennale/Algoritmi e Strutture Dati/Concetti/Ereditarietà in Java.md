---
title: Ereditarietà in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - oop
  - java
---

# Ereditarietà in Java

> [!summary] In breve
> Con `extends` una sottoclasse eredita campi e metodi della superclasse, può aggiungerne e **ridefinirne** (overriding); Java ha ereditarietà singola tra classi.

- Relazione "è un" (*is-a*): ogni oggetto della sottoclasse è anche della superclasse.
- **Specializzazione** (ridefinire un metodo) ed **estensione** (aggiungere metodi).
- `super.metodo()` richiama la versione della superclasse; `super(...)` il suo costruttore.
- Tutte le classi discendono da `Object`.
- Una classe può implementare **più interfacce** ma estendere una sola classe.

## Collegamenti

- **Concetti correlati**: [[Polimorfismo e smistamento dinamico]] · [[Interfacce e classi astratte]] · [[Ereditarietà in C]] · [[Cast in Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Ereditarietà|Lezione 2 — Ereditarietà]]
