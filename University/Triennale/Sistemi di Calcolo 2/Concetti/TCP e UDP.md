---
title: TCP e UDP
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
  - trasporto
---

# TCP e UDP

> [!summary] In breve
> TCP: affidabile, orientato alla connessione, flusso di byte full duplex con controllo di flusso e congestione. UDP: datagram senza connessione né garanzie, header di 8 byte.

| | TCP | UDP |
| --- | --- | --- |
| Connessione | three-way handshake (SYN, SYN-ACK, ACK) | no |
| Garanzie | consegna, ordine, niente duplicati | nessuna |
| Unità | flusso di byte | datagram |
| Header | 20 byte (porte, seq, ack, flag, window…) | 8 byte (porte, lunghezza, checksum) |
| Usi | web, email, SSH | DNS, streaming, giochi, multicast |

- IP + porta identificano un **processo**; una connessione è la quadrupla (IP client, porta client, IP server, porta server).

## Collegamenti

- **Concetti correlati**: [[Socket]] · [[Protocollo IP]] · [[Modello OSI e TCP-IP]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[06 - SDC2 - Reti di Calcolatori#Livello di trasporto: TCP e UDP|Lezione 6 — Livello di trasporto: TCP e UDP]]
> - [[06 - SDC2 - Reti di Calcolatori#TCP|Lezione 6 — TCP]]
> - [[06 - SDC2 - Reti di Calcolatori#UDP|Lezione 6 — UDP]]
