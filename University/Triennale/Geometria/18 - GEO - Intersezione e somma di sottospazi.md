---
title: "Intersezione e somma di sottospazi"
aliases:
  - "GEO — Intersezione e somma di sottospazi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "18"
pdf_pages: "279–306"
---

# Intersezione e somma di sottospazi

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 18 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 18.1 - Intersezione di sottospazi vettoriali

Vedi [[GEO - Intersezione di sottospazi]].

L’intersezione $E\cap F$ di sottospazi è un sottospazio, perché le combinazioni lineari restano sia in $E$ sia in $F$.

Se $E$ e $F$ sono dati da equazioni, per l’intersezione si mettono insieme tutti i vincoli. Se sono dati da generatori, si impone $\sum_i a_iu_i=\sum_j b_jv_j$ e si risolve rispetto ai coefficienti.

Per $E=\{(x,y,z):z=0\}$ e $F=\{(x,y,z):y=0\}$, l’intersezione è l’asse $x$, generato da $(1,0,0)$.

_(Accascina–Monti, § 18.1, libro pp. 263–265; PDF pp. 279–281.)_

## 18.2 - Somma di sottospazi vettoriali

Vedi [[GEO - Somma di sottospazi e Grassmann]].

La somma è

$$E+F=\{e+f:e\in E,\ f\in F\}.$$

È il più piccolo sottospazio contenente entrambi. Se sono noti generatori di $E$ e $F$, la loro unione genera $E+F$. L’unione insiemistica $E\cup F$, invece, in generale non è un sottospazio.

La formula di Grassmann misura le direzioni contate due volte:

$$\dim(E+F)=\dim E+\dim F-\dim(E\cap F).$$

Per i due piani coordinati precedenti, $\dim(E+F)=2+2-1=3$: la loro somma è $\mathbb R^3$.

_(Accascina–Monti, § 18.2, libro pp. 265–271; PDF pp. 281–287.)_

## 18.3 - Somma diretta di sottospazi

Vedi [[GEO - Somma diretta]].

La somma è diretta, indicata $E\oplus F$, se $E\cap F=\{0\}$. In tal caso ogni vettore della somma ha un’unica decomposizione $v=e+f$.

Infatti, se $e+f=e'+f'$, allora $e-e'=f'-f\in E\cap F$, dunque $e=e'$ e $f=f'$. Viceversa, un vettore comune non nullo avrebbe due decomposizioni.

Per $E=\langle(1,0,0),(0,1,0)\rangle$ e $F=\langle(0,0,1)\rangle$ vale $\mathbb R^3=E\oplus F$. Le dimensioni si sommano e le basi dei due sottospazi si concatenano.

_(Accascina–Monti, § 18.3, libro pp. 271–275; PDF pp. 287–291.)_

## Ripasso attivo

- **Intersezione di sottospazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Intersezione di sottospazi]].
- **Somma di sottospazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Somma di sottospazi e Grassmann]].
- **Somma diretta di sottospazi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Somma diretta]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 279 (PDF p. 295). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[17 - GEO - Basi di spazi vettoriali]] · Successiva: [[19 - GEO - Sottospazi affini]]

[[MOC - Geometria]]
