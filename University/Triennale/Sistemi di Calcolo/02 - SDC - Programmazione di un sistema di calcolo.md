---
title: Programmazione di un sistema di calcolo
aliases:
  - SDC — Come viene programmato un sistema di calcolo
  - Sistemi di Calcolo — Capitolo 2
tags:
  - sistemi-di-calcolo
  - compilazione
  - gcc
  - elf
  - objdump
source: Dispensa Sistemi di Calcolo.pdf (cap. 2, pp. 28–35)
---

# Programmazione di un sistema di calcolo

> [!abstract] Scopo del capitolo
> La CPU esegue solo linguaggio macchina, ma nessuno programma direttamente in binario. Il capitolo spiega come si colma questa distanza: linguaggi di **alto e basso livello**, **compilazione** vs **interpretazione**, i quattro stadi della **compilazione di un programma C** (preprocessore, compilatore, assemblatore, linker) con la toolchain **gcc**, i formati dei file (**ELF**, **Mach-O**) e il **disassemblaggio** con `objdump`. È il ponte verso il capitolo 3, dove si legge l'assembly generato.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]]

## Linguaggi di alto e basso livello

![[SDC-p028-1.png]]

Lo spettro va dai linguaggi di **alto livello** (C, Python, Java, JavaScript) a quelli di **basso livello**: Java bytecode, **assembly**, **linguaggio macchina**. Un linguaggio è "di alto livello" quando i suoi costrutti sono lontani da quelli della macchina; ci sono gradazioni intermedie (i costrutti del C sono più vicini alla macchina di quelli di Java o Python).

- Il **linguaggio macchina** è pensato per la CPU ed è del tutto inadatto per programmare.
- I linguaggi di **alto livello** offrono costrutti più potenti, sono più facili da imparare, da mantenere e da correggere (*debugging*).
- L'**assembly** (o linguaggio assemblativo) è un linguaggio di basso livello che descrive le istruzioni macchina con una sintassi leggibile: è una **traslitterazione** del linguaggio macchina, che associa a ogni codice binario di istruzione un **codice mnemonico** (es. `c3` → `ret`). Lo usa chi deve scrivere codice molto ottimizzato o parti di sistemi operativi.

> [!note] Assembly ≠ linguaggio macchina
> Sono in corrispondenza quasi uno a uno, ma non sono sinonimi: l'assembly è **testo**, il linguaggio macchina è **binario**. Serve un assemblatore per passare dal primo al secondo.

_(dispensa, p. 28)_

## Compilazione vs interpretazione

Vedi [[Compilazione e Interpretazione]].

| | Compilazione | Interpretazione | Ibrido |
| --- | --- | --- | --- |
| **Descrizione** | il programma viene **tradotto** in codice macchina nativo eseguibile dalla CPU | il programma viene eseguito direttamente da un **interprete**, senza compilarlo (linguaggi di *scripting*) | si compila in un **linguaggio intermedio**, che poi viene interpretato |
| **Esempi** | C, C++, Fortran | Python, Perl, PHP, JavaScript | Java (→ Java bytecode) |
| **Vantaggi** | codice ottimizzato per la piattaforma: le **migliori prestazioni** | **portabile** (basta avere l'interprete), nessuna compilazione: sviluppo più agile | portabile ovunque esista un interprete del linguaggio intermedio |
| **Svantaggi** | **non portabile**: gira solo sulla piattaforma per cui è stato compilato | **più lento** del codice nativo | come l'interpretazione |

Alcuni interpreti (es. la JVM per il bytecode Java) usano la **JIT** (*Just-In-Time compilation*): compilano in codice nativo le parti da eseguire subito prima di eseguirle, recuperando gran parte delle prestazioni. È lo stesso principio del processore virtuale visto in [[02 - SO - Programmi, Makefile e pkg-config#Portabilità e macchine virtuali|Sistemi Operativi]].

_(dispensa, pp. 28–29)_

## Stadi della compilazione di un programma C

Vedi [[Compilazione e Linking con gcc]].

Un programma C è formato da uno o più moduli (**translation unit**), ognuno in un file `.c`. Il caso più semplice è un'unica translation unit:

```c
// hello.c
#include <stdio.h>
int main() {
    printf("Hello world\n");
    return 0;
}
```

Dal punto di vista dell'utente, la compilazione trasforma `hello.c` nell'eseguibile `hello`:

![[SDC-p030-1.png]]

In realtà la **compilation toolchain** esegue, senza che ce ne accorgiamo, quattro stadi distinti:

![[SDC-p030-2.png]]

1. **Preprocessore** (`cpp`): prende un testo C e produce un altro testo C in cui le direttive `#include`, `#define`, … sono state elaborate (il risultato non contiene più `#`). Include il contenuto dei file indicati: qui legge anche `stdio.h` dalle directory di sistema. Output: `hello.i` (testo).
2. **Compilatore** (`cc1`): verifica la correttezza sintattica del C preprocessato e lo traduce in **assembly** per la piattaforma di destinazione. Output: `hello.s` (testo). Non produce direttamente codice macchina.
3. **Assemblatore** (`as`): traduce l'assembly in **codice macchina**, generando un **file oggetto**. Output: `hello.o` (binario).
4. **Linker** (`ld`): collega più file oggetto in un unico **eseguibile**. Qui collega `hello.o` con `printf.o` (il codice di `printf` dalla libreria di sistema). Output: `hello` (binario). Il linker è l'ultimo stadio e associa i **simboli** (nomi di funzioni e variabili) agli **indirizzi** di memoria.

_(dispensa, p. 30)_

### La toolchain gcc

I programmi che realizzano gli stadi sono `cpp`, `cc1`, `as` e `ld`. Normalmente non si invocano direttamente: si usa `gcc` con delle opzioni per fermarsi a uno stadio:

```bash
gcc -E hello.c > hello.i    # solo preprocessore (senza > stampa a video)
gcc -S hello.i              # compila in assembly: hello.s
gcc -c hello.s              # assembla: hello.o
gcc hello.o -o hello        # collega con le librerie di sistema: hello
```

Il comando unico `gcc hello.c -o hello` è del tutto equivalente: crea i file intermedi come file temporanei nascosti e li elimina alla fine.

> [!tip] Per il capitolo 3
> `gcc -S` è il modo più rapido per vedere come il compilatore traduce un pezzo di C in assembly. Con `-m32` si ottiene assembly IA32 a 32 bit, quello usato nella dispensa.

_(dispensa, p. 31)_

## Formati dei file: ELF e Mach-O

Vedi [[Loader ed ELF]].

Il comando `file` dice di che tipo è un file, esaminandone il contenuto:

```
$ file hello.c   →  C source, ASCII text
$ file hello.i   →  C source, ASCII text
$ file hello.s   →  ASCII text
$ file hello.o   →  ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
$ file hello     →  ELF 64-bit LSB executable, x86-64, ..., dynamically linked (uses shared libs), ...
```

- `hello.c`, `hello.i`, `hello.s` sono **file di testo**; `hello.o` e `hello` sono **binari**.
- Su Linux gli ultimi due sono in formato **ELF** (*Executable and Linkable Format*), che rappresenta tutte le informazioni di un programma in codice macchina. Il `.o` è *relocatable* (rilocabile, non ancora collegato); l'eseguibile è *executable* e *dynamically linked* (usa librerie condivise). ELF è usato anche dalle console PlayStation e da alcuni smartphone.
- **macOS** e **iOS** usano invece il formato **Mach-O** (`Mach-O 64-bit object x86_64`, `Mach-O 64-bit executable x86_64`).

Un file ELF **non può essere eseguito né linkato su macOS**, e un Mach-O non può esserlo su Linux, **anche se l'hardware è identico**. I formati eseguibili quindi **non garantiscono la portabilità**: dipendono dal sistema operativo, oltre che dall'ISA.

> [!note] `file` non guarda l'estensione
> `file` legge il contenuto (i *magic number* iniziali, es. `\x7fELF`), non l'estensione: rinominare `hello` in `hello.txt` non cambia il risultato.

_(dispensa, pp. 31–33)_

## Disassemblare con objdump

Vedi [[objdump]].

**Disassemblare** significa tradurre le istruzioni macchina nell'assembly corrispondente, per poterle leggere: è l'operazione inversa dell'assemblaggio.

```c
// somma.c
int somma(int x, int y) {
    return x + y;
}
```

```bash
gcc -c somma.c
objdump -d somma.o
```

![[SDC-p034-1.png]]

Per ogni funzione l'output mostra tre colonne:

1. lo **spiazzamento** (offset) dell'istruzione all'interno della sezione, in esadecimale;
2. il **codice macchina** in esadecimale;
3. il corrispondente **codice assembly** (mnemonici).

Le istruzioni x86 hanno **lunghezza variabile**: `retq` è un solo byte (`c3`), `mov %rsp,%rbp` sono tre byte (`48 89 e5`). Le istruzioni del prologo (`push %rbp`, `mov %rsp,%rbp`) e quelle che salvano `%edi`/`%esi` sullo stack si capiranno con lo stack frame del [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Funzioni|capitolo 3]].

### Disassemblato misto: objdump -S

Compilando con `-g` (informazioni di debug), `objdump -S` produce un disassemblato **misto**, con il codice sorgente inframmezzato a quello macchina/assembly:

```
$ gcc -g -c somma.c
$ objdump -S somma.o

0000000000000000 <somma>:
int somma(int x, int y){
   0:  55                push   %rbp
   1:  48 89 e5          mov    %rsp,%rbp
   4:  89 7d fc          mov    %edi,-0x4(%rbp)
   7:  89 75 f8          mov    %esi,-0x8(%rbp)
    return x+y;
   a:  8b 45 f8          mov    -0x8(%rbp),%eax
   d:  8b 55 fc          mov    -0x4(%rbp),%edx
  10:  01 d0             add    %edx,%eax
}
  12:  5d                pop    %rbp
  13:  c3                retq
```

Le istruzioni con offset da `a` a `12` (escluso) sono la traduzione di `return x+y;`: carica i due parametri in `%eax` e `%edx`, li somma e lascia il risultato in `%eax`, il registro del valore di ritorno. Anche con `-S` restano visibili sia il codice macchina sia l'assembly.

Lo stesso strumento è la base dell'analisi dei binari in [[2 - MA - X86 Assembly|Malware Analysis]].

_(dispensa, pp. 33–35)_

## Domande riepilogative

> [!question]- Risposte (clicca per espandere)
> 1. **Falso**: l'assembly è una traslitterazione testuale del linguaggio macchina.
> 2. **Vero**.
> 3. **Vero**: un programma C senza direttive `#`.
> 4. **Falso**: produce assembly; il codice macchina lo produce l'assemblatore.
> 5. **Vero**.
> 6. **Falso**: un file oggetto è rilocabile e non ancora collegato.
> 7. **Vero**.
> 8. **Falso**: ne descrive il **tipo** in base al contenuto.
> 9. **Vero**.
> 10. **Falso**: mostra sorgente, codice macchina **e** assembly.

_(dispensa, p. 35)_
