---
title: Message Passing
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
  - ipc
---

# Message Passing

> [!summary] In breve
> Comunicazione e sincronizzazione con `send(dest, msg)` e `receive(src, msg)`, atomiche; può essere bloccante o no, con indirizzamento diretto o indiretto (mailbox).

| Combinazione | Uso |
| --- | --- |
| send e receive bloccanti | rendezvous, sincronizzazione stretta |
| send non bloccante, receive bloccante | la più utile (server) |
| entrambi non bloccanti | nessuno aspetta |

- Indirizzamento **diretto** (receive esplicita o implicita) o **indiretto** con mailbox: one-to-one, many-to-one (port), one-to-many, many-to-many.
- Messaggio = header (tipo, destinazione, sorgente, lunghezza, controllo) + body.
- Mutua esclusione: una mailbox con un solo messaggio-gettone.
- Nei sistemi distribuiti: Message-Oriented Middleware.

## Collegamenti

- **Concetti correlati**: [[Inter-Process Communication]] · [[Produttore-Consumatore]] · [[Remote Procedure Call]] · [[Middleware]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Scambio di messaggi|Lezione 2 — Scambio di messaggi]]
> - [[02 - SDC2 - Concorrenza#Sincronizzazione|Lezione 2 — Sincronizzazione]]
> - [[02 - SDC2 - Concorrenza#Indirizzamento|Lezione 2 — Indirizzamento]]
> - [[05 - SDC2 - Comunicazione tra Processi#Message passing|Lezione 5 — Message passing]]
> - [[08 - SDC2 - Sistemi Distribuiti#Message passing distribuito|Lezione 8 — Message passing distribuito]]
