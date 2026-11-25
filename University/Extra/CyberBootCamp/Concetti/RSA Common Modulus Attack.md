---
title: RSA Common Modulus Attack
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - rsa
  - attack
---

# RSA Common Modulus Attack

> [!summary] In breve
> Stesso messaggio cifrato con lo **stesso modulo** e due esponenti coprimi $e_1, e_2$: con Euclide esteso si trovano $a, b$ con $ae_1 + be_2 = 1$, e $m = c_1^a c_2^b \bmod n$.

$$c_1^a c_2^b = m^{a e_1 + b e_2} = m$$
```python
g, a, b = xgcd(e1, e2)          # Sage; serve g == 1
m = pow(c1, a, n) * pow(c2, b, n) % n   # pow gestisce l'esponente negativo
```
- Un coefficiente è sempre negativo: serve l'inverso del ciphertext (`pow(c, -k, n)` in Python ≥ 3.8).
- Esempio della slide: $e_1 = 4$, $e_2 = 3$ → $m = c_1 \cdot c_2^{-1}$.

## Collegamenti

- **Concetti correlati**: [[RSA]] · [[SageMath]] · [[Malleabilità di RSA]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Stesso messaggio, esponenti diversi|Lezione 7 — Stesso messaggio, esponenti diversi]]
