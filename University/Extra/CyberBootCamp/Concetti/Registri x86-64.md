---
title: Registri x86-64
tags:
  - cyberbootcamp
  - concetto
  - assembly
---

# Registri x86-64

> [!summary] In breve
> Piccolo insieme di celle velocissime della CPU. Lo stesso registro si nomina a dimensioni diverse (`RAX`→`EAX`→`AX`→`AL`); alcuni hanno un ruolo fisso (argomenti, ritorno, stack/base/instruction pointer).

- `RAX` (64) ⊃ `EAX` (32) ⊃ `AX` (16) ⊃ `AH`/`AL` (8). Scrivere su `EAX` azzera i 32 bit alti.
- Ruoli chiave: `rax` ritorno · `rdi,rsi,rdx,rcx,r8,r9` primi sei argomenti interi o puntatori in System V AMD64 · `rbp` base pointer · `rsp` stack pointer · `rip` istruzione corrente.
- `r8`–`r15` esistono solo in 64 bit.

| 64 | 32 | 16 | 8 |
|---|---|---|---|
| `rax` | `eax` | `ax` | `al` |
| `rdi` | `edi` | `di` | `dil` |

## Collegamenti

- **Concetti correlati**: [[Istruzioni x86-64]] · [[Stack Frame x86-64]] · [[Registri Caller-saved e Callee-saved]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Registri|Lezione 3 — Registri]]
> - [[04 - CB - Binary Exploitation 1#Come la CPU esegue il codice|Lezione 4 — Come la CPU esegue il codice]]
