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

## 7. Richiamo attivo

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