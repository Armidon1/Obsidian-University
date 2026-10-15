---
title: Bcrypt
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - password
  - crittografia
---

# Bcrypt

> [!summary] In breve
> Funzione di protezione delle password volutamente lenta, con salt casuale e fattore di costo regolabile, basata su Blowfish.

- Salt + fattore di costo + password → chiave → cifra una stringa nota.
- Costo $c$ = $2^c$ iterazioni: si aumenta quando le CPU accelerano.
- Formato: `$2a$12$<salt 22 car.><hash 31 car.>`.
- Alternative: **Argon2** (oggi raccomandato da OWASP, memory-hard), scrypt, PBKDF2.

```ruby
has_secure_password                 # Rails, colonna password_digest
user.authenticate(params[:password])
```

## Collegamenti

- **Concetti correlati**: [[Password Storage]] · [[Salt]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[14 - LASS - Autenticazione#Soluzione 5 - bcrypt con salt|Lezione 14 — Soluzione 5 - bcrypt con salt]]
> - [[14 - LASS - Autenticazione#BCrypt|Lezione 14 — BCrypt]]
