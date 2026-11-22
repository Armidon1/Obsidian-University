---
title: Registri Caller-saved e Callee-saved
tags:
  - cyberbootcamp
  - concetto
  - assembly
---

# Registri Caller-saved e Callee-saved

> [!summary] In breve
> Chi salva i registri attraverso una `call`? I **callee-saved** li preserva il chiamato (restano invariati dopo la call); i **caller-saved** può cambiarli il chiamato, quindi li salva il chiamante se gli servono dopo.

| Caller-saved (volatili) | Callee-saved (preservati) |
|---|---|
| `rax`, `rcx`, `rdx`, `rdi`, `rsi`, `r8`–`r11` | `rbx`, `rbp`, `rsp`, `r12`–`r15` |

- **callee-saved**: il chiamato li `push`a all'inizio e li `pop`pa prima del `ret`, se li usa.
- **caller-saved**: il chiamante li salva prima della `call` se vuole ritrovarli.

## Collegamenti

- **Concetti correlati**: [[Calling Convention]] · [[Registri x86-64]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Caller-saved e callee-saved|Lezione 3 — Caller-saved e callee-saved]]
