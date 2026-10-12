---
title: Produttore-Consumatore
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
  - problemi-classici
---

# Produttore-Consumatore

> [!summary] In breve
> Produttori mettono dati in un buffer e consumatori li prelevano: niente inserimenti in un buffer pieno, niente prelievi da uno vuoto, un solo accesso alla volta.

```c
semaphore s = 1, n = 0, e = N;   // mutua esclusione, elementi, posti liberi
producer: produce(); wait(e); wait(s); append(); signal(s); signal(n);
consumer: wait(n); wait(s); take(); signal(s); signal(e); consume();
```

- Con semafori binari: il test su `n` fuori dalla sezione critica fa consumare un elemento inesistente (n = −1); metterlo dentro causa deadlock; la soluzione è la copia locale `m = n`.
- **Scambiare due `wait`** (es. `wait(s)` prima di `wait(e)`) porta a **deadlock**; scambiare due `signal` è innocuo.
- Varianti: monitor (`notfull`, `notempty`), message passing (mailbox `mayproduce` / `mayconsume`).

## Collegamenti

- **Concetti correlati**: [[Semafori]] · [[Monitor]] · [[Message Passing]] · [[Shared Memory POSIX]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Produttore/consumatore|Lezione 2 — Produttore/consumatore]]
> - [[02 - SDC2 - Concorrenza#Buffer circolare finito|Lezione 2 — Buffer circolare finito]]
> - [[05 - SDC2 - Comunicazione tra Processi#Produttore/consumatore con shared memory|Lezione 5 — Produttore/consumatore con shared memory]]
