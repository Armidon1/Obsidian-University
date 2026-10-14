---
title: Commutazione di Pacchetto
tags:
  - telecomunicazioni
  - concetto
  - nucleo
  - commutazione
---

# Commutazione di Pacchetto

> [!summary] In breve
> I messaggi sono divisi in **pacchetti** che attraversano i commutatori **senza risorse riservate**. Ogni commutatore fa **store-and-forward**: riceve tutto il pacchetto, lo mette in coda e lo inoltra in base alla **tabella di inoltro**.

- Trasmissione di un pacchetto: $L/R$ secondi.
- **Store-and-forward**, 1 pacchetto su $N$ collegamenti: $d_{\text{end-to-end}} = N \dfrac{L}{R}$.
- $P$ pacchetti su $N$ collegamenti: $(N + P - 1)\dfrac{L}{R}$.
- **Buffer di output** → ritardo di **accodamento** (variabile) e **perdita** se il buffer è pieno.
- **Tabella di inoltro**: indirizzo IP di destinazione → collegamento d'uscita. È compilata dai **protocolli di instradamento**.
- Pro: migliore condivisione della banda, più utenti (35 contro 10 nell'esempio del libro), più semplice. Contro: ritardi non garantiti (*best effort*).

## Collegamenti

- **Concetti correlati**: [[Commutazione di Circuito]] · [[Ritardi nelle Reti a Commutazione di Pacchetto]] · [[Intensità di Traffico]] · [[Protocollo IP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Commutazione di pacchetto|Capitolo 1 — Commutazione di pacchetto]]
> - [[01 - TLC - Reti di calcolatori e Internet#Trasmissione store-and-forward|Capitolo 1 — Trasmissione store-and-forward]]
> - [[01 - TLC - Reti di calcolatori e Internet#Ritardi di accodamento e perdita di pacchetti|Capitolo 1 — Ritardi di accodamento e perdita di pacchetti]]
> - [[01 - TLC - Reti di calcolatori e Internet#Tabelle di inoltro e protocolli di instradamento|Capitolo 1 — Tabelle di inoltro e protocolli di instradamento]]
> - [[01 - TLC - Reti di calcolatori e Internet#Confronto tra commutazione di pacchetto e di circuito|Capitolo 1 — Confronto tra commutazione di pacchetto e di circuito]]
