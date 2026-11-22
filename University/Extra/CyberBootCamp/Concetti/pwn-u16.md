---
title: pwn-u16
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u16
---

# u16

> [!abstract] In breve
> Decodifica un campo di 2 byte in un intero a 16 bit.

## Sintassi

`u16(dati, endian="little", signed=False)`

## Esempio

```python
from pwn import u16

campo = bytes.fromhex("02 01")
assert u16(campo, endian="little", signed=False) == 258
```

Con `endian='little'` il byte meno significativo viene per primo. La chiamata richiede esattamente 2 byte. Usa `signed=True` se il formato prevede un intero con segno.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-p16|p16]] · [[pwn-unpack|unpack]]
- [Documentazione ufficiale di u16](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u16)
