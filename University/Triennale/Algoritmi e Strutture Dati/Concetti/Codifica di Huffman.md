---
title: Codifica di Huffman
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - compressione
  - greedy
---

# Codifica di Huffman

> [!summary] In breve
> Codice a prefisso ottimo a lunghezza variabile: si fondono ripetutamente i due alberi con frequenza minima (con una coda prioritaria); i caratteri frequenti ottengono codici corti. Tempo $O(n + d\log d)$.

```text
per ogni carattere c: albero con la sola foglia c, chiave f(c), in Q
finché |Q| > 1:
  (f1, T1) = Q.removeMin(); (f2, T2) = Q.removeMin()
  inserisci in Q l'albero con figli T1, T2 e chiave f1 + f2
```

- Il codice di un carattere è il cammino radice→foglia (sinistra = 0, destra = 1).
- **Codice a prefisso**: caratteri solo nelle foglie → nessun codice è prefisso di un altro → decodifica univoca.
- Ottimalità: in un codice ottimo i due caratteri meno frequenti possono essere fratelli (proprietà di scelta greedy).

## Collegamenti

- **Concetti correlati**: [[Metodo greedy]] · [[Coda prioritaria (ADT)]] · [[Trie]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#L'algoritmo di codifica di Huffman|Lezione 13 — L'algoritmo di codifica di Huffman]]
