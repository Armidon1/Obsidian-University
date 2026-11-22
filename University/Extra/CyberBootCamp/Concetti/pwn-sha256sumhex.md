---
title: pwn-sha256sumhex
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/hashes.html#pwnlib.util.hashes.sha256sumhex
---

# sha256sumhex

> [!abstract] In breve
> Calcola il digest SHA-256 e lo rappresenta in esadecimale.

## Sintassi e ritorno

- `sha256sumhex(dati)`
- **Ritorno** · `str` di 64 caratteri

Il valore rappresenta gli stessi 32 byte di `sha256sum()`, con due caratteri esadecimali per byte.

## Esempio

```python
from pwn import sha256sumhex

import hashlib

assert sha256sumhex(b"bootcamp") == hashlib.sha256(b"bootcamp").hexdigest()
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sha256sum|sha256sum]]
- [Documentazione ufficiale di sha256sumhex](https://docs.pwntools.com/en/stable/util/hashes.html#pwnlib.util.hashes.sha256sumhex)
