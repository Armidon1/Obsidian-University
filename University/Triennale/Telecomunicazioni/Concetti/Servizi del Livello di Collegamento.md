---
title: Servizi del Livello di Collegamento
tags:
  - telecomunicazioni
  - concetto
  - livello-collegamento
---

# Servizi del Livello di Collegamento

> [!summary] In breve
> Il livello di collegamento sposta un datagramma tra due nodi **adiacenti** incapsulandolo in un **frame**. Può offrire framing, accesso al mezzo (MAC), consegna affidabile e rilevazione/correzione degli errori. È implementato soprattutto nella **scheda di rete**.

| Servizio | Note |
| --- | --- |
| Framing | campo dati + intestazione |
| Accesso al collegamento (MAC) | banale sul punto a punto, cruciale sul broadcast |
| Consegna affidabile | ACK e ritrasmissioni; utile sul wireless, spesso assente su fibra e rame |
| Rilevazione e correzione degli errori | in hardware (CRC) |

- **Nodo** = host, router, switch, AP; **collegamento** = canale tra nodi adiacenti.
- La NIC ha un controller in hardware; il driver sulla CPU gestisce interrupt e indirizzi: software e hardware si incontrano.
- Analogia: il turista (datagramma) viaggia in auto, aereo e treno (protocolli diversi per ogni collegamento).

## Collegamenti

- **Concetti correlati**: [[Network Adapter e Driver]] · [[CRC]] · [[Protocolli di Accesso Multiplo]] · [[Frame Ethernet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#6.1 Livello di collegamento: introduzione|Capitolo 6 — 6.1 Livello di collegamento: introduzione]]
> - [[06 - TLC - Livello di collegamento e reti locali#Servizi offerti dal livello di collegamento|Capitolo 6 — Servizi offerti dal livello di collegamento]]
> - [[06 - TLC - Livello di collegamento e reti locali#Dov'è implementato il livello di collegamento?|Capitolo 6 — Dov'è implementato il livello di collegamento?]]
