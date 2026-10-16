---
title: Tipologie di esercizi d'esame
aliases:
  - MC — Tipologie di esercizi d'esame
tags:
  - modelli-di-calcolo
  - esami
source: pdf/Esami (19 tracce, giugno 2019 – luglio 2023)
---

# Tipologie di esercizi d'esame

> [!abstract]
> Raccolta degli esercizi ricorrenti nelle 19 tracce della prova di Modelli (Fondamenti di Informatica II) in `pdf/Esami/`, da giugno 2019 a luglio 2023, raggruppati per tipo. Per ogni tipo: dove compare, il **metodo** di risoluzione e il collegamento alla lezione. Alcuni esercizi sono svolti per intero come esempio. Le tracce dal 2021 in poi chiedono sempre di **motivare** i passaggi: "risposte secche sì/no prive di elaborazione non saranno valutate".
> Mappa del corso: [[MOC - Modelli di Calcolo]].

## Panoramica

| tipo | frequenza | lezioni |
|---|---|---|
| contare esecuzioni, notazione asintotica, ricorrenze | quasi ogni traccia | [[02 - MC - Notazione asintotica\|2]], [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza\|4]] |
| definire P, NP, NP-completi; certificati; riduzioni | ogni traccia | [[14 - MC - Classi P e NP e NP-completezza\|14]] |
| costruire un ASF / un'espressione regolare / una grammatica regolare | ogni traccia | [[10 - MC - Automi a stati finiti ed espressioni regolari\|10]] |
| grammatiche CF: linguaggio generato, derivazioni, ambiguità, tipo | quasi ogni traccia | [[09 - MC - Grammatiche e gerarchia di Chomsky\|9]], [[11 - MC - Analisi sintattica top-down e automi a pila\|11]] |
| FIRST/FOLLOW, LL(1), parser top-down | molto frequente | [[11 - MC - Analisi sintattica top-down e automi a pila\|11]] |
| bottom-up, shift/reduce, LR(0) | dal 2022 | [[12 - MC - Parsing bottom-up\|12]] |
| macchine di Turing, universale, Church-Turing | frequente | [[08 - MC - Macchine di Turing e calcolabilità\|8]] |
| decidibilità, Halting Problem, diagonalizzazione | frequente | [[06 - MC - Cardinalità e diagonalizzazione\|6]], [[07 - MC - Halting Problem\|7]] |
| DPLL, CNF/DNF | 2020–2022 | [[13 - MC - Forme normali e algoritmo DPLL\|13]] |
| programmazione dinamica (LCS), Boyer-Moore | 2019–2020 | (parte di algoritmi, vedi ASD) |

## 1. Analisi di costo

### Contare le esecuzioni di un'istruzione

*Giugno 2019, settembre 2019*: per $n > 1$, $T(n)$ = numero esatto di esecuzioni di `a ← a + 2` in

```text
for i ← 1 to n-1 do
   for j ← n-i+1 to n do
      a ← a + 2
```

**Metodo**: si conta il numero di iterazioni del ciclo interno per ogni valore dell'esterno e si somma. Per $i$ fissato, $j$ va da $n - i + 1$ a $n$: sono $i$ iterazioni. Quindi
$$T(n) = \sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = \Theta(n^2), \qquad T(10) = 45$$

*Luglio 2023*: costo di

```c
for(i = n/2; i <= n; i++)
   for(j = 1; j <= n; j = j * 2)
      k = k + n/2;
```

Il ciclo esterno fa $n/2 + 1$ iterazioni; quello interno raddoppia $j$, quindi $\lfloor \log_2 n \rfloor + 1$. $T(n) = (n/2 + 1)(\lfloor \log_2 n \rfloor + 1) = \Theta(n \log n)$.

### Vero o falso sulle notazioni

*Settembre 2021, giugno 2023*. **Metodo**: si applica la definizione o le regole pratiche ([[02 - MC - Notazione asintotica#Regole pratiche per confrontare funzioni|lezione 2]]).

| affermazione | | |
|---|---|---|
| $O(f \cdot g) = O(f) \cdot O(g)$ | vera | (come insiemi di prodotti) |
| $5 + 100n + 3n^2 = O(n^4)$ | vera | upper bound non stretto |
| $5 + 100n + 3n^2 = O(n)$ | falsa | il termine $n^2$ domina |
| $n\log n + n + 3n^2 = \Omega(n^3)$ | falsa | cresce come $n^2$ |
| $5 + 100n + 3n^2 = \Omega(n)$ | vera | |
| $n^3 + 100n + 1000 \in \Omega(n^2)$ | vera | |
| $n \log n \in \Omega(n)$, $n \log n \notin O(n)$ | vera / vera | |
| $f \in O(g) \wedge f \in \Omega(g) \Rightarrow f \in \Theta(g)$ | vera | proprietà 2 |

*Settembre 2021*: software A costa $0{,}001\,n$ ms, B costa $500\sqrt n$ ms. Per la notazione $O$ è migliore **B** ($O(\sqrt n)$ contro $O(n)$). Per $n = 10^8$: A impiega $10^5$ ms = 100 s, B impiega $500 \cdot 10^4$ ms = 5000 s: in pratica è migliore **A**. Le costanti contano finché $n$ non è abbastanza grande (qui il sorpasso è a $n = 2{,}5 \cdot 10^{11}$).

**Domande teoriche frequenti**: perché si ignorano le costanti (vantaggi: indipendenza dal modello e dall'hardware, conta la crescita; svantaggi: costanti enormi rendono inutilizzabili algoritmi "migliori", come per il merge sort su vettori piccoli); perché caso peggiore e dimensione dell'input ([[01 - MC - Costo degli algoritmi e modello CEM#Ingredienti dell'analisi|lezione 1]]); cos'è l'istruzione dominante; cosa significa "P è asintoticamente migliore di Q" (esiste $n_0$ oltre il quale costa meno, a meno di costanti).

### Ricorrenze e ricorsioni

| esercizio | soluzione |
|---|---|
| $T(n) = 2T(n/2) + n^2$, $T(1) = 1$ (giugno 2023) | albero: livello $i$ costa $2^i (n/2^i)^2 = n^2/2^i$; somma geometrica $\le 2n^2$: $\Theta(n^2)$ |
| albero delle chiamate binario completo con $n$ foglie, lavoro 1 per nodo (2019, 2020, 2022) | $2n - 1$ nodi: $\Theta(n)$; con 8 foglie $T = 15$ |
| chiamate di `fibo(5)` con `if(n <= 1) return n;` (luglio 2021) | 15 (vedi [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Forma chiusa dei numeri di Fibonacci]]) |
| chiamate di `fib(4)` con `if(n < 2) return 1;` (febbraio 2020) | $T(0)=T(1)=1$, $T(n) = 1 + T(n-1) + T(n-2)$: $T(4) = 9$; costo $\Theta(\varphi^n)$ |
| `toto(6)` con `if(n <= 2) return n;` e `toto(n-1) * toto(n-2)` (luglio 2021 B) | $T(n) = 1$ per $n \le 2$: $T(3) = 3$, $T(4) = 5$, $T(5) = 9$, $T(6) = 15$ |
| spazio e tempo di `boh(boh(a+1))` (febbraio 2022) | $\Theta(11 - a)$ in tempo e spazio (vedi lezione 4) |

## 2. Classi di complessità e riduzioni

### Definizioni

*Ogni traccia*. Definire P, NP (con la MT non deterministica **e** con i certificati, giustificandone l'equivalenza), NP-completo, NP-hard; relazioni di contenimento ($\mathrm{P} \subseteq \mathrm{NP}$, NP-completi $= \mathrm{NP} \cap$ NP-hard, figura della [[14 - MC - Classi P e NP e NP-completezza#Classi di complessità|lezione 14]]). Rilevanza pratica di P vs NP ([[14 - MC - Classi P e NP e NP-completezza#Implicazioni pratiche|implicazioni pratiche]]).

### Mostrare che un problema è in NP

**Metodo**: si dà il **certificato** (di lunghezza polinomiale) e l'**algoritmo di verifica** polinomiale, oppure l'algoritmo non deterministico che lo "indovina".

| problema | certificato | verifica |
|---|---|---|
| SAT / 4-SAT | assegnazione | si valuta ogni clausola: $O(|F|)$ |
| Vertex Cover (al più $k$ nodi; o $\lceil n/10 \rceil$) | l'insieme $S$ | ogni arco ha un estremo in $S$: $O(|E|)$ |
| 3-colorazione / 4-colorazione | un colore per nodo | ogni arco ha estremi di colore diverso |
| programmazione lineare intera | un'assegnazione di interi | si valutano i vincoli (ma serve che una soluzione piccola esista) |

(4-SAT e 4-colorazione: la prova è identica a SAT e 3-colorazione; cambia solo la verifica del formato.)

### Dimostrare che un problema è NP-completo

**Metodo** ([[14 - MC - Classi P e NP e NP-completezza#NP-completezza|lezione 14]]): (1) il problema è in NP; (2) riduzione **da** un problema noto NP-completo (3SAT/3CNF) **al** problema nuovo, verificata in entrambi i versi. Le riduzioni chieste: 3SAT → Independent Set (giugno 2022), 3SAT → programmazione intera (giugno 2023), riduzione a scelta (luglio 2019).

### Conseguenze ipotetiche

| ipotesi | conseguenza |
|---|---|
| upper bound $O(n^6)$ per 3-COLORABILITÀ | $\mathrm{P} = \mathrm{NP}$ (è NP-completo) |
| lower bound $\Omega(2^{n/3})$ per VERTEX COVER | $\mathrm{P} \ne \mathrm{NP}$ |
| upper bound esponenziale per 3-SAT | nessuna |
| lower bound polinomiale per un problema di NP | nessuna |
| lower bound esponenziale per un problema di NP | $\mathrm{P} \ne \mathrm{NP}$ |
| algoritmo polinomiale per Vertex Cover / un NP-completo XYZ | $\mathrm{P} = \mathrm{NP}$: ogni problema di NP si riduce a XYZ in tempo polinomiale, e componendo si ottiene un algoritmo polinomiale |
| si prova $\mathrm{P} \subsetneq \mathrm{NP}$ | i problemi NP-completi non sono in P; in $\mathrm{NP} \setminus \mathrm{P}$ ci sono tutti gli NP-completi (e, per il teorema di Ladner, anche problemi "intermedi") |
| problema NP-hard con algoritmo $\Theta(2^n)$: è NP-completo? (ottobre 2021) | non necessariamente: serve anche che sia **in NP** (può stare in EXP fuori da NP) |
| due NP-completi risolti in $O(f_1)$ e $O(f_2)$ (ottobre 2021) | si riducono l'uno all'altro: $f_1(n) = O(f_2(p(n)) + q(n))$ e viceversa, con $p, q$ polinomi |
| A NP-completo: si riduce a SAT? SAT si riduce ad A? (febbraio 2022) | sì e sì (A è in NP e SAT è in NP); le complessità differiscono al più per una composizione polinomiale |
| "cammino minimo in P, quindi in NP, quindi P = NP" (settembre 2022) | errore: serve un algoritmo polinomiale per un problema NP-**completo** |
| MTND che accetta in $\Theta(n^2)$: quanto impiega una MT deterministica? (ottobre 2021) | simulazione in ampiezza: $2^{O(n^2)}$ (con $d$ scelte per passo, $O(n^2 d^{n^2})$) |
| riducibilità transitiva (luglio 2019) | composizione di polinomi: [[14 - MC - Classi P e NP e NP-completezza#Robustezza della definizione]] |

## 3. Automi, espressioni regolari, grammatiche regolari

**Metodo generale** ([[10 - MC - Automi a stati finiti ed espressioni regolari|lezione 10]]):
- gli **stati** ricordano solo l'informazione necessaria (parità, resto, ultimi simboli letti, quanta parte di un pattern si è già vista);
- per "contiene $w$" si costruisce l'automa cerca-sottostringa (stati $0, \dots, |w|$, con i ritorni corretti sui mismatch); per "**non** contiene" lo si complementa;
- per "contiene $w_1$ **e** $w_2$" si usa l'automa **prodotto**;
- da ER ad ASF con le costruzioni di chiusura, poi la costruzione per sottoinsiemi se serve un ASFD;
- da ASF a grammatica: arco $A \xrightarrow{c} B$ ⇒ $A \to cB$ (e $A \to c$ se $B$ è finale);
- da grammatica/ASF a ER con le equazioni e il lemma di Arden.

| esercizio (traccia) | idea |
|---|---|
| contiene 010 e 111 (giugno 2019 A) | prodotto di due cerca-sottostringa |
| almeno due 1 e uno 0 (giugno 2019 B) / due 1 adiacenti e uno 0 (maggio 2020) | stati (numero di 1 fino a 2) × (visto uno 0) |
| numero pari di 0 e pari di 1 (luglio 2019); dispari di $a$ e dispari di $b$ (febbraio 2020) | automa delle parità PP/PD/DP/DD |
| multipli di 5 (settembre 2019); multipli di 3 (febbraio 2022) | ultima cifra; resto della somma delle cifre |
| ER $bb((aa)^* + b)^*a$ → ASF e grammatica regolare (gennaio 2020) | chiusura, poi archi → produzioni |
| ogni 1 seguito da 010 / preceduto da 00 (giugno 2021) | automa, grammatica tipo 3, ER |
| non contiene 101 (ottobre 2021) | $0^*(1^+00^+)^*(1^* + 1^+0)$ |
| se contiene $aba$ allora non contiene $bb$ (ottobre 2021) | complemento di "contiene $aba$" ∪ "non contiene $bb$" |
| non contiene $aba$ (settembre 2021) | cerca-sottostringa complementato |
| contiene / non contiene le ultime 3 cifre della matricola (aprile e giugno 2022, luglio 2023); contiene $a$ ma non $b$ (settembre 2022) | cerca-sottostringa su $\{0, \dots, 9\}$; per $a$/$b$: 3 stati (niente, visto $a$, visto $b$ = pozzo) |
| ASFD per $(a + bb)^*ab^*$ (febbraio 2022) | ASFND e sottoinsiemi |
| grammatica regolare per $(00 + 0^*11)^*1$ (settembre 2022) o $(0 + 11)^*1$ (giugno 2023) | ASF, poi produzioni |
| stringhe binarie senza 11 (giugno 2022) / senza 01 (giugno 2023) | $S \to 0S \mid 1A \mid \varepsilon$, $A \to 0S \mid \varepsilon$ / $1^*0^*$: $S \to 1S \mid 0A \mid \varepsilon$, $A \to 0A \mid \varepsilon$ |
| ASFND vs ASFD (settembre 2021) | stessi linguaggi (costruzione per sottoinsiemi) |
| linguaggio finito ⇒ regolare; unione di regolari è regolare (giugno 2023) | automa ad albero; costruzione dell'unione |

## 4. Grammatiche libere dal contesto

**Metodo**: per **generare** un linguaggio si "pareggiano" i simboli che devono essere in numero uguale con una produzione ricorsiva centrale ($S \to aSb$) e si aggiungono gli extra; per **riconoscere** il linguaggio generato si calcolano alcune derivazioni e si generalizza; per l'**ambiguità** si esibiscono due alberi per la stessa stringa; per il **tipo** si cerca il tipo più restrittivo del *linguaggio*, non della grammatica data.

| esercizio | soluzione |
|---|---|
| $a^n b^m$ con $m > n$ (giugno 2019) | $S \to aSb \mid B$, $B \to bB \mid b$ |
| $0^n 1^m$ con $m < n$ | $S \to 0S1 \mid A$, $A \to 0A \mid 0$ |
| $S \to aAb \mid aSb$, $A \to aaAbb \mid ab$ (giugno 2019, settembre 2021) | $a^n b^n$, $n \ge 2$; ambigua; $A \to aaAbb$ inutile ([[09 - MC - Grammatiche e gerarchia di Chomsky#Esempi di grammatiche (25/03/2022)]]) |
| $S \to aS \mid aA$, $A \to bA \mid b$ (luglio 2019) | $a^+ b^+$, tipo 3, non ambigua |
| $S \to Sa \mid Ab \mid A$, $A \to Ab \mid b$ (febbraio 2020) | $b^+ a^*$; ambigua ($bb$: $S \to Ab$ con $A \to b$, oppure $S \to A \to Ab$) |
| $S \to aSc \mid aTc \mid ac \mid bc$, $T \to bTc \mid bc$ (maggio 2020) | tipo 2; ambigua (è l'esempio della [[12 - MC - Parsing bottom-up\|lezione 12]]) |
| $S \to SaS \mid SbS \mid c$ (giugno 2021) | $c((a + b)c)^*$; ambigua ($cacbc$ ha due alberi); non ambigua: $S \to Sac \mid Sbc \mid c$ |
| $S \to SS \mid (S) \mid ()$ (febbraio 2022) | parentesi bilanciate non vuote; non LL(1) (ricorsione sinistra, prefissi comuni); con $S \to SS \mid (S) \mid \varepsilon$ si aggiunge $\varepsilon$ ed è ambigua |
| $S \to A \mid bSc \mid aa$, $A \to S \mid B$ (giugno 2023) | $b^n aa c^n$; ambigua per il ciclo $S \to A \to S$; non ambigua: $S \to bSc \mid aa$, che è anche LL(1) |
| espressioni con `id`, `+`, `-`, parentesi, non ambigua (luglio 2019, febbraio 2020) | $E \to E + T \mid E - T \mid T$, $T \to \mathrm{id} \mid (E)$; non è di tipo 3 perché le parentesi vanno bilanciate (pumping lemma su $(^n \mathrm{id})^n$) |
| espressioni booleane, formule CNF, formule 3CNF in $a, b, c$ (2019–2022) | stessa struttura a livelli: $E \to E \vee T \mid T$, $T \to T \wedge F \mid F$, $F \to \neg F \mid (E) \mid i$ |
| concatenazione di due CF è CF (settembre 2022) | $S \to S_1 S_2$ con alfabeti non terminali disgiunti |
| "aumentare/diminuire le stringhe cambia il tipo?" (luglio 2021) | falso ([[09 - MC - Grammatiche e gerarchia di Chomsky#Esempi di grammatiche (25/03/2022)]]) |
| $0^h 1^k$, $h > k > 0$ (o $h < k$): CF e non regolare (luglio 2021) | grammatica + pumping lemma ([[10 - MC - Automi a stati finiti ed espressioni regolari#Pumping lemma]]) |
| una grammatica di tipo 3 può essere ambigua? (luglio 2021) | sì, per esempio $S \to aS \mid aA$, $A \to aA \mid a$ genera $aa$ in due modi; ma ogni linguaggio regolare ha una grammatica regolare non ambigua (quella di un ASFD) |
| gerarchia di Chomsky, proprietà rilevante di ogni tipo (giugno 2019, luglio 2023) | tabella della [[09 - MC - Grammatiche e gerarchia di Chomsky#Gerarchia di Chomsky]] |

## 5. Parsing

### FIRST, FOLLOW, LL(1)

**Metodo** ([[11 - MC - Analisi sintattica top-down e automi a pila|lezione 11]]): (1) FIRST di ogni non terminale e di ogni parte destra; (2) FOLLOW partendo da $\$ \in \mathrm{FOLLOW}(S)$; (3) SELECT di ogni produzione; (4) LL(1) se le produzioni sullo stesso non terminale hanno SELECT disgiunti. Se non lo è: eliminare la ricorsione sinistra, fattorizzare.

| esercizio | soluzione |
|---|---|
| $S \to T\$$, $T \to (T)T \mid \varepsilon$ (gennaio 2020) | $\mathrm{SELECT}(T \to (T)T) = \{(\}$, $\mathrm{SELECT}(T \to \varepsilon) = \mathrm{FOLLOW}(T) = \{\$, )\}$: disgiunti, **è LL(1)** |
| $S \to A \mid xAy$, $A \to y \mid yxA$ (settembre 2021) | $A \to y$ e $A \to yxA$ hanno prefisso comune: non LL(1). Fattorizzando: $A \to yA'$, $A' \to xA \mid \varepsilon$; $\mathrm{SELECT}(A' \to \varepsilon) = \mathrm{FOLLOW}(A') = \{\$, y\}$, disgiunto da $\{x\}$: LL(1) |
| $S \to ACxA$, $C \to xy$, $A \to yB$, $B \to \varepsilon \mid xyB$ (aprile 2022) | $L = y(xy)^*\,xy\,x\,y(xy)^*$; $\mathrm{FOLLOW}(B) = \mathrm{FOLLOW}(A) = \{x, \$\}$ interseca $\mathrm{SELECT}(B \to xyB) = \{x\}$: **non** LL(1) |
| $S \to AxyxA$, $A \to yB$, $B \to \varepsilon \mid xyB$ (luglio 2023) | stesso conflitto su $x$: non LL(1) |
| grammatica LL(1) per $\{a^n \mid n \ge 1\}$ (maggio 2020) | $S \to aS'$, $S' \to aS' \mid \varepsilon$ |
| grammatica LL(1) per le parentesi bilanciate e parse tree di `((()()))()` (settembre 2019) | $S \to (S)S \mid \varepsilon$ |
| FIRST e FOLLOW con $\varepsilon$-produzioni (giugno 2021) | applicare l'algoritmo iterativo fino al punto fisso, attenzione ai non terminali annullabili |

**Domande teoriche**: descrivere un parser top-down (input: token; output: albero o errore; algoritmo: discesa ricorsiva o tabella con pila), requisiti della grammatica (non ambigua, niente ricorsione sinistra, niente prefissi comuni, SELECT disgiunti), vantaggi (semplice, efficiente, buona diagnostica) e svantaggi (classe di grammatiche ristretta, bisogna trasformarle).

### Bottom-up e LR(0)

*Febbraio 2022, aprile 2022, giugno 2022, luglio 2023*. Cosa sono shift e reduce; caratteristiche del parsing bottom-up; definizione di LR(0).

> [!example] $S \to aS \mid ab \mid aSb$ è LR(0)? (giugno 2022)
> Si aumenta con $S' \to S$. $s_0 = \{S' \to \cdot S,\ S \to \cdot aS \mid \cdot ab \mid \cdot aSb\}$. Con $a$: $s_1 = \{S \to a \cdot S \mid a \cdot b \mid a \cdot Sb\}$ più la chiusura su $S$. Da $s_1$ con $S$: $s_2 = \{S \to aS \cdot,\ S \to aS \cdot b\}$: un item **completo** insieme a uno **incompleto** ⇒ conflitto shift-reduce. **Non è LR(0)** (servirebbe guardare se il prossimo simbolo è $b$).

## 6. Macchine di Turing e calcolabilità

| esercizio | dove studiarlo |
|---|---|
| definizione di MT (deterministica, a un nastro), configurazioni, accettazione | [[08 - MC - Macchine di Turing e calcolabilità#Funzioni calcolabili secondo Turing]] |
| cosa calcola la MT in figura, configurazione finale (giugno e luglio 2021) | simulare passo per passo su un input piccolo, poi descrivere ad alto livello |
| MT a due nastri: perché "superiore"? (giugno 2019) | stesso potere, più veloce (fino a quadraticamente) |
| MT non deterministica: condizioni di accettazione e rifiuto; perché "superiore"? (2019, 2022) | [[08 - MC - Macchine di Turing e calcolabilità#MT non deterministiche (MTND)]] |
| nastro semi-infinito ha pieno potere? (settembre 2019, 2021) | piegare il nastro su due tracce |
| MT universale: input, output, importanza; può simulare se stessa? (2020, 2022, 2023) | [[08 - MC - Macchine di Turing e calcolabilità#Macchina di Turing universale]] |
| tesi di Church-Turing; vale per gli ASF/ASFND? (2021, 2022) | [[Tesi di Church-Turing]] |
| decidibile, indecidibile, semidecidibile; esempi (2020–2023) | [[Linguaggio decidibile]], [[Linguaggio semidecidibile]] |
| Halting Problem: decidibile? semidecidibile? prova (2021–2023) | [[07 - MC - Halting Problem\|lezione 7]] |
| "$M$ su $x$ andrà in loop?" (giugno 2023) | complemento di HP: indecidibile, nemmeno semidecidibile |
| programmi Python sintatticamente corretti vs HP (settembre 2021) | il primo è decidibile (un parser, linguaggio CF), HP è semidecidibile non decidibile |
| $Z$ indecidibile: il complemento è decidibile? $L_1 \cup L_2$ con entrambi indecidibili? (febbraio 2022) | i decidibili sono chiusi per complemento, quindi $\bar Z$ è indecidibile; $L_1 \cup L_2$ può essere decidibile ($L \cup \bar L = \Sigma^*$) o no ($L \cup L = L$) |
| numerabilità e diagonalizzazione: linguaggi su $\{0, 1\}$ non numerabili (settembre 2019) | [[06 - MC - Cardinalità e diagonalizzazione#L'insieme delle parti dei naturali non è numerabile]] |

## 7. Logica e SAT

| esercizio | metodo |
|---|---|
| illustrare DPLL, costo, simularlo su una formula CNF (gennaio 2020, luglio 2021) | unit propagation, pure literal, scelta e backtracking; costo $O(2^n)$ ([[13 - MC - Forme normali e algoritmo DPLL#Esempio (dalla prova di luglio 2021)]]) |
| pseudo-codice di DPLL; si applica a 4DNF? (giugno 2022) | per una DNF basta il test lineare sui termini ([[13 - MC - Forme normali e algoritmo DPLL#DNF e soddisfacibilità]]) |

> [!example] DPLL su $(a \vee b \vee \neg c) \wedge (\neg b \vee d) \wedge (\neg a \vee c \vee d \vee \neg e) \wedge (\neg a \vee b \vee \neg d \vee e) \wedge (c \vee d \vee \neg e) \wedge (c \vee \neg d \vee \neg e) \wedge (a \vee c \vee d \vee e) \wedge (a \vee c \vee d \vee \neg e)$ (gennaio 2020)
> Numerando le clausole da 1 a 8: nessuna è unitaria e nessun letterale è puro (ogni variabile compare con entrambi i segni; per esempio $c$ è negata solo nella clausola 1).
> 1. Si sceglie $c = 1$: le clausole 3, 5, 6, 7, 8 (che contengono $c$) spariscono; la clausola 1 **perde** $\neg c$ e diventa $(a \vee b)$. Restano $(a \vee b)$, $(\neg b \vee d)$, $(\neg a \vee b \vee \neg d \vee e)$.
> 2. Ora $e$ compare solo positivo: è puro, $e = 1$ cancella la terza clausola.
> 3. $a$ compare solo positivo in $(a \vee b)$: puro, $a = 1$.
> 4. Resta $(\neg b \vee d)$: $\neg b$ è puro, $b = 0$. Formula vuota: **soddisfacibile**.
>
> Assegnazione: $a = 1$, $b = 0$, $c = 1$, $e = 1$, $d$ qualunque. Verifica: la clausola 1 è vera per $a$, la 2 per $\neg b$, la 4 per $e$, tutte le altre per $c$. ✓
>
> Attenzione al passo 1: quando si assegna $c = 1$, le clausole con $\neg c$ non spariscono, perdono solo quel letterale.

## 8. Altri argomenti (parte di algoritmi)

Alcune tracce del 2019–2020 includono esercizi della parte di algoritmi di Fondamenti II:
- **Programmazione dinamica, LCS** (luglio 2019, settembre 2019, maggio 2020): completare $L[i, j] = L[i-1, j-1] + 1$ se $x_i = y_j$, altrimenti $L[i, j] = \max(L[i-1, j], L[i, j-1])$; costo $\Theta(nm)$; differenza con il divide et impera (sottoproblemi sovrapposti, si memorizzano i risultati).
- **Boyer-Moore** (novembre 2019): vedi [[Algoritmo di Boyer-Moore]] nel corso di Algoritmi e Strutture Dati.

## Riepilogo

> [!summary] Cosa ripassare per primo
> 1. Contare le esecuzioni e risolvere ricorrenze ([[02 - MC - Notazione asintotica|2]], [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza|4]]).
> 2. Definizioni di P/NP/NP-completo e conseguenze ipotetiche ([[14 - MC - Classi P e NP e NP-completezza|14]]).
> 3. Costruire ASF ed ER, passare fra ASF, grammatiche ed ER ([[10 - MC - Automi a stati finiti ed espressioni regolari|10]]).
> 4. Grammatiche CF: linguaggio, ambiguità, tipo ([[09 - MC - Grammatiche e gerarchia di Chomsky|9]]).
> 5. FIRST/FOLLOW/LL(1) e LR(0) ([[11 - MC - Analisi sintattica top-down e automi a pila|11]], [[12 - MC - Parsing bottom-up|12]]).
> 6. Halting Problem e MT universale ([[07 - MC - Halting Problem|7]], [[08 - MC - Macchine di Turing e calcolabilità|8]]).
