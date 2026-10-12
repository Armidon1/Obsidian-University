---
title: Sistema Operativo
tags:
  - sistemi-operativi
  - concetto
  - kernel
---

# Sistema Operativo

> [!summary] In breve
> Software che controlla l'esecuzione degli altri programmi, gestisce le risorse (CPU, memoria, I/O) e fornisce un'astrazione dell'hardware.

- **Due compiti centrali**: gestire le risorse prevenendo i conflitti, e gestire gli errori di programmi e hardware.
- **Per l'utente**: risorse gestite in modo efficiente, facili da usare, programmi eseguiti correttamente.
- **Servizi**: esecuzione di programmi, astrazioni di I/O, file system, IPC, gestione delle risorse, protezione, gestione delle eccezioni, statistiche d'uso.
- **Manager**: processi, memoria, I/O, file, rete, login, comandi.
- Gli strumenti forniti insieme all'OS (editor, compilatori, shell) **non** fanno parte del kernel, ma dell'ecosistema.
- Un OS moderno è una **macchina guidata dagli interrupt**: si attiva solo su interrupt, eccezioni e syscall.

## Collegamenti

- **Concetti correlati**: [[Architettura a Strati]] · [[Kernel Monolitico e Microkernel]] · [[Interrupt]] · [[System Call]] · [[Dual Mode]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SO - Introduzione e Git#Che cos'è un sistema operativo|Lezione 1 — Che cos'è un sistema operativo]]
> - [[01 - SO - Introduzione e Git#Servizi offerti da un OS|Lezione 1 — Servizi offerti da un OS]]
> - [[01 - SO - Introduzione e Git#Componenti di un OS moderno|Lezione 1 — Componenti di un OS moderno]]
> - [[01 - SDC - Cosa è un sistema di calcolo#Sistema operativo|Sistemi di Calcolo, cap. 1 — Sistema operativo]]
