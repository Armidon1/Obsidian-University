---
title: "Fenomeni elettrici e legge di Gauss"
aliases:
  - "F2 — Fenomeni elettrici e legge di Gauss"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "9-56"
---

# Fenomeni elettrici e legge di Gauss

> [!abstract]
> L’elettrostatica studia cariche ferme e campi indipendenti dal tempo. Si passa dagli esperimenti di elettrizzazione alla legge di Coulomb, poi dal campo delle singole cariche al suo flusso attraverso una superficie.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Carica elettrica e induzione elettrostatica

Vedi [[F2 - Carica elettrica e induzione elettrostatica]].

La carica ha due segni, è additiva e si conserva in un sistema isolato. A scala microscopica i trasferimenti ordinari avvengono in multipli della carica elementare $e$. Un conduttore possiede portatori mobili; in un isolante le cariche sono maggiormente vincolate. Un corpo neutro può essere attratto da un corpo carico perché le cariche si redistribuiscono o si polarizzano. Nell'induzione non si crea carica: si modifica la sua distribuzione. Il collegamento a terra permette scambio di carica con un grande serbatoio.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Legge di Coulomb e campo elettrico

Vedi [[F2 - Legge di Coulomb e campo elettrico]].

Nel vuoto la forza su $q$ prodotta da una carica puntiforme $Q$ è
$$\mathbf F=\frac{qQ}{4\pi\varepsilon_0r^2}\hat{\mathbf r},\qquad\mathbf E=\frac{\mathbf F}{q}.$$
$\hat{\mathbf r}$ è diretto da $Q$ al punto di osservazione; il segno del prodotto stabilisce attrazione o repulsione. Il campo si definisce mediante una carica di prova abbastanza piccola da non perturbare le sorgenti. Si misura in $\mathrm{N/C}$, equivalenti a $\mathrm{V/m}$. Le linee di campo sono tangenti a $\mathbf E$, non sono traiettorie obbligate delle particelle.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Sovrapposizione e distribuzioni continue

Vedi [[F2 - Sovrapposizione e distribuzioni continue]].

Il campo totale è la somma vettoriale dei contributi. Per una distribuzione volumica,
$$\mathbf E(\mathbf r)=\frac1{4\pi\varepsilon_0}\int\rho(\mathbf r')\frac{\mathbf r-\mathbf r'}{|\mathbf r-\mathbf r'|^3}dV'.$$
Si sostituisce $dq=\lambda\,dl$ o $dq=\sigma\,dS$ per fili o superfici. È essenziale distinguere coordinate della sorgente e del punto di osservazione. Prima di integrare, usare la simmetria per cancellare componenti opposte e individuare la direzione del campo. In corrispondenza di distribuzioni idealmente singolari possono comparire discontinuità o divergenze.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Flusso, angolo solido e legge di Gauss

Vedi [[F2 - Flusso, angolo solido e legge di Gauss]].

Il flusso orientato è $\Phi_E=\int_S\mathbf E\cdot\hat{\mathbf n}\,dS$. Per una superficie chiusa la normale è uscente e
$$\oint_S\mathbf E\cdot d\mathbf S=\frac{Q_{\mathrm{int}}}{\varepsilon_0}.$$
L'angolo solido sotteso da $dS$ visto dalla sorgente è $d\Omega=(\hat{\mathbf r}\cdot\hat{\mathbf n})dS/r^2$; per una superficie chiusa che avvolge la sorgente l'integrale vale $4\pi$. Le cariche esterne possono contribuire al campo sulla superficie, ma il loro flusso netto è nullo. Flusso nullo non significa campo nullo.

![[F2-p030-1.png]]

*Figura 1-26: l’analogia con la portata di un fluido rende visibile il prodotto scalare. Attraversa la superficie solo la componente della velocità normale alla sezione; il fattore coseno compare per la stessa ragione nel flusso elettrico.* _(Libro, p. 22; PDF p. 30.)_

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Uso delle simmetrie e divergenza

Vedi [[F2 - Uso delle simmetrie e divergenza]].

Gauss fornisce direttamente $E$ quando la simmetria permette di portarlo fuori dall'integrale. Per una sfera uniformemente carica di raggio $R$ e carica $Q$, $E=Qr/(4\pi\varepsilon_0R^3)$ all'interno e $E=Q/(4\pi\varepsilon_0r^2)$ all'esterno. Per un filo infinito $E=\lambda/(2\pi\varepsilon_0r)$; per un piano infinito isolante $|E|=|\sigma|/(2\varepsilon_0)$ su ciascun lato. Localmente $\nabla\cdot\mathbf E=\rho/\varepsilon_0$. Il piano conduttore richiede invece le condizioni di equilibrio del capitolo 3.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Verifiche sperimentali e unità

Vedi [[F2 - Verifiche sperimentali e unità]].

La bilancia di torsione collega una forza elettrica a un momento meccanico misurabile e consente di verificare la dipendenza dalla distanza. Nell'esperimento di Millikan si bilanciano o confrontano peso efficace, forza elettrica e resistenza viscosa di goccioline: dalle misure emerge la quantizzazione della carica. Le unità vanno trattate coerentemente: qui tutte le formule sono nel Sistema Internazionale. I coefficienti $1/(4\pi\varepsilon_0)$ e $\mu_0/(4\pi)$ non si trasferiscono senza conversione ai sistemi gaussiani.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Derivazione guidata

Per una sfera uniformemente carica usa una superficie gaussiana concentrica di raggio $r$. Per simmetria $\mathbf E$ è radiale e $E$ costante sulla superficie, quindi il flusso è $4\pi r^2E$. Se $r<R$, la carica interna è $Q(r/R)^3$: segue $E=Qr/(4\pi\varepsilon_0R^3)$. Se $r>R$ la carica interna è $Q$ e segue l'andamento $r^{-2}$. La legge di Gauss è sempre valida; la simmetria è ciò che rende possibile ricavare il campo da questo solo integrale.

_(Libro, cap. 1; pagine stampate 1–48; PDF pp. 9–56.)_

## Esempio svolto

> [!example] Applicazione originale
> Una superficie chiusa racchiude $q_1=3\,\mathrm{nC}$ e $q_2=-1\,\mathrm{nC}$. Il flusso è $2\cdot10^{-9}/\varepsilon_0\simeq226\,\mathrm{N\,m^2/C}$. Aggiungere una carica esterna cambia il campo nei singoli punti ma non questo valore del flusso.

## Richiami matematici

[[GEO - Prodotto scalare geometrico]] · [[10 - AN1 - Integrali Multipli]] · [[GEO - Riferimento cartesiano ortonormale]].

## Verifica attiva

Una superficie gaussiana racchiude carica totale nulla. Il campo è nullo ovunque sulla superficie?

> [!check]- Risposta ragionata
> No. È nullo il flusso netto: contributi entranti e uscenti possono compensarsi mentre il campo locale resta non nullo.

## Navigazione

Precedente: [[00 - F2 - Guida allo studio]] · Successivo: [[02 - F2 - Potenziale elettrostatico]].
