---
title: SageMath
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - tools
---

# SageMath

> [!summary] In breve
> Sistema di calcolo simbolico basato su Python: nelle CTF di crittografia fa in una riga aritmetica modulare, inversi, CRT, fattorizzazione, logaritmo discreto e sistemi di equazioni.

| Cosa | Sage | Python puro |
|---|---|---|
| anello $\mathbb{Z}_n$ | `Zn = Zmod(n)`; `Zn(a)` | `a % n` |
| inverso | `1 / Zn(a)`, `Zn(a)^-1` | `pow(a, -1, n)` |
| potenza modulare | `Zn(a)^b`, `pow(a, b, n)` | `pow(a, b, n)` |
| Euclide esteso | `xgcd(a, b)` → `(g, x, y)` | `sympy.gcdex` |
| CRT | `crt(vals, mods)` | `sympy.ntheory.modular.crt(mods, vals)` |
| fattorizzazione | `factor(N, algorithm='pari'/'ecm'/'qsieve')` | `sympy.factorint` |
| logaritmo discreto | `Zmod(p)(A).log(g)` | `sympy.discrete_log(p, A, g)` |
| radice modulare | `sqrt(Zmod(p)(a), all=True)` | `sympy.sqrt_mod(a, p, all_roots=True)` |
| radice intera | `Integer(c).nth_root(e)` | `gmpy2.iroot(c, e)` |
| sistema | `p, q = var('p q'); solve([p*q == N, p+q == S], p, q)` | `sympy.solve` |

- `Zn(6)^-1` in `Zmod(10)` → `ZeroDivisionError`: l'inverso esiste solo se $\gcd(a,n)=1$.
- `2 ^ huge % n` è lentissimo (calcola prima la potenza intera): usa sempre `pow` o `Zmod`.

## Collegamenti

- **Concetti correlati**: [[Modular Arithmetic]] · [[Teorema Cinese del Resto]] · [[Fattorizzare il Modulo RSA]] · [[pycryptodome]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Aritmetica modulare in Sage|Lezione 7 — Aritmetica modulare in Sage]]
> - [[07 - CB - Crypto 2#Esponenziazione modulare|Lezione 7 — Esponenziazione modulare]]
