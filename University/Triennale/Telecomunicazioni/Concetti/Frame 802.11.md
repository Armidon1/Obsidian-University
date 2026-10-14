---
title: Frame 802.11
tags:
  - telecomunicazioni
  - concetto
  - wifi
---

# Frame 802.11

> [!summary] In breve
> Il frame 802.11 ha controllo (2), durata (2), **quattro indirizzi MAC** (6 ciascuno), numero di sequenza (2), payload (0–2312) e CRC (4). Il terzo indirizzo, quello del **router**, collega il BSS alla rete cablata.

| Direzione | Indirizzo 1 | Indirizzo 2 | Indirizzo 3 |
| --- | --- | --- | --- |
| AP → H1 | H1 | AP | R1 (router) |
| H1 → AP | AP | H1 | R1 |

- Indirizzo 4: solo reti ad hoc.
- L'AP è di livello 2 e converte tra frame Ethernet e 802.11 usando l'indirizzo 3.
- Numero di sequenza: riconosce i duplicati (come rdt2.1). Durata: canale riservato.
- Controllo: tipo/sottotipo (associazione, RTS, CTS, ACK, dati), verso AP / da AP, WEP…

## Collegamenti

- **Concetti correlati**: [[Wi-Fi 802.11]] · [[Frame Ethernet]] · [[Protocollo ARP]] · [[Indirizzo MAC]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Il frame IEEE 802.11|Capitolo 7 — Il frame IEEE 802.11]]
> - [[07 - TLC - Reti mobili e wireless#I tre campi indirizzo|Capitolo 7 — I tre campi indirizzo]]
