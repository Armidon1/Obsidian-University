---
title: LAN Virtuali
tags:
  - telecomunicazioni
  - concetto
  - vlan
  - lan
---

# LAN Virtuali

> [!summary] In breve
> Una **VLAN** definisce più LAN logiche su un'unica infrastruttura di switch, risolvendo isolamento del traffico, spreco di switch e spostamenti di utenti. Tra switch si usa il **trunking** con frame **802.1Q** etichettati.

- **Basate sulle porte**: es. porte 2–8 = Ingegneria, 9–15 = Informatica; ogni gruppo è un **dominio broadcast**.
- Tra VLAN diverse si passa per un **router** (anche integrato nello switch).
- **Trunking**: una porta appartiene a tutte le VLAN; senza trunking servirebbero $N$ porte per $N$ VLAN.
- **802.1Q**: tag di 4 byte dopo il MAC sorgente → TPID `81-00` + tag control information (**VLAN ID** di 12 bit, **priorità** di 3 bit); CRC ricalcolato.
- Altre basi per le VLAN: MAC, protocollo di rete; estensione tramite router.

## Collegamenti

- **Concetti correlati**: [[Switch a Livello di Collegamento]] · [[Frame Ethernet]] · [[VLAN]] · [[Reti dei Data Center]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#LAN virtuali (VLAN)|Capitolo 6 — LAN virtuali (VLAN)]]
