---
title: Outside-in Testing
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
  - bdd
  - tdd
---

# Outside-in Testing

> [!summary] In breve
> Si parte da un test di accettazione che fallisce sul comportamento visibile all'utente e si scende verso controller e model scrivendo test sempre più interni.

1. test di **accettazione** che fallisce (Cucumber, interazione con la pagina);
2. test di **integrazione** che fallisce (controller);
3. **unit test** che fallisce (model);
4. codice fino al verde, risalendo.

Due cicli annidati: Cucumber (esterno) e RSpec (interno).

## Collegamenti

- **Concetti correlati**: [[Behavior-Driven Development]] · [[Test-Driven Development]] · [[Unit, Functional e Integration Test]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Outside-in testing in una figura|Lezione 15 — Outside-in testing in una figura]]
> - [[15 - LASS - Testing BDD e TDD#Cucumber e RSpec|Lezione 15 — Cucumber e RSpec]]
