---
title: Classi Ruby e Accessor
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - ruby
---

# Classi Ruby e Accessor

> [!summary] In breve
> Le classi Ruby hanno il costruttore initialize e generano getter e setter con attr_accessor / attr_reader, un esempio di metaprogrammazione.

```ruby
class Book
  attr_accessor :isbn      # getter isbn e setter isbn=
  attr_reader :price       # solo getter
  def initialize(isbn, price = 0, *altri)
    @isbn = isbn
    @price = price
  end
end
b = Book.new('x', 10)
b.class        # => Book
b.is_a?(Book)  # => true
```

## Collegamenti

- **Concetti correlati**: [[Ruby]] · [[Tipi di Variabili in Ruby]] · [[Active Record]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[03 - LASS - Ruby Essentials#Classi|Lezione 3 — Classi]]
> - [[03 - LASS - Ruby Essentials#Controllare la classe di un'istanza|Lezione 3 — Controllare la classe di un'istanza]]
