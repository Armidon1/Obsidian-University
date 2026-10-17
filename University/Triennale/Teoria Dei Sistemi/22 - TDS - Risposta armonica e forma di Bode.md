---
title: Risposta armonica e forma di Bode
aliases:
  - TDS — Risposta armonica e forma di Bode
tags:
  - teoria-dei-sistemi
  - regime-permanente
  - risposta-armonica
  - diagrammi-di-bode
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 119–126); libro Monaco et al., §5.1.1, §5.2
---

# Risposta armonica e forma di Bode

> [!abstract] Scopo della lezione
> 1. Si completa il [[21 - TDS - Risposta a regime permanente|regime permanente]] con ingresso **polinomiale**, leggendo i coefficienti come quelli dello sviluppo di Maclaurin di $W(s)$, con esempi e un caso in cui il regime **non esiste**.
> 2. Si passa all'ingresso **periodico**: prima l'esponenziale $e^{at}$ (regime $e^{at}W(a)$), poi il seno. L'uscita a regime è una sinusoide della **stessa frequenza**, con ampiezza e fase modificate da $W(j\omega)$: la **risposta armonica**.
> 3. Per studiare modulo e fase di $W(j\omega)$ al variare di $\omega$ si usano la **forma di Bode** (fattorizzazione con costanti di tempo), i **decibel** e la scala logaritmica: i **diagrammi di Bode**, a partire dalla costante e dal termine $s$.
>
> Segue [[23 - TDS - Diagrammi di Bode]]. Indice: [[MOC - Teoria dei Sistemi]].

## Uscita a regime permanente con ingresso polinomiale

Vedi [[TDS - Regime permanente]].

Nella scorsa lezione, con $u(t)=\frac{t^k}{k!}$:

$$y_{RP}(t)=\sum_{i=0}^k\frac{t^{k-i}}{(k-i)!}\,\frac1{i!}\left[\frac{d^i}{ds^i}W(s)\right]_{s=0}$$

Cioè, con un ingresso polinomiale nella forma notevole (diviso per il fattoriale), l'uscita a regime è un polinomio in $t$ con potenze da 0 a $k$, moltiplicate per coefficienti facili da calcolare:

$$c_i=\frac1{i!}\left[\frac{d^i}{ds^i}W(s)\right]_{s=0}$$

Sono **esattamente** i coefficienti dello **sviluppo di Maclaurin** di $W(s)$ (Taylor in $s=0$, vedi [[Serie di Taylor]]):

$$W(s)=W(s)\big|_{s=0}+\frac{dW(s)}{ds}\Big|_{s=0}s+\frac12\frac{d^2W(s)}{ds^2}\Big|_{s=0}s^2+\dots+\frac1{k!}\frac{d^kW(s)}{ds^k}\Big|_{s=0}s^k+\dots=c_0+c_1s+c_2s^2+\dots+c_ks^k+\dots$$

Quindi l'uscita a regime si scrive più semplicemente

$$y_{RP}(t)=\sum_{i=0}^k\frac{t^{k-i}}{(k-i)!}\,c_i$$

ricordando però che qui $c_0$ moltiplica la potenza **massima** di $t$ e $c_k$ è il termine **noto** (il contrario rispetto allo sviluppo di Maclaurin).

> [!note] Annotazione di Simone
> Accanto a $c_i$: **"Coefficiente facile da calcolare che combacia ai coefficienti di Maclaurin"**.

### Esempi di $y_{RP}$ con ingresso polinomiale

> [!note] Annotazione di Simone
> A margine: **"Qui si nota esplicitamente come è molto più rapido il calcolo della risposta a regime permanente con le ultime nozioni viste nella scorsa lezione"**.

**Esempio 1.** $u(t)=\frac{t^2}{2}$ (ingresso polinomiale), $W(s)=\frac1{s+1}$:

$$y_{RP}(t)=\frac{t^2}2c_0+tc_1+c_2=\frac{t^2}{2}W(s)\big|_{s=0}+t\frac{dW(s)}{ds}\Big|_{s=0}+\frac12\frac{d^2W(s)}{ds^2}\Big|_{s=0}=\frac{t^2}2\cdot\frac1{s+1}\Big|_{0}+t\cdot\frac{-1}{(s+1)^2}\Big|_{0}+\frac12\cdot\frac{2}{(s+1)^3}\Big|_{0}=\frac{t^2}{2}-t+1$$

> [!warning] Correzione
> Negli appunti l'ultimo termine è scritto $\frac12\cdot\frac{1}{(s+1)^3}$, con risultato $\frac{t^2}{2}-t+\frac12$. Ma la derivata seconda di $\frac{1}{s+1}$ è $\frac{2}{(s+1)^3}$, quindi $c_2=\frac12\cdot2=1$ e $y_{RP}(t)=\frac{t^2}{2}-t+1$. Lo conferma lo sviluppo $\frac{1}{1+s}=1-s+s^2-\dots$, cioè $c_0=1$, $c_1=-1$, $c_2=1$. Verifica diretta: $y=\frac{t^2}2-t+1$ soddisfa $\dot y+y=u$ (il sistema $W=\frac1{s+1}$), perché $(t-1)+\big(\frac{t^2}2-t+1\big)=\frac{t^2}2$ ✔.

**Esempio 2.** Se $u(t)=\frac{t^2}{2}+t$, per linearità ai termini di $\frac{t^2}2$ già calcolati si aggiungono quelli di $t$ (con $k=1$: $tc_0+c_1$):

$$y_{RP}(t)=\underbrace{\frac{t^2}2c_0+tc_1+c_2}_{\text{termini di }t^2/2}+\underbrace{tc_0+c_1}_{\text{termini di }t}=\Big(\frac{t^2}2-t+1\Big)+(t-1)=\frac{t^2}2$$

> [!warning] Correzione
> Con il valore errato di $c_2$ gli appunti trovano $\frac{t^2}{2}-\frac12$; correggendo $c_2=1$ si ottiene $y_{RP}(t)=\frac{t^2}{2}$. Verifica: $\dot y+y=t+\frac{t^2}{2}=u$ ✔.

> [!note] Annotazioni di Simone
> A margine: "Altro Caso particolare"; sopra $\frac{t^2}2$: "Già calcolato", sopra $t$: "Nuovo".

**Esempio 3.** $u(t)=t^3$ non è in forma notevole (non è diviso per $3!$): va considerato come $u(t)=\frac{t^3}{3!}\cdot3!$, si fa lo sviluppo di $\frac{t^3}{3!}$ e si moltiplica tutto per $3!$:

$$y_{RP}=\left(\frac{t^3}{3!}c_0+\frac{t^2}{2!}c_1+tc_2+c_3\right)\cdot3!=t^3c_0+\frac{3!}{2!}t^2c_1+3!\,tc_2+3!\,c_3$$

> [!note] Annotazioni di Simone
> A margine: "Altro Caso particolare"; sopra $\frac{t^3}{3!}$: "Forma Polinomiale".

**Esempio 4.** Attenzione con

$$u(t)=t,\qquad W(s)=\frac1{(s+1)(s-1)}$$

I poli di $W(s)$ non sono tutti negativi: il polo $s=1$ indica un autovalore $\lambda=1>0$. In $W$ c'è un modo naturale che **non tende a zero**, e la **risposta a regime permanente non può esistere** (applicare la formula darebbe un numero, ma privo di significato).

> [!note] Annotazione di Simone
> In rosso: **"IMPORTANTISSIMA OSSERVAZIONE"**.

## Uscita a regime permanente con ingresso periodico

Gli ingressi che "permangono" nel tempo a un valore limitato sono quello **costante** (studiato fino al livello polinomiale) e quello **periodico**. Prima di $u(t)=\sin\omega t$ si studia per semplicità l'ingresso esponenziale, per poi ricondursi al seno con i numeri complessi.

> [!note] Annotazioni di Simone
> Accanto a "costante": "Caso Polinomiale"; in testa alla pagina, in rosso: **"STUDIAMO PRIMA INGRESSO ESPONENZIALE PER POI RICONDURCI A QUELLO PERIODICO"**.

### Ingresso esponenziale

Con $u(t)=e^{at}$:

$$y_{RP}(t)=\int_{-\infty}^{t}W(t-\tau)e^{a\tau}\,d\tau=\int_0^{+\infty}W(\theta)e^{a(t-\theta)}\,d\theta=e^{at}\int_0^{+\infty}W(\theta)e^{-a\theta}\,d\theta=e^{at}\,W(s)\big|_{s=a}$$

L'integrale del penultimo passaggio è esattamente $W(s)$ con $s=a$; e poiché $s$ è complessa, si può prendere qualsiasi $a\in\mathbb C$.

> [!note] Annotazioni di Simone
> "Risposta a regime permanente con un ingresso Esponenziale"; accanto a $e^{-a\theta}$: **"$a\in\mathbb C$, perciò sviluppo Laplace come ci fosse $s$ e poi sostituisco $s=a$"**.

> [!tip] Funzione di trasferimento come "autovalore"
> Gli esponenziali sono speciali per i sistemi lineari stazionari: entrano $e^{at}$ ed esce (a regime) $W(a)\,e^{at}$, lo stesso esponenziale moltiplicato per un numero. Per questo $W(s)$ si chiama anche **funzione di trasferimento**: dice di quanto viene "trasferito" un esponenziale di esponente $s$.

### Ingresso sinusoidale

Con

$$u(t)=\sin\omega t=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$$

applicando il risultato precedente (con $a=\pm j\omega$) e la linearità:

$$y_{RP}(t)=\frac{e^{j\omega t}W_s(j\omega)-e^{-j\omega t}W_s(-j\omega)}{2j}$$

dove $W_s(j\omega):=W(s)|_{s=j\omega}$.

> [!note] Notazione
> Il professore scrive $W(j\omega)$; gli appunti usano $W_s(j\omega)$ per chiarire che si tratta di $W(s)$ calcolata in $s=j\omega$, e non della funzione $W(t)$. Qui si segue la stessa scelta.

$W_s(j\omega)$ è un numero complesso: lo si scrive in forma **modulo-fase**, $W_s(j\omega)=|W_s(j\omega)|\,e^{j\angle W_s(j\omega)}$:

$$y_{RP}(t)=\frac{e^{j\omega t}|W_s(j\omega)|e^{j\angle W_s(j\omega)}-e^{-j\omega t}|W_s(-j\omega)|e^{j\angle W_s(-j\omega)}}{2j}$$

Si dimostra (con le trasformate di Fourier) che il **modulo** di una trasformata è una funzione **pari** e la **fase** una funzione **dispari**:

$$|W_s(-j\omega)|=|W_s(j\omega)|,\qquad\angle W_s(-j\omega)=-\angle W_s(j\omega)$$

(per $W(s)$ a coefficienti reali basta osservare che $W_s(-j\omega)=W_s(j\omega)^*$.) Allora:

$$y_{RP}(t)=|W_s(j\omega)|\cdot\frac{e^{j(\omega t+\angle W_s(j\omega))}-e^{-j(\omega t+\angle W_s(j\omega))}}{2j}=|W_s(j\omega)|\,\sin\big(\omega t+\angle W_s(j\omega)\big)$$

> [!important] Regime permanente a un ingresso sinusoidale
> $$u(t)=\sin\omega t\quad\Longrightarrow\quad y_{RP}(t)=|W_s(j\omega)|\,\sin\big(\omega t+\angle W_s(j\omega)\big)$$
> L'uscita a regime ha la **stessa pulsazione** dell'ingresso; cambiano solo l'**ampiezza** (moltiplicata per $|W_s(j\omega)|$) e la **fase** (spostata di $\angle W_s(j\omega)$).

> [!note] Annotazioni di Simone
> A mano: "Risposta a regime permanente con un ingresso Periodico"; "$W_s(j\omega)$ è la risposta armonica (vedi dopo)"; "Essendo un numero complesso posso riscriverlo come modulo e fase"; "Importanti osservazioni su modulo e fase di una trasformata"; **"La risposta a regime permanente l'ho calcolata esattamente come nel caso esponenziale, trovandomi in una situazione in cui $s=j\omega$, proprio perché $u(t)=\sin\omega t=\frac{e^{j\omega t}-e^{-j\omega t}}{2j}$"**; "Notiamo che la risposta RP dipende solo ed esclusivamente della…".

> [!quote] Dal libro — risposta armonica
> "La risposta a regime permanente ad un ingresso periodico puro con pulsazione $\omega$, è una funzione dello stesso tipo dell'ingresso con la stessa pulsazione, modificata in modulo e fase di quantità $M(\omega)$ e $\varphi(\omega)$ che sono il modulo e la fase di $W(s)$ calcolata in $s=j\omega$." Il libro lo illustra con un **altimetro**: un altimetro ideale ha $M(\omega)=1$ e $\varphi(\omega)=0$ a ogni frequenza; due altimetri reali $A_1$ e $A_2$ che a una certa pulsazione misurano 0,8 e 0,95 volte l'ampiezza vera hanno errori del 20% e del 5%, e il secondo risponde anche più velocemente al gradino (costanti di tempo minori). _(libro, §5.1.1, pp. 222–224)_

## Studio della risposta armonica

Vedi [[TDS - Risposta armonica]].

> [!note] Annotazione di Simone
> Accanto al titolo, in viola: **"RISPOSTA ARMONICA"**.

La funzione $W_s(j\omega)$ si chiama **risposta armonica**, ed esiste solo quando esiste la risposta a regime permanente. Se l'ingresso è una sinusoide di un certo periodo, l'uscita a regime ha **lo stesso periodo** (la stessa frequenza) e al più un'**ampiezza** diversa e uno **sfasamento**. Queste due quantità dipendono da $W_s(j\omega)$, con $\omega\in\mathbb R$: basta studiare la funzione $W_s(j\omega)$, e in particolare (essendo complessa) il suo modulo $|W_s(j\omega)|$ e la sua fase $\angle W_s(j\omega)$, separatamente.

Per esempio, se si vuole che l'uscita sia **amplificata** rispetto all'ingresso e si hanno due pulsazioni $\omega_1$ e $\omega_2$ tali che

![[TDS-L22-01.png]]

si sceglie $\omega_2$: anche se genera in uscita una sinusoide **più sfasata** rispetto all'ingresso ($|\angle W_s(j\omega)|$ maggiore), è di **ampiezza maggiore** ($|W_s(j\omega)|$ maggiore). Questo diagramma, con sopra il grafico del modulo e sotto quello della fase, si chiama **diagramma di Bode**.

> [!note] Annotazioni di Simone
> A margine: **"Periodo della risposta RP è lo stesso dell'ingresso $u(t)=\sin(\omega t)$, mentre ampiezza e sfasamento dipendono solo ed esclusivamente dalla risposta armonica $W_s(j\omega)$ ⇓ Possiamo studiare solo ed esclusivamente $W_s(j\omega)$, in particolare modulo e fase, al variare di $\omega$."** e **"IMPORTANTISSIMO"** accanto a "diagramma di Bode".

$W_s(j\omega)=W(s)|_{s=j\omega}$ è una funzione strettamente propria (a meno che ci sia $D$), quindi è un rapporto tra un numeratore $n(s)$ e un denominatore $d(s)$:

$$W_s(j\omega)=W(s)\big|_{s=j\omega}=\frac{n(s)}{d(s)}\Big|_{s=j\omega}$$

Con $p=q=1$, il denominatore ha grado $n$ e il numeratore grado minore; si fattorizzano tramite le radici (reali o complesse coniugate):

$$\frac{n(s)}{d(s)}\Big|_{s=j\omega}=\frac{k_1(\ \ )\cdots(\ \ )}{k_2(\ \ )\cdots(\ \ )}\Big|_{s=j\omega}\tag{$\spadesuit$}$$

dove nelle parentesi ci sono i fattori con le radici. Per le proprietà del modulo e della fase dei numeri complessi:

$$|T_1T_2|=|T_1|\,|T_2|,\quad\left|\frac{T_1}{T_2}\right|=\frac{|T_1|}{|T_2|},\qquad\angle(T_1T_2)=\angle T_1+\angle T_2,\quad\angle\frac{T_1}{T_2}=\angle T_1-\angle T_2$$

(se $T_1=\rho_1e^{j\theta_1}$ e $T_2=\rho_2e^{j\theta_2}$, allora $T_1T_2=\rho_1\rho_2e^{j(\theta_1+\theta_2)}$). Quindi, portata $W_s(j\omega)$ nella forma ($\spadesuit$), il **modulo** è il prodotto (e rapporto) dei moduli dei fattori, e la **fase** è la somma delle fasi dei fattori al numeratore meno quelle dei fattori al denominatore.

> [!note] Annotazioni di Simone
> A mano: "La risposta armonica ha una forma a frazione"; "Allora, una volta trovata questa forma, calcolo il modulo e la fase di ogni termine e li sommo/moltiplico"; "Prodotto dei moduli", "Somma dei moduli" (sopra la fase).

## Risposta armonica in forma di Bode

Vedi [[TDS - Diagrammi di Bode]].

Fattorizzando $W(s)$ si ottengono quattro tipi di termini:
- **costanti**;
- termini di tipo $s$, dalle radici $s_i=0$;
- termini di tipo $(s-s_i)$, da radici reali;
- termini complessi coniugati, $(s-s_i)(s-s_i^*)$.

Tralasciando per ora le radici complesse, conviene scrivere i termini $(s-s_i)$ nella forma $(1\pm\dots)$:

$$(s-s_i)\ \longrightarrow\ -s_i\left(1-\frac{s}{s_i}\right)$$

così tutte le costanti si raccolgono in un unico termine $K$ che moltiplica tutto:

$$W(s)=K\,\frac{\left(1-\frac{s}{s_1}\right)\left(1-\frac{s}{s_2}\right)\cdots\left(1-\frac{s}{s_n}\right)}{\left(1-\frac{s}{s_{n+1}}\right)\left(1-\frac{s}{s_{n+2}}\right)\cdots\left(1-\frac{s}{s_{2n}}\right)}$$

Scritta così, il calcolo in $s=0$ è banale: $W(0)=K$. Questa fattorizzazione si chiama **forma di Bode**.

> [!note] Annotazioni di Simone
> A mano: "4 tipologie di termini"; "$-s_i$ lo consideriamo come costante"; "Preferiamo questa forma"; **"'Forma di Bode' particolarmente comoda per calcolare modulo e fase di $W_s(j\omega)$ e tracciare i diagrammi di Bode"**.

> [!warning] Precisazione
> Così scritta, $W(0)=K$ vale solo se non ci sono termini $s$ (poli o zeri nell'origine): i termini $s^{\pm h}$ restano fuori dalla forma $(1\pm\dots)$, come nell'esempio seguente. In quel caso $K$ si chiama **guadagno** generalizzato. Inoltre gli indici $s_1,\dots,s_n$ e $s_{n+1},\dots,s_{2n}$ degli appunti indicano solo "zeri" e "poli": in generale il loro numero è diverso.

**Esempio.**

$$W(s)=\frac{2(s+1)(s-2)}{s(s+10)(s+2)(s+3)}$$

Si scrivono tutti i termini $(s-s_i)$ come $(1\pm\dots)$, mettendo in evidenza il termine noto:

$$W(s)=\frac{2\cdot(1+s)\cdot(-2)\left(1-\frac s2\right)}{s\cdot10\left(1+\frac{s}{10}\right)\cdot2\left(1+\frac s2\right)\cdot3\left(1+\frac s3\right)}=\underbrace{\frac{2\cdot(-2)}{10\cdot2\cdot3}}_{K}\cdot\frac{(1+s)\left(1-\frac s2\right)}{s\left(1+\frac{s}{10}\right)\left(1+\frac s2\right)\left(1+\frac s3\right)}=-\frac1{15}\cdot\frac{(1+s)\left(1-\frac s2\right)}{s\left(1+\frac{s}{10}\right)\left(1+\frac s2\right)\left(1+\frac s3\right)}$$

Il termine $s$ resta così com'è. La fattorizzazione nella forma di Bode è **unica**.

> [!note] Annotazione di Simone
> Accanto a "unica": **"Nessuna Ambiguità"**.

> [!quote] Dal libro — costanti di tempo
> Il libro scrive i fattori come $(1+\tau s)$, dove $\tau=-\frac{1}{s_i}$ è la **costante di tempo** del polo o dello zero: per esempio $W(s)=\frac{10(s+1)}{s(s-10)(s+0{,}1)}$ in forma di Bode diventa $W(s)=-10\frac{1+s}{s(1-0{,}1s)(1+10s)}$, con un termine costante $K=-10$, un monomio a denominatore, un binomio a numeratore ($\tau_1=1$) e due binomi a denominatore ($\tau=-0{,}1$ e $\tau=10$). _(libro, §5.2, pp. 239–240)_

## Calcolare modulo e fase della risposta armonica

Con due fattori, per esempio

$$W(s)=\frac{1}{(s+10)(s+2)}$$

la **fase** di $W_s(j\omega)$ è semplice: calcolate le fasi di $s+10$ e $s+2$, basta una **somma**. Per il **modulo** no: calcolati i moduli di $s+10$ e $s+2$, serve un **prodotto**, in genere molto più complicato di una somma (soprattutto con i grafici: dati due grafici è facile tracciare quello della somma, non quello del prodotto).

> [!note] Annotazione di Simone
> In rosso: **"PROBLEMA somma fasi ⇒ Easy, prodotto moduli ⇒ Hard"**.

La soluzione è il **logaritmo**: in qualsiasi base,

$$\log_x(ab)=\log_xa+\log_xb,\qquad\log_x\frac ab=\log_xa-\log_xb$$

Il logaritmo è inoltre **monotono**: rispetto alle funzioni originali il grafico è più "schiacciato", ma la monotonia si conserva (dove $f$ cresce cresce anche $\log_xf$, e se $f$ ha un estremo in un punto anche $\log_xf$ lo ha). Per convenzione il modulo di $W_s(j\omega)$ si calcola **in decibel**:

$$|W_s(j\omega)|_{\text{dB}}=20\log_{10}|W_s(j\omega)|$$

cioè in base 10, con il coefficiente 20 (per compensare lo "schiacciamento" del grafico). A differenza di $|W_s(j\omega)|$, che occupa solo la parte superiore del grafico ($\ge0$), $|W_s(j\omega)|_{\text{dB}}$ occupa **tutto** il grafico: il logaritmo è negativo quando il modulo è minore di 1. Nella parte negativa del grafico ci sono quindi tutti i valori per cui la sinusoide si **attenua**, nella parte positiva quelli per cui si **amplifica**.

> [!note] Annotazioni di Simone
> A margine: "Soluzione"; "Sfruttiamo la proprietà dei logaritmi per il calcolo del modulo"; "Altra caratteristica da tenere in considerazione".

> [!note] Perché proprio 20
> La scelta viene dalla teoria dei segnali: il decibel di una quantità $q$ è definito come $10\log_{10}|q|^2$, che è esattamente $20\log_{10}|q|$. La parola "decibel" indica in generale il logaritmo del rapporto tra due grandezze omogenee; si scrive anche $|q|_{\text{dB}}$.

## Grafico logaritmico di funzioni base

> [!note] Annotazione di Simone
> In testa alla pagina, in viola: **"Rappresentazione Forma Bode termini Base"**.

La $W(s)$ fattorizzata (e quindi la risposta armonica) contiene costanti, termini $s$, termini $(s-s_i)$ con radici reali e termini complessi coniugati. Vediamo come si rappresentano nel diagramma di Bode.

### Costante

Una costante $k$ ha modulo $|k|$, che si rappresenta come $20\log_{10}|k|$, indipendente da $\omega$. Essendo $k$ reale, la sua fase è $0$ se $k\ge0$, altrimenti $\pi$ o $-\pi$ (per convenzione si prende $-\pi$):

![[TDS-L22-02.png]]

Per esempio con $k=-10$: modulo $20\log_{10}10=20$ dB e fase $\angle(-10)=-\pi$. Il modulo in dB non cambia tra $k$ positivo o negativo; cambia solo la fase.

> [!note] Annotazioni di Simone
> A mano: "Coefficiente $k$", "Nota questo", "Modulo indipendente da $\omega$", "Se $k\ge0 \Rightarrow \angle k=0$", "Se $k<0\Rightarrow\angle k=-\pi$", "Per convenzione vedi sopra".

### Termine $s$ (monomio)

Nella risposta armonica interessa $W(s)|_{s=j\omega}$, quindi si considera

$$s\big|_{s=j\omega}=j\omega$$

Il suo modulo è $|j\omega|=\sqrt{0^2+\omega^2}=|\omega|$, e in decibel

$$|\omega|_{\text{dB}}=20\log_{10}|\omega|$$

Con $\omega$ in scala reale (lineare) il grafico è una curva logaritmica:

![[TDS-L22-03.png]]

> [!note] Annotazioni di Simone
> A mano: "Consideriamo sempre $s=j\omega$"; "A noi interessa sempre il modulo in decibel perché così lo posso sommare con gli altri moduli in decibel, anziché farne un prodotto, che è più difficile"; "Monomio $s=j\omega$"; "Scala Reale ($\omega$ reale)".

Disegnare il logaritmo non è comodo, soprattutto quando bisogna sommare grafici. Diventa tutto più facile se in ascissa, invece di $\omega$, si mette $\log_{10}\omega$ (scala logaritmica): il grafico diventa una **retta**.

![[TDS-L22-04.png]]

Ogni unità dell'asse non è più costante: è una **decade**, da 1 a 10, da 10 a 100, da 100 a 1000, … in modo esponenziale (lo stesso per i termini negativi del logaritmo: da 1 a 0,1, da 0,1 a 0,01, …). La scala è lineare **rispetto alle decadi**. L'asse $y$ invece è lineare: per questo il piano si dice **semilogaritmico** (logaritmico rispetto a un solo asse).

> [!note] Annotazioni di Simone
> A mano: "più facile da sommare graficamente"; "Consideriamo $\log_{10}(\omega)$ perciò una Scala Logaritmica"; "asse delle ascisse è logaritmico"; "Spiega il piano semilogaritmico".

Essendo $j\omega$ la variabile, con $\omega\ge0$ la **fase è costante a $\frac\pi2$** ($j\omega$ è un immaginario puro sul semiasse immaginario positivo, e forma sempre un angolo $\frac\pi2$ con l'asse reale):

![[TDS-L22-05.png]]

Il modulo $|j\omega|_{\text{dB}}=20\log_{10}|\omega|$ è una retta che "sale" di 20 unità a ogni potenza di 10: la pendenza è di **20 decibel per decade**, $20$ dB/dec. Passa per 0 dB in $\omega=1$.

> [!note] Annotazioni di Simone
> A mano: "$|j\omega|_{\text{dB}}=20\log_{10}(|\omega|)$ è una retta per questo motivo", "scala logaritmica cioè consideriamo $\log_{10}(\omega)$", "$\angle s=\angle j\omega=\frac\pi2$".

> [!quote] Dal libro — monomio a numeratore e a denominatore
> Per il **monomio** $j\omega$: $M_{\text{dB}}=20\log_{10}\omega=20x$ (con $x=\log_{10}\omega$), retta con pendenza 20 dB/decade, fase costante $\frac\pi2$. Un fattore monomio a **denominatore** $\frac{1}{j\omega}$ dà andamenti opposti: $M_{\text{dB}}=-20x$ e fase $-\frac\pi2$ (Figura 5.7 del libro). _(libro, §5.2, p. 237)_
