# GDB — Guida Completa

> [!abstract] Cos'è GDB **GNU Debugger (GDB)** è il debugger standard su Linux per programmi C/C++ (e non solo). Permette di eseguire un programma passo-passo, ispezionare registri e memoria, impostare breakpoint e analizzare crash. È lo strumento principale per il **reverse engineering** e il **pwning** in ambito CTF.

---

## Installazione

```bash
sudo apt install gdb python3 python3-pip -y
```

### Plugin consigliati

```bash
# GEF (GDB Enhanced Features) — consigliato per CTF/pwning
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

# Dipendenze opzionali GEF
pip3 install capstone unicorn keystone-engine ropper
```

Consiglio del grande **Professor Demetrescu** (mi manchi): 
inserire in `/home/utente/.gdbinit`:
```
define go:
	start
	layout src
	layout regs
	focus cmd
end
```

in questo modo starti gdb, scegli il break point della funzione che vuoi analizzare (con `break nome_funzione`) e poi esegui `go`.

---

## Avvio

```bash
gdb ./programma               # avvio diretto
gdb ./programma core          # analisi di un core dump
gdb -p <PID>                  # attach a processo in esecuzione
gdb --args ./prog arg1 arg2   # con argomenti
```

> [!tip] Compilazione ottimale Compila sempre con questi flag per il debugging:
> 
> ```bash
> gcc -g -fno-stack-protector -no-pie -o vuln vuln.c
> ```
> 
> - `-g` → include simboli di debug
> - `-fno-stack-protector` → disabilita canary
> - `-no-pie` → indirizzi fissi (più facile da analizzare)

---

## Comandi Essenziali

### Esecuzione

|Comando|Alias|Descrizione|
|---|---|---|
|`run`|`r`|Avvia il programma|
|`run < input.txt`||Avvia con input da file|
|`continue`|`c`|Continua fino al prossimo breakpoint|
|`kill`|`k`|Termina il processo|
|`quit`|`q`|Esci da GDB|

### Step-by-step

|Comando|Alias|Descrizione|
|---|---|---|
|`step`|`s`|Esegui una riga C (entra nelle funzioni)|
|`next`|`n`|Esegui una riga C (salta le funzioni)|
|`stepi`|`si`|Esegui una **istruzione assembly** (entra)|
|`nexti`|`ni`|Esegui una **istruzione assembly** (salta)|
|`finish`|`fin`|Esegui fino al `return` della funzione corrente|
|`until <N>`||Esegui fino alla riga N|

> [!warning] step vs stepi `step`/`next` lavorano a livello di **codice sorgente C** (richiede `-g`). `stepi`/`nexti` lavorano a livello di **istruzioni assembly** — necessari quando non ci sono simboli.

---

## Breakpoint

### Impostare breakpoint

```bash
break main                    # su funzione
break vulnerable_function
break vuln.c:42               # su file:riga
break *0x401162               # su indirizzo esatto (assembly)
break *main+10                # offset da simbolo
```

### Gestire breakpoint

```bash
info breakpoints              # lista tutti i breakpoint (i b)
delete 1                      # elimina breakpoint #1
delete                        # elimina tutti
disable 2                     # disabilita #2 (senza eliminarlo)
enable 2                      # riabilita #2
```

### Breakpoint condizionali

```bash
break main if argc == 2       # si attiva solo se condizione vera
condition 1 i == 5            # aggiunge condizione al breakpoint #1
```

### Watchpoint (breakpoint su memoria)

```bash
watch *0x7fffffffdcf0         # si ferma quando quell'indirizzo cambia
watch variabile               # si ferma quando la variabile cambia
rwatch variabile              # si ferma in lettura
awatch variabile              # si ferma in lettura E scrittura
```

---

## Registri

```bash
info registers                # tutti i registri (i r)
info registers rsp rbp rip    # solo quelli specificati
i r rax rbx rcx rdx           # shorthand

print $rip                    # stampa valore di un registro
print/x $rsp                  # in esadecimale
print/d $rax                  # in decimale
print/t $rax                  # in binario
```

### Registri x86-64 principali

|Registro|Uso|
|---|---|
|`rip`|Instruction Pointer — istruzione corrente|
|`rsp`|Stack Pointer — cima dello stack|
|`rbp`|Base Pointer — base del frame corrente|
|`rax`|Valore di ritorno delle funzioni|
|`rdi rsi rdx rcx r8 r9`|Argomenti delle funzioni (in ordine)|
|`eflags`|Flag: ZF, CF, PF, SF, OF...|

---

## Esaminare la Memoria

### Comando `x` (examine)

**Sintassi:** `x/<N><formato><size> <indirizzo>`

```bash
x/32xb $rsp        # 32 byte in hex
x/32xw $rsp        # 32 word (4 byte) in hex
x/32xg $rsp        # 32 giant (8 byte) in hex — ideale su 64bit
x/s $rsp           # interpreta come stringa
x/i $rip           # interpreta come istruzione assembly
x/10i $rip         # prossime 10 istruzioni
```

|Size|Significato|
|---|---|
|`b`|byte (1 byte)|
|`h`|halfword (2 byte)|
|`w`|word (4 byte)|
|`g`|giant (8 byte)|

|Formato|Significato|
|---|---|
|`x`|esadecimale|
|`d`|decimale|
|`u`|decimale senza segno|
|`o`|ottale|
|`t`|binario|
|`s`|stringa|
|`i`|istruzione assembly|

---

## Analisi dello Stack

```bash
# Dump raw dello stack
x/32xg $rsp

# Navigare i frame
backtrace            # mostra call stack completo (bt)
frame 0              # seleziona frame (0 = corrente)
frame 2              # vai al frame 2
info frame           # dettagli del frame corrente
info locals          # variabili locali del frame
info args            # argomenti della funzione corrente
```

### Calcoli sugli indirizzi

```bash
print/x $rbp - $rsp              # dimensione del buffer locale
print/x $rbp + 8                 # indirizzo del return address
printf "offset: %d\n", $rbp-$rsp # formattazione custom
```

> [!example] Layout tipico dello stack Dato `char buffer[0x10]` con `RSP=0x7fffffffdcf0` e `RBP=0x7fffffffdd00`:
> 
> ```
> 0x7fffffffdcf0  [ buffer[0x10] — 16 byte ]  ← RSP
> 0x7fffffffdd00  [ saved RBP   —  8 byte  ]  ← RBP
> 0x7fffffffdd08  [ return addr —  8 byte  ]  ← RBP+8
> ```
> 
> Per raggiungere il return address: `16 + 8 = 24 byte` di padding.

---

## Print e Espressioni

```bash
print variabile               # valore di una variabile (p)
print/x variabile             # in hex
print *puntatore              # dereference
print array[3]                # elemento di array
print sizeof(buffer)          # sizeof
print (int)0x41               # cast
print $rbp - $rsp             # espressione aritmetica tra registri
```

### Modificare valori a runtime

```bash
set $rip = 0x401234           # modifica registro
set variable x = 42           # modifica variabile
set *0x7fffffffdcf0 = 0x41    # scrivi in memoria
```

---

## Disassembly

```bash
disassemble                   # funzione corrente
disassemble main              # funzione specifica
disassemble 0x401150          # da indirizzo
disassemble /m vulnerable_function   # con sorgente intercalata
disassemble /r main           # con bytes raw

set disassembly-flavor intel  # sintassi Intel (più leggibile)
set disassembly-flavor att    # sintassi AT&T (default)
```

---

## Info Utili

```bash
info functions                # lista tutte le funzioni
info variables                # lista tutte le variabili globali
info address main             # indirizzo di un simbolo
info symbol 0x401162          # simbolo a quell'indirizzo
info proc mappings            # mappa della memoria del processo
info sharedlibrary            # librerie condivise caricate
maintenance info sections     # sezioni ELF
```

---

## GEF — Comandi Aggiuntivi

> [!info] Installazione GEF
> 
> ```bash
> bash -c "$(curl -fsSL https://gef.blah.cat/sh)"
> ```

```bash
context                       # panoramica completa: reg + stack + asm
stack 20                      # primi 20 entry dello stack
registers                     # registri colorati e annotati
vmmap                         # mappa virtuale della memoria (RWX)
checksec                      # protezioni del binario (NX, PIE, canary...)
```

### Pattern ciclico (De Bruijn)

```bash
pattern create 100            # genera stringa di 100 byte univoca
# → usa come input al programma
pattern offset $rip           # trova quanti byte prima di sovrascrivere RIP
pattern offset 0x6161616162   # oppure con valore hex diretto
```

> [!tip] Uso pratico
> 
> 1. `pattern create 100` → copia l'output
> 2. `run` → incolla come input
> 3. Il programma crasha — RIP contiene parte del pattern
> 4. `pattern offset $rip` → ti dice l'offset esatto del return address

### Altre utility GEF

```bash
heap chunks                   # analisi heap
got                           # Global Offset Table
plt                           # Procedure Linkage Table
elf-info                      # info sull'eseguibile ELF
xor-memory display $rsp 64 0x41  # XOR di un blocco di memoria
hexdump byte $rsp 32          # hexdump leggibile
dereference $rsp 20           # dereference ricorsivo dello stack
```

---

## Workflow CTF — Buffer Overflow

```bash
# 1. Analisi iniziale
gdb ./vuln
(gdb) checksec                      # verifica protezioni
(gdb) info functions                # cerca funzioni interessanti (es: win, flag)

# 2. Trova l'offset
(gdb) pattern create 100
(gdb) run                           # inserisci il pattern come input
(gdb) pattern offset $rip           # → es: offset = 24

# 3. Verifica l'offset
(gdb) run
# inserisci: python3 -c "print('A'*24 + 'B'*8)"
(gdb) x/xg $rbp+8                   # deve mostrare 0x4242424242424242

# 4. Trova l'indirizzo target
(gdb) print &win_function
(gdb) info address win_function     # → es: 0x401196

# 5. Costruisci il payload (fuori da gdb)
# python3 -c "import struct; print('A'*24 + struct.pack('<Q', 0x401196))"
```

---

## File .gdbinit

Puoi salvare configurazioni persistenti in `~/.gdbinit`:

```bash
set disassembly-flavor intel
set pagination off
set print pretty on
set print array on
break main
```

> [!note] Autocaricamento locale GDB carica anche un `.gdbinit` nella directory corrente (se abilitato). Utile per avere configurazioni per-progetto.

---

## Comandi Rapidi — Cheatsheet

```bash
r                    # run
c                    # continue
s / si               # step (sorgente / assembly)
n / ni               # next (sorgente / assembly)
fin                  # finish
b <sym/addr>         # breakpoint
i b                  # info breakpoints
d <N>                # delete breakpoint N
p/x $reg             # print registro in hex
x/32xg $rsp          # dump stack
bt                   # backtrace
i frame              # info frame corrente
i locals             # variabili locali
disas /m <func>      # disassembly con sorgente
set $rip = 0x...     # modifica RIP
q                    # quit
```