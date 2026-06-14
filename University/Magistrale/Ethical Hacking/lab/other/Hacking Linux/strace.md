# strace

Tool da riga di comando che traccia in **tempo reale** le system call (e i segnali) effettuate da un processo, mostrando nome, argomenti, valore di ritorno ed eventuali errori.

```bash
strace ./programma arg1 arg2
strace -p <PID>          # attacca a un processo già in esecuzione
```

Output tipico:

```
execve("./programma", ["./programma"], 0x7ffd... /* 60 vars */) = 0
brk(NULL)                               = 0x55c000
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f...
read(3, "Hello, World!\n", 14)          = 14
write(1, "Hello, World!\n", 14)         = 14
exit_group(0)                           = ?
```

## Come funziona internamente

`strace` usa la syscall **`ptrace(2)`** per agganciarsi al processo target. Il kernel notifica il tracer (strace) ogni volta che il processo tracciato entra/esce da una syscall, permettendo a `strace` di leggerne argomenti e valore di ritorno **senza modificare il binario**.

A differenza di [[ldd]] e di `readelf`, `strace` **non analizza la struttura statica del file ELF** — osserva il comportamento dinamico del processo durante l'esecuzione reale.

## Cosa rivela

- **File**: `open`/`openat`, `read`, `write`, `close`, `stat` → quali file vengono letti/scritti/cercati
- **Memoria**: `mmap`, `brk`, `mprotect` → allocazioni, mapping di librerie
- **Processi**: `fork`, `execve`, `wait4`, `exit_group`
- **Rete**: `socket`, `connect`, `bind`, `send`/`recv`
- **Segnali**: `rt_sigaction`, ricezione di `SIGSEGV`, `SIGTERM`, ecc.
- **Errori**: ogni syscall fallita mostra il codice errore (es. `ENOENT`, `EACCES`)

> [!tip] Dedurre le dipendenze dinamiche Filtrando le `openat()` su file `.so` si può osservare quali librerie vengono effettivamente caricate a runtime — un effetto collaterale utile, ma non lo scopo principale dello strumento (per quello c'è `ldd`/`readelf -d`).

## Opzioni utili

```bash
strace -f ./programma        # traccia anche i processi figli (fork/clone)
strace -e trace=open,read,write ./programma   # filtra solo certe syscall
strace -e trace=network ./programma           # solo syscall di rete
strace -c ./programma         # statistiche riassuntive (conteggio, tempo per syscall)
strace -o output.txt ./programma              # salva su file
strace -T ./programma          # mostra il tempo impiegato da ogni syscall
strace -tt ./programma          # timestamp con microsecondi
```

## strace vs ldd vs readelf

|Strumento|Cosa fa|Esecuzione?|Domanda a cui risponde|
|---|---|---|---|
|`ldd`|risolve dipendenze dinamiche dichiarate (`DT_NEEDED`)|sì (solo loader)|"di cosa ha bisogno per partire?"|
|`readelf -d`|legge i tag `.dynamic` senza risolverli|no|"cosa dichiara di aver bisogno?"|
|`strace`|traccia tutte le syscall a runtime|sì (programma intero, fino in fondo)|"cosa fa, passo per passo, mentre gira?"|

## Note pratiche

- Aggiunge un overhead significativo: il programma gira **molto più lentamente** sotto `strace`
- Su binari **setuid/setgid** può non funzionare per motivi di sicurezza
- Strumento complementare a `ltrace` (traccia chiamate a librerie dinamiche invece che syscall) e a debugger come `gdb`

## Collegamenti

- [[ldd]]
- [[ELF]]