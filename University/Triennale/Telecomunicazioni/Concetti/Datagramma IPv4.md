---
title: Datagramma IPv4
tags:
  - telecomunicazioni
  - concetto
  - ip
  - ipv4
---

# Datagramma IPv4

> [!summary] In breve
> Il datagramma IPv4 ha un'intestazione di **20 byte** (senza opzioni) con versione, lunghezze, TOS, campi di frammentazione, **TTL**, **protocollo**, checksum dell'intestazione e indirizzi sorgente/destinazione a 32 bit.

| Campo | Note |
| --- | --- |
| Versione (4) / Lungh. intestazione (4) | di solito 20 byte |
| TOS (8) | priorità; 2 bit per ECN |
| Lunghezza datagramma (16) | max 65.535 byte |
| Identificatore / flag / offset | frammentazione |
| **TTL** (8) | −1 a ogni router, a 0 si scarta |
| **Protocollo** (8) | 6 = TCP, 17 = UDP (collante rete ↔ trasporto) |
| Checksum intestazione (16) | ricalcolato da ogni router |
| Sorgente / destinazione (32 + 32) | — |
| Opzioni | variabili (eliminate in IPv6) |

- Checksum in IP **e** in TCP/UDP: il primo copre solo l'intestazione, e i livelli possono stare in pile diverse.
- TCP + IP senza opzioni = **40 byte** di intestazioni.

## Collegamenti

- **Concetti correlati**: [[Frammentazione IP]] · [[Indirizzamento IPv4]] · [[Protocollo IPv6]] · [[Protocollo IP]] · [[Checksum Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Formato dei datagrammi IPv4|Capitolo 4 — Formato dei datagrammi IPv4]]
