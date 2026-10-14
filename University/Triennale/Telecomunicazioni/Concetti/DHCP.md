---
title: DHCP
tags:
  - telecomunicazioni
  - concetto
  - ip
  - dhcp
  - livello-applicazione
---

# DHCP

> [!summary] In breve
> Il **Dynamic Host Configuration Protocol** (RFC 2131) assegna automaticamente a un host IP, maschera, gateway e DNS locale (plug-and-play). Usa 4 messaggi UDP in broadcast: **discover, offer, request, ACK**.

| Passo | Da → a | Note |
| --- | --- | --- |
| DHCP **discover** | 0.0.0.0:68 → 255.255.255.255:67 | il client non ha ancora un IP |
| DHCP **offer** | server:67 → 255.255.255.255:68 | `yiaddr` proposto, maschera, **lease time**; possono rispondere più server |
| DHCP **request** | 0.0.0.0:68 → 255.255.255.255:67 | sceglie un'offerta |
| DHCP **ACK** | server:67 → 255.255.255.255:68 | conferma |

- Indirizzo **persistente** o **temporaneo**; la concessione si può rinnovare.
- **Agente di relay** (nel router) per le sottoreti senza server.
- Limite: cambiando sottorete cambia l'IP, e la connessione TCP non sopravvive.

## Collegamenti

- **Concetti correlati**: [[Indirizzamento IPv4]] · [[NAT]] · [[Gateway]] · [[Gerarchia dei DNS Server]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Come ottenere l'indirizzo di un host: DHCP|Capitolo 4 — Come ottenere l'indirizzo di un host: DHCP]]
