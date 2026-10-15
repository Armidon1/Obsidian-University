---
title: Disuguaglianze e Legge dei Grandi Numeri
aliases:
  - PS — Disuguaglianze e Legge dei Grandi Numeri
tags:
  - probabilita-e-statistica
  - markov
  - chebyshev
  - legge-dei-grandi-numeri
source: pdf/Probabilità e Statistica Dispensa.pdf
---

# Disuguaglianze e Legge dei Grandi Numeri

> [!abstract]
> Spesso di una v.a. non conosciamo la distribuzione, ma solo la **media**, o la media e la **varianza** (lezione [[04 - PS - Valore Atteso, Varianza e Covarianza|4]]). Le disuguaglianze di **Markov** e di **Chebyshev** permettono comunque di dare una **stima dall'alto** della probabilità di eventi "estremi". Da Chebyshev si ricava poi la **legge debole dei grandi numeri**: la media aritmetica di tante copie indipendenti di una v.a. tende al suo valore atteso. È la giustificazione rigorosa dell'idea di [[01 - PS - Spazi di Probabilità e Calcolo Combinatorio#Frequenza empirica|frequenza empirica]] da cui era partito il corso.
> Il risultato più forte di questo tipo, il [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Teorema del limite centrale|teorema del limite centrale]], arriverà alla fine.
> Mappa del corso: [[MOC - Probabilità e Statistica]].

---

## Disuguaglianza di Markov

Vedi [[Disuguaglianza di Markov]].

> [!important] Disuguaglianza di Markov
> Se $X$ è una v.a. che **non è mai negativa**, allora per ogni $a>0$
> $$P(X\ge a)\le\frac{E[X]}{a}$$

*Dimostrazione (caso discreto).* Nella somma che definisce $E[X]$ tutti i termini sono $\ge0$ (perché $X\ge0$); se ne teniamo solo una parte la somma diminuisce. Teniamo i soli valori $x_i\ge a$, e in essi sostituiamo $x_i$ con $a$, che è più piccolo:
$$E[X]=\sum_ix_i\,p_X(x_i)\ge\sum_{i:\,x_i\ge a}x_i\,p_X(x_i)\ge\sum_{i:\,x_i\ge a}a\,p_X(x_i)=a\,P(X\ge a)$$
Quindi $E[X]\ge a\,P(X\ge a)$, cioè $P(X\ge a)\le E[X]/a$.

> [!tip] Intuizione
> Se una v.a. non negativa ha media piccola, non può assumere spesso valori grandi: se il reddito medio è 30 000 €, al più il 10% della popolazione può guadagnare 300 000 € o più (altrimenti solo loro alzerebbero la media sopra 30 000). La stima è grossolana ma vale **per ogni** distribuzione.

_(dispensa, p. 43)_

---

## Disuguaglianza di Chebyshev

Vedi [[Disuguaglianza di Chebyshev]].

> [!important] Disuguaglianza di Chebyshev
> Se $X$ è una v.a. con media $\mu$ e varianza $\sigma^2$, allora per ogni $r>0$
> $$P(|X-\mu|\ge r)\le\frac{\sigma^2}{r^2}$$

È più precisa di Markov perché usa un'informazione in più (la varianza) e non richiede $X\ge0$.

*Dimostrazione.* Gli eventi $\{|X-\mu|\ge r\}$ e $\{(X-\mu)^2\ge r^2\}$ coincidono, quindi sono equiprobabili. Siccome $(X-\mu)^2$ è una v.a. non negativa, possiamo applicarle Markov con $a=r^2$:
$$P(|X-\mu|\ge r)=P\big((X-\mu)^2\ge r^2\big)\le\frac{E[(X-\mu)^2]}{r^2}=\frac{\sigma^2}{r^2}$$

![[PS-p044-1.png]]

L'esempio della slide applica Chebyshev nella forma "almeno": in un esame con 50 studenti, voto medio $\mu=24$ e $\sigma=2$, quanti studenti hanno un voto tra 21 e 27? L'intervallo è $\mu\pm k\sigma$ con $k=\frac{24-21}{2}=1{,}5$, quindi
$$P(\mu-k\sigma<X<\mu+k\sigma)\ge1-\frac1{k^2}=1-\frac1{2{,}25}\approx0{,}56$$
La frequenza di chi ha un voto tra 21 e 27 non è inferiore al 56%: almeno $50\cdot0{,}56=28$ studenti (non meno di 28).

> [!important] Attenzione al verso della disuguaglianza
> $$P(|X-\mu|\ge r)\le\frac{\sigma^2}{r^2}\qquad\Longleftrightarrow\qquad P(|X-\mu|<r)\ge1-\frac{\sigma^2}{r^2}$$
> La prima stima dall'alto la probabilità di **allontanarsi** dalla media; la seconda (passando al complementare) stima dal basso la probabilità di **restare vicini**, cioè $P(\mu-r<X<\mu+r)$. La dispensa la scrive con $\le r$; la differenza tra $<$ e $\le$ non cambia la stima ($\{|X-\mu|\le r\}\supseteq\{|X-\mu|<r\}$).

> [!example] Esempio (Example 6.21) — stima di una coda binomiale
> *Sia $X\sim\mathrm{Bin}(n,p)$ e $p<\alpha<1$. Stimare dall'alto $P(X\ge\alpha n)$; valutare per $p=\frac12$, $\alpha=\frac34$.*
> $E[X]=np$, $\mathrm{Var}(X)=np(1-p)$. L'idea è "aggiungere il valore assoluto", che allarga l'evento:
> $$P(X\ge\alpha n)=P(X-np\ge\alpha n-np)\le P(|X-np|\ge n(\alpha-p))\le\frac{\mathrm{Var}(X)}{n^2(\alpha-p)^2}=\frac{p(1-p)}{n(\alpha-p)^2}$$
> Per $p=\frac12$, $\alpha=\frac34$: $\;P\big(X\ge\frac{3n}{4}\big)\le\frac{1/4}{n/16}=\frac4n$.

L'importanza delle disuguaglianze di Markov e Chebyshev sta nel fatto che permettono di limitare le probabilità di eventi rari per v.a. di cui conosciamo **solo la media**, oppure **la media e la varianza**. Naturalmente, quando la distribuzione è nota, tali probabilità si possono calcolare esattamente e non c'è bisogno di ricorrere a maggiorazioni.

> [!note] Disequazioni con il valore assoluto
> Per tradurre $|f(x)-c|\ge a$ in eventi "normali": l'insieme delle soluzioni è l'**unione** delle soluzioni di $f(x)-c\ge a$ e di $-f(x)+c\ge a$. Esempio: $|x-50|\ge10\iff x\ge60$ oppure $x\le40$.

### Forma con k deviazioni standard

Se nella disuguaglianza di Chebyshev si pone $r=k\sigma$, essa assume la forma

$$P(|X-\mu|>k\sigma)\le\frac1{k^2}$$

In altri termini, la probabilità che una v.a. differisca dalla sua media per più di $k$ volte la deviazione standard non può superare $\frac1{k^2}$: oltre 2σ al più il 25%, oltre 3σ al più l'11%, **qualunque** sia la distribuzione. _(dispensa, pp. 43–46)_

---

## Legge debole dei grandi numeri

Vedi [[Legge Debole dei Grandi Numeri]] e [[Media Campionaria]].

Grazie alla disuguaglianza di Chebyshev si dimostra la **legge debole dei grandi numeri**: la media aritmetica di $n$ copie indipendenti di una v.a. tende al valore atteso di quest'ultima per $n\to\infty$. La convergenza si precisa così: scelto un $\varepsilon$ comunque piccolo, la media aritmetica si discosta dal valore atteso per più di $\varepsilon$ con probabilità che tende a zero quando $n\to\infty$.

> [!important] Teorema (legge debole dei grandi numeri)
> Sia $X_1,X_2,\dots$ una successione di v.a. **i.i.d.** (indipendenti e identicamente distribuite), tutte con media $E[X_i]=\mu$. Allora per ogni $\varepsilon>0$
> $$P\left(\left|\frac{X_1+X_2+\dots+X_n}{n}-\mu\right|>\varepsilon\right)\longrightarrow0\qquad\text{quando }n\to\infty$$

Cioè la **media campionaria** $\bar X_n=\frac1n\sum_{k=1}^nX_k$ "tende" alla media $\mu$ per $n\to\infty$.

*Dimostrazione* (sotto l'ipotesi aggiuntiva che le $X_i$ abbiano varianza finita $\sigma^2$). Dalle proprietà di media e varianza:
$$E\left[\frac{X_1+\dots+X_n}{n}\right]=\frac{n\mu}{n}=\mu\qquad\mathrm{Var}\left(\frac{X_1+\dots+X_n}{n}\right)=\frac1{n^2}\mathrm{Var}(X_1+\dots+X_n)=\frac{\mathrm{Var}(X_1)+\dots+\mathrm{Var}(X_n)}{n^2}=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}$$
dove si sono usati $\mathrm{Var}(aX)=a^2\mathrm{Var}(X)$ e, per l'indipendenza, la [[04 - PS - Valore Atteso, Varianza e Covarianza#Formula della varianza di una somma|varianza della somma]]. Applicando Chebyshev alla v.a. $\bar X_n$:
$$P\left(\left|\bar X_n-\mu\right|>\varepsilon\right)\le\frac{\sigma^2}{n\varepsilon^2}$$
Il secondo membro tende a zero per $n\to\infty$, e l'enunciato è provato. $\square$

> [!important] Il punto chiave: $\mathrm{Var}(\bar X_n)=\sigma^2/n$
> Mediando $n$ osservazioni indipendenti, la media resta $\mu$ ma la varianza si divide per $n$: la distribuzione di $\bar X_n$ si "stringe" attorno a $\mu$. La stessa idea, raffinata, dà il [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Teorema del limite centrale|teorema del limite centrale]], che dice anche *con che forma* $\bar X_n$ si concentra.
> $$P(|\bar X_n-\mu|\ge r)\le\frac{\mathrm{Var}(\bar X_n)}{r^2}=\frac{\sigma^2}{nr^2}$$

### Interpretazione frequentista della probabilità

Una applicazione del teorema permette di giustificare l'interpretazione frequentista della probabilità. Supponiamo di ripetere in successione molte copie indipendenti di un esperimento, in ciascuna delle quali può verificarsi un evento $E$. Poniamo
$$X_i:=\begin{cases}1&\text{se $E$ si realizza nell'esperimento $i$-esimo}\\0&\text{altrimenti}\end{cases}$$
La somma $X_1+\dots+X_n$ è il numero di prove, tra le prime $n$, in cui si è verificato $E$. Poiché $E[X_i]=P(X_i=1)=P(E)$, la legge debole dice che **la frazione delle $n$ prove in cui si realizza $E$ tende alla probabilità $P(E)$**. La frequenza empirica della lezione 1 converge davvero alla probabilità.

> [!note] Media campionaria e valore atteso
> La **media campionaria** è una media in cui tutti i campioni hanno lo stesso peso $\frac1n$: $\bar X(n)=\sum_{k=1}^n\frac{X_k}{n}$. A differenza del valore atteso, che è un numero fisso, $\bar X(n)$ è una **v.a.**: cambia a ogni ripetizione dell'esperimento. La dispensa la definisce "meno precisa del valore atteso": più precisamente, è una **stima** di $\mu$ che fluttua attorno a $\mu$ con varianza $\sigma^2/n$, tanto più piccola quanto più grande è $n$.

_(dispensa, pp. 46–48)_

---

## Esercizi svolti

> [!example] Esercizio 1 — la fabbrica (Markov e Chebyshev)
> *Il costo $X_n$ dell'$n$-esimo manufatto è una v.a.; le $(X_n)$ sono i.i.d. con $E[X_n]=1$ e $\mathrm{Var}(X_n)=2$. Il prezzo di vendita è $\frac{11}{10}X_n+\frac12$.*
> 1. Guadagno: $Y_n=\frac{11}{10}X_n+\frac12-X_n=\frac1{10}X_n+\frac12$.
> 2. $E[Y_n]=\frac1{10}+\frac12=\frac35$; $\;\mathrm{Var}(Y_n)=\frac1{100}\mathrm{Var}(X_n)=\frac1{50}$.
> 3. Markov su $\sum_{i=1}^5Y_i$ (supponendo $Y_i\ge0$, cioè costi non negativi): $E[\sum_{i=1}^5Y_i]=5\cdot\frac35=3$, quindi
> $$P\Big(\sum_{i=1}^5Y_i\ge5\Big)\le\frac35$$
> 4. Per la media campionaria $\bar Y_n$: $E[\bar Y_n]=\frac35$, $\mathrm{Var}(\bar Y_n)=\frac{1}{50n}$, e per Chebyshev
> $$P\Big(\big|\bar Y_n-\tfrac35\big|\le\tfrac1{10}\Big)\ge1-\frac{1/(50n)}{1/100}=1-\frac2n\xrightarrow[n\to\infty]{}1$$
> È la legge dei grandi numeri all'opera.
>
> > [!warning] Correzione
> > Negli esercizi (p. 14) al punto 3 si scrive $Y_1+\dots+Y_5=5Y_n$, che è falso (sono v.a. diverse, solo con la stessa distribuzione). Il risultato $\frac35$ è comunque corretto, perché per la linearità $E[\sum Y_i]=5E[Y_n]$ e Markov usa solo il valore atteso. Al punto 4 manca il fattore $n$ nella varianza della media campionaria, che è quello che fa tendere la stima a 1.

> [!example] Esercizio 2 — il voto d'esame (Ross, n. 58)
> *Il punteggio di uno studente è una v.a. di media 75.*
> (a) Limite superiore a $P(X\ge85)$: Markov dà $\frac{75}{85}\approx0{,}88$.
> (b) Se anche $\mathrm{Var}(X)=25$: per Chebyshev con $r=10$,
> $$P(65<X<85)=P(|X-75|<10)\ge1-\frac{25}{100}=\frac34$$
> (c) Quanti studenti servono perché con probabilità almeno 0,9 la media non disti più di 5 da 75? $\mathrm{Var}(\bar X_n)=\frac{25}n$, e
> $$P(|\bar X_n-75|\ge5)\le\frac{25/n}{25}=\frac1n\le0{,}1\iff n\ge10$$
> _(esercizi, p. 18)_

> [!example] Esercizio 3 — variabili scorrelate e limitate
> *$(X_k)$ sono v.a. scorrelate con valore atteso nullo e valori in $[-10,10]$. (a) Mostrare che $\mathrm{Var}(X_k)\le100$. (b) Stimare dall'alto $P\big(\big|\frac1n\sum_{k=1}^nX_k\big|>\frac1{10}\big)$.*
> (a) Siccome $E[X_k]=0$, $\mathrm{Var}(X_k)=E[X_k^2]$, e $X_k^2\le100$ sempre, quindi $\mathrm{Var}(X_k)\le100$.
> (b) Le $X_k$ sono scorrelate, quindi le covarianze sono nulle e la [[04 - PS - Valore Atteso, Varianza e Covarianza#Formula della varianza di una somma|varianza della somma]] è la somma delle varianze (basta l'incorrelazione, non serve l'indipendenza): $\mathrm{Var}(\bar X_n)\le\frac{100}n$. Per Chebyshev
> $$P\big(|\bar X_n|>\tfrac1{10}\big)\le\frac{100/n}{1/100}=\frac{10^4}n$$
> (utile solo per $n>10^4$).
>
> > [!warning] Correzione
> > Negli esercizi (p. 17) si usa la formula della varianza massima $\sigma^2_{\max}=\frac{(\max-\min)^2}4$ ma si calcola $\frac{(10-(-10))^2}{4}=\frac{200}4=50$: in realtà $(20)^2=400$ e il risultato è $100$, che coincide con il limite richiesto dal testo.

> [!example] Esercizio 4 — la sfida a scacchi (Chebyshev con covarianza)
> *Albino e Ben giocano 100 partite indipendenti; in ciascuna Albino vince con probabilità $\frac12$, Ben con $\frac13$, patta con $\frac16$. Stimare con Chebyshev la probabilità che Albino non vinca la sfida (vittorie di Albino ≤ vittorie di Ben).*
> Per ogni partita sia $D_i=+1$ se vince Ben, $-1$ se vince Albino, $0$ se patta, e $Z=\sum_{i=1}^{100}D_i$ = vittorie di Ben − vittorie di Albino. Le $D_i$ sono i.i.d. con
> $$E[D_i]=\tfrac13-\tfrac12=-\tfrac16\qquad E[D_i^2]=\tfrac13+\tfrac12=\tfrac56\qquad\mathrm{Var}(D_i)=\tfrac56-\tfrac1{36}=\tfrac{29}{36}$$
> Quindi $E[Z]=-\frac{50}3$, $\mathrm{Var}(Z)=\frac{2900}{36}=\frac{725}9$, e
> $$P(Z\ge0)\le P\big(|Z-E[Z]|\ge\tfrac{50}3\big)\le\frac{725/9}{2500/9}=0{,}29$$
>
> > [!warning] Correzione
> > Negli esercizi (p. 20) si scrive $\mathrm{Var}(Y-X)=\mathrm{Var}(Y)+\mathrm{Var}(X)$ con $X\sim B(100,\frac12)$ e $Y\sim B(100,\frac13)$, cioè trattando $X$ e $Y$ come indipendenti. Non lo sono: nella stessa partita, se vince uno non vince l'altro, e $\mathrm{Cov}(X,Y)<0$. Inoltre $\mathrm{Var}(Y)=100\cdot\frac13\cdot\frac23=\frac{200}9$, non $\frac{200}3$. Il calcolo con le $D_i$ evita il problema e dà la stima $0{,}29$.
