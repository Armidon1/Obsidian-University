---
title: Indirizzamento IPv4
tags:
  - telecomunicazioni
  - concetto
  - ip
  - indirizzamento
---

# Indirizzamento IPv4

> [!summary] In breve
> Un indirizzo IPv4 è di **32 bit** in notazione decimale puntata ed è assegnato a un'**interfaccia**, non a un host: un router ne ha uno per ogni interfaccia.

- $2^{32} \approx 4$ miliardi di indirizzi.
- `193.32.216.9` = `11000001 00100000 11011000 00001001`.
- Unicità globale, tranne le reti private dietro **NAT**.
- Una parte dell'indirizzo è il **prefisso di sottorete** ([[Sottorete]], [[CIDR]]).
- **Broadcast**: `255.255.255.255`, consegnato a tutti gli host della sottorete.
- Gli indirizzi si ottengono così: blocco dall'ISP ← registri regionali (RIPE in Europa) ← **ICANN**; host via **DHCP**.

## Collegamenti

- **Concetti correlati**: [[Sottorete]] · [[CIDR]] · [[DHCP]] · [[NAT]] · [[Datagramma IPv4]] · [[Protocollo IP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Indirizzamento IPv4|Capitolo 4 — Indirizzamento IPv4]]
> - [[04 - TLC - Livello di rete - piano dei dati#Come ottenere un blocco di indirizzi|Capitolo 4 — Come ottenere un blocco di indirizzi]]
