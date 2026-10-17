---
title: TDS - Osservabilità
tags:
  - teoria-dei-sistemi
  - concetto
  - osservabilita
---

# TDS - Osservabilità

> [!summary] In breve
> Stati inosservabili: danno uscita libera nulla; formano $\mathcal I=\ker\mathcal O$, con $\mathcal O=(C;CA;\dots;CA^{n-1})$. Il sistema è tutto osservabile se $\mathrm{rank}\,\mathcal O=n$.

- Due stati sono indistinguibili se la loro differenza è inosservabile.
- Cayley-Hamilton: bastano $n$ blocchi di righe.
- $\mathcal I$ è $A$-invariante e contenuto in $\ker C$.
- Base (base di $\mathcal I$ | completamento): $\tilde A=\begin{psmallmatrix}A_{11}&A_{12}\\0&A_{22}\end{psmallmatrix}$, $\tilde C=(0\ C_2)$.
- Duale della raggiungibilità: $(A,C)$ osservabile ⟺ $(A',C')$ raggiungibile.

## Collegamenti

- **Concetti correlati**: [[TDS - Raggiungibilità]] · [[TDS - Scomposizione di Kalman]] · [[TDS - Osservatore asintotico]] · [[TDS - Eccitabilità e osservabilità dei modi]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[26 - TDS - Stati inosservabili#Stati indistinguibili e inosservabili|Lezione 26 — Stati indistinguibili e inosservabili]]
> - [[26 - TDS - Stati inosservabili#Il teorema di Cayley-Hamilton|Lezione 26 — Il teorema di Cayley-Hamilton]]
> - [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo l'osservabilità|Lezione 27 — Partizione del sistema secondo l'osservabilità]]
