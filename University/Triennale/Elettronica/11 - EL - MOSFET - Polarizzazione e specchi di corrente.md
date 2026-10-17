---
title: "MOSFET - Polarizzazione e specchi di corrente"
aliases:
  - "EL — MOSFET - Polarizzazione e specchi di corrente"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# MOSFET - Polarizzazione e specchi di corrente

> [!abstract]
> Si determina il punto di riposo prima del guadagno: partitori, degenerazione di source e generatori di corrente fissano le condizioni del dispositivo.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 130–134.

Precedente: [[10 - EL - MOSFET - Struttura e regioni di funzionamento]] · Successiva: [[12 - EL - MOSFET - Piccolo segnale e carichi attivi]]

## Partitore di gate e degenerazione di source

Per il ripasso: [[EL - Polarizzazione con resistenza di source]].

Poiché $I_G\simeq0$, un partitore non caricato fissa:
$$V_G=V_{DD}\frac{R_B}{R_A+R_B}.$$
Con source direttamente a massa, $V_{GS}=V_G$ e la corrente risente fortemente delle variazioni di soglia e K. Inserendo $R_S$:
$$V_{GS}=V_G-I_DR_S,\qquad I_D=K(V_{GS}-V_{th})^2.$$
Se $I_D$ aumenta, sale $V_S$ e diminuisce $V_{GS}$: questa è retroazione negativa locale. Il punto di lavoro diventa meno sensibile ai parametri, ma non è automaticamente al centro della dinamica: occorre progettarlo.

Il condensatore d’ingresso separa la polarizzazione dalla componente continua della sorgente del segnale. Il rapporto del partitore fissa $V_G$; il valore assoluto delle resistenze incide su corrente di riposo, impedenza d’ingresso e risposta in frequenza.

_(dispensa, p. 130)_

![[EL-p130-1.png]]

Il partitore fissa la tensione di gate e il condensatore separa la continua della sorgente. _(dispensa, p. 130)_

![[EL-p130-2.png]]

Dispositivi con parametri diversi possono produrre correnti diverse a parità di tensione di gate. _(dispensa, p. 130)_

![[EL-p130-3.png]]

La resistenza di source fa dipendere VGS dalla corrente e realizza retroazione negativa. _(dispensa, p. 130)_

## Esempio e scelta della radice fisica

Per il ripasso: [[EL - Verifica del punto di lavoro MOS]].

Dati: $V_{DD}=5\,\mathrm V$, $R_A=20\,\mathrm{k\Omega}$, $R_B=30\,\mathrm{k\Omega}$, $R_S=1\,\mathrm{k\Omega}$, $V_{th}=1\,\mathrm V$, $K=1\,\mathrm{mA/V^2}$. Il partitore dà $V_G=3\,\mathrm V$.

In unità V, mA e kΩ si risolve $3=V_{GS}+(V_{GS}-1)^2$. Le radici sono 2 V e −1 V. La seconda non appartiene alla regione $V_{GS}>V_{th}$ assunta per la legge quadratica; si sceglie $V_{GS}=2\,\mathrm V$, $I_D=1\,\mathrm{mA}$ e $V_S=1\,\mathrm V$.

Il vincolo di saturazione è:
$$V_{DS}=5-(1\,\mathrm{mA})(R_D+1\,\mathrm{k\Omega})\ge1\,\mathrm V.$$
Quindi $R_D\le3\,\mathrm{k\Omega}$. L’uguaglianza è il bordo della saturazione: per un segnale variabile si lascia margine, invece di collocare il punto esattamente sul confine.

_(dispensa, p. 131)_

![[EL-p131-1.png]]

Il circuito dell’esercizio permette di trovare prima la corrente e poi il massimo RD compatibile con la saturazione. _(dispensa, p. 131)_

![[EL-p131-2.png]]

Le due intersezioni algebriche non sono entrambe ammissibili: si sceglie quella sopra soglia. _(dispensa, p. 131)_

![[EL-p131-3.png]]

La retta limite corrisponde al confine VDS uguale all’overdrive e fissa RD massimo. _(dispensa, p. 131)_

## Impedenza di ingresso e polarizzazione a corrente

Per il ripasso: [[EL - Rete di polarizzazione e impedenza]] · [[EL - Polarizzazione a corrente imposta]].

Moltiplicare $R_A$ e $R_B$ per lo stesso fattore lascia invariato $V_G$, ma cambia $R_A\parallel R_B$, che è l’impedenza d’ingresso a centro banda della rete di polarizzazione. Resistenze maggiori riducono la corrente assorbita dal partitore, ma interagiscono anche con capacità e correnti non ideali.

Un’alternativa consiste nell’imporre direttamente la corrente nel source. Se il transistor è in saturazione:
$$V_{GS}=V_{th}+\sqrt{I_D/K}.$$
L’alimentazione deve consentire la tensione necessaria sia al transistor sia alla sorgente di corrente. Una sorgente reale mantiene la corrente solo entro il suo intervallo di compliance.

_(dispensa, p. 132)_

![[EL-p132-1.png]]

Una sorgente di corrente nel source impone la corrente continua del transistor. _(dispensa, p. 132)_

![[EL-p132-2.png]]

Il modello di sorgente mantiene la corrente soltanto finché la tensione del carico resta compatibile con la sua compliance. _(dispensa, p. 132)_

![[EL-p132-3.png]]

Gate e source comuni fanno copiare al secondo MOS la tensione di controllo del primo. _(dispensa, p. 132)_

## Specchio di corrente

Per il ripasso: [[EL - Specchio di corrente MOS]] · [[EL - MOS connesso a diodo]].

Due MOS con source e gate comuni hanno la stessa $V_{GS}$. Nel ramo di riferimento il primo è **connesso a diodo**, cioè gate e drain collegati: se acceso e con soglia positiva, $V_{DS}=V_{GS}$ soddisfa la condizione di saturazione.

Trascurando la modulazione e assumendo soglie uguali:
$$\frac{I_{D2}}{I_{D1}}=\frac{K_2}{K_1}=\frac{(W/L)_2}{(W/L)_1}.$$
Il secondo copia o scala la corrente di riferimento, purché abbia $V_{DS2}\ge V_{OV}$. Le correnti non sono necessariamente uguali: dipendono dalle geometrie. Con modulazione occorre considerare anche le diverse tensioni drain-source.

> [!warning] Correzione
> P. 133 pone $I_{D1}=V_{DD}/R$ nonostante la tensione sul MOS connesso a diodo. Nello schema a singola alimentazione la relazione corretta è $I_{REF}=(V_{DD}-V_{GS})/R$. Nello schema disegnato tra $+V_{DD}$ e $-V_{SS}$ diventa $I_{REF}=(V_{DD}+V_{SS}-V_{GS})/R$.

Nella polarizzazione con gate a massa, un NMOS acceso richiede source negativo. La resistenza di gate stabilisce il riferimento continuo senza cortocircuitare a massa il segnale alternato applicato tramite condensatore.

_(dispensa, p. 133)_

![[EL-p133-1.png]]

Lo specchio sottostante imposta la corrente del transistor amplificatore; il riferimento negativo consente un source sotto massa. _(dispensa, p. 133)_

## Esempio con due transistor accoppiati in continua

Nel primo transistor $I_{D1}=2\,\mathrm{mA}$ è fissata dalla sorgente, $K_1=0.5\,\mathrm{mA/V^2}$ e $V_{th}=1\,\mathrm V$. Quindi $V_{GS1}=3\,\mathrm V$. Con gate a massa, $V_{S1}=-3\,\mathrm V$; con $V_{DD}=5\,\mathrm V$ e $R_{D1}=1\,\mathrm{k\Omega}$, $V_{D1}=3\,\mathrm V$ e $V_{DS1}=6\,\mathrm V$.

Il gate del secondo è a $V_{G2}=V_{D1}=3\,\mathrm V$. Con $R_{S2}=1\,\mathrm{k\Omega}$ e $K_2=1\,\mathrm{mA/V^2}$ si risolve $3=V_{GS2}+(V_{GS2}-1)^2$, ottenendo la radice valida 2 V. Ne seguono $I_{D2}=1\,\mathrm{mA}$, $V_{S2}=1\,\mathrm V$, $V_{D2}=5-1\cdot2=3\,\mathrm V$ e **$V_{DS2}=2\,\mathrm V$**. Entrambi i transistor soddisfano la condizione di saturazione.

> [!warning] Correzione
> A p. 134 compare $V_G=V_{GS}-V_S$; deve essere $V_G=V_{GS}+V_S$. Il riepilogo finale scrive $V_{DS2}=1$ V, mentre il suo stesso calcolo dà **2 V**. I valori corretti sono usati qui e nella successiva lezione sugli amplificatori.

_(dispensa, p. 134)_

![[EL-p134-1.png]]

Il gate del secondo MOS è collegato al drain del primo, quindi la polarizzazione va risolta in sequenza. _(dispensa, p. 134)_

