---
title: Dual Mode
tags:
  - sistemi-operativi
  - concetto
  - protezione
  - kernel
---

# Dual Mode

> [!summary] In breve
> La CPU ha due modalità, user e privileged (kernel), indicate da un bit nei FLAG. Le istruzioni e le aree pericolose sono riservate alla modalità privilegiata; si entra in kernel mode solo tramite interrupt/trap.

- **Privileged mode**: accesso completo all'hardware; ci girano l'OS e tutte le ISR.
- **User mode**: solo un sottoinsieme di istruzioni; violazioni → **fault**.
- Modificare il mode bit è privilegiato, quindi un programma utente non può alzarsi i privilegi da solo.
- **Unico ingresso controllato**: `INT 0x80`. La CPU cambia modalità e salta a codice scelto dal kernel; `iret` ripristina i flag e quindi la modalità precedente.
- Il kernel usa un **proprio stack**.
- Protegge l'interrupt vector, i dispositivi mappati in memoria, la configurazione della MMU.

## Collegamenti

- **Concetti correlati**: [[System Call]] · [[Interrupt Vector]] · [[Eccezioni]] · [[MMU]] · [[Kernel Monolitico e Microkernel]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Dual mode|Lezione 6 — Dual mode]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Come entra in modalità privilegiata un programma utente?|Lezione 6 — Come entra in modalità privilegiata un programma utente?]]
> - [[06 - SDC - Esecuzione dei programmi#System call con int $0x80|Sistemi di Calcolo, cap. 6 — System call con int $0x80]]
