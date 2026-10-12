---
title: Pipelining
tags:
  - sistemi-di-calcolo
  - concetto
  - hardware
  - cpu
  - prestazioni
---

# Pipelining

> [!summary] In breve
> Gli stadi di un'istruzione (Fetch, Decode, Execute, Memory, Write-back) si sovrappongono come in una catena di montaggio: la latenza resta uguale, il throughput cresce fino al numero di stadi. Gli hazard (strutturali, sui dati, sul controllo) lo limitano.

```
senza:  F D E M W
                  F D E M W
con:    F D E M W
          F D E M W
            F D E M W
```

- **Hazard strutturale**: due istruzioni vogliono la stessa risorsa (es. la memoria) → cache separate o stallo.
- **Hazard sui dati**: dipendenza da un risultato non ancora scritto → **stallo** con "bolle", oppure **instruction scheduling** (riordino).
- **Hazard sul controllo**: salti condizionati → branch prediction, istruzioni **branchless** (`CMOV`).
- RISC (ARM, MIPS) vs CISC (x86).

## Collegamenti

- **Concetti correlati**: [[Istruzioni di Salto e Condition Code]] · [[Ottimizzazioni del Compilatore]] · [[Macchina di Von Neumann]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SDC - Esecuzione dei programmi#Esecuzione di una singola istruzione|Lezione 6 — Esecuzione di una singola istruzione]]
> - [[06 - SDC - Esecuzione dei programmi#Pipelining|Lezione 6 — Pipelining]]
> - [[06 - SDC - Esecuzione dei programmi#Hazard|Lezione 6 — Hazard]]
