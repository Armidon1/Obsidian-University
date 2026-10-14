---
title: Cronaca di una Richiesta Web
tags:
  - telecomunicazioni
  - concetto
  - sintesi
  - pila-protocollare
---

# Cronaca di una Richiesta Web

> [!summary] In breve
> I 24 passi con cui il portatile di Bob scarica www.google.com mettono insieme tutta la pila: **DHCP** (IP, gateway, DNS), **DNS + ARP** (MAC del gateway), **instradamento** OSPF/BGP, **TCP** (handshake) e **HTTP** (GET e risposta).

| Passi | Protocolli | Risultato |
| --- | --- | --- |
| 1–7 | DHCP su UDP/IP/Ethernet broadcast; autoapprendimento dello switch | IP 68.85.2.101, gateway 68.85.2.1, DNS 68.87.71.226 |
| 8–13 | DNS query; ARP per il MAC del gateway | frame verso il gateway con IP di destinazione = DNS |
| 14–17 | inoltro intra-AS (OSPF/IS-IS/RIP) e BGP | IP di Google 64.233.169.105 |
| 18–21 | TCP SYN / SYNACK, socket di benvenuto e di connessione | connessione stabilita |
| 22–24 | HTTP GET / risposta | pagina visualizzata |

- Omessi: NAT, wireless, sicurezza, cache web, gerarchia DNS.

## Collegamenti

- **Concetti correlati**: [[DHCP]] · [[Protocollo ARP]] · [[Gerarchia dei DNS Server]] · [[Protocollo BGP]] · [[Gestione della Connessione TCP]] · [[Messaggi HTTP]] · [[Pila di Protocolli Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.7 Retrospettiva: cronaca di una richiesta di una pagina web|Capitolo 6 — 6.7 Retrospettiva: cronaca di una richiesta di una pagina web]]
> - [[06 - TLC - Livello di collegamento e reti locali#Si comincia: DHCP, UDP, IP ed Ethernet (passi 1–7)|Capitolo 6 — Si comincia: DHCP, UDP, IP ed Ethernet (passi 1–7)]]
> - [[06 - TLC - Livello di collegamento e reti locali#Ancora all'inizio: DNS e ARP (passi 8–13)|Capitolo 6 — Ancora all'inizio: DNS e ARP (passi 8–13)]]
> - [[06 - TLC - Livello di collegamento e reti locali#Interazione client-server: TCP e HTTP (passi 18–24)|Capitolo 6 — Interazione client-server: TCP e HTTP (passi 18–24)]]
