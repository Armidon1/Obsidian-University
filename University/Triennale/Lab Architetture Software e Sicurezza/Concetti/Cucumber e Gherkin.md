---
title: Cucumber e Gherkin
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - bdd
  - testing
  - cucumber
---

# Cucumber e Gherkin

> [!summary] In breve
> Gherkin è la grammatica strutturata in cui si scrivono feature e scenari (.feature); Cucumber li esegue come test di accettazione e di integrazione.

```gherkin
Feature: User can manually add movie
  Background:
    Given I am on the RottenPotatoes home page
  Scenario: Add a movie
    When I follow "Add new movie"
    And I fill in "Title" with "Men In Black"
    And I press "Save Changes"
    Then I should see "Men In Black"
```

- Keyword: `Feature`, `Rule`, `Scenario`/`Example`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`.
- 1 feature per user story, ≥1 scenari, 3–8 step; happy e sad path.
- Colori: verde passato, giallo non implementato, rosso fallito, blu saltato.

## Collegamenti

- **Concetti correlati**: [[Given When Then]] · [[Step Definition]] · [[Capybara]] · [[Behavior-Driven Development]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[08 - LASS - Behavior-Driven Development#Formulation - Cucumber|Lezione 8 — Formulation - Cucumber]]
> - [[08 - LASS - Behavior-Driven Development#Struttura di Gherkin|Lezione 8 — Struttura di Gherkin]]
> - [[15 - LASS - Testing BDD e TDD#Cucumber e Capybara|Lezione 15 — Cucumber e Capybara]]
> - [[15 - LASS - Testing BDD e TDD#Dal rosso al verde|Lezione 15 — Dal rosso al verde]]
