---
title: Range Ruby
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - ruby
---

# Range Ruby

> [!summary] In breve
> Collezione dei valori tra un inizio e una fine: .. include l'estremo, ... lo esclude; esistono range senza inizio o senza fine.

```ruby
(1..4).to_a    # => [1, 2, 3, 4]
(1...4).to_a   # => [1, 2, 3]
('a'..'c').to_a # => ["a", "b", "c"]
(..4).include?(-50)  # => true
(1..)          # infinito: usare break
```

## Collegamenti

- **Concetti correlati**: [[Ruby]] · [[Blocchi Ruby]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[03 - LASS - Ruby Essentials#Range|Lezione 3 — Range]]
