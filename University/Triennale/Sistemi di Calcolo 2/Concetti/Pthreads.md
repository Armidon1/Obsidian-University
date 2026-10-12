---
title: Pthreads
tags:
  - sistemi-di-calcolo-2
  - concetto
  - thread
  - posix
---

# Pthreads

> [!summary] In breve
> Interfaccia POSIX per i thread (`pthread.h`, `-lpthread`): `pthread_create`, `pthread_exit`, `pthread_join`, `pthread_detach`. Più leggera di `fork`.

```c
pthread_t t;
int *arg = malloc(sizeof(int)); *arg = 7;          // un argomento per thread
int ret = pthread_create(&t, NULL, fun, arg);      // 0 oppure codice d'errore
pthread_join(t, NULL);                             // come waitpid per i thread
```

- I thread sono "pari" (nessuna gerarchia); `main` è il primo thread.
- Terminazione: `return` dalla funzione, `pthread_exit`, `exit` (termina tutto il processo), fine del `main` (se non termina con `pthread_exit`).
- Modelli di programma: manager/worker, pipeline.
- Gli accessi alla memoria condivisa vanno sincronizzati dal programmatore.

## Collegamenti

- **Concetti correlati**: [[Thread]] · [[Thread Safety e Race Condition]] · [[User Level Thread e Kernel Level Thread]] · [[Semafori]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[01 - SDC2 - Processi e Thread#Case study: Pthreads|Lezione 1 — Case study: Pthreads]]
> - [[01 - SDC2 - Processi e Thread#Creazione e terminazione|Lezione 1 — Creazione e terminazione]]
