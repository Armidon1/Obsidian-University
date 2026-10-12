---
title: Thread Safety e Race Condition
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
---

# Thread Safety e Race Condition

> [!summary] In breve
> Race condition: il risultato dipende dall'ordine di esecuzione dei thread che accedono a dati condivisi. Un codice è thread-safe se può essere eseguito da più thread insieme senza race condition.

- Esempio: `count++` su una variabile condivisa = leggi, incrementa, scrivi; due thread intercalati perdono un incremento.
- Il "perdente" della corsa è chi scrive per ultimo: il suo valore è quello che resta.
- Una funzione di libreria che modifica strutture globali senza sincronizzazione **non è thread-safe** (es. `strtok`).
- Soluzione: mutua esclusione sulle sezioni critiche (semafori, mutex, monitor).

## Collegamenti

- **Concetti correlati**: [[Sezione Critica e Mutua Esclusione]] · [[Semafori]] · [[Pthreads]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[01 - SDC2 - Processi e Thread#Thread safety|Lezione 1 — Thread safety]]
> - [[02 - SDC2 - Concorrenza#Race condition|Lezione 2 — Race condition]]
