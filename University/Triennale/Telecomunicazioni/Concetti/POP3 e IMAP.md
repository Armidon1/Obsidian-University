---
title: POP3 e IMAP
tags:
  - telecomunicazioni
  - concetto
  - email
  - livello-applicazione
---

# POP3 e IMAP

> [!summary] In breve
> Sono i protocolli di **accesso alla posta**, che servono perché SMTP è push e non permette al destinatario di "tirare" i messaggi. **POP3** è semplice e senza stato tra sessioni; **IMAP** gestisce cartelle sul server e conserva lo stato.

| | POP3 (RFC 1939) | IMAP (RFC 3501) |
| --- | --- | --- |
| Porta | 110 | — |
| Fasi | autorizzazione (`user`, `pass` in chiaro) → transazione (`list`, `retr`, `dele`) → aggiornamento (`quit`) | — |
| Cartelle | solo locali | **sul server** (INBOX + cartelle utente) |
| Stato tra sessioni | no | **sì** |
| Parti di un messaggio | no | sì (es. solo l'intestazione) |
| Complessità | bassa | alta |

- POP3 "scarica e cancella" sparpaglia la posta tra le macchine; "scarica e mantieni" no.
- **Webmail**: browser ↔ server via HTTP; tra i server si usa comunque SMTP.

## Collegamenti

- **Concetti correlati**: [[Protocollo SMTP]] · [[IMAP]] · [[POP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Protocolli di accesso alla posta|Capitolo 2 — Protocolli di accesso alla posta]]
> - [[02 - TLC - Livello di applicazione#POP3|Capitolo 2 — POP3]]
> - [[02 - TLC - Livello di applicazione#IMAP|Capitolo 2 — IMAP]]
> - [[02 - TLC - Livello di applicazione#Posta basata sul Web|Capitolo 2 — Posta basata sul Web]]
