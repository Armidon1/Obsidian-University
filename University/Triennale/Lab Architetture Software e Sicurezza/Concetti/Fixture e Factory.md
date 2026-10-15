---
title: Fixture e Factory
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
---

# Fixture e Factory

> [!summary] In breve
> Due modi di avere oggetti veri nei test: le fixture precaricano dati statici nel database, le factory creano solo ciò che serve a ogni test.

| | Fixture | Factory |
|---|---|---|
| Come | `spec/fixtures/movies.yml`, ricaricate prima di ogni spec | `FactoryBot.create(:movie, ...)` nel test |
| Pro | dati statici, tutto in un posto | indipendenza tra test |
| Contro | dipendenze nascoste dai dati | un po' più di codice |

## Collegamenti

- **Concetti correlati**: [[Mock e Stub]] · [[RSpec]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Fixtures and Factories|Lezione 15 — Fixtures and Factories]]
> - [[15 - LASS - Testing BDD e TDD#Fixtures|Lezione 15 — Fixtures]]
