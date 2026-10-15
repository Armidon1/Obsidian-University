---
title: Embedded Ruby ERB
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - view
---

# Embedded Ruby ERB

> [!summary] In breve
> Il linguaggio di template delle view Rails: HTML con tag <% %> per eseguire Ruby e <%= %> per inserirne il risultato.

```erb
<% @movies.each do |movie| %>
  <p><%= link_to movie.title, movie_path(movie) %></p>
<% end %>
```

- L'azione `index` di `MoviesController` renderizza `app/views/movies/index.html.erb`.
- Le variabili d'istanza del controller sono copiate nella view (metaprogrammazione).
- Il layout `app/views/layouts/application.html.erb` avvolge tutte le view (`yield`).
- `<%= %>` fa l'escaping HTML automatico (difesa da [[Cross-Site Scripting]]).

## Collegamenti

- **Concetti correlati**: [[Model-View-Controller]] · [[View Partial]] · [[Form Tag Helper]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#Controllers and Views|Lezione 6 — Controllers and Views]]
> - [[06 - LASS - Rails Parte 2#HTML|Lezione 6 — HTML]]
