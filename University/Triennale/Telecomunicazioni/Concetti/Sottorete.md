---
title: Sottorete
tags:
  - telecomunicazioni
  - concetto
  - ip
  - indirizzamento
---

# Sottorete

> [!summary] In breve
> Una **sottorete** è un'isola di interfacce collegate senza router in mezzo. Si individua "staccando" le interfacce da host e router. Le interfacce di una sottorete condividono il prefisso (es. 223.1.1.0/24).

- `/24` = **maschera di sottorete**: i primi 24 bit identificano la sottorete.
- 223.1.1.0/24 contiene 223.1.1.1–.3 (host) e 223.1.1.4 (router).
- Anche un collegamento **punto a punto** tra due router è una sottorete: 3 router in triangolo con 3 LAN danno **6 sottoreti** (223.1.1/2/3 per le LAN, 223.1.7/8/9 per i collegamenti).
- La "nuvola" può essere uno switch Ethernet o un access point wireless.

## Collegamenti

- **Concetti correlati**: [[Indirizzamento IPv4]] · [[CIDR]] · [[Switch]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Sottoreti|Capitolo 4 — Sottoreti]]
