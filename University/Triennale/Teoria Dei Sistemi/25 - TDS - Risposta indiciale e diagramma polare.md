---
title: Risposta indiciale e diagramma polare
aliases:
  - TDS — Risposta indiciale e diagramma polare
tags:
  - teoria-dei-sistemi
  - risposta-indiciale
  - risposta-armonica
  - diagramma-polare
  - banda-passante
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 143–150); libro Monaco et al., §4.5.1, §5.1–5.2
---

# Risposta indiciale e diagramma polare

> [!abstract] Scopo della lezione
> 1. La **risposta indiciale** (risposta al gradino) e i suoi parametri: **guadagno**, **tempo di salita**, **tempo di assestamento**, **sovraelongazione**.
> 2. Il loro corrispettivo nella risposta armonica: **banda passante** $B_3$ (rapidità) e **modulo alla risonanza** $M_r$ (smorzamento), con le relazioni empiriche $B_3t_s\simeq3$ e $\frac{1+\hat s}{M_r}\simeq0{,}85$; il **polo dominante**.
> 3. Un'altra rappresentazione della risposta armonica: il **diagramma polare**, la curva di $W_s(j\omega)$ nel piano complesso, con tre esempi.
>
> Collega [[21 - TDS - Risposta a regime permanente]] e i [[24 - TDS - Termine trinomio e risonanza|diagrammi di Bode]]; il diagramma polare servirà per il [[TDS - Criterio di Nyquist|criterio di Nyquist]]. Segue [[26 - TDS - Stati inosservabili]]. Indice: [[MOC - Teoria dei Sistemi]].

## Risposta indiciale

Vedi [[TDS - Risposta indiciale]].

Finora si è rappresentata $W_s(j\omega)=W(s)|_{s=j\omega}$, che se il sistema ammette risposta a regime permanente si chiama risposta armonica, con i diagrammi di Bode (modulo e fase in funzione della variabile reale $\omega$).

Un ingresso costante, $u(t)=\delta_{-1}(t)$, dà un'uscita a regime costante, $y_{RP}(t)=W_s(0)\delta_{-1}(t)$. Ogni sistema che ammette risposta a regime ha quindi una quantità caratteristica, il **guadagno**, che corrisponde a $W_s(0)$: matematicamente, il valore di $W_s(j\omega)$ per $\omega\to0$.

Con un gradino in ingresso, la risposta forzata vale zero in $t=0$ (se $D=0$) e a regime vale $W_s(0)$. Il modo in cui va da 0 a $W_s(0)$ dipende dai termini di cui è composta $W(s)$:

![[TDS-L25-01.png]]

(in arancione un andamento esponenziale, in blu uno oscillante). L'uscita raggiunge il valore esatto $W_s(0)$ solo a tempo infinito; ma dal punto di vista fisico si sceglie un "margine d'errore", e se l'uscita resta in questo margine da un certo istante in poi si dice che ha raggiunto il regime.

- Il primo istante in cui l'uscita **raggiunge** il guadagno $W_s(0)$ si chiama **tempo di salita** $t_s$.
- Il primo istante in cui l'uscita **entra e resta** nel margine d'errore si chiama **tempo di assestamento** $t_a$.
- Per un'uscita come quella blu interessa anche di quanto, dopo aver superato $W_s(0)$, l'uscita se ne discosta (il "picco" $W_{\max}$): si definisce la **sovraelongazione**
  $$\hat s:=\frac{W_{\max}}{W_s(0)}$$

È utile normalizzare l'asse verticale dividendo per $W_s(0)$: la sovraelongazione diventa chiaramente visibile nel grafico, mentre l'asse dei tempi resta inalterato:

![[TDS-L25-02.png]]

> [!warning] Correzione
> Con la definizione $\hat s=\frac{W_{\max}}{W_s(0)}$ il picco normalizzato varrebbe $\hat s$, mentre nella figura degli appunti (e nella formula $\frac{1+\hat s}{M_r}$ più sotto) vale $1+\hat s$. La definizione coerente, che è anche quella del libro, è
> $$\hat s=\frac{W_{\max}-W_s(0)}{W_s(0)}$$
> cioè la differenza tra il massimo e il valore finale, normalizzata al valore finale (spesso espressa in percentuale).

Questi tre parametri ($t_s$, $t_a$, $\hat s$) non fanno parte del regime permanente ma del periodo prima: caratterizzano la **risposta transitoria**. Quando l'ingresso è un gradino, la risposta forzata $y_F(t)$ si indica spesso con $w_{-1}(t)$ e si chiama **risposta indiciale**.

> [!quote] Dal libro — i parametri della risposta indiciale
> "Se i poli della funzione di trasferimento sono a parte reale strettamente negativa, la risposta indiciale tende ad assumere un valore costante al crescere del tempo e pari al guadagno" ($r_0=\lim_{s\to0}s\cdot\frac{W(s)}{s}=W(0)$, teorema del valore finale). Il libro definisce:
> - **tempo di salita** $T_s$: il tempo per passare dal 10% al 90% del valore finale, ovvero il primo istante in cui la risposta assume il valore finale;
> - **tempo di assestamento** $T_a$: il primo istante da cui la risposta differisce dal valore finale meno di $\varepsilon$ (tipicamente il 2% o il 5% di $K$);
> - **sovraelongazione** $s^*$: la differenza tra il valore massimo e il valore finale, normalizzata rispetto al valore finale (Figura 4.1).
>
> Inoltre, con il teorema del valore iniziale, $w_{-1}(0)=W(\infty)$, che vale 0 se $W$ è strettamente propria e $D$ altrimenti. "Un sistema lineare dinamico ad un ingresso costante risponde con un andamento che al crescere del tempo tende ad un valore costante e proporzionale (pari al guadagno K) all'ingresso, ma vi tende con una velocità ($\frac1{T_a}$) e con modalità che dipendono dai poli della $W(s)$." _(libro, §4.5.1, pp. 191–194)_

## Rapidità del sistema nella risposta armonica

Vedi [[TDS - Risposta armonica]].

La rapidità del sistema a rispondere a un certo ingresso si può "misurare" con $t_s$: più è piccolo, meno il sistema ci mette a raggiungere il valore massimo, e più è "rapido". Questo vale per la risposta indiciale; con un ingresso sinusoidale

$$u(t)=\sin\omega t,\qquad\omega\in\mathbb R$$

come si misura la rapidità nel diagramma di Bode? Un sistema è più rapido quando risponde bene anche a pulsazioni molto elevate: se l'ingresso ha frequenza bassa il sistema ha molto tempo per rispondere, se è elevata può "non fare in tempo".

> [!example] La lampada
> Una lampada a incandescenza impiega cinque secondi per accendersi del tutto: se la si accende e la si spegne dopo tre secondi, si spegne senza aver raggiunto la luminosità massima. Una lampada a LED impiega 0,3 secondi: anche premendo l'interruttore due volte al secondo, raggiunge ogni volta la luminosità massima. La lampada a LED è più "rapida", perché reagisce meglio a frequenze maggiori.

Per misurarlo nel diagramma di Bode si prende il guadagno in decibel, $W_s(0)_{\text{dB}}$, e si considerano **tre decibel in meno**: il primo valore di $\omega$ per cui il modulo di $W_s(j\omega)$ è $W_s(0)_{\text{dB}}-3$ dB si chiama **banda passante** $B_3$ (altre notazioni: $\Omega_3$, $\Omega_B$):

![[TDS-L25-03.png]]

Più è basso il tempo di salita $t_s$, più è alta la banda passante $B_3$.

> [!tip] Perché 3 dB
> $-3$ dB corrispondono a un fattore $10^{-3/20}\approx0{,}707=\frac{1}{\sqrt2}$ in ampiezza, cioè metà della potenza: la banda passante è la pulsazione oltre la quale il sistema "lascia passare" meno di metà della potenza del segnale.

## Attrito del sistema nella risposta armonica

La sovraelongazione $\hat s$ è legata all'**attrito** del sistema: una molla allungata e lasciata andare torna verso la posizione di riposo "molleggiandoci intorno" e si ferma dopo un po'; nell'acqua, con più attrito, la molla non molleggia molto, si discosta meno dalla posizione di riposo e si ferma prima.

Nella risposta armonica il parametro legato all'attrito è lo **smorzamento** $\zeta$: più è basso, più nel grafico di $|W_s(j\omega)|_{\text{dB}}$ compare una "pancia" in una certa zona di pulsazioni, cioè il sistema reagisce in modo molto accentuato in quella zona. Si introduce una grandezza che indica quanto vale il massimo del modulo di $W_s(j\omega)$ rispetto al guadagno:

$$M_r:=\frac{|W|_{\max}}{W_s(0)}$$

il **modulo alla risonanza**, dove $|W|_{\max}$ è il valore massimo assunto da $|W_s(j\omega)|$. Qualitativamente: un sistema con risposta indiciale con elevata sovraelongazione avrà una risposta armonica con elevato modulo alla risonanza.

> [!note] Il modulo in decibel
> Indica quanto viene amplificata (o smorzata) una sinusoide in ingresso: se i valori in decibel sono negativi, la sinusoide viene smorzata (il modulo effettivo è minore di 1), altrimenti amplificata. Il massimo $|W|_{\max}$ è il punto in cui la sinusoide viene amplificata di più; con smorzamento molto basso diventa molto alto.

Anche qui si può **normalizzare** l'asse verticale rispetto al guadagno ed esprimerlo in decibel: il grafico "inizia" sempre a 0 dB, la banda passante è la $\omega$ in cui il grafico normalizzato vale esattamente $-3$ dB, e il modulo alla risonanza corrisponde al massimo del grafico.

> [!warning] Attenzione all'ordine
> Prima si normalizza il modulo, poi lo si esprime in decibel: $\left|\frac{W}{W(0)}\right|_{\text{dB}}$, e non $\frac{|W|_{\text{dB}}}{W(0)}$.

## Relazione tra $B_3$ e $t_s$

Per il sistema

$$W(s)=\frac{K}{1+\frac{2\zeta s}{\omega_n}+\frac{s^2}{\omega_n^2}}$$

si trova che il prodotto tra banda passante e tempo di salita è circa costante, in media 3:

$$B_3\,t_s\simeq3$$

e la relazione tra modulo alla risonanza e sovraelongazione è circa

$$\frac{1+\hat s}{M_r}\simeq0{,}85$$

Queste due approssimazioni "empiriche" valgono anche se nella funzione ci sono altri termini con punti di rottura lontani da $\omega_n$ (per esempio termini $1+\tau s$ con $\frac1\tau$ lontano da $\omega_n$). Quindi, per un sistema con tempo di salita di 5 secondi, la banda passante sarà circa $\frac35$ rad/s.

> [!important] Tempo ↔ frequenza
> | Risposta indiciale (tempo) | Risposta armonica (frequenza) | Relazione |
> |---|---|---|
> | guadagno $w_{-1}(\infty)$ | $W_s(0)$ | coincidono |
> | tempo di salita $t_s$ (rapidità) | banda passante $B_3$ | $B_3t_s\simeq3$ |
> | sovraelongazione $\hat s$ (attrito) | modulo alla risonanza $M_r$ | $\frac{1+\hat s}{M_r}\simeq0{,}85$ |

## Risposta indiciale esponenziale

Un sistema con risposta molto più semplice: ingresso a gradino e risposta indiciale con andamento esponenziale semplice:

![[TDS-L25-04.png]]

Per il tempo di assestamento $t_a$ basta scegliere un margine d'errore. La sovraelongazione non c'è, perché il grafico non supera mai $W_s(0)$: $\hat s=0$. Il tempo di salita invece non può essere definito come prima, perché il grafico non raggiunge mai il valore massimo: lo si "adatta" definendolo, in questo caso, come **il tempo che impiega la risposta a raggiungere il 90% del valore massimo**.

Per esempio

$$W(s)=\frac{0{,}5}{s+1}\qquad\Longrightarrow\qquad w_{-1}(t)=0{,}5\,(1-e^{-t})$$

> [!warning] Correzione
> Negli appunti la risposta indiciale è scritta $0{,}5(1-e^{t})$: è $0{,}5(1-e^{-t})$ (da $\frac{0{,}5}{s(s+1)}=0{,}5\big(\frac1s-\frac1{s+1}\big)$).

![[TDS-L25-05.png]]

Il 90% si raggiunge per $1-e^{-t}=0{,}9$, cioè $t_s=\ln10\approx2{,}3$ s (come nel grafico). Il grafico approssimato della risposta armonica:

![[TDS-L25-14.png]]

Il modulo parte da $(0{,}5)_{\text{dB}}$ e scende con $-20$ dB/dec dal punto di rottura $\omega=1$; la banda passante $B_3$ è dove il modulo è $(0{,}5)_{\text{dB}}-3$ dB.

> [!tip] Verifica della relazione $B_3t_s\simeq3$
> Qui $B_3=1$ (il punto di rottura, vedi sotto) e $t_s\approx2{,}3$: il prodotto è $2{,}3$, dello stesso ordine di 3 (la relazione è empirica e tarata sul sistema del secondo ordine).

In generale si può definire il tempo di salita $t_s$ come il tempo impiegato dalla risposta indiciale per raggiungere il **90%** del valore massimo: nel caso di risposte "ondeggianti" (come nel primo esempio) il tempo per raggiungere il 90% è molto vicino a quello per raggiungere il 100%.

Spesso la banda passante del sistema è influenzata solo dai primi poli che "appaiono" sul grafico del modulo, cioè quelli con punto di rottura ($\omega_n$ per i trinomi, $\frac1\tau$ per i binomi) **più piccolo**: si dice che quel polo è il **polo dominante**.

Quando si è approssimato il modulo nel punto di rottura $\frac1\tau$ dei binomi, si era visto che lì valeva circa 3 decibel: quindi **la banda passante $B_3$ coincide con il punto di rottura $\frac1\tau$** (per un sistema con un solo polo).

> [!quote] Dal libro
> "La pulsazione $\omega=\frac1{|\tau|}$ è quella pulsazione in corrispondenza della quale il valore del guadagno del modulo è $-3$ dB se $\tau>0$ […] questa pulsazione coincide, nel caso in esame di una funzione di trasferimento con un solo polo, con la banda passante $B_3$; ai tre dB di attenuazione corrisponde infatti l'attenuazione di 0.707 in termini reali." E sulla risposta indiciale: "la velocità è tanto maggiore quanto più i poli sono negativi, e la modalità è strettamente collegata ai comportamenti oscillatori con piccolo smorzamento." _(libro, §4.5.1, p. 194; §5.2, p. 239)_

## Rappresentazione della risposta armonica nel diagramma polare

Vedi [[TDS - Diagramma polare]].

La risposta armonica è una funzione complessa: per ogni $\omega$ assume un valore complesso. Lo si può rappresentare in due modi, come i numeri complessi: con modulo e fase (i diagrammi di Bode), oppure con parte reale e immaginaria, cioè come una **curva nel piano reale-immaginario**: i **diagrammi polari**.

### Primo esempio: $W(s)=\frac{1}{s+1}$

Il diagramma di Bode (non approssimato):

![[TDS-L25-06.png]]

Per il diagramma polare si prendono modulo e fase per ogni $\omega$ e si traccia il punto nel piano. Per $\omega\to0^+$ la fase è nulla e il modulo è il guadagno $W_s(0)$: il punto è sull'asse reale, in $W_s(0)$. Al crescere di $\omega$ il modulo diminuisce e la fase va verso $-\frac\pi2$:

![[TDS-L25-07.png]]

> [!warning] Correzione
> Gli appunti dicono "la fase **aumenta** fino a $-\frac\pi2$": la fase **diminuisce** da 0 a $-\frac\pi2$ (in valore assoluto aumenta). Infatti la curva sta nel semipiano $\mathrm{Im}<0$.

Nei diagrammi di Bode si sono trascurati i valori negativi di $\omega$, perché non aggiungevano informazioni (il modulo è pari, la fase dispari). Nel diagramma polare invece si aggiungono: se per $\omega=\bar\omega$ si ha modulo $\rho$ e fase $\theta$, per $\omega=-\bar\omega$ si ha modulo $\rho$ e fase $-\theta$. Il grafico si "duplica" **ribaltandosi sull'asse reale**:

![[TDS-L25-08.png]]

> [!tip] È una circonferenza
> $W_s(j\omega)=\frac{1}{1+j\omega}=\frac{1-j\omega}{1+\omega^2}$: con $x=\frac1{1+\omega^2}$, $y=\frac{-\omega}{1+\omega^2}$ si verifica $\big(x-\frac12\big)^2+y^2=\frac14$. Il diagramma polare completo è la circonferenza di centro $\frac12$ e raggio $\frac12$, percorsa da $0^+$ (in $1$) a $+\infty$ (in $0$) nella metà inferiore.

### Secondo esempio: $W(s)=\frac{1}{s(s+1)}$

Il diagramma di Bode (non approssimato):

![[TDS-L25-09.png]]

Per $\omega\to0^+$ il modulo cresce e va all'infinito (una retta che continua verso sinistra), mentre la fase vale $-\frac\pi2$: a $\omega=0^+$ il punto si trova sull'asse immaginario negativo, infinitamente lontano. Al crescere di $\omega$ il modulo diminuisce e la fase va verso $-\pi$: il punto si discosta dall'asse immaginario, ma tocca l'asse reale solo quando il modulo è nullo:

![[TDS-L25-10.png]]

A sinistra $\omega>0$, a destra il diagramma totale (in tratteggio $\omega<0$, ribaltato).

> [!note] Il diagramma fatto in classe
> Quello mostrato dal professore era leggermente diverso: per $\omega\to0^+$ il grafico tendeva ad accostarsi all'asse verticale.
>
> ![[TDS-L25-11.png]]
>
> Quello negli appunti è il grafico effettivo, senza approssimazione: per $\omega\to0^\pm$ la parte reale resta fissa a $-1$. La fase tende a $-\frac\pi2$ tanto velocemente quanto il modulo cresce, e questo "bilanciamento" fa sì che la parte reale resti fissa. Con i grafici approssimati il bilanciamento non c'è e il grafico assomiglia di più a quello del professore.

> [!tip] Verifica
> $W_s(j\omega)=\frac{1}{j\omega(1+j\omega)}=\frac{1}{-\omega^2+j\omega}=\frac{-\omega^2-j\omega}{\omega^4+\omega^2}=-\frac{1}{1+\omega^2}-j\frac{1}{\omega(1+\omega^2)}$. Per $\omega\to0^+$: parte reale $\to-1$, parte immaginaria $\to-\infty$. C'è quindi un **asintoto verticale** in $\mathrm{Re}=-1$, come nel grafico degli appunti.

### Terzo esempio: $W(s)=\frac{s+1}{s^2+1}$

Il numeratore è un binomio con $\tau=1$, al denominatore c'è un trinomio con $\omega_n=1$ e $\zeta=0$ (non c'è il termine in $s$ al primo grado, ma è comunque un trinomio). Il diagramma di Bode (non approssimato):

![[TDS-L25-12.png]]

Per $\omega\to0^+$ il modulo in decibel vale 0, quindi il modulo effettivo vale 1. Al crescere di $\omega$ il modulo va all'infinito (risonanza con $\zeta=0$) mentre la fase si sposta verso $\frac\pi4$; dopo l'asintoto il grafico "sbuca" da sinistra con un angolo di $-\frac{3\pi}{4}$, e per $\omega\to+\infty$ il modulo diventa sempre più piccolo e il grafico va verso l'origine:

![[TDS-L25-13.png]]

Per la parte con $\omega<0$ basta **ribaltare il grafico rispetto all'asse reale**.

> [!warning] Precisazione
> $W(s)=\frac{s+1}{s^2+1}$ ha poli $\pm j$ sull'asse immaginario: il sistema **non** ammette risposta a regime permanente, quindi a rigore $W_s(j\omega)$ non è una "risposta armonica" (vedi la stessa osservazione in [[23 - TDS - Diagrammi di Bode#Esempio pratico|lezione 23]]); il diagramma polare si traccia comunque, e "esplode" per $\omega\to1$. Lo stesso vale per il secondo esempio, con il polo in $s=0$.

> [!quote] Dal libro
> Il libro tratta i diagrammi polari nel capitolo sui sistemi interconnessi, come base del **criterio di Nyquist** per studiare la stabilità di un sistema a retroazione a partire dalla curva di $W(j\omega)$ (vedi [[TDS - Criterio di Nyquist]]). _(libro, §8.5)_
