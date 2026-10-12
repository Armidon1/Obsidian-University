---
title: Compilazione e Linking con gcc
tags:
  - sistemi-operativi
  - concetto
  - compilazione
---

# Compilazione e Linking con gcc

> [!summary] In breve
> Sorgenti → object file (`gcc -c`) → eseguibile (`gcc -o`, linker) → processo (loader). Ogni passaggio ha le sue opzioni.

| File | Ruolo |
| --- | --- |
| `.h` | header (dichiarazioni) |
| `.c`, `.cpp`, `.S` | sorgenti |
| `.o` | object file |
| `.a` / `.so` | libreria statica / condivisa |
| *(nessuna estensione)* | eseguibile Unix (deve avere un `main`) |

```bash
gcc <opts> -c file.c            # compila in file.o
gcc <opts> -o prog a.o b.o -lm  # collega
```

- `-I<path>`: include path; `-D<macro>`: equivale a `#define`.
- `-L<path>`: directory delle librerie; `-l<nome>`: libreria da collegare (`-lm` → `libm`).
- `gcc -MM` genera le dipendenze (target: header).
- `gcc`/`g++` invocano compilatore, assembler e linker.

## Collegamenti

- **Concetti correlati**: [[Makefile]] · [[pkg-config]] · [[CMake]] · [[Linking Statico e Dinamico]] · [[Loader ed ELF]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[02 - SO - Programmi, Makefile e pkg-config#Costruzione di un eseguibile|Lezione 2 — Costruzione di un eseguibile]]
> - [[02 - SO - Programmi, Makefile e pkg-config#Tipi di file|Lezione 2 — Tipi di file]]
