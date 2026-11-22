---
title: pwn-hexdump
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.hexdump
---

# hexdump

> [!abstract] In breve
> Formatta i byte in una tabella con offset, valori esadecimali e caratteri leggibili.

## Sintassi

`hexdump(dati, width=16)`

## Esempio

```python
from pwn import hexdump

testo = hexdump(b"AB\x00\xff", width=8)
assert "41 42 00 ff" in testo
print(testo)
```

Restituisce una `str` da stampare o salvare. Gli offset aiutano a localizzare un byte in un messaggio.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-flat|flat]] · [[pwn-recv|recv]]
- [Documentazione ufficiale di hexdump](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.hexdump)
