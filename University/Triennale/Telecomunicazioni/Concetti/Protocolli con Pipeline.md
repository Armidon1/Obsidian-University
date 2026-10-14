---
title: Protocolli con Pipeline
tags:
  - telecomunicazioni
  - concetto
  - trasferimento-affidabile
  - prestazioni
---

# Protocolli con Pipeline

> [!summary] In breve
> Il mittente invia **più pacchetti senza attendere gli ACK**, riempiendo la "tubatura". L'utilizzo aumenta, ma servono più numeri di sequenza e dei buffer. Gli approcci sono due: Go-Back-N e ripetizione selettiva.

- Con $n$ pacchetti per RTT: $U = \dfrac{n \cdot L/R}{RTT + L/R}$ (3 pacchetti → utilizzo triplicato).
- Conseguenze:
  - un intervallo di numeri di sequenza più ampio;
  - buffer al mittente (pacchetti non confermati) ed eventualmente al ricevente;
  - una politica per gli errori (GBN o SR).
- La **finestra** limita i pacchetti in volo: può dipendere dal buffer del ricevente (flusso) o dalla rete (congestione).
- Non va confusa con la [[Pipelining|pipeline della CPU]] (Sistemi di Calcolo).

## Collegamenti

- **Concetti correlati**: [[Go-Back-N]] · [[Ripetizione Selettiva]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Protocolli per il trasferimento dati affidabile con pipeline|Capitolo 3 — Protocolli per il trasferimento dati affidabile con pipeline]]
