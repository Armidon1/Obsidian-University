---
title: Diagrammi di Bode
aliases:
  - TDS — Diagrammi di Bode
tags:
  - teoria-dei-sistemi
  - diagrammi-di-bode
  - risposta-armonica
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 127–134); libro Monaco et al., §5.2
---

# Diagrammi di Bode

> [!abstract] Scopo della lezione
> Si prosegue la costruzione dei **diagrammi di Bode** iniziata in [[22 - TDS - Risposta armonica e forma di Bode]]:
> 1. il **termine binomio** $1\pm s\tau$ (radici reali): **costante di tempo**, diagramma **asintotico** del modulo (0 dB poi +20 dB/dec dal **punto di rottura** $1/\tau$) e della fase (una decade prima e una dopo);
> 2. un **esempio completo** con somma grafica dei termini, modulo e fase;
> 3. **potenze** dei fattori (pendenze e fasi moltiplicate);
> 4. le **radici complesse**: il **termine trinomio**, con **pulsazione naturale** $\omega_n$ e **smorzamento** $\zeta$.
>
> Segue [[24 - TDS - Termine trinomio e risonanza]]. Indice: [[MOC - Teoria dei Sistemi]].

## Grafico delle radici reali nella risposta armonica

Vedi [[TDS - Diagrammi di Bode]].

> [!note] Annotazione di Simone
> In testa alla lezione, in viola: **"binomio $s-s_i\to-s_i\left(1-\frac{s}{s_i}\right)$"**.

La scorsa lezione si sono rappresentati i termini costanti e i termini $s$ (radice nulla). Ora le radici reali. Nella forma di Bode

$$s-s_i\ \longrightarrow\ -s_i\left(1-\frac{s}{s_i}\right)$$

il fattore $-s_i$ va nel coefficiente $K$. Il termine rimanente si scrive in una forma più "standard":

$$1\pm\frac{s}{s_i}\ \longrightarrow\ 1\pm s\tau,\qquad\tau=\frac{1}{|s_i|}$$

La quantità $\tau$ si chiama **costante di tempo**. Per esempio, il fattore $s+3$ in forma di Bode è $3\big(1+\frac s3\big)$: il 3 va in $K$ e $\tau=\frac13$.

> [!note] Annotazioni di Simone
> A mano: "Per la forma di Bode", "A noi interessa questo ora", **"'Costante di Tempo' $\tau=\frac{1}{s_i}$"**.

> [!note] Precisazione
> Gli appunti scrivono $\frac{1}{s_i}=\tau$; il segno è tenuto a parte nel $\pm$, quindi qui $\tau$ è positivo e vale $\frac{1}{|s_i|}$ (il libro invece tiene il segno dentro $\tau$, scrivendo sempre $1+j\omega\tau$ con $\tau$ di segno qualsiasi).

### Modulo

La risposta armonica del fattore (si considera sempre il caso particolare $s=j\omega$) è

$$[1\pm s\tau]_{s=j\omega}=1\pm j\omega\tau,\qquad|1\pm j\omega\tau|_{\text{dB}}=20\log_{10}\sqrt{1+\omega^2\tau^2}$$

Non è una funzione facile da disegnare, quindi se ne studia l'andamento **approssimato**:
- per $\omega\tau\ll1$, cioè $\omega\ll\frac1\tau$, $\omega^2\tau^2$ è trascurabile rispetto a 1 e la funzione vale circa $20\log_{10}1=0$;
- per $\omega\tau\gg1$, cioè $\omega\gg\frac1\tau$, l'1 è trascurabile e la funzione vale circa
  $$20\log_{10}\omega\tau=20\log_{10}\omega+20\log_{10}\tau=20\log_{10}\omega-20\log_{10}\frac1\tau$$
  cioè la retta $20\log_{10}\omega$ (pendenza 20 dB/dec, quella del termine $s$) **traslata** a destra: incrocia l'asse esattamente in $\frac1\tau$.

> [!note] Annotazioni di Simone
> A mano: "Noi consideriamo sempre il caso particolare di una risposta Armonica $s=j\omega$"; "Modulo"; "Piccolo Problema che risolvo per approssimazione"; "asintoto 1: se $\omega\ll\frac1\tau$…", "asintoto 2: se $\omega\gg\frac1\tau$…", "Retta", "Costante"; in fondo: **"stessa forma di $f(x)=x-x_0$ allora è una retta di pendenza 20 dB traslata nel punto d'intersezione in $\frac1\tau$"**.

I due **asintoti** della funzione:

![[TDS-L23-01.png]]

Il punto approssimato peggio è proprio $\omega=\frac1\tau$, dove la funzione vale

$$20\log_{10}\sqrt{1+1}=20\log_{10}\sqrt2\approx3$$

un valore abbastanza trascurabile rispetto ai valori che la funzione assume vicino:

![[TDS-L23-02.png]]

> [!note] Annotazioni di Simone
> "un valore molto piccolo messo a confronto con tutto il grafico", "Possiamo approssimarlo come la successiva Figura".

Per semplicità si assume che $|1\pm j\omega\tau|_{\text{dB}}$ coincida con gli asintoti: per $\omega<\frac1\tau$ vale 0, per $\omega>\frac1\tau$ è la retta con pendenza 20 dB/dec traslata in $\frac1\tau$:

![[TDS-L23-03.png]]

Il punto $\frac1\tau$ si chiama **punto di rottura** (o pulsazione di rottura).

### Fase

$$\angle(1\pm j\omega\tau)=\arctan\frac{\pm\omega\tau}{1}=\pm\arctan\omega\tau$$

(parte immaginaria su parte reale; $\tau$ è positivo, il segno sta nel $\pm$).

> [!note] Annotazioni di Simone
> "IMPORTANTE" sul $\pm$; "τ è un numero positivo"; "Im(binomio)", "Re(binomio)".

Il grafico di $\arctan\omega\tau$:

![[TDS-L23-04.png]]

Sommare moltissime arcotangenti non è immediato: come per il modulo, si approssima. In $\omega=\frac1\tau$ l'arcotangente vale esattamente

$$\arctan\left(\frac1\tau\cdot\tau\right)=\arctan1=\frac\pi4$$

Per $\omega$ molto grande $\arctan\omega\tau\to\frac\pi2$, per $\omega$ molto piccolo ($\omega\to0^+$) $\arctan\omega\tau\to0$ (in scala logaritmica si trascurano i valori negativi a sinistra). Si assume quindi che valga 0 prima di un certo valore e $\frac\pi2$ dopo un altro: per convenzione $\frac{0{,}1}{\tau}$ e $\frac{10}{\tau}$ (una decade prima e una dopo $\frac1\tau$). In mezzo si traccia il segmento che congiunge 0 e $\frac\pi2$ passando per $\frac\pi4$ in $\omega=\frac1\tau$:

![[TDS-L23-05.png]]

> [!note] Annotazioni di Simone
> A mano: "Altro problema che risolviamo per approssimazione"; "non possiamo prendere $\omega\le0$"; "Intervallo in cui la fase passa da 0 a $\frac\pi2$: $\left[\frac{0{,}1}{\tau},\frac{10}{\tau}\right]$"; "Ragionamento fatto per approssimazione ma che nella pratica è molto comodo"; "Grafico relativo a $1+j\omega\tau\Rightarrow+\arctan(\omega\tau)$ ⇓ nel caso di $1-j\omega\tau\Rightarrow-\arctan(\omega\tau)$ il grafico è ribaltato rispetto all'asse delle ascisse"; **"Importantissima Osservazione"**; in rosso: **"Se i termini sono al denominatore: modulo specchiato rispetto asse x, fase"** (specchiata).

Il grafico di $-\arctan\omega\tau$ è lo stesso **ribaltato** rispetto all'asse $x$: vale 0 per $\omega<\frac{0{,}1}{\tau}$, $-\frac\pi2$ per $\omega>\frac{10}{\tau}$, e in mezzo è una retta (in scala logaritmica) che congiunge 0 e $-\frac\pi2$, con $-\frac\pi4$ in $\omega=\frac1\tau$.

> [!note] Precisazione
> Anche se nel grafico sembra una retta, in scala logaritmica è un segmento in $\log_{10}\omega$: quando lo si disegna si tracciano segmenti, ricordando che in realtà sono curve logaritmiche.

> [!important] Riepilogo dei termini elementari
> | Termine | Modulo (asintotico) | Fase (asintotica) |
> |---|---|---|
> | $K$ | $20\log_{10}|K|$ costante | $0$ se $K>0$, $-\pi$ se $K<0$ |
> | $s$ a numeratore | retta $+20$ dB/dec, 0 dB in $\omega=1$ | $+\frac\pi2$ |
> | $s$ a denominatore | retta $-20$ dB/dec, 0 dB in $\omega=1$ | $-\frac\pi2$ |
> | $1+s\tau$ a numeratore | 0 fino a $\frac1\tau$, poi $+20$ dB/dec | da 0 a $+\frac\pi2$ tra $\frac{0{,}1}\tau$ e $\frac{10}\tau$ |
> | $1-s\tau$ a numeratore | come sopra | da 0 a $-\frac\pi2$ |
> | binomi a denominatore | modulo ribaltato ($-20$ dB/dec) | fase ribaltata |

> [!quote] Dal libro — termine binomio
> "Per $\omega$ molto minore di $\frac1{|\tau|}$ il diagramma asintotico coincide con l'asse delle ascisse; una retta con pendenza 20 dB per decade rappresenta il valore del modulo per $\omega\gg\frac1{|\tau|}$ […] La rappresentazione approssimata costituita dalla spezzata a due lati si chiama **diagramma asintotico**." L'errore massimo è nel punto di rottura (+3 dB per un binomio a numeratore, −3 dB a denominatore); per la fase l'errore massimo della spezzata a tre lati è circa 6 gradi ($\arctan0{,}1$) nei suoi punti di rottura. Nel caso di un solo polo, $\omega=\frac1{|\tau|}$ coincide con la **banda passante** $B_3$: i 3 dB di attenuazione corrispondono a un fattore 0,707. _(libro, §5.2, pp. 238–239)_

## Esempio pratico

$$W(s)=\frac{10(s-1)}{s(s+100)}$$

Questa funzione ha un autovalore negativo, $-100$, e uno **nullo** (dal termine $s$). Poiché gli autovalori non hanno tutti parte reale minore di zero, **non esiste risposta a regime permanente** e quindi **non esiste risposta armonica**. Però si può comunque calcolare $W_s(j\omega)$: nulla vieta di calcolare $W(s)$ in $s=j\omega$, e questa funzione sarà utile in futuro; semplicemente, qui non si chiama "risposta armonica". In forma di Bode:

$$W(s)=\frac{10(s-1)}{s(s+100)}=\frac{10\cdot(-1)(1-s)}{s\cdot100\cdot\left(1+\frac{s}{100}\right)}=-\frac{1}{10}\cdot\frac{1-s}{s\left(1+\frac{s}{100}\right)}\quad\Longrightarrow\quad W_s(j\omega)=-\frac1{10}\cdot\frac{1-j\omega}{j\omega\left(1+\frac{j\omega}{100}\right)}$$

> [!note] Annotazioni di Simone
> A mano: "IMPORTANTE"; "Autovalore: 0 ⇒ Re(λ)=0≥0"; **"Perciò non esiste una risposta RP e di conseguenza non esisterà una Risposta armonica. Semplicemente $W(j\omega)$ non si chiamerà come tale, ma ci tornerà utile in futuro"**; "Forma di Bode", "K".

Si disegnano modulo e fase di ciascun termine e si fanno le **somme algebriche** per il grafico complessivo.

### Modulo

> [!note] Annotazione di Simone
> A margine: "Esempio Modulo".

- Il termine costante $-\frac1{10}$ ha modulo $20\log_{10}10^{-1}=-20$ dB; il segno negativo **non influisce** sul modulo (blu).
- Il termine $1-s$ al numeratore ha $\tau=1$: nullo fino a $\frac1\tau=1$, poi sale con pendenza 20 dB/dec (arancione).
- Il termine $s$ al denominatore è una retta con pendenza 20 dB/dec che passa per $\omega=1$; ma essendo al denominatore va **sottratto**, quindi lo si considera come $-s$: retta con pendenza $-20$ dB/dec passante per $\omega=1$ (giallo).
- Il termine $1+\frac{s}{100}$ ha $\tau=\frac1{100}$: nullo fino a $\frac1\tau=100$, poi salirebbe con 20 dB/dec; ma essendo al **denominatore** il disegno è ribaltato e dopo 100 **scende** con $-20$ dB/dec (viola).

![[TDS-L23-06.png]]

Sommandole tutte si ottiene (in nero):

![[TDS-L23-07.png]]

> [!tip] Come fare la somma grafica
> Si tiene conto della posizione iniziale e delle pendenze. Nell'intervallo da 0,01 a 1 la retta viola e quella arancione valgono 0, quindi basta sommare la blu ($-20$) e la gialla: si ottiene una retta con la stessa pendenza della gialla ($-20$ dB/dec) abbassata di 20. Tra 1 e 100 si aggiunge l'arancione, con pendenza $+20$: sommata ai $-20$ già presenti dà una retta **costante**. Oltre 100 si aggiunge anche la viola, con $-20$ dB/dec: la pendenza risultante torna a $-20$ dB/dec. In pratica: **a ogni punto di rottura la pendenza cambia di $\pm20$ dB/dec**.

> [!note] Annotazioni di Simone
> "Somma Grafica"; **"Come fare somma Grafica? Così ↓"**; "Si tiene conto della posizione iniziale e delle pendenze".

### Fase

> [!note] Annotazione di Simone
> A margine: "Esempio Fase".

- Il termine costante è negativo, quindi la sua fase è $-\pi$ (blu).
- Il termine $1-s$ ha fase $-\arctan\omega\tau$ con $\tau=1$ (quindi decrescente): vale 0 prima di 0,1 e $-\frac\pi2$ dopo 10, e in mezzo si congiungono gli estremi (arancione).
- Il termine $s$ ha fase costante $\frac\pi2$; ma essendo al denominatore si ribalta: costante a $-\frac\pi2$ (giallo).
- Il termine $1+\frac{s}{100}$ ha fase $\arctan\omega\tau$ con $\tau=\frac1{100}$, ma è al denominatore e si ribalta: vale 0 prima di $\frac{0{,}1}{\tau}=10$ e $-\frac\pi2$ dopo $\frac{10}{\tau}=1000$, e in mezzo la linea che congiunge gli estremi (viola).

![[TDS-L23-08.png]]

Si sommano le rette (come per il modulo):

![[TDS-L23-09.png]]

> [!note] Annotazioni di Simone
> "Allora è decrescente" (sul $-$ di $-\arctan$); "Somma Grafico"; accanto al livello iniziale: "credo $\frac{3\pi}{2}=-\frac\pi2-\pi$"; in rosso: **"Occhio a non confonderti: prima di $\omega=10$ la linea arancione aveva pendenza $-20$ dB e la linea viola 0 dB; dopo $\omega=10$ la situazione è il viceversa ⇒ la pendenza totale è invariata."**

> [!note] Precisazione
> Il livello iniziale della fase è $-\pi-\frac\pi2=-\frac{3\pi}{2}$ (blu + gialla), come ipotizzato a mano da Simone; nel grafico riepilogativo qui sotto l'asse della fase va infatti da $-\frac{3\pi}2$ a $-\frac{5\pi}2$. L'annotazione sulle pendenze si riferisce alla fase: tra 10 e 1000 una delle due rampe finisce e l'altra comincia (per $\omega\in[10,1000]$ è la viola a scendere), quindi tra 0,1 e 1000 la pendenza complessiva resta quella di una sola rampa.

**Riepilogo.** Il sistema reagisce alle frequenze (al valore di $\omega$) così:

![[TDS-L23-10.png]]

Se si volesse un sistema che **amplifica** una sinusoide in ingresso, servirebbe una pulsazione $\omega<0{,}1$: in quella parte di grafico il modulo in decibel è positivo, quindi il modulo effettivo è maggiore di 1. Per qualsiasi $\omega$ maggiore di 0,1 l'ampiezza della sinusoide si riduce, e più $\omega$ è grande, più l'onda in uscita tende a zero. Per cui, se si vuole che il sistema non oscilli molto, basta scegliere $\omega$ alti.

> [!note] Annotazioni di Simone
> "Considerazioni finali riguardo l'esercizio"; "Per questo abbiamo studiato modulo e fase di $W(j\omega)$".

> [!important] Ogni sistema "taglia" le alte frequenze
> I termini $s$ generano in $W_s(j\omega)$ una retta (logaritmica) crescente, e anche i termini $1\pm s\tau$ sono crescenti, o al più nulli fino a un certo valore: tutti hanno la **stessa pendenza** di 20 dB/dec. Al denominatore diventano **decrescenti**. $W(s)$, in qualsiasi sistema, è **strettamente propria** (più termini al denominatore che al numeratore): quindi $|W_s(j\omega)|$ da un certo punto in poi è **decrescente**. Qualsiasi sistema tende a **non reagire alle alte frequenze**.

> [!note] Annotazione di Simone
> A margine: **"Osservazione importante Generale"**.

## Disegnare potenze dei fattori

Con una potenza di un termine, per esempio

$$W(s)=\frac{10(s-1)}{s^2(s+100)}=-\frac1{10}\cdot\frac{s-1}{s^2\left(1+\frac{s}{100}\right)}$$

il grafico è comunque banale come nell'esempio precedente. La differenza è un fattore $s$ in più al denominatore, quindi si potrebbe disegnare $W_s(j\omega)$ considerandola come $-\frac1{10}\frac{s-1}{s\cdot s\cdot(1+\frac{s}{100})}$, cioè disegnando **due volte** il termine $s$.

Tecnicamente è giusto, ma è sconsigliato: bisognerebbe disegnare rette identiche una sopra l'altra, e con potenze maggiori di 2 è ancora peggio (con $s^5$, cinque rette uguali una sopra l'altra). Conviene disegnare **direttamente** la potenza: si fa subito la somma dei due moduli di $j\omega$ in decibel. Se ogni termine è una retta (decrescente, al denominatore) con pendenza $-20$ dB/dec passante per $\omega=1$, la loro somma è una retta passante per 1 con pendenza $-40$ dB/dec; in generale $s^k$ dà una retta per $\omega=1$ con pendenza $-20k$ dB/dec (al denominatore). Per la **fase** lo stesso: se la fase di $s$ al denominatore è $-\frac\pi2$, quella di $s^2$ è $-\pi$ e quella di $s^k$ è $-k\frac\pi2$.

> [!note] Annotazioni di Simone
> "Problema"; "Soluzione Banale ma sconsigliata"; **"Soluzione Modulo uguali"**; **"SOLUZIONE FASE"**.

> [!warning] Correzione
> Negli appunti il secondo passaggio riporta $\frac{s-1}{s^2(\dots)}$ con il segno davanti come nell'esempio precedente; in realtà, scritto $s-1=-(1-s)$, la forma di Bode è $-\frac1{10}\cdot\frac{-(1-s)}{s^2(1+\frac{s}{100})}=\frac1{10}\cdot\frac{1-s}{s^2(1+\frac s{100})}$. Il segno cambia solo la fase (di $\pi$), non il ragionamento sulle potenze.

Lo stesso vale per qualsiasi altro termine:

$$W(s)=-\frac1{10}\cdot\frac{s-1}{s\left(1+\frac{s}{100}\right)^2}$$

Si "disegna due volte" il termine $1+\frac{s}{100}$: disegnarlo una volta significa una retta nulla fino a 100 e poi decrescente con $-20$ dB/dec (al denominatore); due volte significa nulla fino a 100 e poi $-40$ dB/dec. Allo stesso modo, se la fase va da 0 a $-\frac\pi2$ con una retta in mezzo, disegnarla due volte significa una fase da 0 a $-\pi$ nello stesso intervallo.

## Radici complesse in $W(s)$

Vedi [[TDS - Diagrammi di Bode]].

Ora termini con radici complesse coniugate, del tipo $(s-s_0)(s-s_0^*)$ con $s_0=\alpha+j\omega$:

$$(s-s_0)(s-s_0^*)=\big(s-(\alpha+j\omega)\big)\big(s-(\alpha-j\omega)\big)=\big((s-\alpha)-j\omega\big)\big((s-\alpha)+j\omega\big)=(s-\alpha)^2+\omega^2=s^2-2\alpha s+\underbrace{\alpha^2+\omega^2}_{\rho^2}$$

dove $\rho=\sqrt{\alpha^2+\omega^2}$ è il **modulo** di $s_0$. Essendo $\rho^2$ sempre positivo, il segno della parte reale delle radici dipende dal segno di $\alpha$: se $\alpha<0$ il polinomio $s^2-2\alpha s+\rho^2$ ha tutti coefficienti positivi, cioè due permanenze di segno, e quindi (Routh/Cartesio, [[12 - TDS - Criterio di Routh e linearizzazione|lezione 12]]) due radici a parte reale negativa; altrimenti due radici a parte reale positiva o nulla.

> [!warning] Correzione
> Negli appunti si legge "se $\alpha>0$ si hanno due permanenze di segno e quindi due radici a parte reale negativa". È il contrario: le radici sono $\alpha\pm j\omega$, con parte reale $\alpha$. Con $\alpha<0$ il coefficiente $-2\alpha$ è positivo e ci sono due permanenze; con $\alpha>0$ due variazioni.

> [!note] Annotazione di Simone
> Accanto: **"DAL CRITERIO DI BOH"** (Routh), e sotto $\rho^2$: "Modulo²".

In forma di Bode:

$$\rho^2\left(1-\frac{2\alpha s}{\rho^2}+\frac{s^2}{\rho^2}\right)$$

> [!note] Annotazione di Simone
> **"Forma di Bode — ABBIAMO UN TRINOMIO!!"**.

Si guardi il termine $-\frac{2\alpha s}{\rho^2}$, rappresentando $s_0$ e $s_0^*$ nel piano complesso:

![[TDS-L23-11.png]]

$s_0$ ha parte reale $\alpha$ (arancione) e parte immaginaria $\omega$ (blu); $\rho$ (verde) è la distanza dall'origine, e $\theta$ l'angolo tra $\rho$ e l'asse immaginario. Il termine $\frac\alpha\rho$ ha un significato geometrico: in modulo è uguale al seno di $\theta$:

$$\zeta=\left|\frac\alpha\rho\right|=|\sin\theta|$$

La quantità $\frac\alpha\rho$ ha lo stesso segno di $\alpha$; in particolare, se $0\le\theta<\frac\pi2$, $0\le\sin\theta<1$, quindi $0\le|\zeta|<1$. $\zeta$ si chiama **smorzamento**. Il modulo $\rho$ si chiama **pulsazione naturale** (lo si vedrà nella prossima lezione) e si indica con $\omega_n$. Il trinomio si scrive allora

$$\omega_n^2\left(1-\frac{2\zeta s}{\omega_n}+\frac{s^2}{\omega_n^2}\right),\qquad\omega_n=\sqrt{\alpha^2+\omega^2},\quad\zeta=\frac{\alpha}{\omega_n}\ \ \Big(|\zeta|=|\sin\theta|\Big)$$

> [!note] Annotazioni di Simone
> A mano: "SMORZAMENTO (vedi qui sotto)"; "$\sin(\theta)=z$, dove $\theta$ è l'angolo compreso tra $\rho$ e $\omega$"; "$\omega_n=\sqrt{\alpha^2+\omega^2}$", "$z=|\sin\theta|=\left|\frac{\alpha}{\omega_n}\right|$"; "Forma di Bode TRINOMIO".

> [!note] Perché $|\zeta|<1$
> $\theta$ non può essere $\frac\pi2$: se lo fosse il numero sarebbe reale e non si avrebbero radici complesse coniugate. Può invece essere zero: radici immaginarie pure. Quindi $|\zeta|$ può valere 0 ma non 1. La lettera giusta sarebbe la zeta greca $\zeta$; il professore (e gli appunti) usano $z$, qui si usa $\zeta$ come nel libro.

> [!warning] Precisazione sul segno
> Con questa convenzione (quella degli appunti) $\zeta=\frac\alpha{\omega_n}$ ha lo stesso segno di $\alpha$, e il trinomio è $1-\frac{2\zeta s}{\omega_n}+\dots$; per un sistema stabile ($\alpha<0$) $\zeta$ è **negativo**. Il libro usa invece $\zeta=-\frac{\alpha}{\omega_n}$ e scrive il trinomio come $1+\frac{2\zeta}{\omega_n}s+\frac{s^2}{\omega_n^2}$, così che i sistemi stabili abbiano $\zeta>0$. Le due scritture descrivono lo stesso polinomio.

Per semplicità: i fattori $s$ si chiamano **termini monomi**, quelli da radici reali **termini binomi** (scrivibili come $1\pm\tau s$), e quelli da radici complesse **termini trinomi** ($1-\frac{2\zeta s}{\omega_n}+\frac{s^2}{\omega_n^2}$).

> [!quote] Dal libro — pulsazione naturale e smorzamento
> Il termine trinomio "corrisponde alla funzione di trasferimento di un sistema dinamico caratterizzato da una coppia di autovalori complessi coniugati; ciò consente di attribuire un significato fisico a parametri noti quali la pulsazione naturale e lo smorzamento": $\omega_n=\sqrt{\alpha^2+\omega^2}$, $\zeta=-\frac{\alpha}{\omega_n}$. _(libro, §5.2, p. 241)_
