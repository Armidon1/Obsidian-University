---
title: Trie
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - alberi
---

# Trie

> [!summary] In breve
> Un trie memorizza un insieme di stringhe in un albero in cui ogni arco è un carattere: i prefissi comuni sono condivisi e la ricerca di una stringa di lunghezza $m$ costa $O(m)$ (con tabelle hash nei nodi).

- Ipotesi: nessuna stringa è prefisso di un'altra (si aggiunge un terminatore).
- Trie **standard** per $s$ stringhe di lunghezza totale $n$: altezza = stringa più lunga, $s$ foglie, al più $n + 1$ nodi.
- Usi: **word matching** (foglie con le posizioni delle parole), **prefix matching** (autocompletamento).
- Trie **compresso** (Patricia): le catene di nodi con un solo figlio diventano un arco etichettato con una stringa → $O(s)$ nodi; con etichette $(i, j, k)$ = $S[i][j..k]$ lo spazio è $O(s)$.

## Collegamenti

- **Concetti correlati**: [[Trie dei suffissi]] · [[Indice inverso]] · [[Pattern matching su stringhe]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Trie standard|Lezione 13 — Trie standard]]
