---
title: "Autovalori e autovettori"
aliases:
  - "GEO — Autovalori e autovettori"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "31"
pdf_pages: "525–548"
---

# Autovalori e autovettori

> [!abstract] Scopo e percorso
> Autovalori e diagonalizzazione. Questa nota segue il capitolo 31 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 31.1 - Autovalori e autovettori

Vedi [[GEO - Autovalori autovettori e autospazi]].

Un autovettore è un vettore **non nullo** $v$ tale che $f(v)=\lambda v$. L’autovalore $\lambda$ misura la dilatazione o inversione lungo una direzione che l’applicazione non mescola con le altre.

L’autospazio è $E_\lambda=\ker(f-\lambda\operatorname{id})$. Contiene anche zero, che non è un autovettore. Lo zero è un autovalore esattamente quando il nucleo è non banale.

_(Accascina–Monti, § 31.1, libro pp. 509–512; PDF pp. 525–528.)_

## 31.2 - Polinomio caratteristico

Vedi [[GEO - Polinomio caratteristico]].

Per una matrice quadrata $A$ gli autovalori sono le radici reali del polinomio caratteristico

$$p_A(t)=\det(A-tI).$$

Questa è la convenzione del libro; usando $\det(tI-A)$ cambia solo un fattore $(-1)^n$, non le radici. Il criterio deriva dall’esistenza di soluzioni non nulle di $(A-\lambda I)v=0$.

Per $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$, $p_A(t)=(2-t)(3-t)$: gli autovalori sono $2$ e $3$. Una matrice reale può non avere autovalori reali: una rotazione di $90^\circ$ ha polinomio $t^2+1$.

_(Accascina–Monti, § 31.2, libro pp. 512–517; PDF pp. 528–533.)_

## 31.3 - Molteplicità di un autovalore

Vedi [[GEO - Molteplicità algebrica e geometrica]].

La molteplicità algebrica $m_a(\lambda)$ è il numero di volte che $\lambda$ compare come radice; quella geometrica è $m_g(\lambda)=\dim E_\lambda$.

$$1\le m_g(\lambda)\le m_a(\lambda).$$

L’autovalore ripetuto richiede un controllo dell’autospazio: per $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ l’unico autovalore è $1$ con molteplicità algebrica $2$, ma $(A-I)v=0$ impone $y=0$, quindi $m_g=1$.

_(Accascina–Monti, § 31.3, libro pp. 517–521; PDF pp. 533–537.)_

## 31.4 - Autovalori e autovettori di matrici

Vedi [[GEO - Calcolo degli autospazi]].

Il calcolo concreto procede in due fasi: prima si risolve $p_A(t)=0$, poi per ogni autovalore si risolve $(A-\lambda I)v=0$ e se ne trova una base.

Per $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ si ottiene $E_2=\langle(1,0)\rangle$ ed $E_3=\langle(1,1)\rangle$. Autovettori relativi ad autovalori distinti sono indipendenti.

Se $A$ rappresenta un endomorfismo in una base non canonica, le soluzioni trovate sono **coordinate** degli autovettori e vanno ricostruite nella base scelta.

_(Accascina–Monti, § 31.4, libro pp. 521–522; PDF pp. 537–538.)_

## Ripasso attivo

- **Autovalori e autovettori:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Autovalori autovettori e autospazi]].
- **Polinomio caratteristico:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Polinomio caratteristico]].
- **Molteplicità di un autovalore:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Molteplicità algebrica e geometrica]].
- **Autovalori e autovettori di matrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Calcolo degli autospazi]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 527 (PDF p. 543). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[30 - GEO - Endomorfismi]] · Successiva: [[32 - GEO - Diagonalizzazione]]

[[MOC - Geometria]]
