---
title: Radix-sort
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
---

# Radix-sort

> [!summary] In breve
> Per chiavi composte $(k_1, \dots, k_d)$ con componenti in $[0, N-1]$ si applica bucket-sort stabile su ogni componente, **dalla meno significativa alla più significativa**: $O(d(n + N))$.

Esempio con coppie: ordinando prima per la **seconda** componente e poi (stabilmente) per la prima, a parità di prima componente resta l'ordine della seconda → ordine lessicografico.

Ordinando invece prima per la prima componente il risultato **non** è ordinato.

Applicazioni: interi di $d$ cifre in base $N$, stringhe di lunghezza limitata (carattere = componente).

## Collegamenti

- **Concetti correlati**: [[Bucket-sort]] · [[Ordinamento stabile]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Radix-sort|Lezione 12 — Radix-sort]]
