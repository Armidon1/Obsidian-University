---
title: User Level Thread e Kernel Level Thread
tags:
  - sistemi-di-calcolo-2
  - concetto
  - thread
---

# User Level Thread e Kernel Level Thread

> [!summary] In breve
> ULT: i thread sono gestiti da una libreria in spazio utente e il kernel vede solo il processo. KLT: il kernel conosce e schedula ogni thread.

| | ULT | KLT |
| --- | --- | --- |
| Chi li gestisce | libreria utente | kernel |
| Cambio di thread | senza mode switch (veloce) | mode switch verso il kernel |
| System call bloccante | blocca **tutto** il processo | blocca solo quel thread |
| Multiprocessore | non sfruttato | thread su core diversi |
| Portabilità | qualsiasi OS | dipende dall'OS |

- Modelli: molti-a-uno (ULT puri), uno-a-uno (Linux, Windows), molti-a-molti (approccio combinato, es. Solaris).
- Con gli ULT lo stato visto dalla libreria e quello visto dal kernel possono non coincidere.

## Collegamenti

- **Concetti correlati**: [[Thread]] · [[Pthreads]] · [[Process Control Block]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[01 - SDC2 - Processi e Thread#User Level Thread e Kernel Level Thread|Lezione 1 — User Level Thread e Kernel Level Thread]]
> - [[01 - SDC2 - Processi e Thread#Approcci combinati|Lezione 1 — Approcci combinati]]
