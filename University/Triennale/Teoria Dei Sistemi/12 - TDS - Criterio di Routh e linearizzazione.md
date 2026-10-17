---
title: Criterio di Routh e linearizzazione
aliases:
  - TDS — Criterio di Routh e linearizzazione
tags:
  - teoria-dei-sistemi
  - stabilita
  - criterio-di-routh
  - linearizzazione
  - sistemi-non-lineari
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 46–53); libro Monaco et al., §3.3, §3.5
---

# Criterio di Routh e linearizzazione

> [!abstract] Scopo della lezione
> Nella [[11 - TDS - Punti di equilibrio e stabilità|lezione precedente]] la stabilità di un sistema lineare si è ridotta al **segno della parte reale degli autovalori**, e si è vista una condizione solo necessaria sui coefficienti del polinomio caratteristico. Qui:
> 1. il **criterio di Routh** dà il numero di radici a parte reale positiva e negativa **senza calcolarle**, anche con parametri; con i casi particolari (zero in prima colonna, riga tutta nulla);
> 2. la **linearizzazione** attorno a un equilibrio permette di usare questi strumenti anche per sistemi **non lineari**, con il teorema che lega la stabilità del linearizzato a quella del sistema originale;
> 3. un esempio reale: il **modello epidemico SIR** e il numero $R_0$.
>
> Segue [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto]]. Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in rosso: **"ROUTH"**.

## Criterio di Routh

Vedi [[TDS - Criterio di Routh]].

Condizione necessaria perché gli autovalori abbiano tutti parte reale negativa è che i coefficienti $a_0,\dots,a_n$ del polinomio caratteristico siano tutti dello stesso segno; se non lo sono, c'è sicuramente almeno una radice a parte reale non negativa. Per avere una condizione **necessaria e sufficiente** si usa il **criterio di Routh** (Routh-Hurwitz): un algoritmo basato su una tabella con $n+1$ righe, numerate da $n$ a $0$.

**Prime due righe.** Si riempiono con i coefficienti, alternando tra le due righe a zig-zag (il primo coefficiente in alto, il secondo in basso, il terzo in alto, …):

| | | | | |
|---|---|---|---|---|
| $n$ | $a_n$ | $a_{n-2}$ | $a_{n-4}$ | $\cdots$ |
| $n-1$ | $a_{n-1}$ | $a_{n-3}$ | $a_{n-5}$ | $\cdots$ |
| $n-2$ | $b_1$ | $b_2$ | $\cdots$ | |
| $\vdots$ | $\vdots$ | | | |
| $0$ | | | | |

**Righe successive.** Il primo elemento della riga $n-2$, $b_1$, è il determinante della matrice $2\times2$ che ha come prima colonna i **primi due elementi delle due righe precedenti** ($a_n$, $a_{n-1}$) e come seconda colonna gli elementi delle due righe precedenti nella **colonna immediatamente a destra** di quella di $b_1$ ($a_{n-2}$, $a_{n-3}$), il tutto diviso per il primo elemento della riga precedente **cambiato di segno**:

$$b_1=\frac{\begin{vmatrix}a_n&a_{n-2}\\a_{n-1}&a_{n-3}\end{vmatrix}}{-a_{n-1}}=\frac{a_{n-1}a_{n-2}-a_na_{n-3}}{a_{n-1}},\qquad b_2=\frac{\begin{vmatrix}a_n&a_{n-4}\\a_{n-1}&a_{n-5}\end{vmatrix}}{-a_{n-1}}$$

Per $b_2$ restano uguali la prima colonna del determinante e il divisore; cambia solo la seconda colonna, presa una colonna più a destra. Si finisce quando finiscono i termini.

Se i coefficienti sono in numero dispari, la riga $n-1$ ha un "buco" alla fine. Per esempio con 5 coefficienti (grado 4):

| | | | |
|---|---|---|---|
| 4 | $a_4$ | $a_2$ | $a_0$ |
| 3 | $a_3$ | $a_1$ | |
| 2 | $b_1$ | $b_2$ | |
| 1 | $c_1$ | | |
| 0 | $d_1$ | | |

Calcolando $b_2$ si mette uno $0$ al posto della casella vuota: $b_2=\frac{1}{-a_3}\begin{vmatrix}a_4&a_0\\a_3&0\end{vmatrix}=a_0$. Lo zero però **non si scrive nella tabella** (si riferirebbe a un altro polinomio). $b_3$ non si calcola, perché a destra di $a_0$ non c'è nulla: si passa alla riga successiva. Per $c_1$ si procede come per $b_1$, ma con le due righe immediatamente sopra: $c_1=\frac{1}{-b_1}\begin{vmatrix}a_3&a_1\\b_1&b_2\end{vmatrix}$. La tabella si stringe sempre di più, fino alle righe 1 e 0, con un solo termine ciascuna.

**Lettura.** Costruita la tabella, si guarda la **prima colonna**: se due elementi successivi hanno lo stesso segno c'è una **permanenza** (P), se cambiano segno una **variazione** (V). Per esempio con $a_n>0$, $a_{n-1}>0$, $b_1<0$ si ha una permanenza e una variazione.

> [!important] Criterio di Routh
> - A ogni **variazione** di segno nella prima colonna corrisponde una radice a **parte reale positiva**, a ogni **permanenza** una radice a **parte reale negativa**.
> - Quindi le radici hanno tutte parte reale negativa (stabilità asintotica) **se e solo se** nella prima colonna ci sono solo permanenze.

Il criterio è particolarmente utile quando i coefficienti contengono **parametri**: diventa facile dire per quali valori il sistema è stabile o instabile.

> [!quote] Dal libro — perché funziona
> La dimostrazione del libro è ricorsiva. Si costruisce il polinomio $q(\lambda)$ di grado $n-1$ che ha come tabella di Routh quella di $p(\lambda)$ **senza la prima riga**, e si collega $p$ a $q$ con una famiglia $q(k;\lambda)=p(\lambda)-k(a_{n-1}\lambda^n+a_{n-3}\lambda^{n-2}+\dots)$ che passa con continuità da $p$ ($k=0$) a $q$ ($k=a_n/a_{n-1}$). Lungo il percorso una radice va all'infinito, ed è a parte reale negativa se e solo se $a_n$ e $a_{n-1}$ hanno lo stesso segno (una permanenza); le altre $n-1$ radici sono quelle di $q$, e si ripete il ragionamento sulla tabella ridotta. Si arriva al polinomio di secondo grado, per cui vale la regola di Cartesio. _(libro, §3.3.1, pp. 110–113)_

## Esempio numerico di applicazione del criterio

$$p(\lambda)=\lambda^4+2\lambda^3+\lambda^2+3\lambda+5$$

Primo passo: i coefficienti sono tutti **positivi**, cioè **strettamente** maggiori di zero (se mancasse un termine, cioè un coefficiente fosse nullo, la condizione necessaria non sarebbe verificata e ci sarebbero radici a parte reale non negativa). Tabella:

| | | | |
|---|---|---|---|
| 4 | 1 | 1 | 5 |
| 3 | 2 | 3 | |
| 2 | $b_1$ | $b_2$ | |
| 1 | | | |
| 0 | | | |

$$b_1=\frac{\begin{vmatrix}1&1\\2&3\end{vmatrix}}{-2}=\frac{3-2}{-2}=-\frac12,\qquad b_2=\frac{\begin{vmatrix}1&5\\2&0\end{vmatrix}}{-2}=\frac{-10}{-2}=5$$

> [!tip] Scorciatoia
> Quando si aggiunge uno zero per la casella vuota, il risultato è sempre il numero in alto a destra del determinante (qui 5): $\frac{a\cdot0-b\cdot c}{-c}=b$.

$$c_1=\frac{\begin{vmatrix}2&3\\-1/2&5\end{vmatrix}}{1/2}=2\left(10+\frac32\right)=23,\qquad d_1=\frac{\begin{vmatrix}-1/2&5\\23&0\end{vmatrix}}{-23}=\frac{-5\cdot23}{-23}=5$$

A destra di $c_1$ non c'è nulla (mancano i numeri per il determinante); $d_1=5$ si sapeva già per la scorciatoia. Tabella finale:

| | | | |
|---|---|---|---|
| 4 | 1 | 1 | 5 |
| 3 | 2 | 3 | |
| 2 | $-1/2$ | 5 | |
| 1 | 23 | | |
| 0 | 5 | | |

Prima colonna: $1,\ 2,\ -\frac12,\ 23,\ 5$. Permanenza tra 1 e 2, variazione tra 2 e $-\frac12$, variazione tra $-\frac12$ e 23, permanenza tra 23 e 5: **due radici a parte reale positiva** e due a parte reale negativa. Per concludere che il sistema è **instabile** basta già una sola variazione.

**Moltiplicare una riga.** Si può moltiplicare un'intera **riga** per un fattore **positivo** senza cambiare il risultato. Per esempio, moltiplicando la riga 2 per 2:

| | | | |
|---|---|---|---|
| 4 | 1 | 1 | 5 |
| 3 | 2 | 3 | |
| 2 | $-1$ | 10 | |
| 1 | 23 | | |
| 0 | 10 | | |

Le conclusioni sono identiche. Ovviamente non si può moltiplicare per un fattore minore o uguale a zero.

> [!warning] Correzione
> Negli appunti si legge "è possibile moltiplicare una **colonna** per un fattore positivo", ma nell'esempio si moltiplica una **riga** (la riga 2). È la riga che si può moltiplicare, come conferma il libro: "se si moltiplica (divide) una intera riga per lo stesso fattore positivo il risultato non cambia". _(libro, §3.3.1, p. 114)_

## Caso in cui il primo elemento di una riga è nullo

Se durante l'algoritmo il **primo elemento** di una riga viene zero, non si può proseguire, perché per l'elemento sotto si dividerebbe per zero. Per esempio:

$$p(\lambda)=\lambda^5+\lambda^4+\lambda^3+\lambda^2+2\lambda+1$$

| | | | |
|---|---|---|---|
| 5 | 1 | 1 | 2 |
| 4 | 1 | 1 | 1 |
| 3 | 0 | 1 | |
| 2 | $*$ | | |

($b_1=\frac{1\cdot1-1\cdot1}{1}=0$, $b_2=\frac{1\cdot2-1\cdot1}{1}=1$.) Già da qui si sa che le radici **non sono tutte a parte reale strettamente negativa**: il sistema non è asintoticamente stabile. Ma potrebbe ancora essere stabile semplicemente, quindi si continua.

**Procedura.** Si toglie lo zero, si sposta il resto della riga a sinistra di un posto, si cambia segno a tutta la riga e si mette uno zero a destra; poi si somma la riga ottenuta a quella di partenza:

| | | |
|---|---|---|
| 3 | 0 | 1 |
| (traslata, cambiata di segno) | $-1$ | 0 |
| **3′** | $-1$ | 1 |

e si sostituisce la riga 3 con la 3′:

| | | | |
|---|---|---|---|
| 5 | 1 | 1 | 2 |
| 4 | 1 | 1 | 1 |
| **3′** | $-1$ | 1 | |
| 2 | $*$ | | |

Ora l'elemento $*$ si calcola senza problemi. Se gli zeri iniziali sono due o più, si sposta la riga di due o più posti, e **ogni volta che ci si sposta di un posto va cambiato il segno a tutta la riga** (cioè si moltiplica per $(-1)^j$, con $j$ il numero di zeri iniziali). Nell'esempio c'è già una variazione tra la riga 4 e la 3′: c'è sicuramente una radice a parte reale positiva e il sistema è **instabile**.

> [!example] Completamento della tabella
> Proseguendo, nella riga 2 (divisore $-(-1)=1$): $c_1=\frac{\begin{vmatrix}1&1\\-1&1\end{vmatrix}}{1}=2$, $c_2=\frac{\begin{vmatrix}1&1\\-1&0\end{vmatrix}}{1}=1$; riga 1: $\frac{\begin{vmatrix}-1&1\\2&1\end{vmatrix}}{-2}=\frac32$; riga 0: $1$. Prima colonna $1,1,-1,2,\frac32,1$: **due variazioni**, quindi due radici a parte reale positiva.

Se invece risultano tutte permanenze, si può concludere che il polinomio ha radici **non positive** (alcune possono essere sull'asse immaginario): $\mathrm{Re}(\lambda_i)\le0$, e il sistema è al più stabile semplicemente, non asintoticamente; non si può dire che siano tutte negative, perché la tabella è stata "modificata" per gli zeri.

> [!note] Precisazione
> Per la stabilità semplice serve anche che le eventuali radici sull'asse immaginario siano regolari (molteplicità algebrica uguale a quella geometrica), come visto in [[11 - TDS - Punti di equilibrio e stabilità#Definizione operativa di stabilità|lezione 11]].

> [!quote] Dal libro — un'alternativa
> Un altro modo per superare lo zero è moltiplicare il polinomio per un binomio con radice negativa, $p^1(\lambda)=p(\lambda)(\lambda+\lambda_0)$ con $\lambda_0>0$: il numero di radici a parte reale positiva o nulla non cambia, ma la nuova tabella in genere non ha più lo zero in prima colonna. Il libro lo mostra su $p(\lambda)=\lambda^5+\lambda^4+2\lambda^3+2\lambda^2+2\lambda+1$ moltiplicato per $(\lambda+1)$, ritrovando lo stesso risultato (due radici a parte reale positiva). _(libro, §3.3.1, pp. 115–116)_

## Caso in cui un'intera riga è nulla

$$p(\lambda)=\lambda^5+\lambda^4+\lambda^3+\lambda^2+2\lambda+2$$

| | | | |
|---|---|---|---|
| 5 | 1 | 1 | 2 |
| 4 | 1 | 1 | 2 |
| 3 | 0 | 0 | |
| 2 | $*$ | | |

Dalla dimostrazione del criterio si ricava che, se si presenta una riga tutta nulla, è una riga di **indice dispari** (qui la 3: le due righe precedenti devono essere proporzionali, quindi lunghe uguali, e la lunghezza cala solo passando da una riga pari a una dispari). In questo caso il polinomio si fattorizza:

$$p(\lambda)=p_1(\lambda)\,p_2(\lambda)$$

- $p_1(\lambda)$ ha le radici che si leggono dalla parte di tabella completata prima della riga nulla: tra la riga 5 e la 4 c'è una permanenza, quindi $p_1$ ha **una radice negativa** ed è di grado 1;
- $p_2(\lambda)$ ha le restanti $5-1=4$ radici, è di quarto grado e contiene solo **potenze pari**, con coefficienti presi dalla riga **precedente** a quella nulla (la riga 4):

$$p_2(\lambda)=1\lambda^4+1\lambda^2+2$$

A questo punto si può calcolare direttamente le radici di $p_2$, oppure **derivare** $p_2$ e mettere i coefficienti della derivata al posto della riga nulla:

$$\frac{dp_2(\lambda)}{d\lambda}=4\lambda^3+2\lambda$$

| | | | |
|---|---|---|---|
| 5 | 1 | 1 | 2 |
| 4 | 1 | 1 | 2 |
| **3′** | 4 | 2 | |
| 2 | $\vdots$ | $\vdots$ | |

Gli appunti concludono che, avendo una riga di zeri e una tabella modificata, le radici sono al più non positive, ma ci sono radici nulle, e quindi il sistema non può essere asintoticamente stabile.

> [!warning] Correzione
> La conclusione degli appunti su **questo** esempio non è corretta. Completando la tabella:
>
> | | | |
> |---|---|---|
> | 5 | 1 | 1 | 
> | 4 | 1 | 1 |
> | 3′ | 4 | 2 |
> | 2 | $\frac12$ | 2 |
> | 1 | $-14$ | |
> | 0 | 2 | |
>
> ($\frac{\begin{vmatrix}1&1\\4&2\end{vmatrix}}{-4}=\frac12$, $\frac{\begin{vmatrix}1&2\\4&0\end{vmatrix}}{-4}=2$, $\frac{\begin{vmatrix}4&2\\1/2&2\end{vmatrix}}{-1/2}=-14$, $\frac{\begin{vmatrix}1/2&2\\-14&0\end{vmatrix}}{14}=2$.) La prima colonna $1,1,4,\frac12,-14,2$ ha **due variazioni**: ci sono **due radici a parte reale positiva** e il sistema è **instabile**. Non ci sono radici nulle ($p(0)=2\neq0$). In effetti $p(\lambda)=(\lambda+1)(\lambda^4+\lambda^2+2)$, e $\lambda^4+\lambda^2+2=0$ dà $\lambda^2=\frac{-1\pm j\sqrt7}{2}$, cioè quattro radici $\pm(0{,}68\pm j\,0{,}98)$, simmetriche rispetto all'origine: due nel semipiano destro.
>
> Il ragionamento degli appunti ("al più non positive") vale solo quando le radici di $p_2$ stanno sull'**asse immaginario** (per esempio $p_2=\lambda^2+1$). Una riga nulla segnala radici **simmetriche rispetto all'origine**, che possono essere sull'asse immaginario **oppure** a coppie $\pm\sigma$, $\pm(\sigma\pm j\omega)$: per distinguere bisogna completare la tabella.

## Approssimazione di sistemi non lineari

Vedi [[TDS - Linearizzazione]].

> [!note] Annotazione di Simone
> Prima di questa sezione, a mano in rosso: **"APPROSSIMAZIONE SISTEMI NON LINEARI"**.

I sistemi lineari coprono gran parte dei problemi reali, e permettono anche di studiare alcune proprietà dei sistemi **non lineari**: se ci si "avvicina" abbastanza a un punto di equilibrio $x_e$, il sistema non lineare è ben approssimato da uno lineare, ottenuto con lo sviluppo di Taylor al primo ordine (vedi [[Formula di Taylor]] e [[08 - AN1 - Calcolo Differenziale in più Variabili]]):

$$\dot x=f(x,u)\approx f(x_e,0)+\left.\frac{\partial f(x,u)}{\partial x}\right|_{\substack{x=x_e\\u=0}}(x-x_e)+\left.\frac{\partial f(x,u)}{\partial u}\right|_{\substack{x=x_e\\u=0}}u$$

Il simbolo $\left.\frac{\partial f}{\partial x}\right|_{x=x_e,u=0}$ indica la derivata parziale calcolata in $x=x_e$, $u=0$ (per esempio se $f=x^2+2u-4xu$, $\frac{\partial f}{\partial x}=2x-4u$ e nel punto vale $2x_e$). Ricordando che $f(x_e,0)=0$ per definizione di equilibrio, e cambiando variabile $z=x-x_e$ (lo scostamento dall'equilibrio, per cui $\dot z=\dot x$):

$$\dot z=Az+Bu,\qquad A=\left.\frac{\partial f(x,u)}{\partial x}\right|_{\substack{x=x_e\\u=0}},\qquad B=\left.\frac{\partial f(x,u)}{\partial u}\right|_{\substack{x=x_e\\u=0}}$$

$A$ è la matrice **jacobiana** di $f$ rispetto a $x$, calcolata nell'equilibrio.

**Procedura.** Per studiare un sistema non lineare:
1. si calcolano i punti di equilibrio $x_{e1},\dots,x_{ek}$ (con ingresso nullo);
2. per **ciascun** equilibrio si calcolano le derivate parziali, ottenendo $k$ matrici $A_1,\dots,A_k$;
3. si studiano separatamente questi sistemi lineari.

> [!important] Teorema (metodo indiretto di Lyapunov)
> - Se il sistema linearizzato è **asintoticamente stabile**, il sistema non lineare è (localmente) **asintoticamente stabile** in quell'equilibrio.
> - Se il sistema linearizzato è **instabile**, anche il sistema non lineare è **instabile**.
> - Se il linearizzato è solo **semplicemente stabile**, **non si può concludere nulla**.

> [!note] Annotazioni di Simone
> A margine: **"Procedura da fare nella pratica"** e **"Teorema Importante"**; in fondo alla pagina, a mano:
> - sistema approssimato asintoticamente stabile → sistema non lineare asintoticamente stabile
> - sistema approssimato INSTABILE → sistema non lineare INSTABILE
> - sistema approssimato SEMPLICEMENTE stabile → sistema non lineare NON CONCLUDO NULLA → USO LAYPUNOV

> [!quote] Dal libro — condizioni di stabilità
> Il libro precisa il caso "instabile": si conclude l'instabilità se il linearizzato ha autovalori a parte reale **positiva**; se invece è instabile "per la presenza di autovalori con parte reale nulla di ordine geometrico maggiore di uno", di nuovo non si può dedurre nulla. Per esempio, con $J(x_e)=\begin{psmallmatrix}-1&0\\1&-3\end{psmallmatrix}$ l'equilibrio è asintoticamente stabile, con $\begin{psmallmatrix}-1&0\\1&3\end{psmallmatrix}$ instabile, con $\begin{psmallmatrix}-1&0\\1&0\end{psmallmatrix}$ o $\begin{psmallmatrix}0&0\\1&0\end{psmallmatrix}$ non si può dire nulla. Il primo punto si dimostra usando come funzione di Lyapunov per il sistema non lineare quella $V=(x-x_e)'Q(x-x_e)$ del linearizzato (vedi [[TDS - Criterio di Lyapunov]]). Osserva anche che se $J(x_e)$ ha rango pieno l'equilibrio è isolato (condizione sufficiente, non necessaria: $\dot x=-x^3$ ha $J=0$ ma un solo equilibrio). _(libro, §3.5–3.5.1, pp. 131–133)_

> [!example] Dal libro — il pendolo
> $\dot x_1=x_2$, $\dot x_2=-\frac gl\sin x_1-\frac kmx_2+\frac1{ml}u$. Gli equilibri sono $x_{e,2}=0$, $\sin x_{e,1}=0$, cioè $x_{e,1}=h\pi$: il pendolo fermo in basso ($h$ pari) o in alto ($h$ dispari). Linearizzando si trova che il primo è asintoticamente stabile (con attrito $k>0$) e il secondo instabile, come suggerisce l'intuizione. _(libro, §3.5.2, p. 133)_

## Modelli di epidemie: modello SIR

Vedi [[TDS - Punti di equilibrio]].

Un modello usato realmente. In un'epidemia ci sono persone sane ma **suscettibili** di ammalarsi, $S$, che si possono **infettare** entrando in contatto con gli **infetti**, $I$. I contatti fanno aumentare gli infetti e diminuire i suscettibili, proporzionalmente al prodotto $SI$ e a un coefficiente $\beta$ (probabilità di infezione e altri fattori):

$$\begin{cases}\dot S=-\beta SI\\\dot I=\beta SI\end{cases}$$

I suscettibili possono aumentare (nascite, persone che entrano nel campione) di una quantità $B$, e qualcuno può morire per qualsiasi causa ($\mu_SS$):

$$\begin{cases}\dot S=-\beta SI+B-\mu_SS\\\dot I=\beta SI\end{cases}$$

Un infetto può guarire con probabilità $\gamma$ e diventare **recuperato** $R$ (sano e non più reinfettabile), oppure morire con probabilità $\mu_I$; anche i recuperati muoiono con tasso $\mu_R$:

$$\begin{cases}\dot S=-\beta SI+B-\mu_SS\\\dot I=\beta SI-\gamma I-\mu_II\\\dot R=\gamma I-\mu_RR\end{cases}$$

È il **modello SIR**, un modello vecchio e semplicissimo, **non lineare** per via dei prodotti $S\cdot I$.

### Punti di equilibrio

Si annullano le derivate:

$$\begin{cases}-\beta SI+B-\mu_SS=0\\\beta SI-\gamma I-\mu_II=0\\\gamma I-\mu_RR=0\end{cases}$$

Raccogliendo $I$ nella seconda, $I(\beta S-\gamma-\mu_I)=0$: due possibilità, $I=0$ oppure $S=\frac{\gamma+\mu_I}{\beta}$.

**Primo equilibrio** ($I=0$), sostituendo nelle altre:

$$S=\frac{B}{\mu_S},\qquad I=0,\qquad R=0$$

**Secondo equilibrio** ($S=\frac{\gamma+\mu_I}{\beta}$): dalla prima equazione $I=\frac{B-\mu_SS}{\beta S}$, dalla terza $R=\frac{\gamma}{\mu_R}I$:

$$S=\frac{\gamma+\mu_I}{\beta},\qquad I=\frac{B}{\gamma+\mu_I}-\frac{\mu_S}{\beta},\qquad R=\frac{\gamma}{\mu_R}I$$

Il primo equilibrio dice che, se non ci sono infetti, la popolazione resta costante (**niente epidemia**). Il secondo, meno banale, descrive suscettibili, infetti e recuperati che non variano nel tempo: una situazione **endemica**, con un numero costante di infetti. Ha senso fisico solo se $I>0$, cioè se $\frac{\beta B}{\mu_S(\gamma+\mu_I)}>1$.

### Stabilità del primo equilibrio

Si linearizza. La matrice $A$ è lo **jacobiano** di $f=(f_1,f_2,f_3)$ (le tre equazioni) rispetto a $(S,I,R)$:

$$A=J(x)\big|_{x_e}=\begin{pmatrix}\frac{\partial f_1}{\partial S}&\frac{\partial f_1}{\partial I}&\frac{\partial f_1}{\partial R}\\[1mm]\frac{\partial f_2}{\partial S}&\frac{\partial f_2}{\partial I}&\frac{\partial f_2}{\partial R}\\[1mm]\frac{\partial f_3}{\partial S}&\frac{\partial f_3}{\partial I}&\frac{\partial f_3}{\partial R}\end{pmatrix}_{x_e}=\begin{pmatrix}-\beta I-\mu_S&-\beta S&0\\\beta I&\beta S-\gamma-\mu_I&0\\0&\gamma&-\mu_R\end{pmatrix}_{x_e}$$

(per esempio $\frac{\partial f_1}{\partial R}=0$ perché $f_1=-\beta SI+B-\mu_SS$ non contiene $R$, e $\frac{\partial f_1}{\partial S}=-\beta I-\mu_S$). Nel primo equilibrio:

$$A_1=\begin{pmatrix}-\mu_S&-\frac{\beta B}{\mu_S}&0\\0&\frac{\beta B}{\mu_S}-\gamma-\mu_I&0\\0&\gamma&-\mu_R\end{pmatrix}$$

Per la struttura particolare di $A_1$ (sviluppando il determinante lungo la prima colonna e poi lungo la terza) gli autovalori sono gli elementi diagonali:

$$\lambda_1=-\mu_S,\qquad\lambda_2=\frac{\beta B}{\mu_S}-\gamma-\mu_I,\qquad\lambda_3=-\mu_R$$

Tutti i parametri ($\mu_S,\mu_I,\mu_R,\beta,B,\gamma$) sono **positivi**, quindi $\lambda_1$ e $\lambda_3$ sono sicuramente negativi. Il sistema è asintoticamente stabile in questo equilibrio se

$$\lambda_2=\frac{\beta B}{\mu_S}-\gamma-\mu_I<0\iff\frac{\beta B}{\mu_S(\gamma+\mu_I)}<1$$

La quantità $\frac{\beta B}{\mu_S(\gamma+\mu_I)}$ si indica spesso con $R_0$ (**numero di riproduzione di base**).

> [!tip] Interpretazione di $R_0$
> $\frac{B}{\mu_S}$ è la popolazione di suscettibili in assenza di malattia, $\beta\frac{B}{\mu_S}$ il ritmo con cui un infetto ne contagia altri, e $\frac1{\gamma+\mu_I}$ il tempo medio per cui resta infetto. $R_0$ è quindi il numero medio di persone contagiate da un infetto in una popolazione tutta suscettibile. Se $R_0<1$ l'equilibrio "senza epidemia" è asintoticamente stabile: pochi infetti introdotti si estinguono. Se $R_0>1$ è instabile (per il teorema, perché $\lambda_2>0$) e compare l'equilibrio endemico, studiato nella [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto|lezione successiva]].
