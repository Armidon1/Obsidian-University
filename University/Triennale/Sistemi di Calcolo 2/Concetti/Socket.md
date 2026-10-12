---
title: Socket
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
  - socket
---

# Socket

> [!summary] In breve
> Endpoint di comunicazione (IP + porta) visto dal programma come un descrittore. TCP: socket/bind/listen/accept nel server, socket/connect nel client, poi send/recv e close. UDP: sendto/recvfrom.

```c
int s = socket(AF_INET, SOCK_STREAM, 0);       // SOCK_DGRAM per UDP
struct sockaddr_in a = {0};
a.sin_family = AF_INET; a.sin_port = htons(5001); a.sin_addr.s_addr = INADDR_ANY;
bind(s, (struct sockaddr*)&a, sizeof(a));
listen(s, 5);
int c = accept(s, NULL, NULL);                 // nuovo descrittore per il client
recv(c, buf, n, 0); send(c, buf, n, 0); close(c);
```

- Tipi: stream (TCP), datagram (UDP), raw.
- Porte: 0–1023 riservate (root), 1024–5000 effimere, 5001–65535 per i nostri server.
- **Server concorrente**: `accept` + `fork` (il figlio chiude il socket di ascolto, il padre quello di connessione) o un thread per client.
- `recv` restituisce 0 quando l'altro lato chiude; con TCP può restituire meno byte di quelli inviati.

## Collegamenti

- **Concetti correlati**: [[TCP e UDP]] · [[File Descriptor]] · [[fork]] · [[Modello Client-Server]] · [[Network Adapter e Driver]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[07 - SDC2 - Socket#Socket|Lezione 7 — Socket]]
> - [[07 - SDC2 - Socket#Primitive dei Berkeley socket|Lezione 7 — Primitive dei Berkeley socket]]
> - [[07 - SDC2 - Socket#Client/server TCP|Lezione 7 — Client/server TCP]]
> - [[07 - SDC2 - Socket#Client/server UDP|Lezione 7 — Client/server UDP]]
