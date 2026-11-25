---
title: Fattorizzare il Modulo RSA
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - rsa
  - attack
---

# Fattorizzare il Modulo RSA

> [!summary] In breve
> Se si trova un fattore di $N = pq$, RSA è rotto: $q = N/p$, poi $\varphi(N) = (p-1)(q-1)$ e $d = e^{-1} \bmod \varphi(N)$. Nelle CTF $N$ si fattorizza quando $p$ e $q$ sono generati male.

| Situazione | Come si attacca |
|---|---|
| $N \le 512$ bit | [factordb.com](http://factordb.com); `factor(N, algorithm='pari'/'ecm'/'qsieve')` |
| $p$ e $q$ vicini | Fermat: $N = a^2 - b^2$, parti da $a = \lceil\sqrt N\rceil$ finché $a^2 - N$ è un quadrato |
| più moduli | $\gcd(N_1, N_2)$ a coppie: un primo condiviso li rompe entrambi |
| $q = f(p)$ semplice | risolvi $p \cdot f(p) = N$ (es. $q = 3p+1 \Rightarrow 3p^2 + p - N = 0$) |
| $q = f(p)$ monotona | ricerca binaria su $p \cdot f(p) = N$ |
| leak di $p + q = S$ | $p, q$ radici di $x^2 - Sx + N$; oppure $\varphi(N) = N - S + 1$ |

```python
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, N)
```

## Collegamenti

- **Concetti correlati**: [[Factorize a Number]] · [[RSA]] · [[SageMath]] · [[RSA con Esponente Piccolo]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Fattorizzare N|Lezione 7 — Fattorizzare N]]
> - [[07 - CB - Crypto 2#p e q troppo vicini|Lezione 7 — p e q troppo vicini]]
> - [[07 - CB - Crypto 2#Fattori comuni tra moduli diversi|Lezione 7 — Fattori comuni tra moduli diversi]]
> - [[07 - CB - Crypto 2#q dipende da p|Lezione 7 — q dipende da p]]
> - [[07 - CB - Crypto 2#Leak di p + q|Lezione 7 — Leak di p + q]]
