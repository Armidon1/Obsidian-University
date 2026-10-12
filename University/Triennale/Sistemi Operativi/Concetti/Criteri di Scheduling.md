---
title: Criteri di Scheduling
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# Criteri di Scheduling

> [!summary] In breve
> Massimizzare utilizzo della CPU e throughput; minimizzare turnaround, waiting e response time.

| Metrica | Definizione |
| --- | --- |
| Utilizzo | frazione di tempo in cui la CPU è occupata |
| Throughput | processi completati per unità di tempo |
| Turnaround | fine − arrivo |
| Waiting | tempo passato nella coda ready (= turnaround − burst) |
| Response | dall'arrivo della richiesta all'inizio della risposta |

- Interattivi → response time basso; batch → throughput alto.
- Si visualizzano con **diagrammi di Gantt**.

## Collegamenti

- **Concetti correlati**: [[First Come First Served]] · [[Shortest Job First]] · [[Round Robin]] · [[Valutazione degli Algoritmi di Scheduling]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Criteri di scheduling|Lezione 9 — Criteri di scheduling]]
> - [[09 - SO - CPU Scheduling#Diagrammi di Gantt|Lezione 9 — Diagrammi di Gantt]]
