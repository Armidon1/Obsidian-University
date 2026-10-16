---
title: Metodo di bisezione
tags:
  - analisi-1
  - concetto
  - continuità
  - calcolo-numerico
---

# Metodo di bisezione

> [!summary] In breve
> Per approssimare uno zero di f continua con f(a)f(b) < 0: si dimezza l'intervallo tenendo la metà in cui f cambia segno; dopo n passi l'errore è ≤ (b − a)/2ⁿ.

```
finché b − a > tolleranza:
    m = (a + b) / 2
    se f(a) · f(m) ≤ 0:  b = m
    altrimenti:           a = m
restituisci (a + b) / 2
```

- Intervalli incapsulati $I_0 \supset I_1 \supset \ldots$, lunghezza $\frac{b - a}{2^n}$.
- $a_n \nearrow c$, $b_n \searrow c$ e $f(c)^2 \le 0 \Rightarrow f(c) = 0$.
- Lento (una cifra binaria per passo) ma funziona per ogni funzione continua; è lo stesso schema della [[Ricerca binaria]].

## Collegamenti

- **Concetti correlati**: [[Teorema degli zeri]] · [[Teorema delle successioni monotone]] · [[Ricerca binaria]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[04 - AN1 - Funzioni Continue#Metodo di bisezione|Lezione 4 — Metodo di bisezione]]
