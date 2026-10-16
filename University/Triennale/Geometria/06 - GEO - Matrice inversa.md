---
title: "Matrice inversa"
aliases:
  - "GEO — Matrice inversa"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "6"
pdf_pages: "103–122"
---

# Matrice inversa

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 6 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 6.1 - Matrice unità

Vedi [[GEO - Matrice identità]].

La matrice identità $I_n$ ha $1$ sulla diagonale e $0$ altrove. È l’elemento neutro del prodotto: per $A$ di tipo $(p,q)$, $I_pA=A$ e $AI_q=A$.

La dimensione dell’identità dipende quindi dal lato del prodotto. Questo controllo evita espressioni formalmente scorrette con matrici rettangolari.

_(Accascina–Monti, § 6.1, libro pp. 87–89; PDF pp. 103–105.)_

## 6.2 - Matrice inversa

Vedi [[GEO - Matrice inversa]].

Una matrice quadrata $A$ è invertibile se esiste $B$ tale che $AB=BA=I$. L’inversa è unica e si indica $A^{-1}$. Il criterio decisivo è

$$A\text{ invertibile}\iff\det A\ne0.$$

La formula generale è $A^{-1}=\operatorname{adj}(A)/\det A$, dove la matrice aggiunta è la **trasposta** della matrice dei cofattori. In ordine due:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

Per $A=\begin{pmatrix}1&2\\3&5\end{pmatrix}$ risulta $\det A=-1$ e $A^{-1}=\begin{pmatrix}-5&2\\3&-1\end{pmatrix}$; il prodotto con $A$ dà $I_2$.

_(Accascina–Monti, § 6.2, libro pp. 89–92; PDF pp. 105–108.)_

## 6.3 - Proprietà dell’inversa

Vedi [[GEO - Proprietà della matrice inversa]].

Per matrici invertibili valgono

$$(A^{-1})^{-1}=A,\qquad(AB)^{-1}=B^{-1}A^{-1},\qquad(A^T)^{-1}=(A^{-1})^T,\qquad\det A^{-1}=\frac1{\det A}.$$

L’ordine nell’inversa di un prodotto si inverte: $(AB)(B^{-1}A^{-1})=AIA^{-1}=I$. Se $A$ è invertibile, $AB=AC$ implica $B=C$ moltiplicando a sinistra per $A^{-1}$.

> [!important] Il lato conta
> Da $AX=B$ si ottiene $X=A^{-1}B$; da $XA=B$ si ottiene $X=BA^{-1}$. Non si può spostare l’inversa liberamente.

_(Accascina–Monti, § 6.3, libro pp. 92–94; PDF pp. 108–110.)_

## 6.4 - Teorema di Cramer

Vedi [[GEO - Teorema di Cramer]].

Un sistema quadrato $Ax=b$ con $\det A\ne0$ ha un’unica soluzione $x=A^{-1}b$. Il teorema di Cramer la esprime come

$$x_i=\frac{\det A^{(i)}}{\det A},$$

dove $A^{(i)}$ sostituisce la colonna $i$ con $b$. Per $x+2y=4$, $x+5y=6$ si hanno $\det A=3$, $\det A^{(1)}=8$, $\det A^{(2)}=2$: dunque $(x,y)=(8/3,2/3)$.

Se $\det A=0$ Cramer non si applica: il sistema può avere nessuna o infinite soluzioni. Serviranno rango e teorema di Rouché-Capelli.

_(Accascina–Monti, § 6.4, libro pp. 94–97; PDF pp. 110–113.)_

## Ripasso attivo

- **Matrice unità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Matrice identità]].
- **Matrice inversa:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Matrice inversa]].
- **Proprietà dell’inversa:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proprietà della matrice inversa]].
- **Teorema di Cramer:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Teorema di Cramer]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 100 (PDF p. 116). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[05 - GEO - Determinanti]] · Successiva: [[07 - GEO - Rango di una matrice]]

[[MOC - Geometria]]

La nota esistente [[Invertible Matrix]] offre un ripasso in inglese sull’invertibilità.
