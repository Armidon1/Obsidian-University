---
title: Cifrari a Blocchi e CBC
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - block-cipher
---

# Cifrari a Blocchi e CBC

> [!summary] In breve
> Un **cifrario a blocchi** cifra blocchi di $k$ bit con una permutazione determinata dalla chiave, realizzata con funzioni iterate di tabelle e permutazioni (DES 64/56, AES 128/128–256). Il **CBC** concatena i blocchi, $c(i) = K_S(m(i) \oplus c(i-1))$ con un IV, perché blocchi uguali non diano cifrati uguali.

- $k = 3$: $8! = 40.320$ corrispondenze; in generale $(2^k)!$.
- Struttura tipica: 64 bit → 8 tabelle da 8 bit → permutatore a 64 bit → $n$ iterazioni (ogni bit d'ingresso influenza tutti quelli d'uscita).
- AES a 128 bit: ~149 trilioni di anni con una macchina che rompe DES in 1 s.

Esempio CBC (Tabella 8.1, testo `010 010 010`, IV = 001):
```text
c(1) = K(010 ⊕ 001) = K(011) = 100
c(2) = K(010 ⊕ 100) = K(110) = 000
c(3) = K(010 ⊕ 000) = K(010) = 101
```
- L'IV viaggia in chiaro; i protocolli (SSL, IPsec) devono distribuirlo.

## Collegamenti

- **Concetti correlati**: [[Crittografia a Chiave Simmetrica]] · [[Block Cipher]] · [[CBC]] · [[AES]] · [[DES]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Cifrari a blocchi|Capitolo 8 — Cifrari a blocchi]]
> - [[08 - TLC - Sicurezza nelle reti#Cifrari a blocchi concatenati (CBC)|Capitolo 8 — Cifrari a blocchi concatenati (CBC)]]
