---
title: Funzioni Hash Crittografiche
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - hash
  - integrita
---

# Funzioni Hash Crittografiche

> [!summary] In breve
> Una funzione hash associa a un messaggio di qualsiasi lunghezza una sintesi di lunghezza fissa $H(m)$. Quella **crittografica** deve rendere computazionalmente impossibile trovare $x \ne y$ con $H(x) = H(y)$. Esempi: **MD5** (128 bit) e **SHA-1** (160 bit).

- Il checksum Internet non basta: "IOU100.99BOB" e "IOU900.19BOB" hanno lo stesso checksum `B2 C1 D2 AC`.
- MD5 (RFC 1321): padding, lunghezza a 64 bit, accumulatore, 4 cicli su blocchi di 16 parole da 32 bit.
- SHA-1 (FIPS 1995): standard federale USA.
- Si usano in **MAC**, **firme digitali** e autenticazione.

## Collegamenti

- **Concetti correlati**: [[Codice di Autenticazione del Messaggio]] · [[Firma Digitale]] · [[Checksum Internet]] · [[MD5]] · [[SHA-1]] · [[Hashing]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.3 Integrità dei messaggi e firma digitale|Capitolo 8 — 8.3 Integrità dei messaggi e firma digitale]]
> - [[08 - TLC - Sicurezza nelle reti#Funzioni hash crittografiche|Capitolo 8 — Funzioni hash crittografiche]]
