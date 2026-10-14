---
title: Frame Ethernet
tags:
  - telecomunicazioni
  - concetto
  - ethernet
---

# Frame Ethernet

> [!summary] In breve
> Il frame Ethernet ha **preambolo** (8 byte), **MAC destinazione** e **sorgente** (6 + 6), **tipo** (2), **dati** (46–1500) e **CRC** (4).

| Campo | Byte | Note |
| --- | --- | --- |
| Preambolo | 8 | 7 × `10101010` + `10101011`: sveglia e sincronizza i clock |
| Destinazione | 6 | MAC o broadcast |
| Sorgente | 6 | MAC |
| Tipo | 2 | protocollo superiore (IP, ARP = 0806…) |
| Dati | 46–1500 | MTU 1500; si riempie fino a 46 |
| CRC | 4 | rilevazione degli errori |

- Il campo tipo è l'analogo del campo protocollo di IP e delle porte del trasporto.
- **802.1Q** aggiunge un tag VLAN di 4 byte e ricalcola il CRC.

## Collegamenti

- **Concetti correlati**: [[Ethernet]] · [[CRC]] · [[Indirizzo MAC]] · [[LAN Virtuali]] · [[Frammentazione IP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Struttura del frame Ethernet|Capitolo 6 — Struttura del frame Ethernet]]
