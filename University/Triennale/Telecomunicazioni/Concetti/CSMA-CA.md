---
title: CSMA-CA
tags:
  - telecomunicazioni
  - concetto
  - wifi
  - accesso-multiplo
---

# CSMA-CA

> [!summary] In breve
> Il MAC di 802.11: ascolta il canale, attendi **DIFS**, e se il canale è occupato fai un **backoff casuale** che scende solo a canale libero. Trasmetti l'intero frame e attendi un **ACK** (dopo SIFS). Previene le collisioni invece di rilevarle.

1. Canale libero → trasmetti dopo DIFS.
2. Altrimenti backoff esponenziale binario; il contatore si **congela** a canale occupato.
3. Contatore a 0 → trasmetti tutto il frame.
4. ACK ricevuto → avanti; nessun ACK → backoff più grande e ritrasmissione.

- Niente collision detection: trasmettere e ricevere insieme costa troppo, e il terminale nascosto renderebbe molte collisioni non rilevabili.
- Differenza con CSMA/CD: Ethernet trasmette appena il canale si libera, 802.11 aspetta il backoff per evitare collisioni costose.
- **ARQ a livello di collegamento** per l'alto BER.

## Collegamenti

- **Concetti correlati**: [[CSMA-CD]] · [[RTS e CTS]] · [[Terminale Nascosto]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Protocollo MAC di 802.11 (CSMA/CA)|Capitolo 7 — Protocollo MAC di 802.11 (CSMA/CA)]]
> - [[07 - TLC - Reti mobili e wireless#Conferma di avvenuta ricezione|Capitolo 7 — Conferma di avvenuta ricezione]]
> - [[07 - TLC - Reti mobili e wireless#Il protocollo CSMA/CA|Capitolo 7 — Il protocollo CSMA/CA]]
