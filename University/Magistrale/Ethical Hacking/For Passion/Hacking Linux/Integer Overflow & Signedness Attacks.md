
---
## tags: [ethical-hacking, hacking-exposed-7, ch5, memory-corruption, data-driven, exam-prep] chapter: 5 exam: ETH-2026-06-05 related: [[data_driven_attacks]], [[format_string_attacks]]

# Integer Overflow & Signedness Attacks

> [!abstract] TL;DR Bug aritmetici nel codice C/C++ in cui un calcolo su interi produce un valore **sbagliato ma sintatticamente valido**. Il valore poi viene usato come **size** in `malloc`/`memcpy`/loop → memory corruption. Non è un buffer overflow "diretto": è un **buffer overflow generato a monte da matematica sbagliata**. Famiglia: vedi [[data_driven_attacks]].

---

## 1. Perché esistono: la matematica in C non è la matematica

In C gli interi hanno **dimensione fissa** (8/16/32/64 bit) e il linguaggio:

1. **Non rileva overflow** a runtime (per `unsigned` è UB-free wraparound, per `signed` è UB ma in pratica wrappa).
2. Fa **conversioni implicite** tra signed/unsigned e tra tipi di larghezza diversa.
3. Non distingue semanticamente "lunghezza di un buffer" da "intero qualunque" — tutto è `int` o `size_t`.

Risultato: il programmatore scrive `a + b` aspettandosi la matematica delle elementari, ma ottiene una macchina modulare. **Il bug è invisibile a una code review superficiale** perché il codice "sembra giusto".

> [!tip] Analogia sysadmin È come `df -h` che mostra spazio disco come `uint32_t` su filesystem grossi: a un certo punto wrappa e ti dice che hai 2GB liberi mentre in realtà ne hai 6TB. Stesso identico pattern: tipo troppo piccolo per il valore reale.

---

## 2. Integer Overflow Attack

### 2.1 Meccanica

```c
unsigned int len1 = get_from_attacker();   // es. 0xFFFFFFF0
unsigned int len2 = get_from_attacker();   // es. 0x20
size_t total = len1 + len2;                // wrap → 0x10  (16 byte!)

char *buf = malloc(total);                  // alloca 16 byte
memcpy(buf,        data1, len1);            // copia ~4GB
memcpy(buf + len1, data2, len2);            // boom, heap già distrutto
```

Il check `if (total < MAX)` **passa** perché `total` è effettivamente piccolo dopo il wrap. La validazione c'è ma è inutile: sta validando il risultato corrotto.

### 2.2 Varianti

|Variante|Dove|Cosa succede|
|---|---|---|
|**Addition overflow**|`a + b`|wrap a un valore piccolo|
|**Multiplication overflow**|`count * sizeof(elem)`|classico in allocatori di array|
|**Truncation**|cast `int → short` o `size_t → int`|si perdono i bit alti|

> [!example] Multiplication overflow tipico
> 
> ```c
> void *xmalloc_array(size_t n, size_t size) {
>     return malloc(n * size);     // n*size wrappa → buffer minuscolo
> }
> ```
> 
> Per questo `calloc(n, size)` esiste ed è sicuro: controlla l'overflow internamente.

### 2.3 Casi reali

- **OpenSSH CVE-2002-0639** (challenge-response): `nresp * sizeof(char*)` overflow → heap overflow remoto pre-auth.
- **JPEG of Death (MS04-028, CVE-2004-0200)**: parser GDI+ calcolava dimensione comment field con overflow → buffer minuscolo, copia gigante. Bastava aprire un'immagine.
- **Linux kernel CVE-2009-1185** (udev): integer overflow in netlink parsing.

---

## 3. Signed Integer Attack (Signedness Bug)

### 3.1 Meccanica

Sfrutta la **doppia interpretazione** dello stesso pattern di bit:

- come `int` (signed): `0xFFFFFFFF` = `-1`
- come `size_t`/`unsigned`: `0xFFFFFFFF` = `4294967295`

```c
int len = read_user_input();              // attaccante manda -1
if (len > MAX_BUF) return -1;             // -1 > MAX_BUF? NO → check passa
if (len > sizeof(buf)) return -1;         // signed vs unsigned: promo a unsigned
                                          //   ma alcuni compilatori comparano signed → bypass
char buf[256];
memcpy(buf, data, len);                   // memcpy vuole size_t → -1 = 4GB
```

### 3.2 Il punto cruciale

Il confronto `len > MAX` può comportarsi diversamente a seconda dei tipi:

- Se `len` è `int` e `MAX` è `int` → confronto signed, `-1 < MAX`, **bypass**.
- Se uno dei due è `unsigned` → C promuove l'altro a unsigned, `-1` diventa `4GB`, check funziona.

Il bug nasce nell'**interfaccia tra API che usano tipi diversi** (e.g. `read()` ritorna `ssize_t`, ma il programmatore lo salva in `int`).

### 3.3 Casi reali

- **Apache mod_ssl CVE-2002-0653**: signedness bug in client cert handling.
- **Snort RPC preprocessor CVE-2003-0033**: lunghezza letta come signed, usata come unsigned.
- **FreeBSD telnetd, OpenSSH (multiple)**: pattern ricorrente nella parsing layer.

---

## 4. Tabella riassuntiva

| |Integer Overflow|Signedness Bug|Truncation|
|---|---|---|---|
|**Dove sta il bug**|Operazione aritmetica|Cast/confronto signed↔unsigned|Cast a tipo più stretto|
|**Cosa diventa errato**|Risultato del calcolo (wrap)|Interpretazione del valore|Bit alti persi|
|**Esempio trigger**|`a+b`, `n*size`|`if(len > MAX)` con `len` signed|`(short)(int_value)`|
|**Conseguenza tipica**|`malloc` undersize → heap overflow|check bypass → memcpy enorme|size sbagliata → corruption|
|**Pre/post check**|check passa su valore wrappato|check passa su valore negativo|check passa pre-cast|

---

## 5. Pattern universale (chiave per Q5)

Tutti e tre seguono lo stesso schema, che ricolleghiamo a [[data_driven_attacks]]:

```
input non fidato (lunghezza/contatore)
   ↓
operazione aritmetica O conversione di tipo
   ↓
valore "intermedio" che soddisfa i check
   ↓
stesso valore usato come SIZE in alloc/copia
   ↓
memory corruption (di solito heap)
```

> [!warning] Riconoscerlo in codice C Cerca questi indicatori in una funzione vulnerabile:
> 
> 1. Una lunghezza/contatore **arriva dall'esterno** (rete, file, argv).
> 2. C'è **aritmetica** su quel valore prima di un'allocazione.
> 3. C'è un **confronto** ma i tipi degli operandi sono misti o tutti signed.
> 4. Il valore finisce in `malloc`/`memcpy`/`strncpy`/`for(i=0; i<n; i++)`.
> 
> Se vedi 1+2+4 senza un check di overflow esplicito → **integer overflow**. Se vedi 1+3+4 con `int` invece di `size_t` → **signedness bug**.

---

## 6. Perché sono insidiosi

- **Nessun crash immediato**: il valore wrappato è valido come numero.
- **Compiler non avverte** di default (serve `-Wsign-compare`, `-Wconversion`).
- **Test funzionali passano**: serve un input ad hoc (numero gigante) per triggerare.
- **Code review fallisce**: il codice "sembra giusto", la matematica umana non wrappa.
- **Spesso pre-auth**: il parser della lunghezza è uno dei primi punti raggiungibili da remoto.

---

## 7. Mitigazioni

|Livello|Tecnica|
|---|---|
|**Codice**|Check esplicito: `if (a > SIZE_MAX - b) error;` prima di `a+b`|
|**API**|`calloc(n, size)` invece di `malloc(n*size)`; SafeInt (C++), `__builtin_add_overflow` (GCC/Clang)|
|**Tipi**|Usare **sempre** `size_t` per lunghezze, mai `int`. Niente conversioni implicite.|
|**Compiler**|`-ftrapv` (trap su signed overflow), `-fsanitize=integer` (UBSan), `-Wsign-compare`|
|**Linguaggio**|Rust ha overflow checks in debug, `checked_add`/`saturating_add` in release. Go panicka su overflow nei tipi sized.|
|**Static analysis**|Coverity, CodeQL, Clang Static Analyzer trovano pattern noti|
|**Runtime**|ASLR/DEP/canary **non aiutano** (sono mitigazioni post-corruption). Servono **prima**.|

> [!note] Punto sottile per l'esame ASLR e canary **non proteggono** dall'integer overflow di per sé. Proteggono dallo _sfruttamento_ del buffer overflow che ne consegue, ma la corruzione avviene comunque. Per questo le mitigazioni vere stanno a livello di linguaggio/compiler/codice, non di OS.

---

## 8. Takeaways

- **Integer overflow** = bug nella **matematica** (a+b o n*size wrappa) → buffer sottodimensionato.
- **Signedness bug** = bug nei **tipi/confronti** (-1 visto come 4GB) → check bypassato.
- Entrambi finiscono in **heap overflow** o **stack overflow** a valle, ma la radice è aritmetica.
- Sono **data-driven attacks** della famiglia memory corruption: il pattern è `input → math/cast → size → corruption`.
- **Riconoscimento**: aritmetica su input esterno + uso come size senza overflow check.
- **Mitigazione vera**: a livello di linguaggio o check espliciti. ASLR/DEP/canary sono mitigazioni a valle, non a monte.

---
## Esempi libro

### Basic example

```C
#include <stdio.h>
int main(int argc, char **argv) {
	long l = 0xdeadbeef;
	short s = l;
	char c = l;
	printf("long: %x\n", l);
	printf("short: %x\n", s);
	printf("char: %x\n", c);
	return(0);
}
```
On a 32-bit Intel platform, the output should be
long: deadbeef
short: ffffbeef
char: ffffffef

### Integer attack
```C
#include <stdio.h>
int get_user_input_length() { return 60000; };

int main(void) {
	int i;
	short len;
	char buf[256];
	char user_data[256];
	len = get_user_input_length();
	
	printf("%d\n", len);
	if(len > 256) {
		fprintf(stderr, "Data too long!");
		exit(1);
	}
	printf("data is less than 256!\n");
	strncpy(buf, user_data, len);
	buf[i] = '\0';
	printf("%s\n", buf);
	return 0;
}
```
And here’s the output of this example:
-5536
data is less than 256!
Bus error (core dumped)

### basic Signed attack
```C
static char data[256];

int store_data(char *buf, int len)
{
	if(len > 256)
	return -1;
	return memcpy(data, buf, len);
}
```

### actual signed attack vulnerable
```C
static bool_t
xdrmem_getbytes(XDR *xdrs, caddr_t addr, int len)
{
	int tmp;
	trace2(TR_xdrmem_getbytes, 0, len);
	if ((tmp = (xdrs->x_handy - len)) < 0) { // [1]
		syslog(LOG_WARNING,
		<omitted for brevity>
		
		return (FALSE);
	}
	xdrs->x_handy = tmp;
	xdrs->x_private += len;
	trace1(TR_xdrmem_getbytes, 1);
	return (TRUE);
}
```
If you haven’t spotted it yet, this integer overflow is caused by a signed/unsigned
mismatch. Here, len is a signed integer. As discussed, if a signed integer is converted to
an unsigned integer, any negative value stored within the signed integer is converted to a
large positive value when stored within the unsigned integer. Therefore, if we pass a
negative value into the xdrmem_getbytes() function for len, we bypass the check in
[1], and the memcpy() in [2] reads past the bounds of xdrs->x_private because the
third parameter to memcpy()automatically upgrades the signed integer len to an
unsigned integer, thus telling memcpy() that the length of the data is a huge positive
number. This vulnerability is not easy to exploit remotely because the different operating
systems implement memcpy() differently
## Wiki-links

- [[data_driven_attacks]] — famiglia generale
- [[format_string_attacks]] — altro classico Ch.5/Ch.10
- [[buffer_overflow]] — la corruzione a valle (se la nota esiste)
- [[heap_exploitation]] — per assignment opzionale post-esame