---
title: Tassonomia di Flynn
tags:
  - sistemi-di-calcolo-2
  - concetto
  - architettura
  - parallelismo
---

# Tassonomia di Flynn

> [!summary] In breve
> Classifica i calcolatori per numero di flussi di istruzioni e di dati: SISD (uniprocessore), SIMD (vettoriali, GPU), MISD (non realizzato), MIMD (multicore, cluster).

| | Dati singoli | Dati multipli |
| --- | --- | --- |
| **Istruzione singola** | SISD | SIMD |
| **Istruzioni multiple** | MISD | MIMD |

- MIMD a **memoria condivisa** (tightly coupled): master/slave o **SMP**.
- MIMD a **memoria distribuita** (loosely coupled): **cluster**.

## Collegamenti

- **Concetti correlati**: [[Symmetric Multiprocessing]] · [[Cluster]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[01 - SDC2 - Processi e Thread#Tassonomia di Flynn|Lezione 1 — Tassonomia di Flynn]]
> - [[01 - SDC2 - Processi e Thread#Architetture dei processori paralleli|Lezione 1 — Architetture dei processori paralleli]]
