---
title: Thread
tags:
  - sistemi-di-calcolo
  - concetto
  - processi
  - concorrenza
---

# Thread

> [!summary] In breve
> Flusso di esecuzione indipendente dentro un processo: condivide codice, heap, globali e file aperti con gli altri thread, ma ha stack, registri ed errno propri. In POSIX: `pthread_create`, `pthread_exit`, `pthread_join`, `pthread_detach`.

| Processi | Thread |
| --- | --- |
| `fork` | `pthread_create(&t, NULL, f, arg)` |
| `exit` | `pthread_exit(retval)` |
| `wait` | `pthread_join(t, &retval)` |
| | `pthread_detach(t)` |

- Le funzioni restituiscono 0 o un **codice di errore** (non −1). Compilare con `-lpthread`.
- Un solo argomento `void*`; il valore di ritorno non deve puntare allo stack del thread.
- `return` dal `main` termina tutti i thread; `pthread_exit` nel `main` li lascia continuare.
- Le risorse condivise vanno **sincronizzate**.

## Collegamenti

- **Concetti correlati**: [[Program File e Processo]] · [[fork]] · [[Context Switch]] · [[Puntatori a Funzione]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SDC - Esecuzione dei programmi#Thread|Lezione 6 — Thread]]
> - [[06 - SDC - Esecuzione dei programmi#Esecuzione di più thread: Pthreads|Lezione 6 — Esecuzione di più thread: Pthreads]]
