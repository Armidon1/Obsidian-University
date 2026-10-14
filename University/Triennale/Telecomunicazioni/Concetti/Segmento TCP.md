---
title: Segmento TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
---

# Segmento TCP

> [!summary] In breve
> Il segmento TCP ha un'intestazione di solito di **20 byte** (porte, seq, ACK, lunghezza, flag, finestra di ricezione, checksum, puntatore urgente, opzioni) più al massimo **MSS** byte di dati.

| Campo | Bit | Uso |
| --- | --- | --- |
| Porte orig / dest | 16 + 16 | multiplexing |
| Numero di sequenza | 32 | affidabilità (numera i byte) |
| Numero di ACK | 32 | affidabilità |
| Lunghezza intestazione | 4 | in parole da 32 bit |
| Flag | ACK, RST, SYN, FIN, PSH, URG (+ CWR, ECE) | controllo |
| Finestra di ricezione | 16 | **controllo di flusso** (`rwnd`) |
| Checksum | 16 | errori |
| Opzioni | var. | MSS, scala della finestra, timestamp |

- **MSS** = dati applicativi massimi per segmento, ricavato dalla **MTU** (Ethernet 1500 → MSS 1460).
- Connessione **full-duplex, punto a punto** (niente multicast), con lo stato **solo negli host**: i router non sanno nulla delle connessioni.

## Collegamenti

- **Concetti correlati**: [[Numeri di Sequenza e ACK TCP]] · [[Controllo di Flusso TCP]] · [[Gestione della Connessione TCP]] · [[Checksum Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Connessione TCP|Capitolo 3 — Connessione TCP]]
> - [[03 - TLC - Livello di trasporto#Struttura dei segmenti TCP|Capitolo 3 — Struttura dei segmenti TCP]]
