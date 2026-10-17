---
title: "Prova finale 2020-2021"
aliases:
  - "CA — Prova finale 2020-2021"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "57-62"
---

# Prova finale 2020-2021

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Realizzazione del controllore

Si assegnano separatamente i poli di controllo e stima, poi si scrive il compensatore nelle coordinate originali. Non identificare i suoi poli isolati con quelli del complesso: questi ultimi sono l'unione delle dinamiche $A+BK$ e $A-LC$.

## Problema 2 - Pendolo e misure disponibili

Dal modello linearizzato si ottiene una coppia raggiungibile; con sola misura angolare il sistema del secondo ordine è osservabile e si può usare un osservatore. Con sola velocità, l'osservabilità dipende dal termine di richiamo: verificare il rango, soprattutto nei casi degeneri.

## Problema 3 - Modo stabile non raggiungibile

Per $\dot x_1=2x_1+(1+\sin^2x_1)x_2+2u$, $\dot x_2=-x_2$, l'origine non forzata è instabile perché la Jacobiana ha autovalori $2,-1$. La linearizzazione ha $B=(2,0)^T$: il modo $-1$ non è raggiungibile ma è stabile. Con $u=k_1x_1+k_2x_2$ basta $k_1<-1$ per ottenere AS locale.

Una legge verificabile globalmente è
$$u=-\frac{2+c}{2}x_1-\frac{1+\sin^2x_1}{2}x_2,\qquad c>0.$$
Sostituendola si ottiene $\dot x_1=-cx_1$, $\dot x_2=-x_2$, quindi GAS. Il confronto evidenzia che la cancellazione riguarda soltanto i termini accessibili al comando; la modalità autonoma stabile può essere lasciata invariata.

_(Eserciziario, pagine PDF 57–62; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 57
> ![[CA-E-p057-1.jpg]]
> Traccia completa della prova finale 2020-2021. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 58
> ![[CA-E-p058-1.jpg]]
> Problema 1: guadagno di stato e controllo dei ranghi. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 59
> ![[CA-E-p059-1.jpg]]
> Problema 1: osservatore e dinamica del compensatore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 60
> ![[CA-E-p060-1.jpg]]
> Problema 2: pendolo, misure disponibili e osservatore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 61
> ![[CA-E-p061-1.jpg]]
> Problema 3: linearizzazione con modo stabile fisso. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 62
> ![[CA-E-p062-1.jpg]]
> Problema 3: controllo non lineare e conclusione globale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
