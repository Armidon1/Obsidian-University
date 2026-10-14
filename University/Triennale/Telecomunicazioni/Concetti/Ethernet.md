---
title: Ethernet
tags:
  - telecomunicazioni
  - concetto
  - ethernet
  - lan
---

# Ethernet

> [!summary] In breve
> La tecnologia LAN cablata dominante (Metcalfe e Boggs, Xerox PARC, anni '70). È passata dal **bus coassiale** alla **stella con hub** alla **stella con switch**; il formato del frame è rimasto invariato. Offre un servizio **senza connessione e non affidabile**.

- Nomi IEEE 802.3: **velocità** + **BASE** (banda base) + **mezzo** (T = doppino), es. 10BASE-T, 100BASE-FX, 1000BASE-LX, 10GBASE-T.
- 10BASE-2/5: coassiale, segmenti di 500 m, repeater.
- 100 Mbps: stesso MAC e frame, più livelli fisici (100 m su doppino, km su fibra).
- Gigabit (802.3z) fino a 40 Gbps: frame standard, punto a punto **full-duplex**, CSMA/CD solo sui canali condivisi.
- Non affidabile: il CRC scarta i frame errati senza ACK; ci pensa eventualmente TCP.
- Hub = livello fisico (bit, broadcast) · switch = livello 2 (frame, store-and-forward, niente collisioni).

## Collegamenti

- **Concetti correlati**: [[Frame Ethernet]] · [[CSMA-CD]] · [[Switch a Livello di Collegamento]] · [[Hub]] · [[Storia di Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Ethernet|Capitolo 6 — Ethernet]]
> - [[06 - TLC - Livello di collegamento e reti locali#Tecnologie Ethernet|Capitolo 6 — Tecnologie Ethernet]]
