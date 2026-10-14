---
title: Controller SDN
tags:
  - telecomunicazioni
  - concetto
  - sdn
  - piano-controllo
---

# Controller SDN

> [!summary] In breve
> Nella SDN il piano di controllo è esterno agli switch: un **controller** logicamente centralizzato (ma fisicamente distribuito) gestisce lo stato della rete e installa le tabelle dei flussi; le **applicazioni di controllo** sopra di esso decidono instradamento, accessi e bilanciamento.

Quattro caratteristiche: **inoltro basato sui flussi**, **separazione dei piani**, **controllo esterno** agli switch, **rete programmabile**.

| Livello del controller | Contenuto |
| --- | --- |
| Interfaccia **northbound** | API REST, Network graph, Intent |
| Stato globale della rete | Statistics, Flow tables, Link-state, Host, Switch info |
| Comunicazione **southbound** | OpenFlow, SNMP |

- Esempio: cade s1–s2 → port-status → aggiornamento del database dei collegamenti → l'applicazione Dijkstra ricalcola → gestore delle tabelle dei flussi → OpenFlow aggiorna s1, s2, s4.
- Controller: NOX (il primo), **OpenDaylight** (SAL, REST API), **ONOS** (Intent, core distribuito), ONIX (Google **B4**, utilizzo dei collegamenti al ~70%).
- Origini: Ethane (2007). Generalizzazione: **NFV**.
- Analogia: dal mainframe verticale al PC "orizzontale".

## Collegamenti

- **Concetti correlati**: [[Protocollo OpenFlow]] · [[Inoltro Generalizzato e OpenFlow]] · [[Algoritmi di Instradamento]] · [[Sistema Distribuito]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.5 Il piano di controllo SDN|Capitolo 5 — 5.5 Il piano di controllo SDN]]
> - [[05 - TLC - Livello di rete - piano di controllo#Controller SDN e applicazioni di controllo|Capitolo 5 — Controller SDN e applicazioni di controllo]]
> - [[05 - TLC - Livello di rete - piano di controllo#Interazione tra piano dei dati e piano di controllo: un esempio|Capitolo 5 — Interazione tra piano dei dati e piano di controllo: un esempio]]
> - [[05 - TLC - Livello di rete - piano di controllo#SDN: il passato e il futuro|Capitolo 5 — SDN: il passato e il futuro]]
