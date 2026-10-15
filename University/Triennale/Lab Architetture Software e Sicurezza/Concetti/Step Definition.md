---
title: Step Definition
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - bdd
  - cucumber
---

# Step Definition

> [!summary] In breve
> Codice Ruby che implementa un passo Gherkin, associato alle frasi degli scenari tramite un'espressione regolare con gruppi di cattura.

```ruby
# features/step_definitions/web_steps.rb
Given /^(?:|I )am on (.+)$/ do |page_name|
  visit path_to(page_name)
end
Then /^I should see "(.*)"$/ do |text|
  expect(page).to have_content(text)
end
```

I gruppi catturati diventano argomenti del blocco; le azioni sul browser le fa [[Capybara]].

## Collegamenti

- **Concetti correlati**: [[Cucumber e Gherkin]] · [[Capybara]] · [[Given When Then]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[08 - LASS - Behavior-Driven Development#Step Definitions|Lezione 8 — Step Definitions]]
> - [[15 - LASS - Testing BDD e TDD#Step e step definition con le regex|Lezione 15 — Step e step definition con le regex]]
