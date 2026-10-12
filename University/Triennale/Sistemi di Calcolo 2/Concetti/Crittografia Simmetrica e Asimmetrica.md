---
title: Crittografia Simmetrica e Asimmetrica
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sicurezza
  - crittografia
---

# Crittografia Simmetrica e Asimmetrica

> [!summary] In breve
> Simmetrica: una chiave condivisa (DES, 3DES, AES), veloce. Asimmetrica: chiave pubblica e privata (RSA, ECC, Diffie-Hellman), per confidenzialità e firme. Hash: impronta di lunghezza fissa, one-way e resistente alle collisioni.

- Forza bruta: ogni bit di chiave raddoppia il tempo (DES a 56 bit: ore; AES a 128 bit: impossibile).
- Cifrari a blocchi (ECB, …) e a flusso (XOR con un keystream).
- Confidenzialità: cifrare con la **pubblica** del destinatario. Autenticazione/firma: cifrare con la **privata** del mittente.
- MAC: tag calcolato con una chiave condivisa. Hash: SHA-256/512 (SHA-1 superato).
- **Certificato**: la CA firma (identità, chiave pubblica). **Busta digitale**: messaggio cifrato con una chiave simmetrica casuale, chiave cifrata con la pubblica del destinatario.

## Collegamenti

- **Concetti correlati**: [[Triade CIA]] · [[Autenticazione e Controllo degli Accessi]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[10 - SDC2 - Sicurezza#Crittografia simmetrica|Lezione 10 — Crittografia simmetrica]]
> - [[10 - SDC2 - Sicurezza#Crittografia a chiave pubblica|Lezione 10 — Crittografia a chiave pubblica]]
> - [[10 - SDC2 - Sicurezza#Funzioni hash sicure|Lezione 10 — Funzioni hash sicure]]
> - [[10 - SDC2 - Sicurezza#Certificati a chiave pubblica|Lezione 10 — Certificati a chiave pubblica]]
> - [[10 - SDC2 - Sicurezza#Buste digitali|Lezione 10 — Buste digitali]]
