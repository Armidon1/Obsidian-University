---
title: AIMD
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - congestione
---

# AIMD

> [!summary] In breve
> **Additive-Increase, Multiplicative-Decrease**: TCP aumenta `cwnd` di 1 MSS per RTT e la dimezza a ogni perdita (tre ACK duplicati). Il risultato è il tipico andamento a **dente di sega**.

- La velocità oscilla tra $\dfrac{W}{2\,RTT}$ e $\dfrac{W}{RTT}$:
  $$\text{throughput medio} = \frac{0{,}75\,W}{RTT}$$
- In funzione delle perdite:
  $$\text{throughput} = \frac{1{,}22 \cdot \text{MSS}}{RTT\sqrt{L}}$$
  10 Gbps, 1500 byte, RTT 100 ms → $W \approx 83.333$ segmenti, $L \approx 2 \cdot 10^{-10}$.
- Varianti: Reno (la più diffusa), Vegas (usa l'aumento dell'RTT), SACK, BIC.
- AIMD equivale a un algoritmo distribuito di ottimizzazione (Kelly 1998).

## Collegamenti

- **Concetti correlati**: [[Controllo di Congestione TCP]] · [[Fairness TCP]] · [[Slow Start e Congestion Avoidance]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Retrospettiva: AIMD|Capitolo 3 — Retrospettiva: AIMD]]
> - [[03 - TLC - Livello di trasporto#Throughput medio di TCP|Capitolo 3 — Throughput medio di TCP]]
> - [[03 - TLC - Livello di trasporto#Futuro di TCP sulle connessioni a larga banda|Capitolo 3 — Futuro di TCP sulle connessioni a larga banda]]
