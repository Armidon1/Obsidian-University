---
title: pwn-ELF
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF
---

# ELF

> [!abstract] In breve
> Apre un file ELF per leggerne architettura, simboli e proprietà.

## Sintassi

`ELF(percorso, checksec=True)`

## Esempio

```python
from pwn import ELF

binario = ELF("/bin/ls", checksec=False)
print(binario.arch, binario.bits, binario.endian)
binario.close()
```

Il percorso identifica il file su disco. `checksec=False` evita il riepilogo automatico all'apertura. Il file viene analizzato senza eseguirlo.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-checksec|checksec]] · [[pwn-process|process]]
- [Documentazione ufficiale di ELF](https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF)
