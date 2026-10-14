---
title: Controllo di Parità
tags:
  - telecomunicazioni
  - concetto
  - errori
---

# Controllo di Parità

> [!summary] In breve
> Un bit di **parità** (pari o dispari) rileva un numero dispari di errori. La **parità bidimensionale** (righe + colonne) individua e **corregge** un errore singolo e ne rileva due: è un esempio di **FEC**.

- Parità pari: il numero totale di 1 nei $d + 1$ bit è pari (`0111000110101011` → bit 1).
- Un numero pari di errori **non viene rilevato**; con errori a **burst** la probabilità di non accorgersene arriva al ~50%.
- 2D: $i + j + 1$ bit di parità; l'incrocio tra la riga e la colonna con parità errata indica il bit da correggere (es. posizione (2,2)).
- **FEC** (*forward error correction*): correggere senza ritrasmettere, risparmiando un RTT (tempo reale, spazio profondo, CD audio).

## Collegamenti

- **Concetti correlati**: [[CRC]] · [[Checksum Internet]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.2 Tecniche di rilevazione e correzione degli errori|Capitolo 6 — 6.2 Tecniche di rilevazione e correzione degli errori]]
> - [[06 - TLC - Livello di collegamento e reti locali#Controllo di parità|Capitolo 6 — Controllo di parità]]
