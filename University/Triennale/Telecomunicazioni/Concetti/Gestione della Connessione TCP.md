---
title: Gestione della Connessione TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - connessione
---

# Gestione della Connessione TCP

> [!summary] In breve
> Apertura con il **three-way handshake** (SYN → SYNACK → ACK), chiusura con FIN/ACK in entrambe le direzioni e attesa in TIME_WAIT. Una porta senza socket risponde con RST. Il SYN flood sfrutta le connessioni mezze aperte; la difesa sono i SYN cookie.

```text
C → S  SYN=1, seq=client_isn
S → C  SYN=1, seq=server_isn, ack=client_isn+1   (SYNACK)
C → S  SYN=0, seq=client_isn+1, ack=server_isn+1 (può contenere dati)
```

| Client | Server |
| --- | --- |
| CLOSED → SYN_SENT → ESTABLISHED | CLOSED → LISTEN → SYN_RCVD → ESTABLISHED |
| → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT (30 s – 2 min) → CLOSED | → CLOSE_WAIT → LAST_ACK → CLOSED |

- **nmap** con un SYN: SYNACK = porta aperta; RST = chiusa, ma nessun firewall; nessuna risposta = probabilmente un firewall.
- **SYN cookie**: numero di sequenza iniziale = hash(IP, porte, segreto); nessuno stato salvato fino all'ACK, valido se ACK = cookie + 1.

## Collegamenti

- **Concetti correlati**: [[Segmento TCP]] · [[Attacchi alle Reti]] · [[SYN Flood DOS]] · [[Nmap scan types]] · [[Multiplexing e Demultiplexing]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Gestione della connessione TCP|Capitolo 3 — Gestione della connessione TCP]]
> - [[03 - TLC - Livello di trasporto#Apertura: three-way handshake|Capitolo 3 — Apertura: three-way handshake]]
> - [[03 - TLC - Livello di trasporto#Chiusura|Capitolo 3 — Chiusura]]
> - [[03 - TLC - Livello di trasporto#Stati TCP|Capitolo 3 — Stati TCP]]
> - [[03 - TLC - Livello di trasporto#Porta senza socket: segmento RST|Capitolo 3 — Porta senza socket: segmento RST]]
