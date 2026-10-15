---
title: Hash e Simboli Ruby
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - ruby
---

# Hash e Simboli Ruby

> [!summary] In breve
> Gli hash sono dizionari chiave → valore; le chiavi sono spesso simboli (:nome), stringhe immutabili e uniche.

```ruby
h = {foo: 0, :bar => 1}   # foo: 0 è la forma breve di :foo => 0
h[:foo]                   # => 0
h.delete(:bar)
{'baz': 2}                # chiave :baz (simbolo!), non "baz"
```

Se l'ultimo argomento di un metodo è un hash, le graffe si omettono: `validates :title, presence: true`. In Rails `params` è un hash (annidato).

## Collegamenti

- **Concetti correlati**: [[Ruby]] · [[Blocchi Ruby]] · [[Form Tag Helper]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[03 - LASS - Ruby Essentials#Hash|Lezione 3 — Hash]]
> - [[03 - LASS - Ruby Essentials#Extras|Lezione 3 — Extras]]
