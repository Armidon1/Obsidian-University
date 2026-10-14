---
title: Costi della Congestione
tags:
  - telecomunicazioni
  - concetto
  - congestione
---

# Costi della Congestione

> [!summary] In breve
> Quando il traffico si avvicina alla capacità della rete crescono i ritardi, servono ritrasmissioni, si inoltrano copie inutili e si spreca il lavoro dei router a monte, fino al **collasso da congestione**.

| Scenario | Ipotesi | Costo |
| --- | --- | --- |
| 1 | 2 mittenti, buffer **illimitati** | throughput max $R/2$ per connessione, **ritardo → ∞** vicino a $R/2$ |
| 2 | buffer **finiti**, ritrasmissioni | ritrasmissioni per le perdite ($R/3$ di dati utili); copie inutili per timeout prematuri ($R/4$) |
| 3 | 4 mittenti, percorsi **multihop** | pacchetti scartati al 2° hop = lavoro del 1° hop **sprecato**; throughput → 0 |

- $\lambda_{in}$ = dati originali; $\lambda'_{in}$ = originali + ritrasmissioni (**carico offerto**).
- Approcci: **end-to-end** (TCP) oppure **assistito dalla rete** (bit di congestione, chokepacket, ATM ABR, ECN).

## Collegamenti

- **Concetti correlati**: [[Intensità di Traffico]] · [[Controllo di Congestione TCP]] · [[ECN]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#3.6 Principi del controllo di congestione|Capitolo 3 — 3.6 Principi del controllo di congestione]]
> - [[03 - TLC - Livello di trasporto#Cause e costi della congestione|Capitolo 3 — Cause e costi della congestione]]
> - [[03 - TLC - Livello di trasporto#Approcci al controllo di congestione|Capitolo 3 — Approcci al controllo di congestione]]
