---
title: Model Validation
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - active-record
  - validazione
---

# Model Validation

> [!summary] In breve
> Regole dichiarate nel model e controllate da valid? prima di ogni salvataggio; sono un caso particolare delle lifecycle callback di Active Record.

```ruby
class Movie < ApplicationRecord
  validates :title, presence: true
  validates :rating, inclusion: { in: %w[G PG PG-13 R NC-17] }, unless: :grandfathered?
  validate :released_1930_or_later      # validatore personalizzato
  before_save :capitalize_title         # callback
end
m.valid?; m.errors.full_messages
```

Ordine al salvataggio: `before_validation` → validazioni → `after_validation` → `before_save` → `before_create/update` → SQL → `after_create/update` → `after_save`. La regola vale ovunque il model venga salvato.

## Collegamenti

- **Concetti correlati**: [[Active Record]] · [[Controller Filter]] · [[Don't Repeat Yourself]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#Model Validation|Lezione 6 — Model Validation]]
> - [[06 - LASS - Rails Parte 2#Le lifecycle callback|Lezione 6 — Le lifecycle callback]]
