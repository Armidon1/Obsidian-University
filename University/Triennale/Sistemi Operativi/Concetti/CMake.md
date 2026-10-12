---
title: CMake
tags:
  - sistemi-operativi
  - concetto
  - compilazione
  - build
---

# CMake

> [!summary] In breve
> Generatore di Makefile multipiattaforma: da `CMakeLists.txt` produce i Makefile per il sistema corrente; le dipendenze sono dedotte automaticamente.

```cmake
cmake_minimum_required(VERSION 2.8)
project(so_game)
find_package(OpenGL REQUIRED)
include_directories(${OPENGL_INCLUDE_DIR})
add_executable(so_game a.c b.c)
add_library(mylib [SHARED] x.c)   # statica se SHARED è omesso
target_link_libraries(so_game ${OPENGL_LIBRARIES} m)
add_subdirectory(sub)             # sub/ ha il suo CMakeLists.txt
```

- Variabili globali, atomiche o liste: `set(V a b c)`, `${V}`, `set(V ${V} d)` per accodare.
- Uso: `cmake <dir>` e poi `make`.

## Collegamenti

- **Concetti correlati**: [[Makefile]] · [[pkg-config]] · [[Compilazione e Linking con gcc]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[02 - SO - Programmi, Makefile e pkg-config#CMake|Lezione 2 — CMake]]
> - [[02 - SO - Programmi, Makefile e pkg-config#Comandi principali|Lezione 2 — Comandi principali]]
