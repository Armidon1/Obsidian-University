---
title: "Equazioni cartesiane nello spazio"
aliases:
  - "GEO — Equazioni cartesiane nello spazio"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "24"
pdf_pages: "397–430"
---

# Equazioni cartesiane nello spazio

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 24 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 24.1 - Equazioni cartesiane di piani

Vedi [[GEO - Equazione cartesiana del piano]].

Un piano nello spazio ha equazione $ax+by+cz+d=0$, con $(a,b,c)\ne0$. È un unico vincolo lineare indipendente in tre incognite, quindi ha dimensione affine $2$.

Il sottospazio direzionale è $ax+by+cz=0$. In un riferimento affine generico i coefficienti descrivono il vincolo; la loro interpretazione come componenti di un vettore normale richiede un riferimento cartesiano ortonormale.

_(Accascina–Monti, § 24.1, libro pp. 381–382; PDF pp. 397–398.)_

## 24.2 - Equazioni cartesiane e parametriche di piani

Vedi [[GEO - Passaggio tra forme di un piano]].

Dalla forma cartesiana si ricavano due parametri risolvendo l’equazione. Da $x+y+z=2$, per esempio, si ottiene $(x,y,z)=(2-s-t,s,t)$.

Dalla parametrica $P=P_0+su+tv$ si elimina $s,t$, oppure si scrive

$$\det\begin{pmatrix}x-x_0&y-y_0&z-z_0\\u_1&u_2&u_3\\v_1&v_2&v_3\end{pmatrix}=0.$$

L’indipendenza di $u,v$ garantisce che il risultato rappresenti effettivamente un piano.

_(Accascina–Monti, § 24.2, libro pp. 382–384; PDF pp. 398–400.)_

## 24.3 - Piano passante per tre punti

Vedi [[GEO - Piano per tre punti]].

Tre punti non allineati determinano un piano unico: si scelgono $u=P_1-P_0$ e $v=P_2-P_0$. Per $P_0=(1,0,0)$, $P_1=(0,1,0)$, $P_2=(0,0,1)$ si ricava $x+y+z=1$.

Se i punti sono allineati, i due direttori sono dipendenti: esistono infiniti piani contenenti la retta e il determinante non fornisce un unico piano.

_(Accascina–Monti, § 24.3, libro pp. 384–386; PDF pp. 400–402.)_

## 24.4 - Intersezione di piani

Vedi [[GEO - Intersezione di piani]].

Due equazioni di piano formano un sistema in tre incognite. Se le righe dei coefficienti hanno rango $2$, l’intersezione è una retta. Se hanno rango $1$, si distinguono piani coincidenti e paralleli distinti confrontando la completa.

Per $x+y+z=1$ e $x-y=0$, si ha $x=y=t$, $z=1-2t$: una retta di direttore $(1,1,-2)$.

_(Accascina–Monti, § 24.4, libro pp. 386–388; PDF pp. 402–404.)_

## 24.5 - Equazioni cartesiane di rette

Vedi [[GEO - Retta come intersezione di piani]].

Una retta nello spazio si può descrivere come intersezione di due piani con coefficienti indipendenti:

$$r:\begin{cases}a_1x+b_1y+c_1z+d_1=0\\a_2x+b_2y+c_2z+d_2=0\end{cases},\qquad\operatorname{rk}A=2.$$

Una sola equazione lineare non può rappresentare una retta in $\mathbb R^3$. Le coppie di equazioni non sono uniche, perché si possono scegliere diversi piani contenenti la stessa retta.

_(Accascina–Monti, § 24.5, libro pp. 388–389; PDF pp. 404–405.)_

## 24.6 - Fasci e stelle di piani

Vedi [[GEO - Fasci e stelle di piani]].

I piani $ax+by+cz+k=0$ formano un fascio di piani paralleli. Due piani distinti incidenti $\pi=0$, $\sigma=0$ generano il fascio con asse la loro retta comune:

$$h\pi+k\sigma=0,\qquad(h,k)\ne(0,0).$$

La stella di piani con centro $P_0$ raccoglie tutti i piani $a(x-x_0)+b(y-y_0)+c(z-z_0)=0$, con $(a,b,c)\ne0$. Per selezionare un piano dal fascio si può imporre il passaggio per un punto esterno all’asse.

_(Accascina–Monti, § 24.6, libro pp. 389–394; PDF pp. 405–410.)_

## 24.7 - Semispazi

Vedi [[GEO - Semispazi e semipiani nello spazio]].

I semispazi aperti delimitati da un piano sono $ax+by+cz+d>0$ e $ax+by+cz+d<0$. Un semipiano **dentro** un piano richiede invece un’uguaglianza che imponga il piano e una disequazione che selezioni il lato rispetto a una retta interna.

Per esempio $z=0$, $x>0$ descrive un semipiano del piano $xy$; la sola condizione $x>0$ descrive un semispazio tridimensionale.

_(Accascina–Monti, § 24.7, libro pp. 394–396; PDF pp. 410–412.)_

## Ripasso attivo

- **Equazioni cartesiane di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equazione cartesiana del piano]].
- **Equazioni cartesiane e parametriche di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Passaggio tra forme di un piano]].
- **Piano passante per tre punti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Piano per tre punti]].
- **Intersezione di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Intersezione di piani]].
- **Equazioni cartesiane di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Retta come intersezione di piani]].
- **Fasci e stelle di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Fasci e stelle di piani]].
- **Semispazi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Semispazi e semipiani nello spazio]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 400 (PDF p. 416). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[23 - GEO - Equazioni cartesiane nel piano]] · Successiva: [[25 - GEO - Funzioni tra insiemi]]

[[MOC - Geometria]]
