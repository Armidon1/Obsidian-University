---
title: "Primo principio della termodinamica"
aliases:
  - "F1 — Primo principio della termodinamica"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "310-351"
---

# Primo principio della termodinamica

> [!abstract]
> Il primo principio è il bilancio energetico del sistema. Distingue una grandezza di stato, l’energia interna, da due modalità di trasferimento, calore e lavoro.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Convenzione dei segni e primo principio

Vedi [[F1 - Convenzione dei segni e primo principio]].

In queste note $Q>0$ indica calore ricevuto dal sistema e $W>0$ lavoro compiuto dal sistema sull'ambiente:
$$\Delta U=Q-W.$$
$U$ è funzione di stato; $Q$ e $W$ dipendono dal percorso. In forma differenziale $dU=\delta Q-\delta W$: il simbolo $\delta$ ricorda che calore e lavoro non sono differenziali di funzioni di stato. In un ciclo $\Delta U=0$ e quindi $Q_{\mathrm{netto}}=W_{\mathrm{netto}}$. Non esiste un "calore contenuto" nel sistema.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Lavoro di espansione e gas ideale

Vedi [[F1 - Lavoro di espansione e gas ideale]].

Il lavoro di frontiera è $\delta W=p_{\mathrm{ext}}dV$ per un pistone con pressione esterna opponente ben definita; in una trasformazione reversibile $p_{\mathrm{ext}}\simeq p$ e $W=\int p\,dV$. La pressione del sistema non va usata indiscriminatamente in processi irreversibili.

Per un gas ideale $U=U(T)$ e $dU=nC_VdT$. Se $C_V$ è costante $\Delta U=nC_V\Delta T$. Non significa che ogni processo abbia calore $nC_V\Delta T$: questa uguaglianza vale per un'isocora con solo lavoro di espansione.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Calori molari e relazione di Mayer

Vedi [[F1 - Calori molari e relazione di Mayer]].

Con solo lavoro $p\,dV$, per il gas ideale $C_P-C_V=R$ e $\gamma=C_P/C_V$. Nel regime classico a gradi di libertà attivi fissi, un gas monoatomico ha $C_V=3R/2$, $C_P=5R/2$. Per un biatomico con rotazioni attive e vibrazioni trascurabili $C_V=5R/2$. L'entalpia $H=U+pV$ è utile a pressione costante: in queste condizioni e con il solo lavoro di espansione $Q_P=\Delta H$.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Trasformazioni fondamentali del gas ideale

Vedi [[F1 - Trasformazioni fondamentali del gas ideale]].

Per capacità termiche costanti:

| Processo | Lavoro del gas | Variazione di energia interna |
|---|---|---|
| Isocoro | $0$ | $nC_V\Delta T$ |
| Isobaro | $p(V_f-V_i)$ | $nC_V\Delta T$ |
| Isotermo reversibile | $nRT\ln(V_f/V_i)$ | $0$ |
| Adiabatico | $-\Delta U$ | $nC_V\Delta T$ |

L'adiabatica **reversibile** soddisfa inoltre $pV^\gamma=\mathrm{costante}$ e $TV^{\gamma-1}=\mathrm{costante}$. Adiabatico significa $Q=0$, non temperatura costante e non automaticamente reversibilità.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Gas reali, cambiamenti di fase e Clapeyron

Vedi [[F1 - Gas reali, cambiamenti di fase e Clapeyron]].

Le interazioni molecolari e il volume proprio delle molecole causano deviazioni da $pV=nRT$. Un modello qualitativo è $(p+a n^2/V^2)(V-nb)=nRT$, con parametri materiali $a,b$. Nei gas reali $U$ può dipendere anche dal volume. La laminazione di Joule-Thomson è approssimativamente isoentalpica in flusso stazionario adiabatico, in assenza di lavoro d'albero e con variazioni cinetiche e potenziali trascurabili: non va confusa con l'espansione libera di Joule.

Nel diagramma $p,T$ le curve di coesistenza separano le fasi; il punto triplo permette tre fasi in equilibrio e il punto critico termina la distinzione liquido-vapore. La pendenza di una curva di coesistenza soddisfa
$$\frac{dp_{\mathrm{eq}}}{dT}=\frac{\lambda}{T(v_2-v_1)},$$
con calore latente e volumi **specifici** riferiti alla stessa quantità di materia. Nell'approssimazione di vapore ideale e volume del liquido trascurabile si ottiene la forma di Clausius-Clapeyron. Non confondere questa relazione con il semplice nome "piano di Clapeyron" per il diagramma $p,V$.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Espansione libera, cicli e teoria cinetica

Vedi [[F1 - Espansione libera, cicli e teoria cinetica]].

Nell'espansione libera in un recipiente isolato contro il vuoto $Q=W=0$. Per un gas ideale $\Delta U=0$ implica $\Delta T=0$, ma il processo è irreversibile e non segue una curva isoterma di stati d'equilibrio intermedi.

Nel modello cinetico monoatomico $\langle K_{\mathrm{trasl}}\rangle=3k_BT/2$ e $p=\tfrac13(N/V)m\langle v^2\rangle$. La temperatura si collega all'agitazione microscopica. I cicli nel piano $p,V$ hanno lavoro netto pari all'area orientata racchiusa quando il percorso è quasistatico.

![[F1-p329-1.png]]

*Figura 12.14: il ciclo di Carnot nel piano pressione-volume comprende due isoterme e due adiabatiche reversibili. L’area racchiusa è il lavoro netto del gas; le adiabatiche non sono segmenti verticali.* _(Libro, p. 320; PDF p. 329.)_

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Derivazione guidata

Per un'adiabatica reversibile di gas ideale con $C_V$ costante, $nC_VdT=-p\,dV=-nRT\,dV/V$. Dividi per $nT$ e integra: $C_V\ln(T_f/T_i)=-R\ln(V_f/V_i)$. Con $R/C_V=\gamma-1$ ottieni $TV^{\gamma-1}=\mathrm{costante}$ e, usando l'equazione di stato, $pV^\gamma=\mathrm{costante}$. Il passaggio $p_{\mathrm{ext}}=p$ usa la reversibilità: per un'adiabatica irreversibile la conclusione non segue.

_(Libro, cap. 12; pagine stampate 301–342; PDF pp. 310–351.)_

## Esempio svolto

> [!example] Applicazione originale
> Una mole di gas ideale si espande reversibilmente a $T=300\,\mathrm K$ raddoppiando il volume. $W=RT\ln2=1{,}73\,\mathrm{kJ}$ e, poiché $\Delta U=0$, $Q=W$. Nell'espansione libera fra gli stessi volumi di un gas ideale isolato sarebbero invece $W=Q=0$: gli stati estremi non determinano gli scambi.

## Richiami matematici

[[06 - AN1 - Calcolo Integrale]] · [[08 - AN1 - Calcolo Differenziale in più Variabili]].

## Verifica attiva

Un gas ideale isolato si espande nel vuoto: quale lavoro compie?

> [!check]- Risposta ragionata
> Nell’espansione libera la pressione opponente è nulla, quindi $W=0$; con $Q=0$ si ha $\Delta U=0$ e la temperatura finale coincide con l’iniziale.

## Navigazione

Precedente: [[11 - F1 - Sistemi termodinamici e temperatura]] · Successivo: [[13 - F1 - Secondo principio ed entropia]].
