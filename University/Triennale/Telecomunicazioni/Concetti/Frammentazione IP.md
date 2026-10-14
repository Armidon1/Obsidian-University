---
title: Frammentazione IP
tags:
  - telecomunicazioni
  - concetto
  - ip
  - ipv4
  - mtu
---

# Frammentazione IP

> [!summary] In breve
> Se un datagramma supera la **MTU** del collegamento d'uscita, il router IPv4 lo divide in **frammenti**, che vengono riassemblati **solo dall'host di destinazione** con identificatore, flag e offset.

- MTU: Ethernet 1500 byte, alcuni collegamenti geografici 576.
- **Identificatore**: uguale per tutti i frammenti. **Flag**: 1 = ne seguono altri, 0 = ultimo. **Offset**: posizione in unità di 8 byte.
- 4000 byte (3980 di dati) su MTU 1500:

| Frammento | Dati | Offset | Flag |
| --- | --- | --- | --- |
| 1 | 1480 | 0 | 1 |
| 2 | 1480 | 185 | 1 |
| 3 | 1020 | 370 | 0 |

- **IPv6**: niente frammentazione nei router, ma ICMP "packet too big" alla sorgente.

## Collegamenti

- **Concetti correlati**: [[Datagramma IPv4]] · [[Protocollo IPv6]] · [[Segmento TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Frammentazione dei datagrammi IPv4|Capitolo 4 — Frammentazione dei datagrammi IPv4]]
