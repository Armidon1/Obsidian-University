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
| Un prompt riconoscibile | `io.recvuntil(b"> ")` | Consuma i dati fino al delimitatore incluso. Con `drop=True` lo omette dal risultato. |
| Un campo binario da inviare | `io.send(dati)` | Scrive i byte forniti. |
| Una risposta da confermare con Invio | `io.sendline(dati)` | Scrive i byte e aggiunge il fine riga configurato. |

> [!tip] Quando una lettura sembra bloccata
> Con `io.recvuntil(b"> ", timeout=2)`, un risultato `b""` indica che il delimitatore non è arrivato entro due secondi. I byte già raccolti restano nel buffer. Se il canale si chiude prima del delimitatore, la chiamata solleva `EOFError`. Controlla spazi e fine riga con `repr(dati)` quando ispezioni una risposta. [Riferimento di recvuntil](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvuntil)

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

## Ripasso

- **Il programma scrive un prompt senza andare a capo. Come lo riconosci?** Con `recvuntil`, usando i byte che segnano la fine del prompt.
- **Devi leggere un intero binario a 32 bit. Quali decisioni prendi?** Leggi quattro byte con `recvn(4)` e li interpreti con `u32` nell'ordine stabilito dal formato.
- **Un messaggio contiene spazi finali significativi. Come li conservi?** Se il delimitatore è `b"\n"`, usa `recvuntil(b"\n", drop=True)`. Un generico `.strip()` eliminerebbe anche gli spazi.

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[Shellcode]] · [[ROP]]
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
