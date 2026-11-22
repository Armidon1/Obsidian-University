---
title: pwn-p64
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p64
---

# p64

> [!abstract] In breve
> Codifica un intero a 64 bit in un campo di 8 byte.

## Sintassi

`p64(valore, endian="little", signed=False)`

## Esempio

```python
from pwn import p64

campo = p64(1000, endian="little", signed=False)
assert campo.hex(" ") == "e8 03 00 00 00 00 00 00"
```

Con `endian='little'` il byte meno significativo viene per primo. La larghezza resta di 8 byte anche per valori piccoli.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-u64|u64]] · [[pwn-pack|pack]]
- [Documentazione ufficiale di p64](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p64)
