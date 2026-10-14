---
title: Indirizzo MAC
tags:
  - telecomunicazioni
  - concetto
  - mac
  - indirizzamento
---

# Indirizzo MAC

> [!summary] In breve
> L'indirizzo di livello 2 di una **scheda di rete**: 48 bit in esadecimale (es. `1A-23-F9-CD-06-9B`), **piatto** e permanente, unico al mondo grazie ai blocchi assegnati dall'IEEE. Il broadcast è `FF-FF-FF-FF-FF-FF`.

| | MAC | IP |
| --- | --- | --- |
| Lunghezza | 48 bit | 32 bit |
| Struttura | piatta | gerarchica |
| Spostandosi | invariato | cambia |
| Analogia | codice fiscale | indirizzo postale |

- L'IEEE vende blocchi di $2^{24}$ (primi 24 bit fissi).
- Le schede scartano i frame non indirizzati a loro, senza interrompere la CPU.
- Gli switch **non** hanno MAC sulle interfacce verso host e router: sono trasparenti.
- Due tipi di indirizzi per l'**indipendenza dei livelli**.

## Collegamenti

- **Concetti correlati**: [[Protocollo ARP]] · [[Frame Ethernet]] · [[Indirizzamento IPv4]] · [[Switch a Livello di Collegamento]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Indirizzi MAC|Capitolo 6 — Indirizzi MAC]]
