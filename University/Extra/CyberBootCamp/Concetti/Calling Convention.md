---
title: Calling Convention
aliases:
  - Convenzione di chiamata
tags:
  - cyberbootcamp
  - sistemi-di-calcolo
  - sistemi-operativi
  - concetto
  - assembly
  - abi
---

# Calling Convention

> [!summary] In breve
> Una *calling convention* (convenzione di chiamata) stabilisce **dove** il chiamante mette i parametri, **dove** il chiamato lascia il valore di ritorno, **chi** toglie i parametri dallo stack e **quali registri** sopravvivono a una `call`. Non fa parte dell'ISA ma dell'**ABI**.
> - **System V AMD64** (Linux x86-64): primi 6 argomenti interi/puntatori in `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`, poi lo stack; `float`/`double` in `xmm0`–`xmm7`; ritorno in `rax` (o `xmm0`).
> - **cdecl / System V i386** (Linux 32 bit): **tutti** i parametri sullo stack, spinti in **ordine inverso**; ritorno in `eax`; il **chiamante** pulisce lo stack.

## Perché serve una convenzione

Una funzione C diventa una sequenza di istruzioni che termina con `ret` e si invoca con `call` (vedi [[call e ret]]). La funzione che chiama è il **chiamante** (*caller*), quella chiamata il **chiamato** (*callee*). Spesso le due sono compilate separatamente, anche da compilatori diversi: una sta nel nostro programma, l'altra nella libc. Perché si capiscano devono rispettare le stesse regole su:

1. dove stanno i **parametri** (registri o stack, e in che ordine);
2. dove sta il **valore di ritorno**;
3. chi **rimuove** i parametri dallo stack dopo la chiamata;
4. quali registri il chiamato può **sporcare** e quali deve **preservare** ([[Registri Caller-saved e Callee-saved]]);
5. l'**allineamento** dello stack al momento della `call`.

Queste regole **non** sono fissate dall'ISA, cioè dal set di istruzioni della CPU. Le fissa l'**ABI** (*Application Binary Interface*), scelta da sistema operativo e compilatori: su Linux e macOS è la **System V ABI**, in versione i386 per IA32 e AMD64 per x86-64. Vedi [[ABI e ISA]].

## Confronto

| | cdecl / System V i386 (32 bit) | System V AMD64 (64 bit) |
|---|---|---|
| Parametri interi/puntatori | tutti sullo **stack**, spinti in ordine inverso | `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`, dal 7° sullo stack |
| Parametri `float`/`double` | sullo stack | `xmm0`–`xmm7` (sequenza separata) |
| Valore di ritorno | `eax` | `rax` (`xmm0` per i floating point) |
| Chi pulisce lo stack | il chiamante (`add esp, 4·n`) | il chiamante, solo per i parametri passati sullo stack |
| Callee-saved | `ebx`, `esi`, `edi`, `ebp`, `esp` | `rbx`, `rbp`, `rsp`, `r12`–`r15` |
| Caller-saved | `eax`, `ecx`, `edx` | tutti gli altri (`rax`, `rcx`, `rdx`, `rdi`, `rsi`, `r8`–`r11`) |
| Stack alla `call` | multiplo di 16 | multiplo di 16 |

## System V AMD64 (64 bit)

I primi sei argomenti interi o puntatori di una parola usano, in ordine, `rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`. Dal settimo in poi gli argomenti di questa classe passano sullo stack. Un risultato intero di una parola torna in `rax`.

I parametri scalari `float` e `double` usano una sequenza **indipendente**, da `xmm0` a `xmm7`. In `double f(int n, double x)`, `n` entra in `edi`, `x` entra in `xmm0` e il risultato torna in `xmm0`.

```asm
mov rdi, <p1>
mov rsi, <p2>
call func        ; rax = valore di ritorno
```

L'esempio delle slide di Binary Exploitation 1: `printf("Ciao %d %d %ld", int1, int2, big_num)` mette il formato in `rdi`, `int1` in `rsi`, `int2` in `rdx` e `big_num` in `rcx`.

![[CB-L04-p27.png]]

> [!note] Funzioni variadiche e `al`
> `printf` è *variadica*: il numero di argomenti non è fissato dal prototipo. Per queste funzioni System V AMD64 chiede al chiamante di mettere in `al` quanti registri `xmm` sta usando. Per questo nel disassemblato si vede spesso `xor eax, eax` (oppure `mov eax, 0`) subito prima di `call printf`: nessun argomento floating point.

Rispetto a IA32 il passaggio nei registri evita accessi alla memoria. Lo si vede nella `swap` di Sistemi di Calcolo (sintassi AT&T, vedi [[Sintassi Intel e AT&T]]): a 64 bit legge i puntatori direttamente da `%rdi` e `%rsi`.

```asm
swap: movl (%rdi), %eax    # a = *x
      movl (%rsi), %ecx    # b = *y
      movl %eax, (%rsi)    # *y = a
      movl %ecx, (%rdi)    # *x = b
      ret
```

A 32 bit la stessa funzione deve leggere i parametri dallo stack (`8(%esp)`, `12(%esp)`), e le servono quattro registri. Il quarto è `%ebx`, che è callee-saved, quindi `swap` lo deve salvare con `pushl` e ripristinare con `popl`.

> [!tip] Lettura del disassemblato
> Scrivere i 32 bit bassi di un registro a 64 bit **azzera** i 32 alti. Per questo un argomento `int` si vede caricato in `edi` invece che in `rdi`, come nell'esempio `double f(int n, double x)` sopra. Vedi [[x86-64]].

## cdecl / System V i386 (32 bit)

A 32 bit **tutti** i parametri passano sullo stack. Nelle note di Sistemi di Calcolo questa convenzione si chiama *System V i386*, nel CyberBootCamp *cdecl*: per gli interi e i puntatori le regole coincidono.

- Il chiamante spinge i parametri in **ordine inverso**: prima l'ultimo, poi il primo. Lo stack cresce verso indirizzi bassi, quindi in memoria i parametri risultano nell'ordine della firma, con il primo all'indirizzo più basso.
- I parametri interi da 1 o 2 byte sono **promossi a 4 byte**: ogni parametro occupa un multiplo di 4 byte.
- Il valore di ritorno scalare (intero o puntatore) torna in **`eax`**.
- Dopo il ritorno è il **chiamante** a togliere i parametri dallo stack.

Chiamata `c = f(10, 20)` in sintassi AT&T, come nella dispensa di Sistemi di Calcolo:

```asm
pushl $20         # secondo parametro
pushl $10         # primo parametro
call f
addl $8, %esp     # il CHIAMANTE toglie i parametri (2 push da 4 byte)
movl %eax, %ecx   # c = risultato

f:  movl 4(%esp), %eax   # x
    addl 8(%esp), %eax   # + y
    ret
```

La stessa chiamata in sintassi Intel, come nelle slide del CyberBootCamp:

```asm
push edi              ; salva edi (se serve conservarlo)
push <param 2>
push <param 1>
call func
...                   ; eax contiene il valore di ritorno
```

Dove si trovano i parametri all'ingresso nel corpo della funzione:

| | Senza frame pointer | Con frame pointer (dopo `push ebp; mov ebp, esp`) |
|---|---|---|
| Indirizzo di ritorno | `(%esp)` | `4(%ebp)` |
| `ebp` del chiamante | n/a | `(%ebp)` |
| 1° parametro | `4(%esp)` | `8(%ebp)` |
| n-esimo parametro | `4n(%esp)` | `4+4n(%ebp)` |

![[SDC-p065-1.png]]

Durante il corpo di `f`, `x = 10` sta in `8(%ebp)`/`4(%esp)` e `y = 20` in `12(%ebp)`/`8(%esp)`. Il prologo e l'epilogo che creano questi offset sono descritti in [[Stack Frame x86-64]] e, per IA32, in [[Stack Frame]].

## Registri preservati

La convenzione divide i registri in due gruppi. Sono riassunti nella tabella di confronto sopra e spiegati in dettaglio in [[Registri Caller-saved e Callee-saved]] (versione CyberBootCamp, x86-64) e in [[Registri Caller-save e Callee-save]] (versione Sistemi di Calcolo, con gli esempi IA32).

- **Caller-saved**: il chiamato può modificarli. Se al chiamante servono dopo la `call`, li salva lui prima della chiamata.
- **Callee-saved**: il chiamato deve restituirli intatti. Se li usa, li salva nel prologo e li ripristina nell'epilogo.

> [!note] Perché `rdi` e `rsi` cambiano gruppo
> In IA32 `esi` e `edi` sono callee-save. In x86-64 `rdi` e `rsi` diventano caller-saved perché portano i primi due parametri: il chiamato li consuma e li sovrascrive.

## Allineamento dello stack

Per convenzione, quando si esegue una `call` lo stack pointer deve essere a un indirizzo **multiplo di 16**. Sistemi di Calcolo la presenta come una regola di prestazioni, e per questo `gcc` genera istruzioni in apparenza inutili per allineare lo stack.

> [!tip] Nel pwn
> A 64 bit la regola ha anche effetti sulla correttezza: alcune funzioni della libc, ad esempio `system`, usano istruzioni SSE come `movaps`, che richiedono dati allineati a 16 byte. Se un exploit salta a una funzione con lo stack disallineato di 8 byte, il programma va in crash dentro la libc. La soluzione tipica è inserire nella catena un gadget `ret` in più, che consuma 8 byte e riallinea lo stack.

## La convenzione delle system call

Anche le [[System Call]] hanno una loro convenzione, distinta da quella delle funzioni. Sistemi Operativi spiega perché i parametri delle syscall passano nei **registri**. L'entrata nel kernel salva tutti i registri del processo (`pushAll()`) e cambia stack (`setSP(kernel_sp)`). Il kernel trova quindi i parametri nei registri salvati, e anche il valore di ritorno torna in un registro.

|                      | Linux x86 (32 bit)                       | Linux x86-64                               |
| -------------------- | ---------------------------------------- | ------------------------------------------ |
| Istruzione           | `int 0x80`                               | `syscall`                                  |
| Numero della syscall | `eax`                                    | `rax`                                      |
| Argomenti            | `ebx`, `ecx`, `edx`, `esi`, `edi`, `ebp` | `rdi`, `rsi`, `rdx`, **`r10`**, `r8`, `r9` |
| Ritorno              | `eax`                                    | `rax` (negativo in caso di errore)         |

> [!warning] `r10` al posto di `rcx`
> Il quarto argomento di una syscall a 64 bit va in `r10`, non in `rcx` come per le funzioni. L'istruzione `syscall` sovrascrive `rcx` (ci salva l'indirizzo di ritorno) e `r11` (ci salva i flag).

È la convenzione usata nella ROP chain di Binary Exploitation 2 per `execve("/bin/sh", 0, 0)`: `rax = 0x3b`, `rdi =` indirizzo di `"/bin/sh"`, `rsi = 0`, `rdx = 0`, poi `syscall`. Vedi [[ROP]] e [[Shellcode]].

## Altre architetture: avr-gcc

Le convenzioni non riguardano solo x86. Nel context switch su AVR di Sistemi Operativi, `archContextSwitch(old_tcb_ptr, new_tcb_ptr)` riceve i parametri secondo la convenzione di **avr-gcc**:

- il primo argomento (16 bit) arriva nella coppia **R25:R24**, il secondo in **R23:R22**;
- i registri callee-saved sono **R2–R17** e **R28–R29**: sono quelli che la funzione salva con `push` prima di cambiare stack.

Vedi [[05 - SO - Stack e Context Switch#Il context switch in assembly|Lezione 5 di SO — Il context switch in assembly]].

## Perché conta nell'exploitation

Nel pwn, conoscere la convenzione serve a **chiamare una funzione con argomenti scelti da noi** dopo aver preso il controllo del return address (vedi [[Sovrascrivere il Return Address]]).

- **32 bit**: i parametri stanno sullo stack, quindi basta scriverli nell'overflow. Al momento dell'ingresso nella funzione, `(%esp)` deve contenere un indirizzo di ritorno e `4(%esp)` il primo parametro. Il payload è quindi: indirizzo della funzione, un indirizzo di ritorno fittizio, poi gli argomenti.

  ```
  [ padding ][ &func ][ ret fittizio ][ arg1 ][ arg2 ]
  ```

- **64 bit**: i parametri stanno nei registri, che con un overflow non si possono scrivere direttamente. Servono **gadget** come `pop rdi ; ret`, che caricano in un registro un valore preso dallo stack. Vedi [[ROP]].

  ```
  [ padding ][ &(pop rdi ; ret) ][ arg1 ][ &func ]
  ```

## Collegamenti

- **Concetti correlati**: [[Registri Caller-saved e Callee-saved]] · [[Registri x86-64]] · [[Stack Frame x86-64]] · [[call e ret]] · [[ROP]]
- **Sistemi di Calcolo**: [[Convenzioni di Chiamata IA32]] · [[x86-64]] · [[ABI e ISA]] · [[Registri Caller-save e Callee-save]] · [[Stack Frame]]
- **Sistemi Operativi**: [[System Call]] · [[Context Switch]]
- **Mappe**: [[MOC - CyberBootCamp]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Parametri e valore di ritorno|CB Lezione 3 — Parametri e valore di ritorno]]
> - [[04 - CB - Binary Exploitation 1#Come la CPU esegue il codice|CB Lezione 4 — Come la CPU esegue il codice]]
> - [[05 - CB - Binary Exploitation 2#ROP per una shell|CB Lezione 5 — ROP per una shell]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Funzioni|SDC Lezione 3 — Funzioni]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Passaggio dei parametri|SDC Lezione 3 — Passaggio dei parametri]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Estensione a x86-64|SDC Lezione 3 — Estensione a x86-64]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#System call|SO Lezione 6 — System call]]
> - [[05 - SO - Stack e Context Switch#Il context switch in assembly|SO Lezione 5 — Il context switch in assembly]]
