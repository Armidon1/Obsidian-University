---
title: Traduzione dei Costrutti C in Assembly
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - linguaggio-c
---

# Traduzione dei Costrutti C in Assembly

> [!summary] In breve
> Ogni costrutto si riscrive prima in C con `if (!test) goto`: if, if-else, while e for diventano un confronto, un salto condizionato sul test negato e dei `jmp`.

```c
// while (test) body;        →        L: if (!test) goto E;
//                                       body; goto L;
//                                    E:
```

```asm
L:  cmpl %ebx, %eax
    ja E           # test negato (a > b, senza segno)
    ...            # body
    jmp L
E:
```

- **if**: salto oltre il blocco; **if-else**: `Jcc E` più `jmp F` alla fine del primo blocco.
- **for** = while con inizializzazione e aggiornamento: produce lo stesso codice.
- **Array**: `a[i]` → `(base,i,sizeof)`; con indice costante → `i*sizeof(base)`.
- **Struct**: `p->campo` → `offset(base)`, tenendo conto del padding.

## Collegamenti

- **Concetti correlati**: [[Istruzioni di Salto e Condition Code]] · [[Modi di Indirizzamento]] · [[Convenzioni di Chiamata IA32]] · [[Allineamento e Padding]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Traduzione dei costrutti C|Lezione 3 — Traduzione dei costrutti C]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Array e aritmetica dei puntatori|Lezione 3 — Array e aritmetica dei puntatori]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Strutture|Lezione 3 — Strutture]]
