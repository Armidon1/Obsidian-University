---
title: Controllo di Flusso TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - flusso
---

# Controllo di Flusso TCP

> [!summary] In breve
> Il controllo di flusso evita che il mittente saturi il **buffer di ricezione** del destinatario: il destinatario comunica lo spazio libero (`rwnd`) e il mittente tiene i byte non riscontrati sotto quel valore.

$$\texttt{rwnd} = \texttt{RcvBuffer} - (\texttt{LastByteRcvd} - \texttt{LastByteRead})$$

$$\texttt{LastByteSent} - \texttt{LastByteAcked} \le \texttt{rwnd}$$

- `rwnd` viaggia nel campo **finestra di ricezione** di ogni segmento ed è dinamica.
- **Finestra a zero**: il mittente continua a inviare segmenti da **1 byte**, così gli ACK prima o poi riportano un `rwnd` > 0.
- Flusso ≠ **congestione**: il primo protegge il destinatario, il secondo la rete.
- UDP non ha controllo di flusso: se il buffer della socket si riempie, i segmenti si perdono.

## Collegamenti

- **Concetti correlati**: [[Segmento TCP]] · [[Controllo di Congestione TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Controllo di flusso|Capitolo 3 — Controllo di flusso]]
