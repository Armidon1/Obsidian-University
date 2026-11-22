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

ELF è il formato di molti eseguibili e librerie Linux. `ELF(percorso)` apre il file per ispezionarlo. L'oggetto espone `.arch` per l'architettura, `.bits` per la larghezza e `.endian` per l'ordine dei byte. `.symbols` associa i nomi disponibili ai loro valori nel file. Un eseguibile privato dei simboli di debug e della tabella dei simboli ordinaria può conservare alcuni simboli dinamici.

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

## Ripasso

- **Il programma scrive un prompt senza andare a capo. Come lo riconosci?** Con `recvuntil`, usando i byte che segnano la fine del prompt.
- **Devi leggere un intero binario a 32 bit. Quali decisioni prendi?** Leggi quattro byte con `recvn(4)` e li interpreti con `u32` nell'ordine stabilito dal formato.
- **Un messaggio contiene spazi finali significativi. Come li conservi?** Se il delimitatore è `b"\n"`, usa `recvuntil(b"\n", drop=True)`. Un generico `.strip()` eliminerebbe anche gli spazi.

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[Shellcode]] · [[ROP]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#pwntools: lo strumento di lavoro|Lezione 4 — pwntools: lo strumento di lavoro]]

## Indice dei metodi e delle funzioni

| Metodo o funzione | Cosa fa | Come si usa |
|---|---|---|
| [[pwn-asm\|asm]] | Assembla istruzioni in byte di codice macchina. | `asm(istruzioni, arch=...)` |
| [[pwn-checksec\|checksec]] | Riassume le protezioni del binario. | `binario.checksec()` su un oggetto creato con `ELF(percorso)` |
| [[pwn-close\|close]] | Chiude il canale e libera le risorse associate. | `io.close()` su un tube da `process(...)` o `remote(...)` |
| [[pwn-disasm\|disasm]] | Traduce il codice macchina in istruzioni leggibili. | `disasm(dati, arch=...)` |
| [[pwn-ELF\|ELF]] | Apre un file ELF e ne legge architettura, simboli e proprietà. | `binario = ELF(percorso)` |
| [[pwn-flat\|flat]] | Combina byte e interi in un unico blocco binario. | `flat(*campi, word_size=...)` |
| [[pwn-hexdump\|hexdump]] | Mostra i byte in esadecimale con i rispettivi offset. | `hexdump(dati)` |
| [[pwn-interactive\|interactive]] | Collega il canale al terminale per interagire a mano. | `io.interactive()` su un tube da `process(...)` o `remote(...)` |
| [[pwn-p8\|p8]] | Codifica un intero a 8 bit in 1 byte. | `p8(valore)` |
| [[pwn-p16\|p16]] | Codifica un intero a 16 bit in 2 byte. | `p16(valore)` |
| [[pwn-p32\|p32]] | Codifica un intero a 32 bit in 4 byte. | `p32(valore)` |
| [[pwn-p64\|p64]] | Codifica un intero a 64 bit in 8 byte. | `p64(valore)` |
| [[pwn-pack\|pack]] | Codifica un intero con una larghezza a scelta. | `pack(valore, word_size)` |
| [[pwn-process\|process]] | Avvia un programma locale e restituisce un canale di I/O. | `io = process([eseguibile, ...])` |
| [[pwn-recv\|recv]] | Legge fino a `n` byte appena ci sono dati. | `io.recv(n)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-recvall\|recvall]] | Raccoglie i dati fino a fine flusso e chiude il canale. | `io.recvall()` su un tube da `process(...)` o `remote(...)` |
| [[pwn-recvline\|recvline]] | Legge una riga fino al fine riga configurato. | `io.recvline()` su un tube da `process(...)` o `remote(...)` |
| [[pwn-recvn\|recvn]] | Aspetta di ricevere esattamente `n` byte. | `io.recvn(n)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-recvuntil\|recvuntil]] | Legge fino al delimitatore indicato. | `io.recvuntil(delimitatore)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-remote\|remote]] | Apre una connessione di rete e restituisce un canale di I/O. | `io = remote(host, porta)` |
| [[pwn-send\|send]] | Invia i byte forniti. | `io.send(dati)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-sendafter\|sendafter]] | Legge fino al delimitatore e poi invia i byte. | `io.sendafter(delimitatore, dati)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-sendline\|sendline]] | Invia i byte e aggiunge il fine riga. | `io.sendline(dati)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-sendlineafter\|sendlineafter]] | Legge fino al delimitatore e poi invia una riga. | `io.sendlineafter(delimitatore, dati)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-settimeout\|settimeout]] | Imposta il tempo d'attesa predefinito per le letture. | `io.settimeout(secondi)` su un tube da `process(...)` o `remote(...)` |
| [[pwn-u8\|u8]] | Legge 1 byte come intero a 8 bit. | `u8(dati)` |
| [[pwn-u16\|u16]] | Legge 2 byte come intero a 16 bit. | `u16(dati)` |
| [[pwn-u32\|u32]] | Legge 4 byte come intero a 32 bit. | `u32(dati)` |
| [[pwn-u64\|u64]] | Legge 8 byte come intero a 64 bit. | `u64(dati)` |
| [[pwn-unpack\|unpack]] | Decodifica i byte come intero della larghezza specificata. | `unpack(dati, word_size)` |
