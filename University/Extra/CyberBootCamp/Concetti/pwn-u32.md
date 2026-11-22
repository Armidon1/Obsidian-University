---
title: pwn-u32
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u32
---

# u32

> [!abstract] In breve
> Decodifica un campo di 4 byte in un intero a 32 bit.

## Sintassi

`u32(dati, endian="big", signed=False)`

## Esempio

```python
from pwn import u32

campo = bytes.fromhex("00 00 00 0c")
assert u32(campo, endian="big", signed=False) == 12
```

Con `endian='big'` il byte più significativo viene per primo. La chiamata richiede esattamente 4 byte. Usa `signed=True` se il formato prevede un intero con segno.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-p32|p32]] · [[pwn-unpack|unpack]]
- [Documentazione ufficiale di u32](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u32)
