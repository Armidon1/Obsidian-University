---
title: "Specifiche dinamiche e simulazioni di controllo"
aliases:
  - "CA — Specifiche dinamiche e simulazioni di controllo"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "61-73"
class_label: "21/03"
---

# Specifiche dinamiche e simulazioni di controllo

> [!abstract]
> Questa lezione sviluppa specifiche dinamiche e simulazioni di controllo seguendo il blocco delle pagine 61–73 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 21/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[07 - CA - Disturbi rumore e astaticità]]. **Dopo:** [[09 - CA - Progetto in frequenza e reti compensatrici]].

## Rapidità sovraelongazione e banda

Vedi [[CA - Tempo di assestamento]] · [[CA - Sovraelongazione]] · [[CA - Banda passante]].

Per un sistema con guadagno statico non nullo, la banda passante a $-3$ dB si misura rispetto a $|T(0)|$, non sempre rispetto a 0 dB assoluti. Un sistema con banda più ampia tende a rispondere più rapidamente, purché il confronto avvenga tra dinamiche simili e senza effetti dominanti di zeri o ritardi.

Per un secondo ordine standard con $0<\zeta<1$:
$$M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}},\quad t_p=\frac\pi{\omega_n\sqrt{1-\zeta^2}},\quad t_{s,2\%}\simeq\frac4{\zeta\omega_n}.$$
$M_p$ è una frazione: $M_p=0.1$ significa 10%. Il tempo di assestamento è una stima basata sull'inviluppo esponenziale, non una formula esatta per qualunque sistema.

> [!example] Traduzione in poli desiderati
> Per sovraelongazione al più 10%, $\zeta\ge-\ln(0.1)/\sqrt{\pi^2+\ln^2(0.1)}\simeq0.591$. Per $t_s\le2$ s si richiede approssimativamente $\zeta\omega_n\ge2$, cioè poli dominanti con parte reale al più $-2$.

_(Dispensa commentata, pagine PDF 61–64; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 61
> ![[CA-p061-1.jpg]]
> Le specifiche dinamiche collegano risposta al gradino, velocità di assestamento e forma del trasferimento chiuso.

> [!example]- Materiale originale — pagina PDF 62
> ![[CA-p062-1.jpg]]
> Il foglio di esempio confronta una specifica sul transitorio con il Bode: il calcolo statico non esaurisce il progetto.

> [!example]- Materiale originale — pagina PDF 63
> ![[CA-p063-1.jpg]]
> Il legame tra margine, risonanza e banda suggerisce come modellare l'anello; sono relazioni di progetto da verificare sul chiuso.

> [!example]- Materiale originale — pagina PDF 64
> ![[CA-p064-1.jpg]]
> La tabella e le annotazioni confrontano rapidità e sovraelongazione: un aumento di banda può accompagnarsi a uno smorzamento peggiore.

## Esperimenti con gradino rampa e disturbi

Vedi [[CA - Verifica in simulazione]].

Le simulazioni mostrano prima la risposta al gradino con integratore nel processo, poi la risposta a rampa e parabola, quindi l'effetto dei disturbi. Si verifica ogni previsione statica dopo aver controllato la stabilità della configurazione simulata.

> [!warning] Correzione: errore sulla rampa
> Nel testo della simulazione (PDF p. 66) si legge che la rampa in uscita «non è unitaria» e si parla di «offset della pendenza». In un anello AS di tipo 1, l'uscita a regime ha **la stessa pendenza** della rampa di riferimento e un errore **costante** di posizione $a/K_v$. Non si tratta di una diversa pendenza a regime.

> [!warning] Correzione: integratore e stabilità
> La pagina 65 associa la dicitura «Processo AS» alla presenza di $1/s$. Un processo con polo in origine non è AS come sistema LTI. Per usare le formule d'errore occorre la stabilità dell'**anello chiuso**, non quella di un processo che contiene un integratore.

L'aggiunta di un integratore puro al controllore può rendere instabile il sistema; l'azione proporzionale introduce smorzamento e può ripristinare un intervallo stabile. Le condizioni specifiche dipendono dal modello e vanno ricavate dal suo polinomio caratteristico.

_(Dispensa commentata, pagine PDF 65–68; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 65
> ![[CA-p065-1.jpg]]
> Il modello Simulink verifica l'inseguimento al gradino e la presenza di errore nullo quando l'anello chiuso stabile contiene l'azione integrale necessaria.

> [!example]- Materiale originale — pagina PDF 66
> ![[CA-p066-1.jpg]]
> Le risposte a rampa e parabola distinguono offset costante ed errore divergente; la pendenza della rampa non va confusa con l'offset di posizione.

> [!example]- Materiale originale — pagina PDF 67
> ![[CA-p067-1.jpg]]
> I disturbi costanti in punti diversi producono effetti diversi; l'integratore aggiunto al controllore può compromettere la stabilità.

> [!example]- Materiale originale — pagina PDF 68
> ![[CA-p068-1.jpg]]
> L'azione proporzionale insieme a quella integrale ripristina smorzamento; il disturbo di misura rimane in conflitto con l'inseguimento del riferimento.

## Dall’anello aperto alla risposta chiusa

Vedi [[CA - Legame tra margine e transitorio]].

I grafici confrontano sistemi con picchi di risonanza simili e bande diverse, poi la stessa struttura con guadagno variato. Aumentare il guadagno spesso alza $\omega_c$, ma può ridurre il margine di fase, aumentare il picco chiuso e rendere più oscillatorio il gradino.

Non c'è una relazione universale che imponga banda passante sempre maggiore di $\omega_c$. La relazione dipende dalla forma dell'anello e dalla normalizzazione. Le corrispondenze «margine maggiore → minore sovraelongazione» e «attraversamento più alto → maggiore rapidità» sono criteri di progetto per famiglie regolari a poli dominanti, da verificare sul trasferimento effettivo.

> [!warning] Correzione del confronto di banda
> A p. 71 la banda passante viene detta «sempre maggiore» della pulsazione di attraversamento. È un'osservazione sul caso rappresentato, non una proprietà generale di ogni sistema retroazionato.

Le ultime pagine propongono esercizi di scelta del guadagno e del compensatore: il vincolo statico fissa il comportamento vicino all'origine, mentre il vincolo dinamico richiede di modellare il diagramma vicino all'attraversamento desiderato.

_(Dispensa commentata, pagine PDF 69–73; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 69
> ![[CA-p069-1.jpg]]
> Le tre curve confrontano picchi di risonanza e bande differenti: la rapidità va valutata insieme all'oscillazione della risposta.

> [!example]- Materiale originale — pagina PDF 70
> ![[CA-p070-1.jpg]]
> I Bode di anello e del chiuso vengono associati alla risposta al gradino: il margine guida qualitativamente la sovraelongazione.

> [!example]- Materiale originale — pagina PDF 71
> ![[CA-p071-1.jpg]]
> Aumentare il guadagno sposta l'attraversamento e modifica il margine; l'effetto sulla banda del caso disegnato non costituisce una disuguaglianza universale.

> [!example]- Materiale originale — pagina PDF 72
> ![[CA-p072-1.jpg]]
> L'esercizio impone prima i requisiti statici e poi quelli dinamici: il controllore deve soddisfare simultaneamente entrambe le parti.

> [!example]- Materiale originale — pagina PDF 73
> ![[CA-p073-1.jpg]]
> Il diagramma dell'esercizio mostra perché un solo guadagno può lasciare poco margine e richiedere una rete compensatrice.
