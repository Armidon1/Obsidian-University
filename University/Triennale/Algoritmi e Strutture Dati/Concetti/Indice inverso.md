---
title: Indice inverso
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - motori-di-ricerca
---

# Indice inverso

> [!summary] In breve
> Mappa da ogni parola (termine indice) alla lista delle pagine che la contengono (lista di occorrenza): il trie dei termini sta in memoria, le liste su disco; una query con più parole è l'intersezione delle liste.

1. array delle **liste di occorrenza** (su disco);
2. **trie compresso** dei termini, con nelle foglie l'indice della lista (in memoria).

- Una parola: word matching nel trie.
- Più parole: intersezione delle liste, efficiente se sono ordinate per indirizzo di pagina.
- Poi le pagine vanno ordinate per **rilevanza** (*ranking*).

Nei DBMS: [[Inverted List]].

## Collegamenti

- **Concetti correlati**: [[Trie]] · [[Insiemi, multi-insiemi e multi-mappe]] · [[Inverted List]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Indici inversi|Lezione 13 — Indici inversi]]
