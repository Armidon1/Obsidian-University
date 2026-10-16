---
title: Macchine di Turing e calcolabilità
aliases:
  - MC — Macchine di Turing e calcolabilità
tags:
  - modelli-di-calcolo
  - calcolabilita
  - macchina-di-turing
  - church-turing
source: Macchine di Turing e calcolabilità.pdf (cap. 12); Informatica Teorica (Crescenzi), parte I
---

# Macchine di Turing e calcolabilità

> [!abstract]
> Le lezioni [[06 - MC - Cardinalità e diagonalizzazione|6]] e [[07 - MC - Halting Problem|7]] hanno ragionato su "programmi" in generale (anche in C). Per parlare di calcolabilità in modo rigoroso serve però un **modello di calcolo** preciso, semplice abbastanza da poterci dimostrare teoremi. È la **macchina di Turing** (MT): un automa a stati finiti con un nastro illimitato su cui leggere e scrivere. Questa lezione definisce la MT come **trasduttore** (calcola funzioni) e come **riconoscitore** (decide o accetta linguaggi), introduce le varianti **multinastro** e **non deterministiche** mostrando che non aumentano il potere di calcolo (ma possono cambiarne il costo), la **macchina universale** (un interprete), la dimostrazione dell'**indecidibilità della terminazione** e le relazioni con i calcolatori reali (le **RAM**). Il collegamento con le [[09 - MC - Grammatiche e gerarchia di Chomsky|grammatiche]]: le MT accettano esattamente i linguaggi di **tipo 0**. Il collegamento con la [[14 - MC - Classi P e NP e NP-completezza|complessità]]: simulare una MT non deterministica con una deterministica costa un tempo esponenziale, ed è il cuore del problema P vs NP.
> Mappa del corso: [[MOC - Modelli di Calcolo]].

## Funzioni calcolabili secondo Turing

Vedi [[Macchina di Turing]].

La macchina di Turing è un **automa con testina di lettura/scrittura** su un **nastro bidirezionale "potenzialmente" illimitato**. A ogni istante la macchina si trova in uno **stato**, appartenente a un insieme finito, e legge un carattere sul nastro. La **funzione di transizione**, in modo deterministico, fa scrivere un carattere, fa spostare la testina in una direzione o nell'altra e fa cambiare lo stato.

Le macchine sono state introdotte da A. M. Turing nel 1935–36 con lo scopo di:
- dare una **definizione formale del concetto di algoritmo**;
- dimostrare l'**esistenza di problemi non risolubili** mediante algoritmi.

Le macchine di Turing:
- consentono il riconoscimento, almeno "parziale" (semidecidibilità, accettazione), di **tutti i linguaggi di tipo 0**;
- sono in grado di simulare ogni linguaggio di programmazione e ogni altro modello di calcolo (**tesi di Church-Turing**).

> [!important] Definizione (macchina di Turing)
> $$M = \langle \Sigma, \flat, K, q_0, F, \delta \rangle$$
> - $\Sigma$: alfabeto di simboli;
> - $\flat$: carattere speciale, **spazio bianco** (*blank*); si scrive $\Sigma_\flat = \Sigma \cup \{\flat\}$;
> - $K$: insieme **finito** di stati;
> - $q_0 \in K$: stato iniziale;
> - $F \subseteq K$: insieme di stati finali;
> - $\delta$: funzione di transizione (**parziale**)
>   $$\delta: K \times \Sigma_\flat \to K \times \Sigma_\flat \times \{d, s, i\}$$
>   dove $d, s, i$ indicano spostamento a **d**estra, a **s**inistra e **i**mmobilità della testina.

$\delta(q, a) = (q', a', m)$ si legge: "nello stato $q$, leggendo $a$, scrivi $a'$, sposta la testina secondo $m$ e passa nello stato $q'$". Se $\delta(q, a)$ non è definita, la macchina si ferma.

> [!example] Esempio
> Si consideri la macchina con transizioni (qui $\flat$ è il blank)
> $$\delta(q_0, a) = (q_0, b, d) \quad \delta(q_0, b) = (q_0, a, d) \quad \delta(q_0, \flat) = (q_1, c, d) \quad \delta(q_1, \flat) = (q_2, \flat, s)$$
> con stato iniziale $q_0$ e stato finale $q_2$.
> - **Input `aaabb`**, testina sul primo carattere: in $q_0$ la macchina scambia $a \leftrightarrow b$ procedendo verso destra (`bbbaa`); al primo blank scrive `c` e passa in $q_1$; al blank successivo torna indietro di una casella e si ferma in $q_2$, **finale**. Il nastro contiene `bbbaac`.
> - **Input `aacbb`**: scambia le prime due ($bb$), poi legge `c` in $q_0$: la transizione non è definita e la macchina si ferma in $q_0$, **non finale** (computazione rifiutante, o "errore").
>
> (Nella dispensa il blank e la lettera $b$ sono stampati con lo stesso simbolo; questa è la lettura coerente delle quattro regole.)

### Configurazioni e computazioni

Anche se il nastro è illimitato, su di esso **in ogni istante c'è un numero finito di caratteri diversi da $\flat$**.

> [!important] Configurazione
> Una **configurazione** è una terna costituita dalla (minima) porzione finita di nastro che contiene i simboli diversi da $\flat$, dalla posizione della testina e dallo stato corrente. Si rappresenta con una stringa di $\Sigma_\flat^* \cdot K \cdot \Sigma_\flat^+$: lo stato è scritto immediatamente prima del carattere osservato dalla testina.

Per esempio `abbbbq`$_i$`abbbbb` indica stato $q_i$, testina sulla `a` dopo le quattro `b`. Conoscere una configurazione e la funzione di transizione permette di determinare la configurazione successiva.

- Si assume di norma che all'inizio il nastro contenga l'input, il resto del nastro contenga $\flat$ e la testina sia sul primo carattere dell'input.
- **Configurazione iniziale**: stringa di $\{q_0\} \cdot \Sigma_\flat^+$.
- **Configurazione finale**: stringa di $\Sigma_\flat^* \cdot F \cdot \Sigma_\flat^+$ (la posizione della testina è in genere irrilevante).

> [!important] Transizioni e computazioni
> - $M$ determina una **transizione** da $c$ a $c'$, scritto $c \vdash c'$, se $c'$ si ottiene da $c$ applicando la funzione di transizione.
> - Una **computazione** è una sequenza, eventualmente infinita, di configurazioni $c_1 \vdash c_2 \vdash \dots \vdash c_i \vdash c_{i+1} \vdash \dots$
> - $c_1 \vdash^* c_2$ indica che esiste una computazione da $c_1$ a $c_2$ con un numero finito (eventualmente 0) di transizioni.
> - Una computazione finita $c_1 \vdash \dots \vdash c_n$ è **massimale** se non esiste $c$ tale che $c_n \vdash c$.

In ogni computazione c'è al più una configurazione finale: raggiunta una configurazione finale il calcolo termina. Il calcolo può terminare anche perché la configurazione successiva non è definita (la funzione di transizione non è definita per quella configurazione). Interessano le computazioni massimali $c_0 \vdash^* c_n$ con $c_n$ **finale**; le altre corrispondono a "errore" o "risultato non definito".

### Macchine trasduttrici

> [!important] Definizioni
> - Una **macchina di Turing trasduttrice** ha ogni configurazione finale del tipo $x \flat q y$, dove $x$ è il contenuto del nastro all'inizio (l'input resta, l'output è scritto alla sua destra).
> - Una macchina trasduttrice **calcola la funzione $f$** se per **tutte e sole** le $x$ su cui $f$ è definita esiste $q \in F$ tale che
> $$q_0 x \vdash^* x \flat q f(x)$$
> - Una funzione (parziale) $f$ per cui esiste una MT che la calcola si dice **calcolabile secondo Turing** (T-calcolabile).

$f$ può essere una funzione da $\Gamma^*$ a $\Gamma^*$ per un opportuno alfabeto $\Gamma \subseteq \Sigma$; in particolare una funzione numerica su interi in notazione binaria o decimale. Esempio: la funzione identità su $\{a, b\}^*$ è calcolata da una macchina che esegue $q_0 x \vdash^* x \flat q x$, con $q$ finale (copia l'input a destra).

Le MT sono uno dei modelli di calcolo più **semplici** e, al tempo stesso, più **potenti**: le funzioni T-calcolabili sono la classe più ampia di funzioni calcolabili mediante algoritmi che si conosca.

> [!important] Tesi di Church-Turing
> Church e Turing hanno avanzato l'ipotesi che **qualunque funzione calcolabile mediante algoritmi sia calcolabile mediante macchine di Turing**. Per questo si dice semplicemente "funzione calcolabile" invece di "T-calcolabile".

Vedi [[Tesi di Church-Turing]]. È una **tesi**, non un teorema: "calcolabile mediante algoritmi" non è un concetto formale, quindi non si può dimostrare; è sostenuta dal fatto che tutti i modelli proposti si sono rivelati equivalenti alle MT ([[#Funzioni non calcolabili e problemi indecidibili|vedi sotto]]).

> [!tip] Esercizi della dispensa
> Realizzare le MT che calcolano $f(x) = x + 1$ (in binario) e $f(x, y) = x + y$ (in decimale).
> *Traccia per $x + 1$*: si va a destra fino al primo blank, si torna indietro di una casella; poi, verso sinistra, ogni `1` diventa `0` (riporto) finché si trova uno `0` o il blank, che diventa `1`. (Per rispettare la convenzione "trasduttrice" bisognerebbe lasciare $x$ intatto e scrivere il risultato a destra: prima si copia, poi si incrementa la copia.)

## Insiemi e linguaggi decidibili e semidecidibili

Le MT si usano anche per **riconoscere linguaggi** (insiemi), cioè per risolvere problemi di decisione.

> [!important] Computazioni accettanti e rifiutanti
> - Una computazione massimale $\langle c_0, \dots, c_n \rangle$ è **accettante** se $c_0$ è iniziale e $c_n$ è finale: **responso affermativo**.
> - È **rifiutante** se $c_0$ è iniziale e $c_n$ non è finale: **responso negativo**.
> - Una computazione **non terminante** non dà **nessun responso**.

Informalmente:
- $M$ **riconosce** un linguaggio $L \subseteq \Sigma^*$ se per **ogni** $x \in \Sigma^*$ è in grado di stabilire se $x \in L$ oppure no;
- $M$ **accetta** $L$ se per tutte e sole le $x \in L$ è in grado di stabilirne l'appartenenza, ma se $x \notin L$ non garantisce un comportamento prestabilito: può dare una risposta negativa ma anche non darne alcuna.

> [!important] Definizioni formali
> - $M$ **riconosce (decide)** $L$ se per ogni $x \in \Sigma^*$ esiste $q \in K$ tale che $q_0 x \vdash^* \alpha q \beta$ con $\alpha \in \Sigma_\flat^*$, $\beta \in \Sigma_\flat^+$, la computazione è massimale, e $q \in F$ **se e solo se** $x \in L$.
> - Un linguaggio riconosciuto da una MT è **decidibile**; altrimenti è **indecidibile**.
> - $M$ **accetta** $L$ se per **tutte e sole** le $x \in L$ esiste $q \in F$ tale che $q_0 x \vdash^* \alpha q \beta$.
> - Un linguaggio accettato da una MT è **semidecidibile**.

Vedi [[Linguaggio decidibile]] e [[Linguaggio semidecidibile]].

- Non è detto che una MT possa sempre riconoscere un linguaggio: **esistono linguaggi di tipo 0 non decidibili**.
- Se un linguaggio è decidibile è anche semidecidibile. La famiglia dei semidecidibili **contiene strettamente** quella dei decidibili: esistono linguaggi semidecidibili ma indecidibili (per esempio il linguaggio della terminazione).

> [!tip] Esercizi della dispensa
> Realizzare le MT che accettano $\{wcw^R \mid w \in (a+b)^+\}$, $\{ww^R \mid w \in (a+b)^+\}$, $\{wcw \mid w \in (a+b)^+\}$.
> *Traccia per $wcw^R$ su un nastro*: si cancella il primo simbolo (ricordandolo nello stato), si corre fino all'ultimo simbolo, si controlla che sia uguale e lo si cancella; si torna all'inizio e si ripete; si accetta quando resta solo `c`. Costo $O(n^2)$. Con due nastri basta $O(n)$ (vedi sotto).

## Macchine di Turing multinastro e non deterministiche

Si possono definire molte **varianti** di MT: a più nastri, non deterministiche, con alfabeto limitato a due soli simboli, con nastro semi-infinito, ecc. **Tutte queste varianti sono computazionalmente equivalenti**: calcolano le stesse funzioni e riconoscono (o accettano) gli stessi linguaggi. Possono però avere **tempi di calcolo** diversi e usare diverse quantità di **spazio**.

### MT multinastro (MTM)

Vedi [[Macchina di Turing multinastro]].

> [!important] Definizione
> Macchina di Turing a $k$ nastri: $M_k = \langle \Sigma, \flat, Z_0, K, q_0, F, \delta^{(k)} \rangle$, con $Z_0$ carattere speciale **iniziale** e
> $$\delta^{(k)}: K \times \Sigma_\flat^k \to K \times \Sigma_\flat^k \times \{d, s, i\}^k$$
> (in un passo si leggono $k$ simboli, uno per nastro, se ne scrivono $k$ e si muovono le $k$ testine indipendentemente).

- **Configurazione**: $q\#\alpha_1 \uparrow \beta_1 \# \alpha_2 \uparrow \beta_2 \# \dots \# \alpha_k \uparrow \beta_k$, dove $\alpha_i \uparrow \beta_i$ indica contenuto e posizione della testina sul nastro $i$ ($\alpha_i$ eventualmente vuota, il primo carattere di $\beta_i$ è quello osservato).
- **Configurazione iniziale**: $q_0 \# \uparrow \beta_1 \# \uparrow Z_0 \# \dots \# \uparrow Z_0$: l'input sta sul primo nastro, gli altri contengono $Z_0$.
- **Configurazione finale**: $q \in F$. Transizioni e computazioni sono analoghe alle MT.

Esempi di macchine a più nastri:
- un **trasduttore** con un nastro di input (sola lettura), uno di output (sola scrittura) e uno o più nastri di lavoro (lettura e scrittura, bidirezionali);
- un **riconoscitore** con un nastro di input (sola lettura, unidirezionale) e uno o più nastri di lavoro.

> [!note] ASF e automi a pila come MT
> - L'[[Automa a stati finiti|automa a stati finiti]] è una MT con **un solo nastro, di sola lettura, unidirezionale**.
> - L'[[Automa a pila|automa a pila]] è una MT a **due nastri**: il primo di sola lettura e unidirezionale (*one way*), il secondo usato in modo LIFO, come una pila.
>
> La gerarchia dei modelli corrisponde alla gerarchia delle restrizioni sui nastri.

> [!example] MTM per riconoscere $xcx^R$, $x \in \{a, b\}^+$
> Due nastri: uno di input, monodirezionale a sola lettura, e uno di lavoro usato **come pila**. Durante la scansione di $x$, fino a `c`, $x$ viene copiata sul nastro di lavoro (in maiuscolo); durante la scansione di $x^R$ si confrontano i caratteri con quelli sul nastro di lavoro, che si percorre all'indietro. Stati: $q_0$ (scansione di $x$), $q_1$ (scansione di $x^R$), $q_2$ (finale).
>
> | regola | significato |
> |---|---|
> | $\delta(q_0, a, Z_0) = \langle q_0, a, A, d, d \rangle$, $\delta(q_0, b, Z_0) = \langle q_0, b, B, d, d \rangle$ | copiatura iniziale |
> | $\delta(q_0, a, \flat) = \langle q_0, a, A, d, d \rangle$, $\delta(q_0, b, \flat) = \langle q_0, b, B, d, d \rangle$ | copiatura a regime |
> | $\delta(q_0, c, \flat) = \langle q_1, c, \flat, d, s \rangle$ | passaggio alla verifica |
> | $\delta(q_1, a, A) = \langle q_1, a, A, d, s \rangle$, $\delta(q_1, b, B) = \langle q_1, b, B, d, s \rangle$ | verifica positiva |
> | $\delta(q_1, \flat, \flat) = \langle q_2, \flat, \flat, i, i \rangle$ | accettazione |
>
> Computazione con input `bacab`: dopo aver copiato `ba` (nastro di lavoro `BA`), legge `c` e passa in $q_1$ con la testina di lavoro su `A`; confronta `a` con `A`, poi `b` con `B`; con entrambi i nastri sul blank accetta in $q_2$. Con input `acb`: copia `a`, legge `c`, poi in $q_1$ legge `b` contro `A`: nessuna regola, si ferma in $q_1$ (rifiuto). Costo $O(n)$.

> [!warning] Correzione
> Nella dispensa la seconda regola di verifica positiva è scritta $\delta(q_0, b, B) = \langle q_1, b, B, d, s \rangle$: lo stato di partenza deve essere $q_1$ (in $q_0$ si sta ancora copiando, e il nastro di lavoro sotto la testina contiene $\flat$, non $B$).

> [!example] MTM per riconoscere $xx^R$
> Con tre nastri: uno di input e due di lavoro. Si copia la stringa su **entrambi** i nastri di lavoro; poi si riporta indietro la testina di uno dei due, e si scandiscono i due nastri **in senso contrario** confrontando i caratteri: se il nastro letto da sinistra e quello letto da destra coincidono simbolo per simbolo, la stringa è palindroma. (Qui, a differenza di $xcx^R$, non c'è un separatore che indichi la metà: confrontare la copia con il suo rovescio evita di doverla indovinare.)

> [!tip] Esercizio
> Realizzare una MT con due nastri (il primo di sola lettura, il secondo di lettura e scrittura, entrambi bidirezionali) che riconosce $\{xcx \mid x \in (a+b)^+\}$. *Traccia*: si copia $x$ sul secondo nastro fino a `c`, si riporta la testina del secondo nastro all'inizio della copia, poi si confrontano i due nastri procedendo **entrambi verso destra**.

#### Equivalenza tra MTM e MT

Strumento di lavoro: la MT con **nastro suddiviso in tracce**. Se il nastro ha $h$ tracce, la testina legge e scrive $h$ caratteri contemporaneamente. La corrispondenza con una MT normale è immediata: se sulle tracce si usano gli alfabeti $\Sigma_1, \dots, \Sigma_h$, una MT equivalente ha un alfabeto $\Sigma$ con $|\Sigma| \ge |\Sigma_1| \times \dots \times |\Sigma_h|$ (ogni simbolo è una "colonna" di $h$ simboli).

> [!important] Teorema
> Data una MTM a $k$ nastri $M = \langle \Sigma, \flat, K, q_0, F, \delta^{(k)} \rangle$, esiste una MT che **simula $t$ passi di $M$ in $O(t^2)$ passi**, usando un alfabeto di cardinalità $O((2|\Sigma|)^k)$.

*Dimostrazione.* Si costruisce una MT $M'$ con nastro diviso in **$2k$ tracce**, poi una MT $M''$ con un solo nastro equivalente a $M'$.
- Le $k$ tracce di posto **pari** di $M'$ rappresentano i $k$ nastri di $M$; sulle $k$ tracce di posto **dispari** un carattere marcatore $\uparrow$ indica la posizione delle testine.
- Per simulare una transizione $\delta^{(k)}(q_i, \sigma_{i1}, \dots, \sigma_{ik}) = \langle q_j, \sigma_{j1}, \dots, \sigma_{jk}, z_{j1}, \dots, z_{jk} \rangle$, $M'$ deve rintracciare le posizioni dei marcatori, scrivere, spostare i marcatori e cambiare stato.
- Per ogni passo di $M$, $M'$ esegue un numero di passi proporzionale alla **distanza fra i due marcatori più lontani**; dopo $t$ passi due marcatori possono essersi allontanati al più di $O(t)$ caselle. Se $M$ esegue $t$ passi, $M'$ ne esegue $O(t^2)$; $M''$ esegue gli stessi passi di $M'$.
- L'alfabeto di $M''$ deve codificare stringhe di $2k$ simboli: $k$ in $\{\flat, \uparrow\}$, uno in $\Sigma_\flat$, $k-1$ in $\Sigma \cup \{\flat, Z_0\}$: $|\Sigma''| = 2^k(|\Sigma| + 1)(|\Sigma| + 2)^{k-1} = O((2|\Sigma|)^k)$. $\square$

Più nastri **non aumentano il potere** di calcolo e lo accelerano **al più quadraticamente**: un rallentamento polinomiale, che non cambia la classe P.

### MT non deterministiche (MTND)

Vedi [[Macchina di Turing non deterministica]].

> [!important] Definizione
> $M = \langle \Sigma, \flat, K, q_0, F, \delta_N \rangle$, con funzione (parziale) di transizione
> $$\delta_N: K \times \Sigma_\flat \to \mathcal{P}(K \times \Sigma_\flat \times \{d, s, i\})$$
> La macchina può eseguire **più transizioni** a partire dalla stessa configurazione.
>
> **Grado di non determinismo**: $\nu(M) = \max |\delta_N(q_i, \sigma_j)|$.

Una computazione non deterministica si rappresenta con un **albero di computazioni deterministiche**: i nodi sono configurazioni, gli archi transizioni. Il grado di non determinismo è il massimo numero di figli di un nodo.

> [!important] Accettazione
> Una MTND **accetta** una stringa se nell'albero di computazione esiste **almeno un ramo** che corrisponde a una computazione accettante (almeno una foglia è una configurazione finale).

Si parla di **accettazione** e non di riconoscimento perché c'è **asimmetria** fra accettare e rifiutare: per accettare basta che esista un cammino accettante, per rifiutare bisogna che **tutti** i cammini siano rifiutanti.

#### Equivalenza tra MT e MTND

> [!important] Teorema
> Le MTND hanno lo stesso potere computazionale delle MT. Data una MTND $M$ con grado di non determinismo $d$, esiste una MT $M'$ equivalente che **simula $k$ passi di $M$ in $O(k\,d^k)$ passi**.

*Dimostrazione.* $M'$ **visita in ampiezza** l'albero di computazione di $M$. Ha tre nastri:
1. il nastro 1 contiene l'input;
2. il nastro 2 serve a generare, in ordine lessicografico (prima le più corte), tutte le sequenze finite di cifre fra 1 e $d$;
3. il nastro 3 è di lavoro.

Le transizioni di ogni insieme $\delta_N(q, \sigma)$ sono numerate da 1 a $d$. Per ogni sequenza generata sul nastro 2, $M'$ copia l'input sul nastro 3 e simula $M$ usando le cifre della sequenza per **scegliere** a ogni passo una delle $d$ transizioni: una sequenza di lunghezza $s$ corrisponde a una computazione di $M$ di $s$ passi. Per esempio, con $s = 4$, $d = 2$ e sequenza `2122`, $M'$ sceglie alla prima mossa la seconda transizione disponibile, alla seconda la prima, e così via. Se qualche foglia dell'albero di $M$ contiene uno stato finale, $M'$ la raggiunge in tempo finito; altrimenti non raggiunge mai uno stato finale.

Se $M$ termina in $k$ passi, $M'$ esamina le sequenze di lunghezza $j = 0, \dots, k$ (sono $d^j$, ognuna simulata in $O(j)$ passi):

$$O\Big(\sum_{j=0}^{k} j\,d^j\Big) = O(k\,d^k)$$

Per dimostrarlo: $\sum_{j=0}^k d^j = \frac{d^{k+1} - 1}{d - 1}$; derivando rispetto a $d$, $\sum_{j=1}^k j\,d^{j-1} = \frac{k d^{k+1} - (k+1)d^k + 1}{(d-1)^2}$, e quindi $\sum_{j=1}^k j\,d^j = O(k\,d^k)$. $\square$

> [!question] Perché in ampiezza e non in profondità?
> Perché un ramo dell'albero può essere **infinito** (una computazione che non termina): una visita in profondità potrebbe infilarsi in quel ramo e non tornare mai indietro, anche se un altro ramo accetta dopo pochi passi. La visita in ampiezza esamina i rami per lunghezza crescente e trova sempre un cammino accettante finito, se esiste.

> [!important] Il problema da un milione di dollari
> Una macchina non deterministica può "risolvere" un problema (per esempio accettare un linguaggio) in tempo **polinomiale** nella lunghezza della stringa, mentre la simulazione deterministica richiede tempo **esponenziale**. *Esiste una simulazione più efficiente? È possibile simulare una MTND con una MT deterministica in tempo polinomiale?* È il problema [[14 - MC - Classi P e NP e NP-completezza|P vs NP]].

### Linguaggi di tipo 0 e MT

> [!important] Teorema
> Un linguaggio $L$ è **semidecidibile se e solo se è di tipo 0**.

*Dimostrazione (traccia).*

**(i) Tipo 0 → MT.** Dato $L$ generato da una grammatica $G$ di tipo 0, si definisce una MT che lo accetta. Per semplicità si usa una MTND $M$ con 2 nastri (si sa che esiste una MT a un nastro che la simula). Il nastro $N_1$ contiene la stringa $x$ da accettare, il nastro $N_2$ le forme di frase via via derivate. Partendo dall'assioma $S$, $M$ applica in modo non deterministico le produzioni applicabili; dopo ogni applicazione, sempre in modo non deterministico, verifica se la forma di frase ottenuta è fatta di soli terminali e coincide con $x$: in tal caso termina in uno stato finale.

**(ii) MT → Tipo 0.** Data una MT $M$ che accetta $L$ (per tutte e sole le $x \in L$ esegue $q_0 x \vdash^* \alpha q_F \beta$, con un unico stato finale $q_F$), si costruisce una grammatica di tipo 0. I non terminali sono simboli ausiliari, simboli per gli stati di $M$ e simboli a **due piste** $\left[\begin{smallmatrix}\sigma_i\\ \sigma_j\end{smallmatrix}\right]$ (sopra un carattere di $\Sigma \cup \{\flat\}$, sotto un carattere di $\Sigma \cup \{\flat\}$). La grammatica:
1. introduce lo stato iniziale $q_0$;
2. genera una qualunque stringa $x$ di $\Sigma^*$ **su entrambe le piste**;
3. genera un numero arbitrario di $\flat$ a destra e a sinistra di $x$ (lo spazio di lavoro);
4. **simula $M$ sulla pista inferiore**: per ogni regola $\delta(q_k, \sigma_i) = (q_h, \sigma_l, d)$ c'è la produzione $q_k \left[\begin{smallmatrix}\sigma_j\\ \sigma_i\end{smallmatrix}\right] \to \left[\begin{smallmatrix}\sigma_j\\ \sigma_l\end{smallmatrix}\right] q_h$ per ogni $\sigma_j$ sulla pista superiore;
5. se e solo se la pista inferiore è una configurazione finale, trasforma la forma di frase nella stringa $x$ ancora presente sulla pista superiore (cancellando i blank e la pista inferiore).

Le produzioni iniziali sono del tipo $S \to A_1 q_0 A_2$, $A_2 \to \left[\begin{smallmatrix}\sigma_i\\ \sigma_i\end{smallmatrix}\right] A_2 \mid A_3$, $A_1 \to A_1 \left[\begin{smallmatrix}\flat\\ \flat\end{smallmatrix}\right] \mid \$$, $A_3 \to \left[\begin{smallmatrix}\flat\\ \flat\end{smallmatrix}\right] A_3 \mid \$$, e quelle finali cancellano marcatori e piste ($q_F \to A_4 A_5$, $A_1 A_4 \to \varepsilon$, $A_5 A_3 \to \varepsilon$, …). $\square$

> [!note] I linguaggi di tipo 1 sono decidibili
> In una grammatica di tipo 1 le forme di frase **non possono diminuire di lunghezza**. Per decidere se $x \in L$ basta generare tutte le forme di frase in ordine di lunghezza crescente fino a $|x|$ (sono in numero finito) e confrontare quelle di soli terminali con $x$. Vedi [[09 - MC - Grammatiche e gerarchia di Chomsky#Gerarchia di Chomsky|gerarchia di Chomsky]].

## Macchina di Turing universale

Vedi [[Macchina di Turing universale]].

Una MT si può **descrivere con una stringa di caratteri** e la descrizione si può fornire come input a un'altra MT. Ci sono vari modi:
- fornire la sequenza delle quintuple della funzione di transizione: $\#\#\, d_1 \#\# d_2 \#\# \dots \#\# d_n$, dove compare la quintupla $q_i \# \sigma_j \# q_h \# \sigma_k \# t_l$ se e solo se esiste la regola $\delta(q_i, \sigma_j) = (q_h, \sigma_k, t_l)$;
- sfruttare il fatto che ogni MT si può realizzare come **composizione di macchine elementari** e descriverla come sequenza di tali macchine.

Sia $D_M$ la descrizione di $M$.

> [!important] Teorema
> Esiste una MT $U$, con stato iniziale $q_{0U}$ (la **macchina di Turing universale**), che, data una qualunque descrizione $D_M$, realizza la computazione
> $$q_{0U}\, D_M \# x \vdash^* \alpha\, q_{fU}\, \beta \quad (q_{fU} \text{ finale})$$
> **se e solo se** $M$, con stato iniziale $q_0$, realizza la computazione $q_0 x \vdash^* \alpha\, q_f\, \beta$ con $q_f$ finale.

*Dimostrazione.* $U$ esegue una per una le trasformazioni richieste dalle quintuple di $M$ contenute in $D_M$; al termine cancella dal nastro la descrizione $D_M$.

La MT universale si può interpretare come:
- un **calcolatore**, con $D_M$ e $x$ come **programma e dati** (è l'idea del calcolatore a programma memorizzato di von Neumann);
- un **interprete** di un linguaggio di programmazione.

> [!example] Domande d'esame
> - *Ingressi e risultato della MT universale; perché è importante?* (febbraio 2020): input $D_M \# x$; si comporta come $M$ su $x$ (termina in uno stato finale se e solo se lo fa $M$, lasciando sul nastro lo stesso risultato). È importante perché mostra che **una sola** macchina fissata può eseguire **qualunque** algoritmo: è il fondamento teorico del calcolatore programmabile, e serve a dimostrare che la terminazione è semidecidibile.
> - *$U$ può simulare se stessa?* (giugno 2022): sì, $U$ è una MT come le altre e ha una descrizione $D_U$; $U$ con input $D_U \# D_M \# x$ simula $U$ che simula $M$ su $x$ (con un rallentamento, ma senza problemi di principio).

## Funzioni non calcolabili e problemi indecidibili

Le MT hanno consentito di:
- definire formalmente i concetti di **algoritmo**, **funzione calcolabile** e **problema decidibile**;
- mostrare l'**esistenza** di funzioni non calcolabili e problemi non decidibili.

### Un po' di storia

- **1900**: al Secondo Congresso Internazionale di Matematica, **Hilbert** formula 23 problemi per il XX secolo. Il secondo riguarda la **consistenza** (non contraddittorietà) dell'aritmetica dei naturali basata sugli assiomi di Peano (1889).
- **1928**: Hilbert riformula le domande sull'aritmetica:
  - è **completa**? (si può dimostrare ogni asserzione vera?)
  - è **consistente**? (non si può dimostrare un'asserzione e anche la sua negazione? Se fosse inconsistente ogni asserzione sarebbe dimostrabile, quindi per dimostrare la consistenza basta trovare un'asserzione non dimostrabile)
  - è **decidibile**? (esiste un algoritmo che decide se un'asserzione è un teorema? È l'*Entscheidungsproblem*)

**Il ruolo dei paradossi** (tutti basati sull'**autoreferenzialità**):
1. Epimenide di Creta (VI sec. a.C.): "Tutti i cretesi sono bugiardi" (non può essere vera ma può essere falsa: non è un vero paradosso);
2. Eubulide di Mileto (IV sec. a.C.): "Questa frase è falsa", "Io sto mentendo" (né vere né false);
3. Buridano (XIV sec.): Socrate dice "Platone dice il falso", Platone dice "Socrate dice il vero" (insieme sono un paradosso);
4. Russell: l'insieme di tutti gli insiemi che non appartengono a se stessi appartiene a se stesso?
5. Russell: in un villaggio il barbiere rade tutti e soli coloro che non si radono da soli; chi rade il barbiere?
6. Gonseth: in una biblioteca può esistere un catalogo di tutti i cataloghi che non contengono se stessi?

- **1931**: **Gödel** dimostra che l'aritmetica non può essere al tempo stesso completa e consistente. Idea: rappresentare la logica (assiomi, regole, dimostrazioni) dentro l'aritmetica con un procedimento di **aritmetizzazione** (gödelizzazione: codificare tutto con numeri interi, come visto per la [[01 - MC - Costo degli algoritmi e modello CEM#Perché i costi uniformi non sono "grossolani"|CEM]]); poi creare un'asserzione autoreferenziale $w$ che afferma "$w$ non è dimostrabile". Se $w$ fosse falsa sarebbe dimostrabile, quindi vera; quindi (se il calcolo non è contraddittorio) $w$ è vera, e allora non è dimostrabile: un'asserzione **vera ma non dimostrabile**. L'aritmetica non è completa, oppure non è consistente (e la consistenza non è dimostrabile dentro la teoria stessa).
- **1935–36**: **Turing** (*On computable numbers, with an application to the Entscheidungsproblem*) definisce il concetto di algoritmo con le sue macchine, mostra che la terminazione di una MT è formulabile come asserzione dell'aritmetica (sempre per gödelizzazione) e che non è risolubile con le MT: è **indecidibile**, e quindi l'aritmetica stessa **non è decidibile**.

Contemporaneamente **Alonzo Church** ha introdotto un concetto di calcolabilità (la $\lambda$-definibilità) basato sul **$\lambda$-calcolo**, dimostrato equivalente alle MT dallo stesso Turing. Da qui la tesi:

> [!important] Tesi di Church-Turing
> "Ogni funzione che sia dimostrata calcolabile con un qualunque approccio formale è calcolabile secondo Turing."

Tutti i formalismi definiti in seguito l'hanno confermata, avendo potere equivalente alle MT: le **funzioni ricorsive** (Kleene, 1936), i **sistemi di riscrittura** (Post, 1943), gli **algoritmi di Markov** (1949), le **macchine a registri** (Shepherdson e Sturgis, 1963).

> [!example] La tesi vale per gli automi a stati finiti? (giugno 2021, giugno 2022)
> No, nel senso che gli ASF **non** hanno il potere delle MT (non riconoscono nemmeno $a^n b^n$): la tesi riguarda i modelli che catturano la nozione generale di algoritmo, e afferma che nessuno supera le MT, non che tutti le eguagliano. Che ASFND e ASFD siano **equivalenti fra loro** è invece un teorema separato (la costruzione per sottoinsiemi della [[10 - MC - Automi a stati finiti ed espressioni regolari#Equivalenza fra ASFND e ASFD|lezione 10]]), analogo a quello fra MTND e MT.

### L'indecidibilità della terminazione

Si assume che le MT siano a un nastro, deterministiche, con alfabeto $\Sigma = \{0, 1\}$. Data $M$, sia $D_M$ la sua codifica in $\Sigma$. Per $x \in \Sigma^*$ si definisce il **predicato della terminazione**

$$h(D_M, x) = \begin{cases} 1 & \text{se } M \text{ con input } x \text{ termina} \\ 0 & \text{se } M \text{ con input } x \text{ non termina} \end{cases}$$

> [!important] Teorema
> Il predicato della terminazione **non è calcolabile secondo Turing**: il problema della terminazione è indecidibile.
>
> È invece T-calcolabile il predicato **parziale** $h(D_M, x) = 1$ se $M$ su $x$ termina, **indefinito** altrimenti (basta simulare $M$ con la macchina universale): la terminazione è **semidecidibile**.

*Dimostrazione.* Si supponga che esista una MT $H$ che calcola $h$. Si costruisce $H'$ che calcola

$$h'(D_M) = \begin{cases} 1 & \text{se } M \text{ con input } D_M \text{ termina} \\ 0 & \text{se } M \text{ con input } D_M \text{ non termina} \end{cases}$$

$H'$ è la composizione di due macchine: la prima, con input $D_M$, produce $D_M \flat D_M$; la seconda è $H$. In altre parole $H'$ verifica se una MT termina quando le viene fornito in input **il proprio codice**. Poi si costruisce $H''$ che calcola

$$h''(D_M) = \begin{cases} 0 & \text{se } h'(D_M) = 0 \\ \text{indefinito} & \text{altrimenti} \end{cases}$$

cioè $H''$ termina con 0 se $H'$ si è fermata con 0, e **si mette a ciclare** se $H'$ si è fermata con 1. Che cosa accade calcolando $h''(D_{H''})$?

$$h''(D_{H''}) = \begin{cases} \text{indefinita} & \text{se } h''(D_{H''}) \text{ è definita} \\ 0 & \text{se } h''(D_{H''}) \text{ è indefinita} \end{cases}$$

In ogni caso una contraddizione: non può esistere la macchina $H$. $\square$

(È la stessa costruzione di `diag` della [[07 - MC - Halting Problem#Costruzione della funzione diagonale|lezione 7]]: $H''$ è `diag`.)

Per la tesi di Church-Turing, la terminazione di un programma è indecidibile **in ogni linguaggio di programmazione**.

**Altri problemi indecidibili in informatica:**
- decidere se un programma è **corretto** (se calcola la funzione desiderata);
- decidere se, dato un programma e una sua procedura (o istruzione), la procedura sarà chiamata (l'istruzione sarà eseguita);
- decidere se una grammatica CF è **ambigua**, o se due grammatiche CF sono **equivalenti**.

**In matematica:**
- decidere se una formula del calcolo dei predicati del prim'ordine è un teorema (valida);
- decidere se un'**equazione diofantea** $p(x_1, \dots, x_n) = 0$ ($p$ polinomio a coefficienti interi) ammette soluzioni intere (il **decimo problema di Hilbert**, risolto negativamente da Matiyasevich nel 1970).

## Relazioni tra macchine di Turing e calcolatori

### Modelli di costo per le RAM

Le **macchine a registri** (RAM, *Random Access Machine*) sono il modello più vicino a un calcolatore reale: una memoria di registri $R[0], R[1], \dots$ ($R[0]$ è l'accumulatore) e un programma in un linguaggio assembler (`LOAD`, `STORE`, `ADD`, `SUB`, `MULT`, `DIV`, `READ`, `WRITE`, `JUMP`, `JGTZ`, `JZERO`, `HALT`).

**Modello a costi uniformi**: ogni istruzione costa 1.
- *Critiche*: moltiplicare due interi di 32 bit costa quanto moltiplicarne due di 1024 bit; accedere a una memoria di 1 kilobyte costa come accedere a una di 1 terabyte.
- *Vantaggi*: è molto semplice ed è il modello più usato per i programmi in linguaggio ad alto livello (è la [[01 - MC - Costo degli algoritmi e modello CEM|CEM]]).

**Modello a costi logaritmici**: i costi sono proporzionali al numero di bit degli operandi e al logaritmo dell'indirizzo dei registri a cui si accede. Con la lunghezza in binario

$$l(n) = \begin{cases} 1 & n = 0 \\ \lfloor \log n \rfloor + 1 & n > 0 \end{cases}$$

l'elaborazione di un intero $n$ costa $l(n)$ e l'accesso al registro $i$ costa $l(i)$.
- *Vantaggi*: la valutazione è più realistica asintoticamente (operandi e memoria molto grandi).
- *Critiche*: l'analisi è più laboriosa. Per esempio `ADD 3` costa $l(3)$ (accesso al registro 3) $+ l(R[3]) + l(R[0])$ (somma); `ADD *3` (indirizzamento indiretto) costa $l(3) + l(R[3]) + l(R[R[3]]) + l(R[0])$.

> [!example] Calcolo di $x^y$ a costi logaritmici
> ```text
>     READ 1         ; R1 = x
>     READ 2         ; R2 = y
>     LOAD =1
>     STORE 3        ; R3 = 1 (risultato)
> 5   LOAD 2
>     JGTZ 14        ; così nella dispensa: vedi la nota sotto
>     LOAD 1
>     MULT 3         ; R3 = R3 * x
>     STORE 3
>     LOAD 2
>     SUB =1
>     STORE 2        ; y = y - 1
>     JUMP 5
> 14  WRITE 3
>     HALT
> ```
> Il ciclo è eseguito $O(y)$ volte. La moltiplicazione all'iterazione $i$ opera su $x^i$, lungo $i \log x$ bit: costo $O(i \log x)$. In totale $\sum_{i=1}^{y} O(i \log x) = O(y^2 \log x)$. A costi uniformi lo stesso programma costerebbe $O(y)$.

In pratica, se i dati hanno dimensione prefissata (per esempio 36 bit) e la memoria ha dimensione prefissata, i due modelli **coincidono**. Se servono operazioni in precisione arbitraria o l'accesso a memoria secondaria, anche per i linguaggi ad alto livello bisogna usare modelli analoghi ai costi logaritmici.

> [!note] Il salto condizionato
> Nel listato della dispensa l'istruzione di uscita è `JGTZ 14` ("salta se positivo"), che con $y > 0$ salterebbe subito alla fine. Perché il ciclo funzioni come descritto serve un salto all'uscita quando $y = 0$ (`JZERO 14`), oppure `JGTZ` verso il corpo del ciclo e un `JUMP 14` dopo. L'analisi del costo non cambia.

### Simulazione di RAM con macchine di Turing

> [!important] Calcolabilità mediante RAM
> $f: \mathbb{N}^n \to \mathbb{N}$ è **calcolabile da una RAM** se esiste un programma $P$ tale che: se $f(x_1, \dots, x_n) = y$, $P$ attivato con $x_1, \dots, x_n$ sul nastro di input termina con $y$ sul nastro di output; se $f(x_1, \dots, x_n)$ non è definita, $P$ non termina.

> [!important] Teorema (MT → RAM)
> Sia $M = \langle \{0,1\}, \flat, K, q_0, F, \delta \rangle$ una MT con nastro semi-infinito. Esistono una RAM e un programma $P$ tali che, se $M$ calcola $q_0 x \vdash^* q_F y$ e la RAM ha la stringa $x$ nelle celle $2, \dots, |x| + 1$, al termine la RAM ha $y$ nelle celle $2, \dots, |y| + 1$. La RAM **simula $T$ passi di $M$ in tempo $O(T \log T)$** a costi logaritmici.

*Dimostrazione.* La cella $i$ del nastro di $M$ corrisponde alla cella $i + 1$ della RAM; la cella 1 contiene la posizione della testina (inizialmente 2). $P$ contiene una sequenza di istruzioni per ogni stato di $M$. Per esempio, se $\delta(q_1, 0) = \langle q_2, 1, d \rangle$ e $\delta(q_1, 1) = \langle q_3, 0, s \rangle$:

```text
q1   LOAD *1      ; legge il simbolo sotto la testina
     JGTZ q1'     ; è un 1 o uno 0?
     LOAD =1
     STORE *1     ; scrive un 1 sul nastro
     LOAD 1
     ADD =1
     STORE 1      ; testina a destra
     JUMP q2      ; nuovo stato
q1'  LOAD =0
     STORE *1     ; scrive uno 0
     LOAD 1
     SUB =1
     STORE 1      ; testina a sinistra
     JUMP q3
```

Ogni passo di $M$ è simulato da al più 8 istruzioni, ognuna di costo $O(\log t_{max})$, dove $t_{max}$ è il massimo numero di celle usate da $M$; se $M$ esegue $T$ passi, $t_{max} \le T + 1$. Costo complessivo $O(T \log T)$. $\square$

> [!important] Teorema (RAM → MT)
> Data una RAM con programma $P$ che calcola $f$, esiste una MT $M$ che, con $x_1, \dots, x_n$ in binario sul nastro di input, termina con $y = f(x_1, \dots, x_n)$ in binario sul nastro di output (e non termina se $f$ non è definita). Se la computazione della RAM ha costo $T$ a costi logaritmici, $M$ la **simula in $O(T^2)$ passi**.

*Dimostrazione.* $M$ ha un nastro di input, uno di output e tre di lavoro. Sul nastro 1 ci sono i registri usati, ciascuno preceduto dal proprio indirizzo: $\#i_1\#R[i_1]\#i_2\#R[i_2]\dots\#i_m\#R[i_m]$; sul nastro 2 l'accumulatore; il nastro 3 serve al funzionamento. Per ogni istruzione della RAM, $M$ ha un insieme di stati:
- **salti** (`JUMP`, `JGTZ`, `JZERO`, `HALT`): si controlla l'accumulatore e si cambia stato;
- istruzioni che **non modificano la memoria** (`LOAD`, `ADD`, `SUB`, `MULT`, `DIV`, `WRITE`): si cerca sul nastro 1 il registro e si esegue l'operazione sul nastro dell'accumulatore;
- istruzioni che **modificano la memoria** (`STORE`, `READ`): si copia sul nastro 3 quanto sta a destra del registro da modificare, si modifica il registro sul nastro 1, si ricopia il resto.

*Analisi.* Ogni operazione costa a $M$ un tempo dell'ordine della lunghezza massima del nastro 1, che è $\le T$: un indirizzo $i$ compare sul nastro 1 solo se la RAM ha acceduto al registro $i$ pagando almeno $\log i$, e occupa proprio $\log i$ celle; lo stesso per i contenuti. Le operazioni sono al più $T$. Totale $O(T \cdot T) = O(T^2)$. $\square$

> [!summary] Conseguenze
> - Tutto ciò che si può fare con una MT (calcolare funzioni, riconoscere o accettare insiemi) si può fare con una RAM e viceversa.
> - Le RAM corrispondono a semplici programmi assembler per una macchina di von Neumann: il loro potere computazionale coincide con quello dei linguaggi ad alto livello.
> - **Tesi di Church-Turing**: tutti i modelli di calcolo (e tutti i linguaggi di programmazione) hanno al massimo lo stesso potere delle MT.
> - Una MT e una RAM **a costi logaritmici** si simulano a vicenda in **tempo polinomiale**. Non vale per le RAM con moltiplicazione a costi uniformi (con $y$ moltiplicazioni successive $x \mapsto x^2$ si ottiene un numero di $2^y$ bit in $y$ passi). Per stabilire se un problema si risolve in tempo polinomiale si può usare indifferentemente una MT o una RAM a costi logaritmici: è la robustezza della [[14 - MC - Classi P e NP e NP-completezza#La classe P|classe P]].

> [!example] Nastro semi-infinito (settembre 2019, settembre 2021)
> *Una MT con nastro semi-infinito (illimitato in una sola direzione) ha ancora pieno potere computazionale?* Sì. Si "piega" il nastro bi-infinito a metà e lo si rappresenta con un nastro semi-infinito a **due tracce**: la traccia superiore contiene le celle $0, 1, 2, \dots$, quella inferiore le celle $-1, -2, -3, \dots$. Gli stati della macchina simulante ricordano su quale traccia si trova la testina: sulla traccia inferiore i movimenti sono invertiti (destra ↔ sinistra), e nella prima cella (marcata con un simbolo speciale) si passa da una traccia all'altra. Il rallentamento è costante. (Il libro di Crescenzi tratta le varianti nel §2.4: nastri bidimensionali, multi-traccia, testina limitata, nastro semi-infinito.)

## Riepilogo

> [!summary]
> - **MT** = $\langle \Sigma, \flat, K, q_0, F, \delta \rangle$, con $\delta: K \times \Sigma_\flat \to K \times \Sigma_\flat \times \{d, s, i\}$ parziale. Configurazioni, transizioni $\vdash$, computazioni massimali.
> - Una MT **calcola** $f$ (trasduttrice), **riconosce/decide** $L$ (si ferma sempre, finale sse $x \in L$) o **accetta** $L$ (si ferma in uno stato finale per tutte e sole le $x \in L$). Decidibile ⊊ semidecidibile.
> - **Multinastro**: simulabile con un nastro in $O(t^2)$. **Non deterministica**: simulabile in $O(k\,d^k)$ con visita in ampiezza. Stesso potere, costi diversi.
> - **Semidecidibile = tipo 0**; i linguaggi di tipo 1 sono decidibili.
> - **MT universale** $U$: con input $D_M \# x$ simula $M$ su $x$ (un interprete).
> - La **terminazione** è indecidibile ma semidecidibile. **Tesi di Church-Turing**: nessun modello ragionevole supera le MT.
> - MT e RAM a costi logaritmici si simulano in tempo polinomiale ($O(T \log T)$ e $O(T^2)$).
