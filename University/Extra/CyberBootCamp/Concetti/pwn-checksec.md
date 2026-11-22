---
title: pwn-checksec
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF.checksec
---

# checksec

> [!abstract] In breve
> Riassume le protezioni rilevate durante l'analisi statica di un file ELF.

## Sintassi

`binario.checksec(banner=True, color=True)`

## Esempio

```python
from pwn import ELF

binario = ELF("/bin/ls", checksec=False)
rapporto = binario.checksec(banner=False, color=False)
print(rapporto)
binario.close()
```

Il riepilogo include proprietà come [[NX]], [[PIE]] e [[Canary dello Stack|stack canary]]. `banner=False` omette il percorso dal riepilogo. La verifica riguarda il file indicato.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-ELF|ELF]]
- [Documentazione ufficiale di checksec](https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF.checksec)
