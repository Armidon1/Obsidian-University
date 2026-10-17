---
title: "Induzione e campi elettromagnetici"
aliases:
  - "F2 — Induzione e campi elettromagnetici"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "245-296"
---

# Induzione e campi elettromagnetici

> [!abstract]
> Un flusso magnetico variabile genera una forza elettromotrice. L’induzione porta dai circuiti quasi stazionari alle equazioni di Maxwell, che descrivono campi elettrici e magnetici dipendenti dal tempo.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Legge di Faraday e verso di Lenz

Vedi [[F2 - Legge di Faraday e verso di Lenz]].

Fissati orientazione del contorno e normale concatenata,
$$\mathcal E_{\mathrm{ind}}=-\frac{d\Phi_B}{dt},\qquad\Phi_B=\int_S\mathbf B\cdot d\mathbf S.$$
Il segno meno esprime Lenz: la corrente indotta tende a opporsi alla **variazione** di flusso, non necessariamente al campo preesistente. Il flusso può variare perché cambia $B$, l'area o l'orientazione. Il numero di spire entra nel flusso concatenato totale. La legge consente f.e.m. anche se il circuito è aperto; la corrente dipende poi dal circuito.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Induzione da movimento e campo elettrico indotto

Vedi [[F2 - Induzione da movimento e campo elettrico indotto]].

Per un circuito mobile con velocità locale $\mathbf u$, la f.e.m. è $\oint(\mathbf E+\mathbf u\times\mathbf B)\cdot d\mathbf l$. Una sbarra di lunghezza $\ell$ che scorre ortogonalmente a sé e a $\mathbf B$ uniforme genera un modulo $B\ell u$. Per un contorno fisso,
$$\oint\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_S\mathbf B\cdot d\mathbf S,\qquad\nabla\times\mathbf E=-\partial_t\mathbf B.$$
Il campo elettrico indotto non è generalmente conservativo: una sola funzione $V$ non può descriverlo globalmente. Nei generatori il lavoro meccanico mantiene il moto contro la reazione elettromagnetica.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Mutua induzione, autoinduzione ed energia

Vedi [[F2 - Mutua induzione, autoinduzione ed energia]].

Per circuiti fissi e mezzi lineari, il flusso concatenato è proporzionale alle correnti: $\Phi_2=M_{21}I_1$ e $\Phi_{\mathrm{proprio}}=LI$. Allora $\mathcal E_L=-L\,dI/dt$ per $L$ costante. La convenzione passiva sul componente dà invece $V_L=L\,dI/dt$: i segni descrivono due definizioni differenti, compatibili.
$$U_B=\tfrac12LI^2,\qquad u_B=\frac{B^2}{2\mu_0}\quad\text{nel vuoto}.$$
La mutua induttanza dipende da geometria e orientazioni. Le formule circuitali presuppongono un regime quasi stazionario in cui i ritardi di propagazione sul circuito sono trascurabili.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Circuiti LC e transitorio RL

Vedi [[F2 - Circuiti LC e transitorio RL]].

Nel circuito LC ideale $L\ddot q+q/C=0$, con $\omega_0=1/\sqrt{LC}$. L'energia oscilla tra $q^2/(2C)$ e $LI^2/2$. Una resistenza dissipa energia e smorza le oscillazioni.

Nel circuito RL alimentato da un gradino $\mathcal E$, con corrente iniziale nulla,
$$I(t)=\frac{\mathcal E}{R}(1-e^{-tR/L}),\qquad\tau=L/R.$$
In spegnimento $I=I_0e^{-t/\tau}$. La corrente nell'induttore non può saltare senza una tensione impulsiva. L'analogia con massa, attrito e molla permette di trasferire gli strumenti dell'oscillatore meccanico.

![[F2-p267-1.png]]

*Figura 6-30: il commutatore collega il circuito RL al generatore oppure lo lascia scaricare attraverso R. L’induttanza rende continua la corrente; la resistenza determina il decadimento dell’energia immagazzinata.* _(Libro, p. 259; PDF p. 267.)_

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Equazioni di Maxwell e corrente di spostamento

Vedi [[F2 - Equazioni di Maxwell e corrente di spostamento]].

Nel vuoto le equazioni locali sono
$$\nabla\cdot\mathbf E=\rho/\varepsilon_0,\quad\nabla\cdot\mathbf B=0,$$
$$\nabla\times\mathbf E=-\partial_t\mathbf B,\quad\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\varepsilon_0\partial_t\mathbf E.$$
La corrente di spostamento $\varepsilon_0\partial_t\mathbf E$ rende Ampère compatibile con la continuità della carica. Nel condensatore in carica il suo flusso fra le armature eguaglia la corrente nel filo nel modello ideale. Nella materia si usano $\mathbf D$ e $\mathbf H$ separando sorgenti libere e legate.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Corrente alternata, trasformatori e filtri

Vedi [[F2 - Corrente alternata, trasformatori e filtri]].

Per sinusoidi si rappresentano tensioni e correnti con fasori complessi. Le impedenze sono $Z_R=R$, $Z_L=i\omega L$, $Z_C=1/(i\omega C)$. In una serie RLC $Z=R+i(\omega L-1/(\omega C))$ e la potenza media assorbita è $V_{\mathrm{rms}}I_{\mathrm{rms}}\cos\varphi$.

Un trasformatore ideale ha $V_2/V_1=N_2/N_1$ e conserva la potenza, quindi il rapporto delle correnti è inverso. Richiede flusso variabile: non trasforma una tensione continua stazionaria. Filtri e risonanza dipendono da come la frequenza modifica l'impedenza. La propagazione libera dei campi è sviluppata nel capitolo seguente.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Induttanza mutua, betatrone e propagazione

Vedi [[F2 - Induttanza mutua, betatrone e propagazione]].

In un sistema lineare reciproco, con orientazioni coerenti, $M_{12}=M_{21}=M$ e l'energia magnetica è $U=\tfrac12L_1I_1^2+\tfrac12L_2I_2^2+MI_1I_2$. La positività impone $M^2\le L_1L_2$; si introduce il coefficiente di accoppiamento $k=M/\sqrt{L_1L_2}$ con segno dipendente dalle orientazioni. I filtri RL e RC selezionano frequenze mediante il rapporto tra le impedenze, mentre la risonanza RLC nasce dalla compensazione delle reattanze.

Nel betatrone un campo magnetico variabile induce il campo elettrico che accelera le particelle, mentre il campo magnetico ne curva l'orbita; per un'orbita circolare fissa la condizione ideale lega il campo medio sul disco a due volte il campo sull'orbita. Quando la dimensione del dispositivo non è piccola rispetto alla lunghezza d'onda, il modello a parametri concentrati cede il posto alla propagazione dei campi.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Derivazione guidata

La divergenza di un rotore è zero. Applicandola alla sola legge magnetostatica $\nabla\times\mathbf B=\mu_0\mathbf J$ otterresti $\nabla\cdot\mathbf J=0$, incompatibile con accumuli di carica variabili. Aggiungendo $\mu_0\varepsilon_0\partial_t\mathbf E$ e usando Gauss ricavi $0=\mu_0[\nabla\cdot\mathbf J+\partial_t\rho]$, esattamente la continuità della carica. La correzione di Maxwell è quindi necessaria per una descrizione coerente dei campi variabili.

_(Libro, cap. 6; pagine stampate 237–288; PDF pp. 245–296.)_

## Esempio svolto

> [!example] Applicazione originale
> Una spira fissa di area $0{,}020\,\mathrm{m^2}$ è normale a un campo che cresce a $0{,}50\,\mathrm{T/s}$. $|\mathcal E|=A|\dot B|=0{,}010\,\mathrm V$. Con $R=2{,}0\,\Omega$ e autoinduzione trascurabile $I=5{,}0\,\mathrm{mA}$. Il verso si sceglie in modo che il campo della corrente indotta contrasti l'aumento del flusso.

## Richiami matematici

[[11 - AN1 - Numeri Complessi]] · [[02 - F1 - Dinamica del punto e leggi di Newton]] · [[06 - AN1 - Calcolo Integrale]].

## Verifica attiva

Fra le armature di un condensatore ideale in carica manca corrente di conduzione: perché Ampère non dà risultati diversi scegliendo superfici diverse?

> [!check]- Risposta ragionata
> La corrente di spostamento fra le armature compensa l’assenza della conduzione. La legge completa di Ampère-Maxwell rende il risultato indipendente dalla superficie scelta con lo stesso contorno.

## Navigazione

Precedente: [[05 - F2 - Campi magnetici stazionari]] · Successivo: [[07 - F2 - Onde elettromagnetiche]].
