---
title: Funzioni della libc
tags:
  - sistemi-di-calcolo
  - concetto
  - linguaggio-c
  - libc
---

# Funzioni della libc

> [!summary] In breve
> Le funzioni standard più usate: stringhe (`strlen`, `strcpy`, `strcmp`, `sprintf`, `sscanf`, `strtok`, `atoi`), memoria (`memcpy`, `memcmp`, `memset`), stream (`fopen`, `fprintf`, `fscanf`, `fgets`, `fread`, `fwrite`), `qsort`/`bsearch`.

- Documentazione: `man 3 <funzione>` (sezione 1 = comandi, 2 = system call, 3 = librerie).
- `strcpy`/`strcat`/`sprintf` non controllano lo spazio → **buffer overflow**: usare `strncpy`, `snprintf`.
- `strtok` modifica il buffer e alla seconda chiamata vuole `NULL`.
- `mem*` lavorano su n byte grezzi, `str*` si fermano a `'\0'`.
- `scanf`/`fscanf` restituiscono il numero di argomenti letti.
- `fread`/`fwrite` scrivono byte binari (little-endian su x86).
- `qsort`/`bsearch` sono generiche grazie a un **comparatore** (puntatore a funzione).
- Matematica: `#include <math.h>` e `-lm`.

## Collegamenti

- **Concetti correlati**: [[Gestione degli Errori in C]] · [[File Descriptor]] · [[Puntatori a Funzione]] · [[strace e ltrace]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[04 - SDC - Librerie standard del C#Stringhe|Lezione 4 — Stringhe]]
> - [[04 - SDC - Librerie standard del C#Memoria|Lezione 4 — Memoria]]
> - [[04 - SDC - Librerie standard del C#File e stream|Lezione 4 — File e stream]]
> - [[04 - SDC - Librerie standard del C#Ricerca e ordinamento: bsearch e qsort|Lezione 4 — Ricerca e ordinamento: bsearch e qsort]]
