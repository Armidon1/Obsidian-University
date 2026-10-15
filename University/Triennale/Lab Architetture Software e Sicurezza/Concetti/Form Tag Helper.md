---
title: Form Tag Helper
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - view
  - form
---

# Form Tag Helper

> [!summary] In breve
> Metodi Rails che generano form HTML con campi chiamati model[attributo], così che i dati arrivino al controller come hash annidato in params.

```erb
<%= form_tag movies_path, method: :post do %>
  <%= text_field :movie, :title %>        <%# name="movie[title]" %>
  <%= submit_tag 'Save Changes' %>
<% end %>
```

Nel controller: `params[:movie]` → `{"title" => "..."}`. Da Rails 4 va filtrato con le strong parameters: `params.require(:movie).permit(:title, ...)`. I form helper aggiungono anche il token anti-[[Cross-Site Request Forgery|CSRF]].

## Collegamenti

- **Concetti correlati**: [[Embedded Ruby ERB]] · [[Flash e Redirect Rails]] · [[Hash e Simboli Ruby]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#Collecting Data from Users|Lezione 6 — Collecting Data from Users]]
> - [[06 - LASS - Rails Parte 2#Form Tag Helper|Lezione 6 — Form Tag Helper]]
> - [[06 - LASS - Rails Parte 2#Acting on Collected Data|Lezione 6 — Acting on Collected Data]]
