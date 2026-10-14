---
title: DOCSIS
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
  - hfc
---

# DOCSIS

> [!summary] In breve
> Il protocollo di livello 2 delle reti via cavo **HFC**. Usa **FDM** per separare downstream e upstream, **TDM** con mini-slot assegnati dal CMTS tramite messaggi **MAP**, e accesso **casuale** con backoff per le richieste di mini-slot.

- Downstream: 6 MHz, ~40 Mbps; trasmette solo il CMTS, quindi nessun problema di accesso.
- Upstream: 6,4 MHz, ~30 Mbps, condiviso tra i modem.
- Richieste di mini-slot in modo casuale → collisione dedotta se manca la risposta nel MAP → binary exponential backoff.
- Usa tutte e tre le famiglie di accesso multiplo, più l'allocazione centralizzata.

## Collegamenti

- **Concetti correlati**: [[Reti di Accesso]] · [[Protocolli di Accesso Multiplo]] · [[CSMA-CD]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#DOCSIS: il livello di collegamento delle reti HFC|Capitolo 6 — DOCSIS: il livello di collegamento delle reti HFC]]
