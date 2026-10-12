---
title: Gestione degli Errori in C
tags:
  - sistemi-di-calcolo
  - concetto
  - linguaggio-c
  - libc
---

# Gestione degli Errori in C

> [!summary] In breve
> Codice di uscita (0 = successo), `atexit` per la pulizia, `assert` per i bug non recuperabili, e per gli errori recuperabili valori di ritorno speciali (NULL o −1) più `errno`/`perror` e un unico punto di cleanup.

- Libc: `NULL` per i puntatori, valori particolari per gli interi. POSIX: **0 = successo, −1 = errore**, più `errno`.
- `perror("msg")` stampa la descrizione dell'ultimo errore.
- `atexit(f)`: handler eseguiti in ordine inverso alla terminazione con `exit`/`return` (non con `_exit`/`abort`).
- `assert(test)`: termina con un messaggio su stderr; viene eliminata con `-DNDEBUG`.
- Pattern: `if (errore) goto cleanup;` con un'unica uscita che libera le risorse.
- Dopo una `fork` il figlio dovrebbe terminare con `_exit`, per non rieseguire gli handler di `atexit`.

## Collegamenti

- **Concetti correlati**: [[Funzioni della libc]] · [[fork]] · [[strace e ltrace]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[04 - SDC - Librerie standard del C#Gestione degli errori|Lezione 4 — Gestione degli errori]]
