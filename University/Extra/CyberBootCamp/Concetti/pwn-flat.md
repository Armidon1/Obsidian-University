---
title: pwn-flat
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.flat
---

# flat

> [!abstract] In breve
> Concatena campi binari, convertendo gli interi in byte secondo il formato scelto.

## Sintassi

`flat(*campi, word_size=32, endianness='big')`

## Esempio

```python
from pwn import flat

record = flat(b"ID", 12, word_size=32, endianness="big")
assert record == b"ID\x00\x00\x00\x0c"
```

Il testo `b'ID'` occupa due byte. L'intero ne occupa quattro per effetto di `word_size=32`. Specifica larghezza e ordine dei byte quando il formato del record li fissa.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-pack|pack]] · [[pwn-hexdump|hexdump]]
- [Documentazione ufficiale di flat](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.flat)
