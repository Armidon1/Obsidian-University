---
title: Sistema Autonomo
tags:
  - telecomunicazioni
  - concetto
  - routing
  - as
---

# Sistema Autonomo

> [!summary] In breve
> Un **AS** è un gruppo di router sotto lo stesso controllo amministrativo, identificato da un **ASN** assegnato da ICANN. Al suo interno usa un protocollo **intra-AS** (OSPF); tra AS diversi si usa **BGP**.

Risolve **due problemi** dell'instradamento "piatto":
- **scalabilità**: centinaia di milioni di host, tabelle e broadcast ingestibili, e un DV che non converge;
- **autonomia amministrativa**: ogni ISP vuole scegliere il proprio algoritmo e nascondere la propria struttura.

| | Intra-AS | Inter-AS |
| --- | --- | --- |
| Protocollo | OSPF, IS-IS, RIP | BGP |
| Priorità | prestazioni | **politiche** |
| Scalabilità | aree OSPF | critica |

- Un ISP può essere un solo AS (i tier-1, giganteschi) o dividersi in più AS.

## Collegamenti

- **Concetti correlati**: [[OSPF]] · [[Protocollo BGP]] · [[BGP]] · [[Gerarchia degli ISP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.3 Instradamento interno ai sistemi autonomi: OSPF|Capitolo 5 — 5.3 Instradamento interno ai sistemi autonomi: OSPF]]
> - [[05 - TLC - Livello di rete - piano di controllo#Politiche di instradamento|Capitolo 5 — Politiche di instradamento]]
