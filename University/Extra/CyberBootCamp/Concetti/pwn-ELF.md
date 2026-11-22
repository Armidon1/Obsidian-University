---
title: pwn-ELF
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF
---

# ELF

> [!abstract] In breve
> `ELF` è la classe di pwntools per ispezionare eseguibili e librerie ELF. Una volta aperto il file puoi leggerne intestazione, sezioni, segmenti, simboli, dipendenze dichiarate e protezioni rilevate.

## Aprire e chiudere il file

`ELF(percorso, checksec=True)` apre il file e mostra un riepilogo delle protezioni. Con `checksec=False` disattivi il riepilogo automatico. Si può richiamare `binario.checksec()` in seguito.

Usa `with ELF(...) as binario` per chiudere il file all'uscita dal blocco oppure chiama `binario.close()` quando hai finito. Negli esempi e nelle tabelle qui sotto, `binario` è l'oggetto restituito da `ELF(...)`.

## Intestazione e identificazione

| Come si usa | Che cosa ottieni |
|---|---|
| `binario.path` | Percorso del file aperto. |
| `binario.arch` | Architettura nel formato usato da pwntools, per esempio `amd64`. |
| `binario.bits`, `binario.bytes` | Larghezza dei puntatori in bit e in byte. |
| `binario.endian` | Ordine dei byte, `little` o `big`. |
| `binario.header` | Intestazione ELF. Per esempio, `binario.header.e_type` contiene il tipo di file. |
| `binario.elftype` | Tipo di file in forma compatta, per esempio `EXEC` o `DYN`. |
| `binario.entry`, `binario.entrypoint`, `binario.start` | Tre nomi per l'indirizzo del punto di ingresso. |
| `binario.buildid` | Build ID GNU come `bytes`, oppure `None` se assente. Puoi mostrarlo con `.hex()` quando è presente. |
| `binario.stripped`, `binario.debuginfo` | Indicatori sull'assenza della tabella ordinaria dei simboli e sulla presenza di `.debug_info`. |
| `binario.dwarf` | Oggetto per consultare le informazioni di debug DWARF. |
| `binario.iter_notes()`, `binario.iter_properties()` | Iterano sulle note ELF e sulle proprietà GNU. |

Impostare `context.binary = binario` configura il contesto di pwntools in base alle proprietà dell'ELF.

## Simboli e funzioni

| Come si usa | Che cosa ottieni |
|---|---|
| `binario.symbols`, `binario.sym` | `dotdict` con chiavi `str` e indirizzi di tipo `int`. `binario.symbols.get(nome)` dà l'indirizzo oppure `None`. |
| `binario.functions` | Mappa da nome a oggetto `Function`. Per esempio, `binario.functions[nome].size` dà la dimensione della funzione registrata. |
| `binario.got`, `binario.plt` | Mappe delle voci GOT e PLT utili per ispezionare il collegamento dinamico. |

I dati disponibili dipendono dal file. Un eseguibile *stripped* può conservare parte dei simboli dinamici. Vedi [[pwn-symbols|symbols]] e [[GOT e PLT]].

## Sezioni e segmenti

Una **sezione** raggruppa dati con uno scopo, come istruzioni, stringhe o simboli. Un **segmento** descrive una regione usata dal loader e le sue proprietà, come i permessi di accesso. Vedi [[Sezioni e Segmenti ELF]].

| Come si usa | Che cosa ottieni |
|---|---|
| `binario.sections`, `binario.iter_sections()` | Elenco o iteratore delle sezioni. Ogni sezione espone `.name`, `.header` e `.data()`. |
| `binario.segments`, `binario.iter_segments()` | Elenco o iteratore dei segmenti. Ogni segmento espone `.header` e `.data()`. |
| `binario.num_sections()`, `binario.num_segments()` | Conteggio di sezioni e segmenti. |
| `binario.get_section(indice)`, `binario.get_segment(indice)` | Sezione o segmento identificato dall'indice. |
| `binario.get_section_by_name(".text")` | Oggetto della sezione richiesta. Restituisce `None` se è assente. |
| `binario.get_section_index(nome)` | Indice della sezione con quel nome, oppure `None`. |
| `binario.section(".text")` | Byte della sezione indicata. Se il nome potrebbe mancare, cerca prima la sezione con `get_section_by_name`. |
| `binario.iter_segments_by_type("PT_LOAD")` | Segmenti del tipo richiesto. I segmenti `PT_LOAD` contengono le regioni caricabili. |
| `binario.executable_segments`, `binario.writable_segments`, `binario.non_writable_segments` | Sottoinsiemi dei segmenti selezionati in base ai permessi. |
| `binario.rwx_segments` | Segmenti scrivibili ed eseguibili secondo la valutazione di pwntools, che tiene conto di NX. |
| `binario.get_segment_for_address(indirizzo, size=1)` | Segmento associato all'intervallo di byte nel file, oppure `None`. |
| `binario.bss()` | Indirizzo della sezione `.bss`, se presente. |

## Leggere il contenuto

Un **offset nel file** conta i byte dall'inizio del file su disco. Un **indirizzo virtuale** identifica una posizione nello spazio di indirizzi descritto dall'ELF. Le funzioni di lettura della tabella usano indirizzi virtuali quando il parametro è `indirizzo`.

| Come si usa | Che cosa ottieni |
|---|---|
| `binario.address` | Indirizzo del segmento con la base più bassa nel modello dell'oggetto ELF. |
| `binario.offset_to_vaddr(offset)`, `binario.vaddr_to_offset(indirizzo)` | Conversione tra offset e indirizzo virtuale. Il risultato è `None` se non esiste una corrispondenza. |
| `binario.read(indirizzo, numero_byte)` | I byte a partire dall'indirizzo indicato nell'immagine ELF. |
| `binario.data`, `binario.get_data()` | Tutti i byte del file rappresentato dall'oggetto. |
| `binario.string(indirizzo)` | Byte di una stringa terminata da NUL all'indirizzo indicato. |
| `binario.u8(indirizzo)`, `binario.u16(indirizzo)`, `binario.u32(indirizzo)`, `binario.u64(indirizzo)` | Un intero decodificato dai byte a quell'indirizzo. |
| `binario.unpack(indirizzo)` | Un intero letto alla larghezza della parola dell'ELF. |
| `binario.search(sequenza_di_byte)` | Iteratore degli indirizzi virtuali in cui compare una sequenza, per esempio una stringa di versione nota. |
| `binario.disasm(indirizzo, numero_byte)` | Rappresentazione testuale delle istruzioni lette dall'ELF. |

`binario.u32(indirizzo)` legge da un oggetto ELF. La funzione autonoma [[pwn-u32|u32]] riceve un oggetto `bytes`, per esempio il risultato di una lettura da file.

## Collegamento dinamico e protezioni

| Come si usa | Che cosa ottieni |
|---|---|
| `binario.linker` | Percorso dell'interprete ELF dichiarato dal file, quando presente. |
| `binario.statically_linked` | Indicatore di collegamento statico. |
| `binario.dynamic_by_tag("DT_NEEDED")` | Prima voce dinamica con quel tag, oppure `None`. Per tutte le dipendenze dichiarate, scorri i tag della sezione `.dynamic`. |
| `binario.dynamic_value_by_tag(tag)` | Valore numerico della voce dinamica cercata, oppure `None` se manca. |
| `binario.dynamic_string(offset)` | Stringa nella tabella dinamica a partire dal suo offset. |
| `binario.rpath`, `binario.runpath` | Percorsi di ricerca codificati nei tag `DT_RPATH` e `DT_RUNPATH`, se presenti. |
| `binario.checksec()` | Riepilogo delle protezioni rilevate. Lo puoi stampare con `print(binario.checksec())`. |
| `binario.nx`, `binario.execstack` | Indicatori relativi alla memoria non eseguibile e alla richiesta di uno stack eseguibile. |
| `binario.pie`, `binario.canary`, `binario.relro` | Proprietà relative a PIE, stack canary e RELRO. |
| `binario.fortify`, `binario.asan`, `binario.msan`, `binario.ubsan` | Indicatori di fortificazione e strumentazione tramite sanitizer. |
| `binario.ibt`, `binario.shadowstack` | Proprietà GNU relative a Indirect Branch Tracking e shadow stack. |

> [!important] Lettura del file ed esecuzione
> `binario.process()` avvia il programma e `binario.debug()` lo avvia sotto GDB. Anche gli attributi `libs`, `libc` e `maps` possono eseguire il binario per determinare le librerie o le mappature effettive. Per ispezionare un ELF sconosciuto, usa le informazioni dichiarate nel file, come `linker` e i tag dinamici.

## Creare o esportare un ELF

| Come si usa | Che cosa fa |
|---|---|
| `ELF.from_bytes(dati, arch=...)` | Crea un oggetto ELF incapsulando byte di codice macchina. |
| `ELF.from_assembly(istruzioni, arch=...)` | Assembla le istruzioni e le incapsula in un oggetto ELF. |
| `binario.write(indirizzo, dati)` | Sostituisce byte nell'immagine aperta. È adatto a modifiche puntuali su un proprio file di prova. |
| `binario.save(percorso_copia)` | Esporta l'immagine ELF, comprese eventuali modifiche. Indica un nuovo percorso per conservare l'originale. |

## Esempio di ispezione statica

```python
from pwn import ELF

with ELF("/bin/ls", checksec=False) as binario:
    print(binario.arch, binario.bits, binario.endian)
    print(f"Sezioni: {binario.num_sections()}")
    print(f"Segmenti: {binario.num_segments()}")

    testo = binario.get_section_by_name(".text")
    if testo is not None:
        print(f".text: {testo.header.sh_size} byte")

    for segmento in binario.iter_segments_by_type("PT_LOAD"):
        print(f"PT_LOAD a offset {segmento.header.p_offset:#x}")

    assert binario.get_data()[:4] == b"\x7fELF"
    print(binario.checksec(banner=False, color=False))
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-symbols|symbols]] per consultare i simboli del file
- [[pwn-checksec|checksec]] · [[pwn-process|process]]
- [Documentazione ufficiale di ELF](https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF)
