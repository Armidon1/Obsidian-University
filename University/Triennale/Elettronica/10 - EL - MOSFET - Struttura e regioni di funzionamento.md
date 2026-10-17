---
title: "MOSFET - Struttura e regioni di funzionamento"
aliases:
  - "EL — MOSFET - Struttura e regioni di funzionamento"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# MOSFET - Struttura e regioni di funzionamento

> [!abstract]
> Il MOSFET controlla una corrente tramite un campo elettrico; distinguere le regioni operative permette di usarlo come amplificatore o interruttore.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 113–129.

Precedente: [[09 - EL - Semiconduttori e diodi]] · Successiva: [[11 - EL - MOSFET - Polarizzazione e specchi di corrente]]

## Struttura MOS e formazione del canale

Per il ripasso: [[EL - Struttura MOSFET]] · [[EL - Inversione e tensione di soglia]].

MOS significa **metal–oxide–semiconductor**, FET **field-effect transistor**. Il gate è separato dal semiconduttore da un ossido isolante: la tensione applicata controlla elettrostaticamente la superficie. Il body è un quarto terminale, spesso collegato a un riferimento comune; il dispositivo non è intrinsecamente a soli tre terminali.

In un NMOS ad arricchimento il body è p e le regioni di source e drain sono n+. Un gate sufficientemente positivo respinge le lacune e attrae elettroni: prima si forma una zona svuotata, poi uno strato di inversione n che collega source e drain. Si definisce $V_{GS}=V_G-V_S$; il canale conduttivo del modello forte inversione richiede $V_{GS}>V_{th}$.

Il gate ideale non assorbe corrente continua, ma possiede capacità che richiedono corrente quando la tensione varia. La corrente convenzionale di drain nell’NMOS entra dal drain e va al source; gli elettroni si muovono nel verso opposto.

Le giunzioni tra body e diffusioni devono restare opportunamente polarizzate per isolare i dispositivi. Le dimensioni W e L determinano la geometria di canale e influenzano corrente e capacità.

_(dispensa, pp. 113–115)_

![[EL-p113-1.png]]

La struttura MOS separa il gate metallico dal body tramite l’ossido. _(dispensa, p. 113)_

![[EL-p113-2.png]]

Un gate positivo sotto soglia allontana le lacune e crea una regione di svuotamento. _(dispensa, p. 113)_

![[EL-p113-3.png]]

Oltre soglia si forma uno strato di inversione ricco di elettroni sotto l’ossido. _(dispensa, p. 113)_

![[EL-p114-1.png]]

Le diffusioni n+ creano source e drain nel body p dell’NMOS. _(dispensa, p. 114)_

![[EL-p114-2.png]]

Senza canale, le giunzioni impediscono una corrente continua significativa fra drain e source nelle polarizzazioni mostrate. _(dispensa, p. 114)_

![[EL-p114-3.png]]

La tensione di gate crea il canale e permette il passaggio della corrente fra le diffusioni. _(dispensa, p. 114)_

![[EL-p115-1.png]]

La vista tridimensionale e la sezione identificano larghezza W, lunghezza L e terminali. _(dispensa, p. 115)_

![[EL-p115-2.png]]

Per piccoli VDS la pendenza aumenta con la tensione di gate perché il canale conduce più facilmente. _(dispensa, p. 115)_

## Triodo, pinch-off e saturazione

Per il ripasso: [[EL - Regioni di funzionamento NMOS]] · [[EL - Pinch-off]].

La tensione locale del canale cresce dal source al drain. La carica d’inversione, proporzionale a $V_{GS}-V_{th}-V(x)$, diminuisce quindi verso il drain. Si definisce l’**overdrive** $V_{OV}=V_{GS}-V_{th}$.

Per un NMOS con $V_{DS}\ge0$:

| Regione | Condizione | Comportamento |
|---|---|---|
| Interdizione | $V_{GS}\le V_{th}$ | $I_D\simeq0$ nel modello semplificato |
| Triodo | $V_{GS}>V_{th}$, $0\le V_{DS}<V_{OV}$ | Corrente dipende da gate e drain |
| Saturazione | $V_{GS}>V_{th}$, $V_{DS}\ge V_{OV}$ | Corrente poco sensibile al drain |

Al confine $V_{DS}=V_{OV}$ la carica d’inversione al bordo drain tende a zero: è il **pinch-off**. Gli elettroni che arrivano dal canale sono trascinati dal campo verso il drain. Il canale non diventa un circuito aperto.

> [!warning] Correzione
> Pp. 116–117 spiegano la corrente dopo il pinch-off con una valanga in una nuova giunzione. La normale saturazione del MOSFET **non richiede breakdown a valanga**: i portatori attraversano la regione ad alto campo verso il drain. La valanga è un fenomeno distinto, associato a tensioni sufficientemente elevate.

_(dispensa, pp. 116–118)_

![[EL-p116-1.png]]

Con piccolo VDS il potenziale locale cambia poco e il canale resta quasi uniforme. _(dispensa, p. 116)_

![[EL-p116-2.png]]

Con VDS maggiore il canale si assottiglia verso il drain perché diminuisce la differenza locale gate-canale. _(dispensa, p. 116)_

![[EL-p117-1.png]]

La figura del sorgente attribuisce erroneamente il funzionamento al breakdown: leggere il callout di correzione sul pinch-off. _(dispensa, p. 117)_

![[EL-p117-2.png]]

La caratteristica passa dalla regione di triodo alla saturazione al valore VDS uguale all’overdrive. _(dispensa, p. 117)_

![[EL-p118-1.png]]

La curva di confine separa triodo e saturazione per diverse tensioni di gate. _(dispensa, p. 118)_

## Leggi di corrente e convenzione per K

Per il ripasso: [[EL - Leggi di corrente del MOSFET]] · [[EL - Resistenza di canale]].

Il modello a canale lungo usa la capacità d’ossido **per unità di area** $C_{ox}=\varepsilon_{ox}/t_{ox}$. In questi appunti si mantiene la convenzione del libro:
$$K=\frac12\mu_n C_{ox}\frac WL\quad[\mathrm{A/V^2}].$$
La carica mobile per unità d’area ha modulo $C_{ox}[V_{OV}-V(x)]$. Applicando il trasporto per deriva e integrando lungo il canale:
$$I_DL=\mu_nWC_{ox}\int_0^{V_{DS}}(V_{OV}-V)\,dV.$$
Ne segue:
$$I_D=K[2V_{OV}V_{DS}-V_{DS}^2]\quad\text{in triodo},$$
$$I_D=KV_{OV}^2\quad\text{in saturazione ideale}.$$
Per $V_{DS}\ll V_{OV}$ si trascura il termine quadratico e il canale equivale a una resistenza:
$$R_{ch}\simeq\frac1{2KV_{OV}}.$$
Non tutta la regione di triodo è rigorosamente ohmica: l’approssimazione richiede un $V_{DS}$ piccolo rispetto all’overdrive.

> [!warning] Correzione
> Pp. 121–122 chiamano transconduttanza $K(V_{GS}-V_{th})^2$: questa espressione è una **corrente**, misurata in A. La transconduttanza è la derivata $g_m=\partial I_D/\partial V_{GS}$, in A/V. Anche il modello resistivo di p. 121 va letto con $R_{ch}=1/[2K(V_{GS}-V_{th})]$, senza un ulteriore $V_{DS}$ al numeratore. In alcuni schemi equivalenti di pp. 119–122 compare inoltre Rin=0 accanto a un ingresso disegnato aperto: il gate ideale ha resistenza di ingresso infinita.

_(dispensa, pp. 119–122)_

![[EL-p119-1.png]]

Il simbolo identifica gate isolato, drain e source; il body è qui sottinteso. _(dispensa, p. 119)_

![[EL-p119-2.png]]

La scelta di source comune consente di leggere VGS come ingresso e la corrente di drain come uscita. _(dispensa, p. 119)_

![[EL-p119-3.png]]

Il modello a due porte richiama una sorgente di corrente controllata dalla tensione. _(dispensa, p. 119)_

![[EL-p119-4.png]]

Il gate ideale va letto come ingresso aperto e resistenza infinita: eventuali scritte Rin=0 nella figura originale sono un refuso. _(dispensa, p. 119)_

![[EL-p120-1.png]]

La porzione differenziale del canale permette di integrare la corrente lungo la direzione source-drain. _(dispensa, p. 120)_

![[EL-p121-1.png]]

In interdizione il cammino drain-source è aperto e la corrente è nulla nel modello semplificato. _(dispensa, p. 121)_

![[EL-p121-2.png]]

In triodo il canale conduce; l’approssimazione di resistenza costante richiede VDS molto minore dell’overdrive. _(dispensa, p. 121)_

![[EL-p122-1.png]]

In saturazione ideale il dispositivo impone una corrente quadratica nella tensione di overdrive. _(dispensa, p. 122)_

![[EL-p122-2.png]]

La transcaratteristica di saturazione è un ramo di parabola sopra soglia; il ramo a sinistra non va usato come regione accesa. _(dispensa, p. 122)_

## Modulazione della lunghezza di canale

Per il ripasso: [[EL - Modulazione di canale e resistenza di uscita]].

Aumentando $V_{DS}$ in saturazione, il punto di pinch-off si sposta e la lunghezza conduttiva effettiva cambia. Il modello correttivo è:
$$I_D\simeq KV_{OV}^2(1+\lambda V_{DS}).$$
Le caratteristiche non sono più orizzontali; la loro estrapolazione incontra circa $-V_A$, con $\lambda\simeq1/|V_A|$. La resistenza incrementale d’uscita è:
$$r_o=\left(\frac{\partial I_D}{\partial V_{DS}}\right)^{-1}\simeq\frac1{\lambda I_D}\simeq\frac{|V_A|}{I_D}.$$
L’ultima forma è un’approssimazione per il consueto modello con modulazione debole. La resistenza è incrementale, non il rapporto statico $V_{DS}/I_D$. Nel modello ideale $\lambda=0$ e $r_o\to\infty$.

_(dispensa, p. 123)_

![[EL-p123-1.png]]

Senza modulazione di canale le caratteristiche di saturazione sono orizzontali. _(dispensa, p. 123)_

![[EL-p123-2.png]]

Con modulazione le rette estrapolate convergono verso la tensione di Early e la loro pendenza introduce ro. _(dispensa, p. 123)_

## PMOS, CMOS e transistor a svuotamento

Per il ripasso: [[EL - PMOS e tecnologia CMOS]] · [[EL - MOS ad arricchimento e a svuotamento]].

Nel PMOS polarità e portatori sono complementari: body n, diffusioni p+, canale di lacune. Per evitare ambiguità si usano le grandezze positive $V_{SG}$, $V_{SD}$ e $|I_D|$:
$$V_{SG}>|V_{thp}|,\qquad V_{SD}\ge V_{SG}-|V_{thp}|\quad\text{in saturazione}.$$
Con questi riferimenti le leggi hanno la stessa forma dell’NMOS, sostituendo $K_n$ con $K_p$.

La tecnologia CMOS integra entrambi i tipi, per esempio creando un pozzo n per i PMOS in un substrato p. Un transistor a **svuotamento** possiede già un canale a tensione gate-source nulla; uno ad **arricchimento** è normalmente spento nel modello semplificato.

| Dispositivo | Segno della soglia | Stato a $V_{GS}=0$ |
|---|---|---|
| NMOS ad arricchimento | $V_{th}>0$ | OFF |
| NMOS a svuotamento | $V_{th}<0$ | ON |
| PMOS ad arricchimento | $V_{th}<0$ | OFF |
| PMOS a svuotamento | $V_{th}>0$ | ON |

Nel modello tecnologico della dispensa $\mu_n\simeq3\mu_p$. Per la stessa forza di pilotaggio e la stessa L si usa quindi una W maggiore per il PMOS; il fattore esatto dipende dal processo.

_(dispensa, pp. 124–126)_

![[EL-p124-1.png]]

Le caratteristiche PMOS si leggono con tensioni VSD positive per mantenere la forma del modello NMOS. _(dispensa, p. 124)_

![[EL-p124-2.png]]

Il simbolo PMOS indica il dispositivo complementare e il verso convenzionale opposto della corrente. _(dispensa, p. 124)_

![[EL-p124-3.png]]

La sezione PMOS scambia i tipi di drogaggio e le polarità rispetto all’NMOS. _(dispensa, p. 124)_

![[EL-p125-1.png]]

Il pozzo n permette di costruire PMOS insieme a NMOS sullo stesso substrato di base. _(dispensa, p. 125)_

![[EL-p125-2.png]]

Nel transistor a svuotamento esiste corrente anche con VGS nulla. _(dispensa, p. 125)_

![[EL-p125-3.png]]

La transcaratteristica del dispositivo a svuotamento ha soglia negativa e corrente non nulla all’origine del gate. _(dispensa, p. 125)_

![[EL-p126-1.png]]

Il simbolo con canale continuo richiama che il canale è già presente senza polarizzazione di gate. _(dispensa, p. 126)_

## Retta di carico, amplificazione e inverter

Per il ripasso: [[EL - MOSFET come amplificatore e inverter]].

Per un NMOS con source a massa e resistore di drain:
$$V_{DS}=V_{DD}-R_DI_D.$$
La retta di carico incontra ogni caratteristica a $V_{GS}$ fissata in un punto di lavoro. Seguendo questi punti al variare di $V_{GS}$ si ricava la transcaratteristica $v_o(v_i)$: uscita alta in interdizione, tratto invertente nella regione di amplificazione, uscita bassa per forte conduzione in triodo.

Per amplificare si imposta un punto in saturazione e si usa un piccolo segnale attorno a esso. Per l’inverter si scelgono i due estremi: ingresso basso → transistor OFF → uscita alta; ingresso alto → canale a bassa resistenza → uscita bassa.

> [!important] Due significati di saturazione
> La **saturazione del MOSFET** è la regione tipicamente usata per amplificare. La **saturazione dell’amplificatore** è il clipping dell’uscita, che impedisce l’amplificazione lineare. I termini descrivono fenomeni diversi.

Nell’esempio di p. 129, $V_{DD}=20\,\mathrm V$, $R_D=1.33\,\mathrm{k\Omega}$, polarizzazione $V_{GS}=5\,\mathrm V$ e segnale $\pm0.5\,\mathrm V$: la retta ha intercette 20 V e circa 15.04 mA. Si usano le caratteristiche per 4.5, 5 e 5.5 V; il grafico permette di verificare se tutto il percorso resta nella regione scelta.

_(dispensa, pp. 127–129)_

![[EL-p127-1.png]]

La tensione d’uscita sul drain dipende dalla caduta causata dalla corrente in RD. _(dispensa, p. 127)_

![[EL-p127-2.png]]

La retta di carico ha intercette VDD e VDD diviso RD. _(dispensa, p. 127)_

![[EL-p127-3.png]]

Le caratteristiche del dispositivo cambiano al variare della tensione di gate. _(dispensa, p. 127)_

![[EL-p127-4.png]]

Ogni intersezione determina un punto di lavoro compatibile sia con il MOS sia con il carico. _(dispensa, p. 127)_

![[EL-p127-5.png]]

La transcaratteristica è alta in OFF, invertente nel tratto centrale e bassa per forte conduzione. _(dispensa, p. 127)_

![[EL-p127-6.png]]

Il percorso dei punti sulla retta di carico spiega l’evoluzione della tensione d’uscita. _(dispensa, p. 127)_

![[EL-p128-1.png]]

Il punto Q permette al segnale di oscillare nel tratto utile senza raggiungere gli estremi. _(dispensa, p. 128)_

![[EL-p129-1.png]]

Il segnale si sovrappone a una polarizzazione di 5 V e il carico resistivo converte le variazioni di corrente in tensione. _(dispensa, p. 129)_

![[EL-p129-2.png]]

Le caratteristiche a 4.5, 5 e 5.5 V intersecano la medesima retta, definendo l’escursione di segnale. _(dispensa, p. 129)_

