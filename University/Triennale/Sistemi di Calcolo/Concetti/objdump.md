---
title: objdump
tags:
  - sistemi-di-calcolo
  - concetto
  - strumenti
  - assembly
---

# objdump

> [!summary] In breve
> Disassembler: `objdump -d` mostra offset, codice macchina e assembly di un oggetto o eseguibile; `objdump -S` (con `gcc -g`) intercala anche il sorgente C.

```
$ gcc -g -c somma.c && objdump -S somma.o
   0:  55          push %rbp
   1:  48 89 e5    mov  %rsp,%rbp
  10:  01 d0       add  %edx,%eax
  13:  c3          retq
```

- Le istruzioni x86 hanno **lunghezza variabile** (`c3` = 1 byte).
- Formati dei binari: **ELF** (Linux), **Mach-O** (macOS), non intercambiabili nemmeno sullo stesso hardware.
- `file` dice il tipo di un file dal contenuto.

## Collegamenti

- **Concetti correlati**: [[Compilazione e Interpretazione]] · [[Loader ed ELF]] · [[Compilazione e Linking con gcc]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[02 - SDC - Programmazione di un sistema di calcolo#Disassemblare con objdump|Lezione 2 — Disassemblare con objdump]]
