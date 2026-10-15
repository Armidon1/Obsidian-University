---
title: Debugging Rails
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - debugging
---

# Debugging Rails

> [!summary] In breve
> Leggere davvero il messaggio di errore e il backtrace, poi strumentare il codice (debug, inspect, raise, logger) o usare un debugger interattivo.

- **Backtrace**: la catena delle chiamate attive fino all'errore.
- `undefined method 'x' for nil:NilClass` → qualcosa ha restituito `nil`.
- Strumentare: `<%= debug(@movie) %>`, `@movie.inspect`, `raise params.inspect`, `Rails.logger.debug("msg")`.
- Log: `log/development.log`; debugger: `byebug` (Rails 6.1).

## Collegamenti

- **Concetti correlati**: [[Truthy e Falsey]] · [[Ruby on Rails]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#Debugging|Lezione 6 — Debugging]]
> - [[06 - LASS - Rails Parte 2#Backtracing|Lezione 6 — Backtracing]]
> - [[06 - LASS - Rails Parte 2#Instrument|Lezione 6 — Instrument]]
