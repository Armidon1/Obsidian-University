---
title: Reimplementare codice decompilato in Python
aliases:
  - CB — Reimplementare codice decompilato in Python
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - python
  - ida
---

# Reimplementare codice decompilato in Python

> [!summary] In breve
> Molte challenge di reversing si risolvono **riscrivendo in Python quello che IDA mostra in C**, con gli stessi dati estratti dal binario, e facendo fare a Python il calcolo. Se il programma *produce* la flag basta rifare lo stesso calcolo; se il programma *controlla* l'input bisogna **invertire** le operazioni. In entrambi i casi bisogna riprodurre fedelmente il C: tipi, ordine dei byte e overflow.

## Il metodo

| Passo | Cosa fare | Strumenti |
|---|---|---|
| 1. Individuare l'algoritmo | la funzione che trasforma i dati (spesso nascosta: nomi simili a quelli di sistema, `.init_array`) | IDA: `X` sulle variabili interessanti, [[init_array e fini_array]] |
| 2. Sistemare i tipi | finché i tipi sono sbagliati, il decompilato è illeggibile | `Y` in IDA, [[Struct in IDA]] |
| 3. Estrarre i dati | globali con `Shift+E`; locali dal decompilato o da GDB | [[Esportare Dati da IDA]], [[pwndbg]] |
| 4. Tradurre i tipi | C → Python | tabella sotto |
| 5. Tradurre il codice riga per riga | stessi cicli, stessi operatori | tabella sotto |
| 6. Riprodurre l'overflow del C | mascherare con `& 0xFF`, `& 0xFFFFFFFF`, … | sezione *Overflow* |
| 7. Verificare | confrontare un valore intermedio con il programma vero | `print(x.hex(" "))` contro `x/25bx` in GDB |

## Esempio completo: Sn4k3

Una funzione dal nome ingannevole, `register_tm_clone` (quella vera di GCC è `register_tm_clones`, con la *s*), modifica l'array globale `food` prima che il gioco parta. Dopo aver corretto il tipo di `v2` con `Y` → `unsigned char v2[25]`, il decompilato è:

```c
unsigned __int8 v2[25];
*(_QWORD *)v2      = 0x424CB3416888AB53;
*(_QWORD *)&v2[8]  = 0xA1BC8955975EACA9;
*(_QWORD *)&v2[16] = 0xF807A4EA7B5AD56;
v2[24] = 66;
for (i = 5; i <= 29; ++i)
    food[i] -= v2[i - 5] ^ 0x42;
```

> [!warning] Prima di correggere il tipo
> IDA aveva mostrato `_QWORD v2[3]` più una `char v3` separata, con valori come `'BL\xB3Ah\x88\xABS'`. Non erano stringhe: erano costanti da 8 byte mostrate come caratteri, e **in ordine invertito** rispetto alla memoria. L'indizio che fosse un array di byte era l'uso: `*((_BYTE *)v2 + i - 5)`, letto un byte alla volta per 25 byte.

`food` è globale (`_BYTE food[30]` in `.data`): si esporta con `Shift+E` → *hex string*. `v2` è locale, quindi si ricostruisce dalle costanti.

```python
import struct

food = bytearray.fromhex("636369747B7448335F623373745F536E346B335F31735F70597468306E7D")
key  = struct.pack("<QQQ", 0x424CB3416888AB53,
                           0xA1BC8955975EACA9,
                           0x0F807A4EA7B5AD56) + bytes([0x42])

for i in range(5, 30):                                   # for (i = 5; i <= 29; ++i)
    food[i] = (food[i] - (key[i - 5] ^ 0x42)) & 0xFF     # food[i] -= v2[i-5] ^ 0x42

print(food.decode())
```

> [!note] L'esca
> Il contenuto originale di `food`, letto in IDA con `R`, è già una flag leggibile: è un'**esca**. La flag vera è quella che si ottiene *dopo* la trasformazione.

### Riga per riga

- **`bytearray.fromhex(...)`**: `"63"` → byte `0x63`, ecc. Si usa `bytearray` e non `bytes` perché `bytes` non si può modificare, mentre il ciclo deve scrivere dentro `food[i]`.
- **`struct.pack("<QQQ", ...)`**: scrive tre interi come byte. `<` = **little-endian** (come x86: il byte meno significativo per primo), `Q` = intero senza segno da 8 byte (`_QWORD`). Fa da solo l'inversione dei byte che altrimenti andrebbe fatta a mano.
- **`0x0F807A4EA7B5AD56`**: IDA scrive `0xF807A4EA7B5AD56`, con 15 cifre. Lo zero iniziale è sottinteso, e mancarlo sposta tutti i byte.
- **`+ bytes([0x42])`**: aggiunge il 25° byte (`v2[24] = 66` = `0x42`). `bytes([...])` crea dei byte da una lista di numeri, `+` concatena.
- **`range(5, 30)`**: `range` **esclude** l'estremo finale, quindi `i <= 29` diventa `30`.
- **`(food[i] - (key[i - 5] ^ 0x42)) & 0xFF`**: le parentesi attorno allo XOR sono obbligatorie (vedi *Precedenza* sotto); `& 0xFF` riproduce l'overflow di un byte.
- **`food.decode()`**: da byte a testo; `print(food)` stamperebbe `bytearray(b'...')`.

## Tradurre i tipi

| C / IDA | Python |
|---|---|
| `char buf[N]`, `_BYTE arr[N]` | `bytearray(...)` (modificabile) o `bytes(...)` |
| `int arr[N]` esportato | lista di `int`; se arriva come byte: `struct.unpack("<%di" % N, data)` |
| `_QWORD`, `__int64` costante | `struct.pack("<Q", x)` oppure `x.to_bytes(8, "little")` |
| `_DWORD`, `int` | `"<I"` / `"<i"` oppure `x.to_bytes(4, "little")` |
| `_WORD`, `short` | `"<H"` / `"<h"` |
| byte da un intero | `bytes([x])` |
| intero da byte | `int.from_bytes(b, "little")` |
| stringa C | `b"..."` (Python non aggiunge lo `\0` finale) |

Formati di `struct`: `B`/`b` = 1 byte, `H`/`h` = 2, `I`/`i` = 4, `Q`/`q` = 8 (maiuscola = senza segno). `<` = little-endian, `>` = big-endian.

## Tradurre gli operatori

| C | Python | Attenzione |
|---|---|---|
| `for (i = a; i < b; i++)` | `for i in range(a, b)` | con `<= b` diventa `range(a, b + 1)` |
| `for (i = a; i > b; i--)` | `for i in range(a, b, -1)` | |
| `x ^ y`, `x & y`, `x \| y` | uguali | |
| `~x` | `~x & 0xFF` (o la maschera della dimensione) | in Python `~x` è negativo |
| `x << n` | `(x << n) & MASK` | in Python non si perdono bit a sinistra |
| `x >> n` (unsigned) | `x >> n` | |
| `x / y` (interi) | `x // y` | con numeri negativi il C tronca verso zero: `int(x / y)` |
| `x % y` | `x % y` | con negativi i risultati differiscono |
| `a -= b ^ c` | `a = a - (b ^ c)` | il C calcola prima tutta la parte destra |
| `__ROL1__(x, n)` | `((x << n) \| (x >> (8 - n))) & 0xFF` | rotazione su 8 bit (16/32/64: cambiare 8 e la maschera) |
| `__ROR1__(x, n)` | `((x >> n) \| (x << (8 - n))) & 0xFF` | |

> [!warning] Precedenza: `-` prima di `^`
> Sia in C che in Python `-` e `+` hanno precedenza **più alta** di `^`, `&` e `|`. Quindi `a - b ^ c` vuol dire `(a - b) ^ c`. Nel dubbio, si mettono le parentesi esattamente come raggruppa IDA.

## Overflow: le maschere

In C un `unsigned char` va da 0 a 255: `0x10 - 0x20` dà `0xF0`, perché il valore "gira". In Python gli interi non hanno limiti e `0x10 - 0x20` dà `-16`. La maschera tiene solo i bit della dimensione giusta:

| Tipo C | Maschera |
|---|---|
| 1 byte (`char`, `_BYTE`) | `& 0xFF` |
| 2 byte (`short`, `_WORD`) | `& 0xFFFF` |
| 4 byte (`int`, `_DWORD`) | `& 0xFFFFFFFF` |
| 8 byte (`__int64`, `_QWORD`) | `& 0xFFFFFFFFFFFFFFFF` |

`-16 & 0xFF` = `0xF0`, come in C. Senza maschera, un `bytearray` dà `ValueError: byte must be in range(0, 256)`.

Per un tipo **con segno** (`int`, `char` signed), dopo la maschera si riconverte: `x - 0x100 if x >= 0x80 else x` (1 byte), `x - (1 << 32) if x >= (1 << 31) else x` (4 byte).

## Rifare o invertire?

| Il programma… | Cosa fare | Esempio |
|---|---|---|
| **produce** la flag (la calcola e la stampa, o la mette in memoria) | **rifare** lo stesso calcolo, nello stesso ordine | Sn4k3 |
| **controlla** l'input (`if (f(input) == target)`) | **invertire** `f`, partendo da `target` e andando all'indietro | crackme |

Per invertire si applicano le operazioni inverse **in ordine contrario**:

| Operazione | Inversa |
|---|---|
| `+ k` | `- k` (con maschera) |
| `- k` | `+ k` (con maschera) |
| `^ k` | `^ k` (lo XOR è l'inverso di sé stesso: `a ^ k ^ k = a`) |
| `ROL n` | `ROR n` |
| `* k` (mod 256) | `* pow(k, -1, 256)`, solo se `k` è dispari |
| scambio di posizioni (`out[p[i]] = in[i]`) | `in[i] = out[p[i]]` |

```c
// controllo nel binario
if ((((input[i] ^ key[i]) + 3) & 0xFF) != target[i]) fail();
```

```python
# inversione: prima si toglie il +3, poi lo XOR
flag = bytes(((target[i] - 3) & 0xFF) ^ key[i] for i in range(len(target)))
```

> [!tip] Se non si riesce a invertire: forza bruta per carattere
> Quando ogni carattere dell'output dipende da **un solo** carattere dell'input, si provano tutti i 256 valori per ogni posizione:
> ```python
> flag = bytearray()
> for i in range(len(target)):
>     for c in range(256):
>         if f(c, i) == target[i]:      # f = il calcolo copiato dal C
>             flag.append(c)
>             break
> ```
> Se invece ogni carattere dipende dai precedenti (es. `key = key * 31 + input[i]`), si procede in ordine, aggiornando lo stato dopo ogni carattere trovato. Per vincoli più complicati si usa un solver come **z3**.

## Verificare

Un byte sbagliato all'inizio (endianness, `range` sbagliato di uno, zero iniziale dimenticato) rovina tutto il risultato senza dare errori. Conviene controllare **i dati intermedi** prima del risultato finale:

```python
print(key.hex(" "))       # 53 ab 88 68 41 b3 4c 42 a9 ac ...
```

```text
pwndbg> breakrva <offset del ciclo>
pwndbg> x/25bx $rbp-0x30          # v2 come sta davvero in memoria
pwndbg> x/30bx &food              # food prima (e dopo, con un altro breakpoint) del ciclo
```

Se i byte coincidono, la traduzione è corretta. Spesso non serve nemmeno lo script: basta un breakpoint dopo il ciclo e `x/s &food`.

## Collegamenti

- **Concetti correlati**: [[Esportare Dati da IDA]] · [[Struct in IDA]] · [[Scorciatoie IDA]] · [[init_array e fini_array]] · [[pwndbg]]
- **Altra challenge con lo stesso schema**: [[Challenge 15+18]] (dati letti a runtime invece di ricostruire la trasformazione)
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> [[02 - CB - Reverse Engineering 1#Estrarre i dati|Lezione 2 — Estrarre i dati]]
