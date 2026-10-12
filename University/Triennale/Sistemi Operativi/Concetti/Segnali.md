---
title: Segnali
tags:
  - sistemi-operativi
  - concetto
  - processi
  - unix
---

# Segnali

> [!summary] In breve
> Notifiche software asincrone a un processo (gli "interrupt dei processi"), identificate da un numero; si inviano con `kill(pid, sig)` e si gestiscono con `sigaction`.

- Esempi: `SIGCHLD` (un figlio è morto), `SIGHUP` (hang up), `SIGALRM` (timer), `SIGINT`, `SIGKILL` (non gestibile).
- Consegna: quando il processo viene ripreso, se ha segnali pendenti il kernel gli fa eseguire prima l'handler, poi il processo riprende da dove era.

```c
struct sigaction act = {0};
act.sa_handler = handler;          // oppure SIG_IGN / SIG_DFL
sigemptyset(&act.sa_mask);         // segnali bloccati durante l'handler
act.sa_flags = SA_RESTART;         // riesegue le syscall interrotte
sigaction(SIGCHLD, &act, &old);
```

- Su Linux un padre che termina **non** invia `SIGHUP` ai figli automaticamente.
- [[disastrOS]] usa `SIGALRM` + `setitimer` come timer interrupt simulato.

## Collegamenti

- **Concetti correlati**: [[wait e Processi Zombie]] · [[Interrupt]] · [[disastrOS]] · [[ucontext]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Terminazione e segnali|Lezione 6 — Terminazione e segnali]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Esempio SIGCHLD/SIGHUP|Lezione 6 — Esempio SIGCHLD/SIGHUP]]
> - [[08 - SO - disastrOS#Il timer: SIGALRM|Lezione 8 — Il timer: SIGALRM]]
> - [[06 - SDC - Esecuzione dei programmi#Segnali|Sistemi di Calcolo, cap. 6 — Segnali]]
