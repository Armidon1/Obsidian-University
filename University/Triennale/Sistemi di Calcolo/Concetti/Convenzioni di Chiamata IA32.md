---
title: Convenzioni di Chiamata IA32
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - abi
  - funzioni
---

# Convenzioni di Chiamata IA32

> [!summary] In breve
> System V i386: i parametri vanno sullo stack in ordine inverso (il primo è a 4(%esp) all'ingresso, 8(%ebp) dopo il prologo), il risultato in %eax, e il chiamante toglie i parametri dallo stack.

```asm
pushl $20         # c = f(10, 20)
pushl $10
call f
addl $8, %esp     # pulisce il chiamante
movl %eax, %ecx

f:  movl 4(%esp), %eax   # x
    addl 8(%esp), %eax   # + y
    ret
```

- Parametri da 1–2 byte promossi a 4.
- Variabili locali in memoria se: array/struct, troppe variabili, o uso di `&`. Si alloca con `subl $k, %esp`.
- Alla `CALL` `%esp` dovrebbe essere multiplo di 16 (allineamento).

## Collegamenti

- **Concetti correlati**: [[Stack Frame]] · [[Registri Caller-save e Callee-save]] · [[ABI e ISA]] · [[x86-64]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Funzioni|Lezione 3 — Funzioni]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Passaggio dei parametri|Lezione 3 — Passaggio dei parametri]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Variabili locali|Lezione 3 — Variabili locali]]
