---
title: Messaggi HTTP
tags:
  - telecomunicazioni
  - concetto
  - http
---

# Messaggi HTTP

> [!summary] In breve
> Una richiesta HTTP ha riga di richiesta (metodo, URL, versione), righe di intestazione, riga vuota e corpo. Una risposta ha riga di stato (versione, codice, frase), intestazioni, riga vuota e corpo con l'oggetto.

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr
```

| Metodo | Effetto |
| --- | --- |
| `GET` | richiede un oggetto (i dati di un form possono andare nell'URL) |
| `POST` | invia dati nel corpo |
| `HEAD` | solo le intestazioni, senza oggetto |
| `PUT` / `DELETE` | carica / cancella un oggetto (spesso disabilitati) |

| Codice | Significato |
| --- | --- |
| 200 OK | successo |
| 301 Moved Permanently | nuovo URL in `Location:` |
| 304 Not Modified | risposta a un GET condizionale |
| 400 Bad Request | richiesta non capita |
| 404 Not Found | oggetto inesistente |
| 505 HTTP Version Not Supported | versione non supportata |

- Intestazioni di risposta importanti: `Date`, `Server`, `Last-Modified` (per le cache), `Content-Length`, `Content-Type` (identifica il tipo, non l'estensione).

## Collegamenti

- **Concetti correlati**: [[Protocollo HTTP]] · [[GET Condizionale]] · [[Cookie HTTP]] · [[HTTP Verb Tampering]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Formato dei messaggi HTTP|Capitolo 2 — Formato dei messaggi HTTP]]
> - [[02 - TLC - Livello di applicazione#Messaggio di richiesta HTTP|Capitolo 2 — Messaggio di richiesta HTTP]]
> - [[02 - TLC - Livello di applicazione#Messaggio di risposta HTTP|Capitolo 2 — Messaggio di risposta HTTP]]
