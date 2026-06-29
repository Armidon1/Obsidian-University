# ldd

Tool da riga di comando per elencare le **librerie condivise** (`.so`) richieste da un eseguibile o da un'altra libreria dinamica, insieme al path dove vengono effettivamente risolte.

```bash
ldd ./programma
```

Output tipico:

```
linux-vdso.so.1 =>  (0x00007ffd...)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f...)
/lib64/ld-linux-x86-64.so.2 (0x00007f...)
```

## Come funziona internamente

`ldd` **non analizza staticamente il file** — esegue il [[ELF - Executable and Linkable Format|dynamic linker/loader]] sul binario, impostando la variabile d'ambiente:

```
LD_TRACE_LOADED_OBJECTS=1
```

Con questa variabile attiva, il loader (es. `/lib64/ld-linux-x86-64.so.2`) fa il suo normale lavoro di startup ma **non avvia il `main()`**: si limita a risolvere le dipendenze e a stamparle.

### Cosa legge dal binario ELF

1. **`PT_INTERP`** (program header) → percorso del dynamic linker da usare
2. **`.dynamic`** (segmento/sezione dinamica) → tag `DT_NEEDED`, uno per ogni libreria richiesta
3. Per ciascun `DT_NEEDED`, il loader cerca il file seguendo l'ordine standard:
    - `RPATH` (se presente nel binario, deprecato)
    - `LD_LIBRARY_PATH` (variabile d'ambiente)
    - `RUNPATH` (successore moderno di RPATH)
    - `/etc/ld.so.cache` (generata da `ldconfig` da `/etc/ld.so.conf`)
    - percorsi di default (`/lib`, `/usr/lib`)
4. Il processo è **ricorsivo**: se una libreria trovata ha a sua volta dipendenze, vengono elencate anche quelle

> [!warning] Sicurezza Poiché `ldd` esegue (in parte) il loader sul binario, su file **non fidati** può essere rischioso — il caricamento di librerie può eseguire codice (es. costruttori `.init_array`). Per un'analisi puramente statica usare:
> 
> ```bash
> readelf -d ./programma   # legge solo i tag .dynamic, nessuna esecuzione
> objdump -p ./programma    # alternativa equivalente
> ```

## ldd vs altri strumenti

|Strumento|Cosa fa|Esecuzione?|
|---|---|---|
|`ldd`|risolve e stampa le dipendenze dinamiche dichiarate (`DT_NEEDED`)|sì (loader)|
|`readelf -d`|legge i tag della sezione `.dynamic` senza risolverli|no|
|`strace`|traccia tutte le syscall a runtime (incluse le `openat()` sulle `.so`)|sì (programma intero)|

`ldd` risponde a "**di cosa ha bisogno questo binario per partire?**". `strace` risponde a "**cosa fa questo programma, passo per passo, mentre è in esecuzione?**" — e tra le tante cose osservate ci sono anche i caricamenti delle librerie.

## Casi particolari

- Su **binari statici** (`ET_EXEC` senza `PT_INTERP`), `ldd` riporta tipicamente "not a dynamic executable"
- `linux-vdso.so.1` è una libreria virtuale fornita dal kernel, non un file su disco
- `ldd` su una libreria (`.so`) ne mostra le dipendenze a sua volta

## Collegamenti

- [[ELF]]
- [[strace]]