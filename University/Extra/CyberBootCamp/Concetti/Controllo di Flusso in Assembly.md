---
title: Controllo di Flusso in Assembly
tags:
  - cyberbootcamp
  - concetto
  - assembly
---

# Controllo di Flusso in Assembly

> [!summary] In breve
> In assembly non esistono `if`/`while`: si costruiscono con `cmp` (confronta e imposta i flag) + salti (`jmp`, `je`, `jl`, `jnz`…). Un ciclo è un `if` che alla fine salta indietro.

- `cmp a, b` calcola `a-b` e aggiorna i **flag** senza salvare; il salto condizionato che segue decide in base ai flag.
- Salti: `jmp` (incond.), `je/jne`, `jl/jle/jg/jge` (ordine con segno), `jb/jbe/ja/jae` (ordine senza segno), `jnz`…

```asm
; if (rdi < rsi) ...
    cmp rdi, rsi
    jl  then
    jmp else
; while: stessa cmp, con jmp indietro a fine corpo
```

## Collegamenti

- **Concetti correlati**: [[Istruzioni x86-64]] · [[Stack Frame x86-64]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Controllo di flusso|Lezione 3 — Controllo di flusso]]
