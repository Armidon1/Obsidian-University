---
title: "Semiconduttori e diodi"
aliases:
  - "EL — Semiconduttori e diodi"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Semiconduttori e diodi

> [!abstract]
> La fisica dei portatori spiega la giunzione PN; modelli via via più semplici rendono risolvibili i circuiti con diodi.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 95–112.

Precedente: [[08 - EL - Multivibratori e generatori di forme d’onda]] · Successiva: [[10 - EL - MOSFET - Struttura e regioni di funzionamento]]

## Bande di energia e drogaggio

Per il ripasso: [[EL - Drogaggio dei semiconduttori]].

Nel cristallo gli stati energetici si organizzano in bande: banda di valenza e di conduzione, separate da un intervallo proibito. Nel silicio il gap è circa 1.1 eV. Il silicio intrinseco possiede elettroni e lacune generati termicamente; ha conducibilità molto inferiore a quella del silicio fortemente drogato, ma non è un isolante perfetto.

Il drogaggio **n** introduce donatori pentavalenti, come il fosforo: gli elettroni sono i portatori maggioritari e gli ioni donatori restano fissi nel reticolo. Il drogaggio **p** introduce accettori trivalenti, come il boro: i portatori maggioritari sono lacune, descrivibili come cariche positive mobili. Il materiale drogato resta globalmente quasi neutro lontano dalle zone di carica spaziale.

> [!warning] Correzione
> A p. 97 l’elettrone libero è chiamato «carica positiva» e si dice che si muove nel verso del campo. L’elettrone ha carica **negativa** e deriva in verso opposto al campo; la corrente convenzionale ha verso opposto al moto elettronico. La lacuna non è uno ione positivo del reticolo che viaggia: è una mancanza di elettrone nella banda di valenza.

_(dispensa, pp. 95–97)_

![[EL-p096-1.png]]

Nel cristallo gli stati energetici si allargano in bande, separate dal gap proibito. _(dispensa, p. 96)_

![[EL-p096-2.png]]

Il silicio forma legami covalenti con quattro vicini; l’eccitazione può liberare una coppia elettrone-lacuna. _(dispensa, p. 96)_

![[EL-p096-3.png]]

Un donatore pentavalente introduce un elettrone debolmente legato che può diventare portatore mobile. _(dispensa, p. 96)_

![[EL-p097-1.png]]

L’accettore trivalente lascia una lacuna nel sistema dei legami. _(dispensa, p. 97)_

![[EL-p097-2.png]]

Le annotazioni distinguono lo ione accettore fisso dalla lacuna che può spostarsi attraverso il riassetto dei legami. _(dispensa, p. 97)_

## Drift, diffusione e potenziale di contatto

Per il ripasso: [[EL - Drift e diffusione]] · [[EL - Giunzione PN e svuotamento]].

La deriva (**drift**) è dovuta al campo elettrico, la diffusione al gradiente di concentrazione. In una dimensione, con $q>0$:
$$J_n=q\mu_n nE+qD_n\frac{dn}{dx},\qquad
J_p=q\mu_p pE-qD_p\frac{dp}{dx}.$$
La relazione di Einstein collega mobilità e diffusione: $D_n=\mu_nV_T$, $D_p=\mu_pV_T$, con $V_T=kT/q\simeq25.3\,\mathrm{mV}$ a 20 °C. La conducibilità dovuta alla deriva è $\sigma=q(\mu_nn+\mu_pp)$.

All’equilibrio drift e diffusione si compensano per ciascun tipo di portatore. Per una barra p a concentrazione variabile, $E=(V_T/p)dp/dx=-dV/dx$, da cui $V_2-V_1=V_T\ln(p_1/p_2)$.

Mettendo a contatto regioni p e n, i portatori diffondono e si ricombinano vicino alla giunzione; restano ioni fissi di segno opposto. Nasce una **regione di svuotamento**, con un campo che ostacola ulteriore diffusione. È svuotata soprattutto di portatori mobili, non di ogni carica elettrica.

_(dispensa, pp. 98–100)_

![[EL-p099-1.png]]

Una differenza di concentrazione fra due zone della barra genera diffusione. _(dispensa, p. 99)_

![[EL-p099-2.png]]

La separazione di carica crea un campo interno che all’equilibrio bilancia la diffusione. _(dispensa, p. 99)_

![[EL-p100-1.png]]

Prima del contatto, le regioni p e n hanno portatori maggioritari diversi. _(dispensa, p. 100)_

![[EL-p100-2.png]]

Dopo il contatto, vicino all’interfaccia restano ioni fissi e si forma una barriera di potenziale. _(dispensa, p. 100)_

## Polarizzazione e legge di Shockley

Per il ripasso: [[EL - Legge di Shockley]].

Si pone $v_D=v_A-v_K$, con anodo nella regione p e catodo nella regione n. La polarizzazione diretta riduce la barriera e favorisce l’iniezione di portatori; quella inversa allarga la regione svuotata. In inversa rimane una piccola corrente, prima del breakdown.

La legge di Shockley è:
$$i_D=I_S\left(e^{v_D/(nV_T)}-1\right).$$
Per $i_D\gg I_S$, $v_D\simeq nV_T\ln(i_D/I_S)$. Tra due punti:
$$V_{D2}-V_{D1}=nV_T\ln\frac{I_{D2}}{I_{D1}}.$$
Con $n=1$, aumentare la corrente di un fattore 10 richiede circa $V_T\ln10\simeq58\,\mathrm{mV}$ a 20 °C. Non esiste una soglia fisica universale e netta a 0.6 o 0.7 V: tali valori sono approssimazioni circuitali.

> [!warning] Correzione
> P. 103 scrive il rapporto $I_{D1}/I_{D2}$ con l’esponente avente segno da rapporto inverso. La relazione coerente è $I_{D2}/I_{D1}=e^{(V_{D2}-V_{D1})/(nV_T)}$.

_(dispensa, pp. 101–103)_

![[EL-p101-1.png]]

La polarizzazione esterna si applica soprattutto alla regione di svuotamento. _(dispensa, p. 101)_

![[EL-p101-2.png]]

L’approssimazione resistiva distingue regioni quasi neutre molto conduttive e regione centrale di giunzione. _(dispensa, p. 101)_

![[EL-p101-3.png]]

La polarizzazione diretta riduce la barriera e consente una corrente convenzionale da p verso n. _(dispensa, p. 101)_

![[EL-p102-1.png]]

La polarizzazione inversa allarga la regione di svuotamento e ostacola la corrente maggioritaria. _(dispensa, p. 102)_

![[EL-p102-2.png]]

La caratteristica di Shockley cresce esponenzialmente in diretta e presenta una piccola corrente inversa. _(dispensa, p. 102)_

![[EL-p102-3.png]]

La barra del simbolo identifica il catodo; la tensione diretta si misura dall’anodo al catodo. _(dispensa, p. 102)_

![[EL-p103-1.png]]

La crescita esponenziale non ha una soglia netta, benché intorno a 0.6–0.7 V la corrente diventi significativa in molti esempi. _(dispensa, p. 103)_

## Breakdown e stabilizzazione

Per il ripasso: [[EL - Breakdown del diodo]].

Con tensione inversa sufficientemente elevata la corrente cresce rapidamente. Il breakdown può dipendere da valanga o da tunneling Zener; non è descritto dalla semplice legge di Shockley. Un diodo progettato per questa regione può stabilizzare una tensione se si limita opportunamente la corrente.

La potenza assorbita, con convenzione passiva, è $p_D=v_Di_D$. In breakdown tensione e corrente sono entrambe negative, quindi la potenza assorbita è positiva. Una resistenza o un limitatore è indispensabile per non superare i limiti del dispositivo.

> [!warning] Correzione
> P. 104 afferma che prima del breakdown «la tensione è nulla». In interdizione è circa nulla la **corrente**, mentre il diodo può sostenere una tensione inversa. Né la caduta diretta né quella Zener rimangono rigorosamente costanti per qualsiasi carico e corrente.

_(dispensa, p. 104)_

![[EL-p104-1.png]]

In inversa compare il breakdown oltre una tensione caratteristica, non previsto dalla semplice equazione di Shockley. _(dispensa, p. 104)_

## Termometria, fotodiodi e celle solari

Per il ripasso: [[EL - Diodo come sensore di temperatura]] · [[EL - Fotodiodo e cella solare]].

A corrente diretta fissata la tensione di giunzione varia con la temperatura; il libro usa circa −2 mV/°C come sensibilità tipica. Non basta dire che $V_T$ cresce con T: anche $I_S$ dipende fortemente dalla temperatura. Misurando la differenza tra due cadute a correnti in rapporto noto si ottiene $\Delta V_D=nV_T\ln(I_2/I_1)$, proporzionale alla temperatura assoluta nel modello.

La luce genera coppie elettrone-lacuna e trasla la caratteristica del diodo:
$$i_D=I_S(e^{v_D/(nV_T)}-1)-I_{PH},\qquad I_{PH}=\mathcal R P_{ott}.$$
La responsività $\mathcal R$ si misura in **A/W**. Il fotodiodo può misurare la potenza ottica; una cella fotovoltaica lavora nella regione con $v_D>0$ e $i_D<0$, quindi eroga potenza elettrica. Il punto di massima potenza massimizza $-v_Di_D$; non corrisponde necessariamente a una tensione fissa di 0.6 V.

> [!warning] Correzione
> P. 106 scrive la responsività in A·W: l’unità corretta è A/W. Il riepilogo di p. 107 associa la termometria al terzo quadrante, ma l’esempio di p. 105 usa una giunzione in **diretta a corrente costante**, nel primo quadrante. La sola posizione nel piano I–V non identifica in generale l’applicazione.

_(dispensa, pp. 105–107)_

![[EL-p105-1.png]]

A corrente fissata le curve a temperature diverse danno cadute dirette differenti. _(dispensa, p. 105)_

![[EL-p105-2.png]]

L’esempio di termometro usa differenze di cadute di giunzione e una catena di amplificazione e conversione. _(dispensa, p. 105)_

![[EL-p106-1.png]]

L’illuminazione trasla la caratteristica verso correnti più negative di una quantità proporzionale alla potenza ottica. _(dispensa, p. 106)_

![[EL-p106-2.png]]

Nel quarto quadrante la cella eroga potenza; il rettangolo tensione-corrente individua il punto di massima erogazione. _(dispensa, p. 106)_

![[EL-p106-3.png]]

La corrente fotogenerata si modella con una sorgente in parallelo alla giunzione. _(dispensa, p. 106)_

## Retta di carico e modelli del diodo

Per il ripasso: [[EL - Retta di carico]] · [[EL - Modelli circuitali del diodo]].

Nel circuito con generatore $V_{DD}$, resistenza R e diodo in serie, KVL dà $i_D=(V_{DD}-v_D)/R$. L’intersezione tra questa **retta di carico** e la caratteristica del diodo è il punto di lavoro. Cambiare $V_{DD}$ trasla la retta; cambiare R ne modifica la pendenza.

| Modello | Stato OFF | Stato ON |
|---|---|---|
| Ideale | $i_D=0$, $v_D\le0$ | $v_D=0$, $i_D\ge0$ |
| Caduta costante | $i_D=0$, $v_D\le V_\gamma$ | $v_D=V_\gamma$, $i_D\ge0$ |
| Lineare a tratti | $i_D=0$ sotto soglia | $v_D=V_\gamma+r_Di_D$ |

Il modello a tratti rende lineare ogni configurazione, ma la scelta della configurazione è parte del problema. La resistenza dinamica locale della legge esponenziale è $r_d\simeq nV_T/I_D$; un valore scelto per una linearizzazione ampia non va confuso automaticamente con questa derivata.

> [!warning] Correzione
> P. 110 scrive $v_D=0$ nello stato OFF del modello a caduta costante. Deve essere **$i_D=0$**; la tensione è determinata dalla rete.

_(dispensa, pp. 108–110)_

![[EL-p108-1.png]]

La maglia con sorgente e resistenza impone una retta di carico al diodo. _(dispensa, p. 108)_

![[EL-p108-2.png]]

L’intersezione fra retta decrescente e caratteristica esponenziale individua tensione e corrente di lavoro. _(dispensa, p. 108)_

![[EL-p108-3.png]]

Il carico in parallelo assorbe parte della corrente e modifica il punto di lavoro della giunzione. _(dispensa, p. 108)_

![[EL-p109-1.png]]

Il modello lineare a tratti sostituisce la regione di conduzione con soglia e resistenza serie. _(dispensa, p. 109)_

![[EL-p110-1.png]]

Il modello a caduta costante trascura la resistenza della regione ON. _(dispensa, p. 110)_

![[EL-p110-2.png]]

Il diodo ideale è aperto in inversa e ha caduta nulla quando conduce corrente nel verso diretto. _(dispensa, p. 110)_

## Analisi per stati e regolatore Zener

Per il ripasso: [[EL - Regolatore Zener]].

Il procedimento è: ipotizzare ON/OFF per ciascun diodo; sostituire i modelli; risolvere la rete lineare; verificare $i_D\ge0$ per ogni diodo ON e la tensione ammessa per ogni diodo OFF. Una corrente negativa in un diodo assunto ON invalida l’ipotesi.

Nell’esempio di selezione a p. 111, i due ingressi sono +1 V e +3 V e il resistore da 2 kΩ va a −3 V. Con diodi ideali conduce quello collegato a +3 V: l’uscita è 3 V e la corrente è $[3-(-3)]/2\,\mathrm{k\Omega}=3\,\mathrm{mA}$. Il diodo collegato a +1 V è inversamente polarizzato.

Nel regolatore Zener di p. 112, $V_S=10\,\mathrm V$, $R=0.5\,\mathrm{k\Omega}$, $V_Z=6.8\,\mathrm V$. In regolazione:
$$I_R=\frac{10-6.8}{0.5\,\mathrm{k\Omega}}=6.4\,\mathrm{mA},\qquad
I_Z=I_R-\frac{6.8}{R_L}.$$
Con modello ideale la condizione $I_Z\ge0$ richiede $R_L\ge1.0625\,\mathrm{k\Omega}$. A vuoto $P_Z=6.8\cdot6.4\,\mathrm{mW}=43.52\,\mathrm{mW}$. Con $R_L=R=0.5\,\mathrm{k\Omega}$, la tensione del partitore è 5 V e lo Zener resta spento. Un regolatore reale richiede anche una corrente minima di ginocchio e il rispetto della potenza massima.

_(dispensa, pp. 111–112)_

![[EL-p111-1.png]]

Assumere il diodo aperto porta a una tensione che ne verifica o smentisce la polarizzazione. _(dispensa, p. 111)_

![[EL-p111-2.png]]

Nel caso corretto il diodo in conduzione collega il nodo al riferimento basso e la corrente si ricava dalla resistenza. _(dispensa, p. 111)_

![[EL-p111-3.png]]

Il diodo verso il riferimento maggiore conduce e seleziona il livello di 3 V; l’altro rimane inverso. _(dispensa, p. 111)_

![[EL-p112-1.png]]

Il simbolo Zener indica un dispositivo usato in breakdown inverso con corrente di riferimento specificata. _(dispensa, p. 112)_

![[EL-p112-2.png]]

Il modello ha una regione centrale aperta e due regioni a tensione approssimativamente fissata. _(dispensa, p. 112)_

![[EL-p112-3.png]]

Il resistore serie limita la corrente; Zener e carico condividono la tensione regolata. _(dispensa, p. 112)_

