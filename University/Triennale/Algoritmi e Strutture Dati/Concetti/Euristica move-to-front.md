---
title: Euristica move-to-front
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - applicazioni
---

# Euristica move-to-front

> [!summary] In breve
> Per mantenere i preferiti si sposta in testa alla lista l'elemento appena acceduto: gli elementi usati spesso restano davanti senza contare esplicitamente gli accessi.

- **Lista ordinata per conteggio**: top-$k$ in $O(k)$, ma ogni accesso costa $O(n)$ per tenere l'ordine.
- **Move-to-front**: accesso $O(1)$ dopo averlo trovato; per il top-$k$ serve una copia e $O(kn)$.
- Sfrutta la **località temporale** degli accessi; caso pessimo se gli accessi sono a rotazione.
- È l'idea dietro gli [[Albero splay|alberi splay]] e la politica LRU.

## Collegamenti

- **Concetti correlati**: [[Albero splay]] · [[Algoritmi di sostituzione delle pagine]] · [[Località dei Riferimenti]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Uso di una lista con l'euristica move-to-front|Lezione 7 — Uso di una lista con l'euristica move-to-front]]
