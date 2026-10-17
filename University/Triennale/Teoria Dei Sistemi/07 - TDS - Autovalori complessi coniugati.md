---
title: Autovalori complessi coniugati
aliases:
  - TDS — Autovalori complessi coniugati
tags:
  - teoria-dei-sistemi
  - modi-naturali
  - autovalori-complessi
  - esponenziale-di-matrice
  - osservabilita
  - eccitabilita
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 16–20); libro Monaco et al., §2.2.1, §2.4
---

# Autovalori complessi coniugati

> [!abstract] Scopo della lezione
> Due completamenti della teoria dei [[06 - TDS - Modi naturali|modi naturali]]:
> 1. con autovalori **multipli**, osservabilità ed eccitabilità di un modo dipendono dalla scelta degli autovettori: servono le nozioni di **completa osservabilità** e **completa eccitabilità**;
> 2. finora gli autovalori erano reali, ma molti sistemi (per esempio l'oscillatore armonico) non hanno leggi puramente esponenziali. Con una coppia di autovalori **complessi coniugati** si cerca una base **reale** del piano dei due autovettori complessi, nella quale la matrice dinamica diventa il blocco $\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$, e si calcola il suo esponenziale.
>
> Il significato fisico (modi pseudoperiodici) è in [[08 - TDS - Modi aperiodici e pseudoperiodici]]. Indice: [[MOC - Teoria dei Sistemi]].

## Completa osservabilità e completa eccitabilità

Vedi [[TDS - Eccitabilità e osservabilità dei modi]].

Se gli autovalori sono tutti distinti, per sapere se un modo è osservabile o eccitabile basta guardare se compare in $y_L(t)$ o in $H(t)$. Con autovalori di molteplicità maggiore di 1 la cosa non funziona più così bene:

$$x_L(t)=e^{At}x_0=\sum_{i=1}^r\sum_{j=1}^{\mu_i}e^{\lambda_it}u_{ij}v_{ij}'x_0=\sum_{i=1}^r\sum_{j=1}^{\mu_i}c_{ij}\,e^{\lambda_it}\,u_{ij}$$

La legge temporale $e^{\lambda_it}$ compare più volte. Gli autovettori scelti individuano sempre lo stesso sottospazio, ma i vettori che lo generano sono arbitrari: non ha senso parlare di "modo naturale osservabile" riferendosi a un singolo termine $e^{\lambda_it}u_{ij}v_{ij}'$ della seconda sommatoria.

> [!example] Il problema
> In dimensione 2, un autovalore $\lambda$ con molteplicità 2 individua due autovettori $u_{11}$, $u_{12}$ in un piano. Può succedere che $Cu_{11}=0$ ma $Cu_{12}\neq0$; con un'altra scelta dei due autovettori il risultato può essere diverso.

**Definizione.** Un modo naturale è **completamente osservabile** (risp. **completamente eccitabile**) se è osservabile (risp. eccitabile) **per ogni** scelta degli autovettori che lo compongono.

> [!quote] Dal libro — la condizione e un esempio
> In formule, per l'autovalore $\lambda_i$ con autospazio $U_i$:
> $$\text{completa eccitabilità: } v'B\neq0\ \ \forall v'\in\mathrm{Gen}\,V_i',\qquad \text{completa osservabilità: } Cu\neq0\ \ \forall u\in U_i$$
> dove $\mathrm{Gen}\,V_i'$ è l'insieme delle combinazioni lineari (non nulle) delle $\mu_i$ righe $v_{ij}'$. **Condizione necessaria**: il sistema deve avere almeno tanti ingressi (uscite) quanta è la molteplicità dell'autovalore.
>
> **Esempio 2.4.1.** $A=\begin{psmallmatrix}1&0&0\\0&1&0\\1&0&2\end{psmallmatrix}$, $B=\begin{psmallmatrix}1\\0\\0\end{psmallmatrix}$, $C=(1\ 1\ 1)$: $\lambda_1=1$ doppio (regolare), $\lambda_2=2$.
> - Con $u_{11}=(1,0,-1)'$, $u_{12}=(0,1,0)'$, $u_2=(0,0,1)'$: $v_{11}'B=1$, $v_{12}'B=0$, $Cu_{11}=0$, $Cu_{12}=1$. Sembra che nessuno dei due modi di $\lambda_1$ sia insieme eccitabile e osservabile, e $W(t)=e^{2t}$.
> - Con $\tilde u_{11}=(1,1,-1)'$, $\tilde u_{12}=(0,1,0)'$: $\tilde v_{11}'B=1$, $\tilde v_{12}'B=-1$, $C\tilde u_{11}=1$, $C\tilde u_{12}=1$. Ora sembrano tutti eccitabili e osservabili, ma i due contributi $e^{t}\cdot1\cdot1$ ed $e^{t}\cdot1\cdot(-1)$ si cancellano e di nuovo $W(t)=e^{2t}$.
>
> Il modo di $\lambda_1$ non è né completamente eccitabile né completamente osservabile: con un solo ingresso e una sola uscita non può esserlo, perché la molteplicità è 2. _(libro, §2.4, pp. 74–76)_

## Autovalori complessi coniugati

Vedi [[TDS - Modi aperiodici e pseudoperiodici]].

Finora abbiamo trattato il caso **regolare** con autovalori reali. Sembrerebbe che i sistemi lineari seguano solo leggi esponenziali, ma è una visione molto limitata: molti sistemi oscillano (come l'oscillatore armonico). Rimuoviamo allora l'ipotesi che gli autovalori siano reali. Poiché $A$ è reale, il suo polinomio caratteristico ha coefficienti reali e le radici complesse compaiono a **coppie coniugate**:

$$\lambda_1,\lambda_2,\dots,\lambda_k,\lambda_k^*,\dots,\lambda_n$$

dove $\lambda^*$ è il coniugato: se $\lambda=\alpha+j\omega$ allora $\lambda^*=\alpha-j\omega$ (si usa $j$ per l'unità immaginaria; vedi [[11 - AN1 - Numeri Complessi]]). Restiamo nell'ipotesi che $A$ sia diagonalizzabile (regolare). Gli autovettori sono

$$u_1,u_2,\dots,u_k,u_k^*,\dots,u_n$$

tutti in $\mathbb R^n$ tranne $u_k$ e $u_k^*$, che stanno in $\mathbb C^n$ (anche gli autovettori di una coppia sono coniugati, perché coniugando $Au=\lambda u$ con $A$ reale si ottiene $Au^*=\lambda^*u^*$). La matrice $U=(u_1\ u_2\ \cdots\ u_k\ u_k^*\ \cdots\ u_n)$ si costruisce senza problemi, e continuano a valere

$$e^{At}=Ue^{\Lambda t}U^{-1}=\sum_{i=1}^ne^{\lambda_it}u_iv_i',\qquad x_L(t)=\sum_{i=1}^nc_i\,e^{\lambda_it}\,u_i$$

Matematicamente non è cambiato nulla. Il problema è l'**interpretazione**: con $n=2$ e una coppia coniugata, $u$ e $u^*$ sono vettori complessi, e per disegnarli servirebbero quattro dimensioni ($\mathbb C^2\simeq\mathbb R^4$); e anche se potessimo, come si disegna un termine $e^{(a+jb)t}$? Vogliamo un modo per "togliere" i termini complessi e avere espressioni **reali**.

### Una base reale per il piano della coppia

Supponiamo $n=2$ con una sola coppia $\lambda,\lambda^*$ di autovettori $u,u^*$. Non è restrittivo: se ci sono altri autovalori, ciò che succede negli altri sottospazi non influenza questa coppia e viceversa.

$$U=(u\ \ u^*),\quad V=(u\ \ u^*)^{-1},\qquad A=\lambda uv'+\lambda^*u^*v^{*\prime}=(u\ \ u^*)\begin{pmatrix}\lambda&0\\0&\lambda^*\end{pmatrix}(u\ \ u^*)^{-1}$$

Cerchiamo due vettori **reali** $w_1,w_2$ che generino lo stesso sottospazio, cioè tali che

$$(u\ \ u^*)=(w_1\ \ w_2)\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

con la matrice $\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$ non singolare (così il cambio di base si può invertire). Poiché $u,u^*$ sono complessi e $w_1,w_2$ reali, questa matrice deve contenere termini complessi. Scriviamo l'autovettore separando parte reale e parte immaginaria:

$$u=u_a+ju_b,\qquad u^*=u_a-ju_b,\qquad u_a,u_b\in\mathbb R^2$$

Allora basta prendere $w_1=u_a$, $w_2=u_b$:

$$(u_a\ \ u_b)\begin{pmatrix}1&1\\j&-j\end{pmatrix}=(u_a+ju_b\ \ \ u_a-ju_b)=(u\ \ u^*)$$

La matrice $\begin{psmallmatrix}1&1\\j&-j\end{psmallmatrix}$ ha determinante $-2j\neq0$, quindi è invertibile. Il cambio di base mostra che $u$ e $u^*$ delimitano in realtà un **piano** reale, non uno spazio a quattro dimensioni.

Sostituiamo in $A$, ricordando che invertendo un prodotto si inverte anche l'ordine dei fattori, $(u\ u^*)^{-1}=\begin{psmallmatrix}1&1\\j&-j\end{psmallmatrix}^{-1}(u_a\ u_b)^{-1}$:

$$A=(u_a\ \ u_b)\begin{pmatrix}1&1\\j&-j\end{pmatrix}\begin{pmatrix}\lambda&0\\0&\lambda^*\end{pmatrix}\begin{pmatrix}1&1\\j&-j\end{pmatrix}^{-1}(u_a\ \ u_b)^{-1}$$

Calcoliamo il prodotto centrale, con $\begin{psmallmatrix}1&1\\j&-j\end{psmallmatrix}^{-1}=\begin{psmallmatrix}1/2&1/(2j)\\1/2&-1/(2j)\end{psmallmatrix}$:

$$\begin{pmatrix}\lambda&\lambda^*\\j\lambda&-j\lambda^*\end{pmatrix}\begin{pmatrix}\frac12&\frac1{2j}\\\frac12&-\frac1{2j}\end{pmatrix}=\begin{pmatrix}\frac{\lambda+\lambda^*}{2}&\frac{\lambda-\lambda^*}{2j}\\[1mm] j\frac{\lambda-\lambda^*}{2}&\frac{\lambda+\lambda^*}{2}\end{pmatrix}$$

Con $\lambda=\alpha+j\omega$: $\lambda+\lambda^*=2\alpha$ e $\lambda-\lambda^*=2j\omega$, quindi

$$\begin{pmatrix}\frac{\lambda+\lambda^*}{2}&\frac{\lambda-\lambda^*}{2j}\\[1mm] j\frac{\lambda-\lambda^*}{2}&\frac{\lambda+\lambda^*}{2}\end{pmatrix}=\begin{pmatrix}\alpha&\omega\\-\omega&\alpha\end{pmatrix}
\qquad\Longrightarrow\qquad
A=(u_a\ \ u_b)\begin{pmatrix}\alpha&\omega\\-\omega&\alpha\end{pmatrix}(u_a\ \ u_b)^{-1}$$

(il termine in basso a sinistra è $j\cdot\frac{2j\omega}{2}=j^2\omega=-\omega$.)

## Calcolo di $e^{At}$ con autovalori complessi

Vedi [[TDS - Esponenziale di matrice]].

Come nel caso reale, $(u_a\ u_b)$ e $(u_a\ u_b)^{-1}$ escono dalla serie perché nelle potenze i fattori interni si cancellano:

$$A^k=(u_a\ u_b)\begin{pmatrix}\alpha&\omega\\-\omega&\alpha\end{pmatrix}^k(u_a\ u_b)^{-1}\quad\Longrightarrow\quad e^{At}=(u_a\ u_b)\left(\sum_{k=0}^\infty\frac{1}{k!}\begin{pmatrix}\alpha&\omega\\-\omega&\alpha\end{pmatrix}^kt^k\right)(u_a\ u_b)^{-1}$$

La serie non è banale da sommare direttamente. Conviene ripartire dalla forma diagonale complessa, dove l'esponenziale è immediato:

$$e^{At}=(u\ \ u^*)\begin{pmatrix}e^{\lambda t}&0\\0&e^{\lambda^*t}\end{pmatrix}(u\ \ u^*)^{-1}=(u_a\ \ u_b)\begin{pmatrix}1&1\\j&-j\end{pmatrix}\begin{pmatrix}e^{\lambda t}&0\\0&e^{\lambda^*t}\end{pmatrix}\begin{pmatrix}1&1\\j&-j\end{pmatrix}^{-1}(u_a\ \ u_b)^{-1}$$

Concentriamoci sulla parte centrale, con $\lambda=\alpha+j\omega$ e $e^{(\alpha\pm j\omega)t}=e^{\alpha t}e^{\pm j\omega t}$:

$$e^{\alpha t}\begin{pmatrix}e^{j\omega t}&e^{-j\omega t}\\je^{j\omega t}&-je^{-j\omega t}\end{pmatrix}\begin{pmatrix}\frac12&\frac1{2j}\\\frac12&-\frac1{2j}\end{pmatrix}
=e^{\alpha t}\begin{pmatrix}\frac{e^{j\omega t}+e^{-j\omega t}}{2}&\frac{e^{j\omega t}-e^{-j\omega t}}{2j}\\[1mm] j\frac{e^{j\omega t}-e^{-j\omega t}}{2}&\frac{e^{j\omega t}+e^{-j\omega t}}{2}\end{pmatrix}
=e^{\alpha t}\begin{pmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{pmatrix}$$

usando le formule di Eulero $\cos z=\frac{e^{jz}+e^{-jz}}{2}$, $\sin z=\frac{e^{jz}-e^{-jz}}{2j}$ (e $j\cdot\frac{e^{jz}-e^{-jz}}{2}=j\cdot j\sin z=-\sin z$). Quindi:

$$\boxed{e^{At}=(u_a\ \ u_b)\begin{pmatrix}e^{\alpha t}\cos\omega t&e^{\alpha t}\sin\omega t\\-e^{\alpha t}\sin\omega t&e^{\alpha t}\cos\omega t\end{pmatrix}(u_a\ \ u_b)^{-1}}$$

La matrice centrale è una **rotazione** di angolo $\omega t$ moltiplicata per il fattore di scala $e^{\alpha t}$: è la radice del comportamento oscillante.

> [!quote] Dal libro — Proposizione 2.2.1
> $$e^{\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}t}=e^{\alpha t}\begin{pmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{pmatrix}$$
> La dimostrazione del libro è più rapida: basta verificare che la matrice a destra valga $I$ in $t=0$ e soddisfi l'equazione $\dot\Phi=\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}\Phi$; per l'unicità della soluzione è proprio l'esponenziale. _(libro, §2.2.1, p. 50)_

> [!example] Verifica: l'oscillatore armonico
> $A=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ (cioè $\ddot q=-q$ con $x=(q,\dot q)$) è già nella forma $\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$ con $\alpha=0$, $\omega=1$. Allora $e^{At}=\begin{psmallmatrix}\cos t&\sin t\\-\sin t&\cos t\end{psmallmatrix}$ e da $x_0=(1,0)'$ si ha $q(t)=\cos t$: l'oscillazione che con soli esponenziali reali non si poteva ottenere.

## Caso complesso con $n>2$ autovalori

Se oltre alla coppia coniugata ci sono altri autovalori, si parte comunque dalla forma spettrale complessa

$$U=(u_1\ \ u_2\ \cdots\ u\ \ u^*\ \cdots\ u_n),\qquad A=U\,\mathrm{diag}(\lambda_1,\lambda_2,\dots,\lambda,\lambda^*,\dots,\lambda_n)\,U^{-1}$$

e si sostituiscono $u,u^*$ con $u_a,u_b$. Si può fare senza problemi perché gli autovettori della base sono **indipendenti** e non si influenzano, e le coppie $u,u^*$ e $u_a,u_b$ generano lo stesso piano. Gli autovalori reali restano invariati; cambia solo il blocco della coppia:

$$\Lambda=\begin{pmatrix}\lambda_1&&&&\\&\ddots&&&\\&&\boxed{\begin{matrix}\lambda&0\\0&\lambda^*\end{matrix}}&&\\&&&\ddots&\\&&&&\lambda_n\end{pmatrix}\ \Longrightarrow\ \begin{pmatrix}\lambda_1&&&&\\&\ddots&&&\\&&\boxed{\begin{matrix}\alpha&\omega\\-\omega&\alpha\end{matrix}}&&\\&&&\ddots&\\&&&&\lambda_n\end{pmatrix}$$

La matrice diventa **diagonale a blocchi**. Funziona anche con più coppie: ogni coppia di autovalori complessi coniugati "esplode" nel suo blocco $\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$, e l'esponenziale si calcola blocco per blocco.

> [!quote] Dal libro — la forma spettrale reale
> Con $\mu$ autovalori reali e $\gamma$ coppie complesse, il libro scrive la forma spettrale reale
> $$A=\sum_{i=1}^{\mu}\lambda_iu_iv_i'+\sum_{j=1}^{\gamma}\Big(\alpha_j(u_{ja}v_{ja}'+u_{jb}v_{jb}')+\omega_j(u_{ja}v_{jb}'-u_{jb}v_{ja}')\Big)$$
> e la corrispondente forma spettrale della matrice di transizione
> $$\Phi(t)=\sum_ie^{\lambda_it}u_iv_i'+\sum_ke^{\alpha_kt}\Big(\cos\omega_kt\,(u_{ka}v_{ka}'+u_{kb}v_{kb}')+\sin\omega_kt\,(u_{ka}v_{kb}'-u_{kb}v_{ka}')\Big)$$
> _(libro, §2.2.1, pp. 50–51)_

## Approfondimento sul cambio degli autovettori

Verifichiamo che il cambio $u,u^*\to u_a,u_b$ funzioni, cioè che resti vero $U^{-1}U=I$: il prodotto $v_i'u_j$ vale 1 solo per $i=j$ e 0 altrimenti. Prima del cambio valeva, per ogni riga $v_i'$ diversa da quelle della coppia,

$$v_i'u=v_i'(u_a+ju_b)=0,\qquad v_i'u^*=v_i'(u_a-ju_b)=0$$

Se valgono contemporaneamente, sommando e sottraendo si ottiene $v_i'u_a=0$ e $v_i'u_b=0$: le altre righe restano ortogonali ai nuovi vettori, e la struttura di $U^{-1}$ si conserva.

> [!warning] Correzione
> Negli appunti la verifica è scritta come $v_i'u=v_i'(\alpha+j\omega)=0$, $v_i'u^*=v_i'(\alpha-j\omega)=0$, con la conclusione "visto che $u_a=\alpha$ e $u_b=\omega$". C'è una confusione di notazione: $\alpha$ e $\omega$ sono le parti reale e immaginaria dell'**autovalore** (scalari), mentre qui servono quelle dell'**autovettore**, $u_a$ e $u_b$ (vettori). La verifica corretta è quella scritta sopra, con $u=u_a+ju_b$.

L'unica cosa che si perde è l'**invarianza dei singoli vettori**: $Au=\lambda u$ e $Au^*=\lambda^*u^*$, ma $u_a$ e $u_b$ non sono autovettori. Resta però **invariante il sottospazio** bidimensionale che generano: infatti $A(u_a\ u_b)=(u_a\ u_b)\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$, cioè $Au_a=\alpha u_a-\omega u_b$ e $Au_b=\omega u_a+\alpha u_b$ stanno ancora nel piano.
