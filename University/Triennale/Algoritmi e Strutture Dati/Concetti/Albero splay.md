---
title: Albero splay
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - analisi-ammortizzata
---

# Albero splay

> [!summary] In breve
> Un albero splay è un BST senza informazioni di bilanciamento che, dopo ogni accesso, porta il nodo in radice con passi zig, zig-zig e zig-zag: $O(\log n)$ ammortizzato per operazione.

| Passo | Configurazione | Azione |
|---|---|---|
| zig | $x$ figlio della radice | una rotazione |
| zig-zig | $x$ e il genitore dallo stesso lato | ruota prima il genitore, poi $x$ |
| zig-zag | lati opposti | ruota $x$ due volte |

- Si estende il nodo trovato (o il genitore della foglia in una ricerca fallita), il nuovo nodo dopo un inserimento, il genitore del nodo rimosso.
- Caso peggiore di una singola operazione $O(n)$, ma $O(\log n)$ ammortizzato (analisi con i ranghi $r(w) = \log n(w)$).
- **Ottimalità statica**: accedere alla voce $i$ costa $O(\log(m/f(i)))$ ammortizzato → gli elementi frequenti costano meno (come [[Euristica move-to-front|move-to-front]]).

## Collegamenti

- **Concetti correlati**: [[Analisi ammortizzata]] · [[Euristica move-to-front]] · [[Rotazione e ristrutturazione di una terna]] · [[Albero AVL]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Alberi splay|Lezione 11 — Alberi splay]]
