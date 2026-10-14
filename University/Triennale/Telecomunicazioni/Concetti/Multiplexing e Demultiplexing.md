---
title: Multiplexing e Demultiplexing
tags:
  - telecomunicazioni
  - concetto
  - livello-trasporto
  - porte
---

# Multiplexing e Demultiplexing

> [!summary] In breve
> Il **demultiplexing** consegna i dati di un segmento alla **socket** giusta usando i campi dell'intestazione; il **multiplexing** raccoglie i dati dalle socket e crea i segmenti. Così la consegna host-to-host diventa process-to-process.

- Porte da **16 bit** (0–65535); le **porte note** sono 0–1023 (HTTP 80, FTP 21, SMTP 25, DNS 53).
- Il client riceve una porta automatica (1024–65535); il server la fissa con `bind()`.

| | Socket UDP | Socket TCP |
| --- | --- | --- |
| Identificata da | (IP dest, porta dest) | (IP orig, porta orig, IP dest, porta dest) |
| Segmenti con origine diversa e stessa destinazione | **stessa** socket | socket **diverse** |

- La porta di origine è l'"**indirizzo di ritorno**": nella risposta le porte si invertono.
- Due client con la stessa porta di origine verso lo stesso server non creano problemi, perché gli IP sono diversi.
- Port scanning (nmap): scoprire le porte aperte, e quindi le applicazioni attive.

## Collegamenti

- **Concetti correlati**: [[Protocollo UDP]] · [[Socket]] · [[Gestione della Connessione TCP]] · [[Nmap scan types]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#3.2 Multiplexing e demultiplexing|Capitolo 3 — 3.2 Multiplexing e demultiplexing]]
> - [[03 - TLC - Livello di trasporto#Multiplexing e demultiplexing non orientati alla connessione (UDP)|Capitolo 3 — Multiplexing e demultiplexing non orientati alla connessione (UDP)]]
> - [[03 - TLC - Livello di trasporto#Multiplexing e demultiplexing orientati alla connessione (TCP)|Capitolo 3 — Multiplexing e demultiplexing orientati alla connessione (TCP)]]
