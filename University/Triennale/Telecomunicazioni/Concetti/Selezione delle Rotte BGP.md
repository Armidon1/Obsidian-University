---
title: Selezione delle Rotte BGP
tags:
  - telecomunicazioni
  - concetto
  - bgp
---

# Selezione delle Rotte BGP

> [!summary] In breve
> Con più rotte verso lo stesso prefisso BGP elimina in sequenza: **preferenza locale** più alta → **AS-PATH più breve** → **NEXT-HOP più vicino** (hot potato) → identificatori BGP.

1. **Preferenza locale**: decisa dall'amministratore (politica).
2. **AS-PATH più breve**: come Bellman-Ford con gli hop tra AS.
3. **NEXT-HOP più vicino** secondo il costo intra-AS: **hot potato**.
4. Identificatori BGP.

Esempio: router 1b, rotte via 2a ("AS2 AS3", costo 2) e via 3d ("AS3", costo 3) → l'hot potato da solo sceglierebbe 2a, ma la regola 2 sceglie **3d**. BGP non è puramente egoista.

## Collegamenti

- **Concetti correlati**: [[Protocollo BGP]] · [[Hot Potato Routing]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Selezione delle rotte migliori|Capitolo 5 — Selezione delle rotte migliori]]
> - [[05 - TLC - Livello di rete - piano di controllo#Algoritmo di selezione delle rotte|Capitolo 5 — Algoritmo di selezione delle rotte]]
