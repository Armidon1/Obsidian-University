---
title: Ruby on Rails
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
---

# Ruby on Rails

> [!summary] In breve
> Framework web lato server scritto in Ruby, opinionated, basato su MVC, DRY e Convention over Configuration.

- Mappa le route HTTP sulle azioni dei controller e genera HTML con le view.
- `rails new app`, `bin/rails server` (porta 3000), `bin/rails console`, `bin/rails generate model ...`.
- Cartelle principali: `app/` (model, view, controller), `config/` (route, database), `db/` (schema, migration), `Gemfile`.
- Un'app Rails è una collezione di **risorse RESTful**, ognuna con model, view e controller.

## Collegamenti

- **Concetti correlati**: [[Don't Repeat Yourself]] · [[Convention over Configuration]] · [[Active Record]] · [[Model-View-Controller]] · [[Routing in Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Rails|Lezione 5 — Rails]]
> - [[05 - LASS - Rails Parte 1#Creare un'app Rails di prova|Lezione 5 — Creare un'app Rails di prova]]
> - [[05 - LASS - Rails Parte 1#Contenuto di un'app Rails|Lezione 5 — Contenuto di un'app Rails]]
