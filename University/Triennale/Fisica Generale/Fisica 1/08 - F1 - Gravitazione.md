---
title: "Gravitazione"
aliases:
  - "F1 — Gravitazione"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "212-227"
---

# Gravitazione

> [!abstract]
> La legge gravitazionale unifica caduta terrestre e moto astronomico. La natura centrale dell’interazione permette di usare insieme conservazione dell’energia e del momento angolare.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Forza, massa e campo gravitazionale

Vedi [[F1 - Forza, massa e campo gravitazionale]].

Due masse puntiformi si attraggono con $\mathbf F=-GMm\hat{\mathbf r}/r^2$, dove $\mathbf r$ va da $M$ a $m$. Il campo è $\mathbf g=\mathbf F/m$. La sovrapposizione permette di integrare i contributi di una distribuzione. All'esterno di una distribuzione sfericamente simmetrica il campo è quello della massa totale concentrata nel centro. Massa inerziale e gravitazionale sono concettualmente distinte; la loro proporzionalità rende universale l'accelerazione di caduta nel medesimo campo.

![[F1-p218-1.png]]

*Figura 8.13: il campo in un punto è la somma vettoriale dei contributi delle singole masse. Non si sommano direttamente i moduli, salvo che i vettori siano concordi.* _(Libro, p. 209; PDF p. 218.)_

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Energia potenziale e campo centrale

Vedi [[F1 - Energia potenziale e campo centrale]].

Fissando $U(\infty)=0$,
$$U(r)=-\frac{GMm}{r},\qquad E=\tfrac12mv^2-\frac{GMm}{r}.$$
La forza si recupera da $-dU/dr$. Vicino al suolo, per $h\ll R_T$, $U(R_T+h)-U(R_T)\simeq mgh$: il potenziale uniforme è un'approssimazione locale di quello newtoniano. Il momento angolare conservato impone moto piano e velocità areolare costante.

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Orbite circolari e leggi di Keplero

Vedi [[F1 - Orbite circolari e leggi di Keplero]].

Per una massa di prova attorno a $M$,
$$v_c=\sqrt{GM/r},\quad T=2\pi\sqrt{r^3/(GM)},\quad E_c=-GMm/(2r).$$
Le orbite legate sono ellissi con il centro attrattore in un fuoco; la seconda legge esprime la costanza della velocità areolare, la terza $T^2=4\pi^2a^3/(GM)$. Quest'ultima usa il semiasse maggiore $a$, non il raggio istantaneo. Nel problema esatto a due corpi il parametro contiene $M+m$.

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Fuga e potenziale efficace

Vedi [[F1 - Fuga e potenziale efficace]].

La velocità minima di fuga da raggio $r$, trascurando atmosfera e altre sorgenti, si ottiene ponendo $E=0$:
$$v_f=\sqrt{2GM/r}=\sqrt2\,v_c.$$
Con momento angolare $L$ fissato il moto radiale soddisfa
$$E=\tfrac12m\dot r^2+U_{\mathrm{eff}}(r),\quad U_{\mathrm{eff}}=\frac{L^2}{2mr^2}-\frac{GMm}{r}.$$
Il primo termine è una barriera centrifuga nella descrizione radiale; il minimo individua l'orbita circolare stabile. Il segno dell'energia distingue orbite legate e non legate nel potenziale newtoniano con zero all'infinito.

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Limiti della gravitazione newtoniana

Vedi [[F1 - Limiti della gravitazione newtoniana]].

La descrizione newtoniana funziona per campi relativamente deboli e velocità piccole rispetto a quella della luce. La relatività generale interpreta la gravità attraverso la geometria dello spaziotempo; la caduta libera è localmente assimilabile a un riferimento inerziale, mentre gli effetti mareali rivelano variazioni del campo fra punti vicini. La precessione del perielio e la deviazione della luce sono fenomeni che richiedono correzioni rispetto al modello newtoniano. Questi cenni non modificano le formule operative dei problemi classici qui trattati, ma ne delimitano il dominio.

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Derivazione guidata

Per un'orbita circolare equilibra la componente radiale della seconda legge: $mv^2/r=GMm/r^2$. Da qui $v^2=GM/r$; sostituendo in $E=mv^2/2-GMm/r$ ottieni $E=-GMm/(2r)$. Usando $T=2\pi r/v$ segue $T^2=4\pi^2r^3/(GM)$. La cancellazione della massa di prova spiega perché, nelle stesse approssimazioni, satelliti diversi sullo stesso raggio hanno uguale periodo.

_(Libro, cap. 8; pagine stampate 203–218; PDF pp. 212–227.)_

## Esempio svolto

> [!example] Applicazione originale
> Se il raggio di un'orbita circolare quadruplica, $v_c$ si dimezza e il periodo cresce di $4^{3/2}=8$ volte. La velocità diminuisce non perché il satellite abbia bisogno di una forza tangenziale frenante, ma perché si stanno confrontando due differenti orbite circolari.

## Richiami matematici

[[06 - AN1 - Calcolo Integrale]] · [[05 - AN1 - Calcolo Differenziale]].

## Verifica attiva

Raddoppiando il raggio di un’orbita circolare, come cambiano velocità e periodo?

> [!check]- Risposta ragionata
> La velocità si moltiplica per $1/\sqrt2$ e il periodo per $2\sqrt2$, mantenendo fissa la massa attrattiva.

## Navigazione

Precedente: [[07 - F1 - Fenomeni di urto]] · Successivo: [[09 - F1 - Onde meccaniche]].
