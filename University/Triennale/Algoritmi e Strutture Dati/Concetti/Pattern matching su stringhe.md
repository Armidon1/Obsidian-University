---
title: Pattern matching su stringhe
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - pattern-matching
---

# Pattern matching su stringhe

> [!summary] In breve
> Dato un testo di lunghezza $n$ e un pattern di lunghezza $m$, trovare dove (e se) il pattern compare come sottostringa; la forza bruta prova tutti gli allineamenti in $O(nm)$.

| Algoritmo | Pre-elaborazione | Caso peggiore | Note |
|---|---|---|---|
| forza bruta | — | $O(nm)$ | semplice |
| [[Algoritmo di Boyer-Moore|Boyer-Moore]] (semplificato) | funzione `last`, $O(m + |\Sigma|)$ | $O(nm + |\Sigma|)$ | velocissimo su testo naturale |
| [[Algoritmo di Knuth-Morris-Pratt|KMP]] | funzione fallimento, $O(m)$ | $O(n + m)$ | ottimo |
| [[Trie dei suffissi]] | sul **testo**, $O(n)$ | $O(m)$ per ricerca | molte ricerche sullo stesso testo |

Terminologia: sottostringa $P[i..j]$, prefisso $P[0..j]$, suffisso $P[i..n-1]$, alfabeto $\Sigma$.

## Collegamenti

- **Concetti correlati**: [[Algoritmo di Boyer-Moore]] · [[Algoritmo di Knuth-Morris-Pratt]] · [[Trie]] · [[Trie dei suffissi]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Algoritmi di pattern matching|Lezione 13 — Algoritmi di pattern matching]]
