---
title: REST
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rest
  - saas
---

# REST

> [!summary] In breve
> REpresentational State Transfer: stile architetturale (non uno standard) in cui le entità sono risorse e ogni richiesta HTTP contiene tutto ciò che serve a identificare risorsa e azione.

- Risorse con un **ID permanente**, operazioni [[CRUDI]].
- Route RESTful = metodo HTTP + URI (`GET /movies/3`).
- **Stateless**: nessuna dipendenza implicita dalle richieste precedenti (`GET /user/301/cart` invece di `GET /cart`).
- Progettare pensando alle **risorse**, non alle azioni dell'utente.
- REST non è autorizzazione: il server deve comunque controllare chi chiede cosa ([[Insecure Direct Object Reference]]).

## Collegamenti

- **Concetti correlati**: [[CRUDI]] · [[Route HTTP e URI]] · [[API]] · [[Routing in Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[04 - LASS - SaaS Essentials#REST|Lezione 4 — REST]]
> - [[04 - LASS - SaaS Essentials#RESTful URI|Lezione 4 — RESTful URI]]
> - [[04 - LASS - SaaS Essentials#RESTful design|Lezione 4 — RESTful design]]
