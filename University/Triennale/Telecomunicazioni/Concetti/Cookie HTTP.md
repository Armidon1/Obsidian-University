---
title: Cookie HTTP
tags:
  - telecomunicazioni
  - concetto
  - http
  - stato
---

# Cookie HTTP

> [!summary] In breve
> I cookie (RFC 6265) aggiungono uno **stato** sopra HTTP, che non ne ha: il server assegna un ID con `Set-cookie:`, il browser lo salva e lo rimanda in ogni richiesta con `Cookie:`.

Quattro componenti:
1. `Set-cookie: 1678` nella **risposta**;
2. `Cookie: 1678` nelle **richieste** successive;
3. un **file di cookie** sull'host, gestito dal browser;
4. un **database** sul sito.

- Usi: carrello della spesa, raccomandazioni, one-click shopping, sessione dopo il login.
- Problema: la **privacy**, perché il sito può profilare l'utente e vendere le informazioni a terzi.

## Collegamenti

- **Concetti correlati**: [[Protocollo HTTP]] · [[Messaggi HTTP]] · [[Cookie]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Interazione utente-server: i cookie|Capitolo 2 — Interazione utente-server: i cookie]]
