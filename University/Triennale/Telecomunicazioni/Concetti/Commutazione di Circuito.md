---
title: Commutazione di Circuito
tags:
  - telecomunicazioni
  - concetto
  - nucleo
  - commutazione
---

# Commutazione di Circuito

> [!summary] In breve
> Prima di comunicare si stabilisce un **circuito** end-to-end e le risorse (banda, buffer) restano **riservate** per tutta la sessione. Garantisce una velocità costante, ma spreca risorse nei periodi di silenzio.

- Esempio classico: la **rete telefonica** tradizionale.
- I circuiti in un collegamento si realizzano con **FDM** o **TDM**.
- Il tempo di trasmissione **non dipende dal numero di collegamenti** (niente store-and-forward).
- Esempio: 640.000 bit, TDM con 24 slot su 1,536 Mbps → 64 kbps → 10 s + 0,5 s di setup = **10,5 s**.

| Circuito | Pacchetto |
| --- | --- |
| risorse preallocate | risorse su richiesta |
| ritardi prevedibili | ritardi variabili |
| spreco nei silenzi | condivisione efficiente |
| setup complesso | nessun setup |

## Collegamenti

- **Concetti correlati**: [[Commutazione di Pacchetto]] · [[Multiplexing FDM e TDM]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Commutazione di circuito|Capitolo 1 — Commutazione di circuito]]
> - [[01 - TLC - Reti di calcolatori e Internet#Confronto tra commutazione di pacchetto e di circuito|Capitolo 1 — Confronto tra commutazione di pacchetto e di circuito]]
