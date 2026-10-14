---
title: Trasferimento Dati Affidabile
tags:
  - telecomunicazioni
  - concetto
  - trasferimento-affidabile
  - rdt
---

# Trasferimento Dati Affidabile

> [!summary] In breve
> Come offrire un canale affidabile (nessun bit perso o corrotto, tutto in ordine) sopra un canale che altera e perde i dati. Il protocollo si costruisce per passi: rdt1.0 → 2.0 → 2.1 → 2.2 → 3.0.

| Versione | Canale | Meccanismi aggiunti |
| --- | --- | --- |
| rdt1.0 | perfetto | nessuno |
| rdt2.0 | errori sui bit | checksum, **ACK/NAK**, ritrasmissione (ARQ, stop-and-wait) |
| rdt2.1 | anche ACK/NAK corrotti | **numero di sequenza** da 1 bit |
| rdt2.2 | idem | niente NAK: **ACK duplicati** con numero di sequenza |
| rdt3.0 | anche **perdite** | **timer** (countdown): ritrasmissione al timeout; *alternanza di bit* |

- Interfacce: `rdt_send()` (dall'alto), `udt_send()` (canale inaffidabile), `rdt_rcv()` (dal basso), `deliver_data()`.
- Descritto con **FSM** (evento / azioni, $\Lambda$ = nulla).
- Stop-and-wait: $U = \dfrac{L/R}{RTT + L/R}$ → con 1 Gbps, 1000 byte e RTT 30 ms vale **0,00027** (267 kbps).

## Collegamenti

- **Concetti correlati**: [[Protocolli con Pipeline]] · [[Go-Back-N]] · [[Ripetizione Selettiva]] · [[Checksum Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#3.4 Principi del trasferimento dati affidabile|Capitolo 3 — 3.4 Principi del trasferimento dati affidabile]]
> - [[03 - TLC - Livello di trasporto#rdt2.0 — canale con errori sui bit|Capitolo 3 — rdt2.0 — canale con errori sui bit]]
> - [[03 - TLC - Livello di trasporto#rdt3.0 — canale con perdite ed errori|Capitolo 3 — rdt3.0 — canale con perdite ed errori]]
> - [[03 - TLC - Livello di trasporto#Riepilogo dei meccanismi|Capitolo 3 — Riepilogo dei meccanismi]]
