---
title: Certificazione della Chiave Pubblica
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - pki
  - ca
---

# Certificazione della Chiave Pubblica

> [!summary] In breve
> Un'**autorità di certificazione** (CA) verifica l'identità di un'entità ed emette un **certificato** (X.509) che lega la sua chiave pubblica all'identità, **firmato** con la chiave privata della CA. Serve a evitare che qualcuno spacci la propria chiave pubblica per quella di un altro.

- Attacco della pizza: Trudy firma con la sua chiave e allega la sua chiave pubblica dicendo che è di Bob → Alice manda la pizza a Bob.
- Ci si fida della chiave certificata solo se ci si fida della CA e dei suoi controlli (es. "Fly-By-Night").
- Campi X.509: versione, numero seriale, algoritmo di firma, emittente (DN), periodo di validità, soggetto (DN), chiave pubblica del soggetto.
- Standard: ITU X.509, RFC 1422. PGP usa invece una **rete di fiducia**.

## Collegamenti

- **Concetti correlati**: [[Firma Digitale]] · [[Certification Authority (CA)]] · [[PKI]] · [[Posta Elettronica Sicura e PGP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Certificazione della chiave pubblica|Capitolo 8 — Certificazione della chiave pubblica]]
