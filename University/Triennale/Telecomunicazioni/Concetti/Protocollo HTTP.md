---
title: Protocollo HTTP
tags:
  - telecomunicazioni
  - concetto
  - livello-applicazione
  - http
  - web
---

# Protocollo HTTP

> [!summary] In breve
> HTTP è il protocollo applicativo del Web: un client (browser) richiede **oggetti** identificati da URL a un server, con messaggi di richiesta e risposta in testo ASCII su **TCP, porta 80**. È **senza stato**: il server non ricorda i client.

- Una pagina web è fatta di oggetti: un file HTML principale più gli oggetti che referenzia.
- URL = **host** + **percorso** (`www.someSchool.edu` + `/someDepartment/picture.gif`).
- Si appoggia a TCP, quindi non deve gestire perdite e riordini.
- **Stateless**: per "ricordare" gli utenti servono i cookie.
- Versioni: HTTP/1.0 (RFC 1945), HTTP/1.1 (RFC 2616, persistente con pipelining), **HTTP/2** (RFC 7540, richieste intercalate e priorità).

## Collegamenti

- **Concetti correlati**: [[Messaggi HTTP]] · [[Connessioni Persistenti e Non Persistenti]] · [[Cookie HTTP]] · [[Web Caching]] · [[HTTP]] · [[HTTP-2]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Panoramica di HTTP|Capitolo 2 — Panoramica di HTTP]]
