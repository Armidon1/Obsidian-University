---
tags:
  - security
  - web-hacking
  - hacking-exposed
source: "Hacking Exposed 7 — Web Application Hacking"
type: nota
up: "[[Web Application Hacking]]"
---

# Session Management

> [!abstract] In una riga
> Attacchi al **token di sessione** con cui l'app ti riconosce dopo il login.

## Cos'è

HTTP è **stateless**: il server non "ricorda" da solo chi sei tra una richiesta e l'altra. Dopo il login l'app ti rilascia un **token di sessione** (di solito un cookie) che il browser rispedisce a ogni richiesta. Chi ottiene o indovina quel token **diventa te**.

## Attacchi tipici

- **Session hijacking:** rubare il token (spesso via [[XSS]], o sniffing su connessioni non cifrate) e impersonare l'utente.
- **Session fixation:** l'attaccante impone alla vittima un token che già conosce, poi la vittima fa login con quel token.
- **Token prevedibili / deboli:** se il token non è abbastanza casuale si può indovinare → si analizza con il **Sequencer** di [[Burp Suite]].
- **Mancata invalidazione** al logout o dopo scadenza.

## Difese

- Token **lunghi e casuali** (alta entropia).
- Cookie con flag **HttpOnly** (non leggibile da JS → limita il furto via [[XSS]]), **Secure** (solo HTTPS), **SameSite** (limita [[CSRF]]).
- **Rigenerare il token al login** (anti-fixation).
- Timeout di inattività e **invalidazione al logout**.
- TLS ovunque.

## Collegamenti

- ⬆️ [[Web Application Hacking]]
- ↔️ [[Authentication Attacks]] · [[XSS]] (vettore di furto) · [[CSRF]]
