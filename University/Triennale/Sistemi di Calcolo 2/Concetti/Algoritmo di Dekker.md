---
title: Algoritmo di Dekker
tags:
  - sistemi-di-calcolo-2
  - concetto
  - mutua-esclusione
  - algoritmi
---

# Algoritmo di Dekker

> [!summary] In breve
> Mutua esclusione software per 2 processi: flag di interesse più una variabile `turn` che decide chi cede in caso di conflitto.

| Tentativo | Difetto |
| --- | --- |
| 1. solo `turn` | alternanza stretta |
| 2. controllo del flag altrui, poi il proprio flag | **niente mutua esclusione** |
| 3. il proprio flag, poi controllo | **deadlock** |
| 4. ritirarsi e riprovare | **livelock** |
| Dekker: flag + `turn` | corretto |

```c
flag[me] = true;
while (flag[other])
    if (turn == other) { flag[me] = false; while (turn == other); flag[me] = true; }
/* CS */
turn = other; flag[me] = false;
```

Più semplice: Peterson (`flag[me] = true; turn = other; while (flag[other] && turn == other);`).

## Collegamenti

- **Concetti correlati**: [[Sezione Critica e Mutua Esclusione]] · [[Algoritmo di Dijkstra per la Mutua Esclusione]] · [[Algoritmo del Panettiere]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Mutua esclusione in software|Lezione 3 — Mutua esclusione in software]]
> - [[03 - SDC2 - Deadlock#Algoritmo di Dekker|Lezione 3 — Algoritmo di Dekker]]
