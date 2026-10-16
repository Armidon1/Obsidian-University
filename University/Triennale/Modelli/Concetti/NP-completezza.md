---
title: NP-completezza
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
---

# NP-completezza

> [!summary] In breve
> Un linguaggio è NP-completo se sta in NP e ogni linguaggio di NP vi si riduce polinomialmente. Se un solo NP-completo fosse in P, sarebbe $\mathrm{P} = \mathrm{NP}$.

**Come si dimostra** che $B$ è NP-completo:
1. $B \in \mathrm{NP}$ (certificato + verificatore polinomiale);
2. $A \le_p B$ con $A$ già noto NP-completo (di solito SAT o 3SAT).

Esempi: SAT (Cook-Levin), 3SAT, programmazione intera, $k$-colorazione ($k \ge 3$), independent set, vertex cover, cricca, partizione, cammino hamiltoniano.

Confine sottile: 2-SAT e 2-colorazione sono in P, 3-SAT e 3-colorazione NP-completi.

## Collegamenti

- **Concetti correlati**: [[Classe NP]] · [[Riduzione polinomiale]] · [[Teorema di Cook-Levin]] · [[Problemi NP-hard]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#NP-completezza|Lezione 14 — NP-completezza]]
> - [[14 - MC - Classi P e NP e NP-completezza#Riduzione da 3SAT a Independent Set|Lezione 14 — Riduzione da 3SAT a Independent Set]]
> - [[14 - MC - Classi P e NP e NP-completezza#Teoria dell'NP-completezza: conclusioni|Lezione 14 — Teoria dell'NP-completezza: conclusioni]]
