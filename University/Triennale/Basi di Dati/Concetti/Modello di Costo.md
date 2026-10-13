---
title: Modello di Costo
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Modello di Costo

> [!summary] In breve
> Il costo delle operazioni si misura in pagine di memoria secondaria accedute: NP(R) pagine, NTP(R) tuple per pagina.

| Operazione | Costo |
|---|---|
| selezione, proiezione | $N_P(R)$ |
| join senza indici | $N_P(R) \times N_P(Q)$ |
| join con indice selettivo su Q | $N_P(R) + N_P(R) \times N_{TP}(R)$ |

Molte tuple o molti attributi o molti NULL → molte pagine → decomporre; join frequenti → accorpare.

## Collegamenti

- **Concetti correlati**: [[Ristrutturazione dello Schema Logico]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Cost Model for File Organizations]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#Modello di costo|Lezione 6 — Modello di costo]]
