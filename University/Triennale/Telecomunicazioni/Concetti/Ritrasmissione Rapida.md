---
title: Ritrasmissione Rapida
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - affidabilita
---

# Ritrasmissione Rapida

> [!summary] In breve
> Fast retransmit: quando riceve **tre ACK duplicati** per lo stesso dato, il mittente TCP ritrasmette subito il segmento mancante, **senza aspettare il timeout**.

Generazione degli ACK (RFC 5681):

| Evento al ricevente | Azione |
| --- | --- |
| arrivo ordinato, tutto il precedente già riscontrato | **ACK ritardato** (fino a 500 ms) |
| arrivo ordinato, un altro segmento in attesa di ACK | subito un ACK cumulativo |
| arrivo fuori ordine (**buco**) | subito un **ACK duplicato** |
| segmento che colma il buco | subito un ACK |

- Tre duplicati e non uno, perché un singolo duplicato può essere un semplice riordinamento.
- Tre ACK duplicati funzionano come un **NAK implicito**.
- TCP è un **ibrido GBN/SR**: ACK cumulativi, ma buffer dei fuori ordine e ritrasmissione di un solo segmento (con SACK è quasi SR).

## Collegamenti

- **Concetti correlati**: [[Numeri di Sequenza e ACK TCP]] · [[Stima di RTT e Timeout TCP]] · [[Controllo di Congestione TCP]] · [[Go-Back-N]] · [[Ripetizione Selettiva]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Trasferimento dati affidabile|Capitolo 3 — Trasferimento dati affidabile]]
> - [[03 - TLC - Livello di trasporto#Alcuni scenari interessanti|Capitolo 3 — Alcuni scenari interessanti]]
> - [[03 - TLC - Livello di trasporto#Ritrasmissione rapida|Capitolo 3 — Ritrasmissione rapida]]
> - [[03 - TLC - Livello di trasporto#Go-Back-N o ripetizione selettiva?|Capitolo 3 — Go-Back-N o ripetizione selettiva?]]
