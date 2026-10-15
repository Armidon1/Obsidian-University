---
title: Mock e Stub
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
  - tdd
---

# Mock e Stub

> [!summary] In breve
> Seam per isolare il codice sotto test: lo stub sostituisce un metodo con una risposta preconfezionata, il mock è un oggetto controfigura che può verificare le chiamate.

```ruby
# RSpec 3
allow(Movie).to receive(:find_in_tmdb).and_return(fake_results)   # stub
expect(Movie).to receive(:find_in_tmdb).with('hardware')          # aspettativa
movie = double('Movie', title: 'Rambo')                           # mock
```

- Unit test: **stub vicino** (massimo isolamento); integration test: **stub lontano** (più interfacce testate).
- Per testare i metodi del model serve l'oggetto vero ([[Fixture e Factory]]).

## Collegamenti

- **Concetti correlati**: [[FIRST Unit Test]] · [[Fixture e Factory]] · [[RSpec]] · [[Unit, Functional e Integration Test]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Mocks and Stubs|Lezione 15 — Mocks and Stubs]]
> - [[15 - LASS - Testing BDD e TDD#Due nuovi concetti di seam|Lezione 15 — Due nuovi concetti di seam]]
> - [[15 - LASS - Testing BDD e TDD#Dove fare lo stub in una Service Oriented Architecture?|Lezione 15 — Dove fare lo stub in una Service Oriented Architecture?]]
