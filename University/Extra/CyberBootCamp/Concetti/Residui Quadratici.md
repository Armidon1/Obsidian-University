---
title: Residui Quadratici
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - diffie-hellman
  - math
---

# Residui Quadratici

> [!summary] In breve
> $a$ è un residuo quadratico modulo $n$ se esiste $x$ con $x^2 \equiv a$. Modulo un primo si riconosce con il criterio di Eulero, e questo basta a rompere il Decisional Diffie-Hellman in $\mathbb{Z}_p^*$.

- Modulo un primo $p$, metà dei numeri non nulli sono QR.
- **Criterio di Eulero**: $a^{(p-1)/2} \equiv 1 \pmod p \iff a$ è QR (altrimenti vale $-1$).
- Se $g$ genera $\mathbb{Z}_p^*$: $g^k$ è QR $\iff k$ pari.

**DDH in $\mathbb{Z}_p^*$**: $z = g^{ab}$ è QR con probabilità 75% ($a$ o $b$ pari), uno $z$ casuale con il 50%.
```python
is_qr = lambda a, p: pow(a, (p - 1) // 2, p) == 1
expected = is_qr(gA, p) or is_qr(gB, p)   # vale se z = g^ab
```
Sage: `sqrt(Zmod(101)(30), all=True)` → `[38, 63]`.

## Collegamenti

- **Concetti correlati**: [[Diffie-Hellman Key Exchange]] · [[Gruppi, Anelli e Campi]] · [[Euler's Theorem]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Residui quadratici|Lezione 7 — Residui quadratici]]
> - [[07 - CB - Crypto 2#DDH in Zp* si rompe|Lezione 7 — DDH in Zp* si rompe]]
> - [[07 - CB - Crypto 2#Decisional Diffie-Hellman|Lezione 7 — Decisional Diffie-Hellman]]
