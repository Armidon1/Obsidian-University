---
title: "Circuiti digitali e logica CMOS"
aliases:
  - "EL — Circuiti digitali e logica CMOS"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Circuiti digitali e logica CMOS

> [!abstract]
> I bit si realizzano con tensioni e correnti: margini di rumore, tempi, potenza e struttura delle reti complementari determinano l’affidabilità della logica.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 165–185.

Precedente: [[12 - EL - MOSFET - Piccolo segnale e carichi attivi]] · Successiva: [[14 - EL - Esercizi di esame svolti]]

## Inverter e margini di rumore

Per il ripasso: [[EL - Margini di rumore]].

Un inverter realizza $Y=\overline A$. La transcaratteristica ideale passa istantaneamente dal livello alto a quello basso; quella reale ha una regione intermedia ripida. Vicino ai livelli validi si desidera $|dv_o/dv_i|<1$, così piccoli disturbi si attenuano attraversando le porte; nella zona di transizione il modulo della pendenza supera 1.

| Simbolo | Significato |
|---|---|
| $V_{IL}$ | Massima tensione d’ingresso riconosciuta come bassa |
| $V_{IH}$ | Minima tensione d’ingresso riconosciuta come alta |
| $V_{OL}$ | Massima tensione d’uscita garantita bassa |
| $V_{OH}$ | Minima tensione d’uscita garantita alta |

I margini sono:
$$NM_L=V_{IL}-V_{OL},\qquad NM_H=V_{OH}-V_{IH}.$$
Nel modello grafico si scelgono spesso $V_{IL}$ e $V_{IH}$ nei punti a pendenza −1. Tra essi non si garantisce una corretta interpretazione binaria. Una caratteristica centrata nella dinamica aiuta a rendere simili i due margini; la robustezza è limitata dal minore, senza bisogno di ipotizzare che gli zeri e gli uni siano equiprobabili.

_(dispensa, pp. 165–167)_

![[EL-p165-1.png]]

La caratteristica ideale e l’interruttore controllato collegano il comportamento elettrico all’operazione NOT. _(dispensa, p. 165)_

![[EL-p165-2.png]]

Un NMOS si approssima come aperto in OFF e resistivo quando fortemente acceso. _(dispensa, p. 165)_

![[EL-p166-1.png]]

La curva reale introduce livelli validi e punti di pendenza −1, che delimitano i margini di rumore. _(dispensa, p. 166)_

![[EL-p167-1.png]]

Una transcaratteristica più ripida lascia più spazio ai livelli logici validi. _(dispensa, p. 167)_

![[EL-p167-2.png]]

Centrare la transizione nella dinamica evita che uno dei due margini diventi il collo di bottiglia. _(dispensa, p. 167)_

## Tempi di salita e propagazione

Per il ripasso: [[EL - Tempi di commutazione e propagazione]].

Le capacità devono essere caricate o scaricate; perciò le tensioni dei nodi non cambiano istantaneamente.

Il tempo di salita $t_r$ si misura dal 10% al 90% dell’escursione; quello di discesa $t_f$ dal 90% al 10%. Il ritardo di propagazione si misura tra l’attraversamento del 50% all’ingresso e quello corrispondente all’uscita. Il pedice di $t_{pHL}$ indica **l’uscita** alta→bassa; $t_{pLH}$ indica bassa→alta.

Per una risposta RC esponenziale, $t_r=\tau\ln9\simeq2.197\tau$ e il tempo dal gradino al 50% è $\tau\ln2\simeq0.693\tau$. Non sono uguali all’assestamento a $5\tau$.

Il ritardo peggiore limita un percorso logico. Il clock di un sistema completo deve lasciare tempo all’intero percorso e agli elementi sequenziali, non soltanto a una singola porta.

_(dispensa, p. 168)_

![[EL-p168-1.png]]

I tempi di salita e discesa usano soglie 10–90%; quelli di propagazione confrontano gli attraversamenti al 50%. _(dispensa, p. 168)_

## Inverter resistivo - energia, potenza e ritardo

Per il ripasso: [[EL - Potenza dinamica CMOS]] · [[EL - Inverter resistivo e compromesso potenza-ritardo]].

L’inverter con NMOS e pull-up resistivo dissipa potenza continua quando l’uscita è bassa: $P_L\simeq V_{DD}^2/R$ se la resistenza ON del MOS è trascurabile. Quando l’uscita è alta e il MOS è spento, $P_H\simeq0$. Con probabilità di uscita bassa $p_L$:
$$P_{stat}\simeq p_L\frac{V_{DD}^2}{R}.$$
L’espressione $V_{DD}^2/(2R)$ usa l’ipotesi particolare $p_L=1/2$.

Per caricare C da zero a $V_{DD}$, l’alimentazione fornisce:
$$E_{supply}=\int V_{DD}i(t)dt=CV_{DD}^2.$$
Metà resta immagazzinata, $E_C=CV_{DD}^2/2$; metà si dissipa nel percorso di carica. La successiva scarica dissipa l’energia immagazzinata. Un ciclo completo 0→1→0 dissipa complessivamente $CV_{DD}^2$. Se ci sono $\alpha f$ transizioni di carica per secondo:
$$P_{dyn}=\alpha fCV_{DD}^2.$$

Il fronte d’uscita crescente ha circa $\tau_{LH}=RC$. Quello decrescente ha $\tau_{HL}\simeq(R\parallel R_{on})C$ e valore finale non esattamente zero se $R_{on}$ non è trascurabile. Diminuire R accelera la salita ma aumenta la potenza statica: nasce il compromesso ritardo-potenza. Con le approssimazioni della dispensa, $P_{stat}\tau_{LH}=CV_{DD}^2/2$.

> [!warning] Correzione
> Pp. 169–170 chiamano potenza $V_{DD}\int i\,dt$ e $CV_{DD}^2$. Sono **energie**, misurate in joule. Solo moltiplicando l’energia per la frequenza degli eventi si ottiene una potenza. Anche l’ipotesi di un ciclo completo per clock va esplicitata tramite l’attività $\alpha$.

_(dispensa, pp. 169–171)_

![[EL-p171-1.png]]

Il carico capacitivo rende la risposta d’uscita più lenta del fronte di ingresso. _(dispensa, p. 171)_

## Porte con interruttori e tecnologia NMOS

Le reti di interruttori combinano condizioni: due interruttori in serie conducono se entrambi sono chiusi, in parallelo se almeno uno è chiuso. Un pull-down comandato dagli ingressi realizza l’inversione della condizione che lo rende conduttivo.

| A | B | AND | OR | NAND | NOR |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

Un carico NMOS a svuotamento sostituisce la resistenza fisica, ma quando il driver conduce resta un cammino di corrente continua. Con $V_{GS,carico}=0$ e carico saturo, $I_L=K_LV_{th,L}^2$, usando la soglia negativa al quadrato. Con uscita bassa la potenza è $V_{DD}I_L$; per occupazioni equiprobabili la media è la metà.

Per ricavare analiticamente le soglie logiche si impone l’uguaglianza tra correnti di driver e carico nelle regioni appropriate, si deriva implicitamente la relazione e si cerca pendenza −1. Le formule devono mantenere la stessa convenzione per K, incluso il fattore 2 nella legge di triodo.

_(dispensa, pp. 172–173)_

![[EL-p172-1.png]]

Le reti a interruttori mostrano serie per la condizione AND e parallelo per OR, con inversioni secondo il nodo osservato. _(dispensa, p. 172)_

![[EL-p173-1.png]]

Il carico NMOS a svuotamento evita la grande resistenza ma mantiene un cammino di corrente continua nell’uscita bassa. _(dispensa, p. 173)_

## Inverter CMOS statico

Per il ripasso: [[EL - Inverter CMOS statico]].

L’inverter complementare collega i gate di NMOS e PMOS all’ingresso comune. Il source NMOS è a massa; quello PMOS a $V_{DD}$:
$$V_{GSn}=v_i,\qquad V_{SGp}=V_{DD}-v_i.$$
Per $v_i=0$ il transistor n è spento e il p porta alta l’uscita. Per $v_i=V_{DD}$ il p è spento e l’n porta bassa l’uscita. Nel modello ideale, senza carico continuo e perdite, non esiste un percorso continuo tra alimentazione e massa nei due stati estremi: $P_{stat}=0$.

Durante la transizione possono condurre entrambi. Il percorso sulla transcaratteristica si ricava da $I_n=|I_p|$: dapprima n saturo/p in triodo, poi entrambi saturi, infine n in triodo/p saturo. Con modulazione nulla il tratto centrale può essere verticale; con resistenze d’uscita finite ha guadagno grande ma finito.

Il consumo statico nullo è un limite ideale: nei dispositivi reali ci sono perdite. La proprietà dipende anche dal carico e dalla presenza di ingressi logici validi.

_(dispensa, pp. 174–176)_

![[EL-p174-1.png]]

Nell’inverter CMOS entrambi i gate ricevono lo stesso ingresso, così le tensioni di controllo variano in versi opposti. _(dispensa, p. 174)_

![[EL-p175-1.png]]

Le caratteristiche n e p si confrontano usando lo stesso nodo d’uscita e riferimenti di tensione coerenti. _(dispensa, p. 175)_

![[EL-p175-2.png]]

Con ingresso nullo l’NMOS è spento e l’uscita si porta al rail alto. _(dispensa, p. 175)_

![[EL-p175-3.png]]

Finché l’ingresso resta sotto la soglia n, il punto d’uscita rimane alto. _(dispensa, p. 175)_

![[EL-p175-4.png]]

Quando entrambi conducono le intersezioni si spostano e l’uscita scende verso la regione di transizione. _(dispensa, p. 175)_

![[EL-p176-1.png]]

L’aumento ulteriore dell’ingresso porta il PMOS verso lo spegnimento e l’uscita verso massa. _(dispensa, p. 176)_

![[EL-p176-2.png]]

La caratteristica completa del CMOS raggiunge i due rail nel modello ideale. _(dispensa, p. 176)_

![[EL-p176-3.png]]

Agli ingressi estremi uno dei MOS interrompe il percorso continuo e la corrente statica ideale è nulla. _(dispensa, p. 176)_

## Simmetria e soglie del CMOS

Per il ripasso: [[EL - Dimensionamento simmetrico CMOS]].

Nel tratto con entrambi saturi:
$$K_n(V_M-V_{thn})^2=K_p(V_{DD}-V_M-|V_{thp}|)^2.$$
Se le soglie sono uguali in modulo, la commutazione è centrata a $V_M=V_{DD}/2$ quando $K_n=K_p$. Con $\mu_n\simeq3\mu_p$ e uguale L, ciò richiede circa $W_p=3W_n$.

Il calcolo del libro assume soglie uguali, $K_n=K_p$, modello quadratico e $\lambda=0$. Imponendo pendenza −1 nei tratti laterali si ottiene:
$$V_{IL}=\frac{3V_{DD}+2V_{th}}8,\qquad V_{IH}=\frac{5V_{DD}-2V_{th}}8.$$
Usando i livelli **nominali ai rail**, $V_{OL}=0$, $V_{OH}=V_{DD}$, i margini nominali della dispensa risultano entrambi $(3V_{DD}+2V_{th})/8$.

> [!warning] Correzione
> Il materiale passa dalla definizione a p. 166 di $V_{OH}$ e $V_{OL}$ come uscite nei punti a pendenza −1 all’uso dei rail nominali a pp. 176–178. Le due convenzioni non vanno mescolate. Se si scelgono i valori della curva nei punti a pendenza −1, il modello dà $V_{OL}=(V_{DD}-2V_{th})/8$, $V_{OH}=V_{DD}-V_{OL}$ e margini $V_{DD}/4+V_{th}/2$. Per un componente reale si usano le specifiche garantite, dichiarando condizioni e carico.

_(dispensa, pp. 177–178)_

![[EL-p177-1.png]]

I punti a pendenza −1 e la posizione della transizione determinano i margini di rumore, con le convenzioni precisate nel testo. _(dispensa, p. 177)_

## Scarica del carico e tempi di propagazione CMOS

Per il ripasso: [[EL - Ritardo di propagazione CMOS]].

Se l’ingresso sale idealmente a $V_{DD}$, il PMOS si spegne e l’NMOS scarica C. All’inizio $v_o=V_{DD}$ per continuità e l’NMOS è **saturo**, quindi conduce corrente quasi costante $K(V_{DD}-V_{th})^2$. Quando $v_o$ scende sotto $V_{DD}-V_{th}$ passa in triodo e la corrente diminuisce.

Per $0<V_{th}<V_{DD}/2$, il ritardo fino a $V_{DD}/2$ comprende due tratti. Ponendo $a=V_{DD}-V_{th}$:
$$t_{sat}=\frac{CV_{th}}{Ka^2},\qquad
t_{tri}=C\int_{V_{DD}/2}^{a}\frac{dv}{K(2av-v^2)}
=\frac{C}{2Ka}\ln\frac{3V_{DD}-4V_{th}}{V_{DD}}.$$
Quindi $t_{pHL}=t_{sat}+t_{tri}$. Con dimensionamento simmetrico il fronte opposto ha lo stesso tempo nel modello. Per $V_{th}=0.2V_{DD}$:
$$t_{pHL}=t_{pLH}\simeq0.805\frac{C}{KV_{DD}},$$
coerente con l’approssimazione 0.8 della dispensa.

> [!warning] Correzione
> A p. 179 si chiama il MOS saturo «cortocircuito». In questa prima fase esso si comporta approssimativamente come un **generatore di corrente**: la scarica iniziale è una rampa. La regione di triodo viene raggiunta dopo.

_(dispensa, pp. 179–181)_

![[EL-p179-1.png]]

Il comando rettangolare fa caricare e scaricare il condensatore d’uscita. _(dispensa, p. 179)_

![[EL-p179-2.png]]

Il condensatore mantiene inizialmente la tensione mentre cambia il transistor che conduce. _(dispensa, p. 179)_

![[EL-p179-3.png]]

Appena l’ingresso commuta il punto passa sulla caratteristica accesa senza cambiare la tensione su C. _(dispensa, p. 179)_

![[EL-p179-4.png]]

Scaricandosi C, il punto percorre prima la zona satura poi la zona di triodo verso l’origine. _(dispensa, p. 179)_

![[EL-p179-5.png]]

Il confronto temporale rende visibile il ritardo dell’uscita rispetto ai fronti di ingresso. _(dispensa, p. 179)_

![[EL-p180-1.png]]

Il ritardo di propagazione termina al passaggio dell’uscita per metà dell’escursione. _(dispensa, p. 180)_

## Consumo durante la commutazione

Per il ripasso: [[EL - Corrente di cortocircuito CMOS]].

Con un fronte d’ingresso di durata finita entrambi i transistor possono condurre contemporaneamente, generando una corrente diretta tra alimentazione e massa. Il picco si trova nella regione centrale. A questo contributo si aggiungono la carica delle capacità e le perdite statiche:
$$P_{tot}\simeq\alpha fC_LV_{DD}^2+P_{sc}+P_{leak}.$$
Il primo termine è il consumo capacitivo; $P_{sc}$ è il contributo di conduzione simultanea; $P_{leak}$ raccoglie le perdite. Fronti d’ingresso più lenti possono aumentare il tempo trascorso con entrambi i dispositivi accesi.

> [!warning] Correzione
> P. 182 dice che questa corrente «non è dovuta all’alimentazione». L’ingresso lento ne causa l’esistenza, ma la corrente scorre tra le alimentazioni e l’energia dissipata è fornita dall’alimentazione stessa.

_(dispensa, p. 182)_

![[EL-p182-1.png]]

L’ingresso attraversa regioni con un solo MOS acceso o con entrambi in conduzione. _(dispensa, p. 182)_

![[EL-p182-2.png]]

La corrente diretta fra alimentazione e massa ha un massimo nella regione centrale della transizione. _(dispensa, p. 182)_

## Reti complementari, NAND e NOR

Per il ripasso: [[EL - Reti pull-up e pull-down]] · [[EL - Porte NAND e NOR CMOS]].

La rete di **pull-down** NMOS porta a zero l’uscita; la rete di **pull-up** PMOS la porta a $V_{DD}$. Le due reti sono duali: serie nell’una corrisponde a parallelo nell’altra. Un PMOS comandato da A conduce quando A è basso: non occorre per questo aggiungere un invertitore al suo gate.

| Porta | Pull-down NMOS | Pull-up PMOS | Funzione |
|---|---|---|---|
| NAND a 2 ingressi | A e B in serie | A e B in parallelo | $\overline{AB}$ |
| NOR a 2 ingressi | A e B in parallelo | A e B in serie | $\overline{A+B}$ |

Ogni rete usa quattro transistor per due ingressi nel CMOS statico complementare. La frase del libro sui «due transistor» delle porte riguarda i modelli a interruttori o a carico semplice, non il conteggio del CMOS completo.

Per stimare i tempi si considera il percorso peggiore: n transistor in serie hanno resistenza approssimativamente n volte quella del singolo; in un parallelo il caso peggiore può essere un solo ramo acceso. Con lunghezze uguali:
$$\text{NOR: }K_{p,eq}\simeq K_p/n,\ K_{n,eq}\simeq K_n;$$
$$\text{NAND: }K_{n,eq}\simeq K_n/n,\ K_{p,eq}\simeq K_p.$$
Il modello di simmetria dà $W_p\simeq3nW_n$ nella NOR e $W_p\simeq3W_n/n$ nella NAND. I limiti minimi di geometria devono essere rispettati: per confrontare l’area a pari prestazioni si dimensiona il percorso lento, non si rendono arbitrariamente piccoli i PMOS. La serie di PMOS rende spesso la NOR meno conveniente a elevato numero di ingressi.

_(dispensa, pp. 183–184)_

![[EL-p183-1.png]]

Gli interruttori complementari evitano un cammino continuo fra i rail nelle combinazioni statiche valide. _(dispensa, p. 183)_

![[EL-p183-2.png]]

La NOR ha pull-down n in parallelo e pull-up p in serie. _(dispensa, p. 183)_

![[EL-p183-3.png]]

La NAND ha pull-down n in serie e pull-up p in parallelo. _(dispensa, p. 183)_

![[EL-p184-1.png]]

Nella NOR a quattro ingressi la catena p rallenta la carica del nodo e richiede un dimensionamento adeguato. _(dispensa, p. 184)_

![[EL-p184-2.png]]

Un inverter equivalente riassume separatamente la forza del pull-up e del pull-down sul carico capacitivo. _(dispensa, p. 184)_

## Porte complesse, XOR e decoder

Per il ripasso: [[EL - Logica CMOS complessa]] · [[EL - XOR e decoder]].

Per progettare una porta complessa si costruisce il pull-down dalla condizione che deve rendere l’uscita bassa; poi si ricava il pull-up duale scambiando serie e parallelo a ogni livello. Nell’esempio disegnato il pull-down conduce per $A[B+CD]$, quindi:
$$Y=\overline{A(B+CD)}.$$
Lo XOR a due ingressi vale:
$$A\oplus B=\overline AB+A\overline B.$$
| A | B | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Un decoder da n a $2^n$ associa ogni parola d’ingresso a una sola uscita attiva. Ogni uscita rappresenta un mintermine degli ingressi o dei loro complementi: per esempio con tre bit $Y_0=\overline b_2\overline b_1\overline b_0$ e $Y_7=b_2b_1b_0$. La polarità dell’uscita dipende dall’implementazione; nella matrice a NOR della figura la riga selezionata ha uscita alta quando tutti i suoi ingressi NOR sono bassi. Le commutazioni reali possono produrre transitori temporanei: la proprietà una-sola-uscita descrive il funzionamento logico a regime.

Collegamento con l’organizzazione digitale: [[Circuiti Combinatori e Addizionatori]].

_(dispensa, p. 185)_

![[EL-p185-1.png]]

I colori evidenziano la dualità serie-parallelo anche all’interno delle sottoreti della porta complessa. _(dispensa, p. 185)_

![[EL-p185-2.png]]

La tabella e la decomposizione dello XOR separano le due combinazioni con ingressi diversi. _(dispensa, p. 185)_

![[EL-p185-3.png]]

La rete a transistor dello XOR usa anche i segnali complementati e mantiene la dualità fra pull-up e pull-down. _(dispensa, p. 185)_

![[EL-p185-4.png]]

Il decoder a tre bit costruisce otto mintermini, uno per ciascuna parola possibile. _(dispensa, p. 185)_

![[EL-p185-5.png]]

La matrice NMOS realizza selezioni di riga dalle linee di indirizzo e dai loro complementi. _(dispensa, p. 185)_

