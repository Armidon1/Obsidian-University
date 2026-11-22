---
title: pwn-disasm
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/asm.html#pwnlib.asm.disasm
---

# disasm

> [!abstract] In breve
> Traduce byte di codice macchina in una rappresentazione testuale delle istruzioni.

## Sintassi

`disasm(dati, arch="amd64")`

## Esempio

```python
from pwn import disasm

testo = disasm(b"\x90", arch="amd64")
assert "nop" in testo
print(testo)
```

Indica l'architettura dei byte in ingresso. L'output può mostrare l'offset, i byte e il mnemonico dell'istruzione.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-asm|asm]] · [[pwn-hexdump|hexdump]]
- [Documentazione ufficiale di disasm](https://docs.pwntools.com/en/stable/asm.html#pwnlib.asm.disasm)
