---
title: Valore Atteso, Varianza e Covarianza
aliases:
  - PS — Valore Atteso, Varianza e Covarianza
tags:
  - probabilita-e-statistica
  - valore-atteso
  - varianza
  - covarianza
  - correlazione
source: pdf/Probabilità e Statistica Dispensa.pdf
---

# Valore Atteso, Varianza e Covarianza

> [!abstract]
> Una distribuzione contiene tutta l'informazione su una v.a., ma spesso basta qualche numero che la riassuma. Questa lezione introduce i tre riassunti fondamentali: il **valore atteso** (dove sta il "centro" della distribuzione), la **varianza** (quanto i valori si disperdono attorno al centro) e la **covarianza** con il **coefficiente di correlazione** (quanto due v.a. variano insieme).
> Si parte dalle [[03 - PS - Variabili Aleatorie Discrete|v.a. discrete]] della lezione 3; i risultati di qui (linearità, varianza della somma) sono il motore di tutto il resto del corso: le [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri|disuguaglianze e la legge dei grandi numeri]] e il calcolo di media e varianza di tutte le distribuzioni notevoli.
> Mappa del corso: [[MOC - Probabilità e Statistica]].

---

## Valore atteso

Vedi [[Expected Value]].

> [!important] Definizione
> Sia $X$ una v.a. **discreta** che può assumere i valori $x_1,x_2,\dots$. Il **valore atteso** di $X$, indicato con $E[X]$, è (se esiste) il numero
> $$E[X]:=\sum_ix_i\,P(X=x_i)$$

In altri termini, è la **media pesata** dei valori possibili di $X$, usando come pesi le probabilità che tali valori vengano assunti. Per questo $E[X]$ si chiama anche **media** di $X$. Fisicamente è il **baricentro** dei valori possibili: se metto una massa $p(x_i)$ nel punto $x_i$ di un'asta, l'asta è in equilibrio in $E[X]$.

> [!warning] Esistenza
> $E[X]$ esiste solo se la serie converge **in valore assoluto**: deve valere $\sum_i|x_i|\,P(X=x_i)<\infty$. Con un numero finito di valori è sempre vero; con infiniti valori va controllato.

> [!note] Il valore atteso non è un valore "atteso" nel senso comune
> Per un dado equilibrato $E[X]=\frac{1+2+\dots+6}{6}=3{,}5$, che non è un risultato possibile. Il nome non vuol dire che ci aspettiamo di vedere 3,5, ma che 3,5 è il **limite a cui tende il punteggio medio** su un numero crescente di lanci: la media aritmetica di tutti i valori ottenuti tende a $7/2$ (lo dimostrerà la [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Legge debole dei grandi numeri|legge dei grandi numeri]]).

**Funzione indicatrice.** Se $I$ è la funzione indicatrice di un evento $A$,
$$I:=\begin{cases}1&\text{se $A$ si verifica}\\0&\text{se $A$ non si verifica}\end{cases}\qquad\Longrightarrow\qquad E[I]=1\cdot P(I=1)+0\cdot P(I=0)=P(A)$$
Il valore atteso della funzione indicatrice di un evento è la probabilità di quell'evento. È un trucco usatissimo: per calcolare il valore atteso di un "conteggio" lo si scrive come somma di indicatrici. _(dispensa, p. 31)_

---

## Proprietà del valore atteso

Consideriamo una v.a. $X$ di cui conosciamo la distribuzione. Se invece del valore atteso di $X$ ci interessasse quello di una sua funzione $g(X)$, come potremmo fare?

Innanzitutto $g(X)$ è a sua volta una v.a., quindi ha una distribuzione che in qualche modo si può ricavare; ottenuta questa, $E[g(X)]$ si calcola con la definizione usuale. Ma c'è una strada molto più comoda.

> [!important] Proposizione (valore atteso di una funzione di v.a.)
> Se $X$ è una v.a. discreta con PMF $p$, allora per ogni funzione reale $g$
> $$E[g(X)]=\sum_xg(x)\,p(x)$$

Non serve calcolare la distribuzione di $g(X)$: basta pesare i valori $g(x)$ con le probabilità di $X$. (Nei testi inglesi è nota come LOTUS, *law of the unconscious statistician*.)

> [!warning] Correzione
> La dispensa (p. 32) riporta come "nota da verificare": *sia $Y=g(X)$; allora $\forall\,y_i=g(x_i)$ si ha $p(y_i)=p(x_i)$*. È vero **solo se $g$ è iniettiva**. Se più valori di $X$ hanno la stessa immagine, le loro probabilità si sommano: $p_Y(y)=\sum_{x:\,g(x)=y}p_X(x)$. Esempio: $X$ uniforme su $\{-1,0,1\}$ e $Y=X^2$: $P(Y=1)=P(X=-1)+P(X=1)=\frac23\ne P(X=1)$. La proposizione sopra funziona proprio perché raccoglie automaticamente questi termini.

### Linearità

Vedi [[Linearità del Valore Atteso]].

> [!important] Corollario (proprietà di linearità)
> Per ogni coppia di costanti reali $a,b$:
> $$E[aX+b]=a\,E[X]+b$$

*Dimostrazione (caso discreto).* Con la proposizione, $g(x)=ax+b$:
$$E[aX+b]=\sum_x(ax+b)p(x)=a\sum_xx\,p(x)+b\underbrace{\sum_xp(x)}_{=1}=a\,E[X]+b$$

Casi particolari:
- $a=0$: $E[b]=b$ → il valore atteso di una costante è la costante stessa;
- $b=0$: $E[aX]=a\,E[X]$.

**Momenti.** Per $n=1,2,\dots$ la quantità $E[X^n]$, quando esiste, si chiama **momento $n$-esimo** di $X$:
$$E[X^n]=\sum_xx^n\,p(x)$$
Il primo momento è la media; il secondo servirà per la varianza.

### Valore atteso della somma di due variabili aleatorie

Se $X$ e $Y$ sono due v.a. e $g$ è una qualunque funzione di due variabili, vale l'analogo della proposizione:
$$E[g(X,Y)]=\sum_x\sum_yg(x,y)\,p(x,y)$$

Applicandolo a $g(X,Y)=X+Y$ si ottiene
$$\boxed{E[X+Y]=E[X]+E[Y]}$$

*Dimostrazione.* Spezzando la somma (proprietà associativa e commutativa della sommatoria):
$$E[X+Y]=\sum_x\sum_y(x+y)p(x,y)=\sum_xx\underbrace{\sum_yp(x,y)}_{p_X(x)}+\sum_yy\underbrace{\sum_xp(x,y)}_{p_Y(y)}=E[X]+E[Y]$$
Le somme interne sono proprio le [[03 - PS - Variabili Aleatorie Discrete#Distribuzione congiunta per v.a. discrete|marginali]].

In generale, per ogni $n$:
$$E[X_1+X_2+\dots+X_n]=E[X_1]+E[X_2]+\dots+E[X_n]$$

> [!important]
> La linearità vale **sempre**, anche se le v.a. sono dipendenti. È questo che rende così potente il trucco "scrivo $X$ come somma di indicatrici": ad esempio [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo del valore atteso|la media dell'ipergeometrica]] si calcola così anche se le estrazioni sono dipendenti.

### Prodotto di variabili indipendenti

$$E[XY]=E[X]\,E[Y]$$

se $X$ e $Y$ sono v.a. **indipendenti**.

*Dimostrazione (caso discreto).* Per l'indipendenza $p(x_i,y_j)=p_X(x_i)p_Y(y_j)$, quindi
$$E[XY]=\sum_i\sum_jx_iy_j\,p(x_i,y_j)=\sum_i\sum_jx_iy_j\,p_X(x_i)p_Y(y_j)=\sum_ix_ip_X(x_i)\sum_jy_jp_Y(y_j)=E[X]E[Y]$$

Senza indipendenza in generale è falso: la differenza $E[XY]-E[X]E[Y]$ è proprio la [[#Covarianza e varianza della somma|covarianza]]. _(dispensa, pp. 32–34)_

---

## Valore atteso condizionato

Vedi [[Valore Atteso Condizionato]].

> [!important] Definizione
> Si definisce **media condizionata** di $X$ dato $Y=y$ la quantità
> $$E[X\mid Y=y]=\sum_xx\,P(X=x\mid Y=y)$$

È il valore atteso calcolato con la [[03 - PS - Variabili Aleatorie Discrete#Distribuzioni condizionali|distribuzione condizionale]] di $X$ dato $Y=y$: la media di $X$ nel "sotto-mondo" in cui sappiamo che $Y=y$.

**Proprietà.**
- **Indipendenza**: se $X$ e $Y$ sono indipendenti, $E[X\mid Y=y]=E[X]$. Infatti
$$E[X\mid Y=y]=\sum_xx\frac{P(X=x,Y=y)}{P(Y=y)}=\sum_xx\frac{p_X(x)p_Y(y)}{p_Y(y)}=E[X]$$
- **Stabilità**: $E[g(Y)X\mid Y=y]=g(y)\,E[X\mid Y=y]$ — sapendo che $Y=y$, $g(Y)$ è la costante $g(y)$ e si porta fuori.
- **Costanti**: $E[c\mid Y=y]=c$.
- **Linearità**: $E[cX+dZ\mid Y=y]=c\,E[X\mid Y=y]+d\,E[Z\mid Y=y]$.

_(dispensa, pp. 34–35)_

### Teorema sul valore atteso del valore atteso condizionato

Vedi [[Teorema del Valore Atteso Iterato]].

> [!important] Teorema
> Sia $g:\mathbb R\to\mathbb R$ misurabile. Allora
> $$E\big[E[g(Y)\mid X]\big]=E[g(Y)]$$
> In particolare (corollario, $g(y)=y$): $\;E\big[E[Y\mid X]\big]=E[Y]$.

*Dimostrazione.* Sia $h(x)=E[g(Y)\mid X=x]$. Per definizione
$$
\begin{aligned}
E[h(X)]&=\sum_xh(x)\,p_X(x)=\sum_xE[g(Y)\mid X=x]\,p_X(x)=\sum_x\sum_yg(y)\frac{P(Y=y,X=x)}{p_X(x)}p_X(x)\\
&=\sum_yg(y)\sum_xP(Y=y,X=x)=\sum_yg(y)\,p_Y(y)=E[g(Y)]
\end{aligned}
$$

> [!note] Come si legge
> $E[Y\mid X]$ è una **v.a.**: è la funzione $h(X)$ che vale $E[Y\mid X=x]$ quando $X=x$. Il teorema dice che la media delle medie condizionate è la media globale. Esplicitamente, nel caso discreto:
> $$E[X]=\sum_yE[X\mid Y=y]\,P(Y=y)$$
> È la versione "per i valori attesi" della [[02 - PS - Probabilità Condizionata e Indipendenza#Fattorizzazione di un evento|formula di fattorizzazione]]: si calcola un valore atteso difficile condizionando a una variabile che rende il problema facile.

> [!example] Esempio — visitatori del museo (somma di un numero aleatorio di v.a.)
> *Il numero $N$ di visite guidate a settimana ha valore atteso 20. Il numero $X_i$ di visitatori della visita $i$-esima ha valore atteso 10; i visitatori di ogni visita sono indipendenti tra loro e da $N$. Numero atteso di visitatori in una settimana?*
> Il totale è $\sum_{i=1}^NX_i$, con un numero di addendi **aleatorio**: non si può usare direttamente la linearità. Condizioniamo a $N$:
> $$E\Big[\sum_{i=1}^NX_i\,\Big|\,N=n\Big]=E\Big[\sum_{i=1}^nX_i\,\Big|\,N=n\Big]=E\Big[\sum_{i=1}^nX_i\Big]=n\,E[X]$$
> (la seconda uguaglianza usa l'indipendenza tra $X_i$ e $N$). Quindi $E[\sum X_i\mid N]=N\,E[X]$ e
> $$E\Big[\sum_{i=1}^NX_i\Big]=E\big[N\,E[X]\big]=E[N]\,E[X]=20\cdot10=200$$

> [!example] Esempio — il bambino nel labirinto
> *Un bambino davanti a tre porte: la 1 porta all'uscita in 5 minuti, la 2 lo riporta al punto di partenza dopo 3 minuti, la 3 dopo 8 minuti. Sceglie ogni volta a caso (non ricorda le porte già provate). Tempo medio per uscire?*
> Sia $X$ il tempo e $Y$ la porta scelta, $P(Y=k)=\frac13$. Condizionando alla prima scelta:
> $$E[X\mid Y=1]=5\qquad E[X\mid Y=2]=3+E[X]\qquad E[X\mid Y=3]=8+E[X]$$
> (con la porta 2 o 3 torna allo stesso punto e il problema ricomincia identico). Quindi
> $$E[X]=\tfrac13\big(5+3+E[X]+8+E[X]\big)\;\Longrightarrow\;3E[X]=16+2E[X]\;\Longrightarrow\;E[X]=16\text{ minuti}$$

_(dispensa, pp. 35–37)_

> [!example] Esercizio svolto — urna e dado (vincita attesa)
> *Da un'urna con due palline "2", tre palline "5" e cinque palline "1" se ne estrae una; poi si lancia un dado tante volte quanto il numero estratto, vincendo 1 € per ogni lancio maggiore di 4. Valore atteso della vincita?*
> Sia $X$ il numero estratto e $Y$ la vincita. Dato $X=n$, $Y$ conta i successi in $n$ lanci con $p=\frac26=\frac13$: $E[Y\mid X=n]=\frac n3$. Allora
> $$E[Y]=E\big[E[Y\mid X]\big]=\frac{E[X]}3=\frac{2\cdot\frac2{10}+5\cdot\frac3{10}+1\cdot\frac5{10}}{3}=\frac{2{,}4}{3}=0{,}8\text{ €}$$
> Negli esercizi (pp. 25–26) il calcolo era impostato passando per tutta la distribuzione di $Y$ e lasciato a metà; con il teorema bastano due righe. Lo stesso esercizio chiede anche $P(Y\ge1)=1-P(Y=0)=1-\big[\frac15(\frac23)^2+\frac3{10}(\frac23)^5+\frac12\cdot\frac23\big]=1-\frac{187}{405}\approx0{,}54$.

---

## Varianza

Vedi [[Variance]].

Il valore atteso dice dove si trova il centro della distribuzione, ma non quanto i valori siano sparpagliati: $X\equiv0$ e $Y=\pm100$ con probabilità $\frac12$ hanno entrambe media 0. Serve una misura di dispersione.

> [!important] Definizione
> Sia $X$ una v.a. con media $\mu:=E[X]$. La **varianza** di $X$, indicata con $\mathrm{Var}(X)$, è (se esiste) la quantità
> $$\mathrm{Var}(X):=E\big[(X-\mu)^2\big]=\boxed{E[X^2]-E[X]^2}\qquad\text{con }E[X^2]=\sum_xx^2p(x)$$

La seconda forma si ottiene sviluppando il quadrato e usando la linearità: $E[X^2-2\mu X+\mu^2]=E[X^2]-2\mu^2+\mu^2$. È quella da usare nei conti ("media dei quadrati meno quadrato della media").

**Identità utile.** Per ogni coppia di costanti reali $a,b$:
$$\mathrm{Var}(aX+b)=a^2\,\mathrm{Var}(X)$$

*Dimostrazione.* $E[aX+b]=a\mu+b$, quindi
$$\mathrm{Var}(aX+b)=E\big[(aX+b-a\mu-b)^2\big]=E\big[(aX-a\mu)^2\big]=E\big[a^2(X-\mu)^2\big]=a^2\,\mathrm{Var}(X)$$

Casi particolari: $\mathrm{Var}(b)=0$ (una costante non varia) e $\mathrm{Var}(X+b)=\mathrm{Var}(X)$ (traslare non cambia la dispersione).

La quantità $\sqrt{\mathrm{Var}(X)}$ si chiama **deviazione standard** di $X$ ($\sigma$): ha la stessa unità di misura di $X$. _(dispensa, p. 38)_

---

## Covarianza e varianza della somma

Vedi [[Covariance]].

La media della somma di v.a. coincide con la somma delle medie. Per la varianza **in generale questo non è vero**. Ad esempio
$$\mathrm{Var}(X+X)=\mathrm{Var}(2X)=2^2\,\mathrm{Var}(X)=4\,\mathrm{Var}(X)\ne\mathrm{Var}(X)+\mathrm{Var}(X)$$
C'è però un caso importante in cui la varianza della somma è la somma delle varianze: quando le v.a. sono **indipendenti**. Per capire perché serve la covarianza.

> [!important] Definizione
> Siano $X$ e $Y$ v.a. di media $\mu_X$ e $\mu_Y$. La loro **covarianza** è (se esiste)
> $$\mathrm{Cov}(X,Y):=E\big[(X-\mu_X)(Y-\mu_Y)\big]$$
> Espandendo il prodotto si trova la formula alternativa
> $$\boxed{\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]}$$

**Proprietà.**
- **Simmetria**: $\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)$.
- La covarianza **generalizza la varianza**: $\mathrm{Cov}(X,X)=\mathrm{Var}(X)$.
- **Costanti**: $\mathrm{Cov}(aX,Y)=\mathrm{Cov}(X,aY)=a\,\mathrm{Cov}(X,Y)$.
- **Lemma (additività)**: $\mathrm{Cov}(X+Y,Z)=\mathrm{Cov}(X,Z)+\mathrm{Cov}(Y,Z)$, e più in generale $\mathrm{Cov}\big(\sum_{i=1}^nX_i,\,Y\big)=\sum_{i=1}^n\mathrm{Cov}(X_i,Y)$.

> [!important] Proposizione (bilinearità)
> $$\mathrm{Cov}\Big(\sum_{i=1}^nX_i,\;\sum_{j=1}^mY_j\Big)=\sum_{i=1}^n\sum_{j=1}^m\mathrm{Cov}(X_i,Y_j)$$

*Dimostrazione.* Si applica il lemma, poi la simmetria, poi di nuovo il lemma:
$$\mathrm{Cov}\Big(\sum_iX_i,\sum_jY_j\Big)=\sum_i\mathrm{Cov}\Big(X_i,\sum_jY_j\Big)=\sum_i\mathrm{Cov}\Big(\sum_jY_j,X_i\Big)=\sum_i\sum_j\mathrm{Cov}(Y_j,X_i)$$
e si conclude applicando ancora la simmetria. _(dispensa, pp. 39–40)_

### Formula della varianza di una somma

Vedi [[Varianza della Somma]].

Ricordando che $\mathrm{Cov}(X,X)=\mathrm{Var}(X)$ e applicando la bilinearità alla v.a. $\sum_iX_i$ (da pensare come un "vettore aleatorio" sommato):

$$\mathrm{Var}\Big(\sum_{i=1}^nX_i\Big)=\mathrm{Cov}\Big(\sum_iX_i,\sum_jX_j\Big)=\sum_i\sum_j\mathrm{Cov}(X_i,X_j)=\sum_{i=1}^n\mathrm{Var}(X_i)+\sum_{i=1}^n\sum_{\substack{j=1\\j\ne i}}^n\mathrm{Cov}(X_i,X_j)$$

I termini con $i=j$ sono le varianze, gli altri le covarianze (ogni coppia compare due volte: $(i,j)$ e $(j,i)$). Per $n=2$:

$$\boxed{\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\,\mathrm{Cov}(X,Y)}\qquad\qquad\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)-2\,\mathrm{Cov}(X,Y)$$

> [!important] Teorema
> Se $X$ e $Y$ sono **indipendenti**, allora $E[XY]=E[X]E[Y]$ e quindi $\mathrm{Cov}(X,Y)=0$. Perciò, se $X_1,\dots,X_n$ sono indipendenti,
> $$\mathrm{Var}\Big(\sum_{i=1}^nX_i\Big)=\sum_{i=1}^n\mathrm{Var}(X_i)$$

Questo risultato sarà usato continuamente: per la varianza della [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Variabili aleatorie binomiali|binomiale]] (somma di Bernoulli indipendenti), per quella della [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Legge debole dei grandi numeri|media campionaria]] e, con le covarianze non nulle, per la [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo della varianza|varianza dell'ipergeometrica]]. _(dispensa, p. 41)_

---

## Coefficiente di correlazione

Vedi [[Coefficiente di Correlazione]].

Se due v.a. non sono indipendenti, la loro covarianza è un importante indicatore della relazione tra loro: un valore **positivo** di $\mathrm{Cov}(X,Y)$ indica che $X$ e $Y$ tendono ad assumere valori grandi o piccoli **contemporaneamente**; un valore negativo che quando una è grande l'altra tende a essere piccola.

La covarianza però dipende dall'unità di misura (passando da metri a centimetri si moltiplica per 100). La forza della relazione è misurata più propriamente dal **coefficiente di correlazione lineare**, un numero puro che tiene conto anche delle deviazioni standard:

$$\mathrm{Corr}(X,Y):=\frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)\,\mathrm{Var}(Y)}}$$

Questa quantità è **sempre compresa tra $-1$ e $1$**; vale $\pm1$ solo se $Y=aX+b$ (relazione lineare esatta).

Se $\mathrm{Corr}(X,Y)=0$ le due v.a. si dicono **incorrelate**.

> [!warning] Incorrelate non vuol dire indipendenti
> Se due v.a. sono **indipendenti** allora sono anche **incorrelate**, ma il viceversa **non** è vero: $\mathrm{Cov}(X,Y)=0$ non implica l'indipendenza. L'indipendenza si verifica solo se $P(X=x,Y=y)=P(X=x)P(Y=y)$ per **ogni** $x$ e $y$. La covarianza misura solo la dipendenza **lineare**.

_(dispensa, p. 42)_

> [!example] Esercizio svolto — incorrelate ma dipendenti
> *Il vettore $(X,Y)$ ha densità congiunta*
>
> | $X\backslash Y$ | 0 | 1 | 2 |
> |:-:|:-:|:-:|:-:|
> | **0** | $\frac13$ | 0 | $\frac13$ |
> | **1** | 0 | $\frac13$ | 0 |
>
> 1. $P(X=0,Y\ge0)=\frac13+0+\frac13=\frac23$; $P(X=Y)=p(0,0)+p(1,1)=\frac23$.
> 2. Marginali: $p_X(0)=\frac23$, $p_X(1)=\frac13$; $p_Y(0)=p_Y(1)=p_Y(2)=\frac13$.
> $E[X]=\frac13$, $E[Y]=\frac13+\frac23=1$, $E[X^2]=\frac13$, $E[Y^2]=\frac13+\frac43=\frac53$.
> $\mathrm{Var}(X)=\frac13-\frac19=\frac29$, $\mathrm{Var}(Y)=\frac53-1=\frac23$.
> 3. $E[XY]=1\cdot1\cdot p(1,1)=\frac13$, quindi $\mathrm{Cov}(X,Y)=\frac13-\frac13\cdot1=0$.
> 4. $X$ e $Y$ **non** sono indipendenti: $p(0,0)=\frac13\ne p_X(0)p_Y(0)=\frac29$. Sono incorrelate ma dipendenti — esattamente il caso del riquadro qui sopra.
> 5. Con $U=\frac12(X+Y)$ e $V=\frac12(Y-X)$, per bilinearità:
> $$\mathrm{Cov}(U,V)=\tfrac14\big[\mathrm{Cov}(X+Y,\,Y-X)\big]=\tfrac14\big[\mathrm{Var}(Y)-\mathrm{Var}(X)\big]=\tfrac14\Big(\tfrac23-\tfrac29\Big)=\tfrac19$$
> (i termini $\mathrm{Cov}(X,Y)$ si cancellano).
>
> > [!warning] Correzione
> > Nello svolgimento (esercizi, pp. 6–8) compaiono due sviste: $\mathrm{Var}(X)=\frac13-\frac16=\frac16$, mentre $E[X]^2=\frac19$ e quindi $\mathrm{Var}(X)=\frac29$; e al punto 4 si conclude prima "indipendenti perché $\mathrm{Cov}=0$", poi corretto in "incorrelate". Il risultato $\mathrm{Cov}(U,V)=\frac19$ è giusto (lì calcolato come $E[UV]-E[U]E[V]=\frac13-\frac29$).

> [!example] Esercizio svolto — covarianza nell'urna R/B
> Riprendendo l'urna della [[03 - PS - Variabili Aleatorie Discrete#Distribuzione congiunta per v.a. discrete|lezione 3]] (3 rosse, 2 bianche, 1 verde, 2 estrazioni):
> - $E[B]=\frac8{15}+2\cdot\frac1{15}=\frac23$, $E[B^2]=\frac8{15}+\frac4{15}=\frac45$, $\mathrm{Var}(B)=\frac45-\frac49=\frac{16}{45}$;
> - $E[R]=\frac9{15}+2\cdot\frac3{15}=1$, $E[R^2]=\frac9{15}+\frac{12}{15}=\frac75$, $\mathrm{Var}(R)=\frac75-1=\frac25$;
> - $E[RB]=1\cdot1\cdot P(R=1,B=1)=\frac25$, quindi $\mathrm{Cov}(R,B)=\frac25-1\cdot\frac23=-\frac4{15}$ (negativa: più rosse → meno bianche);
> - $\mathrm{Corr}(R,B)=\dfrac{-4/15}{\sqrt{\frac25\cdot\frac{16}{45}}}=\dfrac{-4/15}{\sqrt{32/225}}=\dfrac{-4/15}{4\sqrt2/15}=-\dfrac1{\sqrt2}\approx-0{,}707$;
> - $\mathrm{Var}(R-B)=\mathrm{Var}(R)+\mathrm{Var}(B)-2\,\mathrm{Cov}(R,B)=\frac25+\frac{16}{45}+\frac8{15}=\frac{58}{45}$.
>
> > [!warning] Correzione
> > Negli esercizi (p. 12) $\mathrm{Var}(R)$ risulta $\frac43$ e di conseguenza $\mathrm{Var}(R-B)=\frac{20}9$. Il valore corretto è $\mathrm{Var}(R)=\frac25$ (lo conferma la formula dell'[[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo della varianza|ipergeometrica]]: $2\cdot\frac12\cdot\frac12\cdot\frac{6-2}{6-1}=\frac25$), da cui $\mathrm{Var}(R-B)=\frac{58}{45}$.
