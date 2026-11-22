---
title: pwn-sha256sum
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/hashes.html#pwnlib.util.hashes.sha256sum
---

# sha256sum

> [!abstract] In breve
> Calcola il digest SHA-256 di un blocco di dati.

## Sintassi e ritorno

- `sha256sum(dati)`
- **Ritorno** · `bytes` di lunghezza 32

Passa i byte esatti che vuoi confrontare. Per una versione esadecimale leggibile usa `sha256sumhex()`.

## Esempio

```python
from pwn import sha256sum

import hashlib

assert sha256sum(b"bootcamp") == hashlib.sha256(b"bootcamp").digest()
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sha256sumhex|sha256sumhex]]
- [Documentazione ufficiale di sha256sum](https://docs.pwntools.com/en/stable/util/hashes.html#pwnlib.util.hashes.sha256sum)
