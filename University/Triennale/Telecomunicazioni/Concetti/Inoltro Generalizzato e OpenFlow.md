---
title: Inoltro Generalizzato e OpenFlow
tags:
  - telecomunicazioni
  - concetto
  - sdn
  - openflow
  - piano-dati
---

# Inoltro Generalizzato e OpenFlow

> [!summary] In breve
> Generalizza l'inoltro con il paradigma **match-action**: si confrontano campi di livello 2, 3 e 4 e si eseguono azioni (inoltro, scarto, riscrittura). In OpenFlow ogni riga della **tabella dei flussi** ha match, contatori e azioni, ed è installata da un controller remoto.

- **Match** (OpenFlow 1.0): porta di ingresso + MAC src/dst, Eth Type, VLAN ID/Pri, IP src/dst, IP Proto, IP TOS, porte TCP/UDP src/dst. Wildcard (`10.3.*.*`) e priorità. Niente TTL. Viola la stratificazione.
- **Action**: forward (porta, broadcast, multicast, controller), **drop** (nessuna azione), **modify-field**.
- Sostituisce i **middlebox**: router, switch, NAT, firewall, load balancer.

Esempi (s1–s3, h1–h6):
```text
s3: IP Src=10.3.*.*; IP Dst=10.2.*.*            → Forward(3)    inoltro
s2: Ingress port=3; IP Dst=10.1.*.*             → Forward(2)    load balancing
s2: Ingress port=4; IP Dst=10.1.*.*             → Forward(1)
s2: IP Src=10.3.*.*; IP Dst=10.2.0.3            → Forward(3)    firewall
```

## Collegamenti

- **Concetti correlati**: [[Inoltro e Instradamento]] · [[Longest Prefix Match]] · [[NAT]] · [[Load Balancing]] · [[Firewall e Intrusion Detection]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#4.4 Inoltro generalizzato e SDN|Capitolo 4 — 4.4 Inoltro generalizzato e SDN]]
> - [[04 - TLC - Livello di rete - piano dei dati#Match|Capitolo 4 — Match]]
> - [[04 - TLC - Livello di rete - piano dei dati#Action|Capitolo 4 — Action]]
> - [[04 - TLC - Livello di rete - piano dei dati#Esempi del paradigma match-action in OpenFlow|Capitolo 4 — Esempi del paradigma match-action in OpenFlow]]
