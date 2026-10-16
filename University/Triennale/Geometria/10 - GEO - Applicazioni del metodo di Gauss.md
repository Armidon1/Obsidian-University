---
title: "Applicazioni del metodo di Gauss"
aliases:
  - "GEO — Applicazioni del metodo di Gauss"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "10"
pdf_pages: "175–186"
---

# Applicazioni del metodo di Gauss

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 10 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 10.1 - Operazioni elementari

Vedi [[GEO - Operazioni elementari di riga]].

Nel capitolo il libro usa, per l’equivalenza per righe, scambi e somme di multipli di un’altra riga. Queste operazioni conservano il rango; per il determinante, lo scambio cambia segno e la somma lascia il valore invariato.

Si può anche riscalare una riga con un fattore non nullo per eseguire calcoli: il rango resta uguale, ma il determinante viene moltiplicato per quel fattore. È necessario registrarne l’effetto separatamente.

_(Accascina–Monti, § 10.1, libro pp. 159–161; PDF pp. 175–177.)_

## 10.2 - Calcolo del determinante

Vedi [[GEO - Determinante con Gauss]].

Per una matrice quadrata si esegue Gauss fino a ottenere una matrice triangolare $U$. Se sono state fatte soltanto somme di righe e $s$ scambi:

$$\det A=(-1)^s\prod_{i=1}^{n}u_{ii}.$$

Per $A=\begin{pmatrix}1&2&0\\2&5&1\\0&1&3\end{pmatrix}$, $R_2-2R_1$ produce $(0,1,1)$; $R_3-R_2$ produce $(0,0,2)$. Senza scambi, $\det A=1\cdot1\cdot2=2$.

Se si sono anche riscalate righe di fattori $c_1,\ldots,c_k\ne0$, vale $\det U=(-1)^s(c_1\cdots c_k)\det A$. Questa formula permette di recuperare il valore iniziale.

_(Accascina–Monti, § 10.2, libro pp. 161–163; PDF pp. 177–179.)_

## 10.3 - Calcolo del rango

Vedi [[GEO - Rango con Gauss]].

Il rango è il numero di righe non nulle di una forma a scalini, cioè il numero di pivot. Non si contano semplicemente gli elementi diagonali non nulli di una matrice rettangolare: i pivot possono trovarsi su colonne successive a quelle diagonali.

Per $A=\begin{pmatrix}1&2&3\\2&4&6\\0&1&1\end{pmatrix}$ la seconda riga è dipendente dalla prima, mentre la terza introduce un secondo pivot: $\operatorname{rk}A=2$.

> [!tip] Distinguere due calcoli
> Per classificare $Ax=b$ si riduce la completa e si confrontano i pivot nei coefficienti e nella completa. Il rango di $A$ va letto senza contare un eventuale pivot nella colonna dei termini noti.

_(Accascina–Monti, § 10.3, libro pp. 163–166; PDF pp. 179–182.)_

## Ripasso attivo

- **Operazioni elementari:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Operazioni elementari di riga]].
- **Calcolo del determinante:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Determinante con Gauss]].
- **Calcolo del rango:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Rango con Gauss]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 167 (PDF p. 183). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[09 - GEO - Metodo di Gauss]] · Successiva: [[11 - GEO - I vettori geometrici]]

[[MOC - Geometria]]
