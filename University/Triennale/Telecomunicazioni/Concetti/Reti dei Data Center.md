---
title: Reti dei Data Center
tags:
  - telecomunicazioni
  - concetto
  - data-center
  - cloud
---

# Reti dei Data Center

> [!summary] In breve
> Le reti dei data center collegano **rack** di blade tramite switch **TOR**, una gerarchia di switch e router di accesso e confine, e **load balancer** (switch di livello 4 con NAT). Il limite della gerarchia è la capacità host-to-host; la risposta sono le topologie **completamente connesse**.

- Costi: host 45%, infrastruttura 25%, energia 15%, rete 15%.
- Gerarchia: confine → accesso → switch di 1° livello (+ load balancer) → 2° livello → TOR → rack; ridondanza; sottoreti divise in VLAN.
- 40 flussi tra rack su un collegamento da 10 Gbps → **250 Mbps** ciascuno (contro 1 Gbps delle schede).
- Completamente connessa: ogni switch di 1° livello è collegato a tutti quelli di 2° → $n$ percorsi disgiunti (40 Gbps nell'esempio).
- Data center modulari in **container**, degradazione graduale; instradamento casuale o multi-NIC; availability zones (Amazon).

## Collegamenti

- **Concetti correlati**: [[Load Balancing]] · [[NAT]] · [[LAN Virtuali]] · [[Content Distribution Network]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.6 Le reti dei data center|Capitolo 6 — 6.6 Le reti dei data center]]
