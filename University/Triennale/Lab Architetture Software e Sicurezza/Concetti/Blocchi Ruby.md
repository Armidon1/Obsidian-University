---
title: Blocchi Ruby
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - ruby
---

# Blocchi Ruby

> [!summary] In breve
> Pezzi di codice passati a un metodo e chiamati da esso, scritti tra graffe o tra do...end, con i parametri tra barre verticali.

```ruby
[1, 2, 3].each { |n| puts "n = #{n}" }
3.times do
  puts "Hello!"
end
```

Sono ovunque in Rails: `create_table ... do |t|`, `transaction do`, `describe ... do` in RSpec.

## Collegamenti

- **Concetti correlati**: [[Ruby]] · [[Range Ruby]] · [[Hash e Simboli Ruby]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[03 - LASS - Ruby Essentials#Blocchi|Lezione 3 — Blocchi]]
> - [[03 - LASS - Ruby Essentials#Cicli|Lezione 3 — Cicli]]
