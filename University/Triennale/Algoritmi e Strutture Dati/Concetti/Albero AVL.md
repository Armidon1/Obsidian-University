---
title: Albero AVL
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - bilanciamento
---

# Albero AVL

> [!summary] In breve
> Un AVL è un BST in cui, per ogni nodo, le altezze dei due figli differiscono al più di 1: l'altezza è $< 2\log n + 2$ e tutte le operazioni costano $O(\log n)$ nel caso peggiore.

- Altezza: il numero minimo di nodi $n(h) = 1 + n(h-1) + n(h-2)$ cresce come Fibonacci → $n(h) > 2^{h/2 - 1}$.
- **Inserimento**: si risale dal nuovo nodo; al primo nodo sbilanciato $z$, con $y$ figlio più alto e $x$ nipote più alto, `restructure(x)`: **una sola** ristrutturazione basta.
- **Rimozione**: stessa idea (a parità di altezze si sceglie $x$ "allineato" con $y$), ma può servire risalire con $O(\log n)$ ristrutturazioni.
- Ogni nodo memorizza la propria altezza.

## Collegamenti

- **Concetti correlati**: [[Albero di ricerca binario]] · [[Rotazione e ristrutturazione di una terna]] · [[Albero rosso-nero]] · [[Fibonacci ricorsivo]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Alberi AVL|Lezione 11 — Alberi AVL]]
