---
title: TCP su Reti Wireless
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - wireless
---

# TCP su Reti Wireless

> [!summary] In breve
> TCP interpreta ogni perdita come **congestione** e riduce la finestra, ma sul wireless molte perdite sono dovute a **errori sui bit** o a **handoff**. Rimedi: **recupero locale**, TCP **consapevole** del tratto wireless, **suddivisione della connessione**.

| Approccio | Idea |
| --- | --- |
| Recupero locale | ARQ/FEC sul collegamento (es. 802.11) |
| TCP consapevole | distingue le perdite wireless da quelle per congestione |
| Connessione divisa | mobile ↔ AP + AP ↔ host remoto; molto usata nel cellulare |

- Livello di applicazione: banda limitata come "merce preziosa", applicazioni sensibili alla posizione.

## Collegamenti

- **Concetti correlati**: [[Controllo di Congestione TCP]] · [[CSMA-CA]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#7.8 Wireless e mobilità: l'impatto sui protocolli di livello superiore|Capitolo 7 — 7.8 Wireless e mobilità: l'impatto sui protocolli di livello superiore]]
