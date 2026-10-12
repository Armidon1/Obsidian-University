---
title: pkg-config
tags:
  - sistemi-operativi
  - concetto
  - compilazione
  - build
---

# pkg-config

> [!summary] In breve
> Database di file `.pc` che restituisce le opzioni di compilazione (`-I`, `-D`) e di link (`-L`, `-l`) per i pacchetti installati.

- Un pacchetto C/C++ è un insieme di **header** più un insieme di **librerie**.
- `pkg-config --cflags <pkg>`: opzioni per la compilazione dei `.o`.
- `pkg-config --libs <pkg>`: opzioni per il linking.
- Cerca i file `*.pc` nelle directory di `$PKG_CONFIG_PATH`.
- In CMake l'equivalente è `find_package`.

## Collegamenti

- **Concetti correlati**: [[Compilazione e Linking con gcc]] · [[CMake]] · [[Makefile]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[02 - SO - Programmi, Makefile e pkg-config#Pacchetti esterni e pkg-config|Lezione 2 — Pacchetti esterni e pkg-config]]
