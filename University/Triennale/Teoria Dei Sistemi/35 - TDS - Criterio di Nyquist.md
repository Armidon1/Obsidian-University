---
title: Criterio di Nyquist
aliases:
  - TDS — Criterio di Nyquist
tags:
  - teoria-dei-sistemi
  - criterio-di-nyquist
  - retroazione
  - stabilita
  - diagramma-polare
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 220–229); libro Monaco et al., §8.4–8.5.1
---

# Criterio di Nyquist

> [!abstract] Scopo della lezione
> Nella [[34 - TDS - Sistemi interconnessi#Connessione in controreazione e semplificazioni|lezione precedente]] si è visto che la retroazione **cambia gli autovalori**. Qui si risponde alla domanda pratica: conoscendo il sistema **ad anello aperto** $W_{ap}(s)$, si può sapere se il sistema **ad anello chiuso** $W_{ch}=\frac{W_{ap}}{1+W_{ap}}$ è stabile, **senza** calcolarne gli autovalori?
> 1. si lega il polinomio caratteristico chiuso a quello aperto: $\frac{d_{ch}}{d_{ap}}=1+W_{ap}$;
> 2. si conta la **variazione di fase** di un polinomio lungo l'asse immaginario, che dipende da quante radici ha a parte reale positiva;
> 3. ne segue il **criterio di Nyquist**: si contano i giri del [[25 - TDS - Risposta indiciale e diagramma polare#Rappresentazione della risposta armonica nel diagramma polare|diagramma polare]] di $W_{ap}$ attorno al punto $-1$;
> 4. esempi con uno, due e tre poli, l'effetto di un guadagno $K$ (positivo o negativo) e come contare i giri con una semiretta.
>
> Segue [[36 - TDS - Nyquist con poli sull'asse immaginario]]. Indice: [[MOC - Teoria dei Sistemi]].

## Studio della controreazione elementare

Vedi [[TDS - Retroazione]].

Si considera un sistema in **controreazione elementare**: l'ingresso del sistema è un ingresso esterno $v$ a cui viene combinata l'uscita $y$ del sistema stesso:

![[TDS-L35-01.png]]

Dato

$$\mathcal S:\begin{cases}\dot x=Ax+Bu\\y=Cx\end{cases}\iff\mathcal S:\ Y(s)=W(s)U(s)$$

retroazionandone l'uscita il sistema complessivo diventa, come visto nella scorsa lezione,

$$\mathcal S_{tot}:\begin{cases}\dot x=(A-BC)x+Bv\\y=Cx\end{cases}\iff\mathcal S_{tot}:\ Y(s)=\frac{W(s)}{1+W(s)}V(s)$$

> [!warning] Correzione
> Nella figura degli appunti l'uscita entra nel sommatore con il segno **+**, ma le formule ($A-BC$ e $\frac{W}{1+W}$) sono quelle della **controreazione**, cioè con l'uscita **sottratta**: $u=v-y$. Con il segno + si avrebbe $A+BC$ e $\frac{W}{1-W}$. Il libro usa $u=-y+v$. Qui si segue la controreazione, come nelle formule.

Il primo sistema, $\mathcal S$, si chiama **sistema aperto** (o **ad anello aperto**), perché è il sistema prima che la sua uscita sia riportata all'ingresso: lo si indica con $\mathcal S_{ap}$, con matrice dinamica $A_{ap}$ e funzione di trasferimento $W_{ap}(s)$. Il secondo è il sistema **chiuso** (ad anello chiuso), con matrice dinamica $A_{ch}=A_{ap}-BC$ e funzione di trasferimento

$$W_{ch}(s)=\frac{W_{ap}(s)}{1+W_{ap}(s)}$$

$B$ e $C$ restano invariate e sono uguali per i due sistemi.

Il problema del passaggio dal sistema aperto a quello chiuso è che **cambia la stabilità**. Sarebbe utile capire se, e come, dal sistema aperto si possa dedurre qualcosa sul sistema chiuso. Ovviamente si potrebbe trattare il sistema chiuso come un sistema qualsiasi e studiarne autovalori, proprietà, stabilità; ma questo approccio dipende molto dai dati, e se le informazioni sul sistema aperto cambiassero bisognerebbe rifare tutti i calcoli.

## Stabilità del sistema chiuso per $p=q=1$

Con $p=q=1$, esplicitando numeratore e denominatore di $W_{ap}(s)=\frac{n_{ap}(s)}{d_{ap}(s)}$:

$$W_{ch}(s)=\frac{W_{ap}(s)}{1+W_{ap}(s)}=\frac{\frac{n_{ap}(s)}{d_{ap}(s)}}{1+\frac{n_{ap}(s)}{d_{ap}(s)}}=\frac{\frac{n_{ap}(s)}{d_{ap}(s)}}{\frac{d_{ap}(s)+n_{ap}(s)}{d_{ap}(s)}}=\frac{n_{ap}(s)}{d_{ap}(s)+n_{ap}(s)}$$

Nella costruzione di $W_{ch}(s)$ da $W_{ap}(s)$ **non ci possono essere cancellazioni**, perché altrimenti sarebbero già state fatte in $W_{ap}(s)$: se numeratore e denominatore di $W_{ch}$ avessero un fattore comune, poiché il numeratore è $n_{ap}$ e compare anche al denominatore, $d_{ap}$ dovrebbe avere fattori in comune con $n_{ap}$, e lo si sarebbe semplificato già in $W_{ap}$. Quindi la dimensione del sistema chiuso è uguale a quella del sistema aperto.

Il rapporto tra i due denominatori è

$$\frac{d_{ch}(s)}{d_{ap}(s)}=\frac{d_{ap}(s)+n_{ap}(s)}{d_{ap}(s)}=1+\frac{n_{ap}(s)}{d_{ap}(s)}=1+W_{ap}(s)\tag{$\clubsuit$}$$

Studiando questo rapporto si capisce come si comporta il sistema chiuso a partire dal sistema aperto. Si vuole sapere se le radici del polinomio caratteristico del sistema chiuso sono a parte reale negativa; si fa l'ipotesi che $W_{ap}(s)$ non abbia radici a parte reale nulla.

> [!quote] Dal libro — la stessa relazione nello spazio di stato
> Con $d_{AP}(s)=|sI-A|$ e $d_{CH}(s)=|sI-A+BC|$:
> $$\frac{d_{CH}(s)}{d_{AP}(s)}=\frac{|sI-A|\,|I+(sI-A)^{-1}BC|}{|sI-A|}=|I+C(sI-A)^{-1}B|=|I+F(s)|$$
> (usando $|I+MN|=|I+NM|$), con $F(s)=C(sI-A)^{-1}B$ funzione di trasferimento del sistema in catena aperta. Vale anche con più ingressi e uscite. _(libro, §8.5.1, p. 329)_

### Variazione di fase di un polinomio

Si considerino una radice $p_1$ a parte reale negativa e una $p_2$ a parte reale positiva:

![[TDS-L35-04.png]]

Preso un punto $j\omega$ sull'asse immaginario, la quantità $j\omega-p_1$ è il vettore che va da $p_1$ al punto $j\omega$; lo stesso per $j\omega-p_2$:

![[TDS-L35-05.png]]

Si fa "scorrere" $\omega\in\mathbb R$ da $-\infty$ a $+\infty$, così che $j\omega$ scorra lungo l'asse immaginario, e si osserva la variazione di fase dei due vettori:

![[TDS-L35-06.png]]

Per $\omega=-\infty$ i vettori puntano verticalmente verso il basso, per $\omega=+\infty$ verso l'alto. Il vettore della radice a parte reale **negativa** ruota in senso antiorario, con variazione di fase $\Delta\varphi_1=+\pi$; quello della radice a parte reale **positiva** ruota in senso orario, con variazione $-\pi$. Il ragionamento vale per qualsiasi radice.

Un polinomio $p(s)$ di grado $n$ si scrive $p(j\omega)=k(j\omega-p_1)\cdots(j\omega-p_n)$, e la fase di un prodotto è la somma delle fasi. Se ha $P$ radici a parte reale positiva:

$$\Delta\varphi\big(p(j\omega)\big)=-\pi P+\pi(n-P)=\pi n-2\pi P$$

Studiando la variazione di fase del rapporto ($\clubsuit$), con $Z_p$ il numero di radici a parte reale positiva di $d_{ch}(s)$ e $P_p$ quello di $d_{ap}(s)$ (lo stesso grado $n$):

$$\Delta\varphi\big(d_{ch}(j\omega)\big)=n\pi-2\pi Z_p,\qquad\Delta\varphi\big(d_{ap}(j\omega)\big)=n\pi-2\pi P_p$$

> [!note] Le lettere $P$ e $Z$
> Sono mnemoniche: $d_{ap}$ è al **denominatore**, dove ci sono i **poli** ($P$); $d_{ch}$ è al numeratore del rapporto, dove ci sono gli **zeri** ($Z$).

La variazione di fase del rapporto (fase di un quoziente = differenza delle fasi) è

$$\Delta\varphi\left(\frac{d_{ch}(j\omega)}{d_{ap}(j\omega)}\right)=\Delta\varphi\big(d_{ch}(j\omega)\big)-\Delta\varphi\big(d_{ap}(j\omega)\big)=2\pi(P_p-Z_p)$$

È sempre un multiplo di $2\pi$: tanti "giri" quanta è la differenza $P_p-Z_p$. Il sistema chiuso è stabile se non ci sono radici a parte reale positiva, cioè se $Z_p=0$.

## Studio della stabilità dal diagramma polare di $W_{ap}(s)+1$

Vedi [[TDS - Criterio di Nyquist]].

Per contare la variazione di fase si usa il diagramma polare di $1+W_{ap}(j\omega)$, che è quello di $W_{ap}(j\omega)$ (noto, perché $W_{ap}$ è la funzione di trasferimento prima della chiusura) **traslato di 1 verso destra** (basta aggiungere 1 a tutti i punti). Oppure, più facilmente, si "sposta" l'asse immaginario di 1 verso sinistra e si considera il punto $-1$ sull'asse reale:

![[TDS-L35-07.png]]

Le frecce indicano la direzione da $\omega=-\infty$ a $\omega=+\infty$; la retta tratteggiata è l'asse immaginario "vero" di $1+W_{ap}$, e la variazione di fase di $1+W_{ap}(j\omega)$ attorno all'origine coincide con quella del vettore che va da $-1$ al punto del diagramma di $W_{ap}(j\omega)$. Seguendo il vettore per $\omega$ da $-\infty$ a $+\infty$:

![[TDS-L35-08.png]]

In questo caso la differenza di fase è $\Delta\varphi=\varphi_f-\varphi_i=0$: il vettore non ha compiuto giri, la sua fase si è limitata ad aumentare e diminuire. Se invece il diagramma polare fosse stato

![[TDS-L35-09.png]]

il vettore avrebbe seguito questo percorso:

![[TDS-L35-10.png]]

Il vettore ha girato **due volte** seguendo la curva: $\Delta\varphi=4\pi$. La curva polare è sempre **chiusa**, quindi i giri sono sempre multipli di $2\pi$ (0 incluso). Indicando con $N^+$ il numero di giri in senso **positivo** (antiorario) che il vettore da $-1$ compie attorno al diagramma polare di $W_{ap}(j\omega)$:

$$2\pi(P_p-Z_p)=2\pi N^+\qquad\Longrightarrow\qquad P_p-Z_p=N^+$$

> [!important] Criterio di Nyquist
> Il sistema ad anello chiuso è stabile ($Z_p=0$) se e solo se il numero di giri in senso antiorario del diagramma polare di $W_{ap}(j\omega)$ (per $\omega$ da $-\infty$ a $+\infty$) attorno al punto $-1$ è uguale al numero di poli a parte reale positiva del sistema aperto:
> $$N^+=P_p$$
> $N^+$ può essere negativo, se i giri sono in senso orario: due giri in senso negativo danno $N^+=-2$. Se il sistema aperto è stabile ($P_p=0$), il criterio diventa $N^+=0$ (**forma ridotta**): il diagramma non deve circondare $-1$.

> [!quote] Dal libro — enunciato
> "Questo fornisce la condizione di stabilità del criterio di Nyquist: condizione necessaria e sufficiente per la stabilità asintotica di un sistema a retroazione unitaria è che il numero di giri che il vettore rappresentativo di $1+F(j\omega)$ compie attorno allo zero, ciò che è lo stesso, il numero di giri che il vettore rappresentativo di $F(j\omega)$ compie attorno al punto $(-1,j0)$, quando $\omega$ varia da $-\infty$ a $+\infty$ sia uguale al numero di autovalori a parte reale positiva del sistema in catena diretta." "Il criterio consente di valutare la stabilità del sistema complessivo, a partire dalla conoscenza delle proprietà di stabilità del sistema in catena diretta e dall'esame grafico del comportamento in frequenza." _(libro, §8.5.1, pp. 330–331)_

> [!tip] Perché ci si riconduce sempre a questo schema
> Il libro osserva che le interconnessioni serie e parallelo non modificano gli autovalori (sono "acicliche"); è la presenza di **cicli** (retroazione) a cambiare la dinamica. Qualunque sistema con un ciclo si può ricondurre, per la stabilità, a un sistema a **retroazione unitaria** con in catena diretta la serie dei sottosistemi del ciclo: gli autovalori del sistema complessivo non dipendono da dove si trovano i sottosistemi nel ciclo. _(libro, §8.4–8.5, pp. 325–328)_

## Stabilità di sistemi comuni

**Un polo.** Un sistema aperto stabile:

$$W_{ap}(s)=\frac1{1+s\tau}$$

È stabile, quindi $P_p=0$. Per verificare se il sistema **chiuso** sarà stabile si disegna il diagramma polare, partendo dal diagramma di Bode:

![[TDS-L35-02.png]]

Per $\omega\to0^+$ il modulo è 0 dB (cioè vale 1) e la fase è 0: il punto $(1,0)$. Per $\omega$ crescenti la fase diminuisce fino a $-\frac\pi2$ e il modulo fino a 0 ($-\infty$ dB): un arco che parte da $(1,0)$ e, passando sotto l'asse reale, finisce in $(0,0)$. Con la parte per $\omega<0$:

![[TDS-L35-11.png]]

I giri attorno a $-1$ sono zero, perché $-1$ non è "contenuto" nella curva:

![[TDS-L35-12.png]]

Quindi $N^+=0$, da cui $Z_p=0$: il sistema chiuso resta stabile.

**Due poli.**

$$W_{ap}(s)=\frac1{(1+s\tau_1)(1+s\tau_2)}$$

Il diagramma polare è molto simile a quello della prima figura della sezione precedente: $N^+=0$ e il sistema resta stabile.

**Tre poli.**

$$W_{ap}(s)=\frac1{(1+s\tau_1)(1+s\tau_2)(1+s\tau_3)}$$

Il diagramma di Bode assomiglia a questo:

![[TDS-L35-03.png]]

Per $\omega\to0^+$ si è sempre nel punto $(1,0)$. All'aumentare di $\omega$ fase e modulo scendono finché la fase arriva a $-\frac32\pi$: da $(1,0)$ la funzione "gira intorno" all'origine e finisce per adagiarsi sull'asse immaginario a $-\frac32\pi$. Contando anche la parte negativa:

![[TDS-L35-13.png]]

Il modulo è sempre **decrescente**: se nel tratto positivo la funzione parte da $(1,0)$, non potrà toccare di nuovo l'asse reale (a sinistra) nel punto $-1$, ma lo passerà sicuramente più a destra. Il punto $-1$ sta a sinistra della curva:

![[TDS-L35-14.png]]

I giri attorno a $-1$ sono zero e il sistema continua a essere stabile.

> [!warning] Precisazione
> Che il modulo sia decrescente non basta da solo: quando la curva attraversa il semiasse reale negativo (fase $-\pi$), il modulo vale $|W_{ap}|<1$ solo perché si parte da modulo 1 e si scende. Con un guadagno $K>1$ davanti (sezione seguente) il punto di attraversamento si sposta e può andare oltre $-1$.

## Studio della stabilità in presenza di un fattore $K$

Se compare un coefficiente $K>0$:

$$W_{ap}(s)=\frac{K}{(1+s\tau_1)(1+s\tau_2)(1+s\tau_3)}$$

la fase non cambia (perché $K>0$), ma il modulo nel diagramma di Bode viene **traslato** in alto o in basso a seconda che $K>1$ o $K<1$. Traslare il modulo di $K$ significa che il diagramma polare ha in ogni punto modulo $K$ volte maggiore: il grafico si "gonfia", ed è possibile che, da un certo valore di $K$ in poi, contenga effettivamente il punto $-1$:

![[TDS-L35-15.png]]

> [!warning] Correzione
> Nel disegno degli appunti gli assi sono etichettati al contrario ("Re" sull'asse verticale e "Im" su quello orizzontale): l'asse orizzontale è quello reale.

Per comodità, invece di aumentare la dimensione del grafico, è più semplice **ridurre la scala** di $K$ volte. Con $K=2$ si posiziona il punto 1 in $\frac12$, quindi il punto $-1$ diventa $-\frac12$:

![[TDS-L35-16.png]]

In generale il punto $-1$ va a finire in $-\frac1K$, e basta vedere se il **nuovo** $-1$ è all'interno o all'esterno del grafico. Nel diagramma di Bode si guarda dove la fase vale $-\pi$, e lì quanto vale il modulo in dB: se è negativo, il modulo effettivo è minore di 1 (approfondito nella [[36 - TDS - Nyquist con poli sull'asse immaginario|prossima lezione]]).

Se $K<0$, oltre al fatto che il grafico si scala secondo $|K|$, la fase non è 0 ma $-\pi$: il diagramma di Bode della fase si trasla in basso di $\pi$, e nel diagramma polare questo è una **rotazione** di $\pi$ del grafico stesso. Di nuovo, invece di ruotare il grafico si ruota il sistema di riferimento (gli assi). Con $K=-2$:

![[TDS-L35-17.png]]

Il punto che prima corrispondeva a 1 ora corrisponde a $-2$, quindi il nuovo $-1$ è quello che prima corrispondeva a $+\frac12$. Il verso di percorrenza del grafico **non cambia**, perché si tratta di una rotazione, non di una riflessione.

Al variare di $K$ il punto $-1$ si "sposta" allontanandosi o avvicinandosi al grafico. C'è un valore particolare $\bar K$ oltre il quale $-1$ "entra" nella curva e il sistema diventa instabile: può essere chiesto di trovarlo.

> [!tip] Come si trova $\bar K$
> Si cerca la pulsazione $\omega_\pi$ in cui la fase di $W_{ap}$ (con $K=1$) vale $-\pi$: lì il diagramma attraversa il semiasse reale negativo nel punto $-|W_{ap}(j\omega_\pi)|$. Il sistema chiuso è stabile finché $-\frac1K$ resta a sinistra di questo punto, cioè finché $K<\bar K=\frac1{|W_{ap}(j\omega_\pi)|}$. Nel diagramma di Bode: $\bar K$ in dB è l'opposto del modulo (in dB) letto alla fase $-\pi$, il **margine di guadagno**.
>
> Esempio con $\tau_1=\tau_2=\tau_3=1$, cioè $W_{ap}=\frac{K}{(1+s)^3}$: la fase vale $-\pi$ quando $3\arctan\omega=\pi$, $\omega=\sqrt3$; lì $|W_{ap}|=\frac{1}{(\sqrt{1+3})^3}=\frac18$, quindi $\bar K=8$. Si verifica con Routh: $d_{ch}=(1+s)^3+K=s^3+3s^2+3s+1+K$, stabile se $9>1+K$, cioè $K<8$ ✔.

## Contare i giri con una semiretta

Per contare facilmente il numero di giri attorno a $-1$, si traccia dal punto $-1$ una **semiretta** in una direzione qualsiasi e si contano le intersezioni con la curva del diagramma polare **con segno**: se nel punto d'intersezione la curva attraversa la semiretta "da destra" (guardando la semiretta da $-1$) si conta $+1$, se l'attraversa "da sinistra" si conta $-1$.

![[TDS-L35-18.png]]

Nella figura di sinistra, tracciando la semiretta da $-1$ verso l'esterno della figura non si hanno intersezioni, quindi $N^+=0$; tracciandola verso la curva, la prima intersezione conta $+1$ (da destra) e la seconda $-1$ (da sinistra): la somma è di nuovo 0. Nella figura di destra entrambi gli incroci avvengono da sinistra, quindi si conta $-1$ due volte: $N^+=-1-1=-2$.

> [!note] Il risultato non dipende dalla semiretta
> Qualunque direzione si scelga, la somma con segno è la stessa: è il numero di giri attorno a $-1$ (l'**indice** della curva rispetto al punto). Conviene scegliere la direzione che dà meno intersezioni.

Tutto questo vale con le ipotesi fatte: sistema a un ingresso e un'uscita ($p=q=1$) e nessuna radice sull'asse immaginario (nessuna radice a parte reale nulla). La prima non è un problema, perché nella stragrande maggioranza dei casi si lavora con sistemi a un ingresso e un'uscita; la seconda invece capita spesso, e il modo di trattarla è l'argomento della [[36 - TDS - Nyquist con poli sull'asse immaginario|prossima lezione]].

> [!quote] Dal libro — Figura 8.12
> Per $F(s)=\frac{k}{(1+\tau_1s)(1+\tau_2s)(1+\tau_3s)}$ ($P_P=0$): se il punto $-1$ è esterno (a sinistra) alla curva si ha $N=0=P_P$ e il sistema è stabile; altrimenti $N=-2\neq P_P$ e il sistema chiuso è instabile (con due poli a parte reale positiva). "È usuale nell'impiego del metodo fare riferimento ad un diagramma tracciato e, anziché scalare la curva di un fattore $k$ variabile, valutare la stabilità al variare del guadagno modificando di un fattore inverso la scala sugli assi, ciò che corrisponde a spostare il punto $(-1,j0)$ collocandolo, nella scala originaria, nel punto $(-\frac1k,j0)$." _(libro, §8.5.1, pp. 331–332)_
