---
title: Connessioni Persistenti e Non Persistenti
tags:
  - telecomunicazioni
  - concetto
  - http
  - prestazioni
---

# Connessioni Persistenti e Non Persistenti

> [!summary] In breve
> Con connessioni **non persistenti** ogni oggetto ha una nuova connessione TCP, quindi 2 RTT per oggetto. Con connessioni **persistenti** (default di HTTP/1.1) tutti gli oggetti viaggiano sulla stessa connessione, anche in pipelining.

- **RTT**: tempo di andata e ritorno di un piccolo pacchetto (propagazione + accodamento + elaborazione).
- Non persistente, per ogni oggetto:
  $$T \approx 2\,\text{RTT} + t_{\text{trasmissione}}$$
  1 RTT per il **three-way handshake** TCP e 1 RTT per richiesta e risposta.
- Pagina con HTML + 10 JPEG → **11 connessioni** (i browser ne aprono 5–10 in parallelo).
- Svantaggi delle non persistenti: buffer e variabili TCP per ogni connessione, carico sul server, 2 RTT per oggetto.
- Persistenti: il server lascia aperta la connessione e la chiude dopo un timeout di inattività; **pipelining** = richieste una dopo l'altra senza attendere le risposte.

## Collegamenti

- **Concetti correlati**: [[Protocollo HTTP]] · [[Ritardi nelle Reti a Commutazione di Pacchetto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Connessioni persistenti e non persistenti|Capitolo 2 — Connessioni persistenti e non persistenti]]
> - [[02 - TLC - Livello di applicazione#HTTP con connessioni non persistenti|Capitolo 2 — HTTP con connessioni non persistenti]]
> - [[02 - TLC - Livello di applicazione#HTTP con connessioni persistenti|Capitolo 2 — HTTP con connessioni persistenti]]
