---
title: Architettura a Strati
tags:
  - sistemi-operativi
  - concetto
  - architettura
  - portabilita
---

# Architettura a Strati

> [!summary] In breve
> Ogni strato offre un'astrazione (API) a quello superiore e usa solo i servizi di quello inferiore: è questo che rende i programmi portabili.

Strati, dal basso verso l'alto: **hardware → kernel → system standard (POSIX/Win32) → libc (language standard) → programmi utente**.

| Livello | Portabilità |
| --- | --- |
| **Syscall** | specifiche del kernel, nessuna portabilità |
| **System standard** (POSIX, Win32) | portabile tra OS della stessa famiglia |
| **Language standard** (libc) | portabile ovunque esista la libreria, ma non copre tutto (es. socket) |

- **Regola di design**: le funzionalità di alto livello si costruiscono *solo* su quelle di livello inferiore.
- **Regola pratica**: un'applicazione usa sempre **lo strato più alto possibile**.
- Esempio: `printf` (libc) → `vfprintf` → … → syscall `write`. Lo si vede con `strace`.

## Collegamenti

- **Concetti correlati**: [[Sistema Operativo]] · [[System Call]] · [[vDSO]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[01 - SO - Introduzione e Git#Organizzazione a strati|Lezione 1 — Organizzazione a strati]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Standard di linguaggio e standard di sistema|Lezione 6 — Standard di linguaggio e standard di sistema]]
