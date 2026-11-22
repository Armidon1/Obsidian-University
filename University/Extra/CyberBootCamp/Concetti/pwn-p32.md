---
title: pwn-p32
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p32
---

# p32

> [!abstract] In breve
> Codifica un intero a 32 bit in un campo di 4 byte.

## Sintassi

`p32(valore, endian="big", signed=False)`

## Esempio

```python
from pwn import p32

campo = p32(12, endian="big", signed=False)
assert campo.hex(" ") == "00 00 00 0c"
```

Con `endian='big'` il byte più significativo viene per primo. La larghezza resta di 4 byte anche per valori piccoli.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-u32|u32]] · [[pwn-pack|pack]]
- [Documentazione ufficiale di p32](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p32)
