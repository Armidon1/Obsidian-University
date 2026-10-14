---
title: SNMP e Gestione di Rete
tags:
  - telecomunicazioni
  - concetto
  - snmp
  - gestione
---

# SNMP e Gestione di Rete

> [!summary] In breve
> La gestione di rete usa un **server di gestione** (nel NOC) che, tramite il protocollo **SNMP**, legge e scrive le **MIB** dei dispositivi gestiti attraverso i loro **agenti**. SNMPv2 funziona a richiesta-risposta o con **trap**, di solito su UDP.

- **MIB**: oggetti gestiti (contatori, descrizioni, stato, informazioni di protocollo), definiti con il linguaggio **SMI**; circa 400 moduli MIB negli RFC.
- Il protocollo **non gestisce** la rete: è uno strumento per l'amministratore.

| PDU | Direzione |
| --- | --- |
| GetRequest / GetNextRequest / GetBulkRequest | manager → agente |
| SetRequest | manager → agente |
| InformRequest | manager → manager |
| Response | agente → manager (o manager → manager) |
| SNMPv2-Trap | agente → manager, asincrono, senza riscontro |

- UDP è "il mezzo di trasporto preferito"; **Request ID** per rilevare le perdite; nessuna ritrasmissione imposta dal protocollo.
- **SNMPv3** = SNMPv2 + sicurezza e amministrazione.

## Collegamenti

- **Concetti correlati**: [[Protocollo UDP]] · [[SNMP]] · [[Controller SDN]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.7 Gestione della rete e SNMP|Capitolo 5 — 5.7 Gestione della rete e SNMP]]
> - [[05 - TLC - Livello di rete - piano di controllo#Infrastruttura di gestione|Capitolo 5 — Infrastruttura di gestione]]
> - [[05 - TLC - Livello di rete - piano di controllo#SNMP (simple network management protocol)|Capitolo 5 — SNMP (simple network management protocol)]]
