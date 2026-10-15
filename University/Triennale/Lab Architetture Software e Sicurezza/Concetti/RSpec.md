---
title: RSpec
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
  - rspec
  - tdd
---

# RSpec

> [!summary] In breve
> DSL di testing Ruby: example group con describe/context, example con it, expectation con expect(...).to matcher.

```ruby
describe Movie do
  before(:each) { @m = Movie.new(title: 'X') }
  it 'is valid with a title' do
    expect(@m).to be_valid
  end
  it 'saves' do
    expect { @m.save! }.to change { Movie.count }.by(1)
  end
end
```

- `expect(valore)` per i valori, `expect { blocco }` per gli effetti (`raise_error`, `change`).
- Matcher: `eq`, `be_truthy`, `be_nil`, `be_within().of()`, `match`, `be_xxx` dinamici.
- `rspec-rails`: `get`/`post`, `response`, `render_template`.

## Collegamenti

- **Concetti correlati**: [[Test-Driven Development]] · [[FIRST Unit Test]] · [[Mock e Stub]] · [[Red-Green-Refactor]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#RSpec, un DSL per il testing|Lezione 15 — RSpec, un DSL per il testing]]
> - [[15 - LASS - Testing BDD e TDD#RSpec: struttura|Lezione 15 — RSpec: struttura]]
> - [[15 - LASS - Testing BDD e TDD#Matcher|Lezione 15 — Matcher]]
> - [[15 - LASS - Testing BDD e TDD#Cosa c'è in rspec-rails?|Lezione 15 — Cosa c'è in rspec-rails?]]
