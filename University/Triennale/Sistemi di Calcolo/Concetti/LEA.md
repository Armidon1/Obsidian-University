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

## MOV vs LEA

**per copiare soltanto EAX in EDX, puoi usare `movl`**. In AT&T:

```
movl %eax, %edx
leal (%eax), %edx
```

Entrambe producono `EDX = EAX`, senza leggere la memoria. In questo caso `lea` non offre un vantaggio particolare.

L’utilità emerge quando devi **calcolare un’espressione**, invece di copiare un valore. Per esempio:

```
leal -3(%eax,%ecx,2), %edx
# EDX = EAX + ECX*2 - 3
```

Con `movl` non puoi chiedere quel calcolo:

```
movl -3(%eax,%ecx,2), %edx
# EDX = M[EAX + ECX*2 - 3]
```

Qui `movl` calcola l’indirizzo e poi **legge la memoria**; `leal` conserva direttamente il risultato del calcolo.

Per ottenere la stessa espressione senza `lea`, una possibile sequenza sarebbe:

```
movl %ecx, %edx
addl %edx, %edx     # ECX*2
addl %eax, %edx
subl $3, %edx
```

`lea` può quindi condensare diverse operazioni in una sola istruzione e **non modifica i flag**, mentre `addl` e `subl` li modificano.

Un altro esempio concreto è ottenere l’indirizzo di una variabile locale:

```
leal -8(%ebp), %eax   # EAX = &variabile
movl -8(%ebp), %eax   # EAX = valore della variabile
```

La frase «`leal` serve a scrivere programmi più veloci» è dunque troppo assoluta: **serve a calcolare indirizzi o certe espressioni aritmetiche; il vantaggio di prestazioni dipende dal caso**.
## Collegamenti

- **Concetti correlati**: [[Modi di Indirizzamento]] · [[Ottimizzazioni del Compilatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#LEA (load effective address)|Lezione 3 — LEA (load effective address)]]
