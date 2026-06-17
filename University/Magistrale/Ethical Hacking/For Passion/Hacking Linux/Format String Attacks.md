---

tags:

- exploitation
- memory-corruption
- format-string
- buffer-overflow-family
- hacking-exposed-7
- data-driven-attacks aliases:
- format string vulnerability
- format string bug
- FSB
- printf vulnerability

---

# Format String Attacks — Quando il Format è Input dell'Utente

## 1. Il bug pattern

```c
// SICURO
printf("%s", user_input);   // %s è la format string, user_input è l'argomento

// VULNERABILE
printf(user_input);          // user_input È la format string
```

Quando l'utente controlla la **format string** passata a `printf`, può iniettare format specifier che `printf` interpreterà — leggendo/scrivendo memoria che non doveva.

> [!warning] Lo stesso pattern di [[Data-Driven Attacks]] Anche qui il dato dell'utente attraversa il confine **dato → codice**. La format string è "codice interpretato" per `printf` — esattamente come SQL è codice interpretato dal DB, o template string è codice per il template engine. Stesso pattern, contesto diverso.

Vale per **tutta la famiglia**: `printf`, `fprintf`, `sprintf`, `snprintf`, `syslog`, `vfprintf`, ecc.

---

## 2. Perché succede — printf è variadic

`printf` è una **funzione a numero di argomenti variabile** (varargs). Sa quanti argomenti sono stati passati **solo guardando la format string**:

```c
printf("a: %d; b: %d", a, b);
// printf vede 2 format specifier (%d %d) → si aspetta 2 argomenti
// li legge dallo stack secondo la calling convention
```

```
Stack durante la chiamata:
+--------------------+
|  &"a: %d; b: %d"   |  ← address della format string
+--------------------+
|  valore di a       |
+--------------------+
|  valore di b       |
+--------------------+
```

`printf` ha un **puntatore interno** che scorre lo stack — per ogni `%d`, legge 4 byte dal puntatore e avanza.

### Il bug strutturale

E se passi **più specifier che argomenti**?

```c
printf("a: %d; b: %d", a);
// printf si aspetta 2 argomenti, gliene passi 1
// per il secondo %d legge dallo stack quello che c'è — qualsiasi cosa
```

```
+--------------------+
|  &format string    |
+--------------------+
|  valore di a       |
+--------------------+
|  ???               |  ← printf legge qui per il secondo %d
+--------------------+
```

`printf` non sa che non gli hai passato il secondo argomento. Legge dallo stack quello che capita.

> [!note] Il punto chiave `printf` non valida nulla — si fida ciecamente che il numero di specifier corrisponda al numero di argomenti. Se controlli la format string, controlli quanto e cosa printf legge dallo stack.

---

## 3. I format specifier pericolosi

| Specifier      | Cosa fa                                                                           | Pericolo                        |
| -------------- | --------------------------------------------------------------------------------- | ------------------------------- |
| `%x`           | Legge 4 byte dallo stack e stampa in hex                                          | **Leak della stack**            |
| `%d` / `%u`    | Legge 4 byte dallo stack come intero                                              | Stack leak (meno comodo)        |
| `%s`           | Legge un **puntatore** dallo stack e stampa la stringa puntata                    | **Read arbitrario di memoria**  |
| `%n`           | Scrive il numero di byte stampati finora **all'indirizzo** puntato dall'argomento | **Write arbitrario in memoria** |
| `%p`           | Come %x ma format pointer                                                         | Stack leak                      |
| `%hn` / `%hhn` | Versioni narrow di %n (write di short / byte)                                     | Write preciso                   |

> [!warning] %n è il vero killer Mentre `%x` e `%s` permettono solo lettura, **`%n` permette scrittura arbitraria** — può sovrascrivere return address, GOT entries, function pointers. È il motore che trasforma una format string bug in RCE.

---

## 4. Cosa puoi fare — escalation di impatto

### 4.1 Leak dello stack — `%x`

```c
printf("%x %x %x %x");
// printf legge 4 valori dallo stack (sono ciò che c'è là)
// stampa: 7ffec3d4 00400540 7fff5c80 401234
```

Hai appena leakato 4 valori dello stack. Tipicamente trovi: canary, return address, saved RBP, puntatori a libc.

### 4.2 Leak del canary e ASLR bypass

I primi due step di ogni exploit moderno:

1. Leak canary con format string → bypass stack canary
2. Leak indirizzo libc dallo stack → calcolo offset → bypass ASLR

Le format string sono lo strumento più comune per fare info leak — il prerequisito per quasi ogni exploit moderno.

### 4.3 Read arbitrario — `%s` + indirizzo crafted

Se l'input dell'utente finisce sullo stack (es. `char buf[200]` poi `printf(buf)`), puoi mettere indirizzi **dentro la format string stessa**:

```
input = "\x10\x01\x48\x08 %x %x %x %x %s"
                     ^               ^
                     |               leggi memoria all'indirizzo
                     indirizzo target (su stack)
```

Logica:

1. `\x10\x01\x48\x08` viene messo all'inizio del buffer (sullo stack)
2. Ogni `%x` fa avanzare il puntatore interno di printf di 4 byte
3. Dopo abbastanza `%x`, il puntatore interno arriva al punto del buffer dove sta il tuo indirizzo
4. `%s` lo interpreta come puntatore e stampa la stringa **all'indirizzo che hai scritto**

→ **Hai letto memoria arbitraria** del processo.

```
Stack durante printf(buf):
+----------------------+
|  buf[0..3] = \x10\x01\x48\x08  |  ← tuo indirizzo target
+----------------------+
|  buf[4..7] = " %x %x..."       |
+----------------------+
|  ...                           |  ← printf scorre con %x
+----------------------+
|  arriva qui col puntatore     |  ← %s qui interpreta come pointer
+----------------------+
                                    → legge la stringa a 0x10014808
```

### 4.4 Write arbitrario — `%n`

Stessa tecnica, ma con `%n` al posto di `%s`. `%n` scrive il numero di byte stampati finora all'indirizzo puntato.

```
input = "<indirizzo target>%<n_byte>x%n"
```

Per scrivere un valore specifico V, fai in modo che printf stampi V byte prima del `%n`, controllando il padding con `%<numero>x`.

Tipici target di scrittura:

- **Return address** sullo stack
- **GOT entries** (Global Offset Table) — sovrascrivi `puts@GOT` → la prossima `puts()` chiama `system()`
- **vtable pointer** di oggetti C++
- **`__malloc_hook` / `__free_hook`** (legacy glibc)

---

## 5. La sfida pratica — trovare l'offset

Il "challenge" che cita HE7: **a che offset (in termini di `%x`) sullo stack si trova il tuo input?**

Tecnica standard di scoperta:

```c
// Inserisci un marker riconoscibile
input = "AAAA %x %x %x %x %x %x %x %x %x %x"

// Output:
// AAAA 7fff... 4006... 0000... 4141 4141 ...
//                                 ↑↑↑↑
//                                 trovato! "AAAA" come hex
```

Quando vedi `41414141` (AAAA in hex) nell'output, sai a quale offset si trova il tuo buffer. Da lì costruisci l'exploit usando quella distanza.

[[Format String Attacks#Chiarimenti|guarda qui per capire meglio]]
### Notazione direct parameter access — `%n$x`

Una volta noto l'offset, invece di scrivere `%x %x %x %x %x %x` puoi usare:

```c
"%7$x"   // leggi direttamente il 7° argomento (offset 7)
```

Molto più pulito e affidabile per costruire exploit.

---

## 6. Da format string a RCE — esempio completo

```c
// Programma vulnerabile
void vuln() {
    char buf[200];
    fgets(buf, 200, stdin);
    printf(buf);   // VULNERABILE
}
```

Catena d'attacco tipica:

```
Step 1: Leak del canary
    input = "%7$lx"   ← leak primo qword utile
    → ottieni il canary

Step 2: Leak indirizzo libc
    input = "%23$lx"  ← leak return address o saved frame
    → calcola base libc

Step 3: Sovrascrivi GOT entry di printf con address di system
    input = "<GOT_printf>%<padding>c%n"
    → la prossima printf() chiamerà system()

Step 4: Trigger
    input = "/bin/sh"   ← stringa per system()
    → quando il programma chiama printf("/bin/sh"), in realtà
      esegue system("/bin/sh") → shell!
```

---

## 7. Mitigazioni

|Mitigazione|Come funziona|Limiti|
|---|---|---|
|**Compiler warning `-Wformat`**|Avverte se format string non è letterale|Solo se il bug è ovvio in build time|
|**`-Wformat-security`**|Errore se format string non è letterale|Aggressive, raccomandato|
|**`_FORTIFY_SOURCE`**|Sostituisce printf con versioni che validano|Solo per letterali noti|
|**Linker `-Wl,-z,now`**|RELRO full → GOT diventa read-only dopo init|Impedisce overwrite GOT|
|**ASLR + canary**|Rendono i leak comunque necessari|Le format string sono ottimi info leak|
|**Static analysis** (Coverity, Clang Static Analyzer)|Trova chiamate `printf(var)`|Falsi negativi su flow complessi|

> [!tip] La fix è sempre la stessa
> 
> ```c
> // SEMPRE
> printf("%s", user_input);
> // MAI
> printf(user_input);
> ```
> 
> Non c'è eccezione legittima a questa regola. Se vedi `printf(var)` in un codebase, è quasi certamente un bug.

---

## 8. Stato attuale — quanto è ancora rilevante?

|Contesto|Format string bug oggi?|
|---|---|
|Codice C nuovo|Raro — compiler warning lo blocca|
|Codice C legacy|Comune — vecchi codebase non rebuildati con warning|
|CTF / wargame|**Onnipresente** — tema classico di pwn challenges|
|Sistemi embedded|Frequente — compilatori vecchi, no warning|
|Software di rete con logging custom|Possibile — `syslog(user_input)` è equivalente|

> [!note] Per pentest / CTF Format string è **must-know** per challenges di binary exploitation. È spesso l'unica primitiva disponibile per fare info leak (canary, libc base) prima di sfruttare un buffer overflow. Workflow tipico in pwn challenges:
> 
> 1. Trovi format string bug → ottieni canary e libc leak
> 2. Trovi buffer overflow → sfrutti con conoscenza di canary e libc
> 3. ROP / ret2libc verso shell

---

## Takeaways

1. Format string vulnerability = controllo dell'utente sulla format string passata a `printf` (o famiglia)
2. `printf` legge dallo stack usando la format string come "guida" — controlli la guida, controlli cosa legge
3. Specifier pericolosi: **`%x` leak**, **`%s` read arbitrario**, **`%n` write arbitrario**
4. La tecnica chiave: inserire **indirizzi dentro la format string stessa**, poi usare `%x` per posizionare il puntatore interno fino a quegli indirizzi
5. **`%n` trasforma una format string bug in RCE** — typically sovrascrivendo GOT entries o return address
6. Le format string sono **lo strumento principale di info leak** per bypassare canary e ASLR in exploit moderni
7. Fix definitivo: `printf("%s", user_input)` — mai `printf(user_input)`
8. Compiler warning (`-Wformat-security`) chiude il bug a build time se attivato

---

## Wiki-links

- [[data_driven_attacks]]
- [[buffer_overflow]]
- [[stack_canary]]
- [[ASLR]]
- [[got_overwrite]]
- [[rop_return_oriented_programming]]
- [[binary_exploitation]]
- [[pwn_ctf]]
- [[hacking_exposed_7_unix]]

---
# Chiarimenti

Hai un equivoco fondamentale: **`%x` non viene "pushato" sullo stack**. È solo testo dentro la format string. Ricostruiamo cosa succede davvero.

## Cosa viene davvero pushato

Quando il programma esegue:

```c
char buf[200];
strcpy(buf, "AAAA %x %x %x %x ...");  // buf contiene la stringa
printf(buf);                            // chiamata vulnerabile
```

Quello che viene push'ato è **solo un argomento**: il **puntatore** al buffer. La format string in sé non viene messa sullo stack a pezzi — il suo contenuto (incluso "AAAA %x %x") sta dentro `buf`, che è una variabile locale già allocata sullo stack.

```
Stack (32-bit, semplificato):

  indirizzi alti
+-----------------------+
|  ... (frame chiamante)|
+-----------------------+
|  buf[196..199]        |
|  ...                  |
|  buf[8..11]  "%x %x"  |
|  buf[4..7]   = "AAAA" |  ← le tue A sono QUI, già sullo stack
|  buf[0..3]   = "AAAA" |     come contenuto di un local del chiamante
+-----------------------+
|  altre var locali     |
+-----------------------+
|  saved EBP            |
+-----------------------+
|  return address       |
+-----------------------+
|  &buf  ← puntatore    |  ← UNICO argomento push'ato per printf
+-----------------------+   
|  ... stack di printf  |
  indirizzi bassi
```

`%x` non è un argomento. `%x` è **un'istruzione per printf** che dice "leggi un valore dal prossimo slot variadico". Non aggiunge nulla allo stack.

---

## Cosa fa printf con `%x`

Printf mantiene un **puntatore interno** che parte subito dopo la format string (dove dovrebbero stare gli argomenti variadici). Ogni `%x` fa avanzare quel puntatore di 4 byte (su 32-bit) e stampa quei 4 byte come hex.

```
Puntatore interno di printf:
  parte qui (subito dopo &buf nello stack frame)
  ↓
  legge 4 byte → stampa → avanza
  legge 4 byte → stampa → avanza
  ...
  continua a salire nello stack
  ↓
  prima o poi raggiunge la zona dove sta buf
  ↓
  legge i 4 byte = "AAAA" = 0x41414141
  ↓
  stampa "41414141" — segnale che ci sei arrivato!
```

---

## La direzione che ti confondeva

Tu pensavi: "ogni `%x` aggiunge cose allo stack → mi allontano da AAAA". In realtà:

- `%x` **non aggiunge nulla** — è solo testo
- Il puntatore interno di printf **sale** nello stack (verso indirizzi più alti)
- `buf` (con dentro AAAA) **è già lì sopra**, perché è una variabile locale del chiamante allocata prima della chiamata a printf
- Quindi più `%x` metti, più ti **avvicini** al punto dove sta scritto AAAA

```
puntatore interno parte qui (vicino allo stack di printf)
     ↓ 
   %x  → legge & stampa, avanza di 4 byte
   %x  → avanza
   %x  → avanza
   ...  → continua a salire
   %x  → AVANZA E RAGGIUNGE buf → legge "AAAA" → stampa "41414141"
                                     ↑
                                     fermo qui — hai trovato l'offset
```

---

## Sintesi del fraintendimento

|Tuo modello mentale|Cosa succede davvero|
|---|---|
|`%x` viene push'ato sullo stack|`%x` è testo nella format string, non viene push'ato|
|Più `%x` = più lontano da AAAA|Più `%x` = puntatore interno avanza verso dove sta AAAA|
|AAAA è "indietro nel passato"|AAAA è in alto nello stack (frame del chiamante), printf parte in basso e sale|

Quando vedi `41414141` nell'output, hai contato quanti `%x` sono serviti per arrivarci → quello è l'**offset** del tuo input dal punto di vista di printf. Da lì puoi usare `%<n>$x` per accedere direttamente a quell'offset.

# Domanda: quindi se passo un buffer di 12 byte, printf(buffer) mi mette nello stack tutti i 12 byte. supponiamo che il buffer sia stato riempito solo di 4 byte, mi servono 3 %x per raggiungere il valore del mio buffer (il terzo %x mi mostra i 4 byte scritti), giusto?

Quasi — ma c'è ancora un'imprecisione importante da chiarire.

## Il buffer **non viene "messo" sullo stack da printf**

Il buffer **era già sullo stack** prima della chiamata a printf. È una variabile locale della funzione chiamante. Printf riceve solo **un puntatore** a quel buffer, non il contenuto.

```c
void vulnerable() {
    char buf[12];           ← buf è una local, allocata SUBITO sullo stack
    strcpy(buf, "AAAA");    ← scrivi nel buffer (già sullo stack)
    printf(buf);            ← passi il PUNTATORE, non i 12 byte
}
```

L'unica cosa che viene "pushata" per la chiamata a printf è l'indirizzo `&buf` (4 byte su 32-bit) — non i 12 byte.

---

## L'offset non dipende dalla dimensione del buffer

Questo è il punto chiave. Il numero di `%x` necessari per raggiungere il buffer dipende da **dove sta il buffer rispetto al punto di partenza del puntatore interno di printf**, non da quanto è grande.

Su 32-bit x86 con cdecl, lo stack appare così quando printf inizia:

```
indirizzi alti
+----------------------+
|  buf[8..11]          |
|  buf[4..7]           |   ← contenuto del buffer (già allocato)
|  buf[0..3] = "AAAA"  |
+----------------------+
|  saved EBP           |   ← di vulnerable()
+----------------------+
|  return addr         |   ← di vulnerable()
+----------------------+
|  &buf                |   ← argomento di printf (PUSH'ato prima della call)
+----------------------+
|  ret addr di printf  |
+----------------------+  ← ESP qui dentro printf
indirizzi bassi
```

Il puntatore interno di printf parte **subito dopo `&buf`** (dove ci sarebbero gli argomenti variadici) e sale verso l'alto.

Quanti `%x` per arrivare a `buf[0..3]`?

|`%x` n.|Cosa legge|
|---|---|
|1°|`saved EBP` di vulnerable()|
|2°|`return addr` di vulnerable()|
|3°|`buf[0..3]` = **"AAAA"** → stampa `41414141` ✓|

In **questo specifico caso** servono 3 `%x` — ma è una coincidenza del layout, non perché il buffer è 12 byte. Sarebbero stati 3 `%x` anche con un buffer da 100 byte, perché la distanza è data dalle cose **tra** il punto di partenza di printf e il buffer (saved EBP, return addr).

---

## Cosa cambia con la dimensione del buffer

La dimensione del buffer determina **quanti `%x` consecutivi puoi fare dentro il buffer** una volta arrivato:

```
Buffer 12 byte = 3 dword:
   %3$x → buf[0..3]  = "AAAA" 
   %4$x → buf[4..7]  ← contenuto del buffer
   %5$x → buf[8..11] ← contenuto del buffer
   %6$x → STAI USCENDO dal buffer, leggi quello che c'è dopo
```

Quindi il buffer da 12 byte permette di "navigare" 3 dword **dentro** il buffer prima di uscire. Se metti indirizzi crafted dentro il buffer, ognuno occupa una dword e quindi un offset disponibile.

---

## Riassunto della logica corretta

|Tua frase|Versione corretta|
|---|---|
|"printf mette nello stack tutti i 12 byte"|Il buffer era già sullo stack come local; printf riceve solo `&buf`|
|"Mi servono 3 %x per raggiungere il valore del mio buffer"|Servono X `%x` per raggiungere il buffer, dove X **dipende dal layout dello stack**, non dalla size del buffer|
|"Il 3° %x mi mostra i 4 byte scritti"|Il **X-esimo** %x (qualunque sia X per quel programma) ti mostra i primi 4 byte del buffer|

Il modo pratico di scoprirlo è proprio quello del messaggio precedente: metti "AAAA" all'inizio del tuo input, butti tanti `%x` finché non vedi `41414141` nell'output. Il numero progressivo di quel `%x` è il tuo offset, e dipende da quel programma specifico.

# DOMANDA: se continuo un altra volta trovo il | ret addr di printf?

Bella domanda — e qui mi tocca correggermi. Il diagramma che avevo dato sopra era impreciso. Lo rifaccio fatto bene.

## Il layout corretto

Quando una funzione standard alloca locali e poi chiama printf, l'ordine in memoria è:

```
indirizzi alti
+----------------------+
| ret addr (caller     |
|  di vulnerable())    |  ← dove vulnerable() tornerà
+----------------------+
| saved EBP            |  ← saved dal prologue di vulnerable()
+----------------------+
| buf[8..11]           |  
| buf[4..7]            |  ← buf è una local, va SOTTO saved EBP
| buf[0..3] = "AAAA"   |     (locals sono a offset negativi da EBP)
+----------------------+
| &buf                 |  ← arg di printf, push'ato PRIMA della call
+----------------------+
| ret addr             |  ← push'ato dalla CALL printf (= dove printf torna)
+----------------------+
| saved EBP            |  ← saved dal prologue di printf
+----------------------+  ← ESP/EBP dentro printf
| ... locals di printf |
indirizzi bassi
```

L'errore nel mio diagramma precedente era che avevo messo `saved EBP` e `return addr di vulnerable()` **sotto** buf — invece stanno **sopra** buf, perché le local di una funzione sono sempre a indirizzi più bassi del saved EBP.

## La risposta alla tua domanda

Il puntatore interno di printf parte subito sopra `&buf` (dove cominciano gli argomenti variadici teorici) e **sale**, verso indirizzi più alti. Quindi:

```
%x #1  → buf[0..3] = AAAA  ← già qui!
%x #2  → buf[4..7]
%x #3  → buf[8..11]
%x #4  → saved EBP di vulnerable()
%x #5  → ret addr al CALLER di vulnerable()   ← NON di printf
%x #6  → frame del chiamante, e così via verso l'alto
```

**Il "ret addr di printf" (l'indirizzo dove printf torna, cioè dentro vulnerable()) sta SOTTO `&buf`, e printf con `%x` va sempre nella direzione opposta — sale.** Non lo raggiungerai mai continuando con `%x` in più.

## Cosa raggiungi continuando

Continuando oltre il buffer trovi:

1. **saved EBP di vulnerable()** — utile per capire dove sta l'EBP del frame chiamante
2. **return address al chiamante di vulnerable()** — questo è **molto** interessante: leakando questo valore conosci dove sta il codice del programma in memoria, e quindi **bypassi ASLR dell'eseguibile**
3. Andando più su, frame ancora più "vecchi" — main(), libc startup, eventualmente memoria non mappata

## Per arrivare al ret address di printf

Servirebbe leggere "indietro" rispetto al format string, cosa che `%x` non può fare. Però:

- Con `%n` puoi **scrivere** a indirizzi specifici (incluso il ret addr che sta sotto), se conosci la sua location
- Per **leggere** indietro ti servirebbe un altro vettore (un secondo bug, o info leak da altra fonte)

In pratica, in un exploit reale, non hai bisogno di leakare il ret addr di printf — vuoi **sovrascriverlo** o sovrascrivere una GOT entry, e per quello `%n` ti basta perché scrivi tramite un indirizzo che metti tu nel buffer.

---

Scusa per il diagramma confuso prima — il principio del "le locals stanno sotto saved EBP, gli args della chiamata successiva stanno ancora più sotto" è la regola che devi tenere in mente per orientarti.