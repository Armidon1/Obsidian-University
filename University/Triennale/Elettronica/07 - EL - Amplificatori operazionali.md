---
title: "Amplificatori operazionali"
aliases:
  - "EL — Amplificatori operazionali"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Amplificatori operazionali

> [!abstract]
> Dal modello ideale alle configurazioni resistive e dinamiche: le regole del cortocircuito virtuale si applicano solo dopo aver stabilito le condizioni di funzionamento.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 52–84.

Precedente: [[06 - EL - Retroazione]] · Successiva: [[08 - EL - Multivibratori e generatori di forme d’onda]]

## Modello ideale e cortocircuito virtuale

Per il ripasso: [[EL - Operazionale ideale]] · [[EL - Cortocircuito virtuale]].

L’amplificatore operazionale (AO, in inglese **op-amp**) ha due ingressi e un’uscita:
$$v_o=A(v_+-v_-).$$
Nel modello ideale $R_i\to\infty$, $R_o=0$, $A\to\infty$. Le correnti d’ingresso sono nulle; la corrente d’uscita può invece essere diversa da zero ed è fornita o assorbita tramite le alimentazioni.

Con retroazione negativa stabile e uscita non satura si può porre $v_+\simeq v_-$. Questa uguaglianza è il **cortocircuito virtuale**: non esiste un collegamento conduttivo tra gli ingressi. Si parla di massa virtuale soltanto quando uno degli ingressi è effettivamente a massa.

Senza anello lineare, l’operazionale può operare da comparatore: $v_o=L^+$ per $v_+>v_-$, $v_o=L^-$ per $v_+<v_-$. In saturazione le correnti d’ingresso restano nulle nel modello, ma non vale l’uguaglianza delle tensioni.

> [!warning] Correzione
> P. 53 associa l’uguaglianza dei potenziali a un cortocircuito fisico e quindi a corrente infinita. Due nodi allo stesso potenziale non sono necessariamente collegati; nemmeno un filo ideale impone una corrente infinita. Il cortocircuito virtuale è una conseguenza della retroazione e del grande guadagno, non un percorso attraversabile dalla corrente.

_(dispensa, pp. 52–54)_

![[EL-p052-1.png]]

Il morsetto + è non invertente, il morsetto − invertente; l’uscita è riferita a massa. _(dispensa, p. 52)_

![[EL-p052-2.png]]

Il modello ideale deriva da ingresso ad alta resistenza, uscita a bassa resistenza e grande guadagno differenziale. _(dispensa, p. 52)_

![[EL-p053-1.png]]

Nel limite di guadagno infinito la zona lineare differenziale tende a larghezza nulla. _(dispensa, p. 53)_

![[EL-p054-1.png]]

Il ritorno al morsetto − realizza normalmente retroazione negativa; al + realizza positiva negli schemi mostrati. _(dispensa, p. 54)_

![[EL-p054-2.png]]

Il confronto ripetuto nel PDF richiama i due segni della retroazione prima delle configurazioni fondamentali. _(dispensa, p. 54)_

## Configurazione invertente

Per il ripasso: [[EL - Operazionale invertente]] · [[EL - Transresistenza con operazionale]].

Con $R_1$ dall’ingresso al morsetto −, $R_f$ tra uscita e morsetto − e morsetto + a massa, la KCL sul nodo virtuale dà:
$$\frac{v_i}{R_1}+\frac{v_o}{R_f}=0\quad\Rightarrow\quad v_o=-\frac{R_f}{R_1}v_i.$$
L’intera configurazione ha $R_{in}=R_1$ e $R_{out}=0$ nel modello ideale. La resistenza $R_1$ può essere un componente scelto dal progettista, non necessariamente la resistenza interna della sorgente.

La corrente che entra da $R_1$ prosegue in $R_f$; non entra nel morsetto −. Il percorso si chiude attraverso l’uscita e le alimentazioni dell’AO. L’uscita non è semplicemente un filo verso massa: è un generatore controllato.

Se il carico si trova nel ramo di retroazione, la corrente imposta è $i_L=v_i/R_1$, indipendente dal carico finché l’AO può produrre la tensione necessaria. Questo è un generatore di corrente a carico flottante, soggetto a una tensione massima disponibile, detta **compliance**.

Per una sorgente di corrente collegata direttamente al nodo di massa virtuale, $v_o=-R_fi_i$: la configurazione è una transresistenza. Il nodo d’ingresso ha tensione idealmente nulla ma può assorbire corrente dalla rete esterna.

_(dispensa, pp. 55–58)_

![[EL-p055-1.png]]

Senza rete di ritorno, un ingresso sul morsetto − porta la risposta con segno invertente. _(dispensa, p. 55)_

![[EL-p055-2.png]]

Un ingresso sul + porta la risposta con segno non invertente. _(dispensa, p. 55)_

![[EL-p055-3.png]]

Il circuito di ritorno con R1 e R2 permette di mantenere il morsetto − vicino al potenziale del +. _(dispensa, p. 55)_

![[EL-p055-4.png]]

La configurazione invertente è delimitata come blocco a due porte: R1 appartiene alla sua impedenza d’ingresso. _(dispensa, p. 55)_

![[EL-p055-5.png]]

La corrente da R1 attraversa R2 mentre il nodo − resta a zero virtuale. _(dispensa, p. 55)_

![[EL-p056-1.png]]

La caratteristica della configurazione ha pendenza −R2/R1 finché l’uscita non raggiunge i limiti. _(dispensa, p. 56)_

![[EL-p057-1.png]]

La sorgente di prova all’ingresso mostra che la resistenza vista dall’esterno è R1. _(dispensa, p. 57)_

![[EL-p057-2.png]]

La prova d’uscita illustra il modello ideale a resistenza d’uscita nulla, da usare mantenendo coerente l’anello. _(dispensa, p. 57)_

![[EL-p057-3.png]]

La rete equivalente riassume ingresso resistivo e generatore d’uscita comandato con guadagno negativo. _(dispensa, p. 57)_

![[EL-p058-1.png]]

Il ramo di retroazione porta la stessa corrente fissata da Vin e R1 anche se varia il valore del carico R2. _(dispensa, p. 58)_

![[EL-p058-2.png]]

Mettendo il carico nel ramo di ritorno si ottiene una corrente imposta entro i limiti di tensione dell’AO. _(dispensa, p. 58)_

## Configurazione non invertente e buffer

Per il ripasso: [[EL - Operazionale non invertente]] · [[EL - Buffer di tensione]].

Il segnale è applicato al morsetto +. Il morsetto − riceve il partitore tra $R_f$ verso l’uscita e $R_g$ verso massa:
$$v_-=v_o\frac{R_g}{R_g+R_f}=v_i\quad\Rightarrow\quad v_o=\left(1+\frac{R_f}{R_g}\right)v_i.$$
La resistenza d’ingresso ideale è infinita; quella d’uscita è nulla. Il guadagno è almeno unitario per resistenze positive.

Il **buffer** o inseguitore si ottiene riportando direttamente l’uscita al morsetto −: $v_o=v_i$. Serve a trasferire una tensione da una sorgente ad alta impedenza a un carico più pesante. L’energia per pilotare il carico proviene dall’alimentazione del buffer.

Un resistore in serie a un ingresso ideale senza corrente non produce caduta di tensione; questo non significa che il resistore sia fisicamente un cortocircuito. Nel modello reale correnti di bias e capacità possono renderlo rilevante.

_(dispensa, pp. 59–61)_

![[EL-p059-1.png]]

Nel non invertente il segnale va direttamente al morsetto + e il partitore al morsetto −. _(dispensa, p. 59)_

![[EL-p059-2.png]]

Le due resistenze di ritorno sono attraversate dalla stessa corrente: il partitore determina il guadagno positivo. _(dispensa, p. 59)_

![[EL-p060-1.png]]

Il modello equivalente del non invertente ha ingresso aperto e generatore ideale d’uscita. _(dispensa, p. 60)_

![[EL-p061-1.png]]

Le tre varianti mostrate portano a guadagno unitario nel modello ideale. _(dispensa, p. 61)_

![[EL-p061-2.png]]

Il buffer separa la resistenza della sorgente dal carico e trasferisce la tensione senza attenuazione ideale. _(dispensa, p. 61)_

## Esercizi resistivi e verifica della saturazione

Nell’esercizio a due operazionali di p. 62, con $v_i=2\,\mathrm V$, il ramo non invertente fornisce $v_{o1}=3\,\mathrm V$ e quello invertente $v_{o2}=-6\,\mathrm V$. Il carico da $6\,\mathrm{k\Omega}$ è collegato tra le due uscite:
$$i_L=\frac{v_{o1}-v_{o2}}{R_L}=\frac{3-(-6)}6\,\mathrm{mA}=1.5\,\mathrm{mA}.$$
La corrente dipende dalla differenza tra le due uscite, non dalla sola tensione di una di esse.

A p. 63 il circuito cerca di imporre $i_L=4\,\mathrm{mA}$ e $V_X=6\,\mathrm V$, con limiti $\pm12\,\mathrm V$. Per $R_L=1\,\mathrm{k\Omega}$ serve $v_o=10\,\mathrm V$, compatibile. Per $R_L=2\,\mathrm{k\Omega}$ servirebbero 14 V: l’uscita si blocca a 12 V e si deve rifare l’analisi senza massa virtuale.

Nel secondo caso:
$$\frac{12-V_X}{2\,\mathrm{k\Omega}}=1\,\mathrm{mA}+\frac{V_X}{2\,\mathrm{k\Omega}},$$
da cui $V_X=5\,\mathrm V$, $i_L=3.5\,\mathrm{mA}$ e $v_- =V_X-iR_1=-1\,\mathrm V$. Con $v_+=0$ il segno differenziale è positivo e conferma la saturazione alta.

> [!warning] Correzione
> Nell’ultima KCL di p. 63 compare $V_X/R_L$ per la corrente della resistenza a massa: deve essere $V_X/R_2$. Qui $R_2=R_L=2\,\mathrm{k\Omega}$ nel caso saturo, quindi il refuso non cambia il numero finale.

_(dispensa, pp. 62–63)_

![[EL-p062-1.png]]

La consegna collega un non invertente e un invertente ai due lati del carico: la corrente dipende dalla differenza delle uscite. _(dispensa, p. 62)_

![[EL-p062-2.png]]

La stessa consegna è ripetuta nel PDF e conserva i valori delle resistenze utili al calcolo. _(dispensa, p. 62)_

![[EL-p063-1.png]]

Il carico nel circuito di corrente può richiedere una tensione oltre il limite dell’AO: occorre verificare entrambe le ipotesi. _(dispensa, p. 63)_

![[EL-p063-2.png]]

In saturazione alta l’uscita è fissata a 12 V e il nodo X si ricava dalla rete resistiva senza massa virtuale. _(dispensa, p. 63)_

## Operazionale seguito da filtri RC

Il circuito somma un riferimento $V_A=2\,\mathrm V$ e il contributo della corrente su $R_1=3\,\mathrm{k\Omega}$. Con il verso indicato nel libro:
$$V_X=V_A-iR_1.$$
La corrente passa da 0 a 2 mA a $t_0=1\,\mathrm{ms}$, perciò $V_X$ passa da 2 V a −4 V. La variazione è $\Delta V_X=-6\,\mathrm V$.

Con $R_2=5\,\mathrm{k\Omega}$ e $C=0.1\,\mu\mathrm F$, $\tau=R_2C=0.5\,\mathrm{ms}$. Il ramo passa-basso, inizialmente a regime, produce:
$$v_{o1}(t)=-4+6e^{-(t-t_0)/\tau}\quad(t\ge t_0).$$
Il ramo passa-alto ha uscita iniziale nulla e risponde alla variazione:
$$v_{o2}(t)=-6e^{-(t-t_0)/\tau}\quad(t\ge t_0).$$
L’uscita del passa-alto può saltare, perché il salto non è ai capi del condensatore: la tensione **sul condensatore** rimane continua. L’AO resta entro ±12 V e l’ipotesi lineare è coerente.

_(dispensa, pp. 64–67)_

![[EL-p064-1.png]]

Il commutatore collega l’uscita dell’AO a un filtro passa-alto oppure a un passa-basso. _(dispensa, p. 64)_

![[EL-p064-2.png]]

Il riferimento sul + e la corrente sul − contribuiscono entrambi alla tensione al nodo X. _(dispensa, p. 64)_

![[EL-p065-1.png]]

Annullata la corrente, il ramo d’ingresso è aperto e il circuito segue il riferimento di tensione. _(dispensa, p. 65)_

![[EL-p065-2.png]]

Il generatore di corrente passa da zero a 2 mA a 1 ms. _(dispensa, p. 65)_

![[EL-p065-3.png]]

Con il riferimento annullato, la corrente produce un contributo d’uscita di −6 V. _(dispensa, p. 65)_

![[EL-p066-1.png]]

La sovrapposizione somma 2 V costanti e il gradino negativo: il nodo X passa da 2 a −4 V. _(dispensa, p. 66)_

![[EL-p066-2.png]]

Il passa-basso compie una transizione continua da 2 a −4 V con costante di tempo 0.5 ms. _(dispensa, p. 66)_

![[EL-p067-1.png]]

Il passa-alto restituisce il salto di −6 V e poi torna esponenzialmente a zero. _(dispensa, p. 67)_

## Sommatore pesato e progetto dei coefficienti

Per il ripasso: [[EL - Sommatore pesato]].

Con più resistenze d’ingresso sullo stesso nodo virtuale, la KCL dà:
$$v_o=-R_f\sum_k\frac{v_k}{R_k}.$$
Ogni resistenza determina un peso. Gli ingressi sono indipendenti nel modello ideale grazie al nodo a potenziale fissato.

Per ottenere $v_o=-2v_1-4v_2+3v_3$, l’esempio usa $R_f=12\,\mathrm{k\Omega}$: dai primi due coefficienti si ricavano $R_1=6\,\mathrm{k\Omega}$ e $R_2=3\,\mathrm{k\Omega}$. Il terzo segnale entra nel morsetto + tramite un partitore con $R_4=3\,\mathrm{k\Omega}$ verso massa e $R_3$ verso la sorgente. Spegnendo $v_1$ e $v_2$, $R_1\parallel R_2=2\,\mathrm{k\Omega}$ e il guadagno non invertente è 7. Si impone:
$$7\frac{3}{R_3/\mathrm{k\Omega}+3}=3\quad\Rightarrow\quad R_3=4\,\mathrm{k\Omega}.$$
Infine si verifica che la somma delle uscite richieste sia compatibile con la dinamica.

_(dispensa, pp. 68–70)_

![[EL-p068-1.png]]

Le correnti degli ingressi si sommano nel nodo virtuale e proseguono nella resistenza di feedback. _(dispensa, p. 68)_

![[EL-p069-1.png]]

La consegna richiede pesi diversi per i due ingressi invertenti e per quello non invertente. _(dispensa, p. 69)_

![[EL-p069-2.png]]

Considerando un solo ingresso invertente, la configurazione si riduce al rapporto −Rf/R1. _(dispensa, p. 69)_

## Integratore di Miller

Per il ripasso: [[EL - Integratore di Miller]].

Sostituendo i resistori dell’invertente con impedenze, in condizioni di zero stato iniziale $H(s)=-Z_f(s)/Z_{in}(s)$. Per $Z_{in}=R$, $Z_f=1/(sC)$:
$$H(s)=-\frac1{sRC},\qquad v_o(t)=v_o(t_0)-\frac1{RC}\int_{t_0}^{t}v_i(\xi)d\xi.$$
Un ingresso costante genera una rampa. Il polo nell’origine comporta guadagno crescente senza limite verso la continua: anche offset piccoli possono portare l’uscita al limite.

L’integratore pratico pone $R_f$ in parallelo a C:
$$H(s)=-\frac{R_f/R}{1+sR_fC}.$$
Alle basse frequenze il guadagno è finito, $-R_f/R$; per $\omega R_fC\gg1$ il circuito approssima l’integratore ideale.

> [!warning] Correzione
> L’integratore ideale non è un normale passa-basso con un plateau finito in continua: $|H|=1/(\omega RC)$ a tutte le frequenze del modello. Le argomentazioni di pp. 71–72 che spengono automaticamente il generatore controllato dell’AO non sono un metodo generale per ricavare le impedenze. Si parte dalla KCL e si mantengono i generatori dipendenti.

_(dispensa, pp. 71–73)_

![[EL-p071-1.png]]

Con impedenze generiche il guadagno dell’invertente diventa −Z2/Z1, con condizioni iniziali nulle. _(dispensa, p. 71)_

![[EL-p071-2.png]]

Ponendo C nel ramo di feedback si integra la corrente fissata dal resistore d’ingresso. _(dispensa, p. 71)_

![[EL-p072-1.png]]

La sorgente di prova evidenzia la natura attiva dell’anello: il calcolo deve conservare il generatore controllato. _(dispensa, p. 72)_

![[EL-p072-2.png]]

L’integratore ideale ha modulo proporzionale a 1/omega e pendenza costante −20 dB per decade. _(dispensa, p. 72)_

![[EL-p073-1.png]]

La resistenza parallela a C introduce una retroazione anche in continua e limita il guadagno statico. _(dispensa, p. 73)_

![[EL-p073-2.png]]

Il Bode dell’integratore pratico ha un plateau alle basse frequenze e poi pendenza −20 dB per decade. _(dispensa, p. 73)_

## Derivatore e limiti del modello ideale

Per il ripasso: [[EL - Derivatore con operazionale]].

Con C in ingresso e $R_f$ in retroazione:
$$H(s)=-sR_fC,\qquad v_o=-R_fC\frac{dv_i}{dt}.$$
Il guadagno cresce con la frequenza: rumore ad alta frequenza e fronti molto rapidi possono produrre uscite elevate. Il derivatore ideale non ha un plateau ad alta frequenza.

Inserendo $R_s$ in serie al condensatore:
$$H(s)=-\frac{sR_fC}{1+sR_sC}.$$
Per $\omega R_sC\ll1$ deriva il segnale; per $\omega R_sC\gg1$ il guadagno tende a $-R_f/R_s$. Il circuito pratico evita la crescita illimitata nel modello, ma la banda e la stabilità dell’operazionale rimangono vincoli ulteriori.

_(dispensa, pp. 74–75)_

![[EL-p074-1.png]]

Con C in ingresso e R in feedback la corrente è proporzionale alla derivata della tensione d’ingresso. _(dispensa, p. 74)_

![[EL-p074-2.png]]

La prova illustrata riguarda il derivatore ideale; la relazione affidabile si ricava direttamente dalla KCL. _(dispensa, p. 74)_

![[EL-p074-3.png]]

Il derivatore ideale ha guadagno crescente senza limite, con pendenza +20 dB per decade. _(dispensa, p. 74)_

![[EL-p075-1.png]]

La resistenza in serie a C limita la corrente e il guadagno alle alte frequenze. _(dispensa, p. 75)_

![[EL-p075-2.png]]

Il derivatore pratico conserva la crescita iniziale, poi raggiunge un plateau di modulo R/R1. _(dispensa, p. 75)_

## Esercizio con integratore e corrente ripartita

Nel disegno la corrente d’ingresso è **$I_s=3\,\mu\mathrm A$**, con $R_1=2\,\mathrm{k\Omega}$, $R_2=4\,\mathrm{k\Omega}$, $R_3=4\,\mathrm{M\Omega}$ e $C=1\,\mu\mathrm F$. I due nodi invertenti sono a massa virtuale; la corrente si ripartisce in $I_1=2\,\mu\mathrm A$ e $I_2=1\,\mu\mathrm A$.

Si ottiene $v_B=-I_2R_3=-4\,\mathrm V$ e, con condensatore inizialmente scarico:
$$v_A(t)=-\frac{I_1}{C}t=-(2\,\mathrm{V/s})t.$$
Per $0\le t\le5\,\mathrm s$:
$$v_A-v_B=4\,\mathrm V-(2\,\mathrm{V/s})t.$$
A 5 s vale −6 V. Il primo AO raggiunge −12 V soltanto a **6 s**.

> [!warning] Correzione
> P. 76 alterna mA e µA nel testo e nell’integrale: il grafico della consegna indica 3 µA e solo questa unità rende corretti −4 V e −2 V/s. P. 77 afferma che la saturazione comincia oltre 5 s, ma il calcolo riportato la colloca correttamente a 6 s.

_(dispensa, pp. 76–77)_

![[EL-p076-1.png]]

La consegna indica una corrente di 3 microampere, indispensabile per la coerenza delle tensioni e dei tempi. _(dispensa, p. 76)_

![[EL-p076-2.png]]

Il ramo resistivo produce un gradino d’uscita di −4 V. _(dispensa, p. 76)_

![[EL-p076-3.png]]

Il ramo con C in feedback produce una rampa discendente a −2 V al secondo. _(dispensa, p. 76)_

![[EL-p077-1.png]]

La differenza VA−VB parte da 4 V e arriva a −6 V dopo 5 s, prima del clipping a 6 s. _(dispensa, p. 77)_

## Amplificatore differenziale e strumentazione

Per il ripasso: [[EL - Amplificatore differenziale e CMRR]] · [[EL - Amplificatore per strumentazione]].

Si definiscono $v_d=v_2-v_1$ e $v_{cm}=(v_1+v_2)/2$. Un amplificatore differenziale reale produce:
$$v_o=A_dv_d+A_{cm}v_{cm},\qquad \mathrm{CMRR}=\left|\frac{A_d}{A_{cm}}\right|.$$
In dB, $\mathrm{CMRR}_{dB}=20\log_{10}|A_d/A_{cm}|$. L’ideale ha $A_{cm}=0$. La reiezione del modo comune permette di estrarre una piccola differenza sovrapposta a un fondo grande.

Nel differenziale a quattro resistenze:
$$v_o=-\frac{R_2}{R_1}v_1+\left(1+\frac{R_2}{R_1}\right)\frac{R_4}{R_3+R_4}v_2.$$
Se $R_2/R_1=R_4/R_3$, diventa $v_o=(R_2/R_1)(v_2-v_1)$. Occorre l’uguaglianza dei **rapporti**, non necessariamente dei singoli valori. Per $R_1=R_3$ l’ingresso differenziale flottante vede $2R_1$: questo valore si ricava con KCL, senza postulare un flusso di corrente tra i morsetti dell’AO.

Due buffer aumentano l’impedenza vista dalle sorgenti. Nell’amplificatore per strumentazione a tre AO, i primi due stadi non invertenti condividono una resistenza $R_G$ tra i nodi invertenti. Con resistenze di retroazione uguali $R$, il guadagno differenziale del primo stadio è $1+2R/R_G$. Un successivo differenziale di rapporto $k$ dà $v_o=k(1+2R/R_G)(v_2-v_1)$, con segno determinato dall’ordine degli ingressi.

> [!warning] Correzione
> A p. 79 il partitore riporta $R_3+R_3$: il denominatore corretto è $R_3+R_4$. A p. 81 i primi due stadi vengono detti «invertenti», ma i segnali entrano nei morsetti +: sono stadi non invertenti accoppiati.

_(dispensa, pp. 78–81)_

![[EL-p078-1.png]]

I due ingressi del differenziale agiscono su reti invertente e non invertente. _(dispensa, p. 78)_

![[EL-p078-2.png]]

Annullando il secondo ingresso si isola il contributo invertente del primo. _(dispensa, p. 78)_

![[EL-p079-1.png]]

Annullando il primo ingresso si ottiene il contributo non invertente del secondo tramite il partitore. _(dispensa, p. 79)_

![[EL-p080-1.png]]

La prova differenziale coinvolge i due resistori d’ingresso: la resistenza vista dalla sorgente flottante è 2R1 nel caso simmetrico. _(dispensa, p. 80)_

![[EL-p080-2.png]]

Due buffer eliminano idealmente il carico resistivo visto dalle sorgenti del differenziale. _(dispensa, p. 80)_

![[EL-p081-1.png]]

I primi due AO e la resistenza fra i nodi invertenti permettono di regolare il guadagno con un solo componente. _(dispensa, p. 81)_

## Esercizio con riferimento e filtro di ingresso

Il riferimento di 2 V produce a regime un’uscita di 6 V, poiché il guadagno non invertente a continua è $1+12/(2+4)=3$. Per il contributo del segnale si annulla il riferimento e il nodo invertente diventa massa virtuale.

Il condensatore all’ingresso vede $R_1\parallel R_2=(2\parallel4)\,\mathrm{k\Omega}=1.333\,\mathrm{k\Omega}$. Con $C=10\,\mathrm{nF}$:
$$\tau=13.333\,\mu\mathrm s.$$
L’ingresso rettangolare sale da 0 a 6 V a 1 ms e torna a zero a 5 ms. Il contributo d’uscita ha guadagno statico $-R_3/(R_1+R_2)=-2$; dopo il primo fronte:
$$v_o(t)=6-12[1-e^{-(t-1\,\mathrm{ms})/\tau}]\quad\mathrm V.$$
Prima del secondo fronte il valore è praticamente −6 V. Dopo il ritorno dell’ingresso a zero risale verso 6 V con la stessa $\tau$. Il segnale totale resta nei limiti ±20 V indicati nella consegna.

> [!warning] Correzione
> P. 83 arrotonda $\tau$ a 13 µs e poi scrive $5\tau=60$ µs. Con i dati, $5\tau\simeq66.7$ µs. Si verifica la dinamica della **somma** dei contributi, perché la linearità fisica deve valere per l’uscita totale.

_(dispensa, pp. 82–84)_

![[EL-p082-1.png]]

La consegna combina un riferimento di 2 V con un impulso di 6 V, applicato attraverso una rete RC. _(dispensa, p. 82)_

![[EL-p082-2.png]]

Per il contributo continuo del riferimento il condensatore è aperto e il guadagno non invertente è tre. _(dispensa, p. 82)_

![[EL-p082-3.png]]

Per il contributo del segnale il nodo X è l’uscita di un passa-basso caricato dalla resistenza verso la massa virtuale. _(dispensa, p. 82)_

![[EL-p083-1.png]]

La tensione sul condensatore segue il rettangolo filtrato; il guadagno successivo è invertente e pari a −3. _(dispensa, p. 83)_

![[EL-p084-1.png]]

La somma del riferimento e del contributo filtrato porta l’uscita da 6 a −6 V e poi nuovamente a 6 V. _(dispensa, p. 84)_

