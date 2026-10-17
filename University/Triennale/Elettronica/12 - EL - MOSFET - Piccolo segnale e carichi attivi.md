---
title: "MOSFET - Piccolo segnale e carichi attivi"
aliases:
  - "EL — MOSFET - Piccolo segnale e carichi attivi"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# MOSFET - Piccolo segnale e carichi attivi

> [!abstract]
> Si linearizza il dispositivo attorno al punto di riposo e si analizzano guadagno, carico, bypass e limiti dei circuiti integrati.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 135–164.

Precedente: [[11 - EL - MOSFET - Polarizzazione e specchi di corrente]] · Successiva: [[13 - EL - Circuiti digitali e logica CMOS]]

## Linearizzazione e transconduttanza

Per il ripasso: [[EL - Piccolo segnale MOS]] · [[EL - Transconduttanza MOS]].

Si separano grandezze totali, continue e incrementali: $v_{GS}=V_{GSQ}+v_{gs}$, $i_D=I_{DQ}+i_d$. Con $\lambda=0$:
$$i_D=K(V_{OV}+v_{gs})^2=KV_{OV}^2+2KV_{OV}v_{gs}+Kv_{gs}^2.$$
Il termine quadratico distorce. Trascurandolo rispetto a quello lineare:
$$|v_{gs}|\ll2V_{OV},\qquad i_d\simeq g_mv_{gs},$$
$$g_m=2KV_{OV}=\frac{2I_{DQ}}{V_{OV}}=2\sqrt{KI_{DQ}}.$$
In pratica si sceglie un segnale molto più piccolo dell’overdrive per avere una buona linearità; occorre anche mantenere il transistor nella regione operativa per l’intera escursione.

> [!warning] Correzione
> P. 136 scrive $v_{gs}\ll2(V_{GS}-V_{th})^2$: le unità V e V² non coincidono. La condizione ricavata dal rapporto tra i termini è **$|v_{gs}|\ll2(V_{GSQ}-V_{th})$**.

Il modello incrementale ha ingresso di gate aperto alle basse frequenze, generatore $g_mv_{gs}$ da drain a source e, se si considera la modulazione, resistenza $r_o$ tra drain e source.

_(dispensa, pp. 135–137)_

![[EL-p135-1.png]]

Il segnale variabile si somma alla tensione continua che stabilisce il punto Q. _(dispensa, p. 135)_

![[EL-p135-2.png]]

Un’escursione grande percorre una regione curva della parabola e distorce la forma d’onda. _(dispensa, p. 135)_

![[EL-p136-1.png]]

La tangente in Q rappresenta bene soltanto un’escursione sufficientemente piccola. _(dispensa, p. 136)_

![[EL-p137-1.png]]

Il confronto distingue il generatore non lineare per grandi segnali dal modello lineare gm per piccoli segnali. _(dispensa, p. 137)_

![[EL-p137-2.png]]

Le sorgenti continue diventano riferimenti a massa per le sole variazioni di segnale. _(dispensa, p. 137)_

## Source comune e modello incrementale

Per il ripasso: [[EL - Amplificatore a source comune]].

Nel circuito di piccolo segnale si annullano le **variazioni** delle sorgenti continue: una tensione costante diventa massa per il segnale, una corrente costante diventa circuito aperto. Non si distrugge il punto di polarizzazione già calcolato: esso resta contenuto nei parametri $g_m$ e $r_o$.

Con source a massa per il segnale e resistore di drain:
$$v_o=-g_mv_{gs}R_D,\qquad A_v=-g_mR_D.$$
Con carico e resistenza intrinseca:
$$A_v=-g_m(R_D\parallel R_L\parallel r_o).$$
Un ingresso positivo aumenta la corrente assorbita dal nodo drain e ne abbassa la tensione: da qui il segno negativo. Aumentare $R_D$ aumenta il guadagno ma riduce $V_{DSQ}$ e può togliere margine alla saturazione.

_(dispensa, p. 138)_

![[EL-p138-1.png]]

Il MOS sostituito dal generatore gm per vgs rende immediato il segno invertente dell’uscita. _(dispensa, p. 138)_

![[EL-p138-2.png]]

La resistenza ro in parallelo alla sorgente controllata rappresenta la pendenza delle caratteristiche reali. _(dispensa, p. 138)_

## Esempio con bypass della resistenza di source

Per il ripasso: [[EL - Condensatore di bypass]] · [[EL - Degenerazione di source]].

Dati principali: $V_{DD}=10\,\mathrm V$, $R_A=6\,\mathrm{k\Omega}$, $R_B=4\,\mathrm{k\Omega}$, $R_D=2\,\mathrm{k\Omega}$, $R_S=0.5\,\mathrm{k\Omega}$, $R_L=10\,\mathrm{k\Omega}$, $R_{sig}=50\,\Omega$, $K=0.5\,\mathrm{mA/V^2}$, $V_{th}=1\,\mathrm V$, $\lambda=0$.

In continua i condensatori sono aperti. Si trova $V_G=4\,\mathrm V$, $V_{GSQ}=3\,\mathrm V$, $I_D=2\,\mathrm{mA}$, $V_S=1\,\mathrm V$, $V_D=6\,\mathrm V$, $V_{DS}=5\,\mathrm V$. Il transistor è saturo e $g_m=2\,\mathrm{mS}$.

I condensatori di accoppiamento bloccano le componenti continue della sorgente e del carico. Quello di **bypass** in parallelo a $R_S$ lascia la degenerazione attiva in continua, ma rende il source circa a massa per il segnale nella banda in cui la propria impedenza è piccola.

Con bypass efficace:
$$A_v=-g_m(R_D\parallel R_L)\frac{R_A\parallel R_B}{R_{sig}+R_A\parallel R_B}
=-3.333\frac{2400}{2450}\simeq-3.265.$$
Il libro trascura il partitore e ottiene −3.33. Per una sinusoide a 1 kHz di 0.2 V picco-picco l’ampiezza d’uscita è circa 0.3265 V di picco, oppure 0.333 V con l’approssimazione.

Senza bypass, trascurando $r_o$:
$$A_v=-\frac{g_m(R_D\parallel R_L)}{1+g_mR_S}\frac{2400}{2450}\simeq-1.633.$$
La polarizzazione è invariata; il guadagno di segnale diminuisce e la degenerazione resta attiva.

> [!warning] Correzione
> P. 140 scrive $V_{DS}=V_{DD}-I_D(R_D-R_S)$: il segno corretto è **$R_D+R_S$**, che fornisce i 5 V riportati. P. 141 chiama «continue» le componenti che cortocircuitano il bypass: sono quelle **variabili nella banda utile**.

_(dispensa, pp. 139–143)_

![[EL-p139-1.png]]

Il circuito completo distingue condensatori di accoppiamento e bypass della resistenza di source. _(dispensa, p. 139)_

![[EL-p139-2.png]]

La consegna usa una sinusoide di 0.2 V picco-picco e periodo di 1 ms. _(dispensa, p. 139)_

![[EL-p139-3.png]]

In continua i condensatori sono aperti e il partitore determina la tensione di gate. _(dispensa, p. 139)_

![[EL-p141-1.png]]

Con bypass efficace il source è a massa per il segnale, mentre gate e drain vedono i rispettivi paralleli resistivi. _(dispensa, p. 141)_

![[EL-p142-1.png]]

L’uscita mantiene la frequenza, inverte la polarità e ha ampiezza circa 0.33 V nell’approssimazione del libro. _(dispensa, p. 142)_

![[EL-p142-2.png]]

Senza bypass il source varia e riduce vgs: la degenerazione diminuisce il guadagno. _(dispensa, p. 142)_

## Capacità interne e banda

Per il ripasso: [[EL - Capacità interne MOS e banda]].

Il gate presenta capacità verso source e drain: $C_{gs}$ e $C_{gd}$. Contribuiscono sia le sovrapposizioni geometriche sia la carica di canale. In saturazione il canale è maggiormente associato al source; l’accoppiamento gate-drain resta comunque importante.

Il modello ad alta frequenza aggiunge queste capacità a $g_mv_{gs}$ e $r_o$. Aumentando la frequenza diventano necessari flussi di carica maggiori: sorgenti e resistenze finite non riescono a mantenere istantaneamente le tensioni, e il guadagno cambia.

Il comportamento passa-basso si spiega con le impedenze e i poli della rete, non con un contatto fisico improvviso tra terminali. I condensatori di accoppiamento e bypass introducono invece la dipendenza alle basse frequenze: le due famiglie di capacità fissano estremi diversi della banda.

_(dispensa, pp. 144–145)_

![[EL-p144-1.png]]

Il disegno ideale allinea esattamente il gate allo spazio fra le diffusioni. _(dispensa, p. 144)_

![[EL-p144-2.png]]

Il disallineamento lascerebbe una zona non controllata dal gate, motivando le tolleranze geometriche. _(dispensa, p. 144)_

![[EL-p144-3.png]]

La sovrapposizione del gate a source e drain introduce capacità di overlap. _(dispensa, p. 144)_

![[EL-p144-4.png]]

In saturazione la carica di canale contribuisce soprattutto alla capacità verso source. _(dispensa, p. 144)_

![[EL-p144-5.png]]

Il modello ad alta frequenza aggiunge Cgs e Cgd ai parametri incrementali. _(dispensa, p. 144)_

![[EL-p145-1.png]]

I condensatori di accoppiamento limitano il basso e quelli interni limitano l’alto della banda. _(dispensa, p. 145)_

## Esercizi a due stadi e generatore di polarizzazione

Nella cascata di pp. 146–147, i punti di riposo sono quelli calcolati nella lezione precedente: $Q_1$ con $(V_{GS},I_D,V_{DS})=(3\,\mathrm V,2\,\mathrm{mA},6\,\mathrm V)$; $Q_2$ con $(2\,\mathrm V,1\,\mathrm{mA},2\,\mathrm V)$. Entrambi hanno $g_m=2\,\mathrm{mS}$. Con bypass efficaci, $R_{D1}=1\,\mathrm{k\Omega}$ e $R_{D2}\parallel R_L=1\,\mathrm{k\Omega}$:
$$A_1=-2,\quad A_2=-2,\quad A_{tot}=+4.$$

Nell’esempio di pp. 148–150, $M_2$ è il generatore di corrente sotto il source di $M_1$, con alimentazioni ±5 V. Il partitore fissa $V_{G2}=-3$ V, quindi $V_{GS2}=2$ V e $I_D=0.25$ mA. Ne segue $V_{GS1}=2$ V, $V_{S1}=-2$ V. Poiché il carico è connesso anche in continua, la KCL al drain dà $V_{D1}=0$ V; quindi $V_{DS1}=2$ V e $V_{DS2}=3$ V: entrambi saturi. Il bypass rende il source di $M_1$ a massa per il segnale; $g_{m1}=0.5$ mS e $R_D\parallel R_L=10$ kΩ producono $A_v=-5$.

_(dispensa, pp. 146–150)_

![[EL-p146-1.png]]

La cascata a due MOS usa sorgenti di polarizzazione e bypass per separare continua e segnale. _(dispensa, p. 146)_

![[EL-p147-1.png]]

Il modello di piccolo segnale è la cascata di due stadi invertenti con carico sull’ultimo. _(dispensa, p. 147)_

![[EL-p148-1.png]]

Il secondo MOS sottostante polarizza il driver a corrente fissata; il carico d’uscita è presente anche in continua. _(dispensa, p. 148)_

![[EL-p149-1.png]]

Il bypass porta il source del driver a massa per il segnale. _(dispensa, p. 149)_

![[EL-p149-2.png]]

Il modello incrementale del driver mostra RD e RL in parallelo e un generatore gm per vin. _(dispensa, p. 149)_

## Operazionale e MOS in cascata

Nel convertitore corrente-corrente di pp. 151–152, la polarizzazione del MOS fornisce $V_{GS}=3$ V, $I_D=2$ mA, $V_{DS}=4$ V e $g_m=2$ mS. Il primo stadio è una transresistenza: $v_G=-i_{in}R_2$. Il secondo divide la corrente controllata tra $R_D$ e $R_L$:
$$A_i=\frac{i_{out}}{i_{in}}=g_mR_2\frac{R_D}{R_D+R_L}
=2\,\mathrm{mS}\cdot10\,\mathrm{k\Omega}\cdot\frac25=8.$$

Nell’esempio al gradino di pp. 153–154, il gate passa da 0 a 3 V. Il source vede $R_S\parallel R_1=2$ kΩ perché l’altro estremo di $R_1$ è una massa virtuale. Si trova $V_{GS}=2$ V, $I_D=0.5$ mA e $V_S=1$ V. Il drain è a $10-0.5\cdot6=7$ V, quindi $V_{DS}=6$ V e il MOS è saturo.

Il successivo integratore pratico ha $R_1=4$ kΩ, $R_2=8$ kΩ, $C=0.5$ µF. La risposta a partire da condensatore scarico è:
$$v_o(t)=-2[1-e^{-t/(4\,\mathrm{ms})}]\,\mathrm V.$$
Il valore finale è −2 V; l’assestamento a $5\tau$ richiede circa 20 ms. La transizione non è un piccolo segnale attorno al punto spento: si usano le leggi non lineari per determinare il nuovo stato del MOS e poi si studia il filtro.

_(dispensa, pp. 151–154)_

![[EL-p151-1.png]]

Lo stadio operazionale converte una corrente d’ingresso in una tensione che pilota il gate. _(dispensa, p. 151)_

![[EL-p152-1.png]]

Il MOS vede il segnale di gate e divide la corrente fra RD e RL. _(dispensa, p. 152)_

![[EL-p152-2.png]]

La sostituzione incrementale permette di moltiplicare la transresistenza del primo stadio per la conversione corrente del secondo. _(dispensa, p. 152)_

![[EL-p153-1.png]]

Il gradino sul gate produce un nuovo livello sul source, che alimenta l’integratore pratico successivo. _(dispensa, p. 153)_

![[EL-p154-1.png]]

L’uscita dell’integratore pratico tende esponenzialmente a −2 V con costante di tempo di 4 ms. _(dispensa, p. 154)_

## Carichi attivi NMOS

Per il ripasso: [[EL - Carico attivo MOS]].

Una resistenza di drain molto alta aumenta il guadagno, ma occupa area e comporta una grande caduta continua. Un **carico attivo** offre una resistenza incrementale elevata senza richiedere un resistore fisico altrettanto grande.

Con una sorgente ideale di corrente sopra il drain, il carico di segnale è aperto; il guadagno è limitato da $r_o$. Se anche $r_o$ fosse infinito, il modello diventerebbe degenere e non determinerebbe un guadagno lineare finito né un punto d’uscita univoco: il «guadagno infinito» è un limite ideale.

Un NMOS a svuotamento può funzionare da carico con gate e source cortocircuitati, quindi $V_{GS2}=0$ e corrente fissata dalla sua caratteristica. Trascurando l’effetto body:
$$A_v=-g_{m1}(r_{o1}\parallel r_{o2}).$$
La transcaratteristica si ricava intersecando la caratteristica del driver con quella del carico riportata rispetto a $V_{DD}$. Il tratto più ripido corrisponde a entrambi i transistor saturi.

_(dispensa, pp. 155–158)_

![[EL-p155-1.png]]

Il resistore di drain determina il guadagno ma comporta una caduta continua e occupazione d’area. _(dispensa, p. 155)_

![[EL-p155-2.png]]

Il confronto geometrico mostra che una resistenza integrata può occupare molto più spazio del transistor. _(dispensa, p. 155)_

![[EL-p155-3.png]]

Un generatore di corrente sopra il drain realizza un carico attivo con elevata resistenza incrementale. _(dispensa, p. 155)_

![[EL-p155-4.png]]

La resistenza intrinseca ro limita il guadagno quando il carico ideale è aperto per il segnale. _(dispensa, p. 155)_

![[EL-p156-1.png]]

La caratteristica del MOS a svuotamento evidenzia corrente presente anche a VGS nulla. _(dispensa, p. 156)_

![[EL-p156-2.png]]

Il transistor superiore a svuotamento può essere usato come dispositivo di carico. _(dispensa, p. 156)_

![[EL-p157-1.png]]

Collegando gate e source del carico si fissa VGS2 a zero. _(dispensa, p. 157)_

![[EL-p157-2.png]]

La curva di carico riportata dal rail alto si interseca con le caratteristiche del driver. _(dispensa, p. 157)_

![[EL-p157-3.png]]

Le regioni della transcaratteristica dipendono dalla combinazione delle regioni dei due MOS. _(dispensa, p. 157)_

![[EL-p157-4.png]]

Nel caso ideale due tratti di corrente costante possono coincidere e dare un tratto verticale della transcaratteristica. _(dispensa, p. 157)_

![[EL-p158-1.png]]

Con modulazione di canale la coincidenza ideale diventa una regione ripida ma con pendenza finita. _(dispensa, p. 158)_

![[EL-p158-2.png]]

I modelli incrementali mostrano che il generatore gm del carico è nullo se vgs2 è nullo. _(dispensa, p. 158)_

![[EL-p158-3.png]]

Le resistenze d’uscita dei due dispositivi sono in parallelo al generatore di segnale del driver. _(dispensa, p. 158)_

## Effetto body

Per il ripasso: [[EL - Effetto body]].

Se source e body non hanno lo stesso potenziale, cambia la condizione elettrostatica del canale e quindi la corrente. Nel modello incrementale:
$$i_d=g_mv_{gs}+g_{mb}v_{bs}+\frac{v_{ds}}{r_o}.$$
Il rapporto $g_{mb}/g_m$ è dipendente dal dispositivo e dal punto di lavoro; il valore circa 0.2 usato nel libro è indicativo.

Nel carico NMOS con gate-source collegati, il termine $g_mv_{gs}$ è nullo, ma quello di body può non esserlo perché il body resta al riferimento comune mentre il source segue l’uscita. Per questo specifico circuito il contributo equivale a una conduttanza d’uscita aggiuntiva:
$$A_v=-g_{m1}\left(r_{o1}\parallel r_{o2}\parallel\frac1{g_{mb2}}\right).$$
Se domina $1/g_{mb2}$, il guadagno tende a $-g_{m1}/g_{mb2}$. Il rapporto delle geometrie influenza il risultato e può riproporre il problema dell’area occupata.

_(dispensa, pp. 159–160)_

![[EL-p159-1.png]]

Il modello a quattro terminali introduce il generatore gmb controllato dalla tensione body-source. _(dispensa, p. 159)_

![[EL-p159-2.png]]

Una sorgente di corrente controllata dalla propria tensione ai morsetti equivale a una conduttanza, con polarità passive coerenti. _(dispensa, p. 159)_

![[EL-p159-3.png]]

Nel carico superiore il body è fisso mentre il source segue l’uscita: compare una corrente incrementale aggiuntiva. _(dispensa, p. 159)_

![[EL-p160-1.png]]

Il contributo di body equivale in questo circuito a una resistenza 1/gmb in parallelo al carico d’uscita. _(dispensa, p. 160)_

## Carichi PMOS e collegamento alla logica CMOS

Per il ripasso: [[EL - Amplificatore CMOS con carico attivo]].

Un PMOS di carico può avere source e body entrambi al potenziale alto; l’NMOS driver può avere source e body al potenziale basso. In questa configurazione i contributi incrementali di body sono evitabili. Uno specchio PMOS imposta la corrente di carico tramite un ramo di riferimento.

Con polarizzazione fissa del gate del carico, il circuito è un amplificatore a source comune con carico attivo:
$$A_v\simeq-g_{mn}(r_{on}\parallel r_{op}).$$
La resistenza finita delle caratteristiche rende il tratto centrale molto ripido ma non verticale. L’escursione deve mantenere entrambi i dispositivi nella regione richiesta: per esempio, con source dell’NMOS a massa, $v_o\gtrsim V_{OVn}$ e $v_o\lesssim V_{DD}-V_{OVp}$ per tenere entrambi saturi.

> [!important] Carico polarizzato e inverter CMOS
> Nel carico attivo il gate del PMOS è fissato dal ramo di polarizzazione. Nell’**inverter CMOS statico** della lezione successiva, i gate di NMOS e PMOS ricevono entrambi l’ingresso. Questa differenza è essenziale per la corrente statica: non si può attribuire al carico polarizzato il consumo idealmente nullo dell’inverter complementare.

> [!warning] Correzione
> A p. 161 si descrive il transistor a diodo come avente drain e source cortocircuitati; il collegamento necessario è tra **gate e drain**. La stessa pagina usa poi correttamente $V_{GS}=V_{DS}$.

_(dispensa, pp. 161–164)_

![[EL-p161-1.png]]

Lo specchio NMOS impone la stessa VGS ai due dispositivi e scala la corrente tramite le geometrie. _(dispensa, p. 161)_

![[EL-p161-2.png]]

Lo specchio PMOS porta la corrente di riferimento al carico del driver NMOS. _(dispensa, p. 161)_

![[EL-p162-1.png]]

Il PMOS di carico ha tensione di gate fissata e una sola caratteristica di corrente nel modello statico. _(dispensa, p. 162)_

![[EL-p162-2.png]]

La corrente del driver e quella del carico devono essere uguali al punto d’intersezione. _(dispensa, p. 162)_

![[EL-p162-3.png]]

Nel modello ideale l’uguaglianza delle correnti di saturazione genera il tratto verticale. _(dispensa, p. 162)_

![[EL-p163-1.png]]

La transcaratteristica ideale distingue le regioni del driver e del carico attivo. _(dispensa, p. 163)_

![[EL-p163-2.png]]

Resistenze d’uscita finite rendono la transizione centrale meno ripida. _(dispensa, p. 163)_

![[EL-p163-3.png]]

Il pozzo del PMOS e il substrato dell’NMOS permettono di porre ciascun body al proprio source in questa configurazione. _(dispensa, p. 163)_

