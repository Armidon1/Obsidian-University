---
title: Problemi NP-hard
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
---

# Problemi NP-hard

> [!summary] In breve
> Un problema è NP-hard (NP-difficile) se ogni problema di NP vi si riduce polinomialmente, senza richiedere che stia in NP. NP-completo = NP-hard ∩ NP.

- Possono essere più difficili di tutta NP: formule booleane quantificate (PSPACE), **problema della fermata** (indecidibile).
- Le versioni di **ottimizzazione** dei problemi NP-completi sono NP-hard; si riducono a $O(\log n)$ problemi di decisione con la ricerca binaria (es. numero cromatico).
- Programmazione intera: la riduzione da 3SAT la rende NP-hard; per dire NP-completa serve anche $\mathrm{PI} \in \mathrm{NP}$.

## Collegamenti

- **Concetti correlati**: [[NP-completezza]] · [[Riduzione polinomiale]] · [[Problema della fermata]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#Problemi NP-hard|Lezione 14 — Problemi NP-hard]]
> - [[14 - MC - Classi P e NP e NP-completezza#Problemi di ottimizzazione|Lezione 14 — Problemi di ottimizzazione]]
> - [[14 - MC - Classi P e NP e NP-completezza#Classi di complessità|Lezione 14 — Classi di complessità]]
