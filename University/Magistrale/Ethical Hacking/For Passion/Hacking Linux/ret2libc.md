# Return-to-libc

> Cap. 5 _Hacking UNIX_ — Hacking Exposed 7th ed. Nota di ripasso, taglio da esame.

---

## 1. Il problema che risolve

Il **[[Buffer Overflow]] classico** funziona così: inietti dello shellcode dentro il buffer e sovrascrivi il return address in modo che punti **dentro il buffer stesso**. Al `ret`, la CPU salta sullo stack ed esegue il tuo codice.

La contromisura che ha ucciso questa tecnica è lo **stack non eseguibile** (bit **NX** / No-eXecute, esposto come **DEP** su Windows, principio **W^X**: una pagina o è scrivibile o è eseguibile, mai entrambe). La CPU si rifiuta di eseguire istruzioni nelle pagine dello stack. Lo shellcode iniettato non parte più.

**Return-to-libc nasce esattamente per aggirare NX**, senza eseguire una sola istruzione sullo stack.

---

## 2. L'idea centrale

Invece di saltare a codice **tuo** (sullo stack, non eseguibile), salti a codice **già esistente ed eseguibile**: le funzioni della **libreria standard C (libc)**, che è mappata in quasi ogni processo UNIX ed è marcata eseguibile.

- "Return **into** libc" = sovrascrivi il return address con **l'indirizzo di una funzione di libc**.
- Bersaglio classico: **`system()`**. Perché proprio lei? Perché prende una **stringa** e la esegue come comando di shell (`/bin/sh -c <stringa>`). Quindi `system("/bin/sh")` ti dà direttamente una **shell interattiva**.

Il concetto-chiave da dire all'esame: **non esegui codice sullo stack, riusi codice legittimo che vive altrove**. NX proibisce di _eseguire_ lo stack, non di _saltare_ a codice già eseguibile.

---

## 3. Come si costruisce il payload (32-bit, convenzione cdecl)

In x86 32-bit con convenzione **cdecl**, gli argomenti di una funzione si passano **sullo stack**. Al momento di una `call` normale, lo stack visto dalla funzione chiamata è:

```
[ return address ][ arg1 ][ arg2 ] ...
```

Quindi, per "simulare" una chiamata a `system()` tramite `ret`, devi disporre lo stack **come se system fosse stata chiamata normalmente**. Dal basso (indirizzi bassi) verso l'alto:

```
buffer[]              <- riempito di padding (AAAA...)
saved EBP             <- padding
return address   -->  &system()        (sovrascritto: dove salta il ret)
ritorno fittizio -->  &exit()          (dove "tornerà" system quando finisce)
arg1             -->  &"/bin/sh"        (argomento di system)
```

Cosa succede al `ret` della funzione vulnerabile:

1. La CPU **poppa il return address** (ora `&system()`) **in EIP** e incrementa ESP → salta dentro `system()`.
2. `system()` parte e, secondo cdecl, si aspetta il proprio return address in cima allo stack e il primo argomento subito sopra. Trova il **ritorno fittizio** (`&exit`, così il programma chiude pulito invece di crashare) e l'argomento **`&"/bin/sh"`**.
3. Esegue `system("/bin/sh")` → **shell**.

### Dove sta la stringa "/bin/sh"?

Tre possibilità tipiche:

- **Già dentro libc**: la stringa `"/bin/sh"` esiste letteralmente nel segmento dati di libc — trovi il suo indirizzo e lo usi (trucco molto comune).
- Nel **buffer** che hai riempito tu.
- In una **variabile d'ambiente** (il cui indirizzo sullo stack è abbastanza prevedibile senza ASLR).

---

## 4. Concatenare più chiamate (ret2libc a catena)

Puoi mettere in fila **più funzioni libc**. Esempio classico per recuperare privilegi: se il processo aveva fatto un drop a UID non privilegiato, chiami prima **`setuid(0)`** e poi **`system("/bin/sh")`** per ottenere una root shell.

Il "ritorno fittizio" di una funzione diventa **l'indirizzo della funzione successiva**. Ma con cdecl gli argomenti restano sullo stack, quindi tra una chiamata e l'altra devi **"pulire" gli argomenti**: si usa come ritorno intermedio un piccolo **gadget `pop; ret`** (o `pop; pop; ret` a seconda di quanti argomenti scartare), che scarta i parametri e salta alla funzione dopo.

> Questo `pop; ret` **è già un gadget**: il momento in cui inizi a concatenare ret2libc con gadgetini è la porta d'ingresso della **ROP**.

---

## 5. Varianti del bersaglio (oltre system)

- **`execve("/bin/sh", NULL, NULL)`** — più "pulito" di system, esegue direttamente senza passare da `sh -c`.
- **`mprotect()` / `VirtualProtect()`** — caso elegante: usi ret2libc per **rendere eseguibile una regione di memoria** (disattivi NX su quelle pagine), poi ci salti sopra ed esegui il tuo shellcode. Bypassi NX usando una funzione che disattiva NX.
- **`mmap()`** — mappa nuova memoria eseguibile.

---

## 6. Le difese contro ret2libc (e come si reagisce)

|Difesa|Cosa fa|Reazione dell'attaccante|
|---|---|---|
|**ASLR**|Randomizza la base di libc/stack/heap → non sai dove sta `system()`|**Info leak** (leggi un indirizzo da memoria e calcoli la base di libc) o brute force su 32-bit (entropia bassa)|
|**ASCII-armor**|Mappa libc a indirizzi contenenti un byte nullo (`0x00`)|Il byte nullo **tronca le strcpy** → non riesci a scrivere l'indirizzo di system nel payload. Si reagisce con ROP/gadget altrove o ret2plt|
|**Stack canary**|Valore casuale tra variabili e return address|Becca l'overflow **prima** che il return address venga usato → serve info leak per conoscere il canary|
|**Full RELRO**|GOT in sola lettura|Toglie alcune scritture comode (ret2GOT)|

La risposta generale quando "ret2libc puro" non basta più → **ROP** (catene di gadget), che generalizza tutto.

---

## 7. ret2libc vs ROP (la differenza che vale il punto)

- **ret2libc**: riusi **funzioni intere** di libc (`system`, `execve`...). Limite: dipendi dall'esistenza della funzione comoda, e in **64-bit** gli argomenti vanno nei **registri** (rdi, rsi...), non sullo stack → non basta piazzarli e basta.
- **ROP**: riusi **frammenti** (gadget = sequenze cortissime che finiscono in `ret`), concatenandoli. Ti dà **computazione arbitraria**, puoi **caricare i registri** (indispensabile in 64-bit, es. `pop rdi; ret`), e bypassi NX completamente.

In una frase: **ret2libc è il caso particolare / precursore della ROP**. Stessa filosofia (code reuse, niente esecuzione sullo stack), granularità diversa (funzioni vs gadget).

---

## 8. Risposta-modello breve (da scrivere all'esame)

> Il return-to-libc è una tecnica per sfruttare un buffer overflow quando lo **stack è non eseguibile** (NX/DEP), condizione che blocca il buffer overflow classico basato su shellcode iniettato. Invece di eseguire codice sullo stack, l'attaccante sovrascrive il return address con l'indirizzo di una funzione **già esistente in libc**, tipicamente **`system()`**, e dispone sullo stack un ritorno fittizio e l'argomento (`&"/bin/sh"`). Al `ret`, il flusso salta in `system("/bin/sh")` ottenendo una shell. Il punto è che **non viene eseguita alcuna istruzione sullo stack**: si riusa solo codice legittimo ed eseguibile, aggirando NX. La generalizzazione di questa idea, basata su frammenti di codice ("gadget") anziché funzioni intere, è la **ROP**. Contromisura principale: **ASLR**, che randomizza l'indirizzo di libc.

---

## 9. Errori da NON fare all'esame

- ❌ "esegue codice sullo stack" — è **l'esatto contrario**: il senso è NON eseguire sullo stack.
- ❌ confondere **NX** (riguarda l'_esecuzione_) con **ASLR** (riguarda gli _indirizzi_). NX → ret2libc lo aggira; ASLR → è la difesa che rende ret2libc difficile.
- ❌ scrivere "**libg**" — è **libc**.
- ✅ `system()` perché **esegue una stringa come comando di shell** (motivare sempre il "perché proprio quella").

# Come si comporta lo stack graficamente 
![[ret2libc_stack_prima_dopo.svg|697]]
Ecco il prima/dopo sullo stack. A sinistra il frame "sano" di una funzione vulnerabile, a destra com'è dopo che ci hai scritto sopra il payload ret2libc.Come leggerlo, dal basso verso l'alto:

Nel frame normale (sinistra) il **buffer** sta in fondo, agli indirizzi bassi. Subito sopra c'è il **saved EBP**, e sopra ancora il **return address** — che in condizioni normali punta al codice del chiamante, dove la funzione deve tornare col `ret`. Più in alto c'è il frame del chiamante.

L'overflow scrive **verso l'alto** (freccia arancione): riempi il buffer di padding (le `AAAA`), travolgi il saved EBP, e arrivi a **sovrascrivere il return address con l'indirizzo di `system()`**. Ma non ti fermi lì: continui a scrivere negli slot _sopra_ il return address, perché ti servono per costruire il finto frame di system. Ci metti un **return address fittizio** (dove system "tornerà" quando finisce — spesso `&exit()` o spazzatura) e poi il **puntatore a `"/bin/sh"`**, che sarà l'argomento di system.

Il momento chiave è il `ret` della funzione vulnerabile: la CPU **poppa il return address — che ora è `&system()` — dentro EIP e ci salta**. A quel punto `system()` parte e va a leggersi il suo argomento dallo slot subito sopra: trova `&"/bin/sh"` → esegue `system("/bin/sh")` → shell.

E qui sta tutto il senso: **non hai mai eseguito una sola istruzione sullo stack**. Lo stack resta dati; tu hai solo riusato codice (system) che vive in libc ed è già eseguibile. Ecco perché NX/DEP non ti ferma — proibisce di _eseguire_ lo stack, non di _saltare_ a codice legittimo altrove.

Una nota che lega questo a ROP: questo layout è il caso classico **32-bit**, dove gli argomenti delle funzioni si passano _sullo stack_ — per questo basta piazzare `&"/bin/sh"` in uno slot. In **64-bit** gli argomenti vanno nei _registri_ (rdi, rsi…), quindi non puoi semplicemente metterli sullo stack: ti serve prima un piccolo gadget tipo `pop rdi; ret` per caricare l'argomento nel registro giusto. Ed è esattamente lì che il ret2libc "puro" non basta più e si passa alla ROP che hai visto prima.

Tutto chiaro sul prima/dopo? Se sì, riprendiamo: ti rimando al **Cluster 3 (FTP anonimo + bounce)** oppure direttamente a **symlink/SUID** (la scalata locale a root), come preferisci.

# Graficamente il ROP

Una catena ROP si capisce meglio "camminandoci dentro" passo per passo. Ho usato l'esempio che continua dalla nota di prima: il caso **64-bit** in cui l'argomento va caricato in un registro (`rdi`), quindi serve per forza un gadget — proprio dove il ret2libc puro non basta. Premi "Prossimo passo" e guarda ESP salire lungo la catena, ogni `ret` che lancia il gadget successivo.Il modello mentale da portarti all'esame, in una frase: **lo stack diventa il "programma" (una lista di indirizzi di gadget) ed ESP fa da program counter — è il `ret` di ogni gadget il motore che fa avanzare ESP e salta al pezzo successivo.**

![[Video del 2026-05-31 19-18-02.mp4]]

Tre cose che si vedono bene scorrendo i passi e che valgono il punto pieno:

Il `ret` non è la fine di niente, è il _dispatcher_: pesca il prossimo indirizzo dallo stack e ci salta. Per questo ogni gadget utile deve finire in `ret` — è ciò che permette di concatenarli.

Il gadget `pop rdi ; ret` esiste perché in 64-bit gli argomenti vanno nei registri, non sullo stack: non puoi semplicemente "appoggiare" `/bin/sh` come nel ret2libc a 32-bit, devi _caricarlo_ in `rdi` prima di chiamare `system`. Questo è esattamente il confine dove il ret2libc puro non basta più.

E il punto che chiude il cerchio con NX: in tutta la catena non hai mai eseguito una sola istruzione sullo stack. Riusi solo codice già marcato eseguibile → NX/DEP è completamente aggirato.

Se vuoi, col bottone "Versione a 3 argomenti" ti monto la catena per una chiamata tipo `execve` (rdi, rsi, rdx) che mostra il concatenamento più lungo. Altrimenti riprendiamo il richiamo attivo: **Cluster 3 (FTP)** o **symlink/SUID**?

# Versione a 3 argomenti

Ecco la catena estesa: per `execve("/bin/sh", NULL, NULL)` devi controllare **tre** registri (rdi, rsi, rdx), quindi servono tre gadget di `pop` concatenati prima della funzione. Ho aggiunto anche una finezza realistica — un gadget "sporco" che poppa un registro in più — per mostrarti perché nelle catene vere compaiono le slot di scarto.Due lezioni nuove rispetto alla catena corta, ed entrambe sono il tipo di dettaglio che fa capire al prof che hai capito _davvero_:

![[Video del 2026-05-31 19-21-50.mp4]]
**Un gadget per ogni registro da controllare.** Vuoi tre argomenti? Ti servono tre `pop` (uno per rdi, rsi, rdx), incatenati dai `ret`, e solo alla fine la funzione. È il principio che rende la ROP _componibile_: ogni pezzetto fa una micro-operazione e passa il testimone col `ret`. Da qui all'idea che con abbastanza gadget puoi fare qualunque cosa (ROP "Turing-completa") il passo è breve.

**Le slot di scarto.** Nel mondo reale non trovi sempre il gadget pulito che ti serve. Un `pop rsi ; ret` liscio spesso non esiste; quello che il binario ti offre è `pop rsi ; pop r15 ; ret`. Quel `pop r15` di troppo _deve_ consumare uno slot, quindi sei costretto a mettere un valore-spazzatura nella catena per non sfasare tutto. È per questo che le catene ROP reali sono piene di valori che "non servono a niente": stanno lì solo per assecondare gadget non puliti.

Un'ultima nota per completezza: qui ho modellato `execve` come _funzione di libc_. La variante ancora più comune su Linux è via **syscall diretta** — in quel caso aggiungi un gadget `pop rax ; ret` per mettere `rax = 59` (il numero della syscall execve) e chiudi con un gadget `syscall ; ret` invece della funzione. Stessa identica logica, solo un registro in più.

# differenze assembly tra 32 bit e 64 bit

Tranquillo, e anzi: per il tuo esame il **32-bit è esattamente quello che conta**. Ti chiarisco al volo cosa cambia e quale dei miei visual era quale.

Il **diagramma prima/dopo** che ti ho fatto era **già a 32-bit** (cdecl) — quello è il tuo mondo, va benissimo così. I due **stepper della ROP** invece li ho fatti a 64-bit, ed è lì che è spuntata la complicazione dei registri (`rdi`, `rsi`, `rdx`). Quella complicazione **non esiste a 32-bit**.

Le differenze che contano per gli exploit:

| |32-bit (x86)|64-bit (x86-64)|
|---|---|---|
|Registri|`eax`, `ebx`, `ecx`, `esp`, `eip`…|`rax`…`rsp`, `rip` + `r8`–`r15`|
|**Argomenti di funzione**|**sullo stack** (cdecl)|**nei registri**: rdi, rsi, rdx, rcx, r8, r9|
|Dimensione indirizzi|4 byte|8 byte (spesso con byte nulli in alto)|

La riga in grassetto è tutta la differenza che ti serve sapere. La conseguenza pratica:

**ret2libc a 32-bit è più SEMPLICE, non più difficile.** Siccome gli argomenti vanno sullo stack, per chiamare `system("/bin/sh")` ti basta disporre `[&system][ritorno fittizio][&"/bin/sh"]` — che è _esattamente_ il diagramma che ti ho mostrato. Niente gadget `pop rdi`, perché l'argomento è già lì sullo stack. Quei `pop rdi ; ret` servivano **solo** perché a 64-bit l'argomento deve finire in un registro.

**La ROP a 32-bit esiste comunque**, e il concetto è identico: concateni gadget che finiscono in `ret`, riusi codice esistente, aggiri NX. L'unica differenza è il _ruolo_ del gadget `pop`: a 32-bit, quando incateni più chiamate di funzione, ti serve un `pop ; ret` (o `pop-pop-ret`) per **scartare gli argomenti** della funzione precedente dallo stack e allineare l'indirizzo della prossima — è _pulizia dello stack_, non caricamento di registri. Stessa filosofia, motivo diverso.

Per la risposta d'esame su ROP non devi nemmeno entrare in questo dettaglio: la definizione che conta ("riusi frammenti che finiscono in `ret`, li concateni per ottenere computazione arbitraria, bypassi NX completamente") è **indipendente dall'architettura**. Sei a posto.
