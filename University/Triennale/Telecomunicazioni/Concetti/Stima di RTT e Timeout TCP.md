---
title: Stima di RTT e Timeout TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - timer
---

# Stima di RTT e Timeout TCP

> [!summary] In breve
> TCP stima l'RTT con una media mobile esponenziale dei campioni (`EstimatedRTT`), ne misura la variabilità (`DevRTT`) e imposta il timeout a `EstimatedRTT + 4·DevRTT`.

$$\texttt{EstimatedRTT} = 0{,}875 \cdot \texttt{EstimatedRTT} + 0{,}125 \cdot \texttt{SampleRTT}$$

$$\texttt{DevRTT} = 0{,}75 \cdot \texttt{DevRTT} + 0{,}25 \cdot |\texttt{SampleRTT} - \texttt{EstimatedRTT}|$$

$$\texttt{TimeoutInterval} = \texttt{EstimatedRTT} + 4 \cdot \texttt{DevRTT}$$

- Un solo `SampleRTT` alla volta, **mai** sui segmenti ritrasmessi (Karn).
- **EWMA**: il peso dei vecchi campioni decresce esponenzialmente ($\alpha = 1/8$, $\beta = 1/4$, RFC 6298).
- Timeout iniziale di **1 s**; dopo un timeout si **raddoppia** (0,75 → 1,5 → 3 s), una forma di controllo di congestione.

## Collegamenti

- **Concetti correlati**: [[Ritrasmissione Rapida]] · [[Controllo di Congestione TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Timeout e stima del tempo di andata e ritorno|Capitolo 3 — Timeout e stima del tempo di andata e ritorno]]
> - [[03 - TLC - Livello di trasporto#Stima del tempo di andata e ritorno|Capitolo 3 — Stima del tempo di andata e ritorno]]
> - [[03 - TLC - Livello di trasporto#Impostazione e gestione del timeout|Capitolo 3 — Impostazione e gestione del timeout]]
> - [[03 - TLC - Livello di trasporto#Raddoppio dell'intervallo di timeout|Capitolo 3 — Raddoppio dell'intervallo di timeout]]
