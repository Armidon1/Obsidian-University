---
title: "Interconnessioni e criterio di Nyquist"
aliases:
  - "CA — Interconnessioni e criterio di Nyquist"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "17-34"
class_label: "Blocco in ordine di dispensa; data non assegnata"
---

# Interconnessioni e criterio di Nyquist

> [!abstract]
> Questa lezione sviluppa interconnessioni e criterio di nyquist seguendo il blocco delle pagine 17–34 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Prima:** [[01 - CA - Risposta armonica e diagrammi di Bode]]. **Dopo:** [[03 - CA - Retroazione e stabilità al variare del guadagno]].

## Serie parallelo e retroazione

Vedi [[CA - Interconnessioni]] · [[CA - Retroazione negativa]].

In serie si moltiplicano le FdT, in parallelo si sommano. La retroazione negativa di due blocchi $P$ e $H$ dà $W=P/(1+PH)$. Questa formula discende dalle equazioni $e=r-Hy$, $y=Pe$: va ricavata dai segni dei sommatori, senza affidarsi alla posizione dei blocchi nel disegno.

Nella realizzazione in serie gli stati sono quelli di entrambi i sottosistemi. Il fatto che una FdT si semplifichi non elimina fisicamente uno stato. Perciò un'interconnessione può avere un trasferimento esterno stabile ma un modo interno instabile nascosto. È particolarmente rischioso cancellare poli instabili con zeri del controllore.

Nel caso con trasmissione diretta occorre anche che l'anello sia ben posto: le equazioni algebriche devono ammettere una soluzione unica (nel caso scalare, $1+D_PD_H\ne0$). Vedi [[TDS - Sistemi interconnessi]] e [[TDS - Retroazione]].

_(Dispensa commentata, pagine PDF 17–21; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 17
> ![[CA-p017-1.jpg]]
> La cascata moltiplica i trasferimenti, ma conserva gli stati di entrambi i blocchi: una cancellazione esterna può nascondere un modo interno.

> [!example]- Materiale originale — pagina PDF 18
> ![[CA-p018-1.jpg]]
> Il parallelo somma le FdT con i segni dei rami; gli esempi mettono a confronto comportamento ingresso-uscita e dinamica interna.

> [!example]- Materiale originale — pagina PDF 19
> ![[CA-p019-1.jpg]]
> Le equazioni della retroazione producono il denominatore 1 più la funzione d'anello; la realizzazione a stati mostra quali modi vengono effettivamente modificati.

> [!example]- Materiale originale — pagina PDF 20
> ![[CA-p020-1.jpg]]
> Lo schema retroazionato e le condizioni di ben posizione ricordano che la soluzione dei segnali interni deve esistere ed essere unica.

> [!example]- Materiale originale — pagina PDF 21
> ![[CA-p021-1.jpg]]
> Gli esempi confrontano poli chiusi e modi interni: un trasferimento ridotto stabile non autorizza a cancellare dinamiche instabili.

## Il punto critico e il conteggio di Nyquist

Vedi [[CA - Criterio di Nyquist]] · [[CA - Avvolgimenti del punto critico]].

Posto $F=PH$, l'equazione caratteristica è $1+F(s)=0$. I poli dell'anello chiuso sono quindi collegati al comportamento di $F$ attorno al punto $-1$. Fissiamo la convenzione: $P$ è il numero di poli di $F$ nel semipiano destro, $Z$ il numero di zeri di $1+F$ nello stesso semipiano e $N_{\rm cw}$ il numero netto di avvolgimenti **orari** di $-1$ lungo il diagramma del contorno che racchiude il semipiano destro percorso in senso orario. Allora
$$N_{\rm cw}=Z-P,\qquad Z=P+N_{\rm cw}.$$
Per stabilità AS serve $Z=0$, nessun polo sull'asse immaginario dell'anello chiuso e nessun modo instabile nascosto. Se $P=0$ non devono esserci avvolgimenti netti; se $P>0$ servono $P$ avvolgimenti antiorari.

> [!important] Prima la convenzione
> Nei testi $N$ può contare avvolgimenti antiorari: cambia il segno della formula, non il risultato. Dichiarare sempre verso del contorno e verso positivo del conteggio.

La curva si costruisce dal ramo $\omega>0$, dal suo coniugato e dagli eventuali archi dovuti alle deviazioni attorno ai poli sull'asse immaginario. Non basta osservare il solo ramo positivo. Vedi [[TDS - Criterio di Nyquist]].

_(Dispensa commentata, pagine PDF 22–24; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 22
> ![[CA-p022-1.jpg]]
> L'enunciato di Nyquist collega poli aperti, poli chiusi e giri attorno al punto critico; il verso del conteggio va dichiarato.

> [!example]- Materiale originale — pagina PDF 23
> ![[CA-p023-1.jpg]]
> Il diagramma polare mostra come verificare la stabilità quando il ramo d'anello non ha poli instabili: il punto da sorvegliare è meno uno.

> [!example]- Materiale originale — pagina PDF 24
> ![[CA-p024-1.jpg]]
> Il Bode guida la forma del diagramma polare: i passaggi sul reale negativo determinano i guadagni critici.

## Guadagno variabile e verifica con Routh

Vedi [[CA - Stabilità al variare del guadagno]].

Se $F(s)=kF_0(s)$, un guadagno positivo dilata radialmente il diagramma senza ruotarlo; uno negativo introduce anche una rotazione di $180^\circ$. I valori critici si trovano imponendo $F(j\omega)=-1$. Il guadagno per il quale la curva attraversa $-1$ è un valore di frontiera, non un valore AS.

> [!example] Controllo numerico indipendente
> Per $F=k/[(s+1)(s+2)(s+3)]$, $\chi(s)=s^3+6s^2+11s+6+k$. Routh dà $6+k>0$ e $66>6+k$: dunque $-6<k<60$. Per $k=60$ compaiono $\pm j\sqrt{11}$ e $-6$, per $k=-6$ un polo nullo. I due estremi sono esclusi.

Se esistono poli in origine, la curva richiede l'indentazione del contorno: il ramo può andare all'infinito e il contributo di chiusura non si può ignorare. In presenza di più attraversamenti dell'asse reale negativo va contato l'effetto di tutti gli avvolgimenti. Questo spiega perché un unico margine letto su Bode può essere insufficiente.

_(Dispensa commentata, pagine PDF 25–34; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 25
> ![[CA-p025-1.jpg]]
> Variando il guadagno positivo, la curva cambia scala; le intersezioni critiche separano intervalli con diverso numero di poli instabili.

> [!example]- Materiale originale — pagina PDF 26
> ![[CA-p026-1.jpg]]
> Il confronto fra guadagni positivi e negativi richiede anche una rotazione di 180 gradi, non soltanto una variazione del raggio.

> [!example]- Materiale originale — pagina PDF 27
> ![[CA-p027-1.jpg]]
> Il conteggio degli avvolgimenti viene verificato con il polinomio caratteristico: ogni intervallo richiede una prova rappresentativa.

> [!example]- Materiale originale — pagina PDF 28
> ![[CA-p028-1.jpg]]
> Il Bode e il polare vengono letti insieme per localizzare una soglia; il valore di frontiera non è un punto AS.

> [!example]- Materiale originale — pagina PDF 29
> ![[CA-p029-1.jpg]]
> Il foglio di calcolo applica Routh agli intervalli trovati graficamente: le disuguaglianze completano il disegno di Nyquist.

> [!example]- Materiale originale — pagina PDF 30
> ![[CA-p030-1.jpg]]
> Con poli nell'origine il diagramma si estende all'infinito: il contributo del piccolo arco del contorno non deve essere perso.

> [!example]- Materiale originale — pagina PDF 31
> ![[CA-p031-1.jpg]]
> Gli archi di chiusura completano il conteggio del punto critico; il solo tratto a frequenze finite non descrive l'intero contorno.

> [!example]- Materiale originale — pagina PDF 32
> ![[CA-p032-1.jpg]]
> L'esercizio con più fattori richiede di identificare tutte le rotture e tutti i passaggi critici, non un solo incrocio del Bode.

> [!example]- Materiale originale — pagina PDF 33
> ![[CA-p033-1.jpg]]
> Il confronto con Routh quantifica il guadagno critico; il diagramma distingue poi i casi positivi e negativi.

> [!example]- Materiale originale — pagina PDF 34
> ![[CA-p034-1.jpg]]
> Una coppia complessa modifica modulo e fase vicino alla pulsazione naturale e produce una geometria di Nyquist diversa da quella dei poli reali.

## Esercizi collegati

[[E01 - CA - Prova intermedia 2018-2019]] · [[E02 - CA - Prova intermedia 2019-2020]] · [[E03 - CA - Prova intermedia 2020-2021]] · [[E04 - CA - Prova intermedia 2021-2022]] · [[E05 - CA - Prova intermedia 2022-2023]] · [[E06 - CA - Prova intermedia 2023-2024]] · [[E07 - CA - Prova intermedia 2024-2025]]
