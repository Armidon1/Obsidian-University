# Big-Endian and Little-Endian -  introduzione

Certamente. Questo è un concetto fondamentale, molto più "vicino al ferro" (close to the metal) rispetto al PNT, ma altrettanto critico, specialmente in cybersecurity.

"Endianness" si riferisce a un problema semplice: **l'ordine dei byte in memoria.**

### 🖥️ Il Problema: Dati Multi-Byte

Un computer memorizza i dati in una griglia di byte. Ogni byte ha un indirizzo di memoria unico e sequenziale (es: `1000`, `1001`, `1002`, `1003`...).

Questo è banale per un dato da 1 byte (come un `char` ASCII). Il carattere 'A' (valore esadecimale `0x41`) va nell'indirizzo `1000`. Fine.

Ma cosa succede con un tipo di dato più grande, come un intero a 32-bit (4 byte)?

Prendiamo il numero intero (hex): **`0x1A2B3C4D`**

Questo numero è composto da 4 byte:

- `1A` (il **Most Significant Byte** o MSB - "l'estremità più grande")
    
- `2B`
    
- `3C`
    
- `4D` (il **Least Significant Byte** o LSB - "l'estremità più piccola")
    

Se vogliamo salvare questo valore all'indirizzo di memoria `1000`, il computer ha due scelte logiche:

1. Memorizza il byte "grande" (`1A`) all'indirizzo più basso (`1000`)?
    
2. Memorizza il byte "piccolo" (`4D`) all'indirizzo più basso (`1000`)?
    

Entrambe le risposte sono corrette e portano ai due tipi di endianness.

---

### 1. Big-Endian (BE)

Il Big-Endian memorizza il **Most Significant Byte (MSB) all'indirizzo di memoria più basso**.

È l'ordine "naturale" per come noi umani leggiamo i numeri da sinistra a destra. Il "grande" (big) capo del numero viene per primo.

Usando il nostro esempio `0x1A2B3C4D` da salvare all'indirizzo `1000`:

|**Indirizzo Memoria**|**Valore (Byte)**|**Significato**|
|---|---|---|
|`1000`|`1A`|**MSB**|
|`1001`|`2B`||
|`1002`|`3C`||
|`1003`|`4D`|**LSB**|

- **Chi lo usa:** Architetture "storiche" o "server" (PowerPC di IBM/Motorola, SPARC, MIPS) e, soprattutto, i **protocolli di rete**.
    

### 2. Little-Endian (LE)

Il Little-Endian memorizza il **Least Significant Byte (LSB) all'indirizzo di memoria più basso**.

Questo può sembrare contro-intuitivo a prima vista, ma ha alcuni vantaggi computazionali a basso livello (ad esempio, rende più semplici le conversioni di tipo, come da `int` a `short`).

Usando il nostro esempio `0x1A2B3C4D` da salvare all'indirizzo `1000`:

|**Indirizzo Memoria**|**Valore (Byte)**|**Significato**|
|---|---|---|
|`1000`|`4D`|**LSB**|
|`1001`|`3C`||
|`1002`|`2B`||
|`1003`|`1A`|**MSB**|

- **Chi lo usa:** La maggior parte dell'hardware "consumer" moderno. **Intel (x86) e AMD (AMD64)** sono Little-Endian. Di conseguenza, il tuo PC o Mac (basato su Intel o Apple Silicon in modalità LE) è quasi certamente Little-Endian.
    

---

## 🛡️ Applicazioni Pratiche in Cybersecurity (Perché è cruciale)

Questo non è solo un dettaglio accademico. È una delle principali fonti di bug e vulnerabilità quando i sistemi comunicano.

### 1. Network Byte Order (L'Applicazione n.1)

I padri fondatori di Internet (ARPANET) dovevano scegliere un ordine standard per i campi numerici nei protocolli (come indirizzi IP, porte TCP, ecc.).

Hanno scelto il **Big-Endian**.

Questo standard è ora noto come **Network Byte Order**.

- **Il Problema:** Il tuo laptop Intel (Little-Endian) deve inviare un pacchetto TCP alla porta `80`. Il numero `80` (a 16 bit) è `0x0050`.
    
    - Il tuo PC (LE) lo memorizza in RAM come `50 00`.
        
    - La rete (BE) si aspetta di vederlo come `00 50`.
        
- **La Soluzione:** Usiamo funzioni standard (dalla libreria "socket") per convertire tra l'ordine del nostro "Host" e l'ordine della "Rete":
    
    - `htonl()`: **H**ost **to** **N**etwork **L**ong (converte un `uint32_t` da LE/BE a BE)
        
    - `htons()`: **H**ost **to** **N**etwork **S**hort (converte un `uint16_t` da LE/BE a BE)
        
    - `ntohl()`: **N**etwork **to** **H**ost **L**ong
        
    - `ntohs()`: **N**etwork **to** **H**ost **S**hort
        

> **Scenario Cyber:** Se un programmatore "dimentica" di usare `htons()` quando costruisce un pacchetto di rete custom (es. in uno scanner di porte o in un tool di spoofing), i sistemi Big-Endian leggeranno spazzatura. Se invia `0x0050` (porta 80) come `50 00` (dalla sua memoria LE), il ricevitore di rete lo interpreterà come `0x5000`... che è la porta **20480**. Il pacchetto finirà nel posto sbagliato.

### 2. Sviluppo di Exploit e Shellcode

Quando scrivi un exploit, ad esempio un buffer overflow, devi sovrascrivere l'indirizzo di ritorno (Return Address) nello stack per puntare al tuo codice malevolo (shellcode).

- **Scenario:** Stai attaccando un server x86 (Little-Endian). Vuoi che l'esecuzione salti all'indirizzo `0x08048A4C`.
    
- **Il Problema:** Non puoi semplicemente scrivere la stringa `"\x08\x04\x8A\x4C"` nel tuo payload. Poiché il sistema è Little-Endian, la CPU leggerà quel valore dallo stack _al contrario_.
    
- La Soluzione: Devi scrivere il tuo indirizzo nel payload in formato Little-Endian:
    
    payload = "A"*N + "\x4C\x8A\x04\x08"
    
    Quando la CPU (LE) legge questi 4 byte dalla memoria, li re-assemblerà nel valore corretto 0x08048A4C e salterà lì.
    

Se sbagli l'endianness, causerai un crash (Segmentation Fault) perché la CPU cercherà di saltare all'indirizzo `0x4C8A0408`, che è spazzatura.

### 3. Analisi di File e Reverse Engineering

Diversi formati di file binari (eseguibili, immagini, file di dati) hanno header che specificano l'endianness.

- Gli eseguibili **ELF** (Linux) e **PE** (Windows) sono tipicamente Little-Endian perché girano su hardware x86.
    
- I formati di immagine come JPEG e TIFF usano "magic numbers" all'inizio del file per dichiarare l'endianness (`II` per Intel/Little-Endian, `MM` per Motorola/Big-Endian).
    

Quando fai reverse engineering di un protocollo sconosciuto o di un formato di file (es. analizzando un malware), una delle prime cose da capire è l'endianness dei campi multi-byte.

---

### 💡 Mnemonica (Come ricordarselo)

- **Big-Endian**: Il "Big" end (MSB) va all'indirizzo più **B**asso (anche se questo non c'entra, aiuta). Pensa a "Network Byte Order".
    
- **Little-Endian**: Il "Little" end (LSB) va all'indirizzo più **L**ibero (il più basso). Pensa a "Intel".
    


# chi usa [[Little-Endian]] e chi [[Big-Endian]]

Oggi il mondo informatico è prevalentemente dominato dal **Little Endian** per quanto riguarda l'hardware di consumo, mentre il **Big Endian** regna sovrano nelle reti.

---

### 1. Piattaforme Little Endian (La dominanza attuale)

In questo formato, il **byte meno significativo** viene memorizzato all'indirizzo di memoria più basso (iniziale). È lo standard di fatto per quasi tutti i computer moderni, smartphone e tablet.

- **Architettura x86 e x86-64 (Intel e AMD):** Tutti i PC Windows, i server Linux basati su Intel/AMD e i vecchi Mac (con processori Intel) sono nativamente Little Endian.
    
- **Apple Silicon (M1, M2, M3, ecc.):** Anche se basati su ARM, i chip Apple per i Mac e gli iPad operano in modalità Little Endian per mantenere la compatibilità con l'ecosistema software moderno.
    
- **RISC-V:** La nuova architettura open-source è specificata come Little Endian per l'uso generale.
    
- **Sistemi Operativi Moderni:** Windows, Linux (nella stragrande maggioranza delle configurazioni), macOS, Android e iOS gestiscono la memoria in Little Endian.
    

> **Nota visiva:** Se hai il numero esadecimale `0x12345678`, in Little Endian viene salvato in memoria come: `78 56 34 12`.

### 2. Piattaforme Big Endian (Legacy e Reti)

Qui il **byte più significativo** viene memorizzato per primo. Questo è più intuitivo per la lettura umana (da sinistra a destra), ma meno comune nei processori odierni.

- **Network Byte Order (TCP/IP):** Questa è l'applicazione più importante oggi. **Tutti i protocolli Internet (IP, TCP, UDP)** utilizzano il Big Endian. Indipendentemente dal processore del tuo computer, quando i dati viaggiano sul cavo di rete, devono essere convertiti in Big Endian.
    
- **IBM z/Architecture (Mainframe):** I grandi mainframe IBM, utilizzati dalle banche e assicurazioni, sono storicamente Big Endian e mantengono questa caratteristica per retrocompatibilità.
    
- **Motorola 68000 (Legacy):** Usato nei primi Macintosh, Amiga, Atari ST e console come il Sega Mega Drive.
    
- **SPARC (Oracle/Sun):** I server Sun Microsystems storici usavano Big Endian.
    

> **Nota visiva:** Il numero `0x12345678` in Big Endian viene salvato esattamente come si legge: `12 34 56 78`.

### 3. Architetture Bi-Endian (Ibridi)

Molte architetture moderne sono progettate per supportare entrambi i formati, sebbene il sistema operativo di solito ne scelga uno e si attenga a quello.

- **ARM:** L'architettura ARM (usata in quasi tutti i telefoni cellulari) è tecnicamente bi-endian. Tuttavia, **Android e iOS la eseguono quasi esclusivamente in modalità Little Endian**.
    
- **PowerPC:** Famoso per l'uso nei vecchi Mac (G3, G4, G5) e nelle console (Xbox 360, PS3, Wii). Poteva funzionare in entrambi i modi, ma su Mac e console era tipicamente configurato come Big Endian.
    
- **MIPS:** Usato in vecchi router e console (come Nintendo 64 e PS1/PS2). Può essere configurato in entrambi i modi.
    

---

### Tabella Riassuntiva Rapida

|**Categoria**|**Esempi Principali**|**Endianness Tipica**|
|---|---|---|
|**PC Desktop / Laptop**|Intel, AMD, Apple Silicon|**Little Endian**|
|**Smartphone / Tablet**|ARM (Android, iOS)|**Little Endian** (configurazione OS)|
|**Reti (Internet)**|TCP, IP, UDP|**Big Endian** (Sempre)|
|**Mainframe**|IBM zSeries|**Big Endian**|
|**Console Retro**|Sega Genesis, N64, SNES|**Big Endian**|
|**Console Moderne**|PS5, Xbox Series X, Switch|**Little Endian**|

### Perché è importante saperlo?

Il problema sorge principalmente quando due sistemi diversi devono parlare tra loro (ad esempio, il tuo PC Intel che invia dati a un server mainframe o semplicemente invia un pacchetto su Internet).

Se invii un numero intero (4 byte) dal tuo PC (Little Endian) alla rete (Big Endian) senza convertirlo, il destinatario leggerà un numero completamente diverso. Per questo i programmatori usano funzioni come `htons()` (Host to Network Short) o `htonl()` (Host to Network Long) per garantire che i byte siano nell'ordine corretto prima della trasmissione.

# Perché non si sceglie uno standard preciso? ad esempio solo [[Little-Endian]] da ora in poi?

Hai toccato un punto fondamentale: tecnicamente, non c'è una "superiorità" schiacciante di un formato sull'altro. È un po' come chiedersi perché alcuni paesi guidano a destra e altri a sinistra: entrambi i modi funzionano, ma il problema nasce quando devi attraversare il confine.

La sopravvivenza di questa distinzione è dovuta a un mix di **storia, inerzia tecnologica e piccoli vantaggi specifici** che un tempo erano cruciali.

Ecco perché non ci siamo ancora omologati (e probabilmente non lo faremo mai del tutto):

### 1. Le "Guerre Religiose" (Origine Storica)

Il termine stesso "Endian" deriva da _I viaggi di Gulliver_, dove due fazioni combattevano una guerra per decidere se le uova sode andassero rotte dall'estremità grande (Big-endian) o piccola (Little-endian).

In informatica è successo lo stesso:

- **Intel** ha scommesso sul Little Endian fin dai primi chip 8086.
    
- **Motorola** e **IBM** hanno scommesso sul Big Endian.
    
- Le **Reti (Internet)** sono state standardizzate su Big Endian.
    

Poiché i processori Intel (x86) hanno vinto la guerra dei PC e dei server, il Little Endian è diventato lo standard "di fatto" per il calcolo locale, mentre il Big Endian è rimasto lo standard per la comunicazione.

### 2. Vantaggi Tecnici (Perché non sono _esattamente_ uguali)

Anche se oggi contano meno, ci sono differenze logiche che hanno cementato le scelte decenni fa:

- Il vantaggio del Little Endian (Matematica e Casting):
    
    Immagina di avere un numero a 32 bit (long) e di volerlo leggere come se fosse a 8 bit (char). In Little Endian, l'indirizzo di memoria del numero completo e l'indirizzo del suo byte meno significativo sono lo stesso. Il processore non deve fare calcoli aggiuntivi per "restringere" il dato. Questo rendeva l'hardware leggermente più semplice da progettare negli anni '70/'80.
    
- Il vantaggio del Big Endian (Confronto e Ordine):
    
    È molto più veloce determinare se un numero è positivo o negativo (guardando il primo byte) o confrontare due numeri per vedere quale è più grande, perché i bit più "pesanti" arrivano per primi. È come cercare una parola nel dizionario: guardi la prima lettera, non l'ultima.
    

### 3. L'Inerzia: "Troppo grande per fallire"

Perché non cambiare tutto oggi?

1. **Internet è Big Endian:** Cambiare lo standard TCP/IP richiederebbe di aggiornare ogni singolo router, switch e sistema operativo del pianeta. Impossibile.
    
2. **Il Software Legacy:** Ci sono miliardi di righe di codice scritte assumendo che l'hardware sia Little Endian (su PC) o Big Endian (su Mainframe bancari). Cambiare l'hardware romperebbe il software.
    
3. **I Dati salvati:** Immagina miliardi di file (database, formati immagine, file binari) salvati in un formato. Se domani il mondo cambiasse standard, quei file diventerebbero illeggibili senza una conversione.
    

### 4. La Soluzione Moderna: Convivenza Pacifca

Invece di omologarsi, l'hardware moderno ha reso la conversione quasi "gratuita" in termini di prestazioni.

I processori moderni hanno istruzioni specifiche (come BSWAP su x86) che invertono l'ordine dei byte in un singolo ciclo di clock.

Quindi, il processore lavora come preferisce (Little Endian), e quando deve mandare dati in rete, li "gira" al volo senza che l'utente se ne accorga.

---

**In sintesi:** Non ci omologhiamo perché **costerebbe troppo** riscrivere l'intera infrastruttura mondiale. È più economico mantenere due standard e far fare ai computer il lavoro sporco di traduzione quando si parlano tra loro.

