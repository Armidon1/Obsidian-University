---
title: pwn-bits
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.bits
---

# bits

> [!abstract] In breve
> Scompone i byte nei singoli bit.

## Sintassi e ritorno

- `bits(dati, endian="big")`
- **Ritorno** · `list[int]` con le opzioni predefinite

Con `endian='big'` inizi dal bit più significativo di ogni byte. `zero` e `one` possono sostituire i valori predefiniti.

## Esempio

```python
from pwn import bits

assert bits(b"\xA0") == [1, 0, 1, 0, 0, 0, 0, 0]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-unbits|unbits]]
- [Documentazione ufficiale di bits](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.bits)
