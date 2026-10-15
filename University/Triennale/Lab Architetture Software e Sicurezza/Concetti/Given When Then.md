---
title: Given When Then
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - bdd
  - cucumber
---

# Given When Then

> [!summary] In breve
> Struttura di ogni scenario: Given porta il sistema in uno stato noto, When descrive un'azione, Then verifica il risultato atteso con un'asserzione.

| User story | Scenario |
|---|---|
| As a [ruolo] | Given [ruolo e suo stato] |
| I want [obiettivo] | When [evento/azione] |
| so that [beneficio] | Then [beneficio verificabile] |

- Preferibilmente un solo `When` per scenario.
- `And`/`But` estendono il passo precedente; per Cucumber sono tutti alias.

## Collegamenti

- **Concetti correlati**: [[Cucumber e Gherkin]] · [[User Story]] · [[Step Definition]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[08 - LASS - Behavior-Driven Development#Example / Scenario|Lezione 8 — Example / Scenario]]
> - [[08 - LASS - Behavior-Driven Development#Step: Given|Lezione 8 — Step: Given]]
> - [[08 - LASS - Behavior-Driven Development#Step: When|Lezione 8 — Step: When]]
> - [[08 - LASS - Behavior-Driven Development#Step: Then|Lezione 8 — Step: Then]]
> - [[15 - LASS - Testing BDD e TDD#BDD (Behavior-Driven Development)|Lezione 15 — BDD (Behavior-Driven Development)]]
