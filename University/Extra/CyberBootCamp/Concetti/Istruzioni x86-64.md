---
title: Istruzioni x86-64
tags:
  - cyberbootcamp
  - concetto
  - assembly
---

# Istruzioni x86-64

> [!summary] In breve
> Le istruzioni base operano su `dst, src`: `mov`, `add`, `sub`, `and`, `xor`… Al più **un** operando può stare in memoria. `lea` calcola un indirizzo senza leggerlo; `movzx`/`movsx` estendono a più bit.

- `mov/add/sub/and/or/xor <dst>, <src>`. `src` = registro, immediato o memoria; **memoria→memoria vietato**.
- `xor rax, rax` è l'idioma per azzerare.
- **Accesso memoria**: `TYPE PTR [base + index*scale + off]`, con `TYPE` = `BYTE/WORD/DWORD/QWORD` (1/2/4/8 byte).
- `lea rax, [rsi+rdi*4+6]`: **nessun** accesso, `rax` diventa il puntatore (utile anche come aritmetica).
- Da 32 a 64 bit, `mov eax, edi` estende con zeri e `movsxd rax, edi` estende con segno.
- Da 8 o 16 bit, `movzx` riempie con **zeri** (unsigned), `movsx` estende il **segno** (signed).

## Collegamenti

- **Concetti correlati**: [[Registri x86-64]] · [[Controllo di Flusso in Assembly]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Istruzioni aritmetiche, logiche e di spostamento|Lezione 3 — Istruzioni aritmetiche, logiche e di spostamento]]
