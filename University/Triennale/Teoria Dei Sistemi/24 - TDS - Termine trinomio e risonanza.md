---
title: Termine trinomio e risonanza
aliases:
  - TDS — Termine trinomio e risonanza
tags:
  - teoria-dei-sistemi
  - diagrammi-di-bode
  - risposta-armonica
  - risonanza
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 135–142); libro Monaco et al., §5.2
---

# Termine trinomio e risonanza

> [!abstract] Scopo della lezione
> Si completano i [[23 - TDS - Diagrammi di Bode|diagrammi di Bode]] con il **termine trinomio** (coppia di radici complesse coniugate):
> - **modulo**: asintoti a 0 dB e $\pm40$ dB/dec da $\omega_n$; vicino a $\omega_n$ c'è un "dosso" (o una "pancia") che dipende dallo **smorzamento** $\zeta$ e, al denominatore, diventa un picco di **risonanza**;
> - **fase**: da 0 a $\pm\pi$, più o meno ripida a seconda di $\zeta$ (uno **scalino** per $\zeta=0$);
> - due **esempi completi**, con la tecnica "somma degli asintoti, poi aggiungo il dosso".
>
> Segue [[25 - TDS - Risposta indiciale e diagramma polare]]. Indice: [[MOC - Teoria dei Sistemi]].

## Grafico del modulo del termine trinomio

Vedi [[TDS - Diagrammi di Bode]].

La scorsa volta si è visto il termine trinomio

$$1\pm2\zeta\frac{s}{\omega_n}+\frac{s^2}{\omega_n^2},\qquad0\le\zeta<1$$

(qui $\zeta$ è preso positivo e il segno sta nel $\pm$; negli appunti lo smorzamento si chiama $z$). Disegnando $W_s(j\omega)$ si disegna in realtà

$$1\pm2\zeta\frac{j\omega}{\omega_n}+\frac{(j\omega)^2}{\omega_n^2}=1-\frac{\omega^2}{\omega_n^2}\pm j\frac{2\zeta\omega}{\omega_n}$$

Il modulo in decibel è

$$|\cdot|_{\text{dB}}=20\log_{10}\sqrt{\left(1-\frac{\omega^2}{\omega_n^2}\right)^2+\frac{4\zeta^2\omega^2}{\omega_n^2}}$$

Non è immediato da disegnare: si ragiona per approssimazioni, come per il binomio.

- Per $\frac{\omega}{\omega_n}\ll1$, cioè $\omega\ll\omega_n$: $|\cdot|_{\text{dB}}\approx20\log_{10}1=0$.
- Per $\omega\gg\omega_n$:
  $$|\cdot|_{\text{dB}}\approx20\log_{10}\sqrt{\left(\frac{\omega^2}{\omega_n^2}\right)^2+\frac{4\zeta^2\omega^2}{\omega_n^2}}\approx20\log_{10}\frac{\omega^2}{\omega_n^2}=40\log_{10}\omega-40\log_{10}\omega_n$$
  Il termine al quadrato diventa molto più grande dell'altro e si trascura (perché $\sqrt{\frac{\omega^2}{\omega_n^2}\big(\frac{\omega^2}{\omega_n^2}+4\zeta^2\big)}\approx\frac{\omega^2}{\omega_n^2}$ con $0\le\zeta<1$). In scala logaritmica è una retta con pendenza **40 dB/dec** che vale zero in $\omega=\omega_n$.

È il **doppio** della pendenza del binomio (e del monomio). Più $\zeta$ è vicino a 1, più la parte immaginaria del numero è "nulla" e più il trinomio assomiglia a **due** radici reali coincidenti: per $\zeta\approx1$ il grafico del trinomio è praticamente il doppio di quello del binomio.

L'errore massimo è proprio in $\omega_n$, dove la funzione vale

$$20\log_{10}\sqrt{\left(1-\frac{\omega_n^2}{\omega_n^2}\right)^2+\frac{4\zeta^2\omega_n^2}{\omega_n^2}}=20\log_{10}\sqrt{4\zeta^2}=20\log_{10}2\zeta$$

Per $\zeta\to1$ il modulo tende a $20\log_{10}2\approx6$ (il doppio del binomio); al diminuire di $\zeta$, per $\zeta=\frac12$ il logaritmo vale zero, e scende sempre di più per $\zeta\to0$; per $\zeta=0$ il logaritmo "vale" $-\infty$ e c'è un asintoto verticale:

![[TDS-L24-01.png]]

Una decade prima e una dopo $\omega_n$ il grafico è praticamente sugli asintoti; bisogna stare attenti alle somme vicino a $\omega_n$. Per $\zeta\approx1$ il grafico assomiglia al doppio di quello del binomio. Se le radici complesse sono al **denominatore**, il grafico si ribalta:

![[TDS-L24-02.png]]

La risposta armonica in $\omega=\omega_n$ ha un valore molto alto: il sistema tende a reagire di più se la pulsazione in ingresso si avvicina alla **pulsazione naturale** $\omega_n$ (da cui il nome). È il fenomeno della **risonanza**. Al variare di $\zeta$ cambia la risposta; per questo $\zeta$ si chiama **smorzamento**. Fisicamente è impossibile che lo smorzamento sia esattamente zero.

> [!tip] Come sommare i moduli
> La somma è semplice vicino agli asintoti (una decade prima e una dopo $\omega_n$); ma per valori di $\zeta$ lontani da 0,5 può essere difficile sommare il "dosso" nel disegno. Suggerimento: si fa la somma con il grafico **approssimato agli asintoti** e, ottenuta la funzione finale, si "aggiunge" il dosso (la "pancia" della funzione in $\omega=\omega_n$), un po' a occhio.

> [!quote] Dal libro — trinomio e risonanza
> Al denominatore $M_{\text{dB}}=-20\log_{10}\sqrt{\big(1-\frac{\omega^2}{\omega_n^2}\big)^2+\frac{4\zeta^2}{\omega_n^2}\omega^2}$; in $\omega=\omega_n$ vale $-20\log_{10}2|\zeta|$, si annulla per $|\zeta|=0{,}5$, e per $|\zeta|=1$ vale $-6$ dB, "due volte il valore del termine binomio corrispondente". Asintoticamente: 0 per $\omega\ll\omega_n$, retta a $-40$ dB/decade per $\omega\gg\omega_n$, e l'andamento effettivo coincide con quello asintotico già a una decade da $\omega_n$. "Se lo smorzamento $\zeta$ è basso si ha in prossimità di $\omega_n$ una **risonanza**, un'amplificazione della risposta; l'amplificazione diventa infinita se $\zeta=0$" (Figure 5.10 e 5.11 del libro). _(libro, §5.2, pp. 241–243)_

> [!example] Dal libro — Esempio 5.2.2 (massa-molla-smorzatore)
> $W(s)=\frac1K\cdot\frac{1}{\frac Mks^2+\frac bks+1}$ ha $\omega_n=\sqrt{k/M}$ e $\zeta=\frac{b}{2\sqrt{kM}}$. Con $M=10^4$ kg, $k=10^6$ N/m: $\omega_n=10$ rad/s. Con $b=10^4$, $\zeta=0{,}05$; con $b=10^2$, $\zeta=0{,}0005$. Sollecitando proprio a $\omega=\omega_n$ con una forza di 100 N si ottiene a regime un'oscillazione di $10^{-3}$ m (1 mm) nel primo caso e di **10 cm** nel secondo: con poco smorzamento la risonanza amplifica moltissimo. È il fenomeno che conta nelle strutture "ampie luci/flessibili". _(libro, §5.2, p. 244)_

## Grafico della fase del termine trinomio

$$\angle(\cdot)=\pm\arctan\frac{2\zeta\frac{\omega}{\omega_n}}{1-\frac{\omega^2}{\omega_n^2}}$$

- Per $\omega\ll\omega_n$ il numeratore tende a zero: $\pm\arctan(0)=0$.
- Man mano che $\omega$ cresce, $\frac{\omega}{\omega_n}$ si avvicina a 1, fino a quando il denominatore si annulla per $\omega=\omega_n$: $\pm\arctan(+\infty)=\pm\frac\pi2$.
- Se $\omega$ cresce ancora, l'argomento diventa negativo. Si considera l'arcotangente con valori da 0 a $\pi$, così che per argomenti negativi assuma valori in $\big(\frac\pi2,\pi\big)$; man mano che $\omega$ cresce l'argomento va a zero (da sinistra) e l'arcotangente va a $\pi$: per $\omega\gg\omega_n$ la fase vale $\pm\pi$.

> [!note] Le due arcotangenti
> La tangente è periodica e per invertirla si **restringe il dominio**: al classico $\big(-\frac\pi2,\frac\pi2\big)$ oppure a $[0,\pi)$. Per esempio $\tan\big(-\frac\pi4\big)=\tan\frac{3\pi}{4}=-1$, quindi $\tan^{-1}(-1)$ può valere $-\frac\pi4$ oppure $\frac{3\pi}4$. In analisi si usa la prima (continua e derivabile in 0); qui serve la seconda, che non è continua in 0 ma descrive correttamente la fase che "prosegue" oltre $\frac\pi2$:
>
> ![[TDS-L24-04.png]]

> [!tip] Senza ambiguità
> Il problema sparisce ragionando sul numero complesso $1-\frac{\omega^2}{\omega_n^2}+j\frac{2\zeta\omega}{\omega_n}$: la parte immaginaria è sempre positiva (con $\zeta>0$), mentre la parte reale passa da positiva a negativa in $\omega_n$. Il punto si sposta quindi dal primo al secondo quadrante, e l'argomento passa con continuità da 0 a $\pi$.

Per $\zeta\approx1$ il grafico è praticamente il doppio di quello del binomio; per $\zeta=0$ i due estremi coincidono e si ha uno **scalino**; per valori intermedi il grafico assume valori intermedi:

![[TDS-L24-03.png]]

Lo si approssima con una funzione che vale 0 prima di un certo valore, $\pi$ dopo un altro, e in mezzo una linea che congiunge gli estremi: questi saranno $0{,}1\,\omega_n$ e $10\,\omega_n$ se $\zeta\approx1$; con $\zeta=0$ si traccia il grafico effettivo, uno scalino. Per valori intermedi di $\zeta$ si traccia la retta "a occhio", regolandosi sui due casi estremi:

![[TDS-L24-05.png]]

> [!warning] Attenzione ai segni
> Questo è il grafico della fase del trinomio nella forma $1+2\zeta\frac{s}{\omega_n}+\frac{s^2}{\omega_n^2}$. Con un meno, $1-2\zeta\frac{s}{\omega_n}+\frac{s^2}{\omega_n^2}$, l'arcotangente diventa negativa e il grafico si **ribalta**; lo stesso succede se il trinomio è al **denominatore**. Se c'è un meno **e** sta al denominatore, il grafico **non** si ribalta (si ribalterebbe due volte).

Sommare le fasi di più trinomi è semplice negli asintoti, ma diventa complicato nella parte con la retta che congiunge gli estremi (che ha una pendenza arbitraria, presa "a occhio"): in quelle parti conviene fare la somma **punto per punto**.

## Esempio pratico

$$W(s)=10\,\frac{s-1}{(s^2+s+1)(s+10)}$$

**Esiste la risposta a regime permanente?** Bisogna guardare i poli e verificare che siano tutti a parte reale negativa. $s+10$ ha radice $\lambda_1=-10$; il trinomio $s^2+s+1$ ha una coppia di radici complesse coniugate, e i suoi coefficienti sono tutti positivi: due permanenze, quindi radici a parte reale negativa. Il sistema può quindi ammettere risposta a regime permanente e, di conseguenza, risposta armonica.

> [!note] Precisazione
> In realtà non è sicuro, perché bisognerebbe conoscere gli autovalori in $\Psi$ (quelli osservabili, che possono non comparire in $W$ se non eccitabili). Ma se viene data una $W(s)$ senza specificare nulla, si può assumere che non sia stato trascurato niente di importante e che $W(s)$ descriva pienamente il sistema.

**Forma di Bode.** Per il numeratore e per $s+10$ è banale; per $s^2+s+1$ si potrebbero calcolare le radici, oppure verificare se è **già** in forma di Bode:

$$1+s+s^2\ \longleftrightarrow\ 1+\frac{2\zeta s}{\omega_n}+\frac{s^2}{\omega_n^2}$$

Si avrebbe $\omega_n=1$; e se anche $\zeta$ è ammissibile ($0\le\zeta<1$) il trinomio è già in forma di Bode. Con $\omega_n=1$, $\frac{2\zeta}{\omega_n}=2\zeta=1$, quindi $\zeta=\frac12$: ammissibile.

$$W(s)=10\,\frac{(-1)(1-s)}{(s^2+s+1)\cdot10\left(1+\frac{s}{10}\right)}=-\frac{1-s}{(s^2+s+1)\left(1+\frac{s}{10}\right)}$$

(stiamo disegnando $W_s(j\omega)$, non esattamente $W(s)$; non serve un passaggio in più per scrivere $W(s)|_{s=j\omega}$, ma concettualmente è quello che si fa.)

**Modulo.** Si segnano i punti di interesse sull'asse $x$: per $1-s$ il punto di rottura è $\frac1\tau=1$; per $1+\frac{s}{10}$, $\frac1\tau=10$; per $s^2+s+1$, $\omega_n=1$. Vicino a $\omega_n$ c'è una "pancia" che dipende da $\zeta$, da riportare poi nel grafico finale: nella somma si considerano solo gli asintoti e i "dossi" si aggiungono alla fine.

![[TDS-L24-06.png]]

![[TDS-L24-07.png]]

Poco prima di 1 c'è la piccola "pancia" della funzione (con $\zeta=0{,}5$ il valore in $\omega_n$ è esattamente 0 dB, ma il massimo è leggermente prima). Tra 1 e 10 si sommano la retta viola ($-40$ dB/dec) e l'arancione ($+20$ dB/dec): risultante $-20$ dB/dec. Dopo $\omega=10$ si aggiunge una retta a $-20$ dB/dec: pendenza complessiva $-40$ dB/dec.

**Fase.**
- $-1$ ha fase $-\pi$;
- nel binomio al numeratore c'è un meno: la fase è circa nulla prima di una decade prima di $\frac1\tau$ (cioè prima di 0,1) e vale $-\frac\pi2$ una decade dopo (dopo 10);
- il binomio al denominatore, lo stesso: vale 0 prima di 1 e $-\frac\pi2$ (al denominatore) dopo 100;
- il trinomio: con $\zeta\approx1$ varrebbe 0 prima di $0{,}1\,\omega_n$ e $-\pi$ (al denominatore) dopo $10\,\omega_n$; con $\zeta=0$ sarebbe lo scalino in $\omega_n$ da 0 a $-\pi$; per $\zeta=0{,}5$ si prende una "via di mezzo".

![[TDS-L24-08.png]]

Per la somma si considerano le parti di grafico in cui si aggiungono nuove linee. Prima di $\omega=0{,}1$ la somma vale $-\pi$; in $\omega=0{,}1$ si aggiunge l'arancione con pendenza "$-20$ dB/dec" (cioè $-\frac\pi4$ per decade), e la risultante ha questa pendenza. Nel punto $\omega=a$ (un punto arbitrario, dove si è fatta partire "a occhio" la retta viola) si aggiunge la viola con pendenza non nota: si fa allora la somma manuale delle rette in $\omega=1$ e si uniscono i puntini; lo stesso per $\omega=b$, $\omega=10$ e $\omega=100$. Alla fine del grafico tutto è piatto.

![[TDS-L24-09.png]]

> [!warning] Correzione
> Negli appunti le pendenze della fase sono espresse in "dB/dec" (per esempio "$-20$ dB/dec", "$\frac\pi4$ dB/dec"): la fase si misura in radianti, quindi le pendenze sono in **rad/decade**. Una rampa che passa da 0 a $-\frac\pi2$ in due decade ha pendenza $-\frac\pi4$ rad/dec.

> [!tip] Partire dalla fine
> Arrivati al "punto problematico" (quello fatto "a occhio", tra $a$ e $b$) conviene ripartire **dalla fine**: si sommano i contributi a $\omega\to\infty$ ($-\pi-\frac\pi2-\frac\pi2-\pi=-3\pi$) e si va a ritroso. Leggendo da destra: prima di tutto è piatto a $-3\pi$; a $\omega=100$ si aggiunge la pendenza della retta gialla, che sale (verso sinistra) di $\frac\pi4$ per decade; a $\omega=10$ si aggiunge un'altra retta di $\frac\pi4$ per decade, e si sale con pendenza $\frac\pi2$ per decade. Ci si ferma a $\omega=b$, si calcola la somma solo nel punto $\omega=1$ e si uniscono i punti.

## Altro esempio

$$W(s)=\frac{10}{1+s+100s^2}$$

Il denominatore è in forma di Bode? $\omega_n^2=\frac1{100}\Rightarrow\omega_n=\frac1{10}$, e $\frac{2\zeta}{\omega_n}=20\zeta=1\Rightarrow\zeta=\frac1{20}$, ammissibile: è già in forma di Bode. Per disegnare il modulo, visto che $\zeta\not\approx1$ e $\zeta\neq0$, si calcola il valore effettivo in $\omega=\omega_n=\frac1{10}$:

$$|\cdot|_{\text{dB}}=-20\log_{10}2\zeta=-20\log_{10}\frac1{10}=20$$

(il meno perché il trinomio è al denominatore). Il modulo del trinomio (arancione) e quello della costante $K=10$, cioè 20 dB (blu):

![[TDS-L24-10.png]]

La cosa più semplice è sommare gli asintoti del trinomio (tratteggiati) con il resto, e solo dopo aggiungere il "picco":

![[TDS-L24-11.png]]

A sinistra la somma degli asintoti (20 dB fino a $0{,}1$, poi $-40$ dB/dec); a destra la somma effettiva, con il picco di risonanza che arriva a $20+20=40$ dB in $\omega_n=0{,}1$.

> [!tip] Interpretazione
> Con $\zeta=0{,}05$ il sistema è molto poco smorzato: una sinusoide a $\omega=0{,}1$ rad/s viene amplificata di un fattore $10^{40/20}=100$, contro il fattore 10 (il guadagno statico) per frequenze basse. È il caso dell'esempio massa-molla-smorzatore del libro con poco attrito.

La prossima volta si vedrà come rappresentare $W_s(j\omega)$ nel piano reale-immaginario invece che nel diagramma di Bode, per avere uno schema compatto dei valori di $W(s)$: [[25 - TDS - Risposta indiciale e diagramma polare]].
