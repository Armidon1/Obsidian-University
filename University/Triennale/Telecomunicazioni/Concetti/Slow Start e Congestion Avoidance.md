---
title: Slow Start e Congestion Avoidance
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - congestione
---

# Slow Start e Congestion Avoidance

> [!summary] In breve
> In **slow start** `cwnd` parte da 1 MSS e cresce di 1 MSS per ACK, cioè **raddoppia a ogni RTT**, fino a `ssthresh`. In **congestion avoidance** cresce di **1 MSS per RTT**, in modo lineare. Il **fast recovery** gestisce i tre ACK duplicati.

- Velocità iniziale ≈ MSS/RTT (500 byte, 200 ms → 20 kbps).
- Congestion avoidance: a ogni ACK `cwnd += MSS·(MSS/cwnd)` (MSS 1460, cwnd 14.600 → +1/10 di MSS per ACK).
- Fast recovery: +1 MSS per ogni ACK duplicato; con il nuovo ACK `cwnd = ssthresh` → congestion avoidance; con un timeout → slow start.
- Iniziale: `cwnd = 1 MSS`, `ssthresh = 64 KB`.

Esempio Tahoe/Reno (soglia 8): 1, 2, 4, 8, 9, 10, 11, 12 → 3 ACK duplicati → `ssthresh` = 6
- **Reno**: riparte da 9 (6 + 3), poi lineare;
- **Tahoe**: riparte da 1, esponenziale fino a 6, poi lineare.

## Collegamenti

- **Concetti correlati**: [[Controllo di Congestione TCP]] · [[AIMD]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Slow start|Capitolo 3 — Slow start]]
> - [[03 - TLC - Livello di trasporto#Congestion avoidance|Capitolo 3 — Congestion avoidance]]
> - [[03 - TLC - Livello di trasporto#Fast recovery|Capitolo 3 — Fast recovery]]
