---
title: MPLS
tags:
  - telecomunicazioni
  - concetto
  - mpls
  - traffic-engineering
---

# MPLS

> [!summary] In breve
> **Multiprotocol Label Switching**: un'intestazione con un'**etichetta** fissa tra livello 2 e livello 3 permette ai *label-switched router* di inoltrare senza guardare l'IP. Il vero vantaggio è l'**ingegneria del traffico**, insieme al recupero rapido e alle VPN.

- Intestazione: **Etichetta**, Exp (3 bit), S (fine della pila), TTL.
- Tabella: etichetta in → etichetta out, destinazione, interfaccia.
- Esempio: R4 ha due percorsi verso A (etichetta 10 via R3, etichetta 8 via R2) e può dividere il traffico, cosa che l'instradamento IP non permette.
- Distribuzione delle etichette con RSVP-TE; OSPF esteso.
- Usi: **traffic engineering**, ricostruzione rapida dei percorsi, **VPN**. È il "coltellino svizzero".
- Una rete intera vista come un "collegamento": **canale virtuale**.

## Collegamenti

- **Concetti correlati**: [[Inoltro e Instradamento]] · [[OSPF]] · [[Longest Prefix Match]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.5 Canali virtuali: una rete come un livello di collegamento|Capitolo 6 — 6.5 Canali virtuali: una rete come un livello di collegamento]]
> - [[06 - TLC - Livello di collegamento e reti locali#Multiprotocol label switching (MPLS)|Capitolo 6 — Multiprotocol label switching (MPLS)]]
