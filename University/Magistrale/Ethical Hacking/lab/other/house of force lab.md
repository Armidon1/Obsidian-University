# Handoff — Phase 1 (0x09)

## Stato

|Lab|Stato|
|---|---|
|House of Force|✅ completato|
|fastbin-dup|🔄 prossimo|
|Phase 2 (CTF)|⏳ scadenza 26/06 23.59|

> [!warning] Scadenza domani Consegna flag + report entro **26 giugno 23.59**. L'AI è esplicitamente incoraggiata dal prof. L'assignment migliora il voto solo se supera lo scritto.

---

## Teoria consolidata — malloc internals

### Arena, heap, bins

- **Arena** = struct `malloc_state` di glibc, il _manager_: contiene `fastbins[]`, puntatore `top`, `bins[]`, `next` (lista circolare delle arene). La **main arena** è statica in libc (indirizzo fisso rispetto alla base libc); le arene dei thread nascono via `mmap`.
- **Heap** = memoria grezza contigua da `brk`/`mmap`, divisa in chunk, termina col top chunk.
- **Bins** = liste di chunk liberati dentro l'arena.

|Bin|Range|Politica|
|---|---|---|
|Fast|0x20–0x80|LIFO, O(1), no coalescenza|
|Unsorted|qualsiasi|staging area dei free recenti|
|Small|< 512B|exact-fit, coalescenza|
|Large|≥ 512B|best-fit, ordinata|

> [!note] Cosa glibc ignora Traccia solo memoria disponibile/liberata, non gli oggetti logici. Nessun metadato per-allocazione oltre l'header — è proprio questo spazio che le tecniche heap sfruttano.

### Struttura del chunk

```
[ prev_size (8) ][ size|flags (8) ][ user data ... ]
```

- glibc considera l'header lungo **0x10** (include `prev_size`), anche se `size|flags` è solo 8 byte.
- `prev_size` di un chunk appartiene al **chunk precedente in memoria**: sta al primo indirizzo del chunk corrente, ma se il precedente è in uso quei byte gli vengono _prestati_ come dati.
- Per questo `usable = chunk_size - 8` (si perde solo `size|flags`).
- Se il chunk precedente è in uso può sovrascrivere quei byte; un overflow oltre `chunk_size - 8` corrompe l'header del chunk successivo.

> [!info] Formula della size 
> `chunk_size = max((X + 8 + 15) & ~15, 32)`. Il `+15` prima dell'AND arrotonda **su** al multiplo di 16; `~15` azzera i 4 bit bassi. Il flag `PREV_INUSE` aggiunge `+1` alla size vista in `vis` (es. `0x21` = 0x20 + 1).

### Top chunk e _int_malloc

- Il top chunk ha solo `size`, nessun dato. Malloc lo "morde" dal basso ad ogni allocazione; quando si esaurisce → `sysmalloc` (`brk` estende, altrimenti `mmap`).
- `malloc()` è un wrapper di `_int_malloc(av, size)`, dove `av` è il puntatore all'arena corrente.
- Nel label `use_top`: l'unico controllo è `if (size >= nb + MINSIZE)`. Nessuna validazione del valore di `size`.

> [!warning] Perché HoF funziona Sovrascrivendo il `size` del top chunk con `0xffffffffffffffff`, il check è sempre vero. Malloc crede di avere spazio infinito e calcola `new_top = victim + nb` fidandosi ciecamente → write-what-where via wrap-around a 64 bit. Morto su glibc ≥ 2.29 (`corrupted top size`).

---

## ✅ House of Force — risolto

### Il binario

- glibc **2.28 no-tcache**, **No PIE** (base `0x400000`), Full RELRO, NX. ASLR attivo su heap/libc.
- Leak gratuiti nel sorgente: `puts()` → base libc; `initial_chunk - 0x10` → base heap.

> [!danger] La vulnerabilità `read(0, chunk, malloc_usable_size(chunk) + 8)` — quel `+ 8` legge 8 byte oltre l'usable, finendo nel `size|flags` del chunk successivo. Con un chunk adiacente al top chunk si corrompe il suo `size`.

### Il target

- `char target[16] = "not_pwned_yet"` → sta in **.data** (è inizializzata), non .bss.
- Indirizzo fisso (No PIE): `0x404010`. Leggibile con `elf.sym.target` o `p &target`.
- Opzione 2 del menu stampa `target` → utile per verificare il successo.

### I tre step

1. `malloc(0x18, b"A"*0x18 + p64(0xffffffffffffffff))` → corrompe il size del top chunk.
2. `malloc(nb, ...)` → wrap-around che sposta il top chunk su `target - 0x10`.
3. `malloc(qualsiasi, b"pwned\0")` → malloc restituisce `target`, ci si scrive sopra.

### Formula corretta (64-bit)

> [!info] nb corretto `D = (target - 0x10 - top_chunk_addr) & 0xffffffffffffffff` `nb = (D - 8) & 0xffffffffffffffff`
> 
> Motivazione: `request2size(nb) = (nb + 0x17) & ~0xf`. Siccome `D` è sempre multiplo di 16 (sia `target - 0x10 = 0x404000` che `top_chunk_addr = heap_base + 0x20` sono 0x10-allineati), passare `D` direttamente fa atterrare il new top 16 byte dopo il target. Con `nb = D - 8`, `request2size(D-8) = D`, quindi `new_top = target - 0x10` esatto → step 3 restituisce `target`. Il `-0x10` nell'header è corretto per 64-bit (Malloc Maleficarum usa `-8` perché è 32-bit).

> [!note] Diagnosi con vis 
> `vis` attraversa chunk in avanti (indirizzi crescenti). Dopo step 2, il huge chunk esce dalla pagina heap a `0x405000` e `vis` stampa "end of memory mapping" — questo è **normale**, non un errore. Il new top è a indirizzi più bassi (wrap-around) e `vis` non lo raggiunge. Per verificare dove ha atterrato il top: `p/x main_arena.top` in GDB.

---

## Prossimo: fastbin-dup

### Teoria (da ripassare)

- **Fastbin** = LIFO singly-linked list, chunking solo per size class 0x20–0x80. No coalescenza.
- `fd` pointer: primo 8 byte del user data (quando il chunk è libero).
- **Double-free**: liberare lo stesso chunk due volte → loop nella freelist → due malloc restituiscono lo stesso indirizzo.
- **fd corruption**: sovrascrivere `fd` di un chunk libero → malloc restituisce un indirizzo arbitrario al secondo prelievo.
- `find-fake-fast` (pwndbg): cerca indirizzi in memoria dove il valore a `addr - 0x8` potrebbe passare il size check di glibc.

### Setup previsto

- `DEMO_MODE=1 ./exploit-template.py GDB=1` → pause automatiche con `demo()`.
- Verificare con `fastbins` in pwndbg la struttura della freelist dopo ogni free.

---

## Setup tecnico (memo)

- **tmux**: `Ctrl+b` poi numero = cambia finestra; `c` = nuova; `%`/`"` = split.
- **GDB**: il prompt `pwndbg>` non appare mentre il processo gira — usare `Ctrl+C` o breakpoint.
- Comandi pwndbg utili: `vis`, `heap`, `bins`, `fastbins`, `telescope`, `vmmap`, `p/x main_arena.top`.
- Template: scrivere solo tra i marcatori `=====`. Helper già pronti: `malloc(size, data)`, `demo(msg)`. Leak già risolti in `libc.address` e `heap_base`.
- Note Python: `p64(v)` = pack 8 byte little-endian; **non** usare `id()`; attenzione all'indentazione.

---

## Prossimi step

- [x] House of Force completato — `target` = `pwned` ✓
- [ ] Lab `fastbin-dup` (Phase 1) — double-free, corruzione `fd`, `find-fake-fast`.
- [ ] **Phase 2 (CTF)** — due servizi di rete, sorgenti dal 29/05, build locale con `make` (patchelf alla glibc remota). Sviluppo local-first, no brute force.