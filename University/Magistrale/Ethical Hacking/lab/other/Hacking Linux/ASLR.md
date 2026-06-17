# ASLR — Address Space Layout Randomization

> [!abstract] In una frase
> Il kernel randomizza gli indirizzi delle zone chiave del processo ad ogni esecuzione, rendendo impossibile per l'attaccante hardcodare un indirizzo nell'exploit. Implementata dal **sistema operativo** — non dal compilatore (differenza con il canary e PIE).

Collegamento: [[ETHL 0x07 — Binary Exploitation p1]] · [[Stack Canary]] · [[PIC-PIE]]

---

## 1. Il problema che risolve

Un exploit classico sovrascrive il return address con l'indirizzo di qualcosa di utile — per esempio `system()` in libc per chiamare `system("/bin/sh")`.

Senza ASLR questo funziona sempre:

```
system() è sempre a 0x7ffff7a52290
→ scrivo quell'indirizzo nel return address → shell
```

Con ASLR l'indirizzo cambia ad ogni esecuzione:

```
Esecuzione 1: system() a 0x7f2d4bc52290
Esecuzione 2: system() a 0x7f9a1de52290  ← diverso
Esecuzione 3: system() a 0x7f5c8ab52290  ← diverso
→ non so dove puntare → l'exploit crasha
```

---

## 2. Prima e dopo — visuale

**Senza ASLR** — stesso programma, tre esecuzioni:

```
Esecuzione 1          Esecuzione 2          Esecuzione 3
──────────────        ──────────────        ──────────────
stack  0x7fffffffe000 stack  0x7fffffffe000 stack  0x7fffffffe000
libc   0x7ffff7a00000 libc   0x7ffff7a00000 libc   0x7ffff7a00000
heap   0x00602000     heap   0x00602000     heap   0x00602000
text   0x00400000     text   0x00400000     text   0x00400000
```

**Con ASLR** — stesso programma, tre esecuzioni:

```
Esecuzione 1          Esecuzione 2          Esecuzione 3
──────────────        ──────────────        ──────────────
stack  0x7ffd3a2ce000 stack  0x7ffe891b4000 stack  0x7ffca73d1000
libc   0x7f2d4bc00000 libc   0x7f9a1de00000 libc   0x7f5c8ab00000
heap   0x01f3a000     heap   0x00d82000     heap   0x02c14000
text   0x005a3000     text   0x00e17000     text   0x00391000
```

---

## 3. Cosa viene randomizzato

|Zona|Descrizione|
|---|---|
|**Stack**|variabili locali, return address, canary|
|**Heap**|allocazioni dinamiche (`malloc`)|
|**Librerie condivise**|libc e tutte le `.so` caricate|
|**Base dell'eseguibile**|solo se compilato con **PIE**|
|**VDSO / mmap**|zone mappate dal kernel|

> [!warning] 
> Senza PIE, il codice del programma non viene randomizzato ASLR randomizza stack, heap e librerie. Ma se il binario è compilato **senza PIE**, il segmento `text` (il codice del programma) sta sempre allo stesso indirizzo — tipicamente `0x400000`. Questo è sfruttabile. ASLR e PIE vanno usati insieme per una protezione completa.

---

## 4. I livelli — differenza tra 1 e 2

Esistono due meccanismi di allocazione dell'heap in Linux:

- **`mmap()`** — alloca zone di memoria separate, ovunque nel virtual address space. Usato per allocazioni grandi e per le librerie condivise.
- **`brk()`** — sposta il "program break", il confine superiore del segmento dati. Usato da `malloc()` per le allocazioni piccole, ancorato vicino alla fine del BSS.

```
text   ──────────────
data   ──────────────
BSS    ──────────────
heap   ──────────────  ← cresce verso l'alto via brk()
       ...
libc   ──────────────  ← caricata via mmap()
stack  ──────────────
```

|Livello|Cosa randomizza|
|---|---|
|**0**|Nulla — tutto fisso|
|**1**|Stack, librerie (`mmap`), VDSO, heap `mmap` — ma **`brk()` rimane prevedibile**|
|**2**|Tutto il livello 1 **+ base dell'heap `brk()`**|

```
Livello 1 — due esecuzioni:
  libc   0x7f2d → 0x7f9a   ✅ randomizzata
  heap   0x00602000 → 0x00602000   ❌ sempre uguale

Livello 2:
  libc   0x7f2d → 0x7f9a   ✅ randomizzata
  heap   0x01f3 → 0x00d8   ✅ randomizzata
```

Quasi tutti i sistemi moderni usano livello 2. Il livello 1 esiste per compatibilità con programmi vecchi che si aspettano l'heap a un indirizzo fisso.

---

## 5. Come si configura — `/proc/sys/kernel/randomize_va_space`

Su Linux i parametri del kernel sono esposti come file nel filesystem virtuale `/proc` — non è una cartella reale su disco, il kernel la genera in memoria.

```bash
# leggi il livello attuale
cat /proc/sys/kernel/randomize_va_space
# → 2

# disattiva ASLR (richiede root — utile in laboratorio per debug deterministico)
echo 0 > /proc/sys/kernel/randomize_va_space

# oppure
setarch -R ./mioprogramma    # disattiva solo per quella esecuzione
```

> [!tip] In laboratorio / GDB Durante lo sviluppo di un exploit conviene disattivare ASLR per lavorare con indirizzi stabili. Una volta che l'exploit funziona, si reattiva ASLR e si aggiunge la tecnica di leak per bypassarlo.

---

## 6. `/proc` — perché è utile in exploitation

`/proc/self/maps` mostra la mappa di memoria reale del processo corrente, con gli indirizzi effettivi:

```bash
cat /proc/self/maps
# 7f2d4bc00000-7f2d4bd45000 r-xp ... libc.so
# 7ffd3a2ce000-7ffd3a2ef000 rw-p ... [stack]
```

Se durante un attacco riesci a leggere questo file (o un leak di indirizzo equivalente), conosci la posizione reale di tutto — ASLR è bypassata.

---

## 7. Limiti — quando ASLR non basta

|Tecnica bypass|Come funziona|
|---|---|
|**Info leak**|Una vulnerabilità separata rivela un indirizzo reale → si calcola la base da lì|
|**Brute force**|Su processi a 32 bit lo spazio è piccolo (~16 bit di entropia) → si prova ogni indirizzo|
|**Partial overwrite**|Si sovrascrive solo i byte bassi del return address (che non cambiano con ASLR)|
|**NOP sled**|Su stack di dimensioni note, si aumenta la superficie bersaglio|
|**Binario senza PIE**|Il segmento `text` è fisso → si usa codice del programma stesso come gadget|

---

## 8. Chi implementa cosa — riepilogo difese

|Difesa|Implementata da|Protegge da|
|---|---|---|
|**Canary**|Compilatore (`-fstack-protector`)|Overflow lineare sul return address|
|**ASLR**|Sistema operativo|Indirizzo hardcodato nell'exploit|
|**PIE**|Compilatore (`-fPIE`) + OS|Indirizzo fisso del codice del programma|
|**NX / W^X**|CPU + OS|Esecuzione di shellcode sullo stack|

---

## 9. Richiamo attivo

> [!question] Verifica (a libro chiuso)
> 
> 1. Cosa impedisce esattamente ASLR? Perché senza di essa un exploit è più semplice?
> 2. Quale zona di memoria NON viene randomizzata da ASLR se il binario non ha PIE?
> 3. Qual è la differenza pratica tra livello 1 e livello 2? Cosa aggiunge il 2?
> 4. Cosa sono `brk()` e `mmap()` e perché la distinzione conta per ASLR?
> 5. Come disattivi ASLR in laboratorio? In due modi diversi.
> 6. Cosa contiene `/proc/self/maps` e perché è utile per un attaccante?
> 7. ASLR e PIE — perché vanno usati insieme?ù

