---
title: Active Record
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - active-record
  - orm
---

# Active Record

> [!summary] In breve
> Pattern (e libreria Rails) in cui una classe model corrisponde a una tabella e ogni istanza a una riga, con i metodi CRUD già pronti.

```ruby
class Movie < ApplicationRecord; end   # tabella movies
m = Movie.new(title: 'Inception')      # in memoria
m.save!                                # INSERT
Movie.find(3)                          # SELECT ... WHERE id = 3
m.destroy                              # DELETE
```

- Tabella + ID identificano un'istanza.
- Il marshalling degli attributi è automatico.
- È uno strato di *object-relational mapping*.

## Collegamenti

- **Concetti correlati**: [[Migration Rails]] · [[Associazioni ActiveRecord]] · [[ActiveRecord Query Interface]] · [[Model Validation]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Active Record|Lezione 5 — Active Record]]
> - [[05 - LASS - Rails Parte 1#Usare il model dalla console|Lezione 5 — Usare il model dalla console]]
