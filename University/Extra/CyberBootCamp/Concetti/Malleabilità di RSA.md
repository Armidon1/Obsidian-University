---
title: Malleabilità di RSA
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - rsa
  - attack
---

# Malleabilità di RSA

> [!summary] In breve
> RSA senza padding è moltiplicativo: $E(m_1) \cdot E(m_2) = E(m_1 m_2) \bmod n$. Si può trasformare un ciphertext in quello di un messaggio collegato senza conoscere la chiave.

$$C_1 C_2 \equiv m_1^e m_2^e = (m_1 m_2)^e \pmod n$$
Attacco tipico (oracolo che decifra tutto tranne la flag $c$):
```python
c2 = c * pow(2, e, n) % n            # cifratura di 2m
m2 = oracle_decrypt(c2)              # il server restituisce 2m
m  = m2 * pow(2, -1, n) % n
```
- Insieme al determinismo, è uno dei motivi per cui RSA si usa solo con padding ([[RSA-OAEP]]).

## Collegamenti

- **Concetti correlati**: [[RSA-OAEP]] · [[PKCS1]] · [[RSA Common Modulus Attack]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Malleabilità|Lezione 7 — Malleabilità]]
> - [[07 - CB - Crypto 2#Problemi di RSA e padding|Lezione 7 — Problemi di RSA e padding]]
