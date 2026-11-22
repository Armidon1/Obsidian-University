---
title: pwn-asm
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/asm.html#pwnlib.asm.asm
---

# asm

> [!abstract] In breve
> Assembla istruzioni testuali e restituisce i byte del codice macchina.

## Sintassi

`asm(istruzioni, arch="amd64")`

## Esempio

```python
from pwn import asm

istruzione = asm("nop", arch="amd64")
assert istruzione == b"\x90"
```

`nop` occupa un byte su x86-64. L'architettura determina la codifica. Per assemblare servono il preprocessore C e gli strumenti GNU per l'architettura scelta.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-disasm|disasm]] · [[pwn-hexdump|hexdump]]
- [Documentazione ufficiale di asm](https://docs.pwntools.com/en/stable/asm.html#pwnlib.asm.asm)
