---
title: Anycast IP
tags:
  - telecomunicazioni
  - concetto
  - bgp
  - dns
  - cdn
---

# Anycast IP

> [!summary] In breve
> Lo **stesso indirizzo IP** viene annunciato con BGP da più server in luoghi diversi; i router trattano gli annunci come percorsi alternativi e consegnano al server **più vicino** secondo BGP.

- Esempio: 212.21.21.21 annunciato da Server CDN A (AS3) e B (AS1); il router 2b sceglie B, più vicino.
- Usato soprattutto dal **DNS**: 13 indirizzi di root server, ognuno servito da molti server nel mondo.
- **Poco usato dalle CDN**: un cambio di instradamento può spostare a metà una connessione TCP su un altro server.
- IPv6 lo prevede nativamente come tipo di indirizzo.

## Collegamenti

- **Concetti correlati**: [[Protocollo BGP]] · [[Gerarchia dei DNS Server]] · [[Content Distribution Network]] · [[Protocollo IPv6]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Anycast IP|Capitolo 5 — Anycast IP]]
