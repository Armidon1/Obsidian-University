---
title: Firma Digitale
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - firma
  - integrita
---

# Firma Digitale

> [!summary] In breve
> Bob firma calcolando $K_B^-(H(m))$, cioè cifrando l'hash con la propria **chiave privata**. Chiunque verifica confrontando $K_B^+(\text{firma})$ con $H(m)$. È **verificabile** e **non falsificabile**, e garantisce anche l'integrità.

- Solo Bob conosce $K_B^-$; la chiave pubblica non aiuta a scoprirla.
- Si firma l'**hash**, non tutto il messaggio, perché costa meno.

| | MAC | Firma digitale |
| --- | --- | --- |
| Base | chiave condivisa | chiave privata |
| Crittografia | nessuna | a chiave pubblica |
| Richiede | — | **PKI**, CA |

- Usata in PGP e nei **certificati**.

## Collegamenti

- **Concetti correlati**: [[Crittografia a Chiave Pubblica]] · [[Codice di Autenticazione del Messaggio]] · [[Certificazione della Chiave Pubblica]] · [[PKI]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Firme digitali|Capitolo 8 — Firme digitali]]
