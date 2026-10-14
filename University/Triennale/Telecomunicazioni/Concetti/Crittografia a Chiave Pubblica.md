---
title: Crittografia a Chiave Pubblica
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - asimmetrica
---

# Crittografia a Chiave Pubblica

> [!summary] In breve
> Ogni utente ha una chiave **pubblica** $K^+$ e una **privata** $K^-$, con $K^-(K^+(m)) = K^+(K^-(m)) = m$. Chiunque può cifrare per Bob con $K_B^+$, ma solo Bob decifra. Non serve un segreto condiviso in anticipo (Diffie-Hellman, 1976).

- Riservatezza: cifrare con la chiave **pubblica** del destinatario.
- Firma: cifrare (l'hash) con la propria chiave **privata**.
- Problemi: lentezza → **chiavi di sessione** simmetriche (cifratura ibrida); chiunque può fingersi Alice → **firma digitale** e **certificati**.
- Algoritmi: **RSA**, Diffie-Hellman (per stabilire chiavi).

## Collegamenti

- **Concetti correlati**: [[Algoritmo RSA]] · [[Firma Digitale]] · [[Certificazione della Chiave Pubblica]] · [[Asymmetric Encryption]] · [[Hybrid Encryption]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Crittografia a chiave pubblica|Capitolo 8 — Crittografia a chiave pubblica]]
