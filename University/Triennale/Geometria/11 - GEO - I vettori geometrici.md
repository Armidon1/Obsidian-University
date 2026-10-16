---
title: "I vettori geometrici"
aliases:
  - "GEO — I vettori geometrici"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "11"
pdf_pages: "187–198"
---

# I vettori geometrici

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 11 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 11.1 - Vettori del piano

Vedi [[GEO - Vettori geometrici del piano]].

Fissata un’origine $O$, un vettore geometrico applicato è la coppia di punti $(O,P)$, rappresentata dalla freccia $\overrightarrow{OP}$. Si distinguono direzione, verso e lunghezza. Il vettore nullo è $\overrightarrow{OO}$; non ha una direzione privilegiata.

L’insieme dei vettori del piano con origine $O$ è $V^2(O)$. L’origine comune permette di definire operazioni confrontando le frecce nello stesso spazio.

_(Accascina–Monti, § 11.1, libro pp. 171–172; PDF pp. 187–188.)_

![[GEO-p187-1.png|650]]

**Lettura della figura (PDF p. 187, libro p. 171).** Le frecce con origine comune distinguono posizione del vertice, direzione e verso. Il vettore nullo ha vertice coincidente con l’origine.

## 11.2 - Addizione di vettori

Vedi [[GEO - Somma e differenza di vettori]].

La somma si costruisce con la regola del parallelogramma o trasportando la seconda freccia alla fine della prima. Se $u=\overrightarrow{OA}$ e $v=\overrightarrow{OB}$, il vertice opposto a $O$ del parallelogramma rappresenta $u+v$.

L’opposto $-u$ ha la stessa lunghezza e verso contrario. La differenza $v-u$ rappresenta lo spostamento da $A$ a $B$, trasportato nell’origine: $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$. Non si devono confondere punti e spostamenti.

_(Accascina–Monti, § 11.2, libro pp. 172–175; PDF pp. 188–191.)_

![[GEO-p188-1.png|650]]

**Lettura della figura (PDF p. 188, libro p. 172).** I parallelogrammi e gli allineamenti mostrano la somma e le configurazioni degeneri. La diagonale uscente dall’origine rappresenta il vettore somma.

![[GEO-p189-1.png|650]]

**Lettura della figura (PDF p. 189, libro p. 173).** Le costruzioni confrontano le due disposizioni degli addendi e gli spostamenti lungo una retta: il risultato della somma non dipende dall’ordine.

![[GEO-p190-1.png|650]]

**Lettura della figura (PDF p. 190, libro p. 174).** Le frecce opposte e il parallelogramma illustrano la cancellazione e la costruzione della differenza; un verso invertito corrisponde a un coefficiente negativo.

## 11.3 - Moltiplicazione di un vettore per uno scalare

Vedi [[GEO - Multipli di un vettore geometrico]].

Il vettore $ku$ ha lunghezza $|k|$ volte quella di $u$; mantiene il verso se $k>0$, lo inverte se $k<0$, è nullo se $k=0$. Anche $k0=0$.

Somma e prodotto per scalare soddisfano associatività, commutatività della somma, esistenza di zero e opposto, distributività e compatibilità $h(ku)=(hk)u$. Sono le stesse proprietà già incontrate per le matrici.

_(Accascina–Monti, § 11.3, libro pp. 175–176; PDF pp. 191–192.)_

![[GEO-p191-1.png|650]]

**Lettura della figura (PDF p. 191, libro p. 175).** I vettori allineati illustrano il prodotto per uno scalare: il segno governa il verso e il valore assoluto governa la lunghezza.

## 11.4 - Vettori dello spazio

Vedi [[GEO - Vettori geometrici dello spazio]].

Nello spazio tridimensionale si definisce analogamente $V^3(O)$. Le costruzioni con parallelogrammi restano valide, perché due vettori non paralleli individuano un piano. Il cambiamento di ambiente aumenta le direzioni indipendenti disponibili, senza cambiare le regole algebriche.

_(Accascina–Monti, § 11.4, libro pp. 176–177; PDF pp. 192–193.)_

## 11.5 - Rette e piani per l’origine

Vedi [[GEO - Direzioni per l’origine]].

I vettori con vertice su una retta passante per $O$ restano su quella retta dopo somme e prodotti per scalare. Lo stesso vale per i vettori con vertice in un piano per $O$.

Questa chiusura anticipa i sottospazi vettoriali. Una retta che non passa per $O$ non contiene il vettore nullo e non può avere la stessa struttura con le operazioni usuali: sarà invece un oggetto affine.

_(Accascina–Monti, § 11.5, libro pp. 177–178; PDF pp. 193–194.)_

## 11.6 - Punto medio

Vedi [[GEO - Punto medio vettoriale]].

Se $M$ è il punto medio di $A$ e $B$:

$$\overrightarrow{OM}=\frac12\left(\overrightarrow{OA}+\overrightarrow{OB}\right).$$

Il fattore $1/2$ prende la media dei due vettori posizione. In coordinate, $A=(1,2)$ e $B=(5,4)$ danno $M=(3,3)$; infatti $M-A=(2,1)=B-M$.

_(Accascina–Monti, § 11.6, libro pp. 178–179; PDF pp. 194–195.)_

## Figure del riepilogo e degli esercizi

Queste pagine conservano le figure riprese nel sunto o nelle soluzioni degli esercizi, nell’ordine del libro. Le ripetizioni del materiale originale sono mantenute per collegare definizioni e applicazioni.

![[GEO-p195-1.png|650]]

**Lettura della figura (PDF p. 195, libro p. 179).** La costruzione nel triangolo visualizza la media di due vettori posizione e il punto medio del lato opposto all’origine.

![[GEO-p196-1.png|650]]

**Lettura della figura (PDF p. 196, libro p. 180).** Le figure del riepilogo riprendono vettori applicati e regola del parallelogramma, collegando le definizioni alle operazioni appena studiate.

## Ripasso attivo

- **Vettori del piano:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Vettori geometrici del piano]].
- **Addizione di vettori:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Somma e differenza di vettori]].
- **Moltiplicazione di un vettore per uno scalare:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Multipli di un vettore geometrico]].
- **Vettori dello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Vettori geometrici dello spazio]].
- **Rette e piani per l’origine:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Direzioni per l’origine]].
- **Punto medio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Punto medio vettoriale]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 182 (PDF p. 198). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[10 - GEO - Applicazioni del metodo di Gauss]] · Successiva: [[12 - GEO - Combinazioni lineari di vettori geometrici]]

[[MOC - Geometria]]
