---
title: GET Condizionale
tags:
  - telecomunicazioni
  - concetto
  - http
  - cache
---

# GET Condizionale

> [!summary] In breve
> È una richiesta `GET` con l'intestazione `If-modified-since:`: il server invia l'oggetto solo se è stato modificato, altrimenti risponde `304 Not Modified` con il corpo vuoto.

```http
GET /fruit/kiwi.gif HTTP/1.1
Host: www.exotiquecuisine.com
If-modified-since: Wed, 9 Sep 2015 09:23:24
```

- Il valore di `If-modified-since:` è il `Last-Modified:` che la cache ha salvato insieme all'oggetto.
- `304 Not Modified` senza corpo: niente banda sprecata, e la cache consegna la sua copia.

## Collegamenti

- **Concetti correlati**: [[Web Caching]] · [[Messaggi HTTP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#GET condizionale|Capitolo 2 — GET condizionale]]
