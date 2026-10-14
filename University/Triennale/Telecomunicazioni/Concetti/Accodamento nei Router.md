---
title: Accodamento nei Router
tags:
  - telecomunicazioni
  - concetto
  - router
  - code
---

# Accodamento nei Router

> [!summary] In breve
> Le code si formano alle porte di **ingresso** (struttura lenta, **HOL blocking**) e di **uscita** (molti pacchetti verso la stessa porta). Con il buffer pieno i pacchetti vengono scartati, ed è qui che avvengono le perdite.

- $R_{switch} = N \cdot R_{line}$ → accodamento in ingresso trascurabile, ma in uscita può comunque formarsi una coda (N pacchetti per la stessa uscita).
- **HOL blocking**: il pacchetto dietro uno bloccato aspetta anche se la sua uscita è libera; la coda esplode già al **58%** del carico.
- Politiche di scarto: **drop-tail**, rimozione dalla coda, **AQM** (es. **RED**) che scarta o marca prima che il buffer sia pieno.
- Dimensione del buffer: $B = RTT \cdot C$ (10 Gbps × 250 ms = 2,5 Gbit), oppure $B = RTT \cdot C/\sqrt{N}$ con $N$ flussi.

## Collegamenti

- **Concetti correlati**: [[Scheduling dei Pacchetti]] · [[Strutture di Commutazione]] · [[Intensità di Traffico]] · [[ECN]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Dove si verifica l'accodamento?|Capitolo 4 — Dove si verifica l'accodamento?]]
> - [[04 - TLC - Livello di rete - piano dei dati#Accodamento in ingresso|Capitolo 4 — Accodamento in ingresso]]
> - [[04 - TLC - Livello di rete - piano dei dati#Accodamento in uscita|Capitolo 4 — Accodamento in uscita]]
