---
title: Semafori
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
  - semafori
---

# Semafori

> [!summary] In breve
> Intero con tre operazioni atomiche: init (≥ 0), semWait (decrementa; se < 0 il processo si blocca), semSignal (incrementa; se ≤ 0 sveglia un processo in coda).

- Valore negativo = −(numero di processi in coda).
- **Binario**: valori 0/1. **Mutex**: binario, ma lo sblocca solo chi l'ha bloccato.
- **Strong**: coda FIFO (niente starvation). **Weak**: ordine non specificato.
- Le operazioni vanno rese atomiche (compare&swap con un breve busy waiting, oppure disabilitando gli interrupt).

```c
#include <semaphore.h>
sem_t s;
sem_init(&s, 0, 1);   // pshared = 0: tra thread; 1 unità
sem_wait(&s);  /* sezione critica */  sem_post(&s);
sem_destroy(&s);
```

- Java: `Semaphore(n, fair)`, `acquire()`, `release()`. Python: `threading.Semaphore()`.
- Tra processi: semafori **named** (`sem_open`).

## Collegamenti

- **Concetti correlati**: [[Sezione Critica e Mutua Esclusione]] · [[Produttore-Consumatore]] · [[Lettori-Scrittori]] · [[Monitor]] · [[Problema dei Cinque Filosofi]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Semafori|Lezione 2 — Semafori]]
> - [[02 - SDC2 - Concorrenza#Semaforo binario|Lezione 2 — Semaforo binario]]
> - [[02 - SDC2 - Concorrenza#Implementazione dei semafori|Lezione 2 — Implementazione dei semafori]]
> - [[02 - SDC2 - Concorrenza#Semafori POSIX|Lezione 2 — Semafori POSIX]]
