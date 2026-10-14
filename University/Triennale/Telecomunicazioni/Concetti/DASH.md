---
title: DASH
tags:
  - telecomunicazioni
  - concetto
  - video
  - streaming
---

# DASH

> [!summary] In breve
> **Dynamic Adaptive Streaming over HTTP**: il video è codificato in più versioni con bit rate diversi; il client legge un **manifesto** e sceglie, blocco per blocco, la versione adatta alla banda misurata.

- **Streaming HTTP** semplice: un `GET` per tutto il file, buffer, riproduzione. Il limite è che tutti ricevono la stessa codifica.
- **DASH**:
  - versioni multiple (es. 300 kbps, 1 Mbps, 3 Mbps), ognuna con un URL;
  - il **manifesto** elenca URL e bit rate;
  - si richiedono blocchi di pochi secondi (`GET` con un intervallo di byte);
  - buffer pieno e banda alta → qualità alta; buffer vuoto e banda bassa → qualità bassa.
- Il throughput medio deve essere ≥ al **bit rate** del video.

## Collegamenti

- **Concetti correlati**: [[Content Distribution Network]] · [[Protocollo HTTP]] · [[Throughput e Collo di Bottiglia]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Video su Internet|Capitolo 2 — Video su Internet]]
> - [[02 - TLC - Livello di applicazione#Streaming HTTP e DASH|Capitolo 2 — Streaming HTTP e DASH]]
