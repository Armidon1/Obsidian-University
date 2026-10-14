---
title: Socket UDP e TCP in Python
tags:
  - telecomunicazioni
  - concetto
  - socket
  - programmazione
---

# Socket UDP e TCP in Python

> [!summary] In breve
> Con UDP (`SOCK_DGRAM`) ogni pacchetto porta l'indirizzo di destinazione (`sendto`/`recvfrom`). Con TCP (`SOCK_STREAM`) il client fa `connect()`, il server ha una **socket di benvenuto** (`listen`/`accept`) che crea una **socket di connessione** per ogni client.

```python
# Server TCP minimale
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 12000))
s.listen(1)
while True:
    conn, addr = s.accept()          # socket di connessione
    data = conn.recv(1024).decode()
    conn.send(data.upper().encode())
    conn.close()                     # s resta aperta
```

| | UDP | TCP |
| --- | --- | --- |
| Invio | `sendto(dati, (ip, porta))` | `send(dati)` |
| Ricezione | `recvfrom()` → (dati, indirizzo) | `recv()` |
| Setup | nessuno | `connect()` / `listen()` + `accept()` |
| Socket del server | 1 | benvenuto + una per client |

- Il client non sceglie la propria porta: la assegna il sistema operativo. Il server la fissa con `bind`.
- Applicazioni aperte (porte note, RFC) e proprietarie (da evitare le porte note).

## Collegamenti

- **Concetti correlati**: [[Socket]] · [[Sockets in Python]] · [[Servizi di Trasporto per le Applicazioni]] · [[TCP e UDP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#2.7 Programmazione delle socket: come creare un'applicazione di rete|Capitolo 2 — 2.7 Programmazione delle socket: come creare un'applicazione di rete]]
> - [[02 - TLC - Livello di applicazione#Programmazione delle socket con UDP|Capitolo 2 — Programmazione delle socket con UDP]]
> - [[02 - TLC - Livello di applicazione#Programmazione delle socket con TCP|Capitolo 2 — Programmazione delle socket con TCP]]
