---
title: Algoritmo RSA
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - rsa
---

# Algoritmo RSA

> [!summary] In breve
> RSA: si scelgono i primi $p, q$, poi $n = pq$, $z = (p-1)(q-1)$, $e$ coprimo con $z$ e $d$ con $ed \bmod z = 1$. Chiave pubblica $(n, e)$, privata $(n, d)$; si cifra con $c = m^e \bmod n$ e si decifra con $m = c^d \bmod n$. La sicurezza si basa sulla difficoltà di **fattorizzare** $n$.

Esempio: $p = 5$, $q = 7$ → $n = 35$, $z = 24$, $e = 5$, $d = 29$ ($5 \cdot 29 - 1 = 144 = 6 \cdot 24$).

| Lettera | $m$ | $c = m^5 \bmod 35$ | $c^{29} \bmod 35$ |
| --- | --- | --- | --- |
| l | 12 | 17 | 12 |
| o | 15 | 15 | 15 |
| v | 22 | 22 | 22 |
| e | 5 | 10 | 5 |

- Funziona perché $x^y \bmod n = x^{y \bmod z} \bmod n$, quindi $m^{ed} \bmod n = m^1 \bmod n = m$.
- È lento (DES 100–10.000 volte più veloce), per cui si usa per cifrare una **chiave di sessione**.
- Si raccomanda $pq$ di ~1024 bit; non è dimostrato che non esista un algoritmo di fattorizzazione veloce.

## Collegamenti

- **Concetti correlati**: [[Crittografia a Chiave Pubblica]] · [[RSA]] · [[Problema della Fattorizzazione]] · [[Firma Digitale]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#RSA|Capitolo 8 — RSA]]
