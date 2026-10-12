---
title: Loader ed ELF
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - processi
---

# Loader ed ELF

> [!summary] In breve
> Il loader (invocato da exec) legge l'eseguibile ELF, ne mappa i segmenti in memoria, carica e collega le librerie dinamiche e salta all'entry point.

- **ELF**: ELF header, **program header table** (segmenti, per il loader), sezioni (`.text`, `.rodata`, `.data`…), **section header table** (sezioni, per il linker e il debugger).
- Passi: decodifica dell'header → il dynamic linker carica le `.so` → risolve i simboli (ricorsivamente) → adatta gli indirizzi.
- Su AVR, `.elf` → `.hex` con `avr-objcopy`.

## Collegamenti

- **Concetti correlati**: [[exec e Variabili d'Ambiente]] · [[Linking Statico e Dinamico]] · [[Program File e Processo]] · [[Immagine di Memoria di un Processo]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Dal program file al processo|Lezione 10 — Dal program file al processo]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Lanciare un nuovo programma: exec|Lezione 6 — Lanciare un nuovo programma: exec]]
