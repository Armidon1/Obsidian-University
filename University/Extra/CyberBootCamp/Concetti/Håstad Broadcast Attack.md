---
title: Håstad Broadcast Attack
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - rsa
  - attack
---

# Håstad Broadcast Attack

> [!summary] In breve
> Lo stesso $m$ cifrato con lo stesso $e$ piccolo per $e$ moduli diversi: il [[Teorema Cinese del Resto]] dà $m^e \bmod N_1\cdots N_e$, che è esattamente $m^e$, e basta la radice $e$-esima intera.

$$m^e \equiv c_i \pmod{N_i},\ i = 1..e \;\xrightarrow{\text{CRT}}\; K = m^e \bmod \textstyle\prod N_i = m^e \;\Rightarrow\; m = K^{1/e}$$
```python
K = crt([c1, c2, c3], [N1, N2, N3])   # Sage
m = Integer(K).nth_root(3)
```
- Funziona perché $m < N_i$ per ogni $i$, quindi $m^e < \prod N_i$.
- Servono almeno $e$ ciphertext; i moduli devono essere coprimi (se non lo sono, il $\gcd$ li fattorizza: vedi [[Fattorizzare il Modulo RSA]]).

## Collegamenti

- **Concetti correlati**: [[Teorema Cinese del Resto]] · [[RSA con Esponente Piccolo]] · [[SageMath]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Stesso messaggio, moduli diversi: Teorema Cinese del Resto|Lezione 7 — Stesso messaggio, moduli diversi: Teorema Cinese del Resto]]
