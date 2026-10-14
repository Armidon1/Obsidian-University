---
title: IP Mobile
tags:
  - telecomunicazioni
  - concetto
  - mobilita
  - ip
---

# IP Mobile

> [!summary] In breve
> Lo standard Internet per la mobilità (RFC 5944) con instradamento indiretto. Comprende la **ricerca dell'agente** (avviso ICMP tipo 9 / richiesta tipo 10), la **registrazione** presso l'agente domestico (UDP porta 434) e l'instradamento indiretto con incapsulamento.

- Estensione dell'avviso: bit **H** (agente domestico), **F** (ospitante), **R** (registrazione obbligatoria), **M/G** (incapsulamento), lista dei COA.
- Registrazione in 4 fasi: nodo → agente ospitante → agente domestico → risposta → nodo. Campi: COA, HA, MA, tempo di vita, identificativo (64 bit).
- Le registrazioni scadono; non serve cancellare il COA.
- La sicurezza (autenticazione delle registrazioni) è essenziale.

## Collegamenti

- **Concetti correlati**: [[Instradamento Indiretto e Diretto]] · [[Protocollo ICMP]] · [[Gestione della Mobilità]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#7.6 IP mobile|Capitolo 7 — 7.6 IP mobile]]
> - [[07 - TLC - Reti mobili e wireless#Ricerca dell'agente|Capitolo 7 — Ricerca dell'agente]]
> - [[07 - TLC - Reti mobili e wireless#Registrazione presso l'agente domestico|Capitolo 7 — Registrazione presso l'agente domestico]]
