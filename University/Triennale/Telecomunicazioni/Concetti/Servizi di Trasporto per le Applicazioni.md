---
title: Servizi di Trasporto per le Applicazioni
tags:
  - telecomunicazioni
  - concetto
  - livello-applicazione
  - trasporto
---

# Servizi di Trasporto per le Applicazioni

> [!summary] In breve
> Un'applicazione sceglie il protocollo di trasporto in base a quattro servizi: **affidabilità**, **throughput**, **temporizzazione** e **sicurezza**. Internet offre TCP e UDP, e nessuno dei due garantisce throughput o tempi.

| | TCP | UDP |
| --- | --- | --- |
| Connessione | sì (handshake, full-duplex) | no |
| Affidabilità | sì: senza errori, perdite o duplicati, in ordine | no |
| Controllo di congestione | sì | no |
| Throughput / tempi garantiti | no | no |
| Sicurezza | con **SSL** (a livello applicativo) | no |

- Applicazioni **loss-tolerant** (audio/video) contro applicazioni che richiedono affidabilità (file, posta, web).
- Applicazioni **sensibili alla banda** contro applicazioni **elastiche**.
- Web, posta e file usano TCP; la telefonia usa spesso UDP, con TCP come riserva per i firewall.

## Collegamenti

- **Concetti correlati**: [[TCP e UDP]] · [[Architetture Client-Server e P2P]] · [[Socket UDP e TCP in Python]] · [[HTTPS]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Servizi di trasporto disponibili per le applicazioni|Capitolo 2 — Servizi di trasporto disponibili per le applicazioni]]
> - [[02 - TLC - Livello di applicazione#Servizi di trasporto offerti da Internet|Capitolo 2 — Servizi di trasporto offerti da Internet]]
