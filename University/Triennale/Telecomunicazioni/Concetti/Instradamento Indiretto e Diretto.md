---
title: Instradamento Indiretto e Diretto
tags:
  - telecomunicazioni
  - concetto
  - mobilita
---

# Instradamento Indiretto e Diretto

> [!summary] In breve
> **Indiretto**: il corrispondente scrive all'indirizzo permanente, e l'agente domestico **incapsula** verso il COA; è trasparente ma soffre dell'**instradamento triangolare**. **Diretto**: un agente corrispondente ottiene il COA e fa tunnel direttamente; serve un protocollo di localizzazione e un **agente di appoggio** per i cambi di rete.

Indiretto: (1) corrispondente → rete di appartenenza; (2) agente domestico → incapsula verso il COA; (3) agente ospitante decapsula → nodo; (4) il nodo risponde direttamente.

Funzioni necessarie: registrazione nodo ↔ agente ospitante, registrazione del COA presso l'agente domestico, incapsulamento, decapsulamento.

Diretto: agente corrispondente ↔ agente domestico (COA), poi tunnel verso il COA. Se il nodo cambia rete, l'**agente di appoggio** re-incapsula verso il nuovo COA (soluzione GSM).

## Collegamenti

- **Concetti correlati**: [[Gestione della Mobilità]] · [[IP Mobile]] · [[Protocollo IPv6]] · [[Incapsulamento]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Instradamento verso il nodo mobile|Capitolo 7 — Instradamento verso il nodo mobile]]
> - [[07 - TLC - Reti mobili e wireless#Instradamento indiretto|Capitolo 7 — Instradamento indiretto]]
> - [[07 - TLC - Reti mobili e wireless#Instradamento diretto|Capitolo 7 — Instradamento diretto]]
