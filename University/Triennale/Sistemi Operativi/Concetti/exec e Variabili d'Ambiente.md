---
title: exec e Variabili d'Ambiente
tags:
  - sistemi-operativi
  - concetto
  - processi
  - syscall
  - unix
---

# exec e Variabili d'Ambiente

> [!summary] In breve
> `exec` sostituisce l'immagine del processo corrente con un nuovo eseguibile caricato da disco (stesso PID, non ritorna se ha successo). L'ambiente è `char** environ` ("NAME=VALUE").

- Invoca il **loader**; il nuovo programma parte da `_start` → `__libc_start_main` → `main` → `exit`.
- Varianti: `execv(path, argv)`, `execvp` (cerca nel `PATH`), `execvpe(file, argv, envp)` (ambiente personalizzato).
- Schema tipico: `fork()` e poi `exec()` nel figlio, mentre il padre fa `wait()`.
- `extern char** environ;` dà accesso all'ambiente; `getenv("PATH")`; `env` da terminale. La `fork` copia l'ambiente al figlio.

## Collegamenti

- **Concetti correlati**: [[fork]] · [[Loader ed ELF]] · [[Program File e Processo]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Lanciare un nuovo programma: exec|Lezione 6 — Lanciare un nuovo programma: exec]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Variabili d'ambiente|Lezione 6 — Variabili d'ambiente]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#exit|Lezione 6 — exit]]
