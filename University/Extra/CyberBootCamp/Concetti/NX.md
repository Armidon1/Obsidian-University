---
title: NX
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - mitigations
---

# NX

> [!summary] In breve
> Il bit *Non-eXecutable* impedisce alla CPU di prelevare istruzioni da una pagina marcata NX. È uno dei meccanismi con cui il sistema può applicare W^X.

- Principio W^X: una pagina è scrivibile **o** eseguibile, non entrambe.
- Blocca l'iniezione di codice; **non** blocca il dirottamento del flusso.
- Workaround: [[ROP]] (gadget già presenti nel `.text`).

## Collegamenti

- **Concetti correlati**: [[Ret2Stack]] · [[ROP]] · [[Shellcode]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#La mitigazione: NX|Lezione 5 — La mitigazione: NX]]
