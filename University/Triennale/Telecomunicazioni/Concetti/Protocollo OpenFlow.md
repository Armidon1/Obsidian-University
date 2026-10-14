---
title: Protocollo OpenFlow
tags:
  - telecomunicazioni
  - concetto
  - sdn
  - openflow
---

# Protocollo OpenFlow

> [!summary] In breve
> Protocollo tra controller SDN e switch, su **TCP porta 6653**. Il controller configura e programma le tabelle dei flussi; lo switch notifica eventi e inoltra al controller i pacchetti senza corrispondenza.

| Controller → switch | Switch → controller |
| --- | --- |
| **Configuration**: parametri | **Flow-Removed**: riga cancellata |
| **Modify-State**: aggiungi, cancella o modifica righe; proprietà delle porte | **Port-status**: cambio di stato di una porta |
| **Read-State**: statistiche e contatori | **Packet-in**: pacchetto mandato al controller |
| **Send-Packet**: invia un pacchetto da una porta | |

- Il libro scrive "Packed-in": il nome corretto è **Packet-in**.

## Collegamenti

- **Concetti correlati**: [[Controller SDN]] · [[Inoltro Generalizzato e OpenFlow]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Il protocollo OpenFlow|Capitolo 5 — Il protocollo OpenFlow]]
