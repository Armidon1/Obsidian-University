---
title: Algoritmo di Knuth-Morris-Pratt
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - pattern-matching
---

# Algoritmo di Knuth-Morris-Pratt

> [!summary] In breve
> KMP pre-calcola la funzione fallimento $f(k)$ (più lungo prefisso del pattern che è suffisso di `pattern[1..k]`) e, dopo una discordanza, riparte da $f(k-1)$ senza tornare indietro nel testo: $O(n + m)$.

Esempio `"amalgamation"`:

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8–11 |
|---|---|---|---|---|---|---|---|---|---|
| $f(k)$ | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 3 | 0 |

- Ciclo principale: se `text[j] == pattern[k]` avanzano entrambi; altrimenti, se $k > 0$, $k = f(k-1)$; altrimenti $j{+}{+}$.
- Analisi: ogni iterazione aumenta $j$ o lo spostamento $s = j - k$, entrambi $\le n$ → al più $2n$ iterazioni.
- La funzione fallimento si calcola confrontando il pattern con sé stesso, in $O(m)$.

## Collegamenti

- **Concetti correlati**: [[Pattern matching su stringhe]] · [[Algoritmo di Boyer-Moore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#L'algoritmo di Knuth-Morris-Pratt|Lezione 13 — L'algoritmo di Knuth-Morris-Pratt]]
