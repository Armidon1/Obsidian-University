---
title: Nyquist con poli sull'asse immaginario
aliases:
  - TDS — Nyquist con poli sull'asse immaginario
tags:
  - teoria-dei-sistemi
  - criterio-di-nyquist
  - margine-di-guadagno
  - margine-di-fase
  - stabilita
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 230–241); libro Monaco et al., §8.5.1
---

# Nyquist con poli sull'asse immaginario

> [!abstract] Scopo della lezione
> Si usa il [[35 - TDS - Criterio di Nyquist|criterio di Nyquist]] su esempi concreti e se ne togliono le ipotesi restrittive:
> 1. un esempio completo al variare del guadagno $k$ (positivo e negativo), con il valore critico $\bar k$ trovato dal grafico e **verificato con Routh**;
> 2. il caso in cui $F(s)$ ha **poli nell'origine** (o sull'asse immaginario): si "gira attorno" al polo con un semicerchio di raggio $\varepsilon\to0$, e il diagramma polare si **chiude all'infinito** con uno o più semigiri in senso orario;
> 3. esempi con polo semplice, doppio e triplo in zero;
> 4. il **margine di guadagno** e il **margine di fase**: quanto si può aumentare il guadagno o ruotare la fase prima che il sistema chiuso diventi instabile.
>
> Segue [[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato]]. Indice: [[MOC - Teoria dei Sistemi]].

## Studio della stabilità di un sistema chiuso

Vedi [[TDS - Criterio di Nyquist]].

La funzione di trasferimento di un sistema **ad anello aperto** (i sistemi aperti si chiamano anche "ad anello aperto", quelli chiusi "ad anello chiuso"):

$$W_{ap}(s)=k\,\frac{s+1}{(s+10)^3}=\underbrace{\frac{k}{10^3}}_{K}\cdot\frac{1+s}{\left(1+\frac s{10}\right)^3}$$

Si studia il sistema chiuso in controreazione. Non ci sono poli a parte reale positiva, quindi $P_p=0$. Il diagramma di Bode di $W_{ap}(s)$ con $K=1$ (il diagramma polare si scalerà poi rispetto a $K$):

![[TDS-L36-01.png]]

Il modulo è 0 dB fino a 1, sale con $+20$ dB/dec fino a 10 (zero in $-1$), poi scende con $-40$ dB/dec (polo triplo in $-10$: $+20-60$). La fase sale fino a circa $\frac\pi4$ e poi scende fino a $-\pi$. Il diagramma polare è qualcosa del genere:

![[TDS-L36-08.png]]

A sinistra il tratto $\omega>0$: parte da $(1,0)$, sale con fase positiva (fino a circa $\frac\pi4$), gira e arriva nell'origine con fase $-\pi$ (quindi da sinistra, tangente all'asse reale). A destra il diagramma completo, con il tratto $\omega<0$ (giallo) ribaltato.

**$K>0$.** Si scala il grafico in base a $K$: il punto $-1$ va in $-\frac1K$, e si allontana dal grafico se $K<1$, si avvicina se $K>1$. Poiché la funzione è **tangente all'asse reale** per $\omega=+\infty$ (arriva nell'origine con fase $-\pi$), il punto $-\frac1K$ può essere arbitrariamente vicino all'origine e comunque non entrare nella curva:

![[TDS-L36-09.png]]

Il sistema resta stabile per qualsiasi $K>0$, cioè per qualsiasi guadagno del sistema. Per trovare i valori del $k$ di partenza basta fare $k=K\cdot10^3$; in questo caso il risultato è lo stesso.

**$K<0$.** Si ribaltano gli assi, e il punto $-\frac1K$, a seconda del valore di $K$, può finire dentro la curva. Nel grafico è segnata in giallo la zona in cui cade il punto se $|K|>1$: lì $N^+=1$. Se $|K|$ aumenta, finché il punto resta nella curva si ha $N^+=2$, mentre oltre un certo limite esce dalla curva, dove $N^+=0$:

![[TDS-L36-10.png]]

> [!warning] Precisazione sull'ordine delle zone
> Con $K<0$ il punto critico, negli assi ribaltati, sta in $-\frac{1}{K}=\frac{1}{|K|}>0$ sul semiasse reale **positivo** originale: per $|K|$ piccolo è molto a destra (fuori dalla curva, $N^+=0$), e al crescere di $|K|$ si avvicina all'origine. Il passaggio critico è quando $\frac1{|K|}$ supera il punto $\alpha$ in cui la curva attraversa il semiasse reale positivo. Gli appunti descrivono le zone partendo dall'altro lato; la conclusione (sotto) è la stessa.

Per $K<0$ il sistema è stabile se $K>\bar K$ (cioè $|K|<|\bar K|$) per un certo $\bar K$. In definitiva il sistema è stabile se $K>0$, quindi se $k>0$, oppure se $\bar K<K<0$, cioè $\bar k<k<0$ (con $\bar k=10^3\bar K$).

**Come si trova $\bar K$.** Si torna al diagramma di Bode e si guarda quanto vale il modulo quando la fase vale **0** (per $K<0$ il punto critico è sul semiasse reale positivo, dove la fase di $W_{ap}$ è 0):

![[TDS-L36-02.png]]

Il modulo in quel punto vale circa 10 dB, cioè circa 3,16: è la parte reale della curva quando interseca il semiasse reale positivo (il punto $\alpha$ della figura precedente). Si cerca il $K$, che sarà proprio $\bar K$, tale che il punto $-1$ vada a finire esattamente in $\alpha$:

$$\frac{-1}{\bar K}=\alpha\approx3{,}16\quad\Longrightarrow\quad\bar K\approx-\frac1{3{,}16}\approx-0{,}316$$

Con un grafico più preciso si vedrebbe che il valore effettivo di $\alpha$ è circa $3{,}625$, quindi $\bar K\approx-0{,}276$ e

$$\bar k=1000\,\bar K\approx-276$$

> [!warning] Correzione
> Negli appunti: "è la parte reale della curva quando interseca l'asse **immaginario**" (è l'asse **reale**), "il valore effettivo di $\alpha$ è $-3{,}625$" (è $+3{,}625$, perché $-\frac1{\bar K}=\alpha$ con $\bar K<0$) e "$\bar k=1000\bar K\approx276$" (è $\approx-276$, come confermato da Routh subito dopo).

> [!tip] Il valore esatto
> La fase $\arctan\omega-3\arctan\frac\omega{10}$ si annulla per $\omega^2=24$ ($\omega\approx4{,}9$), dove $|W_{ap}|=\frac{\sqrt{1+24}}{(1+0{,}24)^{3/2}}=\frac{5}{1{,}381}\approx3{,}62$. Quindi $\alpha\approx3{,}62$ e $\bar K\approx-0{,}276$, in accordo con Routh. La lettura "a occhio" dal diagramma asintotico (10 dB) dà solo un ordine di grandezza.

## Verifica della stabilità con Routh

Vedi [[TDS - Criterio di Routh]].

Il denominatore di $W_{ch}(s)$:

$$d_{ch}(s)=d_{ap}(s)+n_{ap}(s)=(s+10)^3+k(s+1)=s^3+30s^2+(300+k)s+(1000+k)$$

Per verificare che le radici siano tutte negative si applica il [[12 - TDS - Criterio di Routh e linearizzazione|criterio di Routh]]. La condizione necessaria (coefficienti tutti positivi) dà già

$$\begin{cases}300+k>0\\1000+k>0\end{cases}\Longrightarrow k>-300$$

Tabella:

| | | |
|---|---|---|
| 3 | 1 | $k+300$ |
| 2 | 30 | $k+1000$ |
| 1 | $\star$ | |
| 0 | | |

$$\star=\frac{\begin{vmatrix}1&k+300\\30&k+1000\end{vmatrix}}{-30}=\frac{k+1000-30k-9000}{-30}=\frac{29k+8000}{30}$$

| | | |
|---|---|---|
| 3 | 1 | $k+300$ |
| 2 | 30 | $k+1000$ |
| 1 | $\frac{29k+8000}{30}$ | |
| 0 | $k+1000$ | |

Tutte permanenze nella prima colonna se

$$\begin{cases}\frac{29k+8000}{30}>0\\k+1000>0\end{cases}\Longrightarrow\begin{cases}k>-\frac{8000}{29}\\k>-1000\end{cases}\Longrightarrow k>-\frac{8000}{29}=\bar k\approx-276$$

È il valore trovato prima.

> [!note] Grafico o Routh?
> Routh dà il valore preciso di $\bar k$, mentre il metodo grafico è spesso molto approssimativo. Ma se il sistema di partenza venisse modificato, con Routh bisognerebbe rifare tutto il calcolo, mentre graficamente basterebbe scalare di nuovo il grafico per avere subito un nuovo valore approssimato di $\bar k$. Il vantaggio è ancora più evidente quando il grado del polinomio è alto.

## Nomenclatura delle $W(s)$

Quando si studiano sistemi complessi conviene non chiamarli $W_1(s),W_2(s),\dots$ ma con un nome significativo: se un sistema è formato da un motore e un treno, è più chiaro chiamare le funzioni di trasferimento $M(s)$ e $T(s)$, e $W(s)$ quella complessiva motore-treno.

In particolare, con sistemi ad anello aperto e chiuso, è uso indicare il sistema **aperto** con $F(s)$ e quello **chiuso** (complessivo) con $W(s)$; gli elementi del sistema aperto si segnano con il pedice $F$, quelli del sistema complessivo senza pedice.

## Caso in cui una radice di $F(s)$ è nulla

Nella lezione precedente si è visto come capire il segno delle radici dal rapporto tra i denominatori

$$\frac{d(s)}{d_F(s)}=1+F(s)\tag{$\clubsuit$}$$

nel caso senza radici nulle. Ora quel caso. Il metodo usato finora **non funziona** così com'è per le radici nulle: per $\omega=-\infty$ la fase del vettore vale $-\frac\pi2$, ma per $\omega=0$ (quando $j\omega$ passa **sopra** la radice) quanto vale la fase? E per $\omega>0$, $\frac\pi2$ o $-\frac{3\pi}2$? Serve una soluzione.

Si prende un punto $j\omega$ sull'asse immaginario. Se invece dell'asse immaginario si scegliesse un'altra curva, il risultato non cambierebbe, **purché tutte le radici restino dalla parte giusta**: quello che conta è che le radici a parte reale negativa si trovino **a sinistra** della curva (e quelle a parte reale positiva a destra):

![[TDS-L36-11.png]]

Ovviamente una curva così non è facile da studiare. Si prende allora una curva più semplice, che vale $j\omega$ ovunque ma "gira intorno" alla radice a parte reale nulla $p_0$, lasciandola a sinistra:

![[TDS-L36-12.png]]

Il "raggiramento" avviene con un raggio $\varepsilon$ abbastanza piccolo da non comprendere radici positive al suo interno; si considera $\varepsilon\to0$. Lasciando $p_0$ a sinistra, la si conta come una radice a parte reale **negativa** (non entra in $P_p$).

**Esempio.** Diagramma di Bode e diagramma polare di

$$F(s)=\frac{1}{s(s+1)}$$

che ha un polo in $-1$ e uno in zero (radice a parte reale nulla):

![[TDS-L36-03.png]]

Nel diagramma polare, quando si disegna, ci si "ferma" poco prima della radice $p_0$ e si riprende poco dopo: il polare ha un tratto che parte all'infinito in basso ($\omega=0^+$) e uno all'infinito in alto ($\omega=0^-$). Unire il punto poco prima di $p_0$ con quello poco dopo con un raggio $\varepsilon$ fa sì che il diagramma polare abbia un collegamento esplicito da $\omega=0^-$ a $\omega=0^+$:

![[TDS-L36-13.png]]

Un altro possibile percorso da $\omega=0^-$ a $\omega=0^+$ sarebbe stato quello tratteggiato. Ma nella figura precedente si aggira il punto **tenendolo sulla sinistra**: anche l'immagine della funzione deve avere l'immagine del punto sulla sinistra. L'immagine di $p_0$ è l'infinito, quindi si sceglie il percorso che "vede l'infinito a sinistra"; percorrendo la linea tratteggiata l'infinito sarebbe a destra, quindi si sceglie l'altro.

Con $\varepsilon$ più piccolo, il "giro" della funzione sarebbe ancora più ampio: più $\varepsilon$ è piccolo, più la curva si avvicina a $p_0$ e più l'immagine va all'infinito. Con $\varepsilon\to0$ il giro diventa **infinitamente grande**, e la possibile intersezione con l'asse reale si sposta infinitamente a destra, fino a non essere più considerata.

> [!important] Chiusura all'infinito
> Per ogni polo nell'origine il diagramma polare si chiude con un **semicerchio di raggio infinito percorso in senso orario** (da $\omega=0^-$ a $\omega=0^+$). Con un polo di molteplicità $h$ in zero, la chiusura è di $h$ semigiri, cioè un angolo di $h\pi$ in senso orario.

Ora si studia la stabilità come per una curva qualsiasi. Se $K>0$, il punto $-\frac1K$ si trova sempre a sinistra della curva e il numero di giri attorno a esso è nullo: per $K$ positivi il sistema resta sempre stabile. Se $K<0$, per qualsiasi valore si ha $N^+=1$: visto che il "giro" della curva è infinitamente lontano, non c'è un punto in cui $-\frac1K$ esca dalla curva. Per $K$ negativi il sistema è sempre instabile.

> [!warning] Precisazione
> Con $K<0$ il punto critico $\frac{1}{|K|}$ è sul semiasse reale positivo, racchiuso dalla chiusura all'infinito, che lo circonda in senso **orario**: il giro conta $N^+=-1$, non $+1$. Comunque sia $N^+\neq P_p=0$, quindi la conclusione degli appunti (instabile per ogni $K<0$) è corretta. Verifica con Routh: $d_{ch}=s^2+s+K$ ha una radice positiva se $K<0$.

> [!quote] Dal libro — singolarità sull'asse immaginario
> "In molte situazioni reali si ha a che fare con funzioni di trasferimento che hanno delle singolarità sull'asse immaginario. In questo caso il diagramma polare non può essere chiuso perché, avvicinandosi $\omega$ alla singolarità, l'ampiezza del diagramma polare tende all'infinito e se il diagramma non è chiuso non si può calcolare il numero di giri attorno al punto $(-1,j0)$. […] La soluzione è modificare il diagramma polare in prossimità dei punti singolari in modo che il risultato sia una curva chiusa." L'esempio del libro è proprio $F(s)=\frac{k}{s(1+\tau s)}$. _(libro, §8.5.1, p. 332)_

## Chiusura con doppio polo in zero

$$F(s)=k\,\frac{s+10}{s^2(s+1)}=10k\,\frac{1+\frac s{10}}{s^2(1+s)}$$

Con $K=10k$, il diagramma di Bode con $K=1$:

![[TDS-L36-04.png]]

Per $\omega\to0^+$ il modulo è infinito e la fase è $-\pi$: il grafico proviene dall'estrema sinistra del piano. Al crescere di $\omega$ il modulo decresce e la fase prima scende leggermente, poi risale fino a tornare a $-\pi$. Con la parte per $\omega<0$ il diagramma polare è approssimativamente:

![[TDS-L36-14.png]]

Va chiuso; stavolta ci sono **due** poli in zero ($s^2$), quindi la variazione di fase dei vettori in quel polo non è $\pi$ ma $2\pi$: nella chiusura bisogna fare **due semigiri**, cioè un giro completo, in senso orario:

![[TDS-L36-15.png]]

I punti segnati in rosso vanno immaginati infinitamente lontani. Attorno al punto $-1$ la funzione fa due giri, entrambi in senso negativo: $N^+=-2$. Per valori di $K$ più grandi il punto si avvicina all'origine ma non esce dalla curva; per valori più piccoli (ma positivi) si sposta a sinistra, ma non uscirà mai dalla curva perché il punto rosso è infinitamente lontano: per qualsiasi $K>0$, $N^+=-2$. Per $K<0$ si considera il punto segnato con 1: lì va a finire $-\frac1K$ quando $K=-1$; la funzione fa un giro in senso negativo, $N^+=-1$, e per lo stesso motivo il punto non può "uscire". Il sistema chiuso è **instabile per ogni $K$**, perché $N^+\neq0$.

> [!tip] Verifica con Routh
> $d_{ch}(s)=s^2(s+1)+k(s+10)=s^3+s^2+ks+10k$. Tabella: $1,\ k;\ 1,\ 10k;\ k-10k=-9k;\ 10k$. Con $k>0$: prima colonna $1,1,-9k,10k$: **due** variazioni, due radici instabili ($N^+=-2=P_p-Z_p$ con $P_p=0$, quindi $Z_p=2$ ✔). Con $k<0$: $1,1,-9k>0,10k<0$: una variazione, una radice instabile ($Z_p=1$ ✔).

## Chiusura con triplo polo in zero

Se nella $F(s)$ invece di $s^2$ ci fosse $s^3$:

$$F(s)=K\,\frac{1+\frac s{10}}{s^3(1+s)}$$

il diagramma di Bode sarebbe:

![[TDS-L36-05.png]]

La fase scende di un altro $-\frac\pi2$: per $\omega\to0^+$ il modulo è infinito e la fase è $-\frac32\pi$. Il diagramma polare per $\omega>0$ è simile al precedente ma ruotato di $-\frac\pi2$; la parte per $\omega<0$, come sempre, è ribaltata:

![[TDS-L36-16.png]]

Con tre poli in zero la chiusura è di $3\pi$: si parte da $\omega=0^-$ e si fa un giro e mezzo ($2\pi+\pi$) in senso orario fino a $\omega=0^+$:

![[TDS-L36-17.png]]

I punti segnati in rosso si trovano all'infinito.

## Altro esempio con polo in zero

$$F(s)=K\,\frac{1}{s(1+s)^2}$$

![[TDS-L36-06.png]]

Per $\omega\to0^+$ la fase è $-\frac\pi2$ e il modulo infinito: si parte dal basso del piano. Poi il modulo decresce e la fase va da $-\frac\pi2$ a $-\frac{3\pi}2$. Il diagramma polare, con la chiusura:

![[TDS-L36-18.png]]

Per $K$ positivi e minori di un certo $\bar K$, il punto critico è nella zona segnata con $A$ in giallo. $\bar K$ è il valore di $K$ per cui il punto è esattamente in $\alpha$; se $K>\bar K$ il punto "entra" nella zona a destra di $\alpha$ (e a sinistra dell'origine), dove $N^+=-2$. Per $K$ negativi il punto è nella zona $B$, e per qualsiasi $K<0$ si ha $N^+=-1$. Il sistema è stabile finché $0<K<\bar K$.

Se $K=\bar K$ si procede come per le radici nulle: si fa "girare intorno" la curva al punto $\alpha$, in modo che, trovandosi esattamente in quel punto, conti come se fosse alla sua sinistra, e quindi $N^+=0$. Però non si può dire che il sistema sia stabile: va "segnato" che è **al più semplicemente stabile** (il sistema chiuso ha radici sull'asse immaginario).

> [!tip] Il valore di $\bar K$
> La fase vale $-\pi$ quando $-\frac\pi2-2\arctan\omega=-\pi$, cioè $\omega=1$; lì $|F|=\frac{1}{1\cdot2}=\frac12$, quindi $\alpha=-\frac12$ e $\bar K=2$. Con Routh: $d_{ch}=s^3+2s^2+s+K$, stabile se $2\cdot1>K$, cioè $0<K<2$ ✔. Per $K=2$ le radici includono $\pm j$.

## Margine di guadagno

Vedi [[TDS - Margini di stabilità]].

D'ora in poi ci si riferisce al punto $-\frac1K$ come $-1$, intendendo che a seconda di $K$ questo punto si può spostare. Nel grafico precedente:

![[TDS-L36-19.png]]

La quantità segnata con $m_g$ si chiama **margine di guadagno**: indica quanta "perturbazione" il sistema sopporta prima di diventare instabile. Se $K$ diventa troppo grande, il punto $-1$ entra nella curva e il sistema diventa instabile; $m_g$ indica di quanto può variare $K$ prima che il punto entri.

Si vede nel diagramma di Bode: quando la fase vale $-\pi$, il modulo vale esattamente $\alpha$ (lì espresso in decibel). $m_g$ è la distanza del modulo (in dB) da 0 dB: se quando la fase è $-\pi$ il modulo vale $-6$ dB, il margine di guadagno è

$$(m_g)_{\text{dB}}=0-(-6\text{ dB})=6\text{ dB}$$

![[TDS-L36-07.png]]

(il diagramma è relativo a un'altra funzione, per accentuare il margine.) Se il modulo in dB alla fase $-\pi$ è **positivo**, il margine di guadagno è negativo e il sistema è già instabile. Il valore effettivo, non in decibel, è il reciproco di $|\alpha|$:

$$m_g=\frac1{|\alpha|}$$

> [!note] Precisazione
> Gli appunti scrivono $m_g=\frac1\alpha$; poiché $\alpha$ è il punto (negativo) in cui la curva attraversa il semiasse reale negativo, la formula va letta con il modulo, $m_g=\frac{1}{|\alpha|}$. È il fattore per cui si può moltiplicare il guadagno prima di arrivare all'instabilità (nell'esempio sopra, $m_g=\bar K=2$).

## Margine di fase

Non solo il modulo può variare: anche la fase potrebbe cambiare in modo da far entrare il punto $-1$ nella curva:

![[TDS-L36-20.png]]

Non ci sono problemi con i vettori arancioni, che restano lontani dal punto critico $-1$; ma il vettore rosso passerebbe esattamente sopra $-1$ (perché ha **modulo 1**), quindi tutti i punti "al di sotto" di quello indicato dal vettore rosso, se ruotati opportunamente, possono rendere instabile il sistema.

Si definisce allora un **margine di fase** $m_\varphi$, il valore massimo di rotazione della fase per cui il sistema resta stabile. Per trovare la fase limite si considerano tutti i vettori di raggio 1 e si escludono quelli di raggio maggiore: graficamente si traccia la circonferenza di raggio 1 centrata nell'**origine**, che interseca la curva polare nei punti in cui il vettore vale 1. Nel diagramma di Bode si cercano i punti in cui il modulo vale 1, cioè 0 dB, e se ne legge la fase; $m_\varphi$ indica quanto può variare la fase prima di arrivare a $-\pi$. Con $\omega_0$ la pulsazione per cui $|F(j\omega_0)|_{\text{dB}}=0$:

$$m_\varphi=\angle F(j\omega_0)-(-\pi)=\angle F(j\omega_0)+\pi$$

> [!warning] Correzione
> Gli appunti dicono di tracciare "la circonferenza di raggio 1 con centro nel punto $-1$": la circonferenza dei punti di modulo 1 (quella dei vettori che partono dall'origine) ha centro nell'**origine** e passa per $-1$. Il margine di fase è l'angolo tra il punto in cui la curva la attraversa e il punto $-1$.

> [!important] I due margini
> | | Si legge dove | Definizione |
> |---|---|---|
> | margine di guadagno $m_g$ | fase $=-\pi$ ($\omega_\pi$) | $(m_g)_{\text{dB}}=-|F(j\omega_\pi)|_{\text{dB}}$, cioè $m_g=\frac1{|F(j\omega_\pi)|}$ |
> | margine di fase $m_\varphi$ | modulo $=0$ dB ($\omega_0$) | $m_\varphi=\angle F(j\omega_0)+\pi$ |
>
> Per un sistema aperto stabile e "ben comportato", il sistema chiuso è stabile se entrambi i margini sono positivi. Più sono grandi, più il sistema chiuso è **robusto** rispetto a incertezze sul guadagno e ritardi (che ruotano la fase).
