---
title: Registri IA32
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - ia32
---

# Registri IA32

> [!summary] In breve
> 8 registri interi a 32 bit (EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP) più EIP ed EFLAGS; di A–D si possono usare parti da 16 e 8 bit.

- `%eax` (32 bit) ⊃ `%ax` (16 bit bassi) ⊃ `%ah` / `%al` (byte 1 / byte 0). Lo stesso per B, C, D; DI, SI, SP, BP solo a 32 e 16 bit.
- **ESP**: cima dello stack. **EBP**: frame pointer (opzionale). **EIP**: prossima istruzione. **EFLAGS**: condition code.
- Suffissi: `b` = 1 byte, `w` = 2 (*word*), `l` = 4. `char`→b, `short`→w, `int`/`long`/puntatore→l.
- Con segno e senza segno: stesso tipo macchina, istruzioni diverse.

## Collegamenti

- **Concetti correlati**: [[x86-64]] · [[Modi di Indirizzamento]] · [[Istruzioni di Salto e Condition Code]] · [[Registri Caller-save e Callee-save]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Registri|Lezione 3 — Registri]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Tipi di dato macchina|Lezione 3 — Tipi di dato macchina]]
