---
title: pwn-u64
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u64
---

# u64

> [!abstract] In breve
> Decodifica un campo di 8 byte in un intero a 64 bit.

## Sintassi

`u64(dati, endian="little", signed=False)`

## Esempio

```python
from pwn import u64

campo = bytes.fromhex("e8 03 00 00 00 00 00 00")
assert u64(campo, endian="little", signed=False) == 1000
```

Con `endian='little'` il byte meno significativo viene per primo. La chiamata richiede esattamente 8 byte. Usa `signed=True` se il formato prevede un intero con segno.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-p64|p64]] · [[pwn-unpack|unpack]]
- [Documentazione ufficiale di u64](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u64)
