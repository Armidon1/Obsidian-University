---
title: Posta Elettronica Sicura e PGP
tags:
  - telecomunicazioni
  - concetto
  - email
  - sicurezza
  - pgp
---

# Posta Elettronica Sicura e PGP

> [!summary] In breve
> Per una mail riservata, autenticata e integra Alice firma $H(m)$ con la propria chiave privata, cifra messaggio e firma con una **chiave di sessione** $K_S$ e cifra $K_S$ con la chiave pubblica di Bob. **PGP** (Zimmermann, 1991) implementa questo schema.

```text
Alice:  [ m + K_A^-(H(m)) ] cifrato con K_S   +   K_B^+(K_S)
Bob:    K_B^-(·) → K_S → decifra → verifica la firma con K_A^+
```

- Alice usa la crittografia a chiave pubblica due volte (firma, chiave di sessione), e Bob pure.
- PGP: MD5/SHA, CAST/3DES/IDEA, RSA; coppia di chiavi con la privata protetta da password; messaggi firmati o segreti.
- Certificazione con una **rete di fiducia** invece che con una CA.

## Collegamenti

- **Concetti correlati**: [[Firma Digitale]] · [[Crittografia a Chiave Pubblica]] · [[PGP]] · [[Protocollo SMTP]] · [[Web of Trust (WoT)]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#E-mail sicure|Capitolo 8 — E-mail sicure]]
> - [[08 - TLC - Sicurezza nelle reti#PGP|Capitolo 8 — PGP]]
