---
title: Numeri di Sequenza e ACK TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
---

# Numeri di Sequenza e ACK TCP

> [!summary] In breve
> TCP numera i **byte**: il numero di sequenza di un segmento è il numero del suo primo byte. Il numero di ACK è il **prossimo byte atteso**, e gli ACK sono **cumulativi**.

- File da 500.000 byte, MSS 1000 → seq 0, 1000, 2000, …
- Ricevuti 0–535 e 900–1000 → ACK = **536**.
- Numero di sequenza iniziale **casuale** (contro i vecchi segmenti e alcuni attacchi).
- Segmenti fuori ordine: l'RFC non dice cosa fare; di solito si tengono nel buffer.
- **Piggybacking**: l'ACK viaggia su un segmento che porta dati.

Telnet, "C" con ISN 42 e 79:
```text
A→B  Seq=42, ACK=79, data='C'
B→A  Seq=79, ACK=43, data='C'   (eco + ACK in piggyback)
A→B  Seq=43, ACK=80
```

## Collegamenti

- **Concetti correlati**: [[Segmento TCP]] · [[Ritrasmissione Rapida]] · [[Go-Back-N]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Numeri di sequenza e numeri di acknowledgment|Capitolo 3 — Numeri di sequenza e numeri di acknowledgment]]
> - [[03 - TLC - Livello di trasporto#Telnet: un caso di studio|Capitolo 3 — Telnet: un caso di studio]]
