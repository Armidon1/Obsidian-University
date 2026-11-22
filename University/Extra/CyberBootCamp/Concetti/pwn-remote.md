---
title: pwn-remote
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.sock.remote
---

# remote

> [!abstract] In breve
> Apre una connessione di rete e la espone come tube.

## Sintassi

`remote(host, port, timeout=...)`

## Esempio

```python
from pwn import remote

with remote("127.0.0.1", 9000, timeout=2) as io:
    print(io.recvline())
```

L'esempio presuppone un servizio TCP locale in ascolto sulla porta 9000 che invii una riga alla connessione. I metodi di I/O funzionano come con [[pwn-process|process]].

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-process|process]] · [[pwn-recvline|recvline]] · [[pwn-settimeout|settimeout]]
- [Documentazione ufficiale di remote](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.sock.remote)
