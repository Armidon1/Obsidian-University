---
title: Traduzione dei programmi C in linguaggio macchina
aliases:
  - SDC — Come viene tradotto in linguaggio macchina un programma C
  - Sistemi di Calcolo — Capitolo 3
tags:
  - sistemi-di-calcolo
  - assembly
  - ia32
  - x86-64
  - stack-frame
source: Dispensa Sistemi di Calcolo.pdf (cap. 3, pp. 36–75)
---

# Traduzione dei programmi C in linguaggio macchina

> [!abstract] Scopo del capitolo
> È il capitolo centrale della prima parte del corso. Descrive l'**ISA IA32** in sintassi **AT&T**: tipi di dato macchina, **registri**, **modi di indirizzamento**, **endianness**, istruzioni di movimento dati, aritmetico-logiche (con `LEA` e gli shift), di **salto** (condizionato, con i **condition code**) e di chiamata a funzione. Poi mostra come `gcc` traduce i costrutti C (`if`, `while`, `for`, funzioni, array, struct) e le convenzioni dell'**ABI System V**: **stack frame**, passaggio dei parametri, registri **caller-save** e **callee-save**, variabili locali. Chiude con le differenze di **x86-64**.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]]

## Astrazioni: memoria e ISA

I sistemi di calcolo si basano su **astrazioni** che danno una visione semplificata della macchina, nascondendo dettagli che in prima battuta si possono ignorare. Le due più importanti:

- la **memoria**, vista come un grande **array di byte**;
- l'**ISA** (*Instruction Set Architecture*, vedi [[ABI e ISA]]), che definisce:
  1. lo **stato** della CPU (registri, flag);
  2. il **formato** delle istruzioni;
  3. l'**effetto** delle istruzioni sullo stato.

I compilatori traducono il C basandosi su questa descrizione astratta. Due ISA molto diffuse:

- **IA32**: la famiglia x86 a **32 bit**;
- **x86-64**: la famiglia x86 a **64 bit**, ottenuta **estendendo** IA32, con cui è **retrocompatibile**. I programmi IA32 girano su x86-64, ma non vale il viceversa, perché x86-64 aggiunge istruzioni nuove.

La dispensa tratta IA32 e nel §3.3 elenca le differenze con x86-64. Per compilare a 32 bit su un sistema a 64 bit si usa `gcc -m32`.

_(dispensa, p. 36)_

## L'ISA IA32 in sintassi AT&T

> [!note] AT&T vs Intel
> Esistono due sintassi per l'assembly x86. Nella **AT&T** (quella di `gcc`/`objdump` e della dispensa) l'ordine è **sorgente, destinazione** (`movl %eax, %ebx` copia EAX in EBX), i registri hanno il prefisso `%`, le costanti il prefisso `$`, e la dimensione è indicata da un suffisso (`b`, `w`, `l`). Nella **Intel** (usata ad esempio da IDA e in [[2 - MA - X86 Assembly|Malware Analysis]]) l'ordine è **destinazione, sorgente** e non ci sono prefissi.

### Tipi di dato macchina

| Tipo macchina | Rappresentazione | Suffisso | Byte |
| --- | --- | --- | --- |
| Byte | intero | `b` | 1 |
| Word | intero | `w` | 2 |
| Double word | intero | `l` | 4 |
| Single precision | virgola mobile | `s` | 4 |
| Double precision | virgola mobile | `l` | 8 |
| Extended precision | virgola mobile | `t` | 12 (10 usati) |

Il **suffisso** si usa per indicare il **tipo degli operandi** di un'istruzione (`movb`, `movw`, `movl`).

> [!warning] Word
> In IA32 una "word" è di **2 byte** (eredità dell'8086 a 16 bit). Non va confusa con la "word" del bus del [[01 - SDC - Cosa è un sistema di calcolo#Bus|capitolo 1]], che indica la dimensione naturale dei dati trasferiti (4 o 8 byte).

### Corrispondenza tra tipi C e tipi macchina

| Tipo C | Tipo macchina | Suffisso | Byte |
| --- | --- | --- | --- |
| `char` | Byte | `b` | 1 |
| `short` | Word | `w` | 2 |
| `int` | Double word | `l` | 4 |
| `long` | Double word | `l` | 4 |
| `long long` | *non supportato* | – | 8 |
| puntatore | Double word | `l` | 4 |
| `float` | Single precision | `s` | 4 |
| `double` | Double precision | `l` | 8 |
| `long double` | Extended precision | `t` | 12 (10 usati) |

- `long long` **non è supportato nativamente** da IA32: il compilatore lo emula con coppie di registri.
- Interi **con e senza segno** hanno lo **stesso tipo macchina** (`char` e `unsigned char` sono entrambi Byte). La differenza sta solo nelle **istruzioni** che li manipolano (es. `movz` vs `movs`, salti `ja` vs `jg`).

_(dispensa, pp. 36–37)_

### Registri

Vedi [[Registri IA32]].

I **registri** sono memorie velocissime dentro la CPU; in assembly hanno **nomi simbolici** e si usano come variabili. IA32 ha **8 registri interi a 32 bit**: A, B, C, D, DI, SI, SP, BP. I primi 6 si possono usare liberamente per interi e puntatori; **SP** e **BP** hanno usi particolari (stack pointer e base pointer).

![[SDC-p038-1.png]]

Si può accedere a parti di un registro con nomi diversi (byte₀ è il meno significativo). Per A:

- `%eax`: i 4 byte (byte₃…byte₀);
- `%ax`: i 2 byte meno significativi (byte₁, byte₀);
- `%al`: il byte meno significativo (byte₀);
- `%ah`: il secondo byte meno significativo (byte₁).

Lo stesso vale per B, C, D (`%ebx/%bx/%bh/%bl`…). Per **DI, SI, BP, SP** non si può accedere a un singolo byte (solo `%edi`/`%di`, ecc.).

Altri registri:

- **EIP**: 32 bit, contiene l'indirizzo della **prossima istruzione** da eseguire (*program counter* o *instruction pointer*);
- **EFLAGS**: 32 bit, lo **stato** del processore (*status register*), che contiene tra l'altro i condition code;
- registri per virgola mobile e calcolo vettoriale (non trattati).

_(dispensa, pp. 38–39)_

### Operandi e modi di indirizzamento

Vedi [[Modi di Indirizzamento]].

Le istruzioni hanno in genere un **operando sorgente** (valore di ingresso) e un **operando destinazione** (dove scrivere il risultato).

- Sorgente: **immediato** (costante codificata nell'istruzione stessa), **registro**, **memoria**.
- Destinazione: solo **registro** o **memoria** (un immediato non può essere una destinazione).

Notazione: `R[E]` = contenuto del registro E; `M_b[x]` = oggetto di b byte all'indirizzo x.

| Tipo | Sintassi | Valore denotato | Nome |
| --- | --- | --- | --- |
| Immediato | `$imm` | `imm` | immediato |
| Registro | `E` | `R[E]` | registro |
| Memoria | `imm` | `M[imm]` | assoluto |
| Memoria | `(Eb)` | `M[R[Eb]]` | indiretto |
| Memoria | `imm(Eb)` | `M[imm+R[Eb]]` | base e spiazzamento |
| Memoria | `(Eb,Ei)` | `M[R[Eb]+R[Ei]]` | base e indice |
| Memoria | `imm(Eb,Ei)` | `M[imm+R[Eb]+R[Ei]]` | base, indice e spiazzamento |
| Memoria | `(,Ei,s)` | `M[R[Ei]·s]` | indice e scala |
| Memoria | `imm(,Ei,s)` | `M[imm+R[Ei]·s]` | indice, scala e spiazzamento |
| Memoria | `(Eb,Ei,s)` | `M[R[Eb]+R[Ei]·s]` | base, indice e scala |
| Memoria | `imm(Eb,Ei,s)` | `M[imm+R[Eb]+R[Ei]·s]` | base, indice, scala e spiazzamento |

La forma generale è quindi

$$\text{indirizzo} = imm + R[E_{base}] + R[E_{indice}] \cdot s, \qquad s \in \{1, 2, 4, 8\}$$

e tutte le altre ne sono casi particolari. `imm` è una costante intera a 32 bit (es. `-24` o `0xAF25CB7E`). Si usano $S_n$ e $D_n$ per un operando sorgente/destinazione di n byte.

> [!tip] Perché esiste la forma con scala
> `(base, indice, scala)` corrisponde esattamente all'accesso `a[i]` di un array con elementi da 1, 2, 4 o 8 byte: `base` = indirizzo di `a`, `indice` = `i`, `scala` = `sizeof(elemento)`. Vedi [[#Array e aritmetica dei puntatori]].

_(dispensa, pp. 39–40)_

### Endianness

Vedi [[Endianness]].

L'**endianness** è l'ordine con cui vengono disposti in memoria i byte di un valore numerico:

- **big-endian**: il byte **più** significativo all'indirizzo più basso (stesso ordine con cui si scrive il numero);
- **little-endian**: il byte **meno** significativo all'indirizzo più basso.

![[SDC-p040-1.png]]

L'intero `0x12345678` all'indirizzo `0x100`: in big-endian i byte sono `12 34 56 78`, in little-endian `78 56 34 12`. **x86 è little-endian**; PowerPC e SPARC sono big-endian. Lo si nota leggendo un dump di memoria con `gdb` o `objdump`: gli interi appaiono "al contrario".

_(dispensa, p. 40)_

## Istruzioni di movimento dati

Copiano byte da memoria a registro, da registro a registro e da registro a memoria. `X:Y` indica la concatenazione delle cifre (es. `A3F:C07` = `A3FC07`).

### MOV: stessa dimensione

| Istruzione | Effetto | Descrizione |
| --- | --- | --- |
| `movb S1,D1` | D₁ ← S₁ | copia 1 byte |
| `movw S2,D2` | D₂ ← S₂ | copia 2 byte |
| `movl S4,D4` | D₄ ← S₄ | copia 4 byte |

### MOVZ e MOVS: destinazione più grande

Servono a copiare un valore in una destinazione **più grande**, cioè a fare le **conversioni** tra tipi interi:

- **MOVZ** (*zero extend*): riempie i byte in più con **zeri**. È la conversione per tipi **senza segno**.
- **MOVS** (*sign extend*): riempie i byte in più con il **bit di segno** (il più significativo) della sorgente. È la conversione per tipi **con segno**, e preserva il valore in complemento a 2.

| Istruzione | Effetto |
| --- | --- |
| `movzbw S1,D2` | D₂ ← 0x00:S₁ |
| `movzbl S1,D4` | D₄ ← 0x000000:S₁ |
| `movzwl S2,D4` | D₄ ← 0x0000:S₂ |
| `movsbw S1,D2` | D₂ ← 0xMM:S₁ |
| `movsbl S1,D4` | D₄ ← 0xMMMMMM:S₁ |
| `movswl S2,D4` | D₄ ← 0xMMMM:S₂ |

con `M` = `F` se il bit di segno della sorgente è 1, `0` altrimenti.

Esempi con `%eax=0x12341234`, `%ecx=0xABCDEFAB`:

| Istruzione | Risultato |
| --- | --- |
| `movzbw %al,%cx` | `%ecx=0xABCD0034` (cambiano solo i 16 bit bassi) |
| `movzbl %al,%ecx` | `%ecx=0x00000034` |
| `movzwl %ax,%ecx` | `%ecx=0x00001234` |

Con `%ecx=0xABCDE1E2`:

| Istruzione | Risultato |
| --- | --- |
| `movsbw %cl,%ax` | `%eax=0x1234FFE2` (0xE2 ha il bit di segno a 1) |
| `movsbl %cl,%eax` | `%eax=0xFFFFFFE2` |
| `movswl %cx,%eax` | `%eax=0xFFFFE1E2` |

> [!warning] Correzione
> Nella dispensa la seconda tabella di esempi di `MOVS` (p. 42: `movsbw %al,%cx` → `0xABCD0034`, …) riporta gli stessi risultati di `MOVZ`. I valori sono comunque corretti, perché `0x34` ha il bit di segno a 0 e quindi l'estensione con segno coincide con quella con zeri. Gli esempi significativi sono quelli con `%cl = 0xE2` (p. 43).

> [!note] Nome nella sintassi Intel
> In sintassi Intel queste istruzioni si chiamano **MOVSX** e **MOVZX**; `MOVS` in Intel è un'altra istruzione (copia di stringhe).

### PUSH e POP

Spostano dati da/verso la **cima dello stack**. Lo stack cresce verso **indirizzi bassi**, e `%esp` punta all'ultimo elemento inserito.

| Istruzione | Effetto | Descrizione |
| --- | --- | --- |
| `pushl S4` | `R[%esp] ← R[%esp]-4`; `M[R[%esp]] ← S4` | mette 4 byte in cima allo stack |
| `popl D4` | `D4 ← M[R[%esp]]`; `R[%esp] ← R[%esp]+4` | toglie 4 byte dalla cima e li copia in D |

_(dispensa, pp. 41–43)_

## Istruzioni aritmetico-logiche

Operano su interi a 1, 2 e 4 byte:

| Istruzione | Effetto | Descrizione |
| --- | --- | --- |
| `INC D` | D ← D+1 | incrementa |
| `DEC D` | D ← D−1 | decrementa |
| `NEG D` | D ← −D | inverte il segno |
| `NOT D` | D ← ~D | complemento a 1 |
| `ADD S,D` | D ← D+S | somma |
| `SUB S,D` | D ← D−S | sottrae (**D − S**, attenzione all'ordine) |
| `IMUL S,D` | D ← D·S | moltiplica con segno; **la destinazione deve essere un registro** |
| `XOR S,D` | D ← D^S | or esclusivo |
| `OR S,D` | D ← D\|S | or |
| `AND S,D` | D ← D&S | and |

### IDIV

`IDIV` (divisione intera con segno) è più complessa: è uno dei casi in cui IA32 usa **registri fissi**, A e D.

| Istruzione | Effetto |
| --- | --- |
| `IDIV V` | A ← D:A / V; D ← D:A % V |
| `idivb V1` | `%al ← %ax / V1`; `%ah ← %ax % V1` |
| `idivw V2` | `%ax ← %dx:%ax / V2`; `%dx ← %dx:%ax % V2` |
| `idivl V4` | `%eax ← %edx:%eax / V4`; `%edx ← %edx:%eax % V4` |

Il dividendo è la **concatenazione D:A** (D contiene i bit più significativi); il **quoziente** va in A e il **resto** in D. Il divisore può essere registro o memoria, **non immediato**. (La versione a 8 bit fa eccezione: usa direttamente `%ax` come dividendo.)

Esempio, `%edi = %edi / %esi`:

```asm
movl %edi, %eax   # dividendo in %eax
movl %eax, %edx   # il dividendo è a 32 bit, ma bisogna estenderlo
sarl $31, %edx    # con segno a 64 bit in %edx:%eax (replica il bit di segno)
idivl %esi        # %edx:%eax / %esi
movl %eax, %edi   # quoziente in %edi
```

L'operazione è **costosa** e occupa i registri A e D, limitando la libertà nell'uso dei registri.

_(dispensa, pp. 43–45)_

### LEA (load effective address)

Vedi [[LEA]].

| Istruzione | Effetto | Descrizione |
| --- | --- | --- |
| `leal S,D4` | D₄ ← &S | calcola l'indirizzo effettivo dell'operando memoria S e lo scrive in D, **senza accedere alla memoria** |

Con `%eax=0x100`, `%ecx=0x7`, `M[0x100]=0xCAFE`:

| Istruzione | Effetto | Risultato |
| --- | --- | --- |
| `movl (%eax),%edx` | R[%edx] ← M[R[%eax]] | `%edx=0xCAFE` (legge la memoria) |
| `leal (%eax),%edx` | R[%edx] ← R[%eax] | `%edx=0x100` (solo l'indirizzo) |
| `leal (%eax,%ecx),%edx` | R[%eax]+R[%ecx] | `%edx=0x107` |
| `leal -3(%eax,%ecx),%edx` | R[%eax]+R[%ecx]−3 | `%edx=0x104` |
| `leal -3(%eax,%ecx,2),%edx` | R[%eax]+R[%ecx]·2−3 | `%edx=0x10B` |
| `leal (%eax,%ecx,2),%edx` | R[%eax]+R[%ecx]·2 | `%edx=0x10E` |
| `leal (,%ecx,4),%edx` | R[%ecx]·4 | `%edx=0x1C` |

`leal` serve a scrivere **programmi più veloci**, per due scopi:

1. calcolare **una sola volta** l'indirizzo di un oggetto in memoria e riusarlo;
2. calcolare **espressioni aritmetiche su interi o puntatori in una sola istruzione**, anche se il risultato non è un indirizzo.

Esempio: `int z = x + y*4 - 7;` con x in `%eax`, y in `%ecx`, z in `%edx`:

| Codice C (forma `a = a op b`) | IA32 | IA32 ottimizzato |
| --- | --- | --- |
| `z=y; z=z*4; z=z-7; z=z+x;` | `movl %ecx,%edx`<br>`imull $4,%edx`<br>`addl $-7,%edx`<br>`addl %eax,%edx` | `leal -7(%eax,%ecx,4),%edx` |

Una sola istruzione al posto di quattro. Il limite: la scala può valere solo **1, 2, 4, 8**, quindi `x+y*5-7` non si può calcolare con una `leal`.

> [!tip] Trucchi del compilatore
> `gcc` usa spesso `leal` per moltiplicazioni piccole: `leal (%eax,%eax,2),%eax` calcola `eax*3` e `leal (%eax,%eax,4),%eax` calcola `eax*5`. Le `leal` "strane" nel codice disassemblato sono quasi sempre aritmetica, non accessi a memoria.

_(dispensa, pp. 45–46)_

### Shift: SHL, SHR, SAL, SAR

Fanno scorrere a sinistra o a destra i bit di un operando. Uno shift a sinistra di 1 posizione moltiplica per 2; uno a destra divide per 2.

| Istruzione | Effetto | Tipo |
| --- | --- | --- |
| `SHL X,D` / `SAL X,D` | D ← D << X | logico/aritmetico a **sinistra** (identici) |
| `SHR X,D` | D ← D >> X | **logico** a destra: entrano **zeri** |
| `SAR X,D` | D ← D >> X | **aritmetico** a destra: entra il **bit di segno** |

D è registro o memoria (1, 2 o 4 byte); X può essere `%cl`, un immediato o 1 (se è 1 si può omettere).

- **SHL e SAL** sono la stessa istruzione (stesso opcode): a sinistra il bit di segno viene comunque espulso. Si usano per **moltiplicare per una potenza di 2** in modo più efficiente di `IMUL`.
- A destra bisogna scegliere: **SAR** per dividere numeri **con segno**, **SHR** per manipolare bit o per numeri senza segno.

Esempi su `%al` (shift di 3 = divisione per 8):

| Istruzione | Prima | Dopo | Decimale |
| --- | --- | --- | --- |
| `sarb $3,%al` | `CA` = `11001010` | `F9` = `11111001` | −54 → −7 = −54/8 |
| `sarb $3,%al` | `7A` = `01111010` | `0F` = `00001111` | 122 → 15 = 122/8 |
| `shrb $3,%al` | `CA` = `11001010` | `19` = `00011001` | −54 → 25 ≠ −54/8 |

L'ultimo caso mostra l'errore di usare uno shift **logico** per dividere un numero negativo: entrano zeri e il segno si perde.

> [!note] Arrotondamento
> −54/8 = −6.75: `sar` dà −7 (arrotonda verso −∞), mentre la divisione intera del C dà −6 (tronca verso 0). Per questo, quando divide interi con segno per potenze di 2, `gcc` aggiunge una correzione prima dello `sar`.

_(dispensa, pp. 46–48)_

## Istruzioni di salto

Vedi [[Istruzioni di Salto e Condition Code]].

Normalmente il controllo procede **in sequenza**: dopo ogni istruzione I, EIP viene incrementato del numero di byte di I. Le **istruzioni di salto** modificano EIP in modo che l'esecuzione prosegua da un altro indirizzo. Tre tipi:

1. salti **incondizionati**: EIP viene sovrascritto con l'indirizzo di destinazione;
2. salti **condizionati**: lo stesso, ma solo se una certa condizione sui dati è vera;
3. **chiamata e ritorno** da funzione.

### JMP: salti incondizionati

| Istruzione | Effetto | Nota |
| --- | --- | --- |
| `jmp etichetta` | R[%eip] ← indirizzo dell'etichetta | salto **diretto** |
| `jmp *S` | R[%eip] ← S | salto **indiretto** |

```asm
    movl $0, %eax
L:  incl %eax
    jmp L          # ciclo infinito: torna a incl
```

`jmp *(%eax)` salta all'indirizzo contenuto in memoria all'indirizzo `%eax`: `%eip ← M[R[%eax]]`. I salti indiretti si usano per gli `switch` (tabelle di salto) e per i puntatori a funzione.

### Jcc e CMP: salti condizionati

Il test si basa sul registro **EFLAGS**, i cui flag vengono aggiornati **come effetto collaterale** della maggior parte delle istruzioni aritmetico-logiche. Un salto condizionato avviene in due passi:

1. un'operazione aritmetico-logica opera sui dati (e aggiorna i flag);
2. in base all'esito, l'istruzione `Jcc` salta o meno all'etichetta.

I quattro **condition code**:

| Flag | Posto a 1 se l'ultima operazione… |
| --- | --- |
| **ZF** (zero) | ha prodotto **zero** |
| **SF** (sign) | ha prodotto un valore **negativo** |
| **CF** (carry) | ha generato un **riporto** (overflow senza segno) |
| **OF** (overflow) | ha generato un **overflow** con segno |

`Jcc etichetta`: if (condizione) R[%eip] ← indirizzo dell'etichetta.

| Suffisso | Sinonimo | Condizione | Significato |
| --- | --- | --- | --- |
| `e` | `z` | ZF | uguale (o zero) |
| `ne` | `nz` | ~ZF | diverso (o non zero) |
| `s` | | SF | negativo |
| `ns` | | ~SF | non negativo |
| `g` | `nle` | ~(SF^OF)&~ZF | maggiore, **con segno** (*greater*) |
| `ge` | `nl` | ~(SF^OF) | maggiore o uguale, con segno |
| `l` | `nge` | SF^OF | minore, con segno (*less*) |
| `le` | `ng` | (SF^OF)\|ZF | minore o uguale, con segno |
| `a` | `nbe` | ~CF&~ZF | maggiore, **senza segno** (*above*) |
| `ae` | `nb` | ~CF | maggiore o uguale, senza segno |
| `b` | `nae` | CF | minore, senza segno (*below*) |
| `be` | `na` | CF\|ZF | minore o uguale, senza segno |

I confronti maggiore/minore **cambiano** a seconda che i valori siano considerati con o senza segno: `g`/`l` (*greater*/*less*) per il segno, `a`/`b` (*above*/*below*) senza segno.

Esempio 1: `decl %eax` + `jz L` corrisponde a `eax--; if (eax == 0) goto L;`.

Esempio 2: `subl %ebx,%eax` + `je L` salta se i due registri erano uguali, ma **distrugge** `%eax`. Per questo esiste **CMP**:

| Istruzione | Effetto | Nota |
| --- | --- | --- |
| `CMP S,D` | calcola D − S | aggiorna i condition code e poi scarta il risultato |

Dopo `CMP S,D`, la condizione testata è "**D op S**" (attenzione all'ordine AT&T):

| Suffisso | Condizione dopo `CMP S,D` | Ovvero |
| --- | --- | --- |
| `e` | D−S == 0 | D == S |
| `ne` | D−S != 0 | D != S |
| `g` | D−S > 0 | D > S |
| `ge` | D−S >= 0 | D >= S |
| `l` | D−S < 0 | D < S |
| `le` | D−S <= 0 | D <= S |
| `a` / `ae` / `b` / `be` | come sopra, su `(unsigned)` | D >, >=, <, <= S senza segno |

Esempio 3: `cmpl %ebx,%eax` + `jle L` → `if (eax <= ebx) goto L;`.

### CALL e RET

| Istruzione | Effetto | Nota |
| --- | --- | --- |
| `CALL S` | `R[%esp]←R[%esp]−4`; `M[R[%esp]]←R[%eip]`; `R[%eip]←S` | mette sullo stack l'**indirizzo di ritorno** (l'istruzione dopo la CALL) e salta a S |
| `RET` | `R[%eip]←M[R[%esp]]`; `R[%esp]←R[%esp]+4` | toglie dallo stack l'indirizzo di ritorno e lo mette in EIP |

Esempio:

```asm
    call f            # f();
    imull $3, %eax    # eax = eax*3;
    ...
f:  movl $2, %eax     # void f() { eax = 2; }
    ret
```

Con il codice agli indirizzi `00001f86 call 00001f94`, `00001f8b imull`, `00001f94 movl`, `00001f99 ret`:

| # | %eip prima | %eax prima | istruzione | %eip dopo | %eax dopo |
| --- | --- | --- | --- | --- | --- |
| 1 | 00001f86 | – | `call 00001f94` | 00001f94 | – |
| 2 | 00001f94 | – | `movl $2,%eax` | 00001f99 | 2 |
| 3 | 00001f99 | 2 | `ret` | 00001f8b | 2 |
| 4 | 00001f8b | 2 | `imull $3,%eax` | 00001f8e | 6 |

![[SDC-p054-1.png]]

La `call` deposita sullo stack l'indirizzo di ritorno `00001f8b`; durante l'esecuzione di `f` l'indirizzo resta in cima allo stack; la `ret` lo toglie e l'esecuzione riprende da `imull`. È lo stesso meccanismo che, con anche i flag, usano gli interrupt ([[Interrupt]]).

_(dispensa, pp. 48–54)_

## Altre istruzioni e vincoli

### CMOVcc: assegnamento condizionato

| Istruzione | Effetto |
| --- | --- |
| `CMOVcc S,D` | if (condizione) D ← S |

Usa le stesse condizioni di `Jcc`, ma invece di saltare **copia**. Riduce il numero di istruzioni ed evita salti (che rallentano la pipeline, vedi [[06 - SDC - Esecuzione dei programmi#Pipelining|capitolo 6]]). Vincoli: la sorgente **non può essere immediata**, la destinazione **deve essere un registro**, solo operandi a **16 e 32 bit**.

`cmpl %ecx,%eax` + `cmovgl %eax,%ecx` → `if (eax > ecx) ecx = eax;` (cioè `ecx = max(eax, ecx)`).

### TEST

| Istruzione | Effetto |
| --- | --- |
| `TEST S,D` | calcola S & D, aggiorna i condition code e scarta il risultato |

È a `AND` quello che `CMP` è a `SUB`. Uso tipico: `testl %eax,%eax` + `jz L` (equivale a `cmpl $0,%eax` + `jz L`), perché l'AND di un valore con sé stesso è zero se e solo se il valore è zero.

### SETcc

| Istruzione | Effetto |
| --- | --- |
| `SETcc D1` | D₁ ← condizione (1 se vera, 0 altrimenti) |

Scrive 0 o 1 in un registro a 8 bit o in un byte di memoria. Calcola espressioni booleane senza salti: `cmpl $0,%eax` + `setl %dl` → `dl = (eax < 0)`.

### Vincoli sulle istruzioni

| Istruzione | Vincolo | Esempio |
| --- | --- | --- |
| `IMUL` | destinazione registro | `imull $2,(%edi)` ✗ |
| `CMOVcc` | sorgente non immediata, destinazione registro, solo 16/32 bit | `cmovgel $2,%eax` ✗, `cmovgeb %cl,%al` ✗ |
| `TEST`, `CMP` | il secondo operando ("destinazione") non immediato | `testl (%eax),$2` ✗ |
| `MOVZ`, `MOVS` | sorgente non immediata, destinazione solo registro | `movzbl $2,%ecx` ✗ |
| `IDIV` | usa D e A, divisore non immediato | `idivl $1` ✗ |

In generale **non si possono avere due operandi in memoria**: `movl (%eax),(%ecx)` non è consentita (serve un registro di appoggio).

_(dispensa, pp. 54–56)_

## Traduzione dei costrutti C

Vedi [[Traduzione dei Costrutti C in Assembly]].

Il compilatore può tradurre lo stesso programma in molti modi diversi (versioni e livelli di ottimizzazione diversi danno assembly diverso). Si usa la notazione `IA32(x)` per "traduzione di x". L'idea di fondo è riscrivere ogni costrutto in C con soli `if` e `goto`: questa forma si traduce poi quasi riga per riga.

### if

![[SDC-p057-1.png]]

| C | C equivalente | IA32 |
| --- | --- | --- |
| `if (test) blocco`<br>`istruzione` | `if (!test) goto L;`<br>`blocco;`<br>`L: istruzione;` | `IA32(test)`<br>`Jcc L`<br>`IA32(blocco)`<br>`L: IA32(istruzione)` |

Si salta sul **test negato**: il salto serve a **saltare il blocco** quando il test è falso.

Esempio (senza segno; a in `%eax`, b in `%ebx`, c in `%ecx`):

| C | C equivalente | IA32 |
| --- | --- | --- |
| `if (a>b) c=10;`<br>`c++;` | `if (a<=b) goto L;`<br>`c=10;`<br>`L: c++;` | `cmpl %ebx,%eax`<br>`jbe L`<br>`movl $10,%ecx`<br>`L: incl %ecx` |

`be` (*below or equal*) perché il confronto è senza segno.

### if…else

![[SDC-p057-2.png]]

| C | C equivalente | IA32 |
| --- | --- | --- |
| `if (test) blocco1`<br>`else blocco2`<br>`istruzione` | `if (!test) goto E;`<br>`blocco1;`<br>`goto F;`<br>`E: blocco2;`<br>`F: istruzione;` | `IA32(test)`<br>`Jcc E`<br>`IA32(blocco1)`<br>`jmp F`<br>`E: IA32(blocco2)`<br>`F: IA32(istruzione)` |

Il salto condizionato evita il blocco 1 quando il test è falso; il `jmp F` alla fine del blocco 1 evita il blocco 2: così i due blocchi sono **mutuamente esclusivi**.

Esempio (con segno): `if (a<=b) c=10; else c=20; c++;` diventa `cmpl %ebx,%eax`, `jg E`, `movl $10,%ecx`, `jmp F`, `E: movl $20,%ecx`, `F: incl %ecx`. Qui si usa `g` (*greater*) perché il confronto è con segno.

### while

![[SDC-p058-1.png]]

| C | C equivalente | IA32 |
| --- | --- | --- |
| `while (test) blocco`<br>`istruzione` | `L: if (!test) goto E;`<br>`blocco;`<br>`goto L;`<br>`E: istruzione;` | `L: IA32(test)`<br>`Jcc E`<br>`IA32(blocco)`<br>`jmp L`<br>`E: IA32(istruzione)` |

Come un `if`, ma dopo il blocco si **torna al test**.

Esempio (somma dei primi b interi, senza segno):

```c
a=1; c=0;
while (a<=b) { c+=a; a++; }
```

```asm
    movl $1, %eax
    movl $0, %ecx
L:  cmpl %ebx, %eax
    ja E              # esci se a > b
    addl %eax, %ecx
    incl %eax
    jmp L
E:
```

### for

![[SDC-p059-1.png]]

| C | C equivalente | IA32 |
| --- | --- | --- |
| `for (ini;test;agg) blocco`<br>`istruzione` | `ini;`<br>`L: if (!test) goto E;`<br>`blocco;`<br>`agg;`<br>`goto L;`<br>`E: istruzione` | `IA32(ini)`<br>`L: IA32(test)`<br>`Jcc E`<br>`IA32(blocco)`<br>`IA32(agg)`<br>`jmp L`<br>`E: IA32(istruzione)` |

`for (a=1; a<=b; a++) c+=a;` produce **esattamente lo stesso codice** del `while` precedente: un `for` è solo un `while` con inizializzazione e aggiornamento.

_(dispensa, pp. 56–60)_

## Funzioni

Vedi [[Convenzioni di Chiamata IA32]].

Una funzione C viene tradotta in una sequenza di istruzioni terminata da `RET` e invocata con `CALL`. La funzione che chiama è il **chiamante** (*caller*), quella chiamata il **chiamato** (*callee*).

Le convenzioni su traduzione delle funzioni, passaggio dei parametri e restituzione dei valori **non fanno parte dell'ISA**: sono stabilite dalla **System V ABI** per IA32, lo standard usato su Linux e macOS (vedi [[ABI e ISA]]).

```c
void f() { g(); h(); }      // f: call g / call h / ret
```

### Restituzione del valore

Per convenzione i valori **scalari** (interi, puntatori) vengono restituiti nel registro **`%eax`**.

| C | C equivalente | IA32 |
| --- | --- | --- |
| `int f(){ return 7+g(); }` | `int tmp = g(); tmp += 7; return tmp;` | `f: call g`<br>`addl $7,%eax`<br>`ret` |
| `int g(){ return 10; }` | | `g: movl $10,%eax`<br>`ret` |

`g` restituisce 10 in `%eax`; `f` ci somma 7 e restituisce 17, sempre in `%eax`.

### Stack frame e registro EBP

Vedi [[Stack Frame]].

Lo stack serve a orchestrare le chiamate e a fornire spazio locale. Ogni invocazione ha uno **stack frame** (o **record di attivazione**), con spazio per variabili locali, parametri da passare ad altre funzioni, ecc.

Per permettere a un **debugger** di elencare le funzioni pendenti dal `main` a quella corrente (il *backtrace*), gli stack frame vengono organizzati in una **lista collegata**: `%ebp` punta al frame corrente, e ogni frame contiene il puntatore (l'`%ebp` salvato) al frame del chiamante. Il collegamento tramite `%ebp` è **opzionale**.

> [!important] Allineamento a 16
> Per convenzione, nel momento in cui si esegue una `CALL`, `%esp` deve essere a un **indirizzo multiplo di 16**. Ha motivazioni di prestazioni, non di correttezza: spiega le istruzioni in apparenza inutili che `gcc` genera per allineare lo stack. La dispensa la ignora negli esempi per semplicità.

La lista di frame si gestisce con un **prologo** e un **epilogo**:

![[SDC-p062-1.png]]

- **prologo**: `pushl %ebp` salva il frame pointer del chiamante; `movl %esp,%ebp` fa puntare `%ebp` al frame corrente;
- **epilogo**: `popl %ebp` ripristina il frame pointer del chiamante, poi `ret`.

Con `gcc -fomit-frame-pointer` il collegamento viene **omesso**: niente prologo ed epilogo, codice più veloce e compatto, ma debugging più difficile.

| C | `gcc -S` (con ebp) | `gcc -S -fomit-frame-pointer` |
| --- | --- | --- |
| `int f(){ return 10; }` | `pushl %ebp`<br>`movl %esp,%ebp`<br>`movl $10,%eax`<br>`popl %ebp`<br>`ret` | `movl $10,%eax`<br>`ret` |

![[SDC-p063-1.png]]

A sinistra lo stack con frame collegati: ogni frame contiene variabili locali, parametri passati, indirizzo di ritorno e `%ebp` salvato, che punta all'`%ebp` salvato del frame precedente (le frecce formano la catena). A destra lo stack senza collegamento: si naviga solo con `%esp`. I triangoli indicano gli indirizzi multipli di 16. Lo stack cresce verso indirizzi bassi.

_(dispensa, pp. 60–63)_

### Passaggio dei parametri

I parametri di tipi primitivi sono passati dal chiamante al chiamato **sullo stack**, disposti in memoria nello **stesso ordine** in cui compaiono nell'intestazione della funzione. I parametri interi da 1 o 2 byte vengono **promossi a 4 byte**, così ogni parametro occupa un multiplo di 4 byte.

![[SDC-p064-1.png]]

Al momento dell'ingresso nel corpo della funzione:

- **con ebp**: il primo parametro è a `8(%ebp)`, il secondo a `12(%ebp)`, l'n-esimo a `4+4n(%ebp)`. In `4(%ebp)` c'è l'indirizzo di ritorno, in `(%ebp)` l'ebp salvato;
- **senza ebp**: il primo parametro è a `4(%esp)` (in `(%esp)` c'è l'indirizzo di ritorno), l'n-esimo a `4n(%esp)`.

| C | IA32 (con ebp) | IA32 (senza ebp) |
| --- | --- | --- |
| `int f(int x, int y) {` | `pushl %ebp`<br>`movl %esp,%ebp` | |
| `return x+y;` | `movl 8(%ebp),%eax`<br>`addl 12(%ebp),%eax` | `movl 4(%esp),%eax`<br>`addl 8(%esp),%eax` |
| `}` | `popl %ebp`<br>`ret` | `ret` |

Chiamata `c = f(10, 20);` (c in `%ecx`):

```asm
pushl $20         # secondo parametro
pushl $10         # primo parametro
call f
addl $8, %esp     # il CHIAMANTE toglie i parametri dallo stack
movl %eax, %ecx   # c = risultato
```

Lo stack cresce verso il basso, quindi i parametri si mettono sullo stack in **ordine inverso** (prima l'ultimo): così in memoria risultano nell'ordine giusto.

![[SDC-p065-1.png]]

Durante il corpo di `f`: x (=10) a `8(%ebp)`/`4(%esp)`, y (=20) a `12(%ebp)`/`8(%esp)`. Dopo il ritorno è il **chiamante** a rimuovere i parametri (`addl $8,%esp`, che compensa le due `push` da 4 byte).

### Registri caller-save e callee-save

Vedi [[Registri Caller-save e Callee-save]].

Una funzione chiamata può sovrascrivere i registri usati dal chiamante. Per preservarli, il loro contenuto va salvato (di solito sullo stack). Due possibilità:

1. **caller-save**: il **chiamante** salva il registro prima della chiamata e lo ripristina subito dopo;
2. **callee-save**: il **chiamato** salva il registro nel **prologo** e lo ripristina nell'**epilogo**.

Per convenzione (System V IA32):

- **caller-save**: **A, C, D**;
- **callee-save**: **B, DI, SI, SP, BP**.

I caller-save si possono usare liberamente in una funzione, ma bisogna salvarli attorno a una chiamata se servono dopo. I callee-save, se una funzione li usa, vanno salvati nel prologo e ripristinati nell'epilogo; in cambio, il loro contenuto è **garantito** attraverso le chiamate.

**Esempio caller-save**: `return g()+h();`, con a in `%eax` e c in `%ecx`:

```asm
f:  call g
    movl %eax, %ecx   # c = g()  (ecx è caller-save!)
    pushl %ecx        # salvalo prima di chiamare h
    call h
    popl %ecx         # ripristinalo
    addl %ecx, %eax   # a = h() + c
    ret
```

**Esempio callee-save**: lo stesso usando B:

```asm
f:  pushl %ebx        # prologo: f usa ebx, quindi lo salva
    call g
    movl %eax, %ebx   # b = g()
    call h            # h, se usasse ebx, lo salverebbe e ripristinerebbe
    addl %ebx, %eax
    popl %ebx         # epilogo
    ret
```

Il prezzo per usare `%ebx` è salvarlo e ripristinarlo in `f`; in cambio non serve salvarlo attorno alla chiamata a `h`.

### Variabili locali

Finora le variabili locali stavano nei registri (la scelta più semplice e veloce). A volte però serve **spazio nello stack frame**:

1. la variabile è un **array** o una **struct** (non entra in un registro);
2. ci sono **più variabili locali che registri** disponibili;
3. si usa l'operatore **`&`** sulla variabile, che quindi deve avere un **indirizzo in memoria**.

Lo spazio si alloca nel prologo (sottraendo k byte a `%esp`) e si dealloca nell'epilogo:

![[SDC-p067-1.png]]

Alle variabili locali si accede con `%esp` più un offset **positivo** oppure, se c'è il frame pointer, con `%ebp` più un offset **negativo**.

Esempio:

```c
int f(int x) {
    int y;
    leggi(&y);     // serve l'indirizzo di y: y deve stare in memoria
    return x + y;
}
```

Con ebp:

```asm
f:  pushl %ebp           # prologo
    movl %esp, %ebp      # prologo
    subl $4, %esp        # prologo: spazio per y
    leal -4(%ebp), %ecx  # ecx = &y   (y è in -4(%ebp))
    pushl %ecx           # passa &y
    call leggi
    addl $4, %esp        # togli il parametro
    movl 8(%ebp), %eax   # eax = x
    addl -4(%ebp), %eax  # eax += y
    addl $4, %esp        # epilogo
    popl %ebp            # epilogo
    ret
```

Senza ebp:

```asm
f:  subl $4, %esp        # prologo: spazio per y
    leal (%esp), %ecx    # ecx = &y   (y è in (%esp))
    pushl %ecx
    call leggi
    addl $4, %esp
    movl 8(%esp), %eax   # x: 4 (y) + 4 (ind. ritorno) = 8
    addl (%esp), %eax
    addl $4, %esp        # epilogo
    ret
```

Si noti la `leal` per calcolare `&y`.

![[SDC-p068-1.png]]

Layout dello stack all'inizio del corpo di `f` nelle due versioni: con ebp, y è sotto l'ebp salvato (`-4(%ebp)` = `%esp`); senza ebp, y è direttamente in `(%esp)` e x è a `8(%esp)`.

_(dispensa, pp. 63–68)_

## Array e aritmetica dei puntatori

L'accesso a celle di array con elementi fino a 8 byte usa l'indirizzamento `(base, indice, scala)`: `base` = indirizzo del primo byte dell'array, `indice` = indice della cella, `scala` = `sizeof(elemento)`. L'indirizzo `base + indice·scala` **realizza l'aritmetica dei puntatori**: in C, `a + i` avanza di `i·sizeof(*a)` byte.

Se l'indice è **noto a tempo di compilazione** si usa `disp(base)` con `disp = i·sizeof(elemento)`.

**Esempio 1**: `a[c]=10;` (a in `%eax`, c in `%ecx`), cioè `*(a+c)=10`:

```asm
movl $10, (%eax,%ecx,4)    # scala 4 = sizeof(int)
```

**Esempio 2**: indici costanti.

```c
int sum(int c[2]) { return c[0]+c[1]; }
```

```asm
sum: movl 4(%esp), %ecx    # ecx = c (un parametro array è un puntatore)
     movl (%ecx), %eax     # c[0]: spiazzamento 0
     addl 4(%ecx), %eax    # c[1]: spiazzamento 4
     ret
```

**Esempio 3**: somma di un array di dimensione n (v in `%ecx`, n in `%edx`, s in `%eax`, i in `%ebx`).

```c
int sum(int* v, int n) {
    int i, s = 0;
    for (i = 0; i < n; i++) s += v[i];
    return s;
}
```

```asm
sum: pushl %ebx                  # prologo (ebx è callee-save)
     movl 8(%esp), %ecx          # ecx = v (8: c'è anche ebx salvato)
     movl 12(%esp), %edx         # edx = n
     movl $0, %eax               # s = 0
     movl $0, %ebx               # i = 0
L:   cmpl %edx, %ebx
     jge E                       # if (i >= n) goto E
     addl (%ecx,%ebx,4), %eax    # s += v[i]
     incl %ebx                   # i++
     jmp L
E:   popl %ebx                   # epilogo
     ret
```

_(dispensa, pp. 68–70)_

## Strutture

Ai campi di una struct si accede con `off(base)`: `base` = indirizzo della struct, `off` = spiazzamento del campo. Il layout in memoria (con il **padding**) è spiegato in [[05 - SDC - Ottimizzazione dei programmi#Ridurre lo spazio di memoria|capitolo 5]].

```c
struct person { char age; char* name; };
char  get_age(struct person *p)  { return p->age; }
char* get_name(struct person *p) { return p->name; }
```

```asm
get_age:  movl 4(%esp), %eax
          movb (%eax), %al      # age: offset 0
          ret
get_name: movl 4(%esp), %eax
          movl 4(%eax), %eax    # name: offset 4
          ret
```

`name` è a offset **4** e non 1: ci sono **3 byte di padding** dopo `age`, perché un puntatore a 32 bit va allineato a 4 byte.

Struct allocata sullo stack:

```c
void f() { struct person p; fill(&p); ... }
```

```asm
f:  subl $12, %esp        # spazio per p (8 byte) e per il parametro di fill (4)
    leal 4(%esp), %ecx    # ecx = &p
    movl %ecx, (%esp)     # passa &p senza push: lo spazio è già riservato
    call fill
    ...
    addl $12, %esp        # dealloca
    ret
```

_(dispensa, pp. 70–71)_

## Estensione a x86-64

Vedi [[x86-64]].

Per compilare a 64 bit su un sistema a 64 bit **non** si usa `-m32`.

### Registri

**16 registri general-purpose a 64 bit** (contro gli 8 a 32 bit di IA32): A, B, C, D, DI, SI, SP, BP, R8–R15.

- RAX, RBX, RCX, RDX, RDI, RSI, RSP, RBP **estendono** a 64 bit i registri a 32 (EAX è la metà bassa di RAX, ecc.).
- Si può accedere agli 8 bit bassi di DI e SI: **DIL** e **SIL** (in IA32 no).
- R8–R15 hanno sottoparti con suffissi: `R8` (64), `R8D` (32 bit bassi), `R8W` (16), `R8B` (8).
- **Ogni scrittura sui 32 bit bassi di un registro a 64 bit azzera automaticamente i 32 bit alti** (`movl $1,%eax` azzera la parte alta di RAX).

### Passaggio dei parametri

A differenza di IA32, dove tutti i parametri vanno sullo stack, in x86-64 i **primi 6 parametri** interi o puntatore vanno nei registri **RDI, RSI, RDX, RCX, R8, R9**; dal settimo in poi si usa lo stack.

`swap` a 64 bit:

```asm
swap: movl (%rdi), %eax    # a = *x
      movl (%rsi), %ecx    # b = *y
      movl %eax, (%rsi)    # *y = a
      movl %ecx, (%rdi)    # *x = b
      ret
```

La stessa funzione in IA32 deve leggere i parametri dallo stack e salvare un registro callee-save:

```asm
swap: pushl %ebx
      movl 8(%esp), %eax
      movl 12(%esp), %ecx
      movl (%eax), %edx
      movl (%ecx), %ebx
      movl %edx, (%ecx)
      movl %ebx, (%eax)
      popl %ebx
      ret
```

```c
#include <stdio.h>
void swap(int*, int*);
int main() {
    int a = 10, b = 20;
    swap(&a, &b);
    printf("a=%d, b=%d\n", a, b);   // a=20, b=10
    return 0;
}
```

### Caller-save e callee-save

Nell'ABI System V AMD64 i **callee-save** sono **B, SP, BP e R12–R15**; tutti gli altri sono caller-save. (Rispetto a IA32, DI e SI diventano caller-save perché servono per i parametri.)

### Suffissi e MOVS/MOVZ

- Il suffisso **`q`** (*quad word*) indica operandi a 64 bit: `movq $10,%rax`.
- `MOVS` e `MOVZ` si estendono a 64 bit: `movsbq (%rax),%rax` legge un byte all'indirizzo RAX, lo estende con segno a 64 bit e lo scrive in RAX.

_(dispensa, pp. 71–73)_

## Domande riepilogative

> [!question]- Risposte (clicca per espandere)
> 1. **Vero**.
> 2. **Falso**: *Instruction Set Architecture*.
> 3. **Vero**.
> 4. **Falso**: `w` = 16 bit; 32 bit è `l`.
> 5. **Falso**: `movb` con destinazione a 16 bit (`%ax`) non è coerente; sarebbe `movb $5,%al` o `movw $5,%ax`.
> 6. **Falso**: due operandi memoria.
> 7. **Vero**.
> 8. **Falso**: l'ordine AT&T è sorgente, destinazione: `movl $0xABADCAFE,%edx`.
> 9. **Vero**: punta alla cima dello stack, che è l'indirizzo più basso.
> 10. **Falso**: `%sil` esiste solo in x86-64.
> 11. **Vero**.
> 12. **Falso**.
> 13. **Vero**.
> 14. **Falso**: `10` senza `$` è un indirizzo assoluto: legge `M[10]`.
> 15. **Vero**.
> 16. **Falso**: in big-endian il più significativo viene memorizzato **per primo** (indirizzo più basso).
> 17. **Vero**.
> 18. **Vero**.
> 19. **Falso**: `movzbw` scrive solo `%cx`, quindi `%ecx=0x12340034`.
> 20. **Vero**: 0x34 ha segno 0, quindi `%cx=0x0034`.
> 21. **Vero**: 0x8234 ha il bit di segno a 1.
> 22. **Falso**: serve `pushl`.
> 23. **Vero**.
> 24. **Falso**: il dividendo è D:A, il quoziente va in A e il resto in D.
> 25. **Vero**: entrambe copiano il valore di `%eax`.
> 26. **Vero**.
> 27. **Vero**: shift aritmetico, entrano 1 (0xC… ha il segno a 1).
> 28. **Vero**.
> 29. **Vero**.
> 30. **Vero**: stesso opcode.
> 31. **Vero**: −2 + 2 = 0, quindi ZF = 1.
> 32. **Falso**: la "destinazione" di CMP non può essere un immediato.
> 33. **Falso**: lo **diminuisce** di 4 (push dell'indirizzo di ritorno).
> 34. **Vero**.
> 35. **Falso**.
> 36. **Vero**.
> 37. **Falso**: non usa lo stack; è un ciclo infinito.
> 38. **Vero**: la parte bassa di `%eax`.
> 39. **Falso**: i parametri sono a indirizzi **superiori** all'indirizzo di ritorno.

_(dispensa, pp. 73–75)_
