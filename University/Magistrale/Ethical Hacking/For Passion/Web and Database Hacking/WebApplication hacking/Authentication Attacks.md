---
tags:
  - security
  - web-hacking
  - hacking-exposed
source: "Hacking Exposed 7 — Web Application Hacking"
type: nota
up: "[[Web Application Hacking]]"
---

# Authentication Attacks

> [!abstract] In una riga
> Attacchi a **come l'applicazione verifica chi sei** (il login).

## Cos'è

L'**autenticazione** risponde alla domanda *"chi sei?"* (≠ [[Authorization|autorizzazione]], che chiede *"cosa puoi fare?"*). Sul web avviene quasi sempre con username + password, idealmente più un secondo fattore. Ogni debolezza in questo meccanismo è un modo per entrare come qualcun altro.

## Attacchi tipici

- **Brute forcing / credential stuffing:** provare molte password (o coppie rubate da altri leak) con tool come **THC-Hydra** ([[Web Hacking Tools]]).
- **Credenziali deboli o di default** (`admin/admin`).
- **Username enumeration:** l'app risponde in modo diverso per utente esistente vs inesistente → l'attaccante scopre gli account validi.
- **Bypass dell'autenticazione:** via [[SQL Injection]] nel form di login o difetti logici.
- **Recupero password insicuro** (domande deboli, token prevedibili).

## Difese

- Policy password robuste e **storage con hashing** moderno (bcrypt/argon2).
- **Account lockout / rate limiting** contro il brute force.
- **MFA** (secondo fattore).
- Messaggi d'errore **generici** ("credenziali non valide", mai "utente inesistente").
- CAPTCHA dopo N tentativi.

## Collegamenti

- ⬆️ [[Web Application Hacking]]
- ↔️ [[Session Management]] (ciò che viene dopo il login) · [[Authorization]] · [[SQL Injection]] (bypass)
