---
title: Route HTTP e URI
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - http
  - rest
---

# Route HTTP e URI

> [!summary] In breve
> Una route è la coppia metodo HTTP + URI; l'URI si compone di scheme, host, porta, path, query e fragment.

`GET http://srch.com:80/main/search?q=cloud&lang=en#top`

| scheme | host | port | path | query | fragment |
|---|---|---|---|---|---|
| http | srch.com | 80 | /main/search | q=cloud&lang=en | top |

- `GET` legge senza effetti collaterali; `POST`, `PUT`, `PATCH`, `DELETE` modificano.
- Parametri: nell'URI (pochi), nel body (dati complessi o richieste che cambiano lo stato), raramente negli header.

## Collegamenti

- **Concetti correlati**: [[HTTP Request e Response]] · [[REST]] · [[Routing in Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[04 - LASS - SaaS Essentials#HTTP Route|Lezione 4 — HTTP Route]]
> - [[04 - LASS - SaaS Essentials#Come si scambiano parametri e dati|Lezione 4 — Come si scambiano parametri e dati]]
