---
title: NAT
tags:
  - telecomunicazioni
  - concetto
  - ip
  - nat
---

# NAT

> [!summary] In breve
> **Network Address Translation**: il router NAT presenta una rete privata (es. 10.0.0.0/24) verso Internet come **un unico indirizzo IP**, riscrivendo IP e porta di sorgente in uscita (e di destinazione in entrata) tramite una **tabella di traduzione**.

- Reti private (RFC 1918), ad esempio **10.0.0.0/8**: indirizzi validi solo localmente ("reami").
- Esempio: 10.0.0.1:3345 → 128.119.40.186:80 diventa **138.76.29.7:5001**, con la riga `138.76.29.7, 5001 ↔ 10.0.0.1, 3345`; la risposta a :5001 viene riscritta verso 10.0.0.1:3345.
- Porte a 16 bit → oltre **60.000 connessioni** per IP pubblico.
- Critiche: le porte sono per i processi, non per gli host; problemi per server e P2P (**NAT traversal**, **UPnP**); viola il principio **end-to-end**.
- È un tipo di **middlebox**, come firewall e load balancer.

## Collegamenti

- **Concetti correlati**: [[Indirizzamento IPv4]] · [[DHCP]] · [[Multiplexing e Demultiplexing]] · [[Inoltro Generalizzato e OpenFlow]] · [[Firewall e Intrusion Detection]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#NAT (network address translation)|Capitolo 4 — NAT (network address translation)]]
