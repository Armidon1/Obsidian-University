---
title: "Progetto in frequenza e reti compensatrici"
aliases:
  - "CA — Progetto in frequenza e reti compensatrici"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "74-92"
class_label: "23/03"
---

# Progetto in frequenza e reti compensatrici

> [!abstract]
> Questa lezione sviluppa progetto in frequenza e reti compensatrici seguendo il blocco delle pagine 74–92 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 23/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[08 - CA - Specifiche dinamiche e simulazioni di controllo]]. **Dopo:** [[10 - CA - Esercizi di compensazione anticipatrice e attenuatrice]].

## Separare precisione e forma dell’anello

Vedi [[CA - Sintesi in frequenza]] · [[CA - Struttura del controllore]].

Il progetto cerca un controllore realizzabile $G$ tale che $F=GP$ abbia integratori e guadagno corretti a bassa frequenza, attraversamento e fase opportuni nella banda di controllo, attenuazione alle alte frequenze. Si scrive spesso
$$G(s)=\frac K{s^h}R(s),\qquad R(0)=1.$$
Il numero $h$ si sceglie dalle specifiche statiche e dai poli in origine già presenti nel processo; $K$ si determina dall'errore ammesso. La rete $R$ modifica la forma del Bode senza alterare il guadagno statico normalizzato.

Procedimento: ricavare $P$ e i trasferimenti dei disturbi; scegliere $h$; imporre $K$; tracciare l'anello non compensato; misurare il difetto di fase e modulo vicino a $\omega_c$; scegliere e verificare la rete. Il progetto si conclude solo dopo stabilità interna, specifiche chiuse e realizzabilità del controllore.

_(Dispensa commentata, pagine PDF 74–76; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 74
> ![[CA-p074-1.jpg]]
> La sintesi in frequenza viene organizzata in scelte di struttura, guadagno e funzione compensatrice.

> [!example]- Materiale originale — pagina PDF 75
> ![[CA-p075-1.jpg]]
> I requisiti statici e dinamici occupano regioni diverse del diagramma: bassa frequenza per precisione, attraversamento per rapidità e robustezza.

> [!example]- Materiale originale — pagina PDF 76
> ![[CA-p076-1.jpg]]
> L'esempio fissa integratori e guadagno dall'errore ammesso, quindi valuta il margine dell'anello iniziale.

## Rete anticipatrice

Vedi [[CA - Rete anticipatrice]] · [[CA - Massimo anticipo di fase]].

Con $0<\alpha<1$ una rete anticipatrice normalizzata è
$$R_a(s)=\frac{1+\tau s}{1+\alpha\tau s}.$$
Lo zero precede il polo e la rete aggiunge fase positiva. Il massimo anticipo e la pulsazione corrispondente sono
$$\varphi_{\max}=\arcsin\frac{1-\alpha}{1+\alpha},\quad \omega_m=\frac1{\tau\sqrt\alpha},\quad |R_a(j\omega_m)|=\frac1{\sqrt\alpha}.$$
Per ottenere $30^\circ$, $\alpha=(1-\sin30^\circ)/(1+\sin30^\circ)=1/3$; il modulo al centro aumenta di $10\log_{10}3\simeq4.77$ dB. Questo sposta l'attraversamento: non si può sommare l'anticipo alla fase letta al vecchio $\omega_c$ e assumere che il margine finale sia esatto.

Si sceglie il centro in prossimità dell'attraversamento desiderato e si impone anche il bilancio del modulo. Se serve troppo anticipo si possono concatenare più reti moderate, controllando l'aumento del guadagno alle alte frequenze.

_(Dispensa commentata, pagine PDF 77–79; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 77
> ![[CA-p077-1.jpg]]
> La rete anticipatrice colloca lo zero prima del polo: offre fase positiva ma aumenta anche il modulo nella banda interessata.

> [!example]- Materiale originale — pagina PDF 78
> ![[CA-p078-1.jpg]]
> La rete attenuatrice colloca il polo prima dello zero: riduce il modulo alto e introduce un ritardo di fase da contenere in attraversamento.

> [!example]- Materiale originale — pagina PDF 79
> ![[CA-p079-1.jpg]]
> I diagrammi universali mostrano l'anticipo e il guadagno della rete in coordinate normalizzate; identificare il significato dell'ascissa prima del dimensionamento.

## Rete attenuatrice e verifica del progetto

Vedi [[CA - Rete attenuatrice]] · [[CA - Verifica delle specifiche]].

Una rete attenuatrice normalizzata può essere scritta
$$R_r(s)=\frac{1+\tau s}{1+m\tau s},\qquad m>1.$$
Il polo precede lo zero: il guadagno ad alta frequenza tende a $1/m$ e la fase è negativa. Posizionare entrambe le rotture abbastanza sotto $\omega_c$ permette di ridurre il modulo nella zona di attraversamento con una perdita di fase contenuta. L'attenuatrice non crea anticipo: può aumentare il margine **indirettamente**, portando l'attraversamento in una regione dove il processo ha meno ritardo di fase.

La precisione si conserva se $R_r(0)=1$ e non si cambia $K$. Un progetto misto usa anticipatrice per la fase e attenuatrice per il bilancio del modulo. Calcolare sempre le funzioni esatte dopo la scelta dei parametri e controllare tutti gli attraversamenti.

Gli esempi delle dispense mostrano che cambiare il guadagno e aggiungere una rete hanno effetti congiunti. La sintesi per tentativi ragionati è accettabile se ogni iterazione verifica i vincoli esatti e non soltanto gli asintoti.

_(Dispensa commentata, pagine PDF 80–82; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 80
> ![[CA-p080-1.jpg]]
> La prima compensazione confronta il margine desiderato con quello disponibile e colloca le rotture per chiudere il bilancio di fase e modulo.

> [!example]- Materiale originale — pagina PDF 81
> ![[CA-p081-1.jpg]]
> Le curve prima e dopo la compensazione mostrano lo spostamento dell'attraversamento: il nuovo margine deve essere misurato nel punto aggiornato.

> [!example]- Materiale originale — pagina PDF 82
> ![[CA-p082-1.jpg]]
> L'esercizio con due reti sfrutta più gradi di libertà per controllare contemporaneamente precisione statica e forma dell'anello.

## Esercizio riassuntivo con disturbo in uscita

Vedi [[CA - Progetto riassuntivo in frequenza]].

Il testo assegna $P(s)=10/[(1+0.1s)(1+0.01s)]$, disturbo costante all'uscita, errore nullo al gradino, errore alla rampa unitaria al più 0.01 e varie coppie di specifiche su banda e risonanza. Poiché $P(0)=10$ e non ci sono integratori, si pone $G=KR/s$, con $R(0)=1$.

Allora $K_v=10K$ ed $e_\infty=1/(10K)\le0.01$ richiede $K\ge10$. Con il minimo $K=10$, $F_0=100/[s(1+0.1s)(1+0.01s)]$.

> [!example] Perché serve compensare
> A $\omega=30$ rad/s, $|F_0|=100/[30\sqrt{10}\sqrt{1.09}]\simeq1.010$ e la fase è $-90^\circ-\arctan3-\arctan0.3\simeq-178.26^\circ$. Il margine vicino all'attraversamento è quasi nullo: i vincoli statici sono rispettati ma il transitorio sarà molto oscillatorio.

Le pagine successive confrontano reti per i tre casi: banda circa 50 rad/s e risonanza al più 9 dB, banda circa 10 rad/s e risonanza al più 4 dB, banda circa 50 rad/s e risonanza al più 1 dB. Banda e $\omega_c$ non sono identiche: il risultato va controllato su $T=F/(1+F)$, normalizzando il modulo al valore statico. Il limite sul picco in dB si converte con $M_r=10^{M_{r,\mathrm{dB}}/20}$.

_(Dispensa commentata, pagine PDF 83–92; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 83
> ![[CA-p083-1.jpg]]
> Il testo dell'esercizio riassuntivo assegna il processo con due poli reali, un disturbo in uscita e tre alternative di banda e risonanza.

> [!example]- Materiale originale — pagina PDF 84
> ![[CA-p084-1.jpg]]
> La soluzione sceglie l'integratore e il minimo guadagno ammesso dalla rampa, poi traccia l'anello non compensato.

> [!example]- Materiale originale — pagina PDF 85
> ![[CA-p085-1.jpg]]
> Il diagramma universale serve a scegliere l'anticipo necessario; il modulo della rete contribuisce allo spostamento di attraversamento.

> [!example]- Materiale originale — pagina PDF 86
> ![[CA-p086-1.jpg]]
> La prima rete viene collocata rispetto alla frequenza obiettivo; i diagrammi confrontano il livello di modulo richiesto e la fase aggiunta.

> [!example]- Materiale originale — pagina PDF 87
> ![[CA-p087-1.jpg]]
> Il nuovo Bode verifica il primo progetto e la sua fase; la compensazione aggiuntiva regola l'attraversamento senza perdere la precisione fissata.

> [!example]- Materiale originale — pagina PDF 88
> ![[CA-p088-1.jpg]]
> Il trasferimento chiuso viene controllato sul picco e sulla banda: l'esito non si deduce dal solo Bode aperto.

> [!example]- Materiale originale — pagina PDF 89
> ![[CA-p089-1.jpg]]
> La variante a banda più bassa usa una diversa collocazione delle rotture; la risposta chiusa va normalizzata al guadagno statico.

> [!example]- Materiale originale — pagina PDF 90
> ![[CA-p090-1.jpg]]
> Il confronto fra anelli della variante mette in evidenza l'attenuazione necessaria e il margine risultante.

> [!example]- Materiale originale — pagina PDF 91
> ![[CA-p091-1.jpg]]
> La variante con picco molto contenuto richiede maggiore smorzamento; la rete finale modifica fase e guadagno nella zona di attraversamento.

> [!example]- Materiale originale — pagina PDF 92
> ![[CA-p092-1.jpg]]
> Gli ultimi grafici confrontano anello finale e modulo chiuso della terza variante, verificando il compromesso richiesto fra banda e risonanza.

## Esercizi collegati

[[E01 - CA - Prova intermedia 2018-2019]] · [[E03 - CA - Prova intermedia 2020-2021]] · [[E05 - CA - Prova intermedia 2022-2023]] · [[E14 - CA - Prova completa del 12 luglio 2019]]
