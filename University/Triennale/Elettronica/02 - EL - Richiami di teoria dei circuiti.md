---
title: "Richiami di teoria dei circuiti"
aliases:
  - "EL — Richiami di teoria dei circuiti"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Richiami di teoria dei circuiti

> [!abstract]
> Gli strumenti per risolvere reti resistive e transitori: leggi di Kirchhoff, equivalenti, generatori controllati ed elementi reattivi.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 8–23.

Precedente: [[01 - EL - Introduzione e segnali]] · Successiva: [[03 - EL - Reti a due porte]]

## Bipoli, leggi di Kirchhoff e collegamenti

Per il ripasso: [[EL - Leggi di Kirchhoff]] · [[EL - Generatori ideali e reali]].

Un bipolo ha due morsetti, una tensione e una corrente di riferimento. Per un resistore ideale, adottando la convenzione passiva, $v=Ri$: la corrente entra nel morsetto indicato positivo. La potenza assorbita è $p=vi=Ri^2\ge0$.

Un generatore ideale di tensione impone $v$ e lascia che il circuito determini $i$; uno di corrente impone $i$ e lascia che il circuito determini $v$. Il generatore reale di tensione si modella con una resistenza in serie, quello reale di corrente con una resistenza in parallelo.

Le due leggi di Kirchhoff sono conservazioni:
$$\sum_k i_k=0\quad\text{a ogni nodo},\qquad \sum_k v_k=0\quad\text{lungo una maglia}.$$
Prima di scrivere le equazioni si scelgono versi e polarità. Un risultato negativo indica che il verso effettivo è opposto a quello scelto.

| Connessione | Condizione | Equivalente |
|---|---|---|
| Serie | Stessa corrente; nessuna derivazione al nodo comune | $R_{eq}=\sum R_k$ |
| Parallelo | Stessi due nodi, quindi stessa tensione | $1/R_{eq}=\sum 1/R_k$ |

Per due resistenze: $R_1\parallel R_2=R_1R_2/(R_1+R_2)$. La vicinanza nel disegno non basta a stabilire serie e parallelo: bisogna controllare i nodi.

_(dispensa, pp. 8–9)_

![[EL-p008-1.png]]

La polarità sul resistore è scelta positiva dal lato in cui entra la corrente. _(dispensa, p. 8)_

![[EL-p008-2.png]]

La somma delle cadute resistive e delle sorgenti determina la tensione tra gli estremi della catena. _(dispensa, p. 8)_

![[EL-p009-1.png]]

Le frecce separano correnti entranti e uscenti: la loro somma algebrica al nodo è nulla. _(dispensa, p. 9)_

![[EL-p009-2.png]]

Il percorso chiuso e le polarità fissano i segni dei termini nell’equazione di maglia. _(dispensa, p. 9)_

![[EL-p009-3.png]]

Due resistori in serie sono attraversati dalla stessa corrente. _(dispensa, p. 9)_

![[EL-p009-4.png]]

Due resistori in parallelo condividono entrambi i nodi e quindi la stessa tensione. _(dispensa, p. 9)_

## Partitori e caratteristiche corrente-tensione

Per il ripasso: [[EL - Partitori ed effetto di carico]].

Per resistenze in serie la tensione si divide in proporzione alla resistenza:
$$v_o=v_i\frac{R_2}{R_1+R_2}.$$
Collegando $R_L$ all’uscita bisogna sostituire $R_2$ con $R_2\parallel R_L$:
$$v_o=v_i\frac{R_2\parallel R_L}{R_1+R_2\parallel R_L}.$$
Questo è l’effetto di carico: collegare un circuito può cambiare il segnale che si voleva misurare.

In un parallelo la corrente si divide in proporzione alle conduttanze. Per due rami:
$$i_1=i_0\frac{R_2}{R_1+R_2},\qquad i_2=i_0\frac{R_1}{R_1+R_2}.$$
Il ramo meno resistivo conduce più corrente. Con $i_0=3\,\mathrm{mA}$, $R_1=1\,\mathrm{k\Omega}$ e $R_2=2\,\mathrm{k\Omega}$ si ottengono $i_1=2\,\mathrm{mA}$ e $i_2=1\,\mathrm{mA}$.

Nel piano con $v$ in ascissa e $i$ in ordinata il resistore ha pendenza $1/R$. Il generatore ideale di tensione è una retta verticale, quello ideale di corrente una retta orizzontale. Per i generatori reali, usando la corrente erogata al carico:
$$v=V_s-R_si,\qquad i=I_s-\frac{v}{R_s}.$$
Un buon generatore di tensione richiede $R_s\ll R_L$; un buon generatore di corrente richiede $R_s\gg R_L$.

_(dispensa, pp. 10–12)_

![[EL-p010-1.png]]

La singola maglia permette di ricavare la corrente e la frazione di tensione su ogni resistore. _(dispensa, p. 10)_

![[EL-p010-2.png]]

Il partitore senza carico trasferisce la frazione R2 divisa per la somma delle resistenze. _(dispensa, p. 10)_

![[EL-p010-3.png]]

Il carico è in parallelo a R2: bisogna ricalcolare il partitore con l’equivalente del parallelo. _(dispensa, p. 10)_

![[EL-p011-1.png]]

La corrente della sorgente si divide tra due rami con la stessa tensione. _(dispensa, p. 11)_

![[EL-p011-2.png]]

Nel piano I–V la pendenza del resistore è la conduttanza, inversa della resistenza. _(dispensa, p. 11)_

![[EL-p011-3.png]]

La serie aumenta la resistenza equivalente e riduce la pendenza della caratteristica I–V. _(dispensa, p. 11)_

![[EL-p012-1.png]]

Il parallelo aumenta la conduttanza equivalente e quindi la pendenza I–V. _(dispensa, p. 12)_

![[EL-p012-2.png]]

La retta verticale indica che la sorgente ideale impone una tensione indipendente dalla corrente. _(dispensa, p. 12)_

![[EL-p012-3.png]]

La resistenza interna inclina la caratteristica: la tensione disponibile diminuisce con la corrente erogata. _(dispensa, p. 12)_

![[EL-p012-4.png]]

La retta orizzontale indica una corrente ideale indipendente dalla tensione ai morsetti. _(dispensa, p. 12)_

![[EL-p012-5.png]]

La corrente del generatore reale si ripartisce tra carico e resistenza interna. _(dispensa, p. 12)_

## Thévenin, Norton e sovrapposizione

Per il ripasso: [[EL - Equivalenti di Thévenin e Norton]] · [[EL - Sovrapposizione degli effetti]].

Una rete lineare vista da due morsetti si può sostituire con un equivalente che riproduce la relazione tensione-corrente ai morsetti:

| Equivalente | Sorgente | Impedenza |
|---|---|---|
| Thévenin | $V_{Th}=V_{oc}$, tensione a vuoto | $Z_{Th}$ in serie |
| Norton | $I_N=I_{sc}$, corrente di cortocircuito | $Z_N$ in parallelo |

Si ha $Z_N=Z_{Th}$ e, con riferimenti coerenti, $V_{Th}=Z_{Th}I_N$. Per calcolare l’impedenza si annullano **solo le sorgenti indipendenti**: generatore di tensione a zero significa cortocircuito; generatore di corrente a zero significa circuito aperto. Se ci sono sorgenti controllate, si mantengono attive e si applica una sorgente di prova: $Z=V_x/I_x$.

> [!warning] Correzione
> A p. 13 il testo richiede di annullare le eccitazioni anche per ricavare $V_{Th}$ e $I_N$. Queste due grandezze si calcolano con le sorgenti originali attive; l’annullamento serve per l’impedenza equivalente. Le figure della stessa pagina distinguono correttamente le due operazioni.

La sovrapposizione permette di sommare i contributi delle sorgenti indipendenti in un circuito lineare. Si attiva una sorgente alla volta e si annullano le altre, mantenendo le resistenze interne e le sorgenti dipendenti. Si sommano tensioni o correnti, non direttamente le potenze, perché $Ri^2$ non è lineare.

Nell’esempio di p. 14, $R_1=50\,\Omega$, $R_2=300\,\Omega$, $R_3=1\,\mathrm{k\Omega}$, $I=3\,\mathrm{mA}$ e $V=10\,\mathrm V$. Con il solo generatore di tensione la corrente in $R_2$ è $10/1350=7.407\,\mathrm{mA}$; il contributo della sorgente di corrente è opposto e vale $3\cdot1050/1350=2.333\,\mathrm{mA}$. La corrente risultante in $R_2$ verso il basso è $5.074\,\mathrm{mA}$ e la sua tensione è $1.522\,\mathrm V$.

_(dispensa, pp. 13–14)_

![[EL-p013-1.png]]

La rete A è sostituita rispetto ai morsetti di collegamento con B. _(dispensa, p. 13)_

![[EL-p013-2.png]]

Il modello Norton conserva la relazione ai morsetti tramite sorgente di corrente e impedenza parallela. _(dispensa, p. 13)_

![[EL-p013-3.png]]

La prova in corto ricava IN; la prova a sorgenti indipendenti annullate ricava l’impedenza. _(dispensa, p. 13)_

![[EL-p013-4.png]]

La stessa rete può essere trattata usando un equivalente di tensione. _(dispensa, p. 13)_

![[EL-p013-5.png]]

Il modello Thévenin usa la tensione a vuoto e l’impedenza in serie. _(dispensa, p. 13)_

![[EL-p013-6.png]]

La figura distingue il calcolo della tensione a vuoto dalla misura dell’impedenza con sorgenti indipendenti annullate; parte della scritta a destra è tagliata già nel sorgente. _(dispensa, p. 13)_

![[EL-p014-1.png]]

Lo svolgimento manoscritto usa la sovrapposizione e mostra separatamente i contributi delle due sorgenti. _(dispensa, p. 14)_

![[EL-p014-2.png]]

La sorgente di corrente è orientata dal nodo A verso il ramo destro; il suo contributo modifica la corrente in R2. _(dispensa, p. 14)_

![[EL-p014-3.png]]

Lo svolgimento è ripetuto nel PDF: l’equazione finale somma algebricamente i contributi indipendenti. _(dispensa, p. 14)_

## Generatori controllati

Per il ripasso: [[EL - Generatori controllati]].

Un generatore controllato impone una grandezza in funzione di un’altra grandezza del circuito. È il modello essenziale di amplificatori e transistor.

| Tipo | Legge | Unità del parametro |
|---|---|---|
| Tensione controllata in tensione | $v_o=\mu v_c$ | V/V |
| Corrente controllata in corrente | $i_o=\beta i_c$ | A/A |
| Tensione controllata in corrente | $v_o=R_m i_c$ | $\Omega$ |
| Corrente controllata in tensione | $i_o=g_m v_c$ | S = A/V |

Nel calcolo di una resistenza equivalente non si elimina una sorgente controllata per il solo fatto di aver annullato le sorgenti indipendenti: la sorgente di prova potrebbe ancora produrre la sua grandezza di controllo.

L’esercizio di p. 16 illustra un controllo di corrente con $\beta=99$: la KCL lega la corrente di controllo, quella comandata e quella nel ramo comune. La tensione della sorgente di corrente non è fissata dal suo valore di corrente, ma si determina dal resto della rete. Lo svolgimento originale è conservato nella figura, con i riferimenti di verso del circuito.

Con $R_1=1\,\mathrm{k\Omega}$, $R_2=2\,\mathrm{k\Omega}$, $R_3=5\,\mathrm{k\Omega}$, $V_{CC}=12$ V e sorgente da 0.6 V con la polarità disegnata:
$$I_1=I_3=(\beta+1)I_2=100I_2,$$
$$12=I_1R_1+I_2R_2+0.6+I_3R_3.$$
Da qui $I_2=11.4/602\,\mathrm{k\Omega}=18.937\,\mu\mathrm A$, $I_1=I_3=1.8937\,\mathrm{mA}$, $V_B=I_3R_3=9.4684$ V e $V_A=12-I_1R_1=10.1063$ V. Il controllo $V_A-V_B=I_2R_2+0.6=0.6379$ V chiude la verifica.

_(dispensa, pp. 15–16)_

![[EL-p015-1.png]]

Il riquadro comune distingue le quattro combinazioni di variabile di controllo e variabile generata; qui interessa il controllo tensione-tensione. _(dispensa, p. 15)_

![[EL-p015-2.png]]

Lo stesso riquadro è ripetuto: nel controllo corrente-corrente il coefficiente è adimensionale. _(dispensa, p. 15)_

![[EL-p015-3.png]]

Nel controllo corrente-tensione il parametro ha unità di resistenza. _(dispensa, p. 15)_

![[EL-p015-4.png]]

Nel controllo tensione-corrente il parametro ha unità di conduttanza. _(dispensa, p. 15)_

![[EL-p016-1.png]]

L’esercizio manoscritto applica KCL al nodo con il generatore controllato: la corrente del ramo comune dipende anche dal fattore beta. _(dispensa, p. 16)_

## Condensatori, induttori e continuità

Per il ripasso: [[EL - Elementi reattivi e continuità]].

Gli elementi reattivi immagazzinano energia. Con convenzione passiva:
$$i_C=C\frac{dv_C}{dt},\qquad v_L=L\frac{di_L}{dt}.$$
In regime sinusoidale $Z_C=1/(j\omega C)$ e $Z_L=j\omega L$. A regime continuo il condensatore ideale è aperto e l’induttore ideale è un cortocircuito. Queste sostituzioni riguardano il regime, non cancellano le condizioni iniziali di un transitorio.

Con correnti finite, $v_C(t_0^+)=v_C(t_0^-)$. Con tensioni finite, $i_L(t_0^+)=i_L(t_0^-)$. L’energia immagazzinata è $E_C=Cv_C^2/2$ e $E_L=Li_L^2/2$.

Un gradino di tensione imposto direttamente a un condensatore ideale richiede una corrente impulsiva. Non si deve descrivere ogni condensatore come un cortocircuito all’istante iniziale: in una rete RC è la sua tensione iniziale a fissare il comportamento iniziale.

_(dispensa, p. 17)_

## Transitori RC e metodo asintotico

Per il ripasso: [[EL - Metodo asintotico RC]] · [[EL - Costante di tempo e assestamento]].

Per una rete lineare del primo ordine, con ingressi costanti dopo $t_0$ e un valore finale finito:
$$v_C(t)=V_\infty+(V_0-V_\infty)e^{-(t-t_0)/\tau},\qquad \tau=R_{eq}C.$$
Si procede così: si calcola $V_0$ dal regime precedente; si usa la continuità di $v_C$; si calcola $V_\infty$ con il nuovo ingresso; si trova $R_{eq}$ vista dal condensatore; si scrive l’esponenziale. A ogni nuova commutazione si riparte dal valore realmente raggiunto, non necessariamente dal regime finale precedente.

Dopo $\tau$ si è percorso il $63.21\%$ della variazione; dopo $5\tau$ il $99.326\%$. Il residuo è $e^{-5}=0.006738$ della variazione iniziale.

> [!warning] Correzione
> P. 19 riporta «99.9%» dopo $5\tau$: il valore è circa **99.33%**. Per il 99.9% servono $\ln(1000)\tau\simeq6.91\tau$. Per un’onda quadra al 50%, se si richiedono $5\tau$ per ciascun livello, serve $T/2\ge5\tau$, ossia $T\ge10\tau$, non semplicemente $T\ge5\tau$.

Nell’esempio di pp. 20–21 il partitore vale $R_2/(R_1+R_2)=2/3$, $R_{eq}=R_1\parallel R_2$ e $\tau\simeq66.7\,\mu\mathrm s$. L’ingresso passa da 1 V a 3 V a $t=1\,\mathrm{ms}$, poi a zero a $t=2\,\mathrm{ms}$:
$$v_C(t)=2+\left(\frac23-2\right)e^{-(t-1\,\mathrm{ms})/\tau}\quad (1\le t/\mathrm{ms}<2).$$
Per $t\ge2\,\mathrm{ms}$, $v_C(t)=v_C(2\,\mathrm{ms}^-)e^{-(t-2\,\mathrm{ms})/\tau}$. In questo caso l’intervallo è molto maggiore di $5\tau$, quindi approssimare il valore alla seconda commutazione con 2 V è accurato.

_(dispensa, pp. 18–21)_

![[EL-p018-1.png]]

Nel circuito RC il gradino d’ingresso richiede una carica progressiva del condensatore. _(dispensa, p. 18)_

![[EL-p018-2.png]]

Subito dopo il gradino il condensatore conserva la tensione iniziale e la caduta compare sul resistore. _(dispensa, p. 18)_

![[EL-p018-3.png]]

Le tangenti iniziali più ripide corrispondono a costanti di tempo minori. _(dispensa, p. 18)_

![[EL-p019-1.png]]

La tangente iniziale incontra l’asintoto dopo una costante di tempo. _(dispensa, p. 19)_

![[EL-p019-2.png]]

La famiglia di risposte mostra che una costante di tempo più piccola accelera l’avvicinamento al valore finale. _(dispensa, p. 19)_

![[EL-p019-3.png]]

La risposta a un’onda rettangolare alterna carica e scarica senza raggiungere istantaneamente i livelli imposti. _(dispensa, p. 19)_

![[EL-p020-1.png]]

Il resistore R2 modifica sia il valore finale sia la resistenza vista dal condensatore. _(dispensa, p. 20)_

![[EL-p020-2.png]]

Con la sorgente indipendente annullata, la prova ai morsetti di C vede R1 e R2 in parallelo. _(dispensa, p. 20)_

![[EL-p020-3.png]]

L’ingresso cambia livello due volte; ciascun intervallo richiede una nuova risposta esponenziale. _(dispensa, p. 20)_

![[EL-p021-1.png]]

Il grafico confronta ingresso e uscita: la tensione sul condensatore resta continua e tende ai nuovi livelli. _(dispensa, p. 21)_

## Carica con un generatore di corrente

Per il ripasso: [[EL - Carica a corrente costante]].

Se la corrente nel condensatore è costante:
$$v_C(t)=v_C(t_0)+\frac{I}{C}(t-t_0).$$
La tensione è una rampa: il generatore ideale continua a fornire carica indipendentemente dalla tensione raggiunta. Se la corrente si annulla e non ci sono perdite, il condensatore mantiene la carica accumulata.

Con un generatore reale, la resistenza parallela offre un percorso alternativo alla corrente. La corrente che carica il condensatore diminuisce all’aumentare della sua tensione e si può ottenere un esponenziale. Nello schema di p. 23, con resistenza serie $R$ e resistenza parallela della sorgente $R_p$, il valore finale è $I_sR_p$ e la resistenza vista da C è $R+R_p$.

> [!warning] Correzione
> Il riepilogo di p. 23 associa in generale «corrente variabile» ed «esponenziale». L’esponenziale deriva dalla particolare equazione differenziale di una rete lineare RC a ingressi costanti. Una corrente variabile arbitraria produce $v_C=v_C(t_0)+(1/C)\int i_C(t)dt$, non necessariamente un esponenziale.

_(dispensa, pp. 22–23)_

![[EL-p022-1.png]]

Una sorgente di corrente costante alimenta il condensatore attraverso il ramo serie. _(dispensa, p. 22)_

![[EL-p022-2.png]]

La pendenza della tensione è I diviso C: corrente costante significa rampa. _(dispensa, p. 22)_

![[EL-p022-3.png]]

Quando la corrente torna a zero il condensatore ideale mantiene il valore raggiunto. _(dispensa, p. 22)_

![[EL-p023-1.png]]

Annullare la sorgente ideale di corrente apre il ramo: non resta un percorso resistivo di scarica. _(dispensa, p. 23)_

![[EL-p023-2.png]]

La resistenza parallela del generatore reale devia corrente mentre sale la tensione, producendo una carica con valore finale finito. _(dispensa, p. 23)_

![[EL-p023-3.png]]

Lo schema della sorgente ideale è ripetuto per confrontarlo con quello reale. _(dispensa, p. 23)_

