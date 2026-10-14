---
title: Switch e Router a Confronto
tags:
  - telecomunicazioni
  - concetto
  - switch
  - router
---

# Switch e Router a Confronto

> [!summary] In breve
> Entrambi sono store-and-forward, ma lo **switch** lavora al livello 2 con i MAC (plug-and-play, veloce, topologia ad albero, nessuna protezione dalle tempeste di broadcast), mentre il **router** lavora al livello 3 con gli IP (instradamento ottimale, isolamento, da configurare).

| | Hub | Router | Switch |
| --- | --- | --- | --- |
| Isolamento del traffico | No | Sì | Sì |
| Plug and play | Sì | No | Sì |
| Instradamento ottimale | No | Sì | No |

- Switch: tabelle ARP grandi nelle reti grandi; un host che genera broadcast continui fa collassare la rete.
- Router: niente cicli grazie al TTL e agli indirizzi gerarchici; topologie ricche con percorsi ridondanti.
- Regola pratica: reti di centinaia di host → switch; migliaia → anche router.

## Collegamenti

- **Concetti correlati**: [[Switch a Livello di Collegamento]] · [[Architettura di un Router]] · [[Hub]] · [[Bridge]] · [[Router]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Switch e router a confronto|Capitolo 6 — Switch e router a confronto]]
