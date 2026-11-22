---
title: pwn-symbols
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF.symbols
---

# symbols

> [!abstract] In breve
> Attributo di un oggetto `ELF` che associa ogni nome disponibile al suo indirizzo. `binario.sym` è un alias di `binario.symbols`.

## Sintassi

- `binario.symbols` è un `dotdict`, un dizionario con nomi di tipo `str` e indirizzi di tipo `int`.
- `binario.symbols[nome]` restituisce un `int` e solleva `KeyError` se il nome è assente.
- `binario.symbols.get(nome)` restituisce un `int` se il simbolo esiste e `None` altrimenti.

## Esempio

```python
from pwn import ELF

binario = ELF("/bin/ls", checksec=False)
try:
    for nome in sorted(binario.symbols)[:5]:
        indirizzo = binario.symbols[nome]
        print(f"{nome} = {indirizzo:#x}")
finally:
    binario.close()
```

L'esempio stampa fino a cinque simboli disponibili e i relativi indirizzi in esadecimale. I nomi dipendono dal file ELF. Un binario *stripped* può conservare simboli dinamici anche se la tabella ordinaria dei simboli è stata rimossa.

## Codificare l’indirizzo in byte

Usa direttamente l’`int` per confronti e calcoli. Se devi scriverlo in un campo binario a 64 bit, `p64(binario.symbols[nome], endian=binario.endian, signed=False)` produce un oggetto `bytes` lungo 8 byte. Per un campo a 32 bit usa `p32`, che produce 4 byte. Scegli larghezza e ordine dei byte in base al formato di destinazione. L’esempio usa `binario.endian` per rispettare l’ordine dei byte dell’ELF.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-ELF|ELF]]
- [[pwn-p32|p32]] · [[pwn-p64|p64]]
- [Documentazione ufficiale di symbols](https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF.symbols)
