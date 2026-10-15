---
title: Controller Filter
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - controller
  - autorizzazione
---

# Controller Filter

> [!summary] In breve
> Metodo eseguito prima (o dopo) delle azioni di un controller, che può preparare condizioni comuni o interrompere la richiesta con un redirect.

```ruby
class ApplicationController < ActionController::Base
  before_action :set_current_user            # before_filter fino a Rails 4
  protected
  def set_current_user
    @current_user ||= Moviegoer.find_by(id: session[:user_id])
    redirect_to login_path and return unless @current_user
  end
end
```

- Limitabile con `only:` / `except:`; eseguiti nell'ordine di dichiarazione.
- Validation protegge i **dati**, filter protegge le **azioni** (può cambiare il flusso).
- Usare `find_by` (che restituisce `nil`) e non `where` (relation sempre truthy).

## Collegamenti

- **Concetti correlati**: [[Model Validation]] · [[Missing Function Level Access Control]] · [[Truthy e Falsey]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#Controller Filters|Lezione 6 — Controller Filters]]
> - [[06 - LASS - Rails Parte 2#Controller Filters vs. Model Validation|Lezione 6 — Controller Filters vs. Model Validation]]
