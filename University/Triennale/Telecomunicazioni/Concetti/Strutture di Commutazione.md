---
title: Strutture di Commutazione
tags:
  - telecomunicazioni
  - concetto
  - router
---

# Strutture di Commutazione

> [!summary] In breve
> Le tre tecniche per spostare i pacchetti dentro il router: **in memoria** (CPU, throughput < B/2), **tramite bus** (un pacchetto alla volta) e **crossbar** (più pacchetti in parallelo, non-blocking tranne che verso la stessa uscita).

| Tecnica | Pro | Contro | Esempio |
| --- | --- | --- | --- |
| Memoria | semplice | throughput < $B/2$, un pacchetto alla volta | Cisco 8500 |
| Bus | niente CPU, etichetta interna | un pacchetto alla volta, limite di banda del bus | Cisco 6500 (32 Gbps) |
| Crossbar ($2n$ bus) | **parallelismo**, non-blocking | conflitto se due pacchetti vanno alla stessa uscita | Cisco 12000 |

- Varianti: reti a più stadi (Cisco CRS) e divisione in chunk ("spray") su $K$ strutture parallele.

## Collegamenti

- **Concetti correlati**: [[Architettura di un Router]] · [[Accodamento nei Router]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Struttura di commutazione|Capitolo 4 — Struttura di commutazione]]
