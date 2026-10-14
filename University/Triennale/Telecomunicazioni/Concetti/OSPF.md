---
title: OSPF
tags:
  - telecomunicazioni
  - concetto
  - routing
  - ospf
  - intra-as
---

# OSPF

> [!summary] In breve
> **Open Shortest Path First** (RFC 2328) è il protocollo **link-state** intra-AS: flooding dello stato dei collegamenti, Dijkstra locale per l'albero dei percorsi minimi, pesi scelti dall'amministratore. Viaggia su IP con protocollo **89**.

- Broadcast a **tutti** i router dell'AS a ogni cambiamento e comunque ogni **30 minuti**.
- Messaggi **HELLO** per verificare i vicini; trasferimento affidabile implementato da OSPF stesso.
- Pesi: tutti a 1 (minimo numero di hop) oppure $\propto 1/\text{capacità}$; invertire il problema (scegliere i pesi per ottenere un certo instradamento) è **ingegneria del traffico**.

Vantaggi:
- **sicurezza**: autenticazione semplice o **MD5** con numeri di sequenza;
- **percorsi a costo uguale** usati insieme;
- **multicast** con MOSPF;
- **gerarchia in aree**: router di confine d'area + **area di dorsale**.

## Collegamenti

- **Concetti correlati**: [[Instradamento Link-State]] · [[Sistema Autonomo]] · [[Protocollo BGP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#OSPF (Open Shortest Path First)|Capitolo 5 — OSPF (Open Shortest Path First)]]
