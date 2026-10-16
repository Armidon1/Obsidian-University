---
title: "Richiami di geometria del piano"
aliases:
  - "GEO — Richiami di geometria del piano"
tags:
  - geometria
  - appendice
source: "pdf/Geometria.pdf"
chapter: "B"
pdf_pages: "755–780"
---

# Richiami di geometria del piano

> [!abstract] Scopo e percorso
> Appendici. Questa nota segue il capitolo B del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## B.1 - Punti e rette

Vedi [[GEO - Punti e rette euclidee]].

La geometria euclidea parte da punti, rette e relazioni fondamentali. Due punti distinti individuano un’unica retta; esistono punti non allineati. La relazione $P\in r$ esprime appartenenza.

Il disegno aiuta a interpretare queste proprietà, ma la verifica di una costruzione si basa sulle ipotesi, non sull’apparenza grafica.

_(Accascina–Monti, § B.1, libro pp. 739–740; PDF pp. 755–756.)_

![[GEO-p755-1.png|650]]

**Lettura della figura (PDF p. 755, libro p. 739).** Due punti distinti determinano una retta. La figura fissa il significato geometrico dell’appartenenza prima delle successive costruzioni.

## B.2 - Semirette, segmenti e semipiani

Vedi [[GEO - Convessità e regioni del piano]].

Un punto di una retta la divide in due semirette. Due punti delimitano un segmento; si distingue quello aperto, senza estremi, da quello chiuso. Una retta divide il piano in due semipiani aperti, che non includono la retta di bordo.

Un insieme è convesso quando contiene il segmento tra ogni coppia di suoi punti. Un disco è convesso; una regione con un rientro o un foro può non esserlo. Se due punti stanno in semipiani opposti, il loro segmento attraversa la retta di confine.

_(Accascina–Monti, § B.2, libro pp. 740–743; PDF pp. 756–759.)_

![[GEO-p756-1.png|650]]

**Lettura della figura (PDF p. 756, libro p. 740).** Le figure distinguono semirette con origine fissata e segmenti delimitati da due estremi: il ruolo del punto iniziale non coincide con quello di un generico punto interno.

![[GEO-p757-1.png|650]]

**Lettura della figura (PDF p. 757, libro p. 741).** Il segmento e la regione ombreggiata introducono la convessità: si controlla se il segmento tra due punti della regione rimane al suo interno.

![[GEO-p758-1.png|650]]

**Lettura della figura (PDF p. 758, libro p. 742).** Il confronto tra regioni con forme differenti rende visibile la differenza tra convessità e presenza di rientranze; la retta finale introduce la separazione in semipiani.

## B.3 - Poligoni

Vedi [[GEO - Poligoni e parallelogrammi]].

Un poligono è delimitato da una spezzata chiusa. Vertici consecutivi individuano i lati; le diagonali uniscono vertici non consecutivi. Convessità e concavità riguardano la regione interna e la permanenza dei segmenti in essa.

I parallelogrammi sono quadrilateri con lati opposti paralleli. Le loro diagonali si tagliano a metà: questa proprietà rende naturale la regola del parallelogramma per sommare vettori.

_(Accascina–Monti, § B.3, libro pp. 743–744; PDF pp. 759–760.)_

![[GEO-p759-1.png|650]]

**Lettura della figura (PDF p. 759, libro p. 743).** La figura delle rette mostra lati opposti del confine; i poligoni successivi identificano lati, vertici e diagonali.

## B.4 - Distanze tra punti

Vedi [[GEO - Distanza euclidea e punto medio]].

La distanza euclidea soddisfa positività, simmetria e disuguaglianza triangolare:

$$d(A,C)\le d(A,B)+d(B,C).$$

L’uguaglianza si ha quando $B$ appartiene al segmento chiuso tra $A$ e $C$. Il punto medio $M$ divide un segmento in due parti uguali: $d(A,M)=d(M,B)=d(A,B)/2$.

_(Accascina–Monti, § B.4, libro pp. 744–745; PDF pp. 760–761.)_

![[GEO-p760-1.png|650]]

**Lettura della figura (PDF p. 760, libro p. 744).** Le configurazioni di quadrilateri distinguono forme generiche e parallelogrammi, le cui coppie di lati opposti sono parallele.

## B.5 - Rette parallele

Vedi [[GEO - Parallelismo euclideo nel piano]].

Nel libro due rette sono parallele se sono distinte senza punti comuni **oppure coincidono**. Con questa convenzione il parallelismo è una relazione di equivalenza.

Il postulato euclideo assicura una sola parallela a una retta data per un punto assegnato. Per le costruzioni vettoriali questa unicità permette di trasportare una direzione senza ambiguità.

_(Accascina–Monti, § B.5, libro pp. 745–747; PDF pp. 761–763.)_

![[GEO-p761-1.png|650]]

**Lettura della figura (PDF p. 761, libro p. 745).** I triangoli e i punti allineati collegano il confronto fra lunghezze alla disuguaglianza triangolare e al segmento che realizza l’uguaglianza.

![[GEO-p762-1.png|650]]

**Lettura della figura (PDF p. 762, libro p. 746).** Le rette parallele mostrano il trasporto di direzioni e le costruzioni ottenute tracciando la parallela per un punto dato.

## B.6 - Angoli

Vedi [[GEO - Angoli euclidei]].

Due semirette con la stessa origine delimitano angoli. Un angolo piatto misura $\pi$ radianti, un giro completo $2\pi$. Due angoli supplementari hanno somma $\pi$; due complementari somma $\pi/2$.

Per due rette incidenti gli angoli opposti al vertice sono uguali e quelli adiacenti sono supplementari. Per questo l’angolo tra rette richiede spesso di scegliere il minore dei due.

_(Accascina–Monti, § B.6, libro pp. 747–749; PDF pp. 763–765.)_

![[GEO-p763-1.png|650]]

**Lettura della figura (PDF p. 763, libro p. 747).** Il parallelogramma e la regione angolare introducono l’angolo come parte del piano delimitata da due semirette di origine comune.

![[GEO-p764-1.png|650]]

**Lettura della figura (PDF p. 764, libro p. 748).** Le configurazioni confrontano angoli opposti al vertice, supplementari e formati da rette parallele: le uguaglianze dipendono dalle relazioni fra le rette.

## B.7 - Ortogonalità

Vedi [[GEO - Perpendicolari nel piano]].

Due rette incidenti sono ortogonali se formano angoli retti. Per un punto del piano passa un’unica retta ortogonale a una retta data. Due rette ortogonali alla stessa retta sono parallele.

Il piede della perpendicolare da un punto a una retta è il punto della retta a distanza minima. È la costruzione geometrica che giustifica le formule analitiche punto-retta.

_(Accascina–Monti, § B.7, libro pp. 749–751; PDF pp. 765–767.)_

![[GEO-p765-1.png|650]]

**Lettura della figura (PDF p. 765, libro p. 749).** Gli incroci di rette distinguono la perpendicolarità da un’intersezione generica; l’angolo retto è la condizione essenziale.

![[GEO-p766-1.png|650]]

**Lettura della figura (PDF p. 766, libro p. 750).** Le costruzioni mostrano la perpendicolare e il piede della proiezione, e collegano rette ortogonali a una stessa retta al parallelismo.

## B.8 - Triangoli

Vedi [[GEO - Teoremi sui triangoli]].

In un triangolo la somma degli angoli interni è $\pi$. Per un triangolo rettangolo di cateti $a,b$ e ipotenusa $c$, il teorema di Pitagora dà $a^2+b^2=c^2$.

Il teorema del coseno generalizza la relazione: $c^2=a^2+b^2-2ab\cos\gamma$, con $\gamma$ angolo tra i lati di lunghezza $a,b$. Il teorema dei seni esprime la proporzionalità tra lati e seni degli angoli opposti. Questi legami spiegano il passaggio fra lunghezze, angoli e prodotti scalari.

_(Accascina–Monti, § B.8, libro pp. 751–754; PDF pp. 767–770.)_

![[GEO-p767-1.png|650]]

**Lettura della figura (PDF p. 767, libro p. 751).** Il quadrilatero con diagonali e i triangoli introducono le proprietà metriche usate nei richiami: le ipotesi geometriche vanno lette prima di applicare le formule.

![[GEO-p768-1.png|650]]

**Lettura della figura (PDF p. 768, libro p. 752).** I triangoli con lati e angoli evidenziati accompagnano i teoremi metrici; la scelta di lato e angolo opposto è necessaria per usare seni e coseni correttamente.

![[GEO-p769-1.png|650]]

**Lettura della figura (PDF p. 769, libro p. 753).** I triangoli rettangoli e le costruzioni ausiliarie mostrano come ricondurre relazioni generali a proiezioni e applicazioni di Pitagora.

## B.9 - Distanze tra insiemi

Vedi [[GEO - Distanza tra insiemi]].

La distanza tra due insiemi si definisce tramite l’estremo inferiore delle distanze tra coppie di punti:

$$d(A,B)=\inf\{d(a,b):a\in A,\ b\in B\}.$$

Negli oggetti geometrici chiusi considerati nel corso, come rette e segmenti, il minimo nei casi studiati viene raggiunto. Per insiemi generici può non esserlo: due intervalli aperti adiacenti hanno distanza zero anche senza punti comuni.

Per un punto e una retta il minimo è raggiunto dal piede della perpendicolare; per rette parallele la separazione è costante lungo le perpendicolari.

_(Accascina–Monti, § B.9, libro pp. 754–756; PDF pp. 770–772.)_

![[GEO-p771-1.png|650]]

**Lettura della figura (PDF p. 771, libro p. 755).** Le proiezioni su rette mostrano i segmenti più corti fra punto e retta o fra rette parallele: sono quelli ortogonali alla direzione della retta.

## B.10 - Simmetrie

Vedi [[GEO - Simmetrie del piano]].

La simmetria centrale di centro $O$ manda $P$ nel punto $P'$ con $O$ punto medio di $PP'$. La simmetria assiale rispetto a $r$ manda $P$ nel punto per cui $r$ è asse perpendicolare del segmento $PP'$; i punti di $r$ restano fissi.

Entrambe conservano le distanze. In coordinate, una simmetria con centro nell’origine è $x\mapsto-x$; una simmetria rispetto all’asse $x$ è $(x,y)\mapsto(x,-y)$.

_(Accascina–Monti, § B.10, libro pp. 756–757; PDF pp. 772–773.)_

![[GEO-p772-1.png|650]]

**Lettura della figura (PDF p. 772, libro p. 756).** La prima costruzione conclude le distanze tra insiemi; le figure successive introducono la simmetria rispetto a un centro o a una retta.

## B.11 - Bisettrici

Vedi [[GEO - Bisettrici come luoghi geometrici]].

La bisettrice divide un angolo in due parti uguali. Il luogo dei punti equidistanti da due rette incidenti è l’unione delle due bisettrici, una per ciascuna coppia di angoli opposti al vertice.

Questa caratterizzazione per distanze permette di ricavarne le equazioni senza misurare direttamente gli angoli.

_(Accascina–Monti, § B.11, libro pp. 757–758; PDF pp. 773–774.)_

![[GEO-p773-1.png|650]]

**Lettura della figura (PDF p. 773, libro p. 757).** Le rette e i punti simmetrici mostrano la conservazione delle distanze e l’asse che divide un segmento ortogonalmente nel suo punto medio.

## B.12 - Circonferenze

Vedi [[GEO - Circonferenza euclidea]].

La circonferenza è il luogo dei punti a distanza fissata $R>0$ da un centro; il disco comprende anche i punti interni. Una retta può essere secante, tangente o esterna.

Il raggio al punto di tangenza è ortogonale alla tangente. L’asse di una corda passa per il centro. Nella geometria analitica queste proprietà diventano condizioni su distanze e prodotti scalari.

_(Accascina–Monti, § B.12, libro pp. 758–759; PDF pp. 774–775.)_

![[GEO-p774-1.png|650]]

**Lettura della figura (PDF p. 774, libro p. 758).** Le bisettrici dividono gli angoli in parti uguali; la circonferenza successiva è un luogo di punti equidistanti dal centro, distinto dal disco interno.

## B.13 - Punti notevoli dei triangoli

Vedi [[GEO - Punti notevoli di un triangolo]].

Le mediane di un triangolo concorrono nel baricentro, le bisettrici nell’incentro, gli assi dei lati nel circocentro e le altezze nell’ortocentro.

| Punto | Proprietà utile |
|---|---|
| Baricentro | $G=(A+B+C)/3$; divide ciascuna mediana nel rapporto $2:1$ |
| Incentro | Equidistante dai lati; centro della circonferenza inscritta |
| Circocentro | Equidistante dai vertici; centro della circonferenza circoscritta |
| Ortocentro | Intersezione delle altezze |

Incentro e baricentro sono interni; circocentro e ortocentro possono essere esterni nei triangoli ottusangoli.

_(Accascina–Monti, § B.13, libro pp. 759–764; PDF pp. 775–780.)_

![[GEO-p775-1.png|650]]

**Lettura della figura (PDF p. 775, libro p. 759).** Le tangenti e le corde visualizzano le relazioni tra raggio e retta tangente, e la caratterizzazione del centro mediante gli assi delle corde.

![[GEO-p776-1.png|650]]

**Lettura della figura (PDF p. 776, libro p. 760).** Le corde e gli angoli sulla circonferenza collegano angoli al centro e alla circonferenza; le costruzioni servono anche a riconoscere i luoghi dei centri.

![[GEO-p777-1.png|650]]

**Lettura della figura (PDF p. 777, libro p. 761).** Le linee notevoli del triangolo mostrano le concorrenze che definiscono incentro, baricentro e gli altri centri, ciascuno legato a una diversa famiglia di rette.

![[GEO-p778-1.png|650]]

**Lettura della figura (PDF p. 778, libro p. 762).** I triangoli finali confrontano posizioni dei punti notevoli in configurazioni diverse: alcuni centri possono trovarsi fuori dal triangolo.

## Ripasso attivo

- **Punti e rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Punti e rette euclidee]].
- **Semirette, segmenti e semipiani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Convessità e regioni del piano]].
- **Poligoni:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Poligoni e parallelogrammi]].
- **Distanze tra punti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanza euclidea e punto medio]].
- **Rette parallele:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Parallelismo euclideo nel piano]].
- **Angoli:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Angoli euclidei]].
- **Ortogonalità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Perpendicolari nel piano]].
- **Triangoli:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Teoremi sui triangoli]].
- **Distanze tra insiemi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanza tra insiemi]].
- **Simmetrie:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Simmetrie del piano]].
- **Bisettrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Bisettrici come luoghi geometrici]].
- **Circonferenze:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Circonferenza euclidea]].
- **Punti notevoli dei triangoli:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Punti notevoli di un triangolo]].

## Collegamenti

Precedente: [[A - GEO - Approfondimenti]] · Successiva: [[C - GEO - Richiami di geometria dello spazio]]

[[MOC - Geometria]]
