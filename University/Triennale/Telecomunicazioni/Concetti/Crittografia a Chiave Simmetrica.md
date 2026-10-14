---
title: Crittografia a Chiave Simmetrica
tags:
  - telecomunicazioni
  - concetto
  - crittografia
---

# Crittografia a Chiave Simmetrica

> [!summary] In breve
> Mittente e destinatario condividono la **stessa chiave segreta**. Dai cifrari classici (Cesare, monoalfabetico, polialfabetico) si arriva ai moderni **cifrari a blocchi** (DES, 3DES, AES) e a flusso (RC4).

| Cifrario | Chiave | Debolezza |
| --- | --- | --- |
| Cesare | spostamento $k$ (25 valori) | forza bruta immediata |
| Monoalfabetico | permutazione dell'alfabeto ($26! \approx 10^{26}$) | analisi delle frequenze, testo noto |
| Polialfabetico | più cifrari + sequenza | — |

- Attacchi: **solo testo cifrato**, **testo in chiaro noto**, **testo in chiaro scelto**.
- Gli algoritmi sono pubblici: il segreto è solo la chiave (principio di Kerckhoffs).
- Il problema principale è **distribuire la chiave**, che si risolve con la chiave pubblica (chiavi di sessione).

## Collegamenti

- **Concetti correlati**: [[Cifrari a Blocchi e CBC]] · [[Crittografia a Chiave Pubblica]] · [[Symmetric Encryption]] · [[Stream Cipher]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.2 Principi di crittografia|Capitolo 8 — 8.2 Principi di crittografia]]
> - [[08 - TLC - Sicurezza nelle reti#Crittografia a chiave simmetrica|Capitolo 8 — Crittografia a chiave simmetrica]]
