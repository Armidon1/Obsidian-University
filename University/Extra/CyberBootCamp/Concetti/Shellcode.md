---
title: Shellcode
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - shellcode
---

# Shellcode

> [!summary] In breve
> Sequenza di istruzioni in **codice macchina** iniettata e fatta eseguire dal processo. L'obiettivo classico è `execve("/bin/sh",0,0)` (una shell). pwntools: `shellcraft.amd64.linux.sh()` + `asm()`.

```asm
mov rax, 59          ; execve
mov rdi, "/bin/sh\0"
mov rsi, 0           ; argv
mov rdx, 0           ; envp
syscall
```
- Codice casuale → **SIG_ILL**; servono istruzioni **legali**.
- Iniettato di solito sullo stack ([[Ret2Stack]]); bloccato da [[NX]].
- `context.arch='amd64'; asm(shellcraft.amd64.linux.sh())`.

## Collegamenti

- **Concetti correlati**: [[Ret2Stack]] · [[NX]] · [[pwntools]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#Ret2Stack: eseguire codice proprio|Lezione 5 — Ret2Stack: eseguire codice proprio]]
> - [[05 - CB - Binary Exploitation 2#Quale codice? La reverse shell|Lezione 5 — Quale codice? La reverse shell]]
