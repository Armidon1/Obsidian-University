---
title: Capybara
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
  - cucumber
---

# Capybara

> [!summary] In breve
> Libreria Ruby che simula un utente in un browser (visita pagine, compila form, clicca), usata da Cucumber per eseguire gli scenari.

```ruby
visit '/movies/new'
fill_in 'Title', with: 'Men In Black'
click_button 'Save Changes'
expect(page).to have_content('Men In Black')
```

Driver: **Rack::Test** (veloce, senza JavaScript) o **Selenium** (browser vero, anche headless).

## Collegamenti

- **Concetti correlati**: [[Cucumber e Gherkin]] · [[Step Definition]] · [[RSpec]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Capybara, un utente finto|Lezione 15 — Capybara, un utente finto]]
> - [[15 - LASS - Testing BDD e TDD#Cucumber testing stacks|Lezione 15 — Cucumber testing stacks]]
> - [[08 - LASS - Behavior-Driven Development#Step: When|Lezione 8 — Step: When]]
