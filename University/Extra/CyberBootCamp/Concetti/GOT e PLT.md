---
title: GOT e PLT
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - elf
  - dynamic-linking
---

# GOT e PLT

> [!summary] In breve
> Le funzioni di libreria si chiamano attraverso uno stub nella **PLT** (codice) che salta all'indirizzo scritto nella **GOT** (dati scrivibili), risolto a runtime da `ld.so`.

```
call printf@plt
printf@plt:  jmp *GOT[printf]       ; 1ª volta: GOT punta al resolver
             push <indice>
             jmp  PLT0 → _dl_runtime_resolve → scrive GOT[printf]
```

- **Lazy binding**: risolve alla prima chiamata; con Full RELRO (`-z now`) tutto all'avvio e GOT read-only.
- `nm`: `U printf@GLIBC_2.2.5` = simbolo non definito nel binario.
- In sicurezza: **GOT overwrite** devia la prossima chiamata.

## Collegamenti

- **Concetti correlati**: [[Dynamic Linking]] · [[Sezioni e Segmenti ELF]] · [[Avvio di un Binario ELF]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#Dynamic linking|Lezione 2 — Dynamic linking]]
> - [[02 - CB - Reverse Engineering 1#GOT e PLT|Lezione 2 — GOT e PLT]]
