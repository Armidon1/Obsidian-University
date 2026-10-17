---
title: "Prova finale 2023-2024 e assegnazione canonica"
aliases:
  - "CA — Prova finale 2023-2024 e assegnazione canonica"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "73-79"
---

# Prova finale 2023-2024 e assegnazione canonica

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[26 - CA - Metodo diretto di Lyapunov]] · [[27 - CA - LaSalle linearizzazione e studio degli equilibri]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Parametri e controllo dell’uscita

Analizzare separatamente i valori che fanno perdere rango a raggiungibilità e osservabilità. Poi verificare i modi associati: un rango deficitario può essere compatibile con la stabilizzazione, ma limita l'assegnazione dei poli. L'esercizio canonico aggiunto alle pp. 78–79 permette di ricontrollare l'assegnazione mediante coefficienti.

## Problema 2 - Sistema di Lorenz

Con $a>0$, $\dot x_1=a(x_2-x_1)$, $\dot x_2=bx_1-x_2-x_1x_3$, $\dot x_3=x_1x_2-cx_3$. Se $c\ne0$, oltre all'origine compaiono $(q,q,b-1)$ con $q=\pm\sqrt{c(b-1)}$ quando $c(b-1)>0$; in $c(b-1)=0$ bisogna analizzare direttamente le equazioni per evitare di contare due volte la stessa soluzione. Se $c=0$, esiste la retta di equilibri $(0,0,x_3)$ e non si deve dividere per $c$ nel calcolo degli equilibri.

Nell'origine il polinomio della Jacobiana è $(\lambda+c)[\lambda^2+(a+1)\lambda+a(1-b)]$: per il criterio indiretto, $c>0,b<1$ garantiscono AS locale.

Per $b=-1,c=1$, la candidata $V=(x_1^2/a+x_2^2+x_3^2)/2$ dà
$$\dot V=-(x_1+x_2)^2-x_3^2\le0.$$
In $E$ vale $x_2=-x_1,x_3=0$, ma $\dot x_3=x_1x_2=-x_1^2$ obbliga $x_1=0$ per restarvi. Il massimo insieme invariante è l'origine; LaSalle e la limitatezza radiale danno GAS.

## Problema 3 - Basta misurare una componente

Per $\dot x_1=x_1+x_1x_2^2+u$, $\dot x_2=-x_1^2x_2-x_2$, scegliere $u=-kx_1$, $k>1$. La linearizzazione è Hurwitz e, con $V=(x_1^2+x_2^2)/2$, $\dot V=-(k-1)x_1^2-x_2^2$: i termini misti non lineari si cancellano. Si ottiene GAS usando soltanto $x_1$, senza osservatore.

_(Eserciziario, pagine PDF 73–79; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 73
> ![[CA-E-p073-1.jpg]]
> Traccia completa della prova finale 2023-2024. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 74
> ![[CA-E-p074-1.jpg]]
> Problema 1: valori parametrici e ranghi. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 75
> ![[CA-E-p075-1.jpg]]
> Problema 1: realizzazione del controllore con osservatore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 76
> ![[CA-E-p076-1.jpg]]
> Problema 2: Lorenz, equilibri e funzione di Lyapunov. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 77
> ![[CA-E-p077-1.jpg]]
> Problema 3: stabilizzazione con misura della sola prima componente. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 78
> ![[CA-E-p078-1.jpg]]
> Esercizio canonico aggiunto: assegnazione dei poli. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 79
> ![[CA-E-p079-1.jpg]]
> Esercizio canonico aggiunto: verifica del polinomio. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
