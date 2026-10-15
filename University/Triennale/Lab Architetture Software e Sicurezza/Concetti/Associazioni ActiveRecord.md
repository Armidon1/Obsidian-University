---
title: Associazioni ActiveRecord
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - active-record
  - associazioni
---

# Associazioni ActiveRecord

> [!summary] In breve
> belongs_to e has_many traducono le foreign key in riferimenti diretti tra oggetti, generando metodi come movie.reviews e review.movie.

```ruby
class Review < ApplicationRecord
  belongs_to :movie          # colonna movie_id
  belongs_to :moviegoer
end
class Movie < ApplicationRecord
  has_many :reviews, dependent: :destroy
end
inception.reviews << Review.new(potatoes: 4)   # imposta movie_id
review.movie                                    # singolare: un oggetto
```

- `belongs_to` sta sul model con la foreign key (`t.references`).
- Opzioni: validazioni sugli associati (`validates_associated`), `dependent: :destroy`.
- Vedi [[Foreign Key]] e [[Join]] in Basi di Dati.

## Collegamenti

- **Concetti correlati**: [[Through-Association]] · [[Active Record]] · [[Nested Routes]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[07 - LASS - Rails Parte 3#Associations|Lezione 7 — Associations]]
> - [[07 - LASS - Rails Parte 3#ActiveRecord Associations|Lezione 7 — ActiveRecord Associations]]
> - [[07 - LASS - Rails Parte 3#Opzioni delle associazioni|Lezione 7 — Opzioni delle associazioni]]
