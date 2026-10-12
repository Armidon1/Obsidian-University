---
title: wait e Processi Zombie
tags:
  - sistemi-operativi
  - concetto
  - processi
  - syscall
  - unix
---

# wait e Processi Zombie

> [!summary] In breve
> `wait(&status)` sospende il padre fino alla terminazione di un figlio e ne restituisce PID e valore di `exit`. Un figlio terminato ma non ancora "atteso" è uno zombie.

- `wait` aspetta **un** figlio qualunque (con n figli servono n wait); `waitpid` aspetta un figlio specifico.
- **Zombie**: le risorse sono già rilasciate, resta solo il PCB con il valore di ritorno.
- **Orfani**: se il padre muore, i figli vengono adottati da **init** (PID 1), che fa periodicamente `wait`.
- `exit(code)` termina il processo (chiamata implicitamente dal C runtime quando il `main` ritorna); il padre riceve `SIGCHLD`.
- In disastrOS, `exit`: figli a init + `SIGHUP`, si diventa Zombie, `SIGCHLD` al padre, e se il padre era in `wait` lo si sveglia e si libera il PCB.

## Collegamenti

- **Concetti correlati**: [[fork]] · [[Segnali]] · [[Stati di un Processo]] · [[disastrOS]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Attesa della terminazione: wait|Lezione 6 — Attesa della terminazione: wait]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Processi zombie|Lezione 6 — Processi zombie]]
> - [[08 - SO - disastrOS#La syscall wait|Lezione 8 — La syscall wait]]
> - [[08 - SO - disastrOS#La syscall exit|Lezione 8 — La syscall exit]]
