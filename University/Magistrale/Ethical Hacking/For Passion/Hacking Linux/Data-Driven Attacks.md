---

tags:

- exploitation
- memory-corruption
- buffer-overflow
- input-validation
- injection
- hacking-exposed-7
- data-driven-attacks aliases:
- data-driven attack
- memory corruption
- injection attacks
- parser exploitation

---

# Data-Driven Attacks — Sfruttare il Parsing di Input Non Fidato

## 1. Il concetto base

> Un attacco data-driven sfrutta il fatto che un servizio attivo **processa input controllato dall'attaccante** in modo improprio, causando comportamento non previsto.

L'attaccante non sfrutta una vulnerabilità di autenticazione né di autorizzazione — sfrutta il fatto che il **codice di parsing/processing** ha bug che si manifestano con input crafted appositamente.

> [!abstract] Il pattern universale **Untrusted input → parser/processor → validazione insufficiente o assente → comportamento errato → controllo da parte dell'attaccante**
> 
> È il pattern che hai già visto in altre forme:
> 
> - [[Browser Attack]] — parser di pagine web → RCE nel renderer
> - [[Promiscuous Mode Attacks]] — parser di pacchetti → RCE nel sniffer
> - **Data-driven attacks** è il termine _generale_ di cui browser/sniffer sono istanze specifiche

---

## 2. Le due famiglie principali

```
Data-driven attacks
├── Memory corruption          ← bug nel linguaggio (C/C++ unsafe)
│   ├── Buffer overflow
│   ├── Format string
│   ├── Integer overflow
│   ├── Use-after-free
│   └── Off-by-one
│
└── Input validation           ← bug nella logica applicativa
    ├── SQL injection
    ├── Command injection
    ├── Path traversal
    ├── XXE (XML External Entity)
    ├── SSRF
    ├── LDAP injection
    └── Template injection (SSTI)
```

**Memory corruption** = il bug è a livello di gestione memoria (puntatori, bounds, lifetime). **Input validation** = il bug è a livello di logica applicativa (dato non sanitizzato finisce in un contesto pericoloso).

Spesso confluiscono: una input validation che permette codice arbitrario nel SQL è simile concettualmente a un buffer overflow che permette codice arbitrario in memoria. Il principio è lo stesso: **il dato attraversa il confine tra "dato" e "codice"**.

---

## 3. Memory corruption — perché C/C++ sono vulnerabili

Linguaggi safe (Java, Python, Go, Rust, JavaScript) hanno **bounds checking** integrato — se scrivi oltre la fine di un array, ricevi un'eccezione invece di corrompere memoria adiacente.

C e C++ non hanno bounds checking di default per ragioni di performance — un `memcpy` o un `strcpy` scrive ciecamente quanto gli dici senza controllare se c'è spazio.

```c
char buf[16];
strcpy(buf, input);   // se input > 16 byte → buffer overflow
                     // memoria adiacente sovrascritta
```

Quel singolo `strcpy` è la radice storica di una percentuale enorme di tutte le CVE mai scritte.

> [!warning] La maledizione del C Linus stesso ha detto che la più grande limitazione di Linux è essere scritto in C. Un linguaggio progettato nel 1972 per macchine con 64KB di RAM, che richiede al programmatore di gestire manualmente lifetime e bounds della memoria, finisce per produrre bug di memoria a ritmo industriale anche con sviluppatori esperti.

---

## 4. Stack-based buffer overflow — l'archetipo

### Layout dello stack

Quando una funzione viene chiamata, lo stack contiene (semplificato):

```
+----------------------+   indirizzi alti
|  Argomenti           |
+----------------------+
|  Return address      |   ← dove tornare quando la funzione finisce
+----------------------+
|  Saved frame pointer |
+----------------------+
|  Variabili locali    |   ← qui sta buf[16]
|  (buf[16])           |
+----------------------+   indirizzi bassi
```

Se scrivi oltre i 16 byte di `buf`, **sovrascrivi il return address**. Quando la funzione ritorna, il processore salta all'indirizzo che hai scritto.

### L'attacco classico

```
1. Attaccante invia 16 byte + 8 byte di indirizzo arbitrario
2. Buffer overflow sovrascrive il return address
3. Funzione ritorna → CPU salta dove vuole l'attaccante
4. Se può eseguire codice in quel punto → RCE
```

### Dal crash a RCE — l'evoluzione

|Era|Tecnica|Mitigazione che l'ha resa difficile|
|---|---|---|
|**Anni '90**|Shellcode sullo stack|DEP/NX rende lo stack non eseguibile|
|**Primi 2000**|Return-to-libc|ASLR randomizza gli indirizzi|
|**Metà 2000**|ROP (Return Oriented Programming)|CFI, control flow integrity|
|**Oggi**|JOP, COOP, exploit chain|Sandboxing, memory tagging (ARM MTE)|

Ogni mitigazione è stata bypassata da una tecnica nuova. È un gioco del gatto e topo continuo.

---

## 5. Heap-based buffer overflow

Più complesso dello stack overflow. Il principio è simile ma il bersaglio è **diverso**: invece del return address sovrascrivi **metadati dell'allocatore** (chunk headers, free list pointers, vtable pointer di oggetti C++).

Sfruttabile per:

- Sovrascrivere vtable → controllo di chiamate virtuali
- Sovrascrivere puntatori a funzione
- Tecniche tipo House of Spirit, House of Force, House of Mind (sfruttamento avanzato di glibc)

Molto più "artigianale" — ogni vulnerabilità richiede tecniche specifiche per quella particolare implementazione di allocator.

---

## 6. Format string vulnerability

```c
printf(user_input);    // VULNERABILE
printf("%s", user_input);  // SICURO
```

Se `user_input` contiene `%s`, `%x`, `%n`, `printf` legge argomenti che non gli hai passato — leggendo dallo stack ciò che capita. Con `%n` scrive in memoria.

Più rara oggi (compilatori warning), ma esiste ancora.

---

## 7. Integer overflow

```c
int size = user_size + 16;       // se user_size = INT_MAX → wraparound
char *buf = malloc(size);        // alloca pochi byte invece di tanti
memcpy(buf, data, user_size);    // overflow nel chunk allocato
```

Numerico → memoria. Spesso usato per portare a buffer overflow indirettamente.

Caso famoso: **CVE-2002-0639 (OpenSSH)** — integer overflow nel challenge response.

---

## 8. Use-after-free

```c
char *p = malloc(100);
free(p);
// ...
*p = 'A';   // USE AFTER FREE — accesso a memoria liberata
```

Tra `free` e l'uso successivo, l'allocator può aver dato quella memoria a qualcun altro. Scrivere lì significa corrompere strutture di un altro oggetto.

**Una delle classi più comuni nei browser** — gestione lifetime di oggetti DOM è notoriamente complessa. La mitigazione MiraclePtr di Chrome (citata in [[browser_attack]]) è specificamente contro questa classe.

---

## 9. Off-by-one

Il classico bug del C:

```c
char buf[10];
for (int i = 0; i <= 10; i++)  // BUG: dovrebbe essere < 10
    buf[i] = data[i];          // scrive 1 byte oltre il buffer
```

Un solo byte fuori posto basta per sovrascrivere il low byte del saved frame pointer o un puntatore vtable. Frequente, sottovalutato.

---

## 10. Mitigazioni moderne contro memory corruption

|Mitigazione|Cosa fa|Bypass|
|---|---|---|
|**Stack canary**|Valore casuale prima del return address — controllato prima di ritornare|Info leak della canary, brute force su processi forkati|
|**DEP / NX**|Pagine di memoria non eseguibili (stack/heap)|Return-to-libc, ROP|
|**ASLR**|Randomizza indirizzi base (libreria, stack, heap, exe)|Info leak, parziale ASLR su 32-bit|
|**PIE**|Eseguibili a position-independent (ASLR sull'exe stesso)|Stesso bypass di ASLR|
|**RELRO**|Tabella di relocation read-only dopo init|Necessario un altro bug|
|**Fortify Source**|Compilatore inserisce check su funzioni note (`strcpy`, ...)|Solo dove il compilatore può inferire la dimensione|
|**CFI**|Control Flow Integrity — salti indiretti validati|Tecniche JOP/COOP residue|
|**Memory tagging** (ARM MTE)|Tag su puntatori e memoria, mismatch = crash|Hardware moderno, ancora poco diffuso|
|**Linguaggi safe** (Rust, Go)|Bounds checking + ownership|Solo per codice nuovo|

> [!tip] Verifica mitigazioni su un binario Linux
> 
> ```bash
> checksec --file=/path/to/binary
> # Mostra: NX, PIE, RELRO, Canary, Fortify
> ```

---

## 11. Input validation attacks — la seconda famiglia

Qui il bug **non** è di memoria — è logico. Il dato dell'utente attraversa il confine tra "dato" e "codice" perché viene interpretato in un contesto che non doveva.

### SQL Injection

```python
# VULNERABILE
query = f"SELECT * FROM users WHERE name = '{username}'"
# Se username = "' OR 1=1 --"
# Diventa: SELECT * FROM users WHERE name = '' OR 1=1 --'
```

Il dato (username) diventa **codice SQL**. Fix: prepared statement / parameterized query.

### Command Injection

```python
# VULNERABILE
os.system(f"ping {ip}")
# Se ip = "8.8.8.8; cat /etc/passwd"
# Esegue ping E cat
```

Il dato (ip) diventa **comando shell**. Fix: passare argomenti come array, no shell.

### Path Traversal

```python
# VULNERABILE
open(f"/var/www/uploads/{filename}")
# Se filename = "../../etc/passwd"
# Apre /etc/passwd
```

Il dato (filename) diventa **path arbitrario**. Fix: validare/normalizzare path, chroot.

### XXE (XML External Entity)

```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
```

Se il parser XML resolve entità esterne → legge file arbitrari. Fix: disabilitare entità esterne nel parser.

### SSRF (Server-Side Request Forgery)

L'app fetcha un URL fornito dall'utente. L'utente fornisce un URL interno (`http://localhost:6379`, `http://169.254.169.254/` per cloud metadata).

Fix: whitelist di domini, blocco di IP privati/loopback.

### LDAP Injection

```python
# VULNERABILE
filter = f"(uid={username})"
# Se username = "*)(uid=*"
# Diventa: (uid=*)(uid=*)
```

Bypass di autenticazione tramite filtro LDAP malformato.

### Template Injection (SSTI)

```python
# VULNERABILE — Jinja2 con input utente nel template
template = "Hello {{ name }}"
render(template.replace("{{ name }}", user_input))
# Se user_input = "{{ 7*7 }}" → 49
# Se user_input = "{{ config.__class__.__init__.__globals__['os'].popen('id').read() }}" → RCE
```

Il dato (input) diventa **codice del template engine**. SSTI moderna è uno dei vettori più potenti su web app.

---

## 12. Il principio unificante

Tutti gli attacchi data-driven hanno la stessa struttura:

```
Dato dell'attaccante → arriva in un contesto che lo INTERPRETA come codice
   ├── Memoria → return address, vtable, allocator → corruzione runtime
   ├── SQL → query → manipolazione DB
   ├── Shell → comando → RCE
   ├── XML → entità → file read
   ├── Template → espressione → RCE
   └── LDAP → filtro → bypass auth
```

**Il dato non è mai stato realmente "solo dato"** — appena viene processato da un parser sufficientemente potente, può influenzare il flusso di esecuzione.

> [!abstract] Generalizzazione Più un parser è espressivo, più è probabile che input crafted possa influenzare il comportamento del programma. Difese principali: **input validation** (whitelist), **separazione contesti** (prepared statements, escape per output), **least privilege** (limita il blast radius), **linguaggi safe** (memory corruption preventiva).

---

## 13. Esempi storici notevoli

|Anno|CVE / Nome|Tipo|Note|
|---|---|---|---|
|1988|**Morris Worm**|Buffer overflow in fingerd|Primo worm di internet, 6000 sistemi|
|2001|**Code Red**|Buffer overflow IIS|350.000 sistemi in 14 ore|
|2003|**SQL Slammer**|Buffer overflow SQL Server|Velocità di propagazione storica|
|2014|**Heartbleed** (CVE-2014-0160)|Buffer over-read OpenSSL|Leak di memoria di processi server|
|2014|**Shellshock** (CVE-2014-6271)|Command injection Bash|RCE remoto via CGI|
|2017|**EternalBlue** (CVE-2017-0144)|Buffer overflow SMB|WannaCry, NotPetya|
|2021|**Log4Shell** (CVE-2021-44228)|Template injection / JNDI|Sfruttamento globale immediato|
|2023|**libwebp** (CVE-2023-4863)|Heap overflow decoder|0-click universale, già citato in [[browser_attack]]|

---

## 14. Difese pratiche

### Lato sviluppo

- **Linguaggi safe** per nuovo codice (Rust per system code, Go per servizi)
- **Input validation** rigorosa (whitelist, no blacklist)
- **Prepared statements** per ogni query DB
- **Output encoding** context-aware (HTML escape vs URL encode vs SQL escape)
- **Static analysis** in CI (Coverity, Semgrep, CodeQL)
- **Fuzzing** continuo (libfuzzer, AFL++)

### Lato deploy

- **Tutte le mitigazioni** (NX, ASLR, PIE, canary, RELRO)
- **Sandboxing** (seccomp, AppArmor, container)
- **Least privilege** — servizi non come root
- **Network segmentation** — limita il blast radius
- **WAF** per attacchi web noti (mitigazione, non difesa)

### Lato monitoring

- **Logging** input anomali
- **EDR/XDR** per detection di pattern di exploitation
- **Patch management** — la più importante: Log4Shell, EternalBlue, Heartbleed sono stati sfruttati massivamente perché molti non hanno patchato in tempo

---

## Takeaways

1. **Data-driven attack** è il termine ombrello per **memory corruption** + **input validation** attacks
2. Il pattern universale: **dato attaccante → parser → confine dato/codice sfumato → controllo**
3. Memory corruption (C/C++) ha origine storica nei language design senza bounds checking
4. Le mitigazioni moderne (NX, ASLR, PIE, canary, CFI) **non eliminano** i bug — alzano il costo dell'exploitation
5. Input validation attacks sono **logici**, indipendenti dal linguaggio: SQLi su Python, Java, PHP funziona se la query è concatenata
6. La differenza pratica: **memory corruption** richiede expertise (ROP, bypass), **input validation** è spesso oneshot
7. **Browser attack** e **promiscuous mode attack** sono istanze di data-driven attack — parser complesso + input non fidato
8. Difesa stratificata: linguaggi safe + validazione + mitigation + monitoring + patch

---

## Wiki-links

- [[browser_attack]]
- [[promiscuous_mode_attacks]]
- [[sql_injection]]
- [[command_injection]]
- [[path_traversal]]
- [[xxe]]
- [[ssrf]]
- [[ssti]]
- [[buffer_overflow]]
- [[heap_exploitation]]
- [[rop_return_oriented_programming]]
- [[ASLR]]
- [[stack_canary]]
- [[heartbleed]]
- [[shellshock]]
- [[log4shell]]
- [[hacking_exposed_7_unix]]