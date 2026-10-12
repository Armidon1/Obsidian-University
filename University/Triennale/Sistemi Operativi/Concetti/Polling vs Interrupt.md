---
title: Polling vs Interrupt
tags:
  - sistemi-operativi
  - concetto
  - interrupt
  - io
---

# Polling vs Interrupt

> [!summary] In breve
> Polling: un ciclo interroga continuamente i dispositivi (spreca CPU ed energia). Interrupt: la CPU dorme e viene svegliata dall'evento.

```c
// polling
while (1) { if (key_pressed) handleKey(); if (disk_finished) handleDisk(); }
// interrupt
void keyISR(); void diskISR();
while (1) halt();   // sleep_cpu() su AVR
```

- Le ISR fanno parte del kernel: un OS è una **macchina interrupt-based** che dorme quando non succede nulla.
- Anche il **busy waiting** su un flag (`while(!flag);`) è una forma di polling: meglio `sleep_cpu()` e ricontrollare il flag al risveglio.

## Collegamenti

- **Concetti correlati**: [[Interrupt]] · [[Timer AVR]] · [[Sistema Operativo]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Polling vs interrupt|Lezione 6 — Polling vs interrupt]]
> - [[04 - SO - Hardware e AVR#Evitare il busy waiting|Lezione 4 — Evitare il busy waiting]]
> - [[06 - SDC - Esecuzione dei programmi#Da waiting a ready: interrupt vs polling|Sistemi di Calcolo, cap. 6 — Da waiting a ready: interrupt vs polling]]
