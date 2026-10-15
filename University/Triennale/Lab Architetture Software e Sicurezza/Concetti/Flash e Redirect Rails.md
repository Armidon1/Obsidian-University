---
title: Flash e Redirect Rails
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - controller
---

# Flash e Redirect Rails

> [!summary] In breve
> Dopo un'azione si fa redirect_to verso una pagina esistente e si passa il messaggio in flash[], che sopravvive esattamente fino alla richiesta successiva.

```ruby
def create
  @movie = Movie.create!(movie_params)
  flash[:notice] = "#{@movie.title} was created."
  redirect_to movies_path      # 302, nuova richiesta GET
end
```

- `flash[:notice]` informativi, `flash[:alert]` errori; si mostrano nel layout.
- Serve perché HTTP è stateless: le variabili d'istanza non sopravvivono al redirect.

## Collegamenti

- **Concetti correlati**: [[Form Tag Helper]] · [[Codici di Stato HTTP]] · [[Don't Repeat Yourself]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[06 - LASS - Rails Parte 2#DRY Redirection and flash[]|Lezione 6 — DRY Redirection and flash[]]]
