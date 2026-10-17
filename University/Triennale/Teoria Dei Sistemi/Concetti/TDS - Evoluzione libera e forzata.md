---
title: TDS - Evoluzione libera e forzata
tags:
  - teoria-dei-sistemi
  - concetto
  - rappresentazione-con-lo-stato
---

# TDS - Evoluzione libera e forzata

> [!summary] In breve
> Stato e uscita sono somma di una parte libera (dovuta a $x_0$) e di una forzata (dovuta a $u$): $x=\Phi x_0+\int Hu$, $y=\Psi x_0+\int Wu$.

- Libera: $x_L(t)=\sum c_ie^{\lambda_it}u_i$, combinazione dei modi naturali.
- Forzata: convoluzione con $H$ o $W$; in Laplace un prodotto $H(s)U(s)$, $W(s)U(s)$.
- La forzata contiene una parte dovuta ai poli del sistema e una dovuta ai poli dell'ingresso.
- Discreto: $x(t)=A^tx_0+\sum_{\tau=0}^{t-1}A^{t-1-\tau}Bu(\tau)$.

## Collegamenti

- **Concetti correlati**: [[TDS - Modi naturali]] · [[TDS - Matrice di transizione dello stato]] · [[TDS - Regime permanente]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[05 - TDS - Calcolo dell'esponenziale di matrice#Evoluzione libera dello stato|Lezione 5 — Evoluzione libera dello stato]]
> - [[08 - TDS - Modi aperiodici e pseudoperiodici#Evoluzione libera generale|Lezione 8 — Evoluzione libera generale]]
> - [[20 - TDS - Risposta forzata nel tempo discreto#Ingresso costante|Lezione 20 — Ingresso costante]]
