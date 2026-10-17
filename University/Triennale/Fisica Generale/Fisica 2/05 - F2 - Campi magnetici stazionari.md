---
title: "Campi magnetici stazionari"
aliases:
  - "F2 — Campi magnetici stazionari"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "195-244"
---

# Campi magnetici stazionari

> [!abstract]
> Correnti e magneti producono un campo che agisce sulle cariche in movimento. La magnetostatica ne descrive le sorgenti, la circuitazione e le forze, distinguendo il campo magnetico da quello elettrostatico.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Magnetismo, Oersted e forza di Lorentz

Vedi [[F2 - Magnetismo, Oersted e forza di Lorentz]].

Una corrente devia un ago magnetico: elettricità e magnetismo sono collegati. La forza su una carica è
$$\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B).$$
$\mathbf B$ si misura in tesla. Il termine magnetico è perpendicolare a $\mathbf v$ e non compie lavoro sulla carica puntiforme: può cambiare la direzione della velocità ma non la sua rapidità. Il segno di $q$ inverte il verso della forza. Nel modello classico non si hanno monopoli magnetici e $\nabla\cdot\mathbf B=0$, ossia il flusso attraverso ogni superficie chiusa è nullo.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Campo delle correnti e forze sui circuiti

Vedi [[F2 - Campo delle correnti e forze sui circuiti]].

Per correnti filiformi stazionarie nel vuoto,
$$d\mathbf B=\frac{\mu_0I}{4\pi}\frac{d\boldsymbol\ell'\times\hat{\mathbf R}}{R^2}.$$
La legge di Biot-Savart si integra sulla sorgente. Per un filo rettilineo infinito $B=\mu_0I/(2\pi r)$; al centro di una spira circolare $B=\mu_0I/(2R)$. Su un tratto di circuito $d\mathbf F=I\,d\boldsymbol\ell\times\mathbf B_{\mathrm{esterno}}$. Due fili paralleli con correnti concordi si attraggono: $F/\ell=\mu_0I_1I_2/(2\pi d)$.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Legge di Ampère e simmetrie

Vedi [[F2 - Legge di Ampère e simmetrie]].

In magnetostatica nel vuoto,
$$\oint_\gamma\mathbf B\cdot d\mathbf l=\mu_0I_{\mathrm{conc}},\qquad\nabla\times\mathbf B=\mu_0\mathbf J.$$
Il verso della normale alla superficie concatenata segue la mano destra rispetto alla percorrenza del contorno. Il campo nel singolo punto dipende anche dalle correnti non concatenate; queste non contribuiscono alla circuitazione netta. Per un solenoide ideale lungo $B\simeq\mu_0nI$ all'interno e quasi zero lontano dai bordi all'esterno. La sola conoscenza della circuitazione non determina il campo senza sufficiente simmetria.

![[F2-p207-1.png]]

*Figura 5-21: il campo locale è prodotto da entrambe le correnti; la circuitazione sul contorno disegnato dipende invece solo dalla corrente concatenata. Invertire una corrente modifica le linee anche fuori dal contorno.* _(Libro, p. 199; PDF p. 207.)_

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Particelle cariche ed effetto Hall

Vedi [[F2 - Particelle cariche ed effetto Hall]].

In $\mathbf B$ uniforme, senza campo elettrico, la componente parallela della velocità resta costante e quella perpendicolare ruota:
$$r_L=\frac{m v_\perp}{|q|B},\qquad\omega_c=\frac{|q|B}{m}.$$
Il moto generale è elicoidale. Nei campi incrociati perpendicolari, una particella non deviata soddisfa $\mathbf E+\mathbf v\times\mathbf B=0$ e, nella geometria del selettore, $v=E/B$. L'effetto Hall nasce dalla separazione trasversale dei portatori fino al bilanciamento fra forza elettrica e magnetica; il segno della tensione fornisce informazioni sul segno dei portatori.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Dipoli e proprietà magnetiche della materia

Vedi [[F2 - Dipoli e proprietà magnetiche della materia]].

Una spira piana ha momento magnetico $\mathbf m=IA\hat{\mathbf n}$, momento torcente $\boldsymbol\tau=\mathbf m\times\mathbf B$ ed energia $U=-\mathbf m\cdot\mathbf B$. Una spira può compiere lavoro meccanico mentre il generatore e il campo scambiano energia: ciò non contraddice il lavoro nullo del termine magnetico sulla singola carica.

Con magnetizzazione $\mathbf M$ si definisce $\mathbf B=\mu_0(\mathbf H+\mathbf M)$. Nei mezzi lineari isotropi $\mathbf B=\mu\mathbf H$. Diamagnetismo, paramagnetismo e ferromagnetismo descrivono risposte diverse; nei ferromagneti isteresi e saturazione impediscono l'uso universale di una permeabilità costante. Il potenziale vettore soddisfa $\mathbf B=\nabla\times\mathbf A$ e non è unico.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Risonanza magnetica e potenziale vettore

Vedi [[F2 - Risonanza magnetica e potenziale vettore]].

I momenti magnetici microscopici sono legati a moti orbitali e spin. In un campo uniforme un momento può precedere; la frequenza di Larmor è proporzionale a $B$ tramite il rapporto giromagnetico della specie. Un campo oscillante appropriato può produrre risonanza, principio alla base della risonanza magnetica nucleare. La descrizione dei livelli di spin richiede la meccanica quantistica: il modello classico di una spira è un'analogia utile ma non una spiegazione completa.

Il potenziale vettore non è direttamente una seconda copia del campo: trasformare $\mathbf A$ in $\mathbf A+\nabla\chi$ lascia invariato $\mathbf B$. Nei campi variabili il campo elettrico generale è $\mathbf E=-\nabla V-\partial_t\mathbf A$.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Derivazione guidata

Per il filo infinito, la simmetria impone un campo azimutale con modulo dipendente solo da $r$. Scegli come contorno una circonferenza concentrica: $\oint\mathbf B\cdot d\mathbf l=B\,2\pi r$. Ampère dà allora $B=\mu_0I/(2\pi r)$. Il verso segue la mano destra rispetto alla corrente. Se aggiungi correnti che rompono la simmetria, l'integrale di Ampère resta valido ma non puoi più sostituirlo automaticamente con $B\,2\pi r$.

_(Libro, cap. 5; pagine stampate 187–236; PDF pp. 195–244.)_

## Esempio svolto

> [!example] Applicazione originale
> Un protone con $m\simeq1{,}67\cdot10^{-27}\,\mathrm{kg}$ e $q\simeq1{,}60\cdot10^{-19}\,\mathrm C$ entra perpendicolarmente a $B=0{,}10\,\mathrm T$ a $v=10^5\,\mathrm{m/s}$. Il raggio è $r_L=1{,}04\,\mathrm{cm}$. Il campo non cambia la sua energia cinetica; una componente iniziale parallela all'asse trasformerebbe il cerchio in un'elica.

## Richiami matematici

[[GEO - Prodotto scalare geometrico]] · [[09 - AN1 - Funzioni a Valori Vettoriali]] · [[01 - F1 - Cinematica del punto]].

## Verifica attiva

Un campo magnetico uniforme può accelerare una particella senza aumentarne l’energia cinetica?

> [!check]- Risposta ragionata
> Sì: il termine magnetico cambia la direzione della velocità. Il suo prodotto scalare con la velocità è nullo, quindi è nulla la potenza magnetica sulla particella.

## Navigazione

Precedente: [[04 - F2 - Correnti elettriche stazionarie]] · Successivo: [[06 - F2 - Induzione e campi elettromagnetici]].
