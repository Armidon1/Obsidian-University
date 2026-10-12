---
title: Deadlock
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
---

# Deadlock

> [!summary] In breve
> Blocco permanente di un insieme di processi, ognuno in attesa di un evento che solo un altro processo bloccato dell'insieme può generare.

- Esempi: incrocio con quattro auto; P ha D e vuole T, Q ha T e vuole D; due `receive` bloccanti che si aspettano a vicenda; richieste di memoria che superano la disponibilità.
- Condizioni (Coffman): mutual exclusion, hold and wait, no preemption, circular wait.
- Approcci: prevention, avoidance, detection + recovery (o ignorarlo).
- Diverso dal **livelock** (i processi si muovono ma non progrediscono) e dalla **starvation** (un processo non viene mai servito).

## Collegamenti

- **Concetti correlati**: [[Condizioni di Coffman]] · [[Gestione del Deadlock]] · [[Grafo di Allocazione delle Risorse]] · [[Risorse Riutilizzabili e Consumabili]] · [[Problema dei Cinque Filosofi]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Deadlock|Lezione 3 — Deadlock]]
> - [[03 - SDC2 - Deadlock#Le quattro condizioni|Lezione 3 — Le quattro condizioni]]
