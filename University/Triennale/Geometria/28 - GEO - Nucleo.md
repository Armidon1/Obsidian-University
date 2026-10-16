---
title: "Nucleo"
aliases:
  - "GEO — Nucleo"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "28"
pdf_pages: "483–502"
---

# Nucleo

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 28 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 28.1 - Nucleo di un omomorfismo

Vedi [[GEO - Nucleo e iniettività]].

Il nucleo è il sottospazio del **dominio** formato dai vettori annullati da $f$:

$$\ker f=\{v\in V:f(v)=0\}.$$

È un sottospazio perché combinazioni di vettori mandati a zero sono ancora mandate a zero. L’applicazione è iniettiva esattamente quando $\ker f=\{0\}$: da $f(u)=f(v)$ segue infatti $f(u-v)=0$.

_(Accascina–Monti, § 28.1, libro pp. 467–470; PDF pp. 483–486.)_

## 28.2 - Calcolo del nucleo

Vedi [[GEO - Calcolo del nucleo e rango-nullità]].

Nelle basi fissate si risolve $Ax=0$. Le soluzioni forniscono le coordinate dei vettori del nucleo. Per $f(x,y,z)=(x+y,y+z)$ si ha $x=-y$ e $z=-y$, quindi

$$\ker f=\langle(-1,1,-1)\rangle.$$

Il teorema delle dimensioni, o rango-nullità, afferma per $V$ finito-dimensionale:

$$\dim V=\dim\ker f+\dim\operatorname{Im}f.$$

Se $A$ ha $n$ colonne e rango $r$, il nucleo ha dimensione $n-r$. Nell’esempio $3=1+2$. Un’applicazione lineare da uno spazio di dimensione maggiore a uno di dimensione minore non può essere iniettiva.

_(Accascina–Monti, § 28.2, libro pp. 470–473; PDF pp. 486–489.)_

## 28.3 - Controimmagini

Vedi [[GEO - Controimmagini affini]].

Per trovare tutti i vettori con immagine $w$ si risolve $Ax=[w]$. Se $w\notin\operatorname{Im}f$ la controimmagine è vuota. Se $f(v_0)=w$, allora

$$f^{-1}(w)=v_0+\ker f.$$

Per l’applicazione precedente, la controimmagine di $(1,0)$ è $(1,0,0)+t(-1,1,-1)$. Il controllo dà $f(1-t,t,-t)=(1,0)$.

Le controimmagini non vuote sono affini paralleli al nucleo: variano di posizione, mentre le direzioni di libertà sono sempre le stesse.

_(Accascina–Monti, § 28.3, libro pp. 473–475; PDF pp. 489–491.)_

## Ripasso attivo

- **Nucleo di un omomorfismo:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Nucleo e iniettività]].
- **Calcolo del nucleo:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Calcolo del nucleo e rango-nullità]].
- **Controimmagini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Controimmagini affini]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 478 (PDF p. 494). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[27 - GEO - Immagine]] · Successiva: [[29 - GEO - Isomorfismi]]

[[MOC - Geometria]]
