---
title: Password Storage
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - password
---

# Password Storage

> [!summary] In breve
> Le password vanno salvate con una funzione lenta e con salt (bcrypt, Argon2, scrypt, PBKDF2), mai in chiaro né con un hash veloce.

| # | Si salva | Problema |
|---|---|---|
| 1 | `password` | DB rubato = password rubate |
| 2 | `sha1(password)` | hash veloci, [[Rainbow Table]] |
| 3 | `sha1(secret + password)` | segreto unico scopribile |
| 4 | `sha1(salt + password)` | ancora troppo veloce |
| 5 | `bcrypt(salt + password)` | soluzione consigliata |

Lato utente: password lunghe (passphrase), mai riusate, password manager. In Rails: `has_secure_password`.

## Collegamenti

- **Concetti correlati**: [[Salt]] · [[Bcrypt]] · [[Rainbow Table]] · [[Autenticazione]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[14 - LASS - Autenticazione#Password Management|Lezione 14 — Password Management]]
> - [[14 - LASS - Autenticazione#Strategie consigliate|Lezione 14 — Strategie consigliate]]
> - [[14 - LASS - Autenticazione#Password Storage|Lezione 14 — Password Storage]]
