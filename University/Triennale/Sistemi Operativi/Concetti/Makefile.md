---
title: Makefile
tags:
  - sistemi-operativi
  - concetto
  - compilazione
  - build
---

# Makefile

> [!summary] In breve
> Script che descrive l'albero delle dipendenze tra file: `make` ricompila solo ciò che è più vecchio delle sue dipendenze.

```make
target: dipendenze
<TAB>comando
```

- Una regola viene eseguita se il **target è più vecchio** di una delle sue dipendenze (confronto dei tempi di modifica).
- `touch file` aggiorna la data di modifica (per forzare la ricompilazione).
- `gcc -MM *.c` genera automaticamente le teste delle regole.
- Su AVR il Makefile del corso usa le variabili `BINS`, `OBJS`, `HEADERS` e `include avr.mk`; `make x.hex` compila e carica.

## Collegamenti

- **Concetti correlati**: [[Compilazione e Linking con gcc]] · [[CMake]] · [[Toolchain AVR]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[02 - SO - Programmi, Makefile e pkg-config#Makefile|Lezione 2 — Makefile]]
> - [[04 - SO - Hardware e AVR#Makefile|Lezione 4 — Makefile]]
