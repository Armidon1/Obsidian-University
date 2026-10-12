---
title: Protocollo IP
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
---

# Protocollo IP

> [!summary] In breve
> Livello rete di Internet: indirizzamento omogeneo (32 bit in IPv4, net-id + host-id) e routing dei datagram, senza connessione e best effort.

- I pacchetti possono perdersi, arrivare fuori ordine, essere duplicati o ritardati.
- Frammentazione e riassemblaggio; ARP per gli indirizzi MAC.
- Classi storiche: A (`0`, /8), B (`10`, /16), C (`110`, /24), D multicast, E riservata; oggi CIDR.
- Header da 20 byte: versione, IHL, TOS, lunghezza, frammentazione, **TTL**, protocollo (6 TCP, 17 UDP), checksum, IP sorgente e destinazione.

## Collegamenti

- **Concetti correlati**: [[Modello OSI e TCP-IP]] · [[ARP]] · [[TCP e UDP]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[06 - SDC2 - Reti di Calcolatori#IP|Lezione 6 — IP]]
> - [[06 - SDC2 - Reti di Calcolatori#Indirizzi IP (IPv4)|Lezione 6 — Indirizzi IP (IPv4)]]
> - [[06 - SDC2 - Reti di Calcolatori#Il pacchetto IP|Lezione 6 — Il pacchetto IP]]
