---
title: strings e binwalk
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - tools
---

# strings e binwalk

> [!summary] In breve
> Strumenti da riga di comando per il primo sguardo a un binario: `file` riconosce il formato, `strings` estrae il testo leggibile, `binwalk` trova ed estrae file incorporati.

```bash
file elf                       # tipo, arch, static/dynamic, stripped
strings elf | grep -i flag     # sequenze stampabili (>= 4 caratteri)
binwalk --dd='.*' elf          # estrae tutti i file incorporati
```

## binwalk

- Scorre il file byte per byte cercando **firme** (magic number): JPEG `FF D8 FF`, `GIF89a`, zip `PK\x03\x04`, gzip `1F 8B`, … Non serve che il programma usi quei dati.
- Possibili **falsi positivi**: una riga conta solo se l'estrazione dà un file valido.
- Dimensione di un blocco ≈ offset della riga successiva − offset della riga.

```bash
binwalk elf                   # elenca offset e tipo
binwalk -e elf                # estrae in _elf.extracted/
binwalk -Me firmware.bin      # estrazione ricorsiva (matryoshka)
binwalk --dd='jpeg' elf       # estrae solo i JPEG (solo 2.x)
binwalk -E elf                # entropia: ~1 = compresso/cifrato
dd if=elf of=x.jpg bs=1 skip=12423   # estrazione a mano dall'offset
```

| Versione | Note |
|---|---|
| 2.x (Python) | tutte le opzioni sopra, più `-R` (cerca byte), `-A` (opcode), `-W` (diff esadecimale) |
| 3.x (Rust) | `--dd`, `-R`, `-A` rimossi: usare `-e` |

Dopo l'estrazione: `file`, `exiftool`, `zsteg`/`steghide` se la flag è nei metadati o nascosta nell'immagine. Alternative per il *file carving*: `foremost`, `scalpel`.

## Collegamenti

- **Concetti correlati**: [[Sezioni e Segmenti ELF]] · [[Scorciatoie IDA]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#File, strings e binwalk|Lezione 2 — File, strings e binwalk]]
> - [[02 - CB - Reverse Engineering 1#Come lavora binwalk|Lezione 2 — Come lavora binwalk]]
