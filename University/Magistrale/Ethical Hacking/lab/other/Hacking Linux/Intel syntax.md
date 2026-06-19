# Assembly — Sintassi Intel vs AT&T

> [!abstract] In una frase Due modi di scrivere le stesse istruzioni x86. AT&T è quella di GCC/GAS e dei libri di Sistemi di Calcolo. Intel è quella di GDB/GEF, Ghidra, pwndbg, e della maggior parte degli exploit. **Stesso risultato, ordine degli operandi invertito.**

Collegamento: [[ETHL 0x07 — Binary Exploitation p1]] · [[Stack Canary]]

---

## 1. La differenza principale: ordine degli operandi

| |Ordine|
|---|---|
|**AT&T**|`istruzione SORGENTE, DESTINAZIONE`|
|**Intel**|`istruzione DESTINAZIONE, SORGENTE`|

```asm
; AT&T
movq $42, %rax        ; rax = 42

; Intel
mov rax, 42           ; rax = 42
```

> [!warning] È la prima cosa da controllare quando leggi assembly Se sbagli l'ordine, misinterpreti ogni istruzione. Guarda sempre se ci sono `%` — se sì, sei in AT&T.

---

## 2. Tabella di conversione rapida

|Caratteristica|AT&T|Intel|
|---|---|---|
|**Ordine operandi**|src, dst|dst, src|
|**Registri**|`%rax`, `%rbp`|`rax`, `rbp`|
|**Costanti immediate**|`$42`, `$0x28`|`42`, `0x28`|
|**Dimensione operazione**|suffisso sull'istruzione|prefisso sulla memoria|
|**Accesso a memoria**|`(%rax)`|`[rax]`|
|**Base + offset**|`0x8(%rbp)`|`[rbp + 0x8]`|
|**Segmento**|`%fs:0x28`|`fs:0x28`|

---

## 3. La dimensione dell'operazione

In AT&T la specifichi con un suffisso sull'istruzione:

```asm
movb   $1, %al      ; b = byte (8 bit)
movw   $1, %ax      ; w = word (16 bit)
movl   $1, %eax     ; l = long (32 bit)
movq   $1, %rax     ; q = quad (64 bit)
```

In Intel la specifichi con un prefisso sul **riferimento a memoria** (sui registri è implicita dalla loro dimensione):

```asm
mov al,  BYTE  PTR [rbp-0x1]   ; 8 bit
mov ax,  WORD  PTR [rbp-0x2]   ; 16 bit
mov eax, DWORD PTR [rbp-0x4]   ; 32 bit
mov rax, QWORD PTR [rbp-0x8]   ; 64 bit
```

> [!tip] Quando non c'è un riferimento a memoria, il prefisso non serve `mov rax, rbx` — la dimensione è implicita: entrambi sono registri a 64 bit. Il prefisso `QWORD PTR` serve solo quando la CPU non può dedurre la dimensione dal contesto (es. `mov [rbp-0x8], 42` — quanti byte scrivi? Serve specificarlo).

---

## 4. Accesso alla memoria

In AT&T le parentesi tonde indicano la dereferenziazione, in Intel le parentesi quadre:

```asm
; AT&T
movq (%rax), %rbx         ; rbx = *rax
movq 0x8(%rbp), %rax      ; rax = *(rbp + 0x8)
movq -0x8(%rbp), %rax     ; rax = *(rbp - 0x8)

; Intel
mov rbx, [rax]            ; rbx = *rax
mov rax, [rbp + 0x8]      ; rax = *(rbp + 0x8)
mov rax, QWORD PTR [rbp-0x8]  ; rax = *(rbp - 0x8)
```

La forma completa dell'indirizzamento (base + indice × scala + offset):

```asm
; AT&T
movl (%rbx, %rcx, 4), %eax    ; eax = *(rbx + rcx*4)

; Intel
mov eax, [rbx + rcx*4]        ; eax = *(rbx + rcx*4)
```

---

## 5. Esempio completo — prologo con canary

```asm
; AT&T (GCC output)
pushq  %rbp
movq   %rsp, %rbp
subq   $0x40, %rsp
movq   %fs:0x28, %rax
movq   %rax, -0x8(%rbp)

; Intel (GDB/GEF/Ghidra)
push   rbp
mov    rbp, rsp
sub    rsp, 0x40
mov    rax, QWORD PTR fs:0x28
mov    QWORD PTR [rbp-0x8], rax
```

Stessa cosa, aspetto diverso.

---

## 6. Come forzare la sintassi in GDB

GDB di default usa AT&T. Per passare a Intel:

```
(gdb) set disassembly-flavor intel
(gdb) disassemble main
```

Per renderlo permanente, aggiungilo a `~/.gdbinit`:

```
set disassembly-flavor intel
```

GEF e pwndbg usano Intel di default.

---

## 7. `movabs` — caso speciale per immediati a 64 bit

`mov` normale accetta immediati fino a **32 bit** (con estensione del segno a 64 bit). Se vuoi caricare un valore a 64 bit pieno in un registro serve `movabs`:

```asm
; Intel
mov    rax, 0x1234           ; ok — valore a 32 bit, esteso a 64
movabs rbx, 0x68732f6e69622f ; necessario — valore a 48 bit, non entra in 32
```

```asm
; AT&T equivalente
movq    $0x1234, %rax
movabsq $0x68732f6e69622f, %rbx
```

In pratica lo vedrai nello shellcode quando si carica la stringa `/bin/sh` in un registro:

```asm
movabs rbx, 0x68732f6e69622f   ; "/bin/sh" in little-endian (7 byte = 56 bit)
```

`0x68732f6e69622f` non entra in 32 bit → `mov` normale non basta → serve `movabs`.

> [!tip] Come riconoscerlo Se GDB/GEF mostra `movabs` invece di `mov`, significa che l'immediato è troppo grande per 32 bit. In AT&T lo stesso caso usa il suffisso `absq` (`movabsq`).


**nota**
`movq` specifica la dimensione dell'**operazione** — quanti bit vengono trasferiti. Ma il problema di `movabs` non riguarda la dimensione dell'operazione, riguarda la dimensione dell'**immediato** nell'encoding dell'istruzione.

Nell'encoding x86-64, la maggior parte delle istruzioni `mov` con immediato riservano solo **32 bit** per codificare la costante nell'istruzione stessa — poi la estendono a 64 bit automaticamente. Quindi:

```asm
movq $0x1234, %rax        ; ok — 0x1234 entra in 32 bit, esteso a 64 ✅
movq $0x68732f6e69622f, %rbx  ; NON ESISTE — la costante è 48 bit,
                               ; non ci sta nell'encoding normale ❌
```

`movabs` usa un encoding diverso che riserva **64 bit** per la costante nell'istruzione:

```asm
movabsq $0x68732f6e69622f, %rbx  ; ok — encoding speciale a 64 bit ✅
```

Quindi la distinzione è:

| |Dimensione operazione|Dimensione immediato|
|---|---|---|
|`movq`|64 bit|max 32 bit (esteso a 64)|
|`movabsq`|64 bit|64 bit pieni|

`movq` sposta 64 bit — ma se la **costante** supera i 32 bit, non puoi usarlo con un immediato. Devi usare `movabs`.

## Compilatore DIVERSO!!
**Perché non posso usare gcc come compilatore?** Ottima domanda! Sono strumenti diversi:

| |**GCC**|**NASM**|
|---|---|---|
|Scopo|Compila **codice C** → assembly → binario|Assembla direttamente **assembly → binario**|
|Sintassi assembly|AT&T (`movl %eax, %ebx`)|Intel (`mov rax, rbx`)|
|Aggiunge|Runtime C, libc, `_start` di sistema|Solo quello che scrivi tu|
|Output|Binario con overhead libc|Binario minimalista|

---

Il tuo file è scritto in **sintassi Intel** (quella di NASM) — GCC non lo capisce direttamente.

Potresti usare GCC ma dovresti:

```bash
# Rinominare in .s e aggiungere direttive AT&T... molto scomodo
gcc -nostdlib -static shellcode.s -o shellcode
```

Per shellcode si usa NASM perché:

- Sintassi Intel è più leggibile
- Controllo totale sui byte generati — zero aggiunge cose nascoste
- È lo standard nel mondo pwn/CTF

In pratica: **GCC** per programmi C, **NASM** per assembly puro.

## 8. Richiamo attivo

> [!question] Converti da AT&T a Intel (a mente)
> 
> 1. `movq %rsp, %rbp`
> 2. `movq -0x8(%rbp), %rdx`
> 3. `subq $0x40, %rsp`
> 4. `movq %fs:0x28, %rax`
> 5. `je <fun+62>` ← questa cambia?

> [!success] Risposte
> 
> 6. `mov rbp, rsp`
> 7. `mov rdx, QWORD PTR [rbp-0x8]`
> 8. `sub rsp, 0x40`
> 9. `mov rax, QWORD PTR fs:0x28`
> 10. `je <fun+62>` ← i salti non cambiano, stessa sintassi in entrambe