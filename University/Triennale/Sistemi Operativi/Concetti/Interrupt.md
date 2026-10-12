---
title: Interrupt
tags:
  - sistemi-operativi
  - concetto
  - hardware
  - interrupt
---

# Interrupt

> [!summary] In breve
> Evento esterno segnalato su un pin che fa salvare PC e flag sullo stack e saltare a una ISR (scelta tramite l'interrupt vector), che termina con `reti`.

1. La CPU controlla il pin di interrupt all'inizio di ogni ciclo/istruzione.
2. Handshake: **IRQ** → la CPU risponde con **INTA** → la periferica mette il proprio numero sul data bus.
3. Si salvano **PC e FLAGS** sullo stack e si salta a `vector[n]`.
4. La ISR (nessun argomento, ritorna `void`) termina con **`reti`**, che ripristina anche i flag (al contrario di `ret`).

- In C: `ISR(TIMER5_COMPA_vect) { ... }` (AVR) oppure `__attribute__((interrupt))`.
- Mentre si gestisce un interrupt, quelli dello stesso tipo sono disabilitati. Le ISR devono essere **brevi** (alzano un flag e delegano il lavoro).
- Le variabili condivise con una ISR vanno dichiarate `volatile`; `cli()`/`sei()` disabilitano/abilitano gli interrupt.
- Sono la base del **preemptive multitasking** e di tutto l'OS.

## Collegamenti

- **Concetti correlati**: [[Interrupt Vector]] · [[Eccezioni]] · [[Polling vs Interrupt]] · [[Context Switch]] · [[Timer AVR]] · [[Interrupt Esterni AVR]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Interrupt|Lezione 4 — Interrupt]]
> - [[04 - SO - Hardware e AVR#L'interrupt handler dal punto di vista software|Lezione 4 — L'interrupt handler dal punto di vista software]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Cosa succede quando arriva un interrupt|Lezione 6 — Cosa succede quando arriva un interrupt]]
> - [[06 - SDC - Esecuzione dei programmi#Interruzioni|Sistemi di Calcolo, cap. 6 — Interruzioni]]
