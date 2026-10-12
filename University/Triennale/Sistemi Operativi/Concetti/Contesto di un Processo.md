---
title: Contesto di un Processo
tags:
  - sistemi-operativi
  - concetto
  - processi
  - context-switch
---

# Contesto di un Processo

> [!summary] In breve
> Lo stato di un flusso di esecuzione: registri della CPU (PC, SP, flag, registri generali) più la memoria del processo. Se la memoria resta al suo posto, basta salvare e ripristinare i registri per sospendere e riprendere un processo.

- Registri: su AVR R0–R31, SREG, PC, SP (SPH:SPL), più RAMPZ/EIND.
- Memoria: `.text` (r-x), `.data` / `.bss` (rw-), `.rodata` (r--), heap, stack.
- In C un flusso è definito dalla **pila dei record di attivazione** e dall'**instruction pointer**: ogni flusso ha bisogno del **proprio stack**.
- I registri si salvano **sullo stack del processo stesso**; nel TCB/PCB basta salvare lo **stack pointer**.

## Collegamenti

- **Concetti correlati**: [[Context Switch]] · [[ucontext]] · [[Immagine di Memoria di un Processo]] · [[Process Control Block]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[05 - SO - Stack e Context Switch#Processo e contesto|Lezione 5 — Processo e contesto]]
> - [[04 - SO - Hardware e AVR#AVR|Lezione 4 — AVR]]
