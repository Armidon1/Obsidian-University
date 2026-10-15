---
title: Truthy e Falsey
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - ruby
---

# Truthy e Falsey

> [!summary] In breve
> In Ruby solo nil e false sono falsi in una condizione; tutto il resto, compresi 0, "" e [], è vero.

```ruby
if 0  then puts "vero" end   # stampa "vero"
if [] then puts "vero" end   # stampa "vero"
if nil then puts "mai" end   # non stampa
```

- `nil` indica anche "nessun valore": l'errore `undefined method for nil:NilClass` nasce da un `nil` inatteso.
- Attenzione in Rails: una relation vuota (`Movie.where(...)`) è **truthy**.

## Collegamenti

- **Concetti correlati**: [[Ruby]] · [[ActiveRecord Query Interface]] · [[Debugging Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[03 - LASS - Ruby Essentials#Condizioni, truthy e falsey|Lezione 3 — Condizioni, truthy e falsey]]
> - [[06 - LASS - Rails Parte 2#Controller Filters|Lezione 6 — Controller Filters]]
