# Double Free

**Categoria:** #binary-exploitation #memory-corruption #pwn  
**Linguaggio:** C / C++  
**Area:** Heap Exploitation

---

## 📖 Cos'è

Una vulnerabilità che avviene quando `free()` viene chiamato **due volte sullo stesso blocco di memoria**. Corrompe le strutture interne dell'heap allocator e può portare a **esecuzione di codice arbitrario**.

---

## 🧠 Prerequisiti — come funziona la memoria

```c
char *ptr = malloc(64);  // alloca 64 byte sull'heap
free(ptr);               // libera quei 64 byte → tornano all'allocatore
```

Quando chiami `free()`, il blocco viene segnato come disponibile e inserito in una struttura interna (es. **tcache** o **fastbin** in glibc).

---

## ❌ Il problema

```c
char *ptr = malloc(64);
free(ptr);   // ✅ primo free — corretto
free(ptr);   // ❌ secondo free — DOUBLE FREE
```

Al secondo `free()`:

- Il blocco è già nella lista dei chunk liberi
- L'allocatore **corrompe le sue linked list interne**
- Il comportamento è **undefined** → crash o exploitabile

---

## 💥 Exploitation — tcache poisoning

La tecnica più comune su glibc moderna:

```
1. malloc(A)    → alloca chunk A
2. free(A)      → A finisce nella tcache
3. free(A)      → A inserito di nuovo → tcache corrotta
4. malloc()     → restituisce A
5. malloc()     → restituisce A di nuovo
→ due puntatori allo stesso blocco di memoria
→ scrivi su uno, controlli l'altro → arbitrary write
```

### Obiettivi tipici dell'exploit

- **Arbitrary write** — scrivere in zone di memoria arbitrarie
- **GOT overwrite** — sovrascrivere la Global Offset Table per hijackare funzioni
- **RCE** — esecuzione di codice arbitrario

---

## 🔍 Esempio di codice vulnerabile

```c
#include <stdlib.h>

int main() {
    char *buf = malloc(128);

    if (errore) {
        free(buf);  // free in caso di errore
    }

    free(buf);      // ❌ DOUBLE FREE se errore == true
    return 0;
}
```

---

## 🛡️ Come si previene

```c
// Azzerare sempre il puntatore dopo free()
free(ptr);
ptr = NULL;  // free(NULL) è no-op → nessun danno al secondo free
```

Altre mitigazioni:

- **AddressSanitizer (ASan)** — rileva double free a runtime durante sviluppo
- **Safe allocator** — allocatori moderni con protezioni integrate (es. jemalloc)

---

## 🔗 Relazioni con altre vulnerabilità

|Vulnerabilità|Relazione|
|---|---|
|Use-After-Free (UAF)|Simile — accesso a memoria già liberata|
|Heap Overflow|Stesso contesto — heap corruption|
|tcache poisoning|Tecnica di exploit del double free|
|GOT overwrite|Obiettivo finale dell'exploit|

---

## 🛠️ Tool utili

```bash
# Rileva double free durante sviluppo/analisi
gcc -fsanitize=address -g programma.c -o programma
./programma

# Analisi binaria
gdb ./programma
pwndbg      # plugin GDB per heap analysis
peda        # alternativa a pwndbg
```

---
# La struttura interna dell'heap in glibc

### Il concetto base: i chunk

Quando chiami `malloc(64)`, glibc non ti dà semplicemente 64 byte. Ti dà un **chunk**, che è una struttura così fatta in memoria:

```
+------------------+
|   prev_size      |  ← 8 byte: dimensione del chunk precedente (se libero)
+------------------+
|   size           |  ← 8 byte: dimensione di questo chunk + flag
+------------------+
|                  |
|   USER DATA      |  ← quello che usi tu (i tuoi 64 byte)
|                  |
+------------------+
```

Il campo `size` contiene anche dei **flag** nei bit meno significativi:

- **P (PREV_INUSE)** — il chunk precedente è allocato
- **M (MMAP)** — chunk ottenuto via mmap
- **A (NON_MAIN_ARENA)** — appartiene a un'altra arena

---

### I chunk liberi hanno una struttura diversa

Quando fai `free()`, i byte che erano tuoi vengono **riutilizzati** dall'allocatore per mantenere la linked list:

```
+------------------+
|   prev_size      |
+------------------+
|   size           |
+------------------+
|   fd             |  ← puntatore al chunk libero successivo (forward)
+------------------+
|   bk             |  ← puntatore al chunk libero precedente (backward)
+------------------+
|   (spazio vuoto) |
+------------------+
```

Questi `fd` e `bk` formano una **doubly linked list** di chunk liberi.

---

### I bin — dove vanno i chunk liberi

glibc organizza i chunk liberi in strutture chiamate **bin**:

```
tcache    → chunk piccoli, per thread (glibc ≥ 2.26)
fastbin   → chunk piccoli, LIFO, no coalescing
smallbin  → chunk medi, doubly linked list
largebin  → chunk grandi
unsorted bin → tutti i chunk appena liberati, smistati dopo
```

La **tcache** (thread cache) è quella più rilevante oggi:

- Ogni thread ha la sua tcache
- È una **singly linked list** (solo `fd`, no `bk`)
- Tiene fino a 7 chunk per ogni dimensione
- **Pochissime protezioni** → bersaglio preferito degli exploit

---

### Cosa succede esattamente durante un Double Free

Partiamo da uno stato iniziale pulito. Allochi un chunk:

```
malloc(64) → restituisce chunk A

tcache[64]: vuoto
```

Primo `free(A)` — corretto:

```
tcache[64]: A → NULL

chunk A in memoria:
fd = NULL  (è il primo della lista)
```

Secondo `free(A)` — double free:

```
tcache[64]: A → A → A → ... (ciclo infinito!)

chunk A in memoria:
fd = A  (punta a se stesso!)
```

La tcache ora ha **un ciclo** nella linked list. Questo è la corruzione.

---

### Come si sfrutta — tcache poisoning passo per passo

```c
void *a = malloc(64);
free(a);         // tcache: [A] → NULL
free(a);         // tcache: [A] → [A] → ciclo

// Ora:
void *x = malloc(64);   // prende A dalla tcache → tcache: [A] → ciclo
                         // x punta ad A

// Scrivi un indirizzo target nel fd di A
// (che ora è sotto il tuo controllo tramite x)
*(long *)x = target_address;

// tcache ora è: [A] → [target_address]

void *y = malloc(64);   // prende A ancora
void *z = malloc(64);   // prende target_address ← ARBITRARY ALLOC!

// z punta a una zona di memoria arbitraria
// puoi scriverci sopra con z
*(long *)z = valore_malevolo;
```

Con `z` puoi scrivere **ovunque in memoria** — hook di funzioni, GOT, stack, ecc.

---

### Protezioni moderne e bypass

|Protezione|Introdotta in|Cosa fa|
|---|---|---|
|tcache double free check|glibc 2.29|controlla se il chunk è già in tcache|
|safe-linking|glibc 2.32|offusca i puntatori `fd` con XOR|
|ASLR|kernel|randomizza gli indirizzi|
|PIE|compilatore|randomizza base dell'eseguibile|

**safe-linking** in particolare rende più difficile il poisoning perché `fd` non è più un indirizzo diretto:

```c
fd = (indirizzo_chunk >> 12) XOR indirizzo_next
```

Ma se hai un **leak di indirizzi** (altra vulnerabilità comune) puoi comunque calcolarlo.

---

## 📚 Lezioni apprese

- Dopo ogni `free()` azzerare sempre il puntatore a `NULL`
- Il double free è alla base di molte tecniche di heap exploitation moderne
- Su glibc ≥ 2.29 ci sono protezioni contro il double free nella tcache, ma esistono bypass
- È una delle vulnerabilità più comuni nel **pwn** dei CTF

---

## 🔗 Riferimenti

- [Azeria Labs - Heap Exploitation](https://azeria-labs.com/heap-exploitation-part-1-understanding-the-glibc-heap-implementation/)
- [How2Heap - shellphish](https://github.com/shellphish/how2heap)
- [GLibc Malloc Internals](https://sourceware.org/glibc/wiki/MallocInternals)

---

## Tags

#double-free #heap #memory-corruption #binary-exploitation #pwn #c #uaf #tcache

