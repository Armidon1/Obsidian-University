---
title: Controllo di Congestione TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - congestione
---

# Controllo di Congestione TCP

> [!summary] In breve
> TCP limita la velocità con la **finestra di congestione** `cwnd` (velocità ≈ `cwnd`/RTT) e la regola in base agli **eventi di perdita** (timeout o tre ACK duplicati) e agli ACK, che lo rendono *self-clocking*.

$$\texttt{LastByteSent} - \texttt{LastByteAcked} \le \min\{\texttt{cwnd}, \texttt{rwnd}\}$$

Principi:
- perdita → **diminuire**;
- ACK non duplicato → **aumentare**;
- **sondare la banda** (come il bambino che chiede giocattoli finché non gli si dice no).

| Evento | Reazione |
| --- | --- |
| timeout | `ssthresh = cwnd/2`, `cwnd = 1 MSS` → slow start |
| 3 ACK duplicati | `ssthresh = cwnd/2`, `cwnd = ssthresh + 3 MSS` → fast recovery (Reno); Tahoe → `cwnd = 1` |

- Le tre fasi: **slow start**, **congestion avoidance**, **fast recovery**.
- **TCP splitting**: front-end vicino all'utente, risposta in circa RTT invece di 4·RTT.

## Collegamenti

- **Concetti correlati**: [[Slow Start e Congestion Avoidance]] · [[AIMD]] · [[Fairness TCP]] · [[ECN]] · [[Costi della Congestione]] · [[Controllo di Flusso TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#3.7 Controllo di congestione TCP|Capitolo 3 — 3.7 Controllo di congestione TCP]]
> - [[03 - TLC - Livello di trasporto#Fast recovery|Capitolo 3 — Fast recovery]]
