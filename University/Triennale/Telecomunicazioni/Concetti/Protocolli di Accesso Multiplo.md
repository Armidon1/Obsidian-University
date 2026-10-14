---
title: Protocolli di Accesso Multiplo
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
  - mac
---

# Protocolli di Accesso Multiplo

> [!summary] In breve
> Coordinano più nodi su un canale **broadcast** condiviso per evitare o gestire le **collisioni**. Si dividono in protocolli a **suddivisione del canale**, ad **accesso casuale** e a **rotazione**.

Protocollo ideale su un canale a $R$ bps:
1. un nodo attivo ottiene $R$;
2. $M$ nodi attivi ottengono $R/M$ in media;
3. è decentralizzato;
4. è semplice.

| Classe | Esempi | Proprietà 1 | Proprietà 2 |
| --- | --- | --- | --- |
| Suddivisione del canale | TDM, FDM, CDMA | ✗ (sempre $R/N$) | ✓ |
| Accesso casuale | ALOHA, CSMA/CD | ✓ | ✗ |
| A rotazione | polling, token | ≈ | ✓ |

- Punto a punto (PPP, HDLC) contro broadcast (Ethernet, Wi-Fi, satellite, HFC).

## Collegamenti

- **Concetti correlati**: [[Protocolli ALOHA]] · [[CSMA-CD]] · [[Protocolli a Rotazione]] · [[Multiplexing FDM e TDM]] · [[DOCSIS]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.3 Collegamenti broadcast e protocolli di accesso multiplo|Capitolo 6 — 6.3 Collegamenti broadcast e protocolli di accesso multiplo]]
> - [[06 - TLC - Livello di collegamento e reti locali#Protocolli a suddivisione del canale|Capitolo 6 — Protocolli a suddivisione del canale]]
