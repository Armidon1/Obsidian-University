---
title: TDS - Sistemi interconnessi
tags:
  - teoria-dei-sistemi
  - concetto
  - sistemi-interconnessi
---

# TDS - Sistemi interconnessi

> [!summary] In breve
> Serie, parallelo e retroazione: nello spazio di stato si aggregano gli stati; serie e parallelo conservano gli autovalori dei sottosistemi, la retroazione li cambia.

| | Spazio di stato | $W(s)$ |
|---|---|---|
| serie | $A=\begin{psmallmatrix}A_1&0\\B_2C_1&A_2\end{psmallmatrix}$ | $W_2W_1$ |
| parallelo | $A=\mathrm{diag}(A_1,A_2)$ | $W_1+W_2$ |
| retroazione | $A=\begin{psmallmatrix}A_1+B_1D_2C_1&B_1C_2\\B_2C_1&A_2\end{psmallmatrix}$ | $(I-W_1W_2)^{-1}W_1$ |

- Cancellazioni in serie/parallelo nascondono modi: per studiarli si realizzano i sottosistemi e poi si connettono.

## Collegamenti

- **Concetti correlati**: [[TDS - Retroazione]] · [[TDS - Funzione di trasferimento]] · [[TDS - Criterio di Nyquist]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[34 - TDS - Sistemi interconnessi#Connessione in serie (spazio di stato)|Lezione 34 — Connessione in serie (spazio di stato)]]
> - [[34 - TDS - Sistemi interconnessi#Connessione in parallelo (spazio di stato)|Lezione 34 — Connessione in parallelo (spazio di stato)]]
> - [[34 - TDS - Sistemi interconnessi#Connessione in retroazione (spazio di stato)|Lezione 34 — Connessione in retroazione (spazio di stato)]]
