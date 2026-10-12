---
title: Risorse Riutilizzabili e Consumabili
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
---

# Risorse Riutilizzabili e Consumabili

> [!summary] In breve
> Riutilizzabili: usate da un processo alla volta e poi rilasciate (CPU, memoria, file, semafori). Consumabili: create e distrutte (interrupt, segnali, messaggi, dati nei buffer).

- Deadlock con risorse riutilizzabili: lock acquisiti in ordine opposto (P: D poi T; Q: T poi D).
- Deadlock con risorse consumabili: P1 e P2 fanno entrambi `receive` bloccante prima di `send`.

## Collegamenti

- **Concetti correlati**: [[Deadlock]] · [[Message Passing]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Risorse riutilizzabili e consumabili|Lezione 3 — Risorse riutilizzabili e consumabili]]
