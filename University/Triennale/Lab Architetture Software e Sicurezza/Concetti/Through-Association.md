---
title: Through-Association
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - associazioni
---

# Through-Association

> [!summary] In breve
> Associazione indiretta tra due model passando per un terzo (has_many :movies, through: :reviews), tradotta da Rails in un doppio join.

```ruby
class Moviegoer < ApplicationRecord
  has_many :reviews
  has_many :movies, through: :reviews
end
alice.movies   # i film recensiti da Alice
```

```sql
SELECT movies.* FROM movies
  JOIN reviews ON movies.id = reviews.movie_id
  WHERE reviews.moviegoer_id = 1
```

## Collegamenti

- **Concetti correlati**: [[Associazioni ActiveRecord]] · [[ActiveRecord Query Interface]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[07 - LASS - Rails Parte 3#Through-Associations|Lezione 7 — Through-Associations]]
