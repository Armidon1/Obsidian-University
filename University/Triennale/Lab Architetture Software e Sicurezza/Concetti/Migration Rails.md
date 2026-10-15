---
title: Migration Rails
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - active-record
  - database
---

# Migration Rails

> [!summary] In breve
> Script Ruby versionato che crea o modifica lo schema del database, mantenendo allineati gli ambienti development, test e production.

```ruby
class CreateMovies < ActiveRecord::Migration[6.1]
  def change
    create_table 'movies' do |t|
      t.string 'title'
      t.datetime 'release_date'
      t.timestamps            # created_at, updated_at
    end
  end
end
```

- `bin/rails generate migration CreateMovies`, poi `bin/rake db:migrate`.
- `bin/rails generate model Movie title:string` crea model e migration insieme.
- La colonna `id` è automatica; da Rails 5 la versione `[6.1]` è obbligatoria.

## Collegamenti

- **Concetti correlati**: [[Active Record]] · [[Ruby on Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Active Record e migration|Lezione 5 — Active Record e migration]]
> - [[05 - LASS - Rails Parte 1#Creare il model e la migration|Lezione 5 — Creare il model e la migration]]
> - [[05 - LASS - Rails Parte 1#Tutto in un comando|Lezione 5 — Tutto in un comando]]
