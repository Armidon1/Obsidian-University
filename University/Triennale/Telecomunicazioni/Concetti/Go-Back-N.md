---
title: Go-Back-N
tags:
  - telecomunicazioni
  - concetto
  - trasferimento-affidabile
  - finestra-scorrevole
---

# Go-Back-N

> [!summary] In breve
> Protocollo a finestra scorrevole: al massimo $N$ pacchetti non confermati, **ACK cumulativi**, **un solo timer**. Al timeout si ritrasmettono **tutti** i pacchetti da `base` in poi; il ricevente scarta quelli fuori ordine.

| Intervallo | Stato |
| --- | --- |
| $[0, base-1]$ | confermati |
| $[base, nextseqnum-1]$ | inviati, non confermati |
| $[nextseqnum, base+N-1]$ | utilizzabili |
| $\ge base+N$ | non utilizzabili |

- Mittente: tre eventi (dati dall'alto, ACK, timeout).
- Ricevente: tiene solo `expectedseqnum`; fuori ordine → **scarta** e rimanda l'ultimo ACK.
- Numeri di sequenza **modulo $2^k$**.
- Pro: ricevente semplice. Contro: un errore provoca molte ritrasmissioni.

## Collegamenti

- **Concetti correlati**: [[Ripetizione Selettiva]] · [[Protocolli con Pipeline]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Go-Back-N (GBN)|Capitolo 3 — Go-Back-N (GBN)]]
