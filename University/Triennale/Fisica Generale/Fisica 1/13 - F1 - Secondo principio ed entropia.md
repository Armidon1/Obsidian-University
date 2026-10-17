---
title: "Secondo principio ed entropia"
aliases:
  - "F1 — Secondo principio ed entropia"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "352-382"
---

# Secondo principio ed entropia

> [!abstract]
> Il bilancio energetico da solo non stabilisce quali trasformazioni siano possibili. Il secondo principio impone un verso ai processi e limita la conversione di calore in lavoro.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Enunciati di Kelvin-Planck e Clausius

Vedi [[F1 - Enunciati di Kelvin-Planck e Clausius]].

Non esiste una macchina ciclica il cui unico risultato sia convertire interamente in lavoro il calore prelevato da una sola sorgente. Non esiste un processo il cui unico risultato sia trasferire calore da un corpo freddo a uno caldo. I due enunciati sono equivalenti: violarne uno permetterebbe di costruire un dispositivo che viola l'altro. Le espressioni "ciclica" e "unico risultato" sono essenziali: un gas può convertire tutto il calore in lavoro durante una singola espansione isoterma, modificando però il proprio stato.

![[F1-p353-1.png]]

*Figura 13.2: combinando una macchina che violerebbe Kelvin-Planck con un frigorifero si otterrebbe un trasferimento netto dal freddo al caldo senza lavoro esterno. I flussi intermedi si cancellano: restano gli effetti netti sull’ambiente.* _(Libro, p. 344; PDF p. 353.)_

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Macchine termiche, frigoriferi e teorema di Carnot

Vedi [[F1 - Macchine termiche, frigoriferi e teorema di Carnot]].

Un motore assorbe $Q_h>0$, cede un calore di modulo $Q_c>0$ e produce $W=Q_h-Q_c$. Il rendimento è $\eta=1-Q_c/Q_h$. Tra due sorgenti a $T_h>T_c$,
$$\eta\le1-\frac{T_c}{T_h},$$
con uguaglianza per ciclo reversibile. Il ciclo di Carnot contiene due isoterme e due adiabatiche reversibili. Per un frigorifero $\mathrm{COP}=Q_c/W\le T_c/(T_h-T_c)$; per una pompa di calore $\mathrm{COP}_h=Q_h/W$. Le temperature nei rapporti sono assolute.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Disuguaglianza di Clausius ed entropia

Vedi [[F1 - Disuguaglianza di Clausius ed entropia]].

Per un ciclo $\oint\delta Q/T_{\mathrm{sorgente}}\le0$, con uguaglianza nel caso reversibile. Si definisce una funzione di stato $S$ tramite
$$S(B)-S(A)=\int_{A}^{B}\frac{\delta Q_{\mathrm{rev}}}{T}.$$
Se il processo reale è irreversibile, si usa un percorso reversibile ausiliario fra gli stessi stati. Non si sostituisce automaticamente il calore reale nell'integrale. L'entropia si misura in $\mathrm{J/K}$; può diminuire in un sistema che cede entropia all'ambiente.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Calcolo dell’entropia e produzione interna

Vedi [[F1 - Calcolo dell’entropia e produzione interna]].

Per un gas ideale, con $C_V$ costante,
$$\Delta S=nC_V\ln\frac{T_f}{T_i}+nR\ln\frac{V_f}{V_i}.$$
Per una sorgente a temperatura costante $\Delta S_{\mathrm{sorgente}}=Q_{\mathrm{ricevuto}}/T$. Per un sistema chiuso $\Delta S=\int\delta Q/T_{\mathrm{confine}}+S_{\mathrm{gen}}$, con $S_{\mathrm{gen}}\ge0$. L'universo sistema più ambiente soddisfa $\Delta S_{\mathrm{universo}}\ge0$; in un'adiabatica reversibile $\Delta S=0$, in un'adiabatica irreversibile cresce.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Energia utilizzabile e significato statistico

Vedi [[F1 - Energia utilizzabile e significato statistico]].

L'energia si conserva ma la sua capacità di produrre lavoro dipende anche dall'entropia e dall'ambiente disponibile. Una produzione di entropia $S_{\mathrm{gen}}$ comporta, rispetto a un ambiente a $T_0$, una perdita di lavoro utile pari a $T_0S_{\mathrm{gen}}$ nel confronto appropriato fra processi con gli stessi vincoli. La relazione statistica $S=k_B\ln\Omega$ collega l'entropia al numero di microstati compatibili con il macrostato, nel caso di microstati equiprobabili. "Disordine" è solo un'immagine intuitiva e non un metodo di calcolo.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Temperatura termodinamica e terzo principio

Vedi [[F1 - Temperatura termodinamica e terzo principio]].

Per un ciclo reversibile di Carnot il rapporto dei moduli dei calori è $Q_c/Q_h=T_c/T_h$: ciò definisce una scala termodinamica indipendente dalla sostanza utilizzata. Nei limiti del gas ideale coincide con la scala assoluta introdotta dalla termometria.

L'enunciato di Nernst riguarda l'annullarsi delle variazioni di entropia di trasformazioni isoterme reversibili quando $T\to0$. Una formulazione usuale assegna entropia nulla a un cristallo perfetto con stato fondamentale non degenere a $0\,\mathrm K$; sistemi con degenerazione o disordine congelato richiedono cautela. Lo zero assoluto non è raggiungibile mediante un numero finito di processi fisici. Non si deve prolungare fino a zero la formula del gas ideale a calori specifici costanti.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Derivazione guidata

Per calcolare $\Delta S$ di un gas ideale scegli un percorso reversibile ausiliario. Dal primo principio $\delta Q_{\mathrm{rev}}=nC_VdT+p\,dV$. Dividi per $T$ e sostituisci $p/T=nR/V$: $dS=nC_VdT/T+nR\,dV/V$. L'integrazione dà la formula logaritmica. Il percorso reversibile serve al calcolo; il risultato dipende solo dagli estremi e vale anche per il processo reale irreversibile che li collega.

_(Libro, cap. 13; pagine stampate 343–373; PDF pp. 352–382.)_

## Esempio svolto

> [!example] Applicazione originale
> Una mole di gas ideale si espande liberamente e adiabaticamente da $V$ a $2V$. Gli stati estremi hanno uguale temperatura, quindi $\Delta S=R\ln2=5{,}76\,\mathrm{J/K}$. Nonostante $Q=0$, l'entropia aumenta: tutta la variazione è produzione interna. Un motore fra $600$ e $300\,\mathrm K$ ha invece rendimento massimo $0{,}50$.

## Richiami matematici

[[06 - AN1 - Calcolo Integrale]] · [[08 - AN1 - Calcolo Differenziale in più Variabili]].

## Verifica attiva

Se un sistema è adiabatico, la sua entropia è necessariamente costante?

> [!check]- Risposta ragionata
> No: senza scambio entropico la variazione coincide con la produzione interna. È zero per il processo reversibile, positiva per quello irreversibile.

## Navigazione

Precedente: [[12 - F1 - Primo principio della termodinamica]] · Successivo: [[MOC - Fisica 1]].
