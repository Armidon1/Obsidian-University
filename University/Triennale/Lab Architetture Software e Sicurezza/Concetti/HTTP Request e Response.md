---
title: HTTP Request e Response
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - http
  - saas
---

# HTTP Request e Response

> [!summary] In breve
> HTTP è il protocollo richiesta/risposta del web: il client apre una connessione TCP e invia metodo, URI, header e body; il server risponde con codice di stato, header e body.

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu

HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

- È **stateless**: lo stato si aggiunge con i [[Cookie HTTP]].
- Porta 80 (HTTP), 443 (HTTPS = HTTP su TLS).
- Approfondimento: [[Protocollo HTTP]], [[Messaggi HTTP]].

## Collegamenti

- **Concetti correlati**: [[Route HTTP e URI]] · [[Codici di Stato HTTP]] · [[Cookie HTTP]] · [[REST]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[04 - LASS - SaaS Essentials#HTTP|Lezione 4 — HTTP]]
> - [[04 - LASS - SaaS Essentials#Struttura di richiesta e risposta|Lezione 4 — Struttura di richiesta e risposta]]
> - [[04 - LASS - SaaS Essentials#HTTP è stateless: i cookie|Lezione 4 — HTTP è stateless: i cookie]]
