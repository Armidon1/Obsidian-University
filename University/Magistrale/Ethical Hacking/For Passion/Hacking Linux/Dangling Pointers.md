## tags: [ethical-hacking, hacking-exposed-7, ch5, memory-corruption, data-driven, use-after-free, exam-prep] chapter: 5 exam: ETH-2026-06-05 related: [[data_driven_attacks]], [[integer_overflow_attacks]], [[format_string_attacks]]

# Dangling Pointers & Use-After-Free

> [!abstract] TL;DR Un **dangling pointer** è un puntatore che punta a memoria non più valida (liberata o uscita di scope). Il puntatore è solo un numero: `free()` libera la memoria ma **non azzera la variabile**. Se la memoria viene riallocata con dati controllati dall'attaccante e poi il puntatore viene usato, → **use-after-free (UAF)** → code execution. Famiglia: [[data_driven_attacks]], ma con dimensione **temporale**.

---

## 1. Il problema di fondo: `free()` non azzera niente

Un puntatore è un `void*` — un intero che contiene un indirizzo. La sequenza standard:

```
PRIMA del free:
cp ──────────────────→ [ "hello", chunk allocato a te ]

DOPO free(cp):
cp ──────────────────→ [ chunk restituito all'allocatore ]
                         ma cp contiene ancora lo stesso indirizzo
```

`free` aggiorna lo stato interno dell'allocatore (`malloc_chunk` metadata, free list, tcache) ma **non tocca la variabile `cp`** del chiamante. Il C non ha modo di farlo: non sa quali variabili contengono quell'indirizzo.

> [!tip] Analogia Linux Come avere un file descriptor di un file `unlink`ato e poi chiamare `write(fd, ...)`. Il kernel ha riassegnato quell'fd al prossimo `open()`. Tu scrivi pensando sia il tuo file, ma scrivi nel file di qualcun altro. Stesso pattern: la risorsa è stata rilasciata e riassegnata, ma tu hai ancora il "manico" vecchio.

---

## 2. Caso 1: Use-After-Free (il pericoloso)

### 2.1 Meccanica base

```c
char *cp = malloc(64);
strcpy(cp, "dato sensibile");
free(cp);
// cp è ora dangling

// Più tardi, magari in un altro path del codice:
process(cp);   // legge la memoria che non gli appartiene più
```

Se nel frattempo nessuno ha riallocato quella zona, leggi ancora "dato sensibile" (apparentemente funziona — bug invisibile). Se è stata riallocata, leggi roba di un altro contesto.

### 2.2 Lo sfruttamento (heap massaging)

L'attaccante deve:

```
t0: triggerare allocazione dell'oggetto vulnerabile (size N)
t1: triggerare la free di quell'oggetto
t2: triggerare una allocazione di size N con dati controllati
    → l'allocatore riassegna LA STESSA zona (LIFO sui chunk same-size)
t3: triggerare l'uso del puntatore dangling
    → il codice vittima legge/usa dati attaccante
```

L'allocatore glibc (tcache, fastbins) **preferisce** restituire chunk appena liberati per cache locality — il che gioca a favore dell'attaccante.

### 2.3 Perché diventa code execution

Il puntatore dangling spesso punta a un **oggetto C++** che contiene:

- una **vtable pointer** (primo campo dell'oggetto)
- function pointer
- callback

```c++
class Widget {
    virtual void render();   // → vtable pointer all'offset 0
};

Widget *w = new Widget();
delete w;                    // w è dangling
// attacker spray: malloc(sizeof(Widget)) con dati controllati
//                 il primo qword punta a vtable fake controllata
w->render();                 // chiama puntatore controllato → ROP
```

---

## 3. Caso 2: Stack pointer escape

```c
char *exampleFunction2(void) {
    char string[] = "Dangling Pointer";   // sullo stack
    return string;                          // ritorna ptr a stack frame morto
}
```

```
Stack DURANTE la funzione:
┌─────────────────────┐
│ "Dangling Pointer"  │ ← string[]
│ saved EBP           │
│ return address      │
└─────────────────────┘
         ↓ funzione ritorna, ESP risale
┌─────────────────────┐
│ prossima funzione   │ ← stessa zona, contenuto sovrascritto
│ usa questo spazio   │
└─────────────────────┘
       ↑
   il caller tiene ancora il puntatore qui
```

**Meno sfruttabile** del caso 1 perché lo stack viene riscritto da ogni chiamata successiva, meno controllabile rispetto all'heap. Però:

- Crash deterministici
- Information leak (se la zona contiene segreti di una funzione successiva)
- A volte exploit se si controlla cosa va sullo stack subito dopo

---

## 4. Il pattern universale, con dimensione temporale

Tutti i memory corruption bug seguono [[data_driven_attacks]], ma UAF aggiunge il **tempo**:

```
allocazione          →    free          →    spray         →    use
   t0                      t1                  t2                 t3
[oggetto valido]      [dangling]         [zona occupata    [accesso a dati
                                          da attaccante]    attaccante]
```

Il bug (free a t1) e il sintomo (a t3) sono **separati nel tempo e nel codice**. Per questo HE7 dice "symptoms are often seen long after... identifying the root cause can be difficult": il debugger ti mostra il crash a t3 in una funzione che sembra OK, mentre il vero bug è il `free` mancante o in eccesso a t1.

> [!warning] Riconoscerlo in code review Indicatori sospetti:
> 
> 1. `free(ptr)` senza `ptr = NULL` subito dopo
> 2. Strutture dati con puntatori a oggetti che possono essere liberati altrove (callback, observer pattern)
> 3. Funzioni che ritornano puntatori a variabili locali (caso 2)
> 4. Doppi free (`free(ptr); ... free(ptr);`) — variante chiamata **double-free**
> 5. Cleanup paths in error handling: spesso si libera due volte o si dimentica di mettere NULL

---

## 5. Casi reali famosi

|CVE / nome|Target|Note|
|---|---|---|
|**MS IIS dangling ptr (BlackHat 2007)**|Microsoft IIS|Watchfire — prima dimostrazione pratica che dangling pointer "teorici" erano exploitabili. Fece nascere UAF come **classe** di vulnerabilità riconosciuta|
|**CVE-2014-1776**|Internet Explorer|UAF in `CMarkup`, exploited in-the-wild prima della patch|
|**CVE-2019-5786**|Chrome FileReader|UAF zero-day, combinato con Windows LPE|
|**Pwn2Own (vari)**|Browser, kernel|UAF è oggi **la** classe di bug dominante per i browser exploit|

> [!note] Perché i browser sono pieni di UAF Modello a oggetti DOM enorme, JavaScript che può triggerare allocazioni/free arbitrarie, codice C++ con vtable ovunque, lifetime management complesso tra DOM, JS engine, layout. La combinazione perfetta. Vedi [[browser_attack]].

---

## 6. Contromisure

### Lato codice

|Tecnica|Come funziona|Limite|
|---|---|---|
|`ptr = NULL` dopo `free`|Dereferenziare NULL crasha subito e in modo deterministo|Non aiuta se ci sono **altre** copie del puntatore|
|**Smart pointer** (C++)|`unique_ptr` (ownership unica), `shared_ptr` (ref counting), `weak_ptr` (non-owning)|Richiede disciplina; raw pointer ancora possibili|
|Static / `malloc` (caso 2)|Sopravvive al ritorno della funzione|Static = problemi di concorrenza; malloc richiede free corretto|
|**RAII** (C++)|Distruttori automatici al fine scope|Solo C++|

### Lato compiler/runtime

|Tecnica|Come funziona|
|---|---|
|**AddressSanitizer** (`-fsanitize=address`)|Marca memoria liberata come poisoned, crasha al primo accesso. Fondamentale per fuzzing|
|**MemorySanitizer**|Rileva uninitialized read|
|**Memory Tagging Extension (ARM MTE)**|Tag a livello hardware: ogni allocazione ha un tag, accesso con tag sbagliato crasha|
|**Heap isolation by type**|Oggetti dello stesso tipo allocati in pool separati — l'attaccante non può ri-occupare una zona Widget con dati arbitrari|
|**Garbage collected runtime** (JVM, Go, Python)|Il problema scompare per costruzione: la memoria non viene liberata finché ci sono referenze|
|**Rust borrow checker**|Impedisce a compile-time di tenere un riferimento a memoria liberata|

### Cosa NON aiuta direttamente

- **ASLR**: l'attaccante non deve indovinare indirizzi assoluti, sfrutta layout heap relativo
- **DEP/NX**: blocca l'esecuzione di dati, ma l'UAF tipicamente porta a vtable hijack → ROP, che bypassa NX
- **Stack canary**: protegge return address sullo stack, non l'heap

> [!tip] Punto sottile per l'esame Le mitigazioni "classiche" (ASLR/DEP/canary) **non risolvono UAF**. Per questo UAF è la classe dominante negli exploit moderni: le difese tradizionali sono inefficaci, servono difese specifiche (sanitizer, MTE, type isolation, garbage collection, linguaggi memory-safe).

---

## 7. Confronto con le altre memory corruption (per fissare la mappa)

|Bug class|Quando agisce|Cosa corrompe|Difficoltà exploit moderno|
|---|---|---|---|
|Stack buffer overflow|Subito (durante la copia)|Stack (ret address, canary)|Media (canary, ASLR aiutano molto)|
|Heap buffer overflow|Subito|Heap (adjacent chunk, metadata)|Alta (heap hardening)|
|[[integer_overflow_attacks]]|Subito (genera uno dei due sopra)|Stesso dei due sopra|= a quelli sopra|
|[[format_string_attacks]]|Subito|Arbitrario (read+write primitive)|Bassa se non patchato (molto potente)|
|**Use-after-free**|**Differita nel tempo**|Vtable, function pointer, oggetti|**Bassa-Media** (ASLR/canary non aiutano)|
|Double-free|Differita|Metadata allocatore|Media|

---

## 8. Takeaways

- **Dangling pointer** = puntatore a memoria non più valida (liberata o fuori scope). Il bug è il puntatore stale, non l'azione di liberare.
- **`free()` libera la memoria ma non azzera la variabile**. Sta al programmatore.
- **Use-after-free** è il caso 1 e quello veramente pericoloso: con heap massaging diventa code execution affidabile.
- **Stack pointer escape** è il caso 2: meno sfruttabile ma causa bug reali.
- **Pattern**: alloca → free → spray → use. La separazione temporale tra bug e sintomo rende il debugging difficile.
- **Le difese classiche (ASLR/DEP/canary) non risolvono UAF**. Servono sanitizer, smart pointer, type isolation, o linguaggi memory-safe.
- **Browser e parser complessi** sono il regno dell'UAF nel mondo reale.
- **Riconoscimento codice**: `free` senza `= NULL`, funzioni che ritornano `&local_var`, cleanup paths complicati, doppia gestione di lifetime tra strutture.

---

## Wiki-links

- [[data_driven_attacks]] — famiglia generale
- [[integer_overflow_attacks]] — altro bug Ch.5 che spesso porta a heap corruption
- [[format_string_attacks]] — confronto come bug class
- [[browser_attack]] — perché i browser sono il regno dell'UAF
- [[heap_exploitation]] — per assignment opzionale (tcache, fastbin) post-esame