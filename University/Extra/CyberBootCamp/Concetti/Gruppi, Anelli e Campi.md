---
title: Gruppi, Anelli e Campi
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - math
---

# Gruppi, Anelli e Campi

> [!summary] In breve
> Un **gruppo** è un insieme con un'operazione che ha chiusura, associatività, identità e inverso; un **campo** ha due operazioni (somma e prodotto) e si può dividere per ogni elemento non nullo; un **anello** è un campo senza l'inverso moltiplicativo.

| Struttura | Operazioni | Si può dividere? | Esempi |
|---|---|---|---|
| Gruppo $(G,\cdot)$ | una | — | $(\mathbb{Z},+)$, $(\mathbb{Z}_p^*,\cdot)$, curve ellittiche |
| Anello | $+$ e $\cdot$ | non sempre | $\mathbb{Z}$, $\mathbb{Z}_n$ con $n$ non primo |
| Campo | $+$ e $\cdot$ | sì (tranne per 0) | $\mathbb{R}$, $\mathbb{Z}_p$ con $p$ primo |

- **Abeliano** = commutativo ($a\cdot b = b\cdot a$). Anche le curve ellittiche sono gruppi abeliani.
- In notazione additiva $a^n$ diventa $na$: per questo DH sul gruppo additivo è banale da rompere.
- $(\mathbb{Z}\setminus\{0\},\cdot)$ **non** è un gruppo: $2$ non ha inverso intero.

## Collegamenti

- **Concetti correlati**: [[Modular Arithmetic]] · [[Diffie-Hellman Key Exchange]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Gruppi, anelli e campi|Lezione 7 — Gruppi, anelli e campi]]
> - [[07 - CB - Crypto 2#Proprietà|Lezione 7 — Proprietà]]
