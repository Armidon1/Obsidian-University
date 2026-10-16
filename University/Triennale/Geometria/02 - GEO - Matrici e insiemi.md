---
title: "Matrici e insiemi"
aliases:
  - "GEO — Matrici e insiemi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "2"
pdf_pages: "41–52"
---

# Matrici e insiemi

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 2 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 2.1 - Matrici

Vedi [[GEO - Tipi di matrici]].

Una matrice $A=(a_{ij})\in M(p,q,\mathbb R)$ è una tabella di $p$ righe e $q$ colonne. L’indice $i$ individua la riga, $j$ la colonna. Due matrici sono uguali se hanno lo stesso tipo e coincidono elemento per elemento.

$$A=\begin{pmatrix}1&2&0\\-1&3&4\end{pmatrix}\in M(2,3,\mathbb R),\qquad a_{23}=4.$$

Una matrice quadrata ha tipo $(n,n)$. È triangolare superiore se $a_{ij}=0$ per $i>j$, inferiore se $a_{ij}=0$ per $i<j$, diagonale se $a_{ij}=0$ per $i\ne j$. È simmetrica se $a_{ij}=a_{ji}$.

Queste strutture saranno utili per leggere rapidamente determinanti, autovalori e proprietà geometriche.

_(Accascina–Monti, § 2.1, libro pp. 25–28; PDF pp. 41–44.)_

## 2.2 - Intersezione e unione di insiemi

Vedi [[GEO - Intersezione e unione di insiemi]].

L’intersezione $A\cap B$ raccoglie gli elementi comuni; l’unione $A\cup B$ quelli presenti in almeno uno dei due insiemi. Il simbolo $\varnothing$ indica l’insieme vuoto.

Per $A=\{1,2,3\}$ e $B=\{3,4\}$ si ha $A\cap B=\{3\}$ e $A\cup B=\{1,2,3,4\}$. La congiunzione logica “e” corrisponde all’intersezione, “o” inclusivo all’unione.

In un sistema, soddisfare tutte le equazioni significa appartenere all’intersezione dei rispettivi insiemi di soluzioni. La distinzione tornerà nello studio dei sottospazi: l’intersezione di sottospazi è un sottospazio, la loro unione in generale no.

_(Accascina–Monti, § 2.2, libro pp. 28–30; PDF pp. 44–46.)_

## 2.3 - Matrice trasposta

Vedi [[GEO - Matrice trasposta]].

La **trasposta** di $A$ si ottiene scambiando righe e colonne:

$$(A^T)_{ij}=a_{ji},\qquad A\in M(p,q,\mathbb R)\Rightarrow A^T\in M(q,p,\mathbb R).$$

Per la matrice precedente $A^T=\begin{pmatrix}1&-1\\2&3\\0&4\end{pmatrix}$. Trasporre due volte restituisce la matrice iniziale: $(A^T)^T=A$. Una matrice è simmetrica esattamente quando $A=A^T$.

> [!note] Notazione
> Nel libro la trasposta è spesso scritta ${}^tA$. Negli appunti si usa $A^T$: l’operazione è la stessa.

_(Accascina–Monti, § 2.3, libro pp. 30–32; PDF pp. 46–48.)_

## Ripasso attivo

- **Matrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Tipi di matrici]].
- **Intersezione e unione di insiemi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Intersezione e unione di insiemi]].
- **Matrice trasposta:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Matrice trasposta]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 35 (PDF p. 51). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[01 - GEO - Equazioni lineari e numeri]] · Successiva: [[03 - GEO - Lo spazio vettoriale delle matrici]]

[[MOC - Geometria]]
