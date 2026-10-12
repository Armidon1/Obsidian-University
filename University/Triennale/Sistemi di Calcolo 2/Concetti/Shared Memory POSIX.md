---
title: Shared Memory POSIX
tags:
  - sistemi-di-calcolo-2
  - concetto
  - ipc
  - memoria
---

# Shared Memory POSIX

> [!summary] In breve
> `shm_open` crea un oggetto di memoria condivisa (un fd), `ftruncate` lo dimensiona, `mmap` lo mappa nel processo; poi si legge e scrive con un puntatore, senza passare dal kernel.

```c
int fd = shm_open("MY_PAGE", O_CREAT | O_RDWR, 0666);
ftruncate(fd, SIZE);
char *p = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, fd, 0);
sprintf(p, "Hello World!");
close(fd);
// ...
shm_unlink("MY_PAGE");      // vuole il NOME
```

- `MAP_SHARED`: le scritture sono visibili agli altri processi.
- La sincronizzazione (es. il produttore/consumatore) usa semafori **named** o in memoria condivisa.

## Collegamenti

- **Concetti correlati**: [[Inter-Process Communication]] · [[mmap]] · [[Produttore-Consumatore]] · [[Semafori]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[05 - SDC2 - Comunicazione tra Processi#Memoria condivisa|Lezione 5 — Memoria condivisa]]
> - [[05 - SDC2 - Comunicazione tra Processi#API POSIX|Lezione 5 — API POSIX]]
