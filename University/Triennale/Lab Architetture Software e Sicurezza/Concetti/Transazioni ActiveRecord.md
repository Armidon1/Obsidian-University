---
title: Transazioni ActiveRecord
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - database
  - transazioni
---

# Transazioni ActiveRecord

> [!summary] In breve
> Blocchi in cui tutte le modifiche al database riescono insieme o vengono annullate insieme (rollback), per connessione al database e non per model.

```ruby
ActiveRecord::Base.transaction do
  david.withdrawal(100)
  mary.deposit(100)
end   # un'eccezione dentro il blocco → rollback, poi l'eccezione si propaga
```

- Il rollback non ripristina gli oggetti Ruby in memoria.
- `save` e `destroy` sono già in una transazione (con validazioni e callback).
- Non adatte a transazioni distribuite su più database.
- Vedi [[Transazione]] in Basi di Dati.

## Collegamenti

- **Concetti correlati**: [[Active Record]] · [[Associazioni ActiveRecord]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[07 - LASS - Rails Parte 3#Transazioni con oggetti Active Record|Lezione 7 — Transazioni con oggetti Active Record]]
