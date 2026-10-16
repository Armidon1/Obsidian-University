---
title: Teorema di Cook-Levin
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
  - sat
---

# Teorema di Cook-Levin

> [!summary] In breve
> SAT è NP-completo: per ogni $L \in \mathrm{NP}$ e ogni $x$ si costruisce in tempo polinomiale una formula $F(x, y)$, nelle variabili del certificato $y$, soddisfacibile se e solo se $x \in L$.

- Si parte dal verificatore polinomiale $V$ e dal polinomio $p$ della definizione di NP.
- La formula descrive con clausole la computazione di $V$ su $(x, y)$ passo per passo e impone che termini in uno stato finale.
- Le variabili libere sono i $p(|x|)$ bit $y_0, \dots, y_{p(|x|)-1}$ del certificato.
- Dopo Cook-Levin, le altre prove di NP-completezza si fanno per riduzione da SAT.

## Collegamenti

- **Concetti correlati**: [[Problema SAT]] · [[NP-completezza]] · [[Classe NP]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#Teorema di Cook-Levin|Lezione 14 — Teorema di Cook-Levin]]
