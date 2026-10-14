---
title: Protocollo IPv6
tags:
  - telecomunicazioni
  - concetto
  - ip
  - ipv6
---

# Protocollo IPv6

> [!summary] In breve
> IPv6 ha indirizzi a **128 bit**, un'intestazione **fissa di 40 byte**, l'etichetta di flusso e gli indirizzi anycast. **Elimina** frammentazione nei router, checksum dell'intestazione e opzioni. La transizione da IPv4 avviene con il **tunneling**.

| IPv4 | IPv6 |
| --- | --- |
| 32 bit | 128 bit |
| intestazione da 20 byte + opzioni | 40 byte fissi |
| TOS | classe di traffico + etichetta di flusso (20 bit) |
| TTL | limite di hop |
| protocollo | intestazione successiva |
| frammentazione nei router | no: ICMP "packet too big" |
| checksum intestazione | no (ridondante) |

- **Tunneling**: il datagramma IPv6 viaggia dentro un datagramma IPv4 tra due nodi IPv6 (B→E); il campo protocollo vale **41**.
- Ultimo blocco IPv4 allocato da IANA: febbraio 2011.
- Lezione: cambiare il livello di rete è come cambiare le fondamenta di una casa.

## Collegamenti

- **Concetti correlati**: [[Datagramma IPv4]] · [[Frammentazione IP]] · [[IPv6]] · [[Storia di Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#IPv6|Capitolo 4 — IPv6]]
> - [[04 - TLC - Livello di rete - piano dei dati#Cambiamenti principali|Capitolo 4 — Cambiamenti principali]]
> - [[04 - TLC - Livello di rete - piano dei dati#Passaggio da IPv4 a IPv6|Capitolo 4 — Passaggio da IPv4 a IPv6]]
