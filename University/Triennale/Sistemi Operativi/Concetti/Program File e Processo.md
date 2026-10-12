---
title: Program File e Processo
tags:
  - sistemi-operativi
  - concetto
  - processi
---

# Program File e Processo

> [!summary] In breve
> Il program file è l'eseguibile su disco (codice macchina + metadati); un processo è un programma in esecuzione. Da un program file possono nascere più processi.

- Il **program file** contiene il codice macchina e le meta-informazioni (sezioni, librerie, entry point) necessarie per costruire una **memory image**; per farlo serve l'OS (il **loader**).
- Un **processo** è un programma in esecuzione. Il suo stato comprende:
  - i **registri** della CPU;
  - la **memoria**: `.text`, `.data`, `.bss`, heap, stack, regioni mappate;
  - le **risorse**: file descriptor, socket, semafori.
- Lo stesso program file caricato più volte dà **processi distinti** (ognuno con il proprio PID e la propria memoria virtuale).
- Un programma può essere eseguito direttamente dalla CPU, da un interprete o da un emulatore; in ogni caso alla fine è la CPU a eseguire istruzioni.

## Collegamenti

- **Concetti correlati**: [[Immagine di Memoria di un Processo]] · [[Loader ed ELF]] · [[Contesto di un Processo]] · [[Process Control Block]] · [[fork]] · [[exec e Variabili d'Ambiente]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[02 - SO - Programmi, Makefile e pkg-config#Program file e processo|Lezione 2 — Program file e processo]]
> - [[05 - SO - Stack e Context Switch#Processo e contesto|Lezione 5 — Processo e contesto]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Processi|Lezione 6 — Processi]]
> - [[06 - SDC - Esecuzione dei programmi#Processi|Sistemi di Calcolo, cap. 6 — Processi]]
