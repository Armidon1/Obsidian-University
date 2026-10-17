---
title: Principio di separazione
aliases:
  - TDS — Principio di separazione
tags:
  - teoria-dei-sistemi
  - osservatore
  - principio-di-separazione
  - retroazione-dallo-stato
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 260–264); libro Monaco et al., §9.3
---

# Principio di separazione

> [!abstract] Scopo della lezione
> 1. Un **esempio completo** di [[39 - TDS - Osservatore asintotico dello stato|osservatore asintotico]] per un sistema con una parte inosservabile (ma stabile): cambio di coordinate, $K$ con la formula di Ackermann sulla parte osservabile, ritorno alle coordinate originali.
> 2. Si mettono insieme **osservatore** e **retroazione** ([[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato|lezione 37]]): invece dello stato vero (non misurabile) si retroaziona la sua **stima**. Il **principio di separazione** dice che gli autovalori del sistema complessivo sono l'unione di quelli di $A+BF$ e di $A-KC$: i due problemi si risolvono **separatamente**.
> 3. Nel legame ingresso-uscita l'osservatore **non si vede**: $W(s)=C\big(sI-(A+BF)\big)^{-1}B$.
>
> Segue [[41 - TDS - Esercizi di riepilogo finale]]. Indice: [[MOC - Teoria dei Sistemi]].

## Esempio pratico

Vedi [[TDS - Osservatore asintotico]].

Costruire un osservatore asintotico del sistema

$$\begin{cases}\dot x=\begin{pmatrix}-2&-4&-4\\5&-7&-4\\-5&5&2\end{pmatrix}x+\begin{pmatrix}1\\1\\-1\end{pmatrix}u\\[2mm]y=\begin{pmatrix}2&-2&-2\end{pmatrix}x\end{cases}$$

### Cambio di coordinate

Un osservatore con gli autovalori scelti si può costruire **se** il sistema è osservabile (altrimenti bisogna verificare se è comunque possibile). La matrice di osservabilità è

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}2&-2&-2\\-4&-4&-4\\8&24&24\end{pmatrix}$$

Ci sono due colonne uguali (la seconda e la terza): il rango è 2, il nucleo ha dimensione 1 e c'è una parte inosservabile. Un vettore di base del nucleo è $(0,1,-1)'$ (si sottraggono le due colonne uguali):

$$\mathcal I=\mathrm{span}\left\{\begin{pmatrix}0\\1\\-1\end{pmatrix}\right\}$$

Si costruisce $T^{-1}$ con un completamento arbitrario e si fa il cambio di base:

$$T^{-1}=\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}\quad\Longrightarrow\quad T=\begin{pmatrix}0&1&0\\1&0&0\\0&1&1\end{pmatrix}$$

$$TAT^{-1}=\begin{pmatrix}0&1&0\\1&0&0\\0&1&1\end{pmatrix}\begin{pmatrix}-2&-4&-4\\5&-7&-4\\-5&5&2\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}=\begin{pmatrix}5&-7&-4\\-2&-4&-4\\0&-2&-2\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}=\left(\begin{array}{c|cc}-3&5&-4\\\hline0&-2&-4\\0&0&-2\end{array}\right)=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}$$

$\tilde A_{11}$ è la matrice dinamica della parte inosservabile, con unico autovalore $\lambda_1=-3$: la parte inosservabile è **stabile** (il sistema è rilevabile). Gli altri due autovalori si vedono a occhio in $\tilde A_{22}$ (è triangolare): entrambi $\lambda_2=-2$, quindi questo autovalore ha molteplicità 2.

C'è una parte inosservabile, quindi non si può creare un osservatore **esattamente** come si vorrebbe; ma se ne può comunque costruire uno. Anzi, non servirebbe nemmeno costruirne uno diverso dal sistema di partenza ($K=0$), perché tutti gli autovalori sono già a parte reale negativa (vedi [[39 - TDS - Osservatore asintotico dello stato#Stimare lo stato di un sistema|lezione 39]]).

### Costruzione dell'osservatore

In questo esercizio però l'obiettivo è che gli autovalori diversi da $-3$ (cioè $-2$) abbiano modi naturali che vanno a zero almeno come $-3$, o più velocemente: si vogliono autovalori

$$\lambda\in(-\infty,-3]$$

Serve $\tilde C_2$:

$$\tilde C=CT^{-1}=\begin{pmatrix}2&-2&-2\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}=\big(\underbrace{0}_{\tilde C_1}\ \ \underbrace{2\ \ -2}_{\tilde C_2}\big)$$

quindi

$$\tilde A_{22}=\begin{pmatrix}-2&-4\\0&-2\end{pmatrix},\qquad\tilde C_2=\begin{pmatrix}2&-2\end{pmatrix}$$

Si cerca $\tilde K_2$ tale che $\sigma(\tilde A_{22}-\tilde K_2\tilde C_2)\in\mathcal D$. Con $\tilde K_2=p^*(\tilde A_{22})\rho$, si trova prima $\rho$, ultima colonna di $\tilde{\mathcal O}_2^{-1}$, dove $\tilde{\mathcal O}_2$ è la matrice di osservabilità del sottosistema osservabile $(\tilde A_{22},\tilde C_2)$:

$$\tilde{\mathcal O}_2=\begin{pmatrix}\tilde C_2\\\tilde C_2\tilde A_{22}\end{pmatrix}=\begin{pmatrix}2&-2\\-4&-4\end{pmatrix}\quad\Longrightarrow\quad\tilde{\mathcal O}_2^{-1}=\begin{pmatrix}1/4&-1/8\\-1/4&-1/8\end{pmatrix},\qquad\rho=\begin{pmatrix}-1/8\\-1/8\end{pmatrix}$$

Si scelgono come autovalori, per esempio, $-3$ e $-4$:

$$p^*(\lambda)=(\lambda+3)(\lambda+4)=\lambda^2+7\lambda+12$$

$$\tilde K_2=p^*(\tilde A_{22})\rho=\big[\tilde A_{22}^2+7\tilde A_{22}+12I\big]\rho=\left[\begin{pmatrix}4&16\\0&4\end{pmatrix}+7\begin{pmatrix}-2&-4\\0&-2\end{pmatrix}+12\begin{pmatrix}1&0\\0&1\end{pmatrix}\right]\rho=\begin{pmatrix}2&-12\\0&2\end{pmatrix}\begin{pmatrix}-1/8\\-1/8\end{pmatrix}=\begin{pmatrix}5/4\\-1/4\end{pmatrix}$$

La matrice dinamica complessiva, nelle nuove coordinate (con $\tilde K_1=0$):

$$\tilde A-\tilde K\tilde C=\begin{pmatrix}-3&5&-4\\0&-2&-4\\0&0&-2\end{pmatrix}-\begin{pmatrix}0\\5/4\\-1/4\end{pmatrix}\begin{pmatrix}0&2&-2\end{pmatrix}=\begin{pmatrix}-3&5&-4\\0&-2&-4\\0&0&-2\end{pmatrix}-\begin{pmatrix}0&0&0\\0&5/2&-5/2\\0&-1/2&1/2\end{pmatrix}=\begin{pmatrix}-3&5&-4\\0&-9/2&-3/2\\0&1/2&-5/2\end{pmatrix}$$

> [!tip] Verifica
> Il blocco $\begin{psmallmatrix}-9/2&-3/2\\1/2&-5/2\end{psmallmatrix}$ ha traccia $-7$ e determinante $\frac{45}4+\frac34=12$: polinomio $\lambda^2+7\lambda+12$, autovalori $-3$ e $-4$ ✔. Con $-3$ della parte inosservabile, l'errore di stima converge come $e^{-3t}$.

### Ritorno nelle coordinate iniziali

Nel sistema iniziale la nuova matrice dinamica è

$$A-KC=T^{-1}(\tilde A-\tilde K\tilde C)T=\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}\begin{pmatrix}-3&5&-4\\0&-9/2&-3/2\\0&1/2&-5/2\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&0\\0&1&1\end{pmatrix}=\begin{pmatrix}-9/2&-3/2&-3/2\\5&-7&-4\\-9/2&9/2&3/2\end{pmatrix}$$

In alternativa, $\tilde K=TK\iff K=T^{-1}\tilde K$:

$$K=T^{-1}\tilde K=\begin{pmatrix}0&1&0\\1&0&0\\-1&0&1\end{pmatrix}\begin{pmatrix}0\\5/4\\-1/4\end{pmatrix}=\begin{pmatrix}5/4\\0\\-1/4\end{pmatrix}$$

$$A-KC=\begin{pmatrix}-2&-4&-4\\5&-7&-4\\-5&5&2\end{pmatrix}-\begin{pmatrix}5/2&-5/2&-5/2\\0&0&0\\-1/2&1/2&1/2\end{pmatrix}=\begin{pmatrix}-9/2&-3/2&-3/2\\5&-7&-4\\-9/2&9/2&3/2\end{pmatrix}$$

> [!note] Perché $K=T^{-1}\tilde K$
> L'osservatore aggiunge il termine $K(y-Cz)$ all'**equazione di stato**: nelle nuove coordinate l'equazione è moltiplicata a sinistra per $T$, quindi $\tilde K=TK$. È il duale della retroazione, dove invece $\tilde F=FT^{-1}$ (la $F$ moltiplica lo stato a destra).

## Principio di separazione

Vedi [[TDS - Principio di separazione]].

Si è visto come modificare la dinamica di un sistema a partire dal suo stato: sommando all'ingresso esterno $v$ una quantità proporzionale allo stato, $Fx$, si impongono a piacimento gli autovalori della parte eccitabile (raggiungibile). Si è visto anche come stimare lo stato di un sistema che non si può leggere, tramite l'uscita, con un osservatore asintotico (se gli autovalori inosservabili sono a parte reale negativa). Ora si mettono insieme i due risultati per modificare la dinamica di un sistema di cui non si legge lo stato: **invece dello stato del sistema, si usa la sua stima asintotica**, data dall'osservatore.

### Costruzione del sistema totale

Dato

$$\mathcal S:\begin{cases}\dot x=Ax+Bu\\y=Cx\end{cases}\qquad\text{con l'osservatore}\qquad\mathcal O:\begin{cases}\dot z=(A-KC)z+Bu+Ky\\y_z=Cz\end{cases}$$

si collega lo stato dell'osservatore al sistema: l'ingresso di $\mathcal S$ diventa $u=v+Fz$:

![[TDS-L40-01.png]]

$$\begin{cases}\dot x=Ax+Bv+BFz\\\dot z=(A-KC)z+Bv+BFz+KCx\end{cases}$$

Lo stato complessivo è l'aggregato $\begin{psmallmatrix}x\\z\end{psmallmatrix}$:

$$\begin{pmatrix}\dot x\\\dot z\end{pmatrix}=\underbrace{\begin{pmatrix}A&BF\\KC&A-KC+BF\end{pmatrix}}_{A_{tot}}\begin{pmatrix}x\\z\end{pmatrix}+\begin{pmatrix}B\\B\end{pmatrix}v$$

In questa forma non è per niente immediato vedere quali siano gli autovalori di $A_{tot}$. Oltre allo stato $z$ dell'osservatore, però, si conosce bene l'evoluzione dell'**errore** $e=z-x$: si passa dallo stato attuale a quello che mette in evidenza $e$,

$$\begin{pmatrix}x\\z\end{pmatrix}\longrightarrow\begin{pmatrix}x\\e\end{pmatrix}=\begin{pmatrix}x\\z-x\end{pmatrix}$$

con il cambio di coordinate

$$M=\begin{pmatrix}I&0\\-I&I\end{pmatrix},\qquad M\begin{pmatrix}x\\z\end{pmatrix}=\begin{pmatrix}Ix+0z\\-Ix+Iz\end{pmatrix}=\begin{pmatrix}x\\z-x\end{pmatrix},\qquad M^{-1}=\begin{pmatrix}I&0\\I&I\end{pmatrix}$$

La nuova matrice dinamica:

$$MA_{tot}M^{-1}=\begin{pmatrix}I&0\\-I&I\end{pmatrix}\begin{pmatrix}A&BF\\KC&A-KC+BF\end{pmatrix}\begin{pmatrix}I&0\\I&I\end{pmatrix}=\begin{pmatrix}A&BF\\KC-A&A-KC\end{pmatrix}\begin{pmatrix}I&0\\I&I\end{pmatrix}=\begin{pmatrix}A+BF&BF\\0&A-KC\end{pmatrix}$$

È **triangolare a blocchi**: gli autovalori di $A_{tot}$ sono quelli di $A+BF$ e di $A-KC$:

$$\sigma(A_{tot})=\sigma(A+BF)\cup\sigma(A-KC)$$

> [!important] Principio di separazione
> Retroazionando la **stima** $z$ dell'osservatore invece dello stato vero, gli autovalori del sistema complessivo (di dimensione $2n$) sono l'unione di quelli che si avrebbero con la retroazione dallo stato ($A+BF$) e di quelli dell'osservatore ($A-KC$). I due problemi — scegliere $F$ e scegliere $K$ — si risolvono **separatamente** e poi si connettono insieme. Vale per i sistemi lineari.

> [!quote] Dal libro — §9.3
> "Questo fatto è noto come **principio di separazione**. Se il sistema è tutto raggiungibile ed osservabile è possibile scegliendo $F$ e $K$ e fissare in modo arbitrario gli autovalori del sistema di controllo. Per fare questo si possono fissare in modo indipendente gli autovalori di $(A-KC)$ (immaginando di costruire un osservatore) e quelli di $(A+BF)$ (immaginando di assegnare gli autovalori con una reazione dello stato)." Il problema della **stabilizzazione mediante reazione dall'uscita** ammette soluzione se e solo se i sottosistemi non osservabile e non raggiungibile sono asintoticamente stabili: il sistema deve essere **stabilizzabile e rilevabile**. _(libro, §9.3, pp. 348–350)_

Essendo presenti gli autovalori di $A+BF$, è come se si stesse davvero mettendo in ingresso al sistema il suo stato: si riesce a modificarne la dinamica pur avendo solo una stima dello stato effettivo.

Nelle nuove coordinate:

$$\bar B_{tot}=MB_{tot}=\begin{pmatrix}I&0\\-I&I\end{pmatrix}\begin{pmatrix}B\\B\end{pmatrix}=\begin{pmatrix}B\\0\end{pmatrix}$$

L'uscita del sistema complessivo è sempre $y=Cx$:

$$y=Cx=C_{tot}\begin{pmatrix}x\\z\end{pmatrix}=\begin{pmatrix}C&0\end{pmatrix}\begin{pmatrix}x\\z\end{pmatrix},\qquad\bar C_{tot}=C_{tot}M^{-1}=\begin{pmatrix}C&0\end{pmatrix}\begin{pmatrix}I&0\\I&I\end{pmatrix}=\begin{pmatrix}C&0\end{pmatrix}$$

## Osservatore nel legame ingresso-uscita

Le matrici del sistema complessivo nelle nuove coordinate sono

$$\bar A_{tot}=\begin{pmatrix}A+BF&BF\\0&A-KC\end{pmatrix},\qquad\bar B_{tot}=\begin{pmatrix}B\\0\end{pmatrix},\qquad\bar C_{tot}=\begin{pmatrix}C&0\end{pmatrix}$$

La funzione di trasferimento del sistema complessivo è

$$\begin{aligned}W_{tot}(s)&=\bar C_{tot}\big(sI-\bar A_{tot}\big)^{-1}\bar B_{tot}=\begin{pmatrix}C&0\end{pmatrix}\begin{pmatrix}sI-(A+BF)&-BF\\0&sI-(A-KC)\end{pmatrix}^{-1}\begin{pmatrix}B\\0\end{pmatrix}\\&=\begin{pmatrix}C&0\end{pmatrix}\begin{pmatrix}\big(sI-(A+BF)\big)^{-1}&\star\\0&\star\end{pmatrix}\begin{pmatrix}B\\0\end{pmatrix}=C\big(sI-(A+BF)\big)^{-1}B\end{aligned}$$

> [!note] Precisazione
> Negli appunti l'inversa a blocchi è scritta con $\star$ anche nel blocco in basso a sinistra: l'inversa di una matrice triangolare a blocchi superiore è ancora triangolare superiore, quindi quel blocco è **0**. Il risultato non cambia, perché quel blocco moltiplica lo zero di $\bar B_{tot}$.

Questa funzione di trasferimento è **esattamente** quella che si avrebbe mettendo in ingresso lo stato vero, cioè come se l'osservatore non ci fosse: la matrice dinamica sarebbe $A+BF$ e la funzione di trasferimento $C\big(sI-(A+BF)\big)^{-1}B$. Il legame ingresso-uscita **non contiene alcuna informazione sull'osservatore**: la parte dell'osservatore si trova nella parte **non raggiungibile** (o non osservabile) del sistema complessivo.

> [!tip] Perché non raggiungibile
> Nelle coordinate $(x,e)$ l'ingresso $v$ entra solo nell'equazione di $x$ ($\bar B_{tot}=(B;0)$): l'errore evolve con $\dot e=(A-KC)e$, **indipendentemente da $v$**. È esattamente la forma della [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo la raggiungibilità|scomposizione rispetto alla raggiungibilità]]: gli $n$ autovalori dell'osservatore sono modi non raggiungibili e, nella $W(s)$, si cancellano.

> [!quote] Dal libro
> "Si ottiene quindi la risposta impulsiva del sistema $\mathcal S$ a cui sia applicato un feedback dallo stato (e quindi di $\mathcal S_F$). Questo vuol dire che, dal punto di vista del comportamento ingresso-uscita, l'impiego di un qualunque ricostruttore equivale ad effettuare un feedback dallo stato. Com'è possibile questo? Ricordando quanto visto nel Capitolo 8 e pensando al caso più semplice di un ingresso e un'uscita, questo è possibile solo in conseguenza di una cancellazione tra gli autovalori dell'osservatore (di $A-KC$) e gli zeri del sistema complessivo." _(libro, §9.3, p. 350)_
