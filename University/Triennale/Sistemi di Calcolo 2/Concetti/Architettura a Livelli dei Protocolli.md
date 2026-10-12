---
title: Architettura a Livelli dei Protocolli
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
---

# Architettura a Livelli dei Protocolli

> [!summary] In breve
> La comunicazione è divisa in livelli: ogni livello parla logicamente con il pari dall'altra parte secondo un protocollo, e fisicamente passa i dati al livello sotto aggiungendo un header (incapsulamento).

- **Protocollo**: regole tra entità pari (sintassi, semantica, timing). **Interfaccia**: servizi tra livelli adiacenti.
- Esempio: filosofo → traduttore → segretaria.
- Incapsulamento: dati → segmento TCP → datagram IP → frame Ethernet.

## Collegamenti

- **Concetti correlati**: [[Modello OSI e TCP-IP]] · [[Protocollo IP]] · [[TCP e UDP]] · [[Architettura a Strati]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[06 - SDC2 - Reti di Calcolatori#Architettura a livelli e protocolli|Lezione 6 — Architettura a livelli e protocolli]]
> - [[06 - SDC2 - Reti di Calcolatori#Gerarchie di protocolli|Lezione 6 — Gerarchie di protocolli]]
> - [[07 - SDC2 - Socket#Richiami di rete|Lezione 7 — Richiami di rete]]
