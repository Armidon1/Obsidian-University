---
title: Bucket-sort
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
---

# Bucket-sort

> [!summary] In breve
> Con chiavi intere in $[0, N-1]$ si mette ogni voce nel bucket $B[k]$ e poi si svuotano i bucket in ordine: $O(n + N)$ tempo e spazio, senza confronti.

```text
B = array di N sequenze vuote
per ogni voce e di S: sposta e in fondo a B[chiave(e)]
per i da 0 a N-1: sposta in fondo a S tutte le voci di B[i], in ordine
```

- Efficiente se $N = O(n)$ (o $O(n\log n)$); inutile se $N \gg n$.
- **Stabile** se i bucket si usano come code (FIFO).
- Base del [[Radix-sort|radix-sort]].

## Collegamenti

- **Concetti correlati**: [[Radix-sort]] · [[Ordinamento stabile]] · [[Limite inferiore per l'ordinamento basato su confronti]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Bucket-sort|Lezione 12 — Bucket-sort]]
