---
title: TDS - Scomposizione di Kalman
tags:
  - teoria-dei-sistemi
  - concetto
  - scomposizione-di-kalman
  - raggiungibilita
  - osservabilita
---

# TDS - Scomposizione di Kalman

> [!summary] In breve
> Lo spazio di stato si divide in quattro parti: raggiungibile/non raggiungibile × inosservabile/osservabile; solo la parte raggiungibile e osservabile compare nella funzione di trasferimento.

- $\chi_1=\mathcal R\cap\mathcal I$, $\chi_1\oplus\chi_2=\mathcal R$, $\chi_1\oplus\chi_3=\mathcal I$, $\chi_4$ completamento.
- $T^{-1}=$ (basi di $\chi_1,\chi_2,\chi_3,\chi_4$).
$$\tilde A=\begin{pmatrix}A_{11}&A_{12}&A_{13}&A_{14}\\0&A_{22}&0&A_{24}\\0&0&A_{33}&A_{34}\\0&0&0&A_{44}\end{pmatrix},\quad\tilde B=\begin{pmatrix}B_1\\B_2\\0\\0\end{pmatrix},\quad\tilde C=\begin{pmatrix}0&C_2&0&C_4\end{pmatrix}$$
- $W(t)=C_2e^{A_{22}t}B_2$: $(A_{22},B_2,C_2)$ è una realizzazione minima.

## Collegamenti

- **Concetti correlati**: [[TDS - Raggiungibilità]] · [[TDS - Osservabilità]] · [[TDS - Realizzazione minima]] · [[GEO - Somma diretta]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Scomposizione di Kalman|Lezione 28 — Scomposizione di Kalman]]
> - [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Struttura delle matrici nella scomposizione di Kalman|Lezione 28 — Struttura delle matrici nella scomposizione di Kalman]]
> - [[29 - TDS - Esercizi sulla scomposizione di Kalman#Primo esercizio|Lezione 29 — Primo esercizio]]
> - [[41 - TDS - Esercizi di riepilogo finale#Scomposizione di Kalman|Lezione 41 — Scomposizione di Kalman]]
