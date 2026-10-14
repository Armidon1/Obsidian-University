---
title: Protocollo UDP
tags:
  - telecomunicazioni
  - concetto
  - livello-trasporto
  - udp
---

# Protocollo UDP

> [!summary] In breve
> UDP (RFC 768) fa il minimo indispensabile: multiplexing con le porte e un checksum. È senza connessione, senza stato, non affidabile, senza controllo di congestione, e ha un'intestazione di 8 byte.

Intestazione: **porta orig · porta dest · lunghezza · checksum** (4 campi da 16 bit).

Perché sceglierlo:
- controllo fine su **cosa e quando** inviare, senza ritardi dovuti alla congestione;
- **nessun handshake**, quindi nessun ritardo iniziale (DNS, QUIC);
- **nessuno stato**, quindi più client per server;
- intestazione di **8 byte** contro 20 di TCP.

Usato da DNS, SNMP, NFS e spesso da multimedia e telefonia. Senza controllo di congestione può **soffocare TCP**. L'affidabilità, se serve, va implementata nell'applicazione (es. QUIC).

## Collegamenti

- **Concetti correlati**: [[Checksum Internet]] · [[Multiplexing e Demultiplexing]] · [[TCP e UDP]] · [[Fairness TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#3.3 Trasporto non orientato alla connessione: UDP|Capitolo 3 — 3.3 Trasporto non orientato alla connessione: UDP]]
> - [[03 - TLC - Livello di trasporto#Perché scegliere UDP invece di TCP|Capitolo 3 — Perché scegliere UDP invece di TCP]]
> - [[03 - TLC - Livello di trasporto#Struttura dei segmenti UDP|Capitolo 3 — Struttura dei segmenti UDP]]
