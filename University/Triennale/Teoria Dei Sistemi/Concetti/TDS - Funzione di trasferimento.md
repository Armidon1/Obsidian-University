---
title: TDS - Funzione di trasferimento
tags:
  - teoria-dei-sistemi
  - concetto
  - funzione-di-trasferimento
---

# TDS - Funzione di trasferimento

> [!summary] In breve
> $W(s)=C(sI-A)^{-1}B+D$, trasformata della risposta impulsiva: $Y_F(s)=W(s)U(s)$. È razionale propria (strettamente se $D=0$) e i suoi poli sono gli autovalori eccitabili e osservabili.

- Non dipende dalle coordinate dello stato.
- Cancellazioni polo-zero → modi nascosti (non raggiungibili o non osservabili).
- $W(0)$ = guadagno statico; $W(j\omega)$ = risposta armonica.
- Serie $W_2W_1$, parallelo $W_1+W_2$, retroazione $\frac{W_1}{1\mp W_1W_2}$.

## Collegamenti

- **Concetti correlati**: [[TDS - Risposta impulsiva]] · [[TDS - Trasformata di Laplace]] · [[TDS - Realizzazione]] · [[TDS - Sistemi interconnessi]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[15 - TDS - Trasformata di Laplace#Trasformate delle matrici della forma esplicita|Lezione 15 — Trasformate delle matrici della forma esplicita]]
> - [[15 - TDS - Trasformata di Laplace#Cenni sulle antitrasformate|Lezione 15 — Cenni sulle antitrasformate]]
> - [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Scomposizione di Kalman|Lezione 28 — Scomposizione di Kalman]]
