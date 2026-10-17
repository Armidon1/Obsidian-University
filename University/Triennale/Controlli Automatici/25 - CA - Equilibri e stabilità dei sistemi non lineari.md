---
title: "Equilibri e stabilità dei sistemi non lineari"
aliases:
  - "CA — Equilibri e stabilità dei sistemi non lineari"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "194-212"
class_label: "05/05"
---

# Equilibri e stabilità dei sistemi non lineari

> [!abstract]
> Questa lezione sviluppa equilibri e stabilità dei sistemi non lineari seguendo il blocco delle pagine 194–212 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 05/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[24 - CA - Inseguimento di riferimenti e modello interno]]. **Dopo:** [[26 - CA - Metodo diretto di Lyapunov]].

## Punti di equilibrio e piano delle fasi

Vedi [[CA - Equilibri non lineari]] · [[CA - Piano delle fasi]].

Per $\dot x=f(x)$, un punto di equilibrio $x_e$ soddisfa $f(x_e)=0$: se si parte lì, si rimane lì. Un sistema non lineare può avere più equilibri isolati, ciascuno con stabilità diversa. La stabilità è una proprietà dell'equilibrio, non un'etichetta unica da attribuire indiscriminatamente al sistema.

Nel pendolo $\dot\theta=\omega$, $\dot\omega=-(g/\ell)\sin\theta-b\omega$, gli equilibri sono $(k\pi,0)$. Nella coordinata angolare su $\mathbb R$ sono infiniti; sul cilindro che identifica angoli equivalenti si distinguono configurazioni basse e alte. Il piano delle fasi mostra traiettorie, attrattori e separatrici senza risolvere esplicitamente ogni evoluzione.

Per confrontare traiettorie vicine a un equilibrio si può traslare $z=x-x_e$. La stabilità di $x_e$ diventa quella dell'origine del sistema traslato. Richiami: [[TDS - Punti di equilibrio]] e [[TDS - Linearizzazione]].

_(Dispensa commentata, pagine PDF 194–204; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 194
> ![[CA-p194-1.jpg]]
> Le slide introducono la teoria della stabilità non lineare come studio qualitativo, distinto dal calcolo esplicito di tutte le soluzioni.

> [!example]- Materiale originale — pagina PDF 195
> ![[CA-p195-1.jpg]]
> Il modello generale non lineare descrive stato, ingresso e uscita e motiva il problema delle perturbazioni dello stato iniziale.

> [!example]- Materiale originale — pagina PDF 196
> ![[CA-p196-1.jpg]]
> L'idea di stabilità confronta evoluzione nominale e perturbata: piccole variazioni iniziali devono restare controllate nel tempo.

> [!example]- Materiale originale — pagina PDF 197
> ![[CA-p197-1.jpg]]
> La teoria separa definizioni, condizioni e criteri, distinguendo la proprietà da verificare dallo strumento usato per provarla.

> [!example]- Materiale originale — pagina PDF 198
> ![[CA-p198-1.jpg]]
> Il problema viene ricondotto all'evoluzione libera attorno a un equilibrio, traslando lo stato quando necessario.

> [!example]- Materiale originale — pagina PDF 199
> ![[CA-p199-1.jpg]]
> Gli equilibri sono zeri del campo vettoriale; nel caso lineare sono il nucleo della matrice A.

> [!example]- Materiale originale — pagina PDF 200
> ![[CA-p200-1.jpg]]
> Il richiamo fisico del pendolo costruisce lo stato angolo-velocità e il termine gravitazionale non lineare.

> [!example]- Materiale originale — pagina PDF 201
> ![[CA-p201-1.jpg]]
> La ricerca degli equilibri del pendolo distingue configurazioni basse e alte e anticipa le loro diverse stabilità.

> [!example]- Materiale originale — pagina PDF 202
> ![[CA-p202-1.jpg]]
> Le slide riportano il modello del pendolo con attrito e mostrano il legame fra coordinate fisiche e stato.

> [!example]- Materiale originale — pagina PDF 203
> ![[CA-p203-1.jpg]]
> Le traiettorie nel piano delle fasi rendono visibili oscillazioni e convergenza; altri esempi ricordano che possono esistere più equilibri isolati.

> [!example]- Materiale originale — pagina PDF 204
> ![[CA-p204-1.jpg]]
> I grafici scalari mostrano come il verso del campo ai lati di un equilibrio consenta di riconoscere attrazione o repulsione.

## Stabilità secondo Lyapunov

Vedi [[CA - Stabilità di Lyapunov]] · [[CA - Attrattività]].

L'equilibrio $x_e$ è stabile se per ogni $\varepsilon>0$ esiste $\delta>0$ tale che $\|x(0)-x_e\|<\delta$ implichi $\|x(t)-x_e\|<\varepsilon$ per ogni $t\ge0$. Il significato è mantenere piccole perturbazioni sempre piccole, non necessariamente farle sparire.

È attrattivo se tutte le traiettorie che partono in un intorno convergono a $x_e$. È asintoticamente stabile se è **sia stabile sia attrattivo**. La sola attrattività non sostituisce la stabilità: nei sistemi non lineari possono esistere escursioni grandi prima della convergenza.

La negazione della stabilità richiede una perturbazione arbitrariamente piccola che prima o poi esca da un intorno fissato. Instabile non significa necessariamente che ogni traiettoria diverga all'infinito: può avvicinarsi a un altro equilibrio o a un ciclo limite.

_(Dispensa commentata, pagine PDF 205–209; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 205
> ![[CA-p205-1.jpg]]
> La definizione di stabilità usa due intorni: la condizione iniziale deve poter essere scelta abbastanza vicina da non uscire dall'intorno assegnato.

> [!example]- Materiale originale — pagina PDF 206
> ![[CA-p206-1.jpg]]
> Gli esempi distinguono proprietà dell'equilibrio e comportamento globale; un ciclo limite può attrarre senza rendere stabile l'origine.

> [!example]- Materiale originale — pagina PDF 207
> ![[CA-p207-1.jpg]]
> Gli schemi scalari evidenziano che la stabilità non richiede convergenza e che una traiettoria limitata non basta a classificare un equilibrio.

> [!example]- Materiale originale — pagina PDF 208
> ![[CA-p208-1.jpg]]
> La stabilità asintotica aggiunge la convergenza locale alla stabilità, e non va confusa con la sola attrattività.

> [!example]- Materiale originale — pagina PDF 209
> ![[CA-p209-1.jpg]]
> Il controesempio mostra una convergenza accompagnata da grandi escursioni: l'attrattività da sola non sostituisce la definizione di stabilità.

## Stabilità esponenziale e proprietà globali

Vedi [[CA - Stabilità esponenziale]] · [[CA - Stabilità globale]] · [[CA - Dominio di attrazione]].

Un equilibrio è localmente esponenzialmente stabile se esistono $c,\alpha,\rho>0$ tali che
$$\|x(t)-x_e\|\le c e^{-\alpha t}\|x(0)-x_e\|\qquad\text{per }\|x(0)-x_e\|<\rho.$$
La stima dà anche una velocità di convergenza uniforme. La stabilità esponenziale implica AS; nei sistemi non lineari il contrario non vale.

> [!example] AS senza convergenza esponenziale
> Per $\dot x=-x^3$, $x(t)=x_0/\sqrt{1+2x_0^2t}$. L'origine è globalmente AS, ma il decadimento è algebrico. La linearizzazione ha autovalore zero e non risolve il problema.

Il dominio di attrazione è l'insieme delle condizioni iniziali da cui si converge all'equilibrio. Si parla di GAS se la stabilità è accompagnata dalla convergenza da ogni stato iniziale dello spazio considerato. Prima di affermare una proprietà globale bisogna specificare lo spazio di stato e l'esistenza delle soluzioni per tutti i tempi positivi.

_(Dispensa commentata, pagine PDF 210–212; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 210
> ![[CA-p210-1.jpg]]
> La stabilità esponenziale introduce una stima uniforme della velocità di convergenza; il caso cubico mostra AS senza decadimento esponenziale.

> [!example]- Materiale originale — pagina PDF 211
> ![[CA-p211-1.jpg]]
> L'inviluppo esponenziale visualizza il vincolo sulla distanza dall'equilibrio e il ruolo della condizione iniziale.

> [!example]- Materiale originale — pagina PDF 212
> ![[CA-p212-1.jpg]]
> La mappa delle proprietà distingue stabilità locale, asintotica, esponenziale e rispettive versioni globali.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]]
