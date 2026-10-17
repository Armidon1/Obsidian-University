---
title: "Metodo diretto di Lyapunov"
aliases:
  - "CA — Metodo diretto di Lyapunov"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "213-244"
class_label: "11/05"
---

# Metodo diretto di Lyapunov

> [!abstract]
> Questa lezione sviluppa metodo diretto di lyapunov seguendo il blocco delle pagine 213–244 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 11/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[25 - CA - Equilibri e stabilità dei sistemi non lineari]]. **Dopo:** [[27 - CA - LaSalle linearizzazione e studio degli equilibri]].

## Caso lineare e idea energetica

Vedi [[CA - Energia come funzione di Lyapunov]] · [[CA - Stabilità lineare e non lineare]].

Per i sistemi LTI finiti la stabilità AS coincide con quella esponenziale; se $A$ è Hurwitz, l'origine è anche globalmente AS. In presenza di equilibri non isolati non si può avere attrazione di un singolo equilibrio da un intero intorno, perché un altro equilibrio vicino non converge a quello scelto.

> [!warning] Correzione della nota di riepilogo
> A p. 214 compare «nei sistemi lineari c'è SOLO l'origine ... quando la matrice A è singolare». Le condizioni sono invertite: se $A$ è **non singolare**, $Ax=0$ ha solo l'origine; se è singolare, $\ker A$ contiene infiniti equilibri. Inoltre questi ultimi non sono necessariamente tutti instabili: $A=0$ rende ogni equilibrio stabile, pur senza AS.

Per un sistema meccanico, l'energia totale suggerisce una funzione scalare che diminuisce lungo le traiettorie. Per massa-molla-smorzatore, con posizione $q$, velocità $v$ e forza elastica $kq+k_3q^3$:
$$V=\frac12mv^2+\frac12kq^2+\frac14k_3q^4,\qquad \dot V=-bv^2.$$
La dissipazione non positiva suggerisce stabilità; il fatto che $\dot V$ possa annullarsi per $v=0$ anche con $q\ne0$ richiede un passaggio ulteriore per la convergenza.

_(Dispensa commentata, pagine PDF 213–220; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 213
> ![[CA-p213-1.jpg]]
> Nel caso lineare la stabilità dei diversi equilibri è collegata dalla linearità; un equilibrio AS deve essere isolato.

> [!example]- Materiale originale — pagina PDF 214
> ![[CA-p214-1.jpg]]
> Il riepilogo manoscritto sugli equilibri contiene le condizioni da precisare: matrice non singolare significa unico equilibrio, matrice singolare significa nucleo non banale.

> [!example]- Materiale originale — pagina PDF 215
> ![[CA-p215-1.jpg]]
> Il criterio spettrale per i sistemi lineari distingue autovalori strettamente a sinistra e quelli marginali con struttura semisemplice.

> [!example]- Materiale originale — pagina PDF 216
> ![[CA-p216-1.jpg]]
> Il metodo diretto è motivato dall'energia di un sistema meccanico: non serve risolvere le traiettorie per studiarne la dissipazione.

> [!example]- Materiale originale — pagina PDF 217
> ![[CA-p217-1.jpg]]
> Il modello massa-molla-smorzatore con richiamo non lineare fornisce un esempio di energia cinetica e potenziale.

> [!example]- Materiale originale — pagina PDF 218
> ![[CA-p218-1.jpg]]
> La candidata energetica viene costruita integrando la forza elastica e sommando l'energia cinetica.

> [!example]- Materiale originale — pagina PDF 219
> ![[CA-p219-1.jpg]]
> La derivata dell'energia lungo il moto si collega all'attrito: il segno non positivo suggerisce stabilità ma non basta da solo per AS.

> [!example]- Materiale originale — pagina PDF 220
> ![[CA-p220-1.jpg]]
> Il calcolo manoscritto verifica la cancellazione dei termini conservativi e isola la dissipazione dello smorzatore.

## Definitezza e derivata lungo le traiettorie

Vedi [[CA - Funzione definita positiva]] · [[CA - Derivata di Lyapunov]] · [[CA - Forme quadratiche positive]].

Traslato l'equilibrio nell'origine, una funzione $V$ è definita positiva (DP) in un intorno se $V(0)=0$ e $V(x)>0$ per $x\ne0$. È semidefinita positiva se può annullarsi anche altrove; negativa definita o semidefinita se $-V$ è rispettivamente positiva definita o semidefinita. Una funzione indefinita assume entrambi i segni arbitrariamente vicino all'origine.

Per $\dot x=f(x)$ e $V\in C^1$:
$$\dot V(x)=\nabla V(x)^Tf(x).$$
Non si deriva $V$ rispetto al tempo tenendo $x$ costante: si applica la regola della catena. Con $V=x^TPx$, $P=P^T$, vale $\dot V=f^TPx+x^TPf$; nel caso lineare è $x^T(A^TP+PA)x$.

Una forma quadratica è DP se $P\succ0$. Per matrici simmetriche il criterio di Sylvester richiede tutti i minori principali **di testa** positivi. Per la semidefinitezza, il controllo dei soli minori di testa non basta. Collegamenti: [[GEO - Diagonalizzazione ortogonale]] e [[GEO - Autovalori autovettori e autospazi]].

_(Dispensa commentata, pagine PDF 221–224; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 221
> ![[CA-p221-1.jpg]]
> Le definizioni di funzioni positive e negative distinguono segno stretto, segno semidefinito e funzioni indefinite.

> [!example]- Materiale originale — pagina PDF 222
> ![[CA-p222-1.jpg]]
> Le curve di livello rappresentano geometricamente una funzione DP e aiutano a costruire regioni invarianti attorno all'equilibrio.

> [!example]- Materiale originale — pagina PDF 223
> ![[CA-p223-1.jpg]]
> Gli esempi confrontano funzioni con zeri isolati e funzioni che si annullano su insiemi più grandi; questa distinzione conta nel teorema diretto.

> [!example]- Materiale originale — pagina PDF 224
> ![[CA-p224-1.jpg]]
> La regola della catena produce la derivata di V lungo la dinamica, da distinguere dalla sola derivata parziale rispetto al tempo.

## Teoremi di stabilità e stabilità asintotica

Vedi [[CA - Criterio diretto di Lyapunov]] · [[CA - Stima del bacino di attrazione]].

Se esiste $V\in C^1$ definita positiva in un intorno dell'origine con $\dot V\le0$, l'origine è stabile. Se inoltre $\dot V<0$ per ogni $x\ne0$ nello stesso intorno, l'origine è AS. Sono condizioni sufficienti per una data candidata: non trovare una funzione adatta non dimostra l'instabilità.

Le curve di livello forniscono regioni positivamente invarianti: si sceglie un sottolivello compatto $\Omega_c=\{x:V(x)\le c\}$ interamente contenuto nella regione in cui valgono le disuguaglianze. Se $\dot V<0$ fuori dall'origine, tale regione dà una stima per difetto del dominio di attrazione.

Per il pendolo smorzato, l'energia $V=\omega^2/2+(1-\cos\theta)$ ha derivata $-b\omega^2\le0$ ma non strettamente negativa: il primo teorema prova stabilità; per AS servirà l'insieme invariante. Si può anche cercare una candidata con termini misti per ottenere una derivata definita negativa localmente.

_(Dispensa commentata, pagine PDF 225–234; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 225
> ![[CA-p225-1.jpg]]
> Il primo teorema usa V positiva e derivata non positiva per impedire l'uscita da un intorno dell'equilibrio.

> [!example]- Materiale originale — pagina PDF 226
> ![[CA-p226-1.jpg]]
> La dimostrazione geometrica costruisce un livello chiuso dentro l'intorno assegnato e sfrutta la monotonia di V lungo ogni traiettoria.

> [!example]- Materiale originale — pagina PDF 227
> ![[CA-p227-1.jpg]]
> La discussione ricorda che una candidata non riuscita non prova instabilità: può essere necessario sceglierne un'altra.

> [!example]- Materiale originale — pagina PDF 228
> ![[CA-p228-1.jpg]]
> L'energia del pendolo ha derivata semidefinita negativa: certifica stabilità ma richiede un argomento ulteriore per la convergenza.

> [!example]- Materiale originale — pagina PDF 229
> ![[CA-p229-1.jpg]]
> Il teorema AS richiede una derivata strettamente negativa fuori dall'equilibrio e fornisce una stima locale del bacino.

> [!example]- Materiale originale — pagina PDF 230
> ![[CA-p230-1.jpg]]
> Il disegno delle curve di livello chiarisce come scegliere sottolivelli interamente contenuti nella regione di validità del segno.

> [!example]- Materiale originale — pagina PDF 231
> ![[CA-p231-1.jpg]]
> L'esempio applica una candidata quadratica e delimita una regione in cui la derivata ha segno negativo.

> [!example]- Materiale originale — pagina PDF 232
> ![[CA-p232-1.jpg]]
> I calcoli e il piano delle fasi confrontano la regione certificata con il comportamento delle traiettorie.

> [!example]- Materiale originale — pagina PDF 233
> ![[CA-p233-1.jpg]]
> Una nuova candidata per il pendolo aggiunge termini utili a ottenere negatività stretta localmente e una stima esplicita del dominio.

> [!example]- Materiale originale — pagina PDF 234
> ![[CA-p234-1.jpg]]
> Il foglio illustrato confronta curve di livello e ritratti di fase: la stima ottenuta non coincide necessariamente con l'intero bacino.

## Instabilità e conclusioni globali

Vedi [[CA - Criterio di instabilità]] · [[CA - Funzione radialmente illimitata]].

Un criterio di instabilità richiede una funzione che cresca lungo le traiettorie in una regione appropriata vicina all'equilibrio. La semplice positività di $\dot V$ in un punto non è sufficiente: si devono verificare le ipotesi della regione e la crescita che forza l'uscita da un intorno.

Per ottenere GAS dal metodo diretto, una condizione sufficiente è: $V$ DP su tutto $\mathbb R^n$, $\dot V$ definita negativa su tutto $\mathbb R^n\setminus\{0\}$ e $V$ radialmente illimitata, cioè $V(x)\to\infty$ per $\|x\|\to\infty$. Questa proprietà rende compatti i sottolivelli e impedisce fughe all'infinito a energia limitata.

> [!example] Conclusione globale
> Per $\dot x=-x-x^3$, $V=x^2/2$ è DP e radialmente illimitata; $\dot V=-x^2-x^4<0$ per $x\ne0$. L'origine è GAS. Il termine cubico aiuta la dissipazione e non va cancellato senza motivo.

_(Dispensa commentata, pagine PDF 235–240; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 235
> ![[CA-p235-1.jpg]]
> Il criterio di instabilità usa una funzione crescente in una regione opportuna: non basta invertire senza ipotesi il criterio di stabilità.

> [!example]- Materiale originale — pagina PDF 236
> ![[CA-p236-1.jpg]]
> L'esempio di instabilità richiama le condizioni della regione in cui la funzione e la sua derivata hanno il segno richiesto.

> [!example]- Materiale originale — pagina PDF 237
> ![[CA-p237-1.jpg]]
> La versione globale del criterio aggiunge la limitatezza radiale di V, per rendere compatti i sottolivelli.

> [!example]- Materiale originale — pagina PDF 238
> ![[CA-p238-1.jpg]]
> Il confronto geometrico mostra che una funzione non radiale può lasciare aperte fughe all'infinito pur mantenendo un valore limitato.

> [!example]- Materiale originale — pagina PDF 239
> ![[CA-p239-1.jpg]]
> L'esempio scalare evidenzia come il segno del campo e una candidata radiale permettano una conclusione globale.

> [!example]- Materiale originale — pagina PDF 240
> ![[CA-p240-1.jpg]]
> La tabella riassume stabilità, AS, GAS e instabilità distinguendo segno di V, segno della derivata e ipotesi globali.

## Costruzione di candidate quadratiche

Vedi [[CA - Scelta della candidata]] · [[CA - Criterio di Sylvester]].

La scelta sistematica $V=x^TPx$ introduce coefficienti da determinare. Prima si impone $P\succ0$, poi si calcola $\dot V$ e si scelgono i coefficienti per annullare termini misti o dominare quelli di segno incerto. La positività di $V$ e la negatività della derivata sono verifiche distinte.

> [!example] Cancellare un termine misto
> Per $\dot x_1=-x_1+2x_2$, $\dot x_2=-2x_1-x_2-x_2^3$, scegliere $V=(x_1^2+x_2^2)/2$. Si ottiene $\dot V=-x_1^2-x_2^2-x_2^4$: i termini misti si cancellano e l'origine è GAS.

Per una matrice $2\times2$ simmetrica $P$, $P\succ0$ equivale a $p_{11}>0$ e $p_{11}p_{22}-p_{12}^2>0$. Controllare soltanto i coefficienti diagonali sarebbe insufficiente. Le pagine della dispensa mostrano come adattare i pesi per ottenere una derivata con segno certificabile.

_(Dispensa commentata, pagine PDF 241–244; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 241
> ![[CA-p241-1.jpg]]
> La costruzione di candidate quadratiche usa una matrice simmetrica positiva e il criterio di Sylvester.

> [!example]- Materiale originale — pagina PDF 242
> ![[CA-p242-1.jpg]]
> L'esempio sceglie pesi per controllare i termini misti e ottenere un segno certo della derivata.

> [!example]- Materiale originale — pagina PDF 243
> ![[CA-p243-1.jpg]]
> Il calcolo parametrico impone prima la positività della matrice e poi le condizioni sui coefficienti della derivata.

> [!example]- Materiale originale — pagina PDF 244
> ![[CA-p244-1.jpg]]
> La scelta finale dei parametri verifica la candidata e distingue il risultato locale dalle condizioni che valgono in tutto lo spazio.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]] · [[E09 - CA - Prova finale 2019-2020]] · [[E11 - CA - Prova finale 2021-2022]] · [[E12 - CA - Prova finale 2022-2023]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]]
