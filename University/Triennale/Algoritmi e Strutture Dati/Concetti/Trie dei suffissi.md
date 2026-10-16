---
title: Trie dei suffissi
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - alberi
---

# Trie dei suffissi

> [!summary] In breve
> Il trie (compresso) di tutti i suffissi di una stringa $X$: occupa $O(n)$ spazio con etichette a intervalli $j..k$ e trova qualunque sottostringa di lunghezza $m$ in $O(m)$.

- Si aggiunge `$` in fondo a $X$ perché nessun suffisso sia prefisso di un altro.
- Esplicitamente i suffissi occupano $n(n+1)/2$ caratteri; la rappresentazione compatta $O(n)$.
- $P$ è sottostringa di $X$ ⇔ $P$ è prefisso di un suffisso ⇔ esiste il cammino di $P$ dalla radice.
- Costruzione: $O(n)$ con algoritmi specializzati (complessi), $O(|\Sigma| n^2)$ con l'inserimento ingenuo.

## Collegamenti

- **Concetti correlati**: [[Trie]] · [[Pattern matching su stringhe]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Trie dei suffissi|Lezione 13 — Trie dei suffissi]]
