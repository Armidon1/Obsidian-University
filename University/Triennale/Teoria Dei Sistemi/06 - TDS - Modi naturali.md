---
title: Modi naturali
aliases:
  - TDS — Modi naturali
tags:
  - teoria-dei-sistemi
  - modi-naturali
  - forma-spettrale
  - osservabilita
  - eccitabilita
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 12–15); libro Monaco et al., §2.3.1, §2.4
---

# Modi naturali

> [!abstract] Scopo della lezione
> Con la forma spettrale della [[05 - TDS - Calcolo dell'esponenziale di matrice|lezione precedente]] l'evoluzione libera è una somma di termini $c_ie^{\lambda_it}u_i$. Qui si dà un nome a questi termini, i **modi naturali**, e se ne studia la struttura:
> - le **matrici residue** $R_i$ e cosa dice il loro rango;
> - la libertà nella **scelta degli autovettori** quando un autovalore è multiplo, e i **sottospazi invarianti**;
> - quali modi compaiono in uscita (**osservabilità**) e quali vengono sollecitati dall'ingresso (**eccitabilità**), e perché nella risposta impulsiva in uscita compaiono solo i modi osservabili **ed** eccitabili.
>
> Segue [[07 - TDS - Autovalori complessi coniugati]]. Indice: [[MOC - Teoria dei Sistemi]].

## Modi naturali

Vedi [[TDS - Modi naturali]].

Quando $A$ è diagonale o diagonalizzabile, l'evoluzione libera dello stato è

$$x_L(t)=\sum_{i=1}^{n}c_i\,e^{\lambda_it}\,u_i$$

Ogni termine $c_ie^{\lambda_it}u_i$ rappresenta un modo *intrinseco* di evolvere del sistema e si chiama **modo naturale**. È fatto di due pezzi:
- una **legge temporale** $c_ie^{\lambda_it}$, che dà l'ampiezza nel tempo;
- un **vettore** $u_i$, che dà la direzione (il sottospazio) lungo cui l'evoluzione avviene.

Poiché gli autovettori sono indipendenti, il moto lungo un autovettore non dipende da quello che succede lungo gli altri: per sapere cosa succede lungo $u_i$ bastano $\lambda_i$ e il coefficiente $c_i=v_i'x_0$.

In generale ci sono $n$ modi naturali, ma in una specifica evoluzione libera possono comparirne meno: se $c_i=0$ (lo stato iniziale non ha componente lungo $u_i$), l'$i$-esimo modo non viene "acceso".

> [!quote] Dal libro — modi aperiodici
> Per un operatore regolare il libro (Teorema 2.3.1) dice che l'evoluzione libera è combinazione lineare di modi naturali di due tipi: **aperiodici** $ce^{\lambda t}u$, associati agli autovalori reali, e **pseudoperiodici** $me^{\alpha t}\big(\sin(\omega t+\varphi)u_a+\cos(\omega t+\varphi)u_b\big)$, associati alle coppie complesse $\alpha\pm j\omega$ (vedi [[08 - TDS - Modi aperiodici e pseudoperiodici]]).
> Per un modo aperiodico: se $\lambda=0$ lo stato resta fermo; se $\lambda>0$ l'evoluzione diverge restando nella direzione dell'autovettore; se $\lambda<0$ converge verso l'origine. Se lo stato iniziale sta su un autovettore $u_i$, solo $c_i\ne0$ e nell'evoluzione compare solo quella legge di moto. _(libro, §2.3.1, pp. 56–58)_

## Considerazioni sulla matrice $A$

Vedi [[TDS - Forma spettrale]].

La forma spettrale

$$A=\sum_{i=1}^n\lambda_i\,u_iv_i'$$

scrive $A$ come somma di matrici $u_iv_i'$. Ognuna è una matrice $n\times n$ di **rango 1** (prodotto di un vettore colonna per un vettore riga); chiamiamola $R_i$. Quindi $A=\lambda_1R_1+\lambda_2R_2+\dots$

Se $A$ è diagonalizzabile ma con autovalori multipli:

$$A=\sum_{i=1}^r\sum_{j=1}^{\mu_i}\lambda_i\,u_{ij}v_{ij}'=\sum_{i=1}^r\lambda_i\underbrace{\sum_{j=1}^{\mu_i}u_{ij}v_{ij}'}_{R_i}$$

Ogni $u_{ij}v_{ij}'=R_{ij}$ ha rango 1, e la **matrice residua**

$$R_i:=\sum_{j=1}^{\mu_i}u_{ij}v_{ij}'=\sum_{j=1}^{\mu_i}R_{ij}$$

ha **rango $\mu_i$** (somma di $\mu_i$ matrici di rango 1 costruite con vettori indipendenti).

> [!example] Riconoscere la molteplicità dal rango
> Se di una $A$ $3\times3$ sappiamo che $A=\lambda_1R_1+\lambda_2R_2$, gli autovalori distinti sono solo 2, quindi uno dei due ha molteplicità 2. Per sapere quale, basta guardare quale tra $R_1$ e $R_2$ ha **rango 2**.

> [!note] Proprietà delle matrici residue
> Dalle relazioni $v_i'u_j=\delta_{ij}$ seguono $R_iR_i=R_i$ (sono **proiettori** sull'autospazio di $\lambda_i$), $R_iR_j=0$ per $i\neq j$ e $\sum_iR_i=I$. Per questo $A^k=\sum_i\lambda_i^kR_i$ e $e^{At}=\sum_ie^{\lambda_it}R_i$.

## Scelta degli autovettori

Consideriamo un sistema con $x\in\mathbb R^3$ e $A$ $3\times3$.

**Autovalori distinti** $\lambda_1,\lambda_2,\lambda_3$. Ogni autovettore è definito univocamente **a meno del modulo**: soluzioni diverse per lo stesso autovettore stanno tutte sulla stessa retta.

![[TDS-L06-01.png]]

In figura l'autovettore $u_1$ (rosso) e la retta che genera (grigia): qualunque altro autovettore di $\lambda_1$ sta su quella retta.

**Un autovalore doppio.** Ora $\lambda_1$ ha molteplicità 2 (algebrica e geometrica) e $\lambda_2$ molteplicità 1. $\lambda_1$ individua due autovettori $u_{11}$, $u_{12}$, $\lambda_2$ l'autovettore $u_3$. I primi due identificano un **piano**, e $u_3$ esce da quel piano.

![[TDS-L06-02.png]]

Il piano verde è l'autospazio $\ker(A-\lambda_1I)$. Se il calcolo dà soluzioni diverse, si ottiene lo stesso risultato a meno di fattori di scala? **No**: per $u_3$ si identifica una *direzione*, ma $u_{11}$ e $u_{12}$ identificano un *piano*, e dentro quel piano si possono trovare due vettori indipendenti del tutto diversi da $u_{11}$, $u_{12}$ che **identificano lo stesso piano**. Le diverse soluzioni sono sempre vettori indipendenti che generano il sottospazio $\ker(A-\lambda_iI)$ (vedi [[28 - GEO - Nucleo]]).

Proseguendo l'esempio, c'è un modo naturale per ogni autovettore: $c_{11}e^{\lambda_1t}$ dice come si muove la componente lungo $u_{11}$, $c_{12}e^{\lambda_1t}$ quella lungo $u_{12}$, $c_2e^{\lambda_2t}$ quella lungo $u_3$. Se $x_0$ sta nel piano $(u_{11},u_{12})$, cioè non ha componente lungo $u_3$, il suo moto è una **retta**: le due componenti seguono la **stessa** legge temporale $e^{\lambda_1t}$ e il vettore viene solo riscalato.

![[TDS-L06-03.png]]

In figura la traiettoria $x(t)$ (arancione) parte da $x_0$ e si muove lungo la retta tratteggiata che passa per l'origine, dentro il piano di $u_{11}$ e $u_{12}$.

Siccome la scelta degli autovettori del piano è arbitraria, si poteva scegliere come autovettore proprio un vettore che giace sulla traiettoria:

![[TDS-L06-04.png]]

Ora $u_{11}$ punta lungo la retta tratteggiata. Scelto così, $u_{11}$ genera un **sottospazio invariante**: il moto che parte da un punto della retta resta sempre sulla retta generata da $u_{11}$. Il fatto che la scelta degli autovettori dentro un autospazio sia libera è molto utile: con la scelta giusta diventano evidenti proprietà che con altri autovettori sarebbero difficili da vedere.

> [!quote] Dal libro
> "In realtà ogni vettore (ogni piano a due dimensioni) nello spazio degli autovettori $U_i$ (delle coppie di autovettori $U_k$) è un autospazio": nel caso regolare con autovalori multipli le evoluzioni che partono da uno stato iniziale dell'autospazio restano in esso e, per un modo aperiodico, avvengono lungo la retta che congiunge $x_0$ all'origine. Il libro riassume: con autovalori coincidenti ma $A$ diagonalizzabile si hanno tanti **modi naturali semplici** quanta è la molteplicità, con **leggi temporali coincidenti**; equivalentemente, un solo modo naturale semplice di dimensione pari alla molteplicità. _(libro, §2.3.1, pp. 60–61)_

## Modi naturali non osservabili

Vedi [[TDS - Eccitabilità e osservabilità dei modi]].

Fatto il calcolo di $e^{At}$, si può fare un passo in più: l'**evoluzione libera in uscita**. Mentre $x_L(t)=\Phi(t)x_0=e^{At}x_0$,

$$y_L(t)=\Psi(t)x_0=Ce^{At}x_0=C\sum_{i=1}^ne^{\lambda_it}u_i\underbrace{v_i'x_0}_{c_i}=\sum_{i=1}^nc_i\,e^{\lambda_it}\,Cu_i$$

(qui per compattezza la sommatoria comprende anche autovalori ripetuti di una $A$ diagonalizzabile). $C$ "entra" nella sommatoria e scavalca gli scalari $c_i$ ed $e^{\lambda_it}$, ma non i vettori: si ferma a sinistra di $u_i$.

- Nell'evoluzione libera dello **stato** ci sono tutti i modi naturali (a meno che $c_i=0$; ma allora basta cambiare stato iniziale per vederli comparire).
- Nell'evoluzione libera dell'**uscita**, invece, il prodotto $Cu_i$ può essere **nullo** per qualche $i$: quei modi spariscono da $y_L(t)$ **qualunque sia** lo stato iniziale.

Questa è una proprietà **intrinseca** del sistema, che dipende dalla sua struttura ($A$ e $C$), non dallo stato iniziale. Se $Cu_i=0$ l'$i$-esimo modo naturale si dice **non osservabile**; sono **osservabili** i modi presenti in $y_L(t)$, che contiene quindi *al più* i modi naturali dello stato.

> [!example] Intuizione
> Se l'autovettore $u_i$ sta nel nucleo di $C$, il moto lungo $u_i$ avviene in una direzione che il "sensore" $C$ non vede: lo stato si muove, ma l'uscita non se ne accorge.

## Modi naturali non eccitabili

Studiamo ora la matrice delle risposte impulsive nello stato, $H(t)=e^{At}B$:

$$e^{At}B=\sum_{i=1}^ne^{\lambda_it}\,u_i\,v_i'B$$

$v_i'B$ è un prodotto vettore riga per matrice e dipende solo dal sistema. Se $v_i'B=0$, l'$i$-esimo modo **non compare** nella risposta impulsiva dello stato: quella legge temporale non contribuisce a "pesare" l'ingresso (nel senso della [[04 - TDS - Uscita forzata e dalla forma esplicita alla implicita#Uscita forzata|media pesata]] della lezione 4). Se $v_i'B=0$ il modo si dice **non eccitabile**; è **eccitabile** se $v_i'B\neq0$, cioè se compare in $H(t)$.

Infine la risposta impulsiva in uscita, $W(t)=Ce^{At}B+D\delta(t)$. Della sola parte dinamica ($D=0$):

$$Ce^{At}B=\sum_{i=1}^ne^{\lambda_it}\,Cu_i\,v_i'B$$

Qui compaiono **entrambi** i prodotti $Cu_i$ e $v_i'B$, quindi spariscono sia i modi non osservabili sia quelli non eccitabili.

> [!important] Riassunto
> | Evoluzione | Espressione | Modi presenti |
> |---|---|---|
> | libera nello stato | $e^{At}x_0=\sum c_ie^{\lambda_it}u_i$ | tutti (con $c_i\neq0$) |
> | libera in uscita | $Ce^{At}x_0=\sum c_ie^{\lambda_it}Cu_i$ | osservabili ($Cu_i\neq0$) |
> | risposta impulsiva nello stato | $e^{At}B=\sum e^{\lambda_it}u_iv_i'B$ | eccitabili ($v_i'B\neq0$) |
> | risposta impulsiva in uscita | $Ce^{At}B=\sum e^{\lambda_it}Cu_iv_i'B$ | osservabili **ed** eccitabili |

> [!quote] Dal libro
> Con autovalori reali e distinti il libro dà le stesse condizioni: l'$i$-esimo modo è osservabile se e solo se $Cu_i\neq0$, come si vede da $\Psi(t)=Ce^{At}=\sum e^{\lambda_it}Cu_iv_i'$; nella $W(t)$ compaiono "tutti e soli i modi naturali per i quali $v_i'B\neq0$ e $Cu_i\neq0$". Per i modi pseudoperiodici la condizione è $v_{ka}'B\neq0$ oppure $v_{kb}'B\neq0$ (eccitabilità) e $Cu_{ka}\neq0$ oppure $Cu_{kb}\neq0$ (osservabilità). Queste nozioni anticipano la **raggiungibilità** e l'**osservabilità** dello spazio di stato ([[TDS - Raggiungibilità]], [[TDS - Osservabilità]]). _(libro, §2.4, p. 74)_

Il caso di autovalori multipli, in cui la scelta degli autovettori non è unica, richiede più attenzione: è l'inizio di [[07 - TDS - Autovalori complessi coniugati#Completa osservabilità e completa eccitabilità|lezione 7]].
