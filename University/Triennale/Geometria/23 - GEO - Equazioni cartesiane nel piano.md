---
title: "Equazioni cartesiane nel piano"
aliases:
  - "GEO — Equazioni cartesiane nel piano"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "23"
pdf_pages: "361–396"
---

# Equazioni cartesiane nel piano

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 23 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 23.1 - Equazioni cartesiane di rette

Vedi [[GEO - Equazione cartesiana della retta]].

Una retta nel piano ha equazione $ax+by+c=0$, con $(a,b)\ne(0,0)$. Moltiplicare tutti i coefficienti per uno stesso numero non nullo lascia invariata la retta. Un direttore è $v=(-b,a)$.

La condizione esclude $0x+0y+c=0$, che descrive il piano intero se $c=0$ e l’insieme vuoto se $c\ne0$.

_(Accascina–Monti, § 23.1, libro pp. 345–347; PDF pp. 361–363.)_

## 23.2 - Equazione cartesiana ed equazioni parametriche

Vedi [[GEO - Passaggio tra forme di una retta]].

Per passare alle parametriche si trova un punto $P_0$ e si usa $(-b,a)$. Viceversa, da $(x,y)=(x_0,y_0)+t(l,m)$ si elimina $t$ ottenendo

$$m(x-x_0)-l(y-y_0)=0.$$

La forma evita divisioni per componenti eventualmente nulle. Da $(x,y)=(1,2)+t(2,-1)$ si ottiene $x+2y-5=0$.

_(Accascina–Monti, § 23.2, libro pp. 347–350; PDF pp. 363–366.)_

## 23.3 - Retta passante per due punti

Vedi [[GEO - Retta per due punti]].

Per due punti distinti $P_0=(x_0,y_0)$ e $P_1=(x_1,y_1)$, la condizione è

$$\det\begin{pmatrix}x-x_0&y-y_0\\x_1-x_0&y_1-y_0\end{pmatrix}=0.$$

Esprime la dipendenza dei vettori $P-P_0$ e $P_1-P_0$. Per $(1,2)$ e $(3,1)$ si ottiene $-(x-1)-2(y-2)=0$, cioè $x+2y-5=0$. Entrambi i punti soddisfano l’equazione.

_(Accascina–Monti, § 23.3, libro pp. 350–352; PDF pp. 366–368.)_

## 23.4 - Intersezione di rette

Vedi [[GEO - Intersezione di rette cartesiane]].

Si risolve il sistema delle due equazioni. Indicando con $A$ la matrice dei coefficienti in $x,y$ e con $[A\mid-c]$ la completa:

| Ranghi | Posizione |
|---|---|
| $\operatorname{rk}A=2$ | Incidenti, un punto |
| $\operatorname{rk}A=1$, completa di rango $2$ | Parallele distinte |
| Entrambe di rango $1$ | Coincidenti |

Per $x+y=1$ e $x-y=3$, sommando si ottiene $x=2$ e quindi $y=-1$.

_(Accascina–Monti, § 23.4, libro pp. 352–354; PDF pp. 368–370.)_

## 23.5 - Fasci di rette

Vedi [[GEO - Fasci di rette]].

Le rette $ax+by+k=0$, al variare di $k$, formano un fascio di parallele. Se $r=0$ e $s=0$ sono due rette incidenti in $P$, tutte le rette per $P$ si ottengono con

$$hr+ks=0,\qquad(h,k)\ne(0,0).$$

La forma con due coefficienti include anche la retta $s=0$, che la sola scrittura $r+\lambda s=0$ omette. Per imporre il passaggio per un altro punto si sostituiscono le sue coordinate e si ricava il rapporto fra $h$ e $k$.

_(Accascina–Monti, § 23.5, libro pp. 354–358; PDF pp. 370–374.)_

## 23.6 - Semipiani

Vedi [[GEO - Semipiani cartesiani]].

I due semipiani aperti delimitati da $ax+by+c=0$ sono descritti da $ax+by+c>0$ e $ax+by+c<0$. Per includere il bordo si usano $\ge0$ e $\le0$.

Un punto di prova permette di riconoscere il lato. Per $x+2y-5=0$, l’origine dà $-5<0$ e appartiene al semipiano negativo. Un sistema di disequazioni descrive l’intersezione dei semipiani: i disegni nelle soluzioni del capitolo mostrano come si restringa la regione ammissibile vincolo dopo vincolo.

_(Accascina–Monti, § 23.6, libro pp. 358–360; PDF pp. 374–376.)_

## Figure del riepilogo e degli esercizi

Queste pagine conservano le figure riprese nel sunto o nelle soluzioni degli esercizi, nell’ordine del libro. Le ripetizioni del materiale originale sono mantenute per collegare definizioni e applicazioni.

![[GEO-p386-1.png|650]]

**Lettura della figura (PDF p. 386, libro p. 370).** Il disegno riunisce le rette di confine usate negli esercizi: si determinano prima intersezioni e direzioni, poi si selezionano i lati richiesti.

![[GEO-p387-1.png|650]]

**Lettura della figura (PDF p. 387, libro p. 371).** Le regioni grigie selezionano semipiani rispetto alle rette di confine. Un punto di prova stabilisce quale segno della disequazione corrisponde al lato colorato.

![[GEO-p388-1.png|650]]

**Lettura della figura (PDF p. 388, libro p. 372).** I semipiani evidenziati sono confrontati con le altre rette del sistema: la soluzione comune richiede che tutti i vincoli risultino verificati insieme.

![[GEO-p389-1.png|650]]

**Lettura della figura (PDF p. 389, libro p. 373).** Le figure proseguono l’intersezione dei semipiani: a ogni vincolo si conserva soltanto la parte di regione già ammissibile che soddisfa anche la nuova disequazione.

![[GEO-p390-1.png|650]]

**Lettura della figura (PDF p. 390, libro p. 374).** Le zone angolari visualizzano intersezioni di semipiani non paralleli. I vertici candidati si ottengono risolvendo sistemi delle rette di bordo.

![[GEO-p391-1.png|650]]

**Lettura della figura (PDF p. 391, libro p. 375).** Le ombreggiature mostrano come un ulteriore confine possa restringere o eliminare una porzione ammissibile. Il bordo è incluso solo per disequazioni non strette.

![[GEO-p392-1.png|650]]

**Lettura della figura (PDF p. 392, libro p. 376).** Le regioni selezionate e il nuovo diagramma di rette appartengono alle soluzioni degli esercizi: ogni disegno va letto insieme alle disequazioni riportate nella pagina.

![[GEO-p393-1.png|650]]

**Lettura della figura (PDF p. 393, libro p. 377).** I tre casi confrontano lati diversi delle stesse rette. Le regioni si ricavano con il segno delle espressioni lineari, senza affidarsi alla sola inclinazione grafica.

![[GEO-p394-1.png|650]]

**Lettura della figura (PDF p. 394, libro p. 378).** Le figure confrontano una regione delimitata e le configurazioni successive: il controllo algebrico delle intersezioni evita di scegliere vertici non ammissibili.

![[GEO-p395-1.png|650]]

**Lettura della figura (PDF p. 395, libro p. 379).** Le ultime regioni degli esercizi illustrano intersezioni anche non limitate: una regione convessa non deve necessariamente essere un poligono chiuso e limitato.

## Ripasso attivo

- **Equazioni cartesiane di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equazione cartesiana della retta]].
- **Equazione cartesiana ed equazioni parametriche:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Passaggio tra forme di una retta]].
- **Retta passante per due punti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Retta per due punti]].
- **Intersezione di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Intersezione di rette cartesiane]].
- **Fasci di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Fasci di rette]].
- **Semipiani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Semipiani cartesiani]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 364 (PDF p. 380). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[22 - GEO - Equazioni parametriche]] · Successiva: [[24 - GEO - Equazioni cartesiane nello spazio]]

[[MOC - Geometria]]
