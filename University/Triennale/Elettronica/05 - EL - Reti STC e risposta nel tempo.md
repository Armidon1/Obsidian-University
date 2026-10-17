---
title: "Reti STC e risposta nel tempo"
aliases:
  - "EL — Reti STC e risposta nel tempo"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Reti STC e risposta nel tempo

> [!abstract]
> Le reti a una costante di tempo collegano filtri in frequenza, transitori esponenziali e deformazione degli impulsi.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 37–46.

Precedente: [[04 - EL - Amplificatori]] · Successiva: [[06 - EL - Retroazione]]

## Una costante di tempo e limiti in frequenza

Per il ripasso: [[EL - Reti STC]].

STC significa **single time constant**. Per una rete RC del primo ordine $\tau=R_{eq}C$; per una RL $\tau=L/R_{eq}$. Si studia una sola variabile di stato indipendente.

Per riconoscere il comportamento si provano i limiti:

| Limite | Condensatore | Induttore |
|---|---|---|
| $\omega\to0$ | Aperto | Cortocircuito |
| $\omega\to\infty$ | Cortocircuito | Aperto |

Nell’RC serie l’uscita su C è passa-basso; su R è passa-alto. La disposizione grafica da sola non è un criterio universale: conta la funzione di trasferimento tra ingresso e uscita scelti.

_(dispensa, p. 37)_

![[EL-p037-1.png]]

Nel passa-basso RC l’uscita è misurata sul condensatore. _(dispensa, p. 37)_

![[EL-p037-2.png]]

Nel passa-alto RC l’uscita è misurata sul resistore. _(dispensa, p. 37)_

## Passa-basso del primo ordine

Per il ripasso: [[EL - Filtro RC passa-basso]].

Applicando il partitore di impedenza al circuito RC:
$$H_{LP}(s)=\frac{K}{1+s\tau},\qquad \omega_0=\frac1\tau,\quad f_0=\frac{1}{2\pi\tau}.$$
Il circuito elementare ha $K=1$. Il modulo è $|K|/\sqrt{1+(\omega\tau)^2}$ e, per $K>0$, la fase è $-\arctan(\omega\tau)$. A frequenze molto basse il modulo tende a $|K|$; oltre il polo scende asintoticamente di 20 dB per decade. Alla frequenza di taglio vale $|K|/\sqrt2$, cioè 3.010 dB sotto il livello in banda, con fase $-45^\circ$.

Il polo è $s=-1/\tau$: lo stesso parametro governa il decadimento nel tempo e il taglio in frequenza. Una risposta più rapida richiede $\tau$ minore e quindi banda maggiore.

_(dispensa, p. 38)_

![[EL-p038-1.png]]

La funzione del passa-basso si ricava con il partitore tra R e l’impedenza di C. _(dispensa, p. 38)_

![[EL-p038-2.png]]

Nel Bode del passa-basso il polo introduce la discesa di 20 dB per decade e il taglio a −3 dB. _(dispensa, p. 38)_

## Passa-alto del primo ordine

Per il ripasso: [[EL - Filtro RC passa-alto]].

Prendendo l’uscita sulla resistenza:
$$H_{HP}(s)=K\frac{s\tau}{1+s\tau},\qquad |H_{HP}(j\omega)|=|K|\frac{\omega\tau}{\sqrt{1+(\omega\tau)^2}}.$$
La continua è annullata dallo zero nell’origine; alle alte frequenze il modulo tende a $|K|$. Sotto il polo la pendenza asintotica è +20 dB/decade. Per $K>0$ la fase passa da $+90^\circ$ a $0^\circ$, con $+45^\circ$ al taglio.

> [!warning] Correzione
> A p. 39 $K$ viene definito come guadagno a $\omega=0$. Per un passa-alto il guadagno in continua è zero: $K$ è il guadagno asintotico alle alte frequenze.

_(dispensa, p. 39)_

![[EL-p039-1.png]]

Il condensatore in serie blocca la continua prima della resistenza d’uscita. _(dispensa, p. 39)_

![[EL-p039-2.png]]

Il Bode del passa-alto sale di 20 dB per decade prima di raggiungere il guadagno asintotico. _(dispensa, p. 39)_

## Gradini e impulsi rettangolari

Per il ripasso: [[EL - Risposta al gradino RC]] · [[EL - Risposta a impulsi rettangolari]].

Per un gradino $V_su(t)$ e condizioni iniziali nulle:
$$v_{LP}(t)=KV_s(1-e^{-t/\tau}),\qquad v_{HP}(t)=KV_se^{-t/\tau}\quad(t>0).$$
Il passa-basso arrotonda il fronte; il passa-alto produce un salto iniziale e poi elimina la componente costante. Per il medesimo RC con $K=1$, KVL impone $v_C+v_R=v_i$: le due risposte sono complementari.

Un impulso rettangolare di durata $T$ si scrive $V_s[u(t)-u(t-T)]$. La risposta è la differenza di due risposte al gradino, una ritardata di $T$. Nel passa-basso, per $t\ge T$:
$$v_o(t)=KV_s(1-e^{-T/\tau})e^{-(t-T)/\tau}.$$
Nel passa-alto, per $t\ge T$:
$$v_o(t)=KV_s(e^{-t/\tau}-e^{-(t-T)/\tau}).$$
Per conservare un impulso con il passa-basso serve $\tau\ll T$; per limitare il calo del livello nel passa-alto serve $\tau\gg T$. Nel primo caso si vuole rapidità; nel secondo una scarica molto lenta durante l’impulso.

> [!warning] Correzione
> A p. 40 il secondo sottotitolo ripete «passa-basso», ma tratta il passa-alto. A pp. 41–42 «impulso» indica un impulso rettangolare di durata finita, non la delta di Dirac. Un gradino non è una sinusoide a frequenza infinita: possiede uno spettro esteso.

_(dispensa, pp. 40–42)_

![[EL-p040-1.png]]

Gli esempi RC e RL sono passa-basso perché conservano l’uscita a bassa frequenza e la annullano nel limite alto. _(dispensa, p. 40)_

![[EL-p040-2.png]]

Gli esempi complementari sono passa-alto: l’uscita si annulla in continua e resta finita nel limite alto. _(dispensa, p. 40)_

![[EL-p040-3.png]]

Il gradino stabilisce il valore costante che il passa-basso dovrà raggiungere. _(dispensa, p. 40)_

![[EL-p040-4.png]]

La carica raggiunge il 63.2% della variazione in una costante di tempo. _(dispensa, p. 40)_

![[EL-p040-5.png]]

Il circuito identifica l’uscita sulla capacità, quindi la risposta non può saltare con correnti finite. _(dispensa, p. 40)_

![[EL-p040-6.png]]

Lo stesso gradino viene applicato al circuito con uscita resistiva. _(dispensa, p. 40)_

![[EL-p040-7.png]]

Nel passa-alto la risposta iniziale decade esponenzialmente verso zero. _(dispensa, p. 40)_

![[EL-p040-8.png]]

Il circuito passa-alto conserva inizialmente la variazione e poi elimina la componente continua. _(dispensa, p. 40)_

![[EL-p041-1.png]]

Le due uscite del medesimo RC si sommano al gradino d’ingresso secondo KVL. _(dispensa, p. 41)_

![[EL-p041-2.png]]

L’impulso rettangolare è la differenza di due gradini separati dal tempo T. _(dispensa, p. 41)_

![[EL-p041-3.png]]

Se tau è molto maggiore di T, l’uscita del passa-basso raggiunge solo una piccola parte del livello prima della scarica. _(dispensa, p. 41)_

![[EL-p041-4.png]]

Se tau è molto minore di T, il passa-basso segue abbastanza fedelmente l’impulso salvo i fronti arrotondati. _(dispensa, p. 41)_

![[EL-p041-5.png]]

Con tau confrontabile con T sono visibili sia il ritardo sia la deformazione del livello. _(dispensa, p. 41)_

![[EL-p042-1.png]]

L’impulso rettangolare fornisce un fronte positivo e uno negativo al passa-alto. _(dispensa, p. 42)_

![[EL-p042-2.png]]

Con tau confrontabile con T il livello cala prima del secondo fronte e poi torna a zero. _(dispensa, p. 42)_

![[EL-p042-3.png]]

Con tau molto maggiore di T il passa-alto conserva meglio il livello durante l’impulso, con piccolo abbassamento. _(dispensa, p. 42)_

![[EL-p042-4.png]]

Con tau molto minore di T il passa-alto risponde soprattutto ai due fronti, generando due picchi opposti. _(dispensa, p. 42)_

![[EL-p042-5.png]]

Il modello in cascata separa risposta alle basse frequenze, guadagno centrale e risposta alle alte frequenze. _(dispensa, p. 42)_

## Esempio di amplificatore a transconduttanza

Per il ripasso: [[EL - Guadagno a centro banda]].

Il circuito ha $G_m=5\,\mathrm{mS}$, $R_s=50\,\Omega$, $R_i=R_o=R_L=10\,\mathrm{k\Omega}$ e $C_L=10\,\mathrm{nF}$. Il generatore controllato assorbe corrente dal nodo d’uscita verso massa, quindi il guadagno è invertente:
$$A_0=-G_m(R_o\parallel R_L)\frac{R_i}{R_s+R_i}
=-25\frac{10000}{10050}\simeq-24.876.$$
Trascurando il partitore d’ingresso si ottiene $-25$, come nel libro. Il condensatore d’uscita realizza un polo passa-basso:
$$\tau=(R_o\parallel R_L)C_L=50\,\mu\mathrm s,\qquad f_H\simeq3.183\,\mathrm{kHz}.$$
Per un gradino di 0.5 V a $t_0=1\,\mathrm{ms}$:
$$v_o(t)\simeq-12.438[1-e^{-(t-t_0)/(50\,\mu\mathrm s)}]\,\mathrm V.$$
Con l’approssimazione $A_0=-25$, il valore finale è −12.5 V. L’assestamento convenzionale a $5\tau$ richiede 250 µs. Questi risultati assumono un modello lineare senza limiti d’uscita; un amplificatore reale va anche verificato contro clipping e limiti di corrente.

> [!warning] Correzione
> A p. 44 si legge $R_i\ll R_s$ per giustificare $v_i\simeq v_s$. La condizione corretta è **$R_i\gg R_s$**, soddisfatta dai valori 10 kΩ e 50 Ω.

_(dispensa, pp. 43–46)_

![[EL-p043-1.png]]

Il generatore controllato assorbe corrente dal nodo d’uscita; CL rende il trasferimento passa-basso. _(dispensa, p. 43)_

![[EL-p043-2.png]]

Aprendo CL per il calcolo del guadagno statico si separano il partitore d’ingresso e il parallelo d’uscita. _(dispensa, p. 43)_

![[EL-p044-1.png]]

Il verso del generatore di corrente rende negativa la tensione del nodo rispetto a massa. _(dispensa, p. 44)_

![[EL-p044-2.png]]

Il guadagno negativo inverte il segnale e ne aumenta l’ampiezza. _(dispensa, p. 44)_

![[EL-p045-1.png]]

L’ingresso dell’esercizio è un gradino di 0.5 V applicato a 1 ms. _(dispensa, p. 45)_

![[EL-p045-2.png]]

La corrente comandata passa al valore costante di 2.5 mA nell’approssimazione che trascura il partitore d’ingresso. _(dispensa, p. 45)_

![[EL-p045-3.png]]

Con sorgenti indipendenti annullate la capacità vede Ro in parallelo a RL. _(dispensa, p. 45)_

![[EL-p046-1.png]]

L’uscita tende esponenzialmente a −12.5 V nell’approssimazione del libro, con durata convenzionale del transitorio di cinque tau. _(dispensa, p. 46)_

