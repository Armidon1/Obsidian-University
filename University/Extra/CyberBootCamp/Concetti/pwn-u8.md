---
title: pwn-u8
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u8
---

# u8

> [!abstract] In breve
> Decodifica un singolo byte in un intero a 8 bit.

## Sintassi

`u8(dati, signed=False)`

## Esempio

```python
from pwn import u8

campo = bytes.fromhex("2a")
assert u8(campo, signed=False) == 42
```

Con un solo byte l'ordine dei byte è ininfluente. La chiamata richiede esattamente un byte. Usa `signed=True` se il formato prevede un intero con segno.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-p8|p8]] · [[pwn-unpack|unpack]]
- [Documentazione ufficiale di u8](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.u8)
