---
title: Classe NP
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
---

# Classe NP

> [!summary] In breve
> NP è la classe dei linguaggi accettati da una MT **non deterministica** in tempo polinomiale; equivalentemente, quelli per cui ogni $x \in L$ ha un **certificato** di lunghezza polinomiale verificabile in tempo polinomiale.

| problema | certificato |
|---|---|
| SAT | assegnazione di verità |
| cricca di $k$ nodi | i $k$ nodi |
| 3-colorazione | un colore per nodo |
| vertex cover / independent set | l'insieme di $k$ nodi |

- Asimmetria: non si richiede un certificato quando $x \notin L$.
- NP = **N**ondeterministic **P**olynomial time, non "non polinomiale".
- $\mathrm{P} \subseteq \mathrm{NP}$; $\mathrm{P} = \mathrm{NP}$? aperto (congettura: no).

## Collegamenti

- **Concetti correlati**: [[Classe P]] · [[NP-completezza]] · [[Macchina di Turing non deterministica]] · [[Problema SAT]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#La classe NP|Lezione 14 — La classe NP]]
> - [[14 - MC - Classi P e NP e NP-completezza#Definizione alternativa: certificati|Lezione 14 — Definizione alternativa: certificati]]
> - [[14 - MC - Classi P e NP e NP-completezza#Macchine di Turing non deterministiche|Lezione 14 — Macchine di Turing non deterministiche]]
