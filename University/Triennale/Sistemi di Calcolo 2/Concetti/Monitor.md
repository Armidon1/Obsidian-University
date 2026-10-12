---
title: Monitor
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
---

# Monitor

> [!summary] In breve
> Costrutto di linguaggio che incapsula dati e procedure: un solo processo alla volta è nel monitor; la sincronizzazione avviene con condition variable (`cwait`, `csignal`).

- I dati locali sono accessibili solo tramite le procedure del monitor.
- `cwait(c)`: sospende il processo su c e libera il monitor. `csignal(c)`: sveglia un processo in attesa su c (se non c'è nessuno il segnale **si perde**, a differenza di un semaforo).
- Code: ingresso, una per condizione, urgent queue.
- Più facile da usare correttamente dei semafori (es. i metodi `synchronized` di Java).
- Nei monitor reali si scrive `while (cond) cwait(c);`.

## Collegamenti

- **Concetti correlati**: [[Semafori]] · [[Produttore-Consumatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Monitor|Lezione 2 — Monitor]]
> - [[02 - SDC2 - Concorrenza#Soluzione con un monitor|Lezione 2 — Soluzione con un monitor]]
