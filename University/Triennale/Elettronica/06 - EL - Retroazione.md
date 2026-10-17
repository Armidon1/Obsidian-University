---
title: "Retroazione"
aliases:
  - "EL — Retroazione"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Retroazione

> [!abstract]
> La retroazione scambia parte del guadagno con precisione, banda e controllo delle impedenze; la stabilità va comunque verificata.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 47–51.

Precedente: [[05 - EL - Reti STC e risposta nel tempo]] · Successiva: [[07 - EL - Amplificatori operazionali]]

## Anello e guadagno retroazionato

Per il ripasso: [[EL - Guadagno di anello]] · [[EL - Retroazione positiva e negativa]].

Una rete di retroazione preleva una parte dell’uscita e la riporta al confronto con l’ingresso. Con retroazione negativa:
$$x_i=x_s-\beta x_o,\qquad x_o=Ax_i.$$
Sostituendo e raccogliendo $x_o$:
$$A_f=\frac{x_o}{x_s}=\frac{A}{1+A\beta}.$$
Il prodotto $T=A\beta$ è il guadagno d’anello nella convenzione con sommatore sottrattivo; $1+T$ è il fattore di retroazione. Se $|T|\gg1$ e l’anello è stabile, $A_f\simeq1/\beta$: il guadagno dipende soprattutto dalla rete di ritorno.

Con segno positivo al sommatore il denominatore diventa $1-A\beta$. La retroazione positiva è utilizzabile per isteresi e oscillazioni; non basta però la sua presenza a garantire un’oscillazione.

> [!warning] Correzione
> Le affermazioni di pp. 47–48 secondo cui la retroazione negativa è sempre stabilizzante e $1+A\beta$ è sempre maggiore di 1 valgono soltanto nel modello statico con segni opportuni. In frequenza $A\beta$ è complesso: ritardi e poli possono rendere instabile anche un anello nominalmente negativo.

_(dispensa, pp. 47–48)_

![[EL-p047-1.png]]

La rete di ritorno preleva l’uscita e ne riporta una parte al confronto in serie con la sorgente. _(dispensa, p. 47)_

![[EL-p048-1.png]]

Il nodo di confronto sottrae la replica beta per l’uscita dall’ingresso di comando. _(dispensa, p. 48)_

## Sensibilità e prodotto guadagno-banda

Per il ripasso: [[EL - Sensibilità del guadagno]] · [[EL - Prodotto guadagno-banda]].

Tenendo $\beta$ costante e differenziando $A_f=A/(1+\beta A)$:
$$\frac{dA_f}{A_f}=\frac{1}{1+\beta A}\frac{dA}{A}.$$
La sensibilità relativa alle variazioni di $A$ si riduce del fattore $1+\beta A$. Con $A=10^4$ e $\beta=0.01$, $A_f\simeq99.01$ e una piccola variazione relativa di $A$ si trasferisce all’uscita divisa per 101.

Per un amplificatore a un solo polo e $\beta$ reale costante:
$$A(s)=\frac{A_M}{1+s/\omega_H},\quad
A_f(s)=\frac{A_M}{1+\beta A_M}\frac{1}{1+s/[\omega_H(1+\beta A_M)]}.$$
Quindi il guadagno si riduce e la pulsazione di taglio cresce dello stesso fattore:
$$A_{Mf}\omega_{Hf}=A_M\omega_H.$$
La conservazione del prodotto vale per questo modello; non implica la conservazione dell’area sotto un grafico di Bode.

> [!warning] Correzione
> A p. 49 una frase inverte il confronto tra variazioni relative: è quella di $A_f$ a essere più piccola. Nella prima formula del polo compare inoltre $1+s\omega_H$: la forma dimensionalmente corretta è $1+s/\omega_H$, usata nei passaggi successivi.

_(dispensa, pp. 49–50)_

![[EL-p050-1.png]]

La retroazione negativa riduce il guadagno a bassa frequenza e sposta in alto il taglio nel modello a un polo. _(dispensa, p. 50)_

## Distorsione e impedenze

Per il ripasso: [[EL - Retroazione e impedenze]].

Riducendo il guadagno complessivo si amplia la dinamica d’ingresso corrispondente alla stessa escursione d’uscita. La retroazione può ridurre distorsioni prodotte all’interno dell’anello, ma non supera i limiti di alimentazione o corrente dell’uscita.

Le impedenze cambiano secondo la connessione:

| Operazione | Effetto ideale dell’anello |
|---|---|
| Confronto in serie all’ingresso | $R_{if}\simeq R_i(1+T)$ |
| Confronto in parallelo all’ingresso | $R_{if}\simeq R_i/(1+T)$ |
| Campionamento di tensione all’uscita, in parallelo | $R_{of}\simeq R_o/(1+T)$ |
| Campionamento di corrente all’uscita, in serie | $R_{of}\simeq R_o(1+T)$ |

Un amplificatore di tensione richiede confronto in serie e prelievo di tensione: aumenta la resistenza d’ingresso e diminuisce quella d’uscita. Per un amplificatore di corrente si sceglie l’opposto. Questi fattori presuppongono un modello coerente dell’anello e dei caricamenti; non si ricavano semplicemente sommando due resistenze visibili nel disegno.

_(dispensa, pp. 50–51)_

![[EL-p050-2.png]]

La pendenza non retroazionata è maggiore, quindi lo stesso limite d’uscita corrisponde a un intervallo d’ingresso minore. _(dispensa, p. 50)_

![[EL-p050-3.png]]

Con guadagno ridotto dalla retroazione cresce la dinamica d’ingresso compatibile con gli stessi limiti d’uscita. _(dispensa, p. 50)_

![[EL-p051-1.png]]

I quattro schemi mostrano confronto di tensione o corrente e prelievo in serie o parallelo. _(dispensa, p. 51)_

