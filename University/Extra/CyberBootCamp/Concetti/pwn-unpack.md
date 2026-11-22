---
title: pwn-unpack
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.unpack
---

# unpack

> [!abstract] In breve
> Decodifica un campo binario in un intero secondo larghezza, ordine e segno.

## Sintassi

`unpack(dati, word_size, endian="big", signed=False)`

## Esempio

```python
from pwn import unpack

campo = bytes.fromhex("00 01 02")
assert unpack(campo, 24, endian="big", signed=False) == 258
```

Per una larghezza fissa i byte del campo devono corrispondere alla dimensione dichiarata. Qui `24` richiede tre byte.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-pack|pack]] · [[pwn-u32|u32]]
- [Documentazione ufficiale di unpack](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.unpack)
