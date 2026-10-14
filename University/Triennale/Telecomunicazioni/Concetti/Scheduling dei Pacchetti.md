---
title: Scheduling dei Pacchetti
tags:
  - telecomunicazioni
  - concetto
  - router
  - code
  - qos
---

# Scheduling dei Pacchetti

> [!summary] In breve
> Il packet scheduler decide l'ordine di trasmissione sulla porta di uscita: **FIFO**, **priorità** (non prelazionabile), **round robin**, **WFQ** (round robin pesato con banda garantita).

| Disciplina | Regola | Note |
| --- | --- | --- |
| FIFO | ordine di arrivo | nessuna garanzia |
| Priorità | prima la classe più alta non vuota | **non prelazionabile**: non interrompe la trasmissione in corso |
| Round robin | classi a turno | conservativo (work-conserving) |
| WFQ | round robin pesato | classe $i$: almeno $R \cdot \dfrac{w_i}{\sum_j w_j}$ |

- Esempio di priorità (1, 3, 4 alti; 2, 5 bassi) → ordine **1, 3, 2, 4, 5**.
- Round robin con 2 classi (1, 2, 4 | 3, 5) → **1, 3, 2, 4, 5**.
- WFQ con pesi 5/3/2 su 10 Mbps → 5/3/2 Mbps; se la classe 3 è vuota → 6,25/3,75.

## Collegamenti

- **Concetti correlati**: [[Accodamento nei Router]] · [[Architettura di un Router]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Schedulazione dei pacchetti|Capitolo 4 — Schedulazione dei pacchetti]]
> - [[04 - TLC - Livello di rete - piano dei dati#Primo arrivato, primo servito (FIFO)|Capitolo 4 — Primo arrivato, primo servito (FIFO)]]
> - [[04 - TLC - Livello di rete - piano dei dati#Code con priorità|Capitolo 4 — Code con priorità]]
> - [[04 - TLC - Livello di rete - piano dei dati#Round robin e accodamento equo ponderato (WFQ)|Capitolo 4 — Round robin e accodamento equo ponderato (WFQ)]]
