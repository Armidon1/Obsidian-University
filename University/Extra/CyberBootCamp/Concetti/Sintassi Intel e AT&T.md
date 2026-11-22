---
title: Sintassi Intel e AT&T
tags:
  - cyberbootcamp
  - concetto
  - assembly
---

# Sintassi Intel e AT&T

> [!summary] In breve
> Due modi di scrivere le stesse istruzioni. **Intel**: `add rdi, 8` (`dst, src`). **AT&T**: `add $8, %rdi` (`src, dst`, `%` sui registri, `$` sugli immediati, suffisso di dimensione `b/w/l/q`).

| | Intel | AT&T |
|---|---|---|
| operandi | `add rdi, 8` | `add $8, %rdi` |
| memoria | `[base+idx*scale+off]` | `off(base,idx,scale)` |
| dimensione | nel `TYPE PTR` | suffisso `b/w/l/q` |

- AT&T è il default GNU; `.intel_syntax noprefix` per usare Intel in un sorgente.
- `objdump -d` → AT&T; `objdump -d -M intel` → Intel. GDB su x86 usa AT&T per impostazione predefinita. Per selezionare Intel: `set disassembly-flavor intel`.

## Collegamenti

- **Concetti correlati**: [[Istruzioni x86-64]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Due sintassi: Intel e AT&T|Lezione 3 — Due sintassi: Intel e AT&T]]
