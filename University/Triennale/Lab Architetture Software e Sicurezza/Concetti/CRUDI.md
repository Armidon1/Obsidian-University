---
title: CRUDI
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rest
---

# CRUDI

> [!summary] In breve
> Le cinque operazioni di un'API RESTful su una risorsa: Create, Retrieve, Update, Delete, Index.

| Op. | Route Rails | Azione |
|---|---|---|
| Index | `GET /movies` | index |
| Create | `POST /movies` | create |
| Retrieve | `GET /movies/3` | show |
| Update | `PUT/PATCH /movies/3` | update |
| Delete | `DELETE /movies/3` | destroy |

In Rails le genera tutte la riga `resources :movies`.

## Collegamenti

- **Concetti correlati**: [[REST]] · [[Routing in Rails]] · [[Active Record]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[04 - LASS - SaaS Essentials#CRUDI|Lezione 4 — CRUDI]]
> - [[05 - LASS - Rails Parte 1#Route di default e CRUDI|Lezione 5 — Route di default e CRUDI]]
