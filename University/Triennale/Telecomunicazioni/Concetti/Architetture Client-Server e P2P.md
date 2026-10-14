---
title: Architetture Client-Server e P2P
tags:
  - telecomunicazioni
  - concetto
  - livello-applicazione
  - architetture
---

# Architetture Client-Server e P2P

> [!summary] In breve
> Le due architetture delle applicazioni di rete. **Client-server**: un server sempre attivo, con indirizzo fisso, serve molti client che non si parlano tra loro. **P2P**: i peer comunicano direttamente e ogni peer aggiunge capacità al sistema (auto-scalabilità).

| | Client-server | P2P |
| --- | --- | --- |
| Infrastruttura | server sempre attivi, spesso in **data center** | minima o assente |
| Comunicazione | client ↔ server | peer ↔ peer, connessi in modo intermittente |
| Scalabilità | serve aggiungere server | **auto-scalabile** |
| Esempi | Web, FTP, Telnet, e-mail | BitTorrent, Xunlei, Skype |

- Esistono **architetture ibride**, come la messaggistica istantanea: server per trovare gli utenti, messaggi diretti tra peer.
- In una sessione, **client** è chi avvia la comunicazione e **server** è chi attende di essere contattato.

## Collegamenti

- **Concetti correlati**: [[Modello Client-Server]] · [[Distribuzione di File P2P]] · [[BitTorrent]] · [[Socket]] · [[Host e Sistemi Periferici]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Architetture delle applicazioni di rete|Capitolo 2 — Architetture delle applicazioni di rete]]
> - [[02 - TLC - Livello di applicazione#Processi client e server|Capitolo 2 — Processi client e server]]
