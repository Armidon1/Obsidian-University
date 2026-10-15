---
title: ActiveRecord Query Interface
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - active-record
  - query
---

# ActiveRecord Query Interface

> [!summary] In breve
> I metodi Active Record per cercare record in modo indipendente dal DBMS: find, first, find_by, where, find_each.

| Metodo | Restituisce | Se non trova |
|---|---|---|
| `find(10)` | oggetto | `RecordNotFound` |
| `first` / `first(3)` | oggetto / array | `nil` / `[]` |
| `find_by(first_name: 'Lifo')` | oggetto | `nil` |
| `find_by!(...)` | oggetto | `RecordNotFound` |
| `where(...)` | relation lazy | relation vuota (truthy) |
| `find_each(batch_size: 1000)` | un record alla volta | — |

Condizioni con hash o `?` sono parametrizzate (no [[SQL Injection]]); mai interpolare stringhe.

## Collegamenti

- **Concetti correlati**: [[Active Record]] · [[Truthy e Falsey]] · [[Prepared Statement]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[07 - LASS - Rails Parte 3#ActiveRecord Query Interface|Lezione 7 — ActiveRecord Query Interface]]
> - [[07 - LASS - Rails Parte 3#find_by|Lezione 7 — find_by]]
> - [[07 - LASS - Rails Parte 3#where|Lezione 7 — where]]
