# ELF - Executable and Linkable Format

Formato standard per file binari su sistemi Unix/Linux: eseguibili, librerie condivise, file oggetto e core dump. vedi anche [[header ELF]]

## Tipi di file ELF

- **ET_REL** – file oggetto rilocabile (`.o`), output del compilatore prima del linking
- **ET_EXEC** – eseguibile statico
- **ET_DYN** – libreria condivisa (`.so`) o eseguibile dinamico (PIE)
- **ET_CORE** – core dump (snapshot della memoria di un processo crashato)

## Struttura generale del file

```
+--------------------+
|     ELF Header     |
+--------------------+
| Program Header Tbl |  <- vista "a runtime" (segmenti)
+--------------------+
|     .text          |
|     .data          |
|     .bss           |
|     .rodata        |
|     ...            |
+--------------------+
| Section Header Tbl |  <- vista "a link-time" (sezioni)
+--------------------+
```

## ELF Header

Dimensione fissa: 52 byte (32 bit) / 64 byte (64 bit). Vedi nota collegata: [[ELF Header]]

Campi principali:

- `e_ident` → magic number `7F 45 4C 46` ("\x7fELF") + classe/endianness/ABI
- `e_type` → tipo di file (vedi sopra)
- `e_machine` → architettura target (x86-64, ARM, RISC-V...)
- `e_entry` → indirizzo del punto di ingresso (entry point)
- `e_phoff` / `e_shoff` → offset alle tabelle program/section header

## Program Header Table

Descrive i **segmenti**: blocchi che il loader mappa in memoria a runtime.

|Tipo|Significato|
|---|---|
|`PT_LOAD`|segmento da caricare in memoria (codice/dati)|
|`PT_DYNAMIC`|informazioni per il linker dinamico (`.dynamic`)|
|`PT_INTERP`|percorso del dynamic linker (es. `/lib64/ld-linux-x86-64.so.2`)|
|`PT_NOTE`|metadati ausiliari|
|`PT_PHDR`|posizione della program header table stessa|

## Section Header Table

Descrive le **sezioni**: vista usata da linker, debugger, strumenti statici.

Sezioni comuni:

- `.text` → codice eseguibile
- `.data` → variabili globali inizializzate
- `.bss` → variabili globali non inizializzate (occupa 0 byte su disco)
- `.rodata` → dati costanti (stringhe, ecc.)
- `.symtab` / `.dynsym` → tabelle dei simboli
- `.strtab` / `.dynstr` → tabelle delle stringhe
- `.dynamic` → tag per il linker dinamico (`DT_NEEDED`, `DT_RPATH`, ...)
- `.rel.*` / `.rela.*` → informazioni di rilocazione
- `.shstrtab` → nomi delle sezioni

> [!tip] Differenza chiave I **segmenti** (program header) servono al **loader a runtime** per caricare il binario in memoria. Le **sezioni** (section header) servono a **linker/debugger** e possono essere rimosse (`strip`) senza impedire l'esecuzione.

## Linking dinamico e dipendenze

Le librerie condivise richieste sono elencate nella sezione `.dynamic` tramite tag `DT_NEEDED`.

Strumenti utili:

- `ldd binario` → mostra le librerie risolte (esegue il loader, attenzione su binari non fidati!)
- `readelf -d binario` → mostra i tag dinamici senza eseguire nulla
- `objdump -p binario` → alternativa a `readelf -d`

Ordine di ricerca delle librerie: `RPATH` → `LD_LIBRARY_PATH` → `RUNPATH` → `/etc/ld.so.cache` → percorsi di default (`/lib`, `/usr/lib`)

## Comandi utili per l'ispezione

```bash
file binario          # tipo di file, architettura, dinamico/statico
readelf -h binario     # ELF header
readelf -l binario     # program headers (segmenti)
readelf -S binario     # section headers
readelf -d binario     # tabella dinamica (dipendenze)
readelf -s binario      # tabella dei simboli
objdump -d binario       # disassemblato
nm binario               # simboli
strings binario          # stringhe leggibili
```

## Collegamenti

- [[ELF Header]]
- [[Linking statico vs dinamico]]
- [[Reverse Engineering - strumenti base]]