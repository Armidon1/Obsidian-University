---
title: Architettura di un Router
tags:
  - telecomunicazioni
  - concetto
  - router
  - piano-dati
---

# Architettura di un Router

> [!summary] In breve
> Un router ha **porte di ingresso**, una **struttura di commutazione**, **porte di uscita** (tutte in hardware, piano dei dati) e un **processore di instradamento** (software, piano di controllo).

- **Porta di ingresso**: terminazione di linea → livello di collegamento → **ricerca** nella tabella (copiata su ogni line card) → struttura di commutazione. Controlla anche versione, checksum e TTL.
- **Porta di uscita**: accodamento → collegamento → linea.
- **Processore di instradamento**: protocolli di instradamento, calcolo della tabella, dialogo con il controller SDN, gestione di rete.
- Perché hardware: 10 Gbps e 64 byte → **51,2 ns** per pacchetto.
- "Porta" = interfaccia fisica, non porta TCP/UDP.
- Analogia della **rotonda**: casello = porta di ingresso, rotonda = struttura di commutazione, uscita = porta di uscita.

## Collegamenti

- **Concetti correlati**: [[Strutture di Commutazione]] · [[Accodamento nei Router]] · [[Longest Prefix Match]] · [[Inoltro e Instradamento]] · [[Router]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#4.2 Che cosa si trova all'interno di un router?|Capitolo 4 — 4.2 Che cosa si trova all'interno di un router?]]
> - [[04 - TLC - Livello di rete - piano dei dati#Elaborazione alle porte di ingresso e inoltro basato sulla destinazione|Capitolo 4 — Elaborazione alle porte di ingresso e inoltro basato sulla destinazione]]
> - [[04 - TLC - Livello di rete - piano dei dati#Elaborazione alle porte di uscita|Capitolo 4 — Elaborazione alle porte di uscita]]
