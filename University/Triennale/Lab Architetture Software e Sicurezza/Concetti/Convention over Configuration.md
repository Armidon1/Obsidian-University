---
title: Convention over Configuration
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - principi
---

# Convention over Configuration

> [!summary] In breve
> Rails adotta convenzioni predefinite (nomi di tabelle, classi, file, route) invece di richiedere lunghi file di configurazione.

| Si scrive | Rails deduce |
|---|---|
| `class Movie < ApplicationRecord` | tabella `movies` |
| `resources :movies` | `MoviesController`, 7 azioni |
| azione `index` | view `app/views/movies/index.html.erb` |
| `t.references :movie` | colonna `movie_id` |

Seguendo le convenzioni si scrive pochissimo; andandoci contro si fatica.

## Collegamenti

- **Concetti correlati**: [[Don't Repeat Yourself]] · [[Ruby on Rails]] · [[Active Record]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Convention over Configuration|Lezione 5 — Convention over Configuration]]
