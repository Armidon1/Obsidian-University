---
title: "Prova intermedia 2021-2022"
aliases:
  - "CA — Prova intermedia 2021-2022"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "17-23"
---

# Prova intermedia 2021-2022

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[07 - CA - Disturbi rumore e astaticità]] · [[14 - CA - Punti multipli e costruzione del luogo delle radici]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Problema 1 - Poli sull asse immaginario

Con $F=k(s+1)/(s^2+1)$ si ha $\chi=s^2+ks+(1+k)$. L'AS richiede **$k>0$**. Per $-1<k<0$ ci sono due poli con parte reale positiva; per $k<-1$ uno. In $k=-1$ c'è un polo nullo e uno positivo; in $k=0$ rimane la coppia $\pm j$.

Il luogo parte da $\pm j$, arriva allo zero $-1$ e all'infinito. Nyquist richiede le deviazioni attorno ai poli sull'asse: la sola curva campionata a frequenze ordinarie non contiene tutto il contorno.

## Problemi 2 e 3 - Progetto con disturbi

Separare il canale del comando da quello del disturbo nel sistema a rami. Per il processo con poli instabili non è consentito applicare meccanicamente il criterio semplificato di Bode: verificare prima Nyquist e il polinomio completo. La dimensione minima del controllore va giustificata confrontando le strutture più semplici con i vincoli richiesti.

## Problema 4 - Vero o falso

«Un integratore nel processo basta per rigettare ogni disturbo costante» è falso: dipende dal punto di iniezione. «Una FdT chiusa stabile certifica sempre stabilità interna» è falso in presenza di modi nascosti. «Una sola lettura di margine positivo vale per qualunque anello» è falso: servono le ipotesi del criterio semplificato. Ogni risposta va motivata con un trasferimento o un controesempio, non con una parola isolata.

_(Eserciziario, pagine PDF 17–23; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 17
> ![[CA-E-p017-1.jpg]]
> Traccia completa della prova intermedia 2021-2022. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 18
> ![[CA-E-p018-1.jpg]]
> Problema 1: Nyquist con poli immaginari e intervallo stabile. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 19
> ![[CA-E-p019-1.jpg]]
> Problema 1: verifica del luogo delle radici. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 20
> ![[CA-E-p020-1.jpg]]
> Problema 2: processo a rami, disturbo e progetto di Bode. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 21
> ![[CA-E-p021-1.jpg]]
> Problema 2: diagrammi e rete risultante. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 22
> ![[CA-E-p022-1.jpg]]
> Problema 3: controllore di dimensione minima e luogo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 23
> ![[CA-E-p023-1.jpg]]
> Problema 4: risposte motivate ai quesiti vero/falso. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
