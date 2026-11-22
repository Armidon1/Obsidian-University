---
title: pwn-ROP
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/rop.html
---

# ROP

> [!abstract] In breve
> `ROP` è una classe di pwntools, definita nel modulo `pwnlib.rop`, che rappresenta gadget e catene di istruzioni riutilizzate dal codice macchina di uno o più file ELF.

## Che cosa rappresenta ogni oggetto

| Voce | Tipo in Python | Che cosa descrive |
|---|---|---|
| Binario aperto da pwntools | `ELF` | Un file da ispezionare per leggere sezioni, segmenti e simboli. |
| `binario.symbols` | `dotdict` con chiavi `str` e valori `int` | Nome e indirizzo dei simboli disponibili nell'ELF. |
| Oggetto della classe ROP | `ROP` | La rappresentazione di una catena associata agli ELF che contengono il codice. |
| Gadget | `Gadget` | Una breve sequenza di istruzioni già presente nel codice macchina, spesso terminata da `ret`. Può trovarsi dentro una funzione. |
| Indirizzo e istruzioni del gadget | `.address` è un `int`. `.insns` è una `list[str]`. `.regs` è un `dict` (o `OrderedDict`). | L'indirizzo indica l'inizio della sequenza. Le stringhe descrivono le istruzioni disassemblate. `.regs` mappa il nome del registro riempito all'offset nel frame (o al registro da cui viene copiato). |
| `rop.gadgets` | `dict[int, Gadget]` | Tutti i gadget che pwntools ha riconosciuto nel binario, indicizzati per indirizzo. |

Un **simbolo** dà un nome a un indirizzo. Un **gadget** descrive il codice che inizia a un indirizzo. Un gadget interno a una funzione può quindi comparire in un rapporto di analisi anche quando manca una voce corrispondente in `binario.symbols`.

> [!note] Indirizzo, testo e byte
> `int` è il tipo dell'indirizzo. Una scritta esadecimale come `0x1000` in un rapporto è il modo in cui quel valore viene visualizzato. Le stringhe in `.insns` descrivono il disassemblato. Il codice macchina corrispondente è una sequenza di byte.

## Dal ritorno di una funzione alla catena

Su x86-64, durante una normale chiamata `call` salva l'indirizzo dell'istruzione successiva. Al termine della funzione, `ret` riprende l'esecuzione da quell'indirizzo. Una catena ROP riutilizza questo meccanismo per far eseguire in sequenza frammenti di codice esistenti. I frammenti possono leggere o modificare registri e memoria, quindi una descrizione della catena riguarda anche gli effetti sullo stato del programma. Vedi [[call e ret]] e [[Calling Convention]].

## Come leggere le mitigazioni di un ELF

| Proprietà | Tipo | Che cosa indica |
|---|---|---|
| `binario.nx` | `bool` | Supporto alla separazione tra memoria eseguibile e regioni dati, come lo stack. Vedi [[NX]]. |
| `binario.pie` | `bool` | L'eseguibile può essere caricato a basi diverse. La base effettiva dipende dalle impostazioni del sistema durante l'esecuzione. Vedi [[PIE]]. |
| `binario.canary` | `bool` | Pwntools rileva l'uso dello stack canary, un valore che può segnalare alcune sovrascritture dello stack. Vedi [[Canary dello Stack]]. |
| `binario.shadowstack` | `bool` | L'ELF dichiara la proprietà SHSTK. Quando è attiva, il processore conserva una seconda copia protetta degli indirizzi di ritorno e la confronta al momento del ritorno. |
| `binario.ibt` | `bool` | L'ELF dichiara Indirect Branch Tracking. Quando è attivo, controlla le destinazioni delle chiamate e dei salti indiretti. |

Shadow Stack e IBT appartengono a CET (*Control-flow Enforcement Technology*). Le proprietà lette nel file descrivono la build. L'attivazione durante l'esecuzione dipende anche da processore, sistema operativo e loader. [Documentazione del kernel Linux su CET](https://docs.kernel.org/arch/x86/shstk.html)

## Elencare tutti i gadget trovati

`find_gadget([...])` cerca un gadget che corrisponda esattamente alla sequenza di istruzioni richiesta (es. `["pop rsi", "ret"]`). Se nel binario non esiste **esattamente** quella sequenza, restituisce `None` invece di una lista: `rop.find_gadget([...])[0]` darebbe allora `TypeError: 'NoneType' object is not subscriptable`. Non tutti i binari hanno gadget "comodi" per ogni registro: dipende da cosa ha generato il compilatore (a volte serve un gadget che riempie più registri insieme, es. `pop rsi; pop r15; ret`).

Per scoprire quali gadget esistono davvero, invece di indovinarli uno a uno, si enumera `rop.gadgets` (il dizionario interno `{indirizzo: Gadget}`):

```python
rop = ROP(exe)
for addr, gadget in rop.gadgets.items():
    print(hex(addr), gadget.insns, gadget.regs)
```

> [!warning] Lacuna nella documentazione ufficiale
> La pagina ufficiale (`docs.pwntools.com/en/stable/rop/rop.html`) non elenca `gadgets` tra i membri della classe `ROP`: compare solo di passaggio in un doctest (`r.gadgets == {}`), senza descriverne il tipo. I campi `.insns` e `.regs` del `Gadget` non sono nominati da nessuna parte nella pagina (si intuiscono solo dalla posizione negli esempi di `repr`, es. `Gadget(0x10000004, ['pop eax', 'ret'], ['eax'], 0x8)`), e la pagina dedicata alla classe `Gadget` risulta a un indirizzo che dà 404. Le informazioni sopra vengono dal sorgente di pwntools (`pwnlib/rop/rop.py` e `pwnlib/rop/gadgets.py`), ispezionabile con `inspect.getfile(ROP)` quando la documentazione online non basta.

## Esempio di ispezione statica

```python
from pwn import ELF

with ELF("/bin/ls", checksec=False) as binario:
    rapporto = binario.checksec(banner=False, color=False)
    assert isinstance(rapporto, str)
    print(rapporto)
    print("Proprietà CET nel file:", {
        "SHSTK": binario.shadowstack,
        "IBT": binario.ibt,
    })
```

`checksec()` restituisce il rapporto come `str`. Per un controllo nello script usa gli attributi booleani. L'esempio legge il file e stampa le proprietà rilevate.

## Ripasso

- **Perché un indirizzo trovato in un rapporto può non avere un nome in `ELF.symbols`?** La sequenza può iniziare all'interno di una funzione senza un simbolo dedicato.
- **Che cosa contiene `.insns`?** Le istruzioni in forma testuale, una stringa per istruzione.
- **Che cosa dimostra `binario.shadowstack == True`?** Che pwntools ha rilevato la proprietà SHSTK nell'ELF. Lo stato effettivo del processo si verifica durante l'esecuzione.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-ELF|ELF]] · [[pwn-symbols|symbols]] · [[pwn-checksec|checksec]]
- [Documentazione ufficiale del modulo ROP](https://docs.pwntools.com/en/stable/rop.html)
