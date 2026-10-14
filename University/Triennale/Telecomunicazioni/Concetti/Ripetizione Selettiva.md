---
title: Ripetizione Selettiva
tags:
  - telecomunicazioni
  - concetto
  - trasferimento-affidabile
  - finestra-scorrevole
---

# Ripetizione Selettiva

> [!summary] In breve
> Selective repeat: il ricevente conferma **ogni pacchetto** e tiene nel buffer quelli fuori ordine; il mittente ha un timer per pacchetto e ritrasmette **solo** quelli sospetti. La finestra deve essere ≤ metà dello spazio dei numeri di sequenza.

- Mittente: `send_base`, timer **logico per pacchetto**, la finestra avanza al primo pacchetto non confermato.
- Ricevente (`rcv_base`):
  1. pacchetto in $[rcv\_base, rcv\_base+N-1]$ → ACK, buffer, consegna in blocco se è `rcv_base`;
  2. pacchetto in $[rcv\_base-N, rcv\_base-1]$ → **ACK comunque**, altrimenti il mittente si bloccherebbe;
  3. altrimenti si ignora.
- Le finestre di mittente e ricevente **non coincidono**.
- **Dilemma**: con 4 numeri e finestra 3 il ricevente non distingue il vecchio pkt0 dal nuovo, quindi $N \le 2^k/2$.
- Riordinamento in rete: non riutilizzare un numero finché non è "sicuro" (vita massima del pacchetto ~3 min).

## Collegamenti

- **Concetti correlati**: [[Go-Back-N]] · [[Protocolli con Pipeline]] · [[Numeri di Sequenza e ACK TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Ripetizione selettiva (SR)|Capitolo 3 — Ripetizione selettiva (SR)]]
> - [[03 - TLC - Livello di trasporto#Il dilemma della finestra troppo grande|Capitolo 3 — Il dilemma della finestra troppo grande]]
> - [[03 - TLC - Livello di trasporto#Riordinamento dei pacchetti|Capitolo 3 — Riordinamento dei pacchetti]]
