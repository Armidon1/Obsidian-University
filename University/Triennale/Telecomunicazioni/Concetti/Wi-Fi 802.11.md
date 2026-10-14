---
title: Wi-Fi 802.11
tags:
  - telecomunicazioni
  - concetto
  - wifi
  - wireless
  - lan
---

# Wi-Fi 802.11

> [!summary] In breve
> La famiglia IEEE 802.11 (b, a, g, n, ac: da 11 a 1300 Mbps, a 2,4 e 5 GHz) condivide il MAC **CSMA/CA** e il formato del frame. Il blocco base è il **BSS**: stazioni + **access point**.

| Standard | Banda | Velocità |
| --- | --- | --- |
| 802.11b | 2,4 GHz | 11 Mbps |
| 802.11a | 5 GHz | 54 Mbps |
| 802.11g | 2,4 GHz | 54 Mbps |
| 802.11n | 2,4 + 5 GHz | 450 Mbps |
| 802.11ac | 5 GHz | 1300 Mbps |

- Retrocompatibilità, riduzione del tasso per coprire distanze maggiori, MIMO e beamforming (n, ac).
- Reti **con infrastruttura** (AP collegati a switch o router) o **ad hoc** (BSS senza AP).
- Funzioni avanzate: **adattamento del tasso** (2 frame senza ACK → scende; 10 confermati → sale) e **risparmio energetico** (sleep tra i beacon da 100 ms, risveglio in 250 µs, ~99% di inattività).
- Mobilità tra BSS della stessa sottorete: IP e TCP restano; l'AP nuovo invia un broadcast con il MAC dell'host per aggiornare lo switch.

## Collegamenti

- **Concetti correlati**: [[Associazione 802.11]] · [[CSMA-CA]] · [[Frame 802.11]] · [[Reti Wireless]] · [[Ethernet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#7.3 Wi-Fi: LAN wireless 802.11|Capitolo 7 — 7.3 Wi-Fi: LAN wireless 802.11]]
> - [[07 - TLC - Reti mobili e wireless#Architettura di 802.11|Capitolo 7 — Architettura di 802.11]]
> - [[07 - TLC - Reti mobili e wireless#Mobilità all'interno di una sottorete IP|Capitolo 7 — Mobilità all'interno di una sottorete IP]]
> - [[07 - TLC - Reti mobili e wireless#Funzionalità avanzate di 802.11|Capitolo 7 — Funzionalità avanzate di 802.11]]
