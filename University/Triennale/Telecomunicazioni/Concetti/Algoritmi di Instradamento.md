---
title: Algoritmi di Instradamento
tags:
  - telecomunicazioni
  - concetto
  - routing
  - piano-controllo
---

# Algoritmi di Instradamento

> [!summary] In breve
> Trovano i percorsi a **costo minimo** su un grafo $G = (N, E)$ in cui i nodi sono router e gli archi collegamenti con costo $c(x,y)$. Si classificano come centralizzati/decentralizzati, statici/dinamici, sensibili/insensibili al carico.

| Criterio | Opzioni |
| --- | --- |
| Informazione | **centralizzato** (globale) = **link-state** · **decentralizzato** = **distance-vector** |
| Dinamica | statico (manuale) · dinamico (adattivo, rischio di cicli e oscillazioni) |
| Carico | sensibile · **insensibile** (RIP, OSPF, BGP) |

- Grafo non orientato: $c(x,y) = c(y,x)$, e $\infty$ se non c'è l'arco.
- Costo di un percorso = somma dei costi; con costi uguali, costo minimo = percorso più breve.
- Due approcci al piano di controllo: **per router** (OSPF, BGP) oppure **logicamente centralizzato** (SDN).

## Collegamenti

- **Concetti correlati**: [[Instradamento Link-State]] · [[Instradamento Distance-Vector]] · [[Inoltro e Instradamento]] · [[Grafo Pesato]] · [[Controller SDN]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.1 Introduzione|Capitolo 5 — 5.1 Introduzione]]
> - [[05 - TLC - Livello di rete - piano di controllo#5.2 Algoritmi di instradamento|Capitolo 5 — 5.2 Algoritmi di instradamento]]
