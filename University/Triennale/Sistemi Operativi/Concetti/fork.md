---
title: fork
tags:
  - sistemi-operativi
  - concetto
  - processi
  - syscall
  - unix
---

# fork

> [!summary] In breve
> Syscall che crea un processo figlio copiando lo spazio di memoria del padre; restituisce 0 nel figlio e il PID del figlio nel padre.

```c
pid_t pid = fork();
if (pid == 0) { /* figlio */ }
else if (pid > 0) { /* padre: pid = PID del figlio */ }
else { /* errore */ }
```

- Dopo la `fork` ci sono **due flussi paralleli**; il figlio eredita una copia dell'ambiente e dei descriptor.
- Grazie al **[[Copy on Write]]** la memoria non viene copiata davvero finché nessuno scrive.
- `vfork`: non copia nulla, da usare solo se il figlio fa subito `exec`.
- In disastrOS: crea un PCB in Ready, imposta `parent = running`, lo aggiunge a `children` e restituisce il PID (versione user space: `spawn(f, arg)`).

## Collegamenti

- **Concetti correlati**: [[exec e Variabili d'Ambiente]] · [[wait e Processi Zombie]] · [[Copy on Write]] · [[Process Control Block]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Creazione di un processo: fork|Lezione 6 — Creazione di un processo: fork]]
> - [[08 - SO - disastrOS#La syscall fork|Lezione 8 — La syscall fork]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#vfork|Lezione 6 — vfork]]
> - [[06 - SDC - Esecuzione dei programmi#Creare processi: fork|Sistemi di Calcolo, cap. 6 — Creare processi: fork]]
