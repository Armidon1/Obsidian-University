---
title: LEA
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - ia32
  - ottimizzazione
---

# LEA

> [!summary] In breve
> `leal S, D` calcola l'indirizzo effettivo di S e lo scrive in D senza accedere alla memoria: serve per calcolare indirizzi e per fare aritmetica veloce in una sola istruzione.

```asm
movl (%eax), %edx            # edx = M[eax]   (legge la memoria)
leal (%eax), %edx            # edx = eax      (nessun accesso)
leal -7(%eax,%ecx,4), %edx   # edx = x + 4*y - 7   (z = x + y*4 - 7)
leal (%eax,%eax,2), %eax     # eax = 3*eax
```

- Scala limitata a 1, 2, 4, 8: `x + y*5 - 7` non si fa con una sola `leal`.
- Usata dal compilatore anche per calcolare `&variabile` locale.

## Collegamenti

- **Concetti correlati**: [[Modi di Indirizzamento]] · [[Ottimizzazioni del Compilatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#LEA (load effective address)|Lezione 3 — LEA (load effective address)]]
