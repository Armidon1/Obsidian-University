---
title: pwn-make_unpacker
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.make_unpacker
---

# make_unpacker

> [!abstract] In breve
> Crea una funzione per decodificare campi binari con impostazioni fissate.

## Sintassi e ritorno

- `make_unpacker(word_size, endian=..., signed=...)`
- **Ritorno** · Funzione che converte `bytes` in un `int`

La funzione creata riutilizza le stesse regole per ogni campo, indipendentemente dalle impostazioni successive del contesto.

## Esempio

```python
from pwn import make_unpacker

decodifica = make_unpacker(16, endian="big", signed=False)
assert decodifica(bytes.fromhex("01 02")) == 258
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-unpack|unpack]]
- [Documentazione ufficiale di make_unpacker](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.make_unpacker)
