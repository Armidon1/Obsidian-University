---
title: Inoltro e Instradamento
tags:
  - telecomunicazioni
  - concetto
  - livello-rete
  - piano-dati
  - piano-controllo
---

# Inoltro e Instradamento

> [!summary] In breve
> L'**inoltro** (piano dei dati) sposta un pacchetto dall'ingresso all'uscita giusta di un router, localmente e in nanosecondi. L'**instradamento** (piano di controllo) calcola i percorsi su tutta la rete, in secondi, e riempie le tabelle di inoltro.

| | Inoltro | Instradamento |
| --- | --- | --- |
| Piano | dati | controllo |
| Ambito | singolo router | rete intera |
| Tempo | ns | s |
| Realizzazione | hardware | software |

- **Tabella di inoltro**: valore dell'intestazione → collegamento d'uscita.
- Piano di controllo **tradizionale**: un algoritmo in ogni router e protocolli di instradamento tra router.
- Piano di controllo **SDN**: un **controller remoto** calcola e distribuisce le tabelle.
- Il modello di servizio di Internet è **best effort**: nessuna garanzia di consegna, ordine, ritardo o banda.
- Analogia: l'instradamento è la pianificazione del viaggio, l'inoltro la scelta a ogni svincolo.

## Collegamenti

- **Concetti correlati**: [[Architettura di un Router]] · [[Longest Prefix Match]] · [[Inoltro Generalizzato e OpenFlow]] · [[BGP]] · [[Router]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#4.1 Panoramica del livello di rete|Capitolo 4 — 4.1 Panoramica del livello di rete]]
> - [[04 - TLC - Livello di rete - piano dei dati#Inoltro e instradamento: piano dei dati e piano di controllo|Capitolo 4 — Inoltro e instradamento: piano dei dati e piano di controllo]]
> - [[04 - TLC - Livello di rete - piano dei dati#Piano di controllo: l'approccio SDN|Capitolo 4 — Piano di controllo: l'approccio SDN]]
> - [[04 - TLC - Livello di rete - piano dei dati#Modelli di servizio|Capitolo 4 — Modelli di servizio]]
