---
title: Algoritmo del Panettiere
aliases:
  - SDC2 — Concorrenza parte 2
  - Sistemi di Calcolo 2 — Lezione 4
tags:
  - sistemi-di-calcolo-2
  - concorrenza
  - mutua-esclusione
  - bakery
source: Appunti Filippo/4-concorrenza_parte2.pdf
---

# Concorrenza parte 2: l'algoritmo del panettiere

> [!abstract] Scopo della lezione
> L'algoritmo di Dijkstra ([[03 - SDC2 - Deadlock#Algoritmo di Dijkstra|lezione 3]]) garantisce mutua esclusione e assenza di deadlock, ma non di starvation, e richiede letture/scritture atomiche su `k`. L'**algoritmo del panettiere** (*Bakery algorithm*, Lamport 1974) risolve entrambi i problemi: ogni processo prende un **biglietto** numerato e si entra in ordine di numero. La lezione costruisce l'algoritmo per tentativi (le prime due versioni **non** garantiscono la mutua esclusione), mostra la versione corretta con l'array `choosing`, la variante con numeri limitati e l'uso in un'applicazione **client/server** a messaggi.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

> [!important] Per l'esame
> All'esame c'è una domanda sull'algoritmo di Dijkstra **o** su quello del panettiere, presentato **con un errore**. Le due versioni sbagliate di questa lezione sono proprio gli errori tipici da riconoscere.

## Dijkstra: riepilogo

![[SDC2-L04-001-000.png]]

![[SDC2-L04-001-001.png]]

(Lo stesso codice della [[03 - SDC2 - Deadlock#Algoritmo di Dijkstra|lezione 3]].) L'algoritmo di Dijkstra:

- garantisce la **mutua esclusione** ed evita il **deadlock**;
- ma la **starvation è ancora possibile**: un processo può perdere la "corsa" sulla variabile `k` all'infinito;
- richiede **letture e scritture atomiche** e **memoria condivisa** per la variabile `k`, che tutti scrivono.

## L'idea del panettiere

Vedi [[Algoritmo del Panettiere]].

Si pensi a una panetteria con il bancone affollato: i clienti prendono un **biglietto numerato**. Se non c'è nessuno in attesa, i biglietti non contano; quando molte persone aspettano, **l'ordine dei biglietti decide l'ordine in cui vengono servite**. Chi arriva dopo prende un numero più alto, quindi nessuno aspetta per sempre: **niente starvation**, perché il servizio è FIFO.

Gli schemi seguenti mostrano, per i processi 1…n, le fasi che attraversano: **remainder** (fuori, numero 0), **entry** divisa in **doorway** (prende il biglietto) e **waiting** (aspetta il proprio turno), **CS** (sezione critica) ed **exit**. Il numero nel cerchio è il biglietto; le frecce numerate indicano l'ordine degli eventi.

![[SDC2-L04-001-002.png]]

All'inizio tutti i processi sono nel remainder con biglietto 0.

![[SDC2-L04-001-003.png]]

Il processo 2 passa per la doorway e prende il biglietto **1** (eventi 1–2); i processi 4 e 5 arrivano dopo e prendono entrambi il biglietto **2** (eventi 3–6); il processo 2, che ha il numero più basso, entra in CS ed esce (eventi 7–8).

![[SDC2-L04-002-004.png]]

Tra i processi 4 e 5, entrambi con biglietto 2, entra il processo **4** (eventi 9–10): a parità di numero si usa l'**ID del processo** come spareggio.

![[SDC2-L04-002-005.png]]

Mentre il 5 aspetta, il processo 4 rientra e prende il biglietto **3** (eventi 11–12), perché il massimo in circolazione è 2; il processo 5 (biglietto 2) entra prima di lui (eventi 13–14). Chi è arrivato prima viene servito prima.

## Prima implementazione (sbagliata)

![[SDC2-L04-002-006.png]]

```c
while (1) {
    /* NCS */
    number[i] = 1 + max {number[j] | (1 <= j <= N) except i};   // doorway: prende il biglietto
    for j in 1 .. N except i {
        while (number[j] != 0 && number[j] < number[i]);        // aspetta chi ha un numero più basso
    }
    /* CS */
    number[i] = 0;                                              // butta il biglietto
}
```

![[SDC2-L04-002-007.png]]

`number[]` è l'array dei biglietti, tutti a 0 all'inizio (0 = "non interessato"). Il biglietto del processo i è 1 più il massimo tra i biglietti degli altri; poi i aspetta, per ogni altro processo j, finché j ha un biglietto e quel biglietto è più basso del suo.

**Problema: non garantisce la mutua esclusione.**

![[SDC2-L04-002-008.png]]

![[SDC2-L04-002-009.png]]

![[SDC2-L04-002-010.png]]

Il calcolo del massimo **non è atomico**: i processi 4 e 5 possono leggere lo stesso massimo e prendere **lo stesso biglietto** (2). Il processo 2, con biglietto 1, entra ed esce (eventi 7–8). Ora 4 e 5 hanno entrambi 2: per ognuno il test `number[j] < number[i]` è falso (2 < 2 è falso), quindi **nessuno dei due aspetta l'altro** ed entrano **entrambi** in sezione critica (eventi 9–10): *no mutual exclusion*.

## Seconda implementazione (sbagliata)

Si aggiunge lo spareggio sull'ID con l'**ordine lessicografico**:

![[SDC2-L04-003-011.png]]

```c
while (1) {
    /* NCS */
    number[i] = 1 + max {number[j] | (1 <= j <= N) except i};
    for j in 1 .. N except i {
        while (number[j] != 0 && (number[j], j) < (number[i], i));
    }
    /* CS */
    number[i] = 0;
}
// ordine lessicografico: (B, j) < (A, i)  ⟺  B < A || (B == A && j < i)
```

![[SDC2-L04-003-012.png]]

A parità di biglietto passa il processo con l'ID più basso.

**Neanche questa garantisce la mutua esclusione.**

![[SDC2-L04-003-013.png]]

![[SDC2-L04-003-014.png]]

![[SDC2-L04-003-015.png]]

Il problema ora è il **momento** in cui il biglietto viene scritto. Il processo 1 è in CS. I processi 3 e 5 stanno calcolando il loro biglietto (la nuvoletta "2": lo hanno calcolato ma **non ancora scritto** in `number[]`). Il processo 5 scrive per primo 2 e, controllando gli altri, vede `number[3] = 0` (il 3 non ha ancora scritto): non lo aspetta ed entra in CS dopo l'1. A questo punto il processo 3 scrive finalmente il suo 2, controlla gli altri e, poiché (2, 3) < (2, 5), **non aspetta il 5**: entra anche lui. Processi 3 e 5 sono in CS insieme.

Serve quindi impedire che un processo venga "scavalcato" mentre un altro **sta ancora scegliendo** il proprio biglietto.

## Bakery algorithm corretto

![[SDC2-L04-003-016.png]]

```c
while (1) {
    /* NCS */
    choosing[i] = true;                                         // sto scegliendo
    number[i] = 1 + max {number[j] | (1 <= j <= N) except i};
    choosing[i] = false;                                        // ho scelto
    for j in 1 .. N except i {
        while (choosing[j] == true);                            // aspetta che j finisca di scegliere
        while (number[j] != 0 && (number[j], j) < (number[i], i));
    }
    /* CS */
    number[i] = 0;
}
```

L'array booleano `choosing[]` (tutto `false` all'inizio) segnala che un processo **è nella doorway**. Prima di confrontarsi con j, il processo i aspetta che j abbia **finito di scegliere**: così non può più leggere `number[j] = 0` mentre j sta per scrivere un biglietto più basso del suo.

Proprietà: **mutua esclusione**, **assenza di deadlock** e **assenza di starvation** (i processi entrano in ordine FIFO di biglietto, a parte gli spareggi).

### Il calcolo del massimo

La riga `number[i] = 1 + max{…}` non è un'operazione unica: si calcola con un ciclo che legge una cella alla volta.

![[SDC2-L04-004-019.png]]

![[SDC2-L04-004-017.png]]

```c
local1 = 0;
for local2 in 1 .. N {
    local3 = number[local2];
    if (local1 < local3)
        local1 = local3;
}
number[i] = 1 + local1;
```

È proprio perché questo ciclo può essere interrotto a metà che due processi possono ottenere lo stesso biglietto (ed è per questo che serve lo spareggio sull'ID).

### Biglietti limitati

![[SDC2-L04-004-018.png]]

```c
while (1) {
    /* NCS */
    while (number[i] == 0) {
        choosing[i] = true;
        number[i] = (1 + max {number[j] | (1 <= j <= N) except i}) % MAXIMUM;
        choosing[i] = false;
    }
    for j in 1 .. N except i {
        while (choosing[j] == true);
        while (number[j] != 0 && (number[j], j) < (number[i], i));
    }
    /* CS */
    number[i] = 0;
}
```

Nella versione base i biglietti possono crescere senza limite (se la sezione critica non si svuota mai). Qui si calcolano **modulo `MAXIMUM`**; se il risultato è 0 (che significherebbe "non interessato") si ripete la scelta.

> [!note]
> Con il modulo, un biglietto "ripartito" da valori bassi potrebbe superare chi ha numeri vicini al massimo: la variante funziona solo se `MAXIMUM` è abbastanza grande rispetto al numero di processi (in pratica, maggiore del numero di biglietti che possono essere attivi contemporaneamente).

### Caratteristiche

- I processi comunicano **scrivendo e leggendo variabili condivise** (come in Dijkstra).
- Letture e scritture **non devono essere atomiche**: un lettore può leggere mentre uno scrittore sta scrivendo, senza notifiche (si può leggere un valore qualsiasi, e l'algoritmo resta corretto). È il grande vantaggio rispetto a Dijkstra.
- Ogni variabile condivisa è **di proprietà di un solo processo**, che è l'unico a scriverla; gli altri la leggono soltanto (`number[i]` e `choosing[i]` sono scritte solo da i).
- Nessun processo fa due scritture concorrenti.
- I tempi di esecuzione dei processi non sono correlati.

## Bakery in un'applicazione client/server

Proprio perché ogni variabile ha un solo proprietario, l'algoritmo si può portare in un **sistema distribuito**, dove non c'è memoria condivisa: ogni processo tiene le proprie variabili e gli altri le "leggono" chiedendole con dei messaggi.

![[SDC2-L04-005-020.png]]

```c
// variabili globali (di ciascun processo), inizializzazione:
int num = 0;
boolean choosing = false;
// e indirizzi IP/porte degli altri processi

while (1) {                              // thread client
    /* NCS */
    choosing = true;                     // doorway
    for j in 1 .. N except i {
        send(Pj, num);                   // chiede a tutti gli altri il loro numero
        receive(Pj, v);
        num = max(num, v);
    }
    num = num + 1;
    choosing = false;
    for j in 1 .. N except i {           // bakery
        do {
            send(Pj, choosing);          // j sta scegliendo?
            receive(Pj, v);
        } while (v == true);
        do {
            send(Pj, v);                 // qual è il numero di j?
            receive(Pj, v);
        } while (v != 0 && (v, j) < (num, i));
    }
    /* CS */
    num = 0;
}

while (1) {                              // thread server
    receive(Pj, message);
    if (message is a number)
        send(Pj, num);                   // risponde con il proprio numero
    else
        send(Pj, choosing);              // risponde con il proprio choosing
}
```

Ogni processo ha due thread: il **client**, che esegue l'algoritmo, e il **server**, che risponde alle "letture" degli altri inviando `num` o `choosing`.

Ipotesi:

- **tempo di risposta finito**: ogni processo prima o poi risponde;
- **canali di comunicazione affidabili**: i messaggi non si perdono.

È un primo esempio di mutua esclusione distribuita, ripresa nei [[08 - SDC2 - Sistemi Distribuiti|sistemi distribuiti]].
