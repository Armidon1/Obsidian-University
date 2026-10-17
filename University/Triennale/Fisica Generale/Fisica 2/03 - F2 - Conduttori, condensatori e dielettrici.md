---
title: "Conduttori, condensatori e dielettrici"
aliases:
  - "F2 — Conduttori, condensatori e dielettrici"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "97-152"
---

# Conduttori, condensatori e dielettrici

> [!abstract]
> Le cariche libere si redistribuiscono fino a rendere nullo il campo nel metallo in equilibrio. Questa proprietà determina la capacità dei conduttori e il funzionamento dei condensatori; nei dielettrici interviene invece la polarizzazione.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Conduttori in equilibrio elettrostatico

Vedi [[F2 - Conduttori in equilibrio elettrostatico]].

Nel materiale conduttore in equilibrio $\mathbf E=0$, il potenziale è costante e l'eccesso di carica si dispone sulle superfici. Il campo subito all'esterno è normale alla superficie; nel vuoto $E_n=\sigma/\varepsilon_0$. Il risultato viene da una piccola superficie gaussiana a cavallo del confine. In una cavità vuota completamente chiusa e priva di cariche, il campo elettrostatico è nullo; se vi sono cariche interne compare carica indotta sulla parete. Schermatura elettrostatica non significa schermatura universale da campi variabili.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Capacità e condensatori

Vedi [[F2 - Capacità e condensatori]].

Per un conduttore isolato $C=Q/V$ rispetto al riferimento scelto; per due armature con cariche opposte $C=Q/\Delta V$. Nel regime lineare $C$ dipende dalla geometria e dal mezzo, non dal valore di $Q$. Si misura in farad. Per armature piane grandi rispetto alla distanza $d$,
$$C=\varepsilon A/d.$$
Per sfere concentriche di raggi $a<b$, $C=4\pi\varepsilon ab/(b-a)$; per cilindri coassiali lunghi $\ell$, $C=2\pi\varepsilon\ell/\ln(b/a)$. Le formule trascurano gli effetti di bordo dove necessario.

![[F2-p112-1.png]]

*Figura 3-18: fra le armature concentriche si sceglie una superficie gaussiana sferica. Il campo è radiale e costante in modulo su di essa; integrarlo radialmente dà la differenza di potenziale e quindi la capacità.* _(Libro, p. 104; PDF p. 112.)_

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Collegamenti ed energia elettrostatica

Vedi [[F2 - Collegamenti ed energia elettrostatica]].

In parallelo le capacità si sommano perché le differenze di potenziale sono uguali. In serie $1/C_{\mathrm{eq}}=\sum_i1/C_i$ se i nodi intermedi sono inizialmente neutri e isolati.
$$U=\int_0^Q\frac{q}{C}dq=\frac{Q^2}{2C}=\tfrac12C(\Delta V)^2.$$
Nel vuoto l'energia è descrivibile con densità $u_E=\varepsilon_0E^2/2$. La pressione elettrostatica su un conduttore nel vuoto è $p=\varepsilon_0E^2/2$. Per calcolare forze tramite variazione di energia occorre specificare se la carica o la tensione è mantenuta costante e includere il generatore.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Polarizzazione e campo nella materia

Vedi [[F2 - Polarizzazione e campo nella materia]].

In un dielettrico i dipoli permanenti o indotti producono cariche legate. La polarizzazione $\mathbf P$ è il momento di dipolo per volume; $\rho_b=-\nabla\cdot\mathbf P$ e $\sigma_b=\mathbf P\cdot\hat{\mathbf n}$. Definendo
$$\mathbf D=\varepsilon_0\mathbf E+\mathbf P,\qquad\nabla\cdot\mathbf D=\rho_{\mathrm{libera}},$$
si separano cariche libere e legate. In un mezzo lineare isotropo $\mathbf P=\varepsilon_0\chi_e\mathbf E$, quindi $\mathbf D=\varepsilon\mathbf E$, con $\varepsilon=\varepsilon_0(1+\chi_e)$. Queste relazioni non sono universali per materiali non lineari o anisotropi.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Condizioni al contorno ed effetto del dielettrico

Vedi [[F2 - Condizioni al contorno ed effetto del dielettrico]].

All'interfaccia elettrostatica $E_{t,2}=E_{t,1}$ e $D_{n,2}-D_{n,1}=\sigma_{\mathrm{libera}}$, usando la medesima normale orientata da 1 a 2. Riempire un condensatore piano con un dielettrico uniforme moltiplica $C$ per $\varepsilon_r$. Se il condensatore è isolato $Q$ resta costante, la tensione e l'energia diminuiscono. Se è collegato a una batteria ideale la tensione resta costante, la carica cresce e cresce anche l'energia del condensatore; la batteria fornisce energia e va inclusa nel bilancio. La densità $u=\mathbf E\cdot\mathbf D/2$ vale nel caso lineare non dispersivo appropriato.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Unicità, immagini, schermo e stabilità

Vedi [[F2 - Unicità, immagini, schermo e stabilità]].

Assegnare il potenziale sul bordo di una regione e la densità di carica determina univocamente la soluzione elettrostatica regolare appropriata. Il metodo delle immagini costruisce una soluzione equivalente **nella regione fisica** sostituendo i conduttori con cariche fittizie. Una carica $q$ a distanza $a$ da un piano conduttore infinito a terra equivale, nel semispazio della carica, a $-q$ nella posizione speculare. La forza attrattiva ha modulo $q^2/(16\pi\varepsilon_0a^2)$; non si usa la soluzione sotto il piano come campo fisico del problema originale.

Uno schermo conduttore chiuso separa problemi interni ed esterni in condizioni elettrostatiche appropriate. Il teorema di Earnshaw esclude un equilibrio stabile puramente elettrostatico per una carica libera in una regione senza sorgenti: un potenziale armonico non ha un minimo o massimo stretto interno. Vincoli materiali, campi variabili o altre forze cambiano le ipotesi.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Derivazione guidata

Per un condensatore piano ideale con cariche opposte, Gauss dà $E=\sigma/\varepsilon$ fra le armature. La differenza di potenziale è $\Delta V=Ed=Qd/(\varepsilon A)$ e quindi $C=\varepsilon A/d$. Per caricarlo gradualmente la tensione non è già quella finale: $dW=(q/C)dq$. Integrando da 0 a $Q$ ottieni $U=Q^2/(2C)$, da cui il fattore $1/2$. Usare sempre la tensione finale nell'intero processo raddoppierebbe erroneamente il lavoro immagazzinato.

_(Libro, cap. 3; pagine stampate 89–144; PDF pp. 97–152.)_

## Esempio svolto

> [!example] Applicazione originale
> Un condensatore da $10\,\mathrm{\mu F}$ a $12\,\mathrm V$ contiene $Q=120\,\mathrm{\mu C}$ e $U=0{,}72\,\mathrm{mJ}$. Dopo averlo scollegato, un dielettrico con $\varepsilon_r=3$ porta $C$ a $30\,\mathrm{\mu F}$, la tensione a $4\,\mathrm V$ e l'energia a $0{,}24\,\mathrm{mJ}$.

## Richiami matematici

[[10 - AN1 - Integrali Multipli]] · [[08 - AN1 - Calcolo Differenziale in più Variabili]].

## Verifica attiva

Inserendo un dielettrico raddoppia la capacità di un condensatore: l’energia aumenta o diminuisce?

> [!check]- Risposta ragionata
> A carica fissata si dimezza; a tensione fissata raddoppia. Nel secondo caso la batteria scambia energia: il vincolo elettrico è parte del problema.

## Navigazione

Precedente: [[02 - F2 - Potenziale elettrostatico]] · Successivo: [[04 - F2 - Correnti elettriche stazionarie]].
