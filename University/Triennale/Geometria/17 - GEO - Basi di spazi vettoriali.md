---
title: "Basi di spazi vettoriali"
aliases:
  - "GEO — Basi di spazi vettoriali"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "17"
pdf_pages: "251–278"
---

# Basi di spazi vettoriali

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 17 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 17.1 - Basi

Vedi [[GEO - Basi e coordinate]].

Una base è una famiglia **generatrice e linearmente indipendente**. Ogni vettore si scrive in un unico modo come combinazione dei vettori di base:

$$v=x_1e_1+\cdots+x_ne_n,\qquad[v]_{\mathcal B}=(x_1,\ldots,x_n)^T.$$

L’esistenza deriva dal generare; l’unicità dall’indipendenza: sottraendo due rappresentazioni si ottiene una combinazione nulla e quindi tutti i coefficienti corrispondenti coincidono.

In $\mathbb R^n$ la base canonica è $(e_1,\ldots,e_n)$. In $M(p,q,\mathbb R)$ è costituita dalle matrici $E_{ij}$ con un unico $1$. Nei polinomi di grado minore di $n$, è $1,x,\ldots,x^{n-1}$.

Per $\mathcal B=((1,0),(1,1))$, il vettore $(3,2)$ ha coordinate $(1,2)$ perché $(3,2)=1(1,0)+2(1,1)$. Vettore e coordinate coincidono numericamente solo nella base canonica.

_(Accascina–Monti, § 17.1, libro pp. 235–239; PDF pp. 251–255.)_

## 17.2 - Dimensione

Vedi [[GEO - Dimensione di uno spazio vettoriale]].

Tutte le basi di uno spazio finitamente generato hanno lo stesso numero di vettori, chiamato dimensione. Quindi $\dim\mathbb R^n=n$, $\dim M(p,q,\mathbb R)=pq$ e $\dim\mathbb R_n[x]=n$ secondo la convenzione del libro.

In uno spazio di dimensione $n$, ogni famiglia indipendente ha al massimo $n$ elementi e ogni famiglia generatrice ne ha almeno $n$. Una famiglia di esattamente $n$ vettori è una base appena si verifica una delle due proprietà. Lo spazio $\{0\}$ ha dimensione zero e base vuota.

_(Accascina–Monti, § 17.2, libro pp. 239–241; PDF pp. 255–257.)_

## 17.3 - Una base per Sol(SO)

Vedi [[GEO - Base di un sistema omogeneo]].

Se $A$ ha $q$ colonne e rango $r$, lo spazio delle soluzioni di $Ax=0$ ha dimensione $q-r$. Dopo Gauss si assegnano parametri alle variabili libere e si raccoglie:

$$x=t_1u_1+\cdots+t_{q-r}u_{q-r}.$$

I vettori ottenuti mettendo un parametro alla volta uguale a $1$ e gli altri a $0$ costituiscono una base. Per $x+y+z=0$:

$$x=(-s-t,s,t)=s(-1,1,0)+t(-1,0,1).$$

I due vettori sono indipendenti e la dimensione è $3-1=2$.

_(Accascina–Monti, § 17.3, libro pp. 241–244; PDF pp. 257–260.)_

## 17.4 - Dimensioni di sottospazi vettoriali

Vedi [[GEO - Dimensione dei sottospazi]].

Se $E\subseteq V$ è un sottospazio e $\dim V=n$, allora $\dim E\le n$. Se le dimensioni sono uguali, $E=V$. Una base di un sottospazio può essere completata a una base dell’ambiente.

Il numero di equazioni scritte non coincide necessariamente con la codimensione: per $E=\operatorname{Sol}(Ax=0)$ è il **rango** dei vincoli a determinare $\dim E=q-r$, perché alcune equazioni possono essere ridondanti.

_(Accascina–Monti, § 17.4, libro pp. 244–246; PDF pp. 260–262.)_

## 17.5 - Calcolo di dimensioni e basi

Vedi [[GEO - Estrazione di una base]].

Per estrarre una base da generatori in coordinate, si dispongono come colonne di $A$, si esegue Gauss e si prendono le colonne **della matrice iniziale** nelle posizioni dei pivot. Il loro numero è $\operatorname{rk}A$.

Per $u=(1,0,1)$, $v=(0,1,1)$, $w=(1,1,2)=u+v$, una base dello span è $(u,v)$ e la dimensione è $2$.

> [!warning] Colonne e righe
> Le operazioni di riga conservano le relazioni di dipendenza tra colonne, ma possono cambiare lo spazio da esse generato nell’ambiente. Per una base dello spazio delle colonne bisogna selezionare le colonne originali.

Per passare da equazioni a generatori si risolve un sistema omogeneo; per passare da generatori a equazioni si impone che un vettore generico appartenga al loro span e si eliminano i parametri.

_(Accascina–Monti, § 17.5, libro pp. 246–249; PDF pp. 262–265.)_

## Ripasso attivo

- **Basi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Basi e coordinate]].
- **Dimensione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimensione di uno spazio vettoriale]].
- **Una base per Sol(SO):** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Base di un sistema omogeneo]].
- **Dimensioni di sottospazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dimensione dei sottospazi]].
- **Calcolo di dimensioni e basi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Estrazione di una base]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 254 (PDF p. 270). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[16 - GEO - Dipendenza e indipendenza lineare]] · Successiva: [[18 - GEO - Intersezione e somma di sottospazi]]

[[MOC - Geometria]]
