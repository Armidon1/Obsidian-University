---
title: Pila di Protocolli Internet
tags:
  - telecomunicazioni
  - concetto
  - protocolli
  - livelli
---

# Pila di Protocolli Internet

> [!summary] In breve
> Internet organizza i protocolli in **5 livelli**: applicazione, trasporto, rete, collegamento, fisico. Ogni livello offre un **servizio** a quello superiore usando quello inferiore. OSI ne ha 7, con presentazione e sessione.

| Livello | Protocolli | Unità |
| --- | --- | --- |
| Applicazione | HTTP, SMTP, FTP, DNS | messaggio |
| Trasporto | TCP, UDP | segmento |
| Rete | IP + protocolli di instradamento | datagramma |
| Collegamento | Ethernet, Wi-Fi, DOCSIS, PPP | frame |
| Fisico | dipende dal mezzo | bit |

- **Vantaggi**: modularità, si può cambiare l'implementazione di un livello senza toccare gli altri. **Svantaggi**: funzioni duplicate, informazioni che servono a livelli diversi.
- Host: 5 livelli · router: 1–3 · switch: 1–2.
- **OSI**: + presentazione (significato, compressione, cifratura) e sessione (sincronizzazione, recupero). In Internet questi servizi, se servono, li implementa l'applicazione.

## Collegamenti

- **Concetti correlati**: [[Incapsulamento]] · [[Protocollo di Rete]] · [[Modello OSI e TCP-IP]] · [[Architettura a Livelli dei Protocolli]] · [[TCP e UDP]] · [[Protocollo IP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Architettura a livelli|Capitolo 1 — Architettura a livelli]]
> - [[01 - TLC - Reti di calcolatori e Internet#Stratificazione dei protocolli|Capitolo 1 — Stratificazione dei protocolli]]
> - [[01 - TLC - Reti di calcolatori e Internet#I cinque livelli di Internet|Capitolo 1 — I cinque livelli di Internet]]
> - [[01 - TLC - Reti di calcolatori e Internet#Il modello OSI|Capitolo 1 — Il modello OSI]]
