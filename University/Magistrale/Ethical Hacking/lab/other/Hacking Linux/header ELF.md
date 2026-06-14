L'header [[ELF]] (Executable and Linkable Format) è la struttura iniziale di ogni file ELF — eseguibili, librerie condivise (.so), file oggetto (.o) e core dump su sistemi Linux/Unix. Serve a descrivere il formato del file e a dare al sistema le informazioni necessarie per interpretarlo correttamente, senza bisogno di leggere tutto il file.

Si trova all'inizio del file (offset 0) e ha dimensione fissa: 52 byte su sistemi a 32 bit, 64 byte su sistemi a 64 bit. La struttura è definita in `<elf.h>` come `Elf32_Ehdr` o `Elf64_Ehdr`.

I campi principali sono:

**e_ident** — i primi 16 byte, includono il "magic number" (0x7F 'E' 'L' 'F') che identifica il file come ELF, seguito da informazioni come la classe (32 o 64 bit), l'endianness (little o big endian), la versione del formato ELF, e l'ABI del sistema operativo target.

**e_type** — indica il tipo di file: oggetto rilocabile (ET_REL), eseguibile (ET_EXEC), libreria condivisa/oggetto dinamico (ET_DYN), o core dump (ET_CORE).

**e_machine** — specifica l'architettura del processore per cui il binario è stato compilato (x86, x86-64, ARM, RISC-V, ecc.).

**e_version** — versione del formato ELF, generalmente sempre 1 (EV_CURRENT).

**e_entry** — l'indirizzo virtuale del punto di ingresso, cioè dove il processore deve iniziare l'esecuzione quando il programma viene caricato.

**e_phoff** e **e_shoff** — offset nel file rispettivamente della program header table e della section header table.

**e_flags** — flag specifici dell'architettura (interpretazione dipendente dal processore).

**e_ehsize** — dimensione dell'header ELF stesso.

**e_phentsize** e **e_phnum** — dimensione di ogni entry nella program header table e numero totale di entry.

**e_shentsize**, **e_shnum**, **e_shstrndx** — analoghi per la section header table, più l'indice della sezione che contiene la tabella dei nomi delle sezioni (.shstrtab).

In pratica, leggendo solo questo header, il loader del sistema operativo (o un linker, o un debugger) sa già: che tipo di file ha davanti, per quale CPU è stato compilato, da dove iniziare l'esecuzione, e dove trovare le tabelle che descrivono il resto del file (segmenti per il caricamento in memoria e sezioni per il linking/debug).

Se vuoi, posso mostrarti un esempio pratico con `readelf -h` su un binario reale o la definizione della struttura in C.

## Cosa c'entra [[strace & ldd|ldd]] con ELF

`ldd` è un programma che mostra le librerie condivise (shared libraries, `.so`) richieste da un eseguibile o da un'altra libreria condivisa, cioè le sue dipendenze dinamiche.

Cosa legge nel binario:

In pratica `ldd` non fa magia propria: in genere imposta variabili d'ambiente speciali (come `LD_TRACE_LOADED_OBJECTS=1`) e poi esegue il dynamic linker/loader (`ld-linux.so` o equivalente) sul binario. Quando viene invocato in questo modo, il loader fa il suo normale lavoro di risoluzione delle dipendenze ma invece di avviare il programma stampa l'elenco delle librerie trovate e dove sono state caricate, poi esce.

Per fare questo, il loader (e quindi indirettamente `ldd`) legge dal binario ELF:

**La program header table**, in particolare i segmenti di tipo `PT_DYNAMIC` e `PT_INTERP`. `PT_INTERP` indica il percorso del dynamic linker da usare (es. `/lib64/ld-linux-x86-64.so.2`).

**La sezione/segmento dinamico (.dynamic)**, che contiene una serie di tag (`DT_NEEDED`, `DT_RPATH`, `DT_RUNPATH`, `DT_SONAME`, ecc.). I tag `DT_NEEDED` elencano i nomi delle librerie condivise richieste (es. `libc.so.6`).

A questo punto il loader cerca ciascuna libreria richiesta seguendo l'ordine standard di ricerca: `RPATH` (se presente nel binario), variabile d'ambiente `LD_LIBRARY_PATH`, `RUNPATH`, cache di `/etc/ld.so.cache` (generata da `ldconfig` a partire da `/etc/ld.so.conf`), e infine percorsi predefiniti come `/lib` e `/usr/lib`.

Per ogni dipendenza trovata, `ldd` stampa il nome della libreria, il percorso effettivo dove è stata localizzata, e l'indirizzo di base a cui è stata mappata in memoria (questo passaggio è ricorsivo: se libc dipende da altre librerie, vengono elencate anche quelle).

Da notare: `ldd` esegue effettivamente il loader sul binario (anche se non lancia il `main`), quindi su un eseguibile non fidato può essere rischioso — è preferibile usare `readelf -d` o `objdump -p` per ispezionare le dipendenze senza eseguire codice.