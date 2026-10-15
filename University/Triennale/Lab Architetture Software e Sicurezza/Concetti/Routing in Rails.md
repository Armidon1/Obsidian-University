---
title: Routing in Rails
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - rest
---

# Routing in Rails

> [!summary] In breve
> Il file config/routes.rb associa le route HTTP alle azioni dei controller; resources :movies genera le 7 route RESTful con i relativi helper.

| Helper | Route | Azione |
|---|---|---|
| `movies_path` | `GET /movies` | index |
| `movies_path` | `POST /movies` | create |
| `new_movie_path` | `GET /movies/new` | new |
| `edit_movie_path(m)` | `GET /movies/:id/edit` | edit |
| `movie_path(m)` | `GET /movies/:id` | show |
| `movie_path(m)` | `PUT /movies/:id` | update |
| `movie_path(m)` | `DELETE /movies/:id` | destroy |

- I parametri dell'URI finiscono in `params` (`params[:id]`).
- `bin/rails routes` le elenca tutte.

## Collegamenti

- **Concetti correlati**: [[CRUDI]] · [[REST]] · [[Nested Routes]] · [[Ruby on Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Route di default e CRUDI|Lezione 5 — Route di default e CRUDI]]
> - [[05 - LASS - Rails Parte 1#Il viaggio di una richiesta|Lezione 5 — Il viaggio di una richiesta]]
> - [[06 - LASS - Rails Parte 2#Routes and Controllers|Lezione 6 — Routes and Controllers]]
