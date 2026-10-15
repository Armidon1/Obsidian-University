---
title: Nested Routes
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - rest
---

# Nested Routes

> [!summary] In breve
> Route annidate che esprimono RESTfully una risorsa contenuta in un'altra, come le recensioni di un film: /movies/:movie_id/reviews/:id.

```ruby
resources :movies do
  resources :reviews
end
```

- `:movie_id` = risorsa proprietaria, `:id` = la recensione.
- Helper: `movie_reviews_path(m)`, `movie_review_path(m, r)`, `new_movie_review_path(m)`.
- Evita di ricordare il film in `session[]` (che non sarebbe RESTful); nel controller un filtro verifica che il film esista.

## Collegamenti

- **Concetti correlati**: [[Routing in Rails]] · [[Associazioni ActiveRecord]] · [[REST]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[07 - LASS - Rails Parte 3#RESTful Routes for Associations|Lezione 7 — RESTful Routes for Associations]]
