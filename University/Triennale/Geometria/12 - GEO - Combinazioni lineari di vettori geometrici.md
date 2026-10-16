---
title: "Combinazioni lineari di vettori geometrici"
aliases:
  - "GEO — Combinazioni lineari di vettori geometrici"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "12"
pdf_pages: "199–208"
---

# Combinazioni lineari di vettori geometrici

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 12 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 12.1 - Combinazione lineare di vettori

Vedi [[GEO - Combinazioni lineari e geometria]].

Una combinazione lineare di $v_1,\ldots,v_r$ è un vettore $a_1v_1+\cdots+a_rv_r$, con coefficienti reali arbitrari. Geometricamente, i multipli di un vettore non nullo riempiono una retta per l’origine; le combinazioni di due vettori non paralleli riempiono il piano da essi individuato.

I vettori sono **linearmente indipendenti** se

$$a_1v_1+\cdots+a_rv_r=0\Rightarrow a_1=\cdots=a_r=0.$$

Sono dipendenti se esiste una relazione nulla con coefficienti non tutti nulli. Questo significa che almeno una delle direzioni proposte è ridondante.

| Ambiente | Interpretazione |
|---|---|
| Un vettore | Indipendente se e solo se non nullo |
| Due vettori | Dipendenti se e solo se paralleli |
| Tre vettori nello spazio | Dipendenti se e solo se complanari con l’origine |
| Piano | Al massimo due vettori indipendenti |
| Spazio | Al massimo tre vettori indipendenti |

> [!example] Generare senza ridondanza
> $u=(1,0)$ e $v=(1,1)$ non sono paralleli. Ogni $(x,y)$ si scrive $(x-y)u+yv$. Aggiungere $w=(2,1)=u+v$ non permette di raggiungere nuovi vettori: introduce la relazione $u+v-w=0$.

L’esistenza di una rappresentazione corrisponde al generare tutto l’ambiente; l’unicità dipende dall’indipendenza. La loro combinazione porterà alla nozione di base.

_(Accascina–Monti, § 12.1, libro pp. 183–189; PDF pp. 199–205.)_

![[GEO-p199-1.png|650]]

**Lettura della figura (PDF p. 199, libro p. 183).** Il parallelogramma rappresenta una combinazione di due direzioni: i coefficienti misurano i multipli dei due vettori sommati.

![[GEO-p202-1.png|650]]

**Lettura della figura (PDF p. 202, libro p. 186).** La costruzione per parallele mostra come esprimere un vettore mediante due direzioni indipendenti nel piano.

## Ripasso attivo

- **Combinazione lineare di vettori:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Combinazioni lineari e geometria]].

## Collegamenti

Precedente: [[11 - GEO - I vettori geometrici]] · Successiva: [[13 - GEO - Spazi vettoriali sui reali]]

[[MOC - Geometria]]
