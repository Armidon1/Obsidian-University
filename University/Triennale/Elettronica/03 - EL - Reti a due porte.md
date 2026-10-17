---
title: "Reti a due porte"
aliases:
  - "EL — Reti a due porte"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Reti a due porte

> [!abstract]
> Descrivere un circuito dai morsetti permette di collegare modelli senza ricostruirne ogni dettaglio interno.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 24–26.

Precedente: [[02 - EL - Richiami di teoria dei circuiti]] · Successiva: [[04 - EL - Amplificatori]]

## Porte e scelta delle variabili

Per il ripasso: [[EL - Reti a due porte]] · [[EL - Parametri di ammettenza]].

Una porta è una coppia di morsetti con correnti uguali e opposte. Una rete a due porte è descritta dalle tensioni $v_1,v_2$ e dalle correnti $i_1,i_2$, qui entrambe **entranti** nei morsetti positivi. Due variabili si scelgono indipendenti; le altre si esprimono mediante relazioni lineari, quando la rappresentazione scelta esiste.

Con i parametri di ammettenza:
$$\begin{bmatrix}i_1\\i_2\end{bmatrix}=\begin{bmatrix}y_{11}&y_{12}\\y_{21}&y_{22}\end{bmatrix}\begin{bmatrix}v_1\\v_2\end{bmatrix}.$$
I quattro $y_{ij}$ hanno unità S. $y_{11}$ e $y_{21}$ si misurano con $v_2=0$, cioè uscita in corto; $y_{12}$ e $y_{22}$ con $v_1=0$, ingresso in corto. Per esempio $y_{21}=i_2/v_1|_{v_2=0}$ descrive la trasmissione diretta, non un guadagno adimensionale.

_(dispensa, p. 24)_

![[EL-p024-1.png]]

Le due porte hanno correnti di riferimento entranti nei morsetti positivi. _(dispensa, p. 24)_

![[EL-p024-2.png]]

Per i parametri Y si scelgono le tensioni come variabili indipendenti. _(dispensa, p. 24)_

![[EL-p024-3.png]]

Le equazioni matriciali Y legano correnti e tensioni, come trascritto nel testo. _(dispensa, p. 24)_

![[EL-p024-4.png]]

Cortocircuitando la porta 2 si misurano gli effetti della tensione applicata alla porta 1. _(dispensa, p. 24)_

![[EL-p024-5.png]]

Con ingresso in corto si misura il ritorno dalla tensione della porta 2 alla corrente della porta 1. _(dispensa, p. 24)_

![[EL-p024-6.png]]

La prova con uscita in corto permette di ricavare la trasmissione y21. _(dispensa, p. 24)_

![[EL-p024-7.png]]

La prova con ingresso in corto permette di ricavare y22. _(dispensa, p. 24)_

## Parametri di impedenza e parametri ibridi

Per il ripasso: [[EL - Parametri di impedenza]] · [[EL - Parametri ibridi]].

La rappresentazione con impedenze è:
$$v_1=z_{11}i_1+z_{12}i_2,\qquad v_2=z_{21}i_1+z_{22}i_2.$$
Tutti gli $z_{ij}$ sono in $\Omega$. La prima colonna si determina a $i_2=0$, uscita aperta; la seconda a $i_1=0$, ingresso aperto. Se le matrici sono invertibili, $Z=Y^{-1}$.

I parametri ibridi usano invece $i_1$ e $v_2$ indipendenti:
$$v_1=h_{11}i_1+h_{12}v_2,\qquad i_2=h_{21}i_1+h_{22}v_2.$$
Le unità sono rispettivamente $\Omega$, 1, 1, S. Per la prima colonna si pone $v_2=0$; per la seconda $i_1=0$. Il vantaggio di una rappresentazione ibrida è poter scegliere una coppia di variabili adatta al dispositivo e alle misure disponibili.

_(dispensa, p. 25)_

![[EL-p025-1.png]]

Per i parametri Z le variabili indipendenti sono le due correnti. _(dispensa, p. 25)_

![[EL-p025-2.png]]

Le equazioni Z sono trascritte nel testo: gli elementi della matrice hanno unità di impedenza. _(dispensa, p. 25)_

![[EL-p025-3.png]]

Con porta 2 aperta, la corrente della porta 1 determina z11. _(dispensa, p. 25)_

![[EL-p025-4.png]]

Con porta 1 aperta, la corrente della porta 2 determina z12. _(dispensa, p. 25)_

![[EL-p025-5.png]]

La tensione della porta 2 dovuta alla corrente della porta 1, a uscita aperta, ricava z21. _(dispensa, p. 25)_

![[EL-p025-6.png]]

La prova con ingresso aperto ricava z22 dalla porta 2. _(dispensa, p. 25)_

![[EL-p025-7.png]]

Le equazioni H mescolano tensione e corrente, perciò i quattro parametri non hanno tutti la stessa unità. _(dispensa, p. 25)_

![[EL-p025-8.png]]

Il modello ibrido sceglie corrente di ingresso e tensione di uscita come comandi indipendenti. _(dispensa, p. 25)_

![[EL-p025-9.png]]

Uscita in corto: il rapporto tra tensione e corrente d’ingresso è h11. _(dispensa, p. 25)_

![[EL-p025-10.png]]

Ingresso aperto: il rapporto tra le tensioni ricava il ritorno h12. _(dispensa, p. 25)_

![[EL-p025-11.png]]

Uscita in corto: il rapporto delle correnti ricava h21. _(dispensa, p. 25)_

![[EL-p025-12.png]]

Ingresso aperto: il rapporto tra corrente e tensione d’uscita ricava h22. _(dispensa, p. 25)_

## Parametri ibridi inversi e circuiti equivalenti

Per il ripasso: [[EL - Parametri ibridi inversi]].

I parametri ibridi inversi usano $v_1$ e $i_2$ indipendenti:
$$i_1=g_{11}v_1+g_{12}i_2,\qquad v_2=g_{21}v_1+g_{22}i_2.$$
Le unità sono S, 1, 1, $\Omega$. La prima colonna si misura con $i_2=0$, la seconda con $v_1=0$.

| Modello | Variabili dipendenti | Indipendenti | Prove |
|---|---|---|---|
| $Y$ | $i_1,i_2$ | $v_1,v_2$ | Cortocircuiti |
| $Z$ | $v_1,v_2$ | $i_1,i_2$ | Circuiti aperti |
| $H$ | $v_1,i_2$ | $i_1,v_2$ | Uscita in corto, ingresso aperto |
| $G$ | $i_1,v_2$ | $v_1,i_2$ | Uscita aperta, ingresso in corto |

Ogni equazione si traduce in resistenze o ammettenze e generatori controllati. Un termine proporzionale alla variabile della stessa porta descrive un’impedenza; un termine legato all’altra porta descrive trasmissione o retroazione. Attenzione: passando alla corrente **erogata** al carico si usa spesso $i_o=-i_2$; il segno di un guadagno cambia con la convenzione.

_(dispensa, p. 26)_

![[EL-p026-1.png]]

Per il modello G le variabili indipendenti sono tensione di ingresso e corrente di uscita. _(dispensa, p. 26)_

![[EL-p026-2.png]]

Le equazioni G sono trascritte nel testo con le rispettive unità. _(dispensa, p. 26)_

![[EL-p026-3.png]]

Con uscita aperta si ricava l’ammettenza g11. _(dispensa, p. 26)_

![[EL-p026-4.png]]

Con ingresso in corto il rapporto di correnti ricava g12. _(dispensa, p. 26)_

![[EL-p026-5.png]]

Con uscita aperta il rapporto di tensioni ricava g21. _(dispensa, p. 26)_

![[EL-p026-6.png]]

Con ingresso in corto il rapporto tensione-corrente d’uscita ricava g22. _(dispensa, p. 26)_

![[EL-p026-7.png]]

I quattro modelli equivalenti usano impedenze e generatori controllati per riprodurre le equazioni Y, Z, H e G. _(dispensa, p. 26)_

