---
title: Pila dei metodi di Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - jvm
  - memoria
---

# Pila dei metodi di Java

> [!summary] In breve
> Ogni thread della JVM ha una pila di frame, uno per ogni metodo attivo, con parametri, variabili locali e program counter di ritorno: è ciò che rende possibile la ricorsione.

- Invocazione → `push` del frame; terminazione → `pop` e ripresa del chiamante dal PC salvato + 1.
- In cima c'è sempre il metodo in esecuzione; sotto i metodi sospesi.
- La JVM ha anche una **pila degli operandi** per valutare le espressioni ($a + b$: push $a$, push $b$, somma).
- Overflow della pila (ricorsione troppo profonda) → `StackOverflowError`.

## Collegamenti

- **Concetti correlati**: [[Ricorsione]] · [[Pila (ADT)]] · [[Allocazione nella memoria heap]] · [[Stack Frame]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Strutture di tipo stack nella Java Virtual Machine|Lezione 15 — Strutture di tipo stack nella Java Virtual Machine]]
