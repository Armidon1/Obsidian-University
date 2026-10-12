---
title: Allocatori di Memoria
aliases:
  - SO — Memory allocators
  - Sistemi Operativi — Lezione 7
tags:
  - sistemi-operativi
  - memoria
  - slab-allocator
  - buddy-allocator
source: lezione7_memory_allocators.docx
---

# Allocatori di Memoria

> [!abstract] Scopo della lezione
> Il kernel non può usare `malloc`: è lui stesso a dover fornire la memoria. Ha quindi bisogno di **allocatori propri**, che gestiscano un buffer di memoria di dimensione data e permettano di **richiedere e rilasciare** pezzi di quel buffer. La lezione presenta i due allocatori più usati nei kernel: lo **SLAB (pool) allocator**, per oggetti **tutti della stessa dimensione** (PCB, nodi di lista…), e il **buddy allocator**, per richieste di **dimensione arbitraria**. Per entrambi si vede un'implementazione completa in C, senza `malloc`. (Negli appunti originali la lezione è *os_06*.)
> Mappa dei concetti: [[MOC - Sistemi Operativi]]

## Il problema

Abbiamo un **buffer di memoria** di dimensione data. Con un allocatore vogliamo che un programma possa **richiedere** un pezzo del buffer e poi **rilasciarlo**. Questi allocatori sono **largamente usati dal kernel** per gestire i piccoli oggetti necessari a implementare le sue strutture dati.

Problemi nella gestione della memoria:

- **Frammentazione** ([[Frammentazione]]): in totale ci sarebbe abbastanza memoria libera per soddisfare una richiesta, ma le allocazioni sparse nel buffer impediscono di trovare un **pezzo contiguo** grande abbastanza.
- **Tempo**: quanto bisogna aspettare per ottenere o rilasciare un blocco? Idealmente O(1).
- **Overhead**: per gestire la memoria ne serve un po' per le **strutture che descrivono il layout** della memoria (chi è libero, chi è occupato).

## SLAB allocator

Vedi [[SLAB Allocator]].

Lo **SLAB allocator** (o **pool allocator**) si usa quando si ha un mucchio di **oggetti di dimensione fissa** (`item_size`) e si sa **quanti** se ne possono avere al massimo. Ad esempio, per gestire la memoria dei nodi di una linked list o dei PCB.

L'allocatore divide la memoria in **blocchi** di dimensione `item_size`:

![[SO-L07-01.png]]

Se la memoria inizia all'indirizzo `buffer_start`, l'indirizzo del blocco *i* è:

$$ptr\_block = buffer\_start + i \cdot item\_size$$

e, dato un indirizzo, si ricava l'indice del blocco:

$$i = \frac{ptr\_block - buffer\_start}{item\_size}$$

Non tutti gli indirizzi sono validi: solo quelli **allineati** ai confini dei blocchi (quelli per cui la divisione non ha resto).

Con lo SLAB **non c'è frammentazione esterna**: i blocchi hanno tutti la stessa dimensione, quindi qualunque blocco libero va bene per qualunque richiesta.

### Allocazione e rilascio in O(1)

Basta tenere una **lista ausiliaria dei blocchi liberi** (*free list*):

- all'inizio la lista contiene **tutti i blocchi**:

  ![[SO-L07-02.png]]

- quando arriva una richiesta, si **restituisce il blocco in testa** e lo si toglie dalla lista:

  ![[SO-L07-03.png]]

- quando un blocco viene rilasciato, lo si **reinserisce in testa** alla lista:

  ![[SO-L07-04.png]]

La lista non resta ordinata, ma non ha importanza: entrambe le operazioni toccano solo la testa, quindi costano **O(1)**.

### La free list senza malloc: array list

Per implementare lo SLAB serve una lista, ma per implementare una lista serve una specie di `malloc`. Come se ne esce?

Si usa una struttura alternativa che funziona su **memoria fissa**: un **array list** ([[Array List]]). Conoscendo la dimensione massima della lista, la si mappa su un **array di `max_size` interi**:

- una variabile `start_pos` (`first_idx`) con l'indice del **primo** elemento;
- un array `int array_list[max_size]`, in cui la cella *i* contiene l'**indice dell'elemento successivo** a *i* (−1 se *i* è l'ultimo o non è nella lista).

Esempio: per rappresentare la lista

![[SO-L07-05.png]]

si usa la struttura

![[SO-L07-06.png]]

L'elemento iniziale è 1; `array[1] = 7`, `array[7] = 2`, `array[2] = 3`, `array[3] = 0`, `array[0] = -1` (fine). Le celle degli elementi non presenti valgono −1. È una linked list in cui i "puntatori" sono **indici** dell'array.

### Implementazione del PoolAllocator

Per gestire uno SLAB servono `N_max * item_size` byte per i blocchi e un array list di `N_max` interi.

**`pool_allocator.h`**:

![[SO-L07-07.png]]

- `PoolAllocatorResult` enumera gli esiti: `Success`, `NotEnoughMemory` (memoria finita), `UnalignedFree` (si restituisce un indirizzo non allineato ai confini dei blocchi), `OutOfRange` (si restituisce un blocco fuori dal buffer), `DoubleFree` (si restituisce due volte lo stesso blocco).
- La struct `PoolAllocator` contiene: `buffer` (il buffer contiguo gestito), `free_list` (l'array list), `buffer_size`, `size` (numero di blocchi liberi), `size_max` (numero massimo di blocchi), `item_size`, `first_idx` (testa della free list, cioè `start_pos`), `bucket_size`.

Le funzioni:

![[SO-L07-08.png]]

un costruttore (`PoolAllocator_init`), una funzione per richiedere un blocco (`getBlock`), una per restituirlo (`releaseBlock`) e una ausiliaria che restituisce una stringa che descrive l'errore (`strerror`).

**`pool_allocator.c`**:

![[SO-L07-09.png]]

Due costanti speciali per la free list: `NullIdx = -1` (fine lista) e `DetachedIdx = -2` (blocco attualmente allocato, cioè staccato dalla lista). `PoolAllocator_strerror` indicizza un array di stringhe con `-result`.

![[SO-L07-10.png]]

`PoolAllocator_init`:

- calcola la dimensione richiesta tenendo conto anche della memoria di gestione: per ogni item servono `item_size` byte **più un `int`** per l'array list: `requested_size = num_items * (item_size + sizeof(int))`. Se il blocco fornito è più piccolo, restituisce `NotEnoughMemory`;
- usa la **prima parte** del buffer come memoria per i blocchi e l'**ultima parte** come `free_list`:

  ![[SO-L07-11.png]]

- popola la free list in modo che ogni elemento punti al successivo (`free_list[i] = i+1`):

  ![[SO-L07-12.png]]

- imposta l'ultimo elemento a `NullIdx` e `first_idx = 0`. Quindi in posizione 0 si legge 1, in posizione 1 si legge 2, e così via. La free list è:

  ![[SO-L07-13.png]]

**`getBlock`**:

![[SO-L07-14.png]]

- se `first_idx == -1` la lista è vuota: restituisce `NULL`;
- stacca il primo elemento (`detached_idx = first_idx`);
- il nuovo `first_idx` è l'indice salvato nella posizione del vecchio (`free_list[first_idx]`);
- decrementa `size` e marca il blocco come `DetachedIdx`;
- restituisce l'indirizzo `buffer + detached_idx * item_size`.

**`releaseBlock`**:

![[SO-L07-15.png]]

- ricava l'indice dall'indirizzo con `offset = block - buffer` e `idx = offset / item_size`;
- **controlli di sicurezza**: se `offset % item_size != 0` → `UnalignedFree`; se l'indice è fuori dal buffer → `OutOfRange`; se il blocco non è marcato `DetachedIdx` (cioè è già nella free list) → `DoubleFree`;
- se è tutto a posto, inserisce il blocco **in testa** alla free list (`free_list[idx] = first_idx; first_idx = idx`) e incrementa `size`.

**`main.c`**:

![[SO-L07-16.png]]

Si definiscono blocchi da 4 KB e 16 elementi; il buffer, che deve contenere anche le informazioni di gestione, è allocato staticamente in `.bss`. Si inizializza l'allocatore e si chiedono **più blocchi di quanti ce ne siano** (`num_items + 10`): le ultime 10 richieste restituiscono `NULL`.

![[SO-L07-17.png]]

Si rilascia tutta la memoria; poi la si rilascia **di nuovo** (si devono ottenere errori `DoubleFree`); poi si alloca metà della memoria e la si rilascia in ordine inverso.

![[SO-L07-18.png]]

Infine si alloca tutta la memoria e si rilasciano prima i blocchi pari e poi i dispari, in ordine inverso: la free list risultante non è ordinata, ma l'allocatore continua a funzionare.

> [!warning] Correzione
> Negli appunti l'implementazione dello slab è chiamata "buddy allocator (che chiamiamo PoolAllocator)": il `PoolAllocator` è lo **SLAB**; il buddy allocator è la seconda parte della lezione.

## Buddy allocator

Vedi [[Buddy Allocator]].

Il **buddy allocator** si usa quando si hanno oggetti di **dimensione arbitraria**. È l'allocatore usato dal kernel Linux per le pagine fisiche.

L'idea è **partizionare ricorsivamente** la memoria **in due metà**, fino a un numero massimo di volte (livelli).

![[SO-L07-19.png]]

Si parte con un blocco da 1 MB. Una richiesta da 90 KB divide 1 MB → 512 + 512 → 256 + 256 → 128 + 128, e assegna un blocco da **128 KB**. Una richiesta da 300 KB riceve un blocco da 512 KB. Quando i 90 KB vengono restituiti, i blocchi liberi vicini si **ricompongono** in un blocco da 512 KB.

Il **buddy** ("compagno") di un blocco è l'**altra metà** ottenuta dividendo il blocco genitore: il suo "fratello".

Allocare un blocco più piccolo della più piccola partizione adatta **spreca memoria**: è **frammentazione interna**. Ad esempio, se si chiedono 90 KB:

![[SO-L07-20.png]]

i 90 KB vengono presi da un blocco da 128 KB (un'ulteriore divisione darebbe blocchi da 64 KB, troppo piccoli), e i restanti 38 KB del blocco vanno sprecati. Il buffer diventa: [90 KB usati | 128 KB | 256 KB | 512 KB].

Quando l'utente restituisce il blocco da 128 KB, l'allocatore si accorge che anche il suo **buddy** è libero, quindi li **unisce** in un blocco da 256 KB; a sua volta il buddy di questo è libero, quindi li unisce in 512 KB, e così via finché non si trova un buddy occupato o si torna alla dimensione iniziale.

### L'albero binario

Dividendo ogni volta in due si crea un **albero binario** sulla memoria: la radice rappresenta tutta la memoria, i figli la prima e la seconda metà, i loro figli le ulteriori partizioni, e così via.

Numerando i nodi per livelli a partire da 1, si ottengono proprietà utili:

![[SO-L07-21.png]]

![[SO-L07-22.png]]

| Grandezza | Formula |
| --- | --- |
| livello del nodo `idx` | `level(idx) = floor(log2(idx))` |
| indice del primo nodo del livello *i* | `firstIdx(i) = 1 << i` (= 2^i) |
| posizione di `idx` all'interno del suo livello | `idx - firstIdx(level(idx))` |
| indice del **buddy** | `buddyIdx(idx) = (idx % 2) ? idx - 1 : idx + 1` (pari → +1, dispari → −1) |
| indice del **genitore** | `parentIdx(idx) = floor(idx / 2)` |
| figli | `2·idx` e `2·idx + 1` |

Implementazione:

![[SO-L07-23.png]]

Quindi **a ogni possibile allocazione corrisponde un indice** nell'albero, e da questo indice si ricavano livello, dimensione, posizione, buddy e genitore **senza memorizzare nient'altro**. La dimensione di un blocco al livello *l* è `mem_size / 2^l` e il suo indirizzo di inizio è `memory + posizione · dimensione`.

### Struttura dati: una free list per livello

Un buddy allocator è una struct `BuddyAllocator` che gestisce un albero di nodi `BuddyListItem`. I nodi sono organizzati nell'albero ma sono anche memorizzati in **liste**: **una lista per ogni livello**, con i blocchi liberi di quel livello. Così si risponde a una richiesta di un blocco di un certo livello in tempo **O(1)** (se la lista non è vuota).

![[SO-L07-24.png]]

![[SO-L07-25.png]]

Le liste sono raccolte in un **array di liste** `free` (con tanti elementi quanti sono i livelli). I `BuddyListItem` stessi vengono allocati con uno **SLAB allocator**: lo SLAB visto prima diventa un mattone del buddy.

**`buddy_allocator.h`**:

![[SO-L07-26.png]]

`BuddyListItem` rappresenta un blocco di memoria:

- `list`: il `ListItem` per inserirlo nella lista del suo livello (ereditarietà alla [[Ereditarietà in C|C]]);
- `idx`: indice nell'albero; `level`: livello;
- `start`: indirizzo di memoria da cui inizia il blocco; `size`: dimensione;
- `buddy_ptr`: puntatore al **fratello**; `parent_ptr`: puntatore al **genitore**.

`level`, `start` e `size` si potrebbero ricavare dall'indice, ma memorizzarli è comodo.

> [!warning] Correzione
> Nelle annotazioni dell'immagine "genitore" e "fratello" sono invertiti: `buddy_ptr` punta al **fratello**, `parent_ptr` al **genitore**.

![[SO-L07-27.png]]

`BuddyAllocator` contiene: `free[MAX_LEVELS]` (array di liste dei blocchi liberi), `occupied[MAX_LEVELS]`, `num_levels`, `list_allocator` (lo SLAB per i `BuddyListItem`), `memory` (la memoria da gestire) e `min_bucket_size` (la dimensione minima di un blocco).

Funzioni:

![[SO-L07-28.png]]

**`buddy_allocator.c`**:

`calcSize` calcola quanta memoria serve all'allocatore per gestire i propri `BuddyListItem`:

![[SO-L07-29.png]]

Il numero massimo di nodi è `1 << (num_levels + 1)`; per ognuno servono `sizeof(BuddyListItem)` byte più un `int` per la free list dello SLAB.

`BuddyAllocator_init` fa da costruttore.

### Allocazione

Quando si alloca un blocco, nei **primi 8 byte** si scrive un'informazione di servizio (il puntatore al `BuddyListItem` del blocco) e all'utente si restituisce un puntatore a `inizio blocco + 8`. Quando l'utente restituisce il puntatore, basta **arretrare di 8 byte** per ritrovare il `BuddyListItem`.

Quando si richiede memoria bisogna:

1. arrotondare `size + 8` alla dimensione della **più piccola partizione** che la contiene;
2. se c'è una partizione libera nella free list di quel livello, restituirla e toglierla dalla lista;
3. altrimenti chiedere una partizione al **livello superiore** e **dividerla in due** (ricorsivamente), riempiendo opportunamente le free list.

![[SO-L07-30.png]]

`BuddyAllocator_malloc`:

- calcola la dimensione totale della memoria: `mem_size = (1 << num_levels) * min_bucket_size` (numero massimo di blocchi al livello più basso × dimensione minima);
- calcola il livello adatto: `level = floor(log2(mem_size / (size + 8)))`, cioè quante volte si può dimezzare la memoria restando ≥ `size + 8`;
- se il livello supera il numero di livelli disponibili, si usa il livello più basso possibile;
- chiede un blocco di quel livello con `BuddyAllocator_getBuddy`;
- scrive nei primi 8 byte del blocco il puntatore al `BuddyListItem` e restituisce `buddy->start + 8`.

Per ritrovare il buddy di un'area quando viene liberata ci sono due opzioni:

- cercare nella lista un item il cui campo `start` coincide con la regione restituita (**lento**);
- **memorizzare l'indirizzo del list item nei primi byte della partizione** (scelta adottata): l'indirizzo restituito all'utente è `inizio_regione + address_size`, e al rilascio basta decrementarlo di `address_size` byte.

### getBuddy

`getBuddy(alloc, level)` cerca nella lista del livello `level` un elemento libero. Se lo trova lo restituisce; altrimenti lo chiede **ricorsivamente** al livello superiore. Se lo ottiene, quell'elemento (già staccato dalla lista superiore) viene diviso: si creano **due figli** al livello richiesto, li si inserisce nella lista, e si restituisce il primo.

Esempio: richiesta di un blocco a livello 2 quando 4 e 5 sono occupati.

![[SO-L07-31.png]]

La lista del livello 2 è vuota; al livello 1 c'è il blocco 3. Lo si toglie dal livello 1 e lo si divide in 6 e 7, che vanno nella lista del livello 2. Viene restituito il primo (6); nella lista resta 7.

![[SO-L07-32.png]]

- Se `level < 0` non c'è niente da fare: si restituisce `NULL`.
- Se la lista del livello è vuota: si chiama ricorsivamente `getBuddy(alloc, level-1)` per ottenere il genitore; si calcolano gli indici dei figli (`left_idx = parent_idx << 1`, `right_idx = left_idx + 1`); si creano i due `BuddyListItem` con lo SLAB (`createListItem`, che li inserisce anche nella free list del livello) e li si collega come buddy l'uno dell'altro.
- Se ora la lista non è vuota, si estrae il primo elemento con `List_popFront` e lo si restituisce.

Esempio con ricorsione su più livelli: richiesta a livello 3 quando 8, 9, 10, 11 sono occupati.

![[SO-L07-33.png]]

Il livello 3 è vuoto → si chiede al livello 2, anch'esso vuoto → si chiede al livello 1, che restituisce 3 (e lo toglie dalla lista). 3 viene diviso in 6 e 7 (livello 2); poi 6 viene diviso in 12 e 13 (livello 3) e si restituisce 12.

### Rilascio

Quando si rilascia memoria bisogna:

1. identificare la regione associata al blocco rilasciato;
2. se il **buddy** della regione **non** è nella free list del livello, aggiungere il blocco alla lista e terminare;
3. se il buddy **è** libero, **unire** i due blocchi (togliendoli dalla free list) e inserire una nuova entry al **livello superiore**, corrispondente al blocco fuso; ripetere ricorsivamente.

![[SO-L07-34.png]]

`BuddyAllocator_free`: arretra di 8 byte dal puntatore ricevuto, legge il puntatore al `BuddyListItem`, controlla con `assert` che `buddy->start` coincida, e chiama `releaseBuddy`.

![[SO-L07-35.png]]

`releaseBuddy` fa l'**auto-merge**:

- rimette l'item nella free list del suo livello (`List_pushFront`);
- se è la radice (nessun genitore), termina;
- se il fratello **non** è libero (non è in nessuna lista: `prev == 0 && next == 0`), termina;
- altrimenti distrugge entrambi gli item (rimuovendoli dalla free list e restituendoli allo SLAB con `destroyListItem`) e chiama **ricorsivamente** `releaseBuddy` sul **genitore**, che continua a unire fratelli finché uno dei due è occupato o si arriva alla radice.

Le funzioni `BuddyAllocator_createListItem` e `BuddyAllocator_destroyListItem` sono da implementare in `buddy_allocator.c`.

Il buddy allocator riesce a gestire un certo livello di frammentazione (grazie al merge dei blocchi), e il **costo massimo** delle operazioni è **O(levels)**.

**`main.c`**:

![[SO-L07-36.png]]

Si usano 9 livelli su 1 MB di memoria, quindi il blocco minimo è 1 MB / 2⁹ = 2 KB; un buffer statico da 100 KB ospita le strutture di gestione. Si verifica con `calcSize` che il buffer basti, si inizializza l'allocatore, si allocano due blocchi da 100 byte e uno da 100000 byte, e poi li si libera (osservando i merge).

### Problemi del buddy allocator e soluzioni

Problemi:

- si spreca **molto spazio** per memorizzare l'albero (un `BuddyListItem` per nodo);
- la **ricorsione** va bene per i compilatori ma andrebbe **evitata dentro un OS** (lo stack del kernel è piccolo e la profondità va controllata).

Soluzioni usate nella pratica:

- l'albero viene memorizzato in una **bitmap** (1 bit per nodo: libero/occupato);
- **nessuna free list**: i blocchi liberi si trovano con controlli bit a bit "brutali" sulla bitmap;
- le macchine moderne fanno questi controlli **64 bit alla volta** (un'istruzione su una parola intera);
- l'approccio è **asintoticamente peggiore**, ma **più veloce nella pratica** (meno memoria, migliore uso della cache, nessuna ricorsione).

> [!tip] Collegamenti
> - Lo SLAB viene usato in [[08 - SO - disastrOS|disastrOS]] per allocare PCB e strutture del kernel senza `malloc`.
> - Il problema della frammentazione tornerà nella gestione della memoria fisica: [[Allocazione Contigua]], [[Paging]] ([[10 - SO - Gestione della Memoria|lezione 10]]).
