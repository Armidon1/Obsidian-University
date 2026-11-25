---
title: Teorema Cinese del Resto
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - math
---

# Teorema Cinese del Resto

> [!summary] In breve
> Dati moduli a due a due coprimi $n_1,\dots,n_k$ e resti $a_1,\dots,a_k$, il sistema $x \equiv a_i \pmod{n_i}$ ha una sola soluzione modulo $n_1 n_2 \cdots n_k$. In inglese CRT (*Chinese Remainder Theorem*).

```python
sage: crt([1, 0, 3], [3, 5, 7])   # x%3=1, x%5=0, x%7=3
10                                 # unica soluzione mod 105
```
Dove torna nelle CTF:
- [[Håstad Broadcast Attack]]: ricostruisce $m^e$ modulo $N_1\cdots N_e$;
- [[Pohlig-Hellman]]: ricompone i logaritmi discreti calcolati per ogni fattore di $p-1$;
- RSA-CRT: decifratura più veloce lavorando separatamente modulo $p$ e modulo $q$.

## Collegamenti

- **Concetti correlati**: [[Håstad Broadcast Attack]] · [[Pohlig-Hellman]] · [[SageMath]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Stesso messaggio, moduli diversi: Teorema Cinese del Resto|Lezione 7 — Stesso messaggio, moduli diversi: Teorema Cinese del Resto]]
> - [[07 - CB - Crypto 2#Quando il logaritmo discreto è facile: Pohlig–Hellman|Lezione 7 — Quando il logaritmo discreto è facile: Pohlig–Hellman]]
