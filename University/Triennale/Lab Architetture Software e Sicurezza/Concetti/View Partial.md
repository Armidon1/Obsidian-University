---
title: View Partial
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - view
---

# View Partial

> [!summary] In breve
> Frammento di view riutilizzabile, salvato in un file che inizia con underscore e incluso con render.

```erb
<%# app/views/movies/_movie.html.erb %>
<div class="row"><%= link_to movie.title, movie_path(movie) %></div>

<%# in index.html.erb %>
<%= render partial: 'movie', collection: @movies %>
```

Con `collection:` il partial viene renderizzato una volta per elemento, con la variabile locale `movie`. Ha accesso alle variabili d'istanza della view.

## Collegamenti

- **Concetti correlati**: [[Embedded Ruby ERB]] · [[Don't Repeat Yourself]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#View Partials|Lezione 6 — View Partials]]
