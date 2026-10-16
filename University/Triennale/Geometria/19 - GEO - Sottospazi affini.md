---
title: "Sottospazi affini"
aliases:
  - "GEO — Sottospazi affini"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "19"
pdf_pages: "307–320"
---

# Sottospazi affini

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 19 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 19.1 - Le rette del piano e dello spazio

Vedi [[GEO - Retta come traslazione]].

Una retta non deve passare per l’origine. Scelto un suo punto $P_0$ e un vettore direttore non nullo $v$, ogni punto ha forma $P_0+tv$. L’insieme delle differenze tra due suoi punti è la retta vettoriale $\langle v\rangle$.

La geometria affine separa quindi una **posizione**, fissata da $P_0$, da una **direzione**, fissata dal sottospazio. Cambiare $P_0$ con un altro punto della stessa retta non cambia la retta.

_(Accascina–Monti, § 19.1, libro pp. 291–293; PDF pp. 307–309.)_

![[GEO-p307-1.png|650]]

**Lettura della figura (PDF p. 307, libro p. 291).** Le rette parallele mostrano la traslazione da una retta affine alla sua direzione passante per l’origine.

## 19.2 - I piani dello spazio

Vedi [[GEO - Piano come traslazione]].

Un piano si descrive come $P_0+\langle u,v\rangle$, con $u,v$ indipendenti. Il piano direzionale passa per l’origine; il piano affine può essere traslato.

Per esempio $z=2$ ha direzione $z=0$. I punti $(0,0,2)$ e $(1,1,2)$ appartengono al piano affine, mentre la loro differenza $(1,1,0)$ appartiene al piano direzionale.

_(Accascina–Monti, § 19.2, libro pp. 293–294; PDF pp. 309–310.)_

![[GEO-p309-1.png|650]]

**Lettura della figura (PDF p. 309, libro p. 293).** I due piani paralleli distinguono i punti di un piano affine dai vettori del suo piano direzionale: le differenze tra punti appartengono alla direzione.

## 19.3 - Sottospazi affini

Vedi [[GEO - Sottospazio affine]].

Un sottospazio affine è una traslazione di un sottospazio vettoriale:

$$P_0+E=\{P_0+e:e\in E\}.$$

La sua dimensione è $\dim E$. Contiene l’origine se e solo se coincide con un sottospazio vettoriale. Il sottospazio direzionale $E$ è unico, mentre il punto base $P_0$ non lo è.

Per verificare che due descrizioni rappresentino lo stesso affine basta controllare che abbiano la stessa direzione e che la differenza dei punti base appartenga a tale direzione.

_(Accascina–Monti, § 19.3, libro pp. 294–296; PDF pp. 310–312.)_

## 19.4 - L’insieme delle soluzioni di un sistema

Vedi [[GEO - Soluzione particolare e omogeneo associato]].

Se $Ax=b$ è compatibile e $x_0$ è una soluzione particolare, allora

$$\operatorname{Sol}(Ax=b)=x_0+\operatorname{Sol}(Ax=0).$$

Infatti $Ax=b$ equivale a $A(x-x_0)=0$. La soluzione particolare fissa la posizione; il sistema omogeneo associato descrive tutte le variazioni possibili.

Per $x+y=2$, una soluzione particolare è $(2,0)$ e l’omogeneo è generato da $(-1,1)$: tutte le soluzioni sono $(2,0)+t(-1,1)$. La dimensione affine è il numero di incognite meno il rango. Se il sistema è incompatibile l’insieme vuoto non è un affine secondo la definizione adottata.

_(Accascina–Monti, § 19.4, libro pp. 296–301; PDF pp. 312–317.)_

## Ripasso attivo

- **Le rette del piano e dello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Retta come traslazione]].
- **I piani dello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Piano come traslazione]].
- **Sottospazi affini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Sottospazio affine]].
- **L’insieme delle soluzioni di un sistema:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Soluzione particolare e omogeneo associato]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 303 (PDF p. 319). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[18 - GEO - Intersezione e somma di sottospazi]] · Successiva: [[20 - GEO - Equazioni vettoriali di rette e piani]]

[[MOC - Geometria]]
