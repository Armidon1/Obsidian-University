---
title: Protocollo SMTP
tags:
  - telecomunicazioni
  - concetto
  - email
  - livello-applicazione
---

# Protocollo SMTP

> [!summary] In breve
> SMTP (RFC 5321) trasferisce la posta **tra mail server** (e da user agent a mail server) su **TCP, porta 25**. È un protocollo **push**, usa connessioni persistenti e richiede messaggi in ASCII a 7 bit.

Componenti della posta: **user agent**, **mail server** (caselle + coda dei messaggi), **SMTP**.

```text
C: HELO crepes.fr
C: MAIL FROM: <alice@crepes.fr>
C: RCPT TO: <bob@hamburger.edu>
C: DATA
C: ...testo...
C: .
C: QUIT
```

- Connessione **diretta** tra il server del mittente e quello del destinatario, senza server intermedi; se fallisce, si riprova ogni ~30 min.
- Le intestazioni del messaggio (`From:`, `To:`, `Subject:`, RFC 5322) sono diverse dai comandi SMTP.

| | HTTP | SMTP |
| --- | --- | --- |
| Tipo | pull | **push** |
| Codifica | libera | ASCII a 7 bit |
| Oggetti multipli | un messaggio per oggetto | tutto in un messaggio |

## Collegamenti

- **Concetti correlati**: [[POP3 e IMAP]] · [[Protocollo HTTP]] · [[SMTP]] · [[MIME]] · [[Componenti Chiave del Sistema Email]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#2.3 Posta elettronica in Internet|Capitolo 2 — 2.3 Posta elettronica in Internet]]
> - [[02 - TLC - Livello di applicazione#SMTP|Capitolo 2 — SMTP]]
> - [[02 - TLC - Livello di applicazione#Confronto con HTTP|Capitolo 2 — Confronto con HTTP]]
> - [[02 - TLC - Livello di applicazione#Formati dei messaggi di posta|Capitolo 2 — Formati dei messaggi di posta]]
