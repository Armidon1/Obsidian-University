---
title: Protocollo BGP
tags:
  - telecomunicazioni
  - concetto
  - routing
  - bgp
  - inter-as
---

# Protocollo BGP

> [!summary] In breve
> **Border Gateway Protocol** (RFC 4271) è il protocollo inter-AS di Internet, la "colla" tra gli ISP. Propaga la **raggiungibilità dei prefissi** CIDR e sceglie i percorsi migliori secondo attributi e **politiche**.

- Sessioni su **TCP porta 179**: **eBGP** tra gateway di AS diversi, **iBGP** (maglia completa) dentro l'AS, non necessariamente su collegamenti fisici.
- Propagazione: 3a →eBGP "AS3 x"→ 2c →iBGP→ 2a →eBGP "AS2 AS3 x"→ 1c →iBGP→ tutto AS1.
- **Rotta** = prefisso + attributi:
  - **AS-PATH**: gli AS attraversati; serve anche a evitare i cicli (se c'è il proprio AS, l'annuncio si rifiuta);
  - **NEXT-HOP**: interfaccia del router che inizia l'AS-PATH.
- Tabella di inoltro: righe $(x, I)$.
- Politiche: le reti **stub** e **multi-homed** non annunciano percorsi di transito; un provider trasporta solo traffico dei propri clienti.

## Collegamenti

- **Concetti correlati**: [[Selezione delle Rotte BGP]] · [[Hot Potato Routing]] · [[Anycast IP]] · [[Sistema Autonomo]] · [[BGP]] · [[CIDR]] · [[Aggregazione di Indirizzi]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.4 Instradamento tra ISP: BGP|Capitolo 5 — 5.4 Instradamento tra ISP: BGP]]
> - [[05 - TLC - Livello di rete - piano di controllo#Il ruolo di BGP|Capitolo 5 — Il ruolo di BGP]]
> - [[05 - TLC - Livello di rete - piano di controllo#Distribuzione delle informazioni dei cammini in BGP|Capitolo 5 — Distribuzione delle informazioni dei cammini in BGP]]
> - [[05 - TLC - Livello di rete - piano di controllo#Politiche di instradamento|Capitolo 5 — Politiche di instradamento]]
> - [[05 - TLC - Livello di rete - piano di controllo#Retrospettiva: come essere presenti in Internet|Capitolo 5 — Retrospettiva: come essere presenti in Internet]]
