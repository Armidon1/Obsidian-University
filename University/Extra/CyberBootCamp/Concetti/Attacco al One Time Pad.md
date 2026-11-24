---
title: Attacco al One Time Pad
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - attack
---

# Attacco al One Time Pad

> [!summary] In breve
> Riusare la stessa chiave `K` per due messaggi rompe l'OTP: `C1 ⊕ C2 = P1 ⊕ P2`, la chiave sparisce. Dai pattern dei testi reali si ricostruiscono i plaintext (*crib dragging*, *many-time pad*).

```
C1 = P1 ⊕ K ,  C2 = P2 ⊕ K
C1 ⊕ C2 = P1 ⊕ P2       # K eliminata
```
- I testi veri hanno **struttura** (spazi, lettere frequenti): basta per separare `P1` e `P2`.
- Con molti riusi (*many-time pad*) l'attacco è automatizzabile (es. tool MTP).
- Morale: chiave **sempre diversa** e lunga → motivazione dei [[Stream Cipher|cifrari a flusso]].

## Collegamenti

- **Concetti correlati** (corso Cybersecurity): [[One-Time Pad (OTP)]] · [[Perfect Cipher]] · [[Stream Cipher]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[06 - CB - Crypto 1#Attacco: non riusare la chiave|Lezione 6 — Attacco: non riusare la chiave]]
