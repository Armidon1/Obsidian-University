---
title: "Approfondimenti"
aliases:
  - "GEO — Approfondimenti"
tags:
  - geometria
  - appendice
source: "pdf/Geometria.pdf"
chapter: "A"
pdf_pages: "729–754"
---

# Approfondimenti

> [!abstract] Scopo e percorso
> Appendici. Questa nota segue il capitolo A del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## A.1 - Equazioni lineari e numeri

Vedi [[GEO - Dimostrazione dell’equivalenza dei sistemi]].

Le operazioni elementari sui sistemi conservano le soluzioni per due motivi: una soluzione delle equazioni iniziali soddisfa anche ogni loro combinazione lineare; inoltre ogni operazione ammessa è reversibile.

Per $E_i\leftarrow E_i+kE_j$, con $i\ne j$, l’inversa è $E_i\leftarrow E_i-kE_j$. Per $E_i\leftarrow cE_i$, con $c\ne0$, l’inversa usa $1/c$. Lo scambio si inverte ripetendo lo stesso scambio. Aggiungere un’identità non impone nuovi vincoli; eliminarla non ne perde.

Per dimostrare l’uguaglianza degli insiemi delle soluzioni servono entrambe le inclusioni: mostrare che le soluzioni iniziali soddisfano le nuove equazioni, da solo, non esclude soluzioni aggiuntive.

_(Accascina–Monti, § A.1, libro pp. 713–715; PDF pp. 729–731.)_

## A.4 - Moltiplicazione tra matrici

Vedi [[GEO - Dimostrazione dell’associatività matriciale]].

L’associatività del prodotto matriciale si verifica confrontando ogni posizione dei due prodotti. Per dimensioni compatibili:

$$((AB)C)_{i\ell}=\sum_k\left(\sum_j a_{ij}b_{jk}\right)c_{k\ell}=\sum_j\sum_k a_{ij}b_{jk}c_{k\ell}=(A(BC))_{i\ell}.$$

La dimostrazione usa distributività e possibilità di riordinare somme finite. Le dimensioni di entrambi i risultati coincidono. Non viene scambiato l’ordine dei fattori: associatività e commutatività sono proprietà differenti.

_(Accascina–Monti, § A.4, libro pp. 715–717; PDF pp. 731–733.)_

## A.5 - Determinanti

Vedi [[GEO - Multilinearità e alternanza del determinante]].

Le dimostrazioni sui determinanti partono dalla definizione ricorsiva e verificano, per induzione sull’ordine, che lo sviluppo lungo righe o colonne diverse dia lo stesso numero. Da qui si ricavano le proprietà operative.

La **multilinearità** significa linearità in una singola riga, a parità delle altre. Se una riga è $u+kv$:

$$\det(\ldots,u+kv,\ldots)=\det(\ldots,u,\ldots)+k\det(\ldots,v,\ldots).$$

L’alternanza cambia il segno quando si scambiano due righe e annulla il determinante se due righe coincidono. Sommare a una riga un multiplo di un’altra non cambia il determinante: il termine aggiuntivo ha due righe uguali.

Queste proprietà spiegano perché Gauss è adatto al calcolo del determinante e perché il fattore di riscalamento di tutta la matrice è $k^n$, con un fattore $k$ proveniente da ciascuna riga.

_(Accascina–Monti, § A.5, libro pp. 717–725; PDF pp. 733–741.)_

## A.6 - Matrice inversa

Vedi [[GEO - Dimostrazione del criterio di invertibilità]].

Se $A$ è invertibile, Binet dà $1=\det I=\det A\det A^{-1}$, dunque $\det A\ne0$.

Per il viceversa si costruisce $B=\operatorname{adj}(A)/\det A$. Nel prodotto $AB$, gli elementi diagonali valgono $1$ per lo sviluppo di Laplace. Gli elementi fuori diagonale valgono zero perché corrispondono allo sviluppo del determinante di una matrice con due righe uguali. Analogamente $BA=I$.

Questo dimostra insieme il criterio di invertibilità e la formula per l’inversa. Lo scambio degli indici nei cofattori, cioè la trasposizione della loro matrice, è necessario perché il prodotto ricostruisca gli sviluppi corretti.

_(Accascina–Monti, § A.6, libro pp. 725–728; PDF pp. 741–744.)_

## A.10 - Applicazioni del metodo di Gauss

Vedi [[GEO - Invarianza del rango per operazioni di riga]].

L’invarianza del determinante sotto $R_i\leftarrow R_i+kR_j$ segue dalla linearità nella riga modificata e dal fatto che il termine aggiuntivo ha righe proporzionali.

L’invarianza del rango sotto operazioni elementari si può comprendere osservando che le nuove righe sono combinazioni delle vecchie e, per reversibilità, le vecchie sono combinazioni delle nuove. Lo spazio generato dalle righe coincide quindi prima e dopo: non si guadagnano né perdono vincoli indipendenti.

Da qui segue che il rango della forma a scalini, dato dal numero delle righe non nulle, è il rango della matrice originale.

_(Accascina–Monti, § A.10, libro pp. 728–731; PDF pp. 744–747.)_

## A.17 - Basi di spazi vettoriali

Vedi [[GEO - Lemma del completamento]].

Il lemma del completamento permette di estendere una famiglia indipendente a una base. Partendo da una base già nota, si inserisce un vettore indipendente e si elimina un vettore vecchio che esso rende ridondante; si ripete.

Il passaggio essenziale è questo: scrivendo il nuovo vettore nella base corrente, almeno uno dei coefficienti dei vettori non ancora sostituiti deve essere non nullo. Altrimenti il nuovo vettore sarebbe combinazione di quelli già inseriti, contro l’indipendenza.

Isolando il vettore vecchio con coefficiente non nullo, si mostra che la famiglia dopo la sostituzione genera ancora tutto lo spazio. La stessa relazione permette di verificare che rimane indipendente.

_(Accascina–Monti, § A.17, libro pp. 731–733; PDF pp. 747–749.)_

## A.18 - Intersezione e somma di sottospazi

Vedi [[GEO - Dimostrazione della formula di Grassmann]].

Per dimostrare Grassmann si sceglie una base $u_1,\ldots,u_r$ di $E\cap F$, completandola a una base di $E$ con $e_1,\ldots,e_{p-r}$ e a una base di $F$ con $f_1,\ldots,f_{q-r}$.

La famiglia unita, contando i vettori $u_i$ una sola volta, genera $E+F$. È anche indipendente: in una relazione nulla, la combinazione dei vettori $f_j$ è uguale a una combinazione di vettori di $E$, dunque appartiene all’intersezione. L’indipendenza della base di $F$ annulla prima i coefficienti dei $f_j$, poi quella della base di $E$ annulla i rimanenti.

Il conteggio dà $r+(p-r)+(q-r)=p+q-r$, cioè

$$\dim(E+F)=\dim E+\dim F-\dim(E\cap F).$$

_(Accascina–Monti, § A.18, libro pp. 733–735; PDF pp. 749–751.)_

## A.32 - Diagonalizzazione

Vedi [[GEO - Indipendenza degli autospazi distinti]].

Le basi di autospazi associati ad autovalori distinti, unite, sono indipendenti. La dimostrazione procede per induzione sul numero di autovalori.

In una relazione nulla tra vettori degli autospazi si applica $f-\lambda_1\operatorname{id}$. I termini del primo autospazio scompaiono; quelli degli altri vengono moltiplicati per $\lambda_i-\lambda_1\ne0$. Per l’ipotesi induttiva tutti i loro coefficienti sono nulli. Nella relazione iniziale restano solo i vettori della base del primo autospazio, quindi anche i loro coefficienti si annullano.

Questo giustifica il criterio della somma delle dimensioni degli autospazi per la diagonalizzabilità.

_(Accascina–Monti, § A.32, libro pp. 735–737; PDF pp. 751–753.)_

## A.38 - Prodotto scalare in Rn

Vedi [[GEO - Dimostrazioni di Schwarz e della triangolare]].

Per Cauchy-Schwarz, se $u=0$ la tesi è immediata. Se $u\ne0$, per ogni $t\in\mathbb R$:

$$0\le\|tu+v\|^2=\|u\|^2t^2+2\langle u,v\rangle t+\|v\|^2.$$

Un trinomio con coefficiente principale positivo, non negativo per ogni $t$, ha discriminante non positivo. Quindi $\langle u,v\rangle^2\le\|u\|^2\|v\|^2$, da cui la disuguaglianza.

La triangolare si ricava sviluppando $\|u+v\|^2$ e usando Schwarz:

$$\|u+v\|^2\le\|u\|^2+2\|u\|\|v\|+\|v\|^2=(\|u\|+\|v\|)^2.$$

Estraendo le radici, essendo entrambi i membri non negativi, si ottiene $\|u+v\|\le\|u\|+\|v\|$.

_(Accascina–Monti, § A.38, libro pp. 737–738; PDF pp. 753–754.)_

## Ripasso attivo

- **Equazioni lineari e numeri:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimostrazione dell’equivalenza dei sistemi]].
- **Moltiplicazione tra matrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimostrazione dell’associatività matriciale]].
- **Determinanti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Multilinearità e alternanza del determinante]].
- **Matrice inversa:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimostrazione del criterio di invertibilità]].
- **Applicazioni del metodo di Gauss:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Invarianza del rango per operazioni di riga]].
- **Basi di spazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Lemma del completamento]].
- **Intersezione e somma di sottospazi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimostrazione della formula di Grassmann]].
- **Diagonalizzazione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Indipendenza degli autospazi distinti]].
- **Prodotto scalare in Rn:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimostrazioni di Schwarz e della triangolare]].

## Collegamenti

Precedente: [[40 - GEO - Geometria in Rn]] · Successiva: [[B - GEO - Richiami di geometria del piano]]

[[MOC - Geometria]]
