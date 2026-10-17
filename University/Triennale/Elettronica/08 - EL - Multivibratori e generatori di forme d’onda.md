---
title: "Multivibratori e generatori di forme d’onda"
aliases:
  - "EL — Multivibratori e generatori di forme d’onda"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Multivibratori e generatori di forme d’onda

> [!abstract]
> La retroazione positiva crea memoria e soglie; aggiungendo una dinamica RC si ottengono oscillazioni o impulsi temporizzati.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 85–94.

Precedente: [[07 - EL - Amplificatori operazionali]] · Successiva: [[09 - EL - Semiconduttori e diodi]]

## Bistabilità e trigger di Schmitt invertente

Per il ripasso: [[EL - Bistabilità e isteresi]] · [[EL - Trigger di Schmitt invertente]].

Un bistabile ha due stati stabili. Con un operazionale retroazionato positivamente, l’uscita si mantiene a $L^+$ o $L^-$. Il nodo + riceve $\beta v_o$, con $0<\beta<1$, mentre l’ingresso è sul nodo −. Il segno $v_+-v_-$ decide la commutazione.

Se l’uscita è alta, rimane alta finché $v_i<\beta L^+$; quando l’ingresso supera questa soglia passa bassa. Se l’uscita è bassa, torna alta quando $v_i<\beta L^-$. Le soglie sono:
$$V_{TH}=\beta L^+,\qquad V_{TL}=\beta L^-.$$
Nell’intervallo tra le soglie l’uscita dipende dalla storia: è l’**isteresi**. Non si applica il cortocircuito virtuale durante gli stati saturi. Lo stato intermedio simmetrico è instabile nel modello del bistabile, ma questo non implica che un qualunque operazionale senza retroazione sia un oscillatore.

_(dispensa, pp. 85–86)_

![[EL-p085-1.png]]

Il ritorno positivo rende possibili due stati saturi persistenti. _(dispensa, p. 85)_

![[EL-p085-2.png]]

L’analogia della palla sulla collina distingue equilibrio intermedio instabile e due stati stabili laterali. _(dispensa, p. 85)_

![[EL-p085-3.png]]

Il segnale sul morsetto − confronta il proprio valore con la soglia determinata dallo stato dell’uscita. _(dispensa, p. 85)_

![[EL-p086-1.png]]

Durante l’aumento dell’ingresso, il salto alto-basso avviene alla soglia beta per L positivo. _(dispensa, p. 86)_

![[EL-p086-2.png]]

Durante la diminuzione dell’ingresso, il salto basso-alto avviene alla soglia beta per L negativo. _(dispensa, p. 86)_

![[EL-p086-3.png]]

La caratteristica completa ha due soglie e dipende dal verso di percorrenza: è un’isteresi. _(dispensa, p. 86)_

## Schmitt non invertente e attraversamenti dello zero

Per il ripasso: [[EL - Trigger di Schmitt non invertente]].

Nel circuito del libro, il morsetto + somma ingresso e uscita:
$$v_+=v_i\frac{R_2}{R_1+R_2}+v_o\frac{R_1}{R_1+R_2},\qquad v_-=0.$$
La commutazione avviene quando questa somma cambia segno. Le soglie d’ingresso sono:
$$V_{TL}=-\frac{R_1}{R_2}L^+,\qquad V_{TH}=-\frac{R_1}{R_2}L^-.$$
Salendo oltre $V_{TH}$ l’uscita diventa alta; scendendo sotto $V_{TL}$ diventa bassa. Per alimentazioni simmetriche le soglie sono simmetriche rispetto a zero.

L’isteresi evita commutazioni multiple quando il rumore fa oscillare l’ingresso attorno a una soglia. Come rilevatore di attraversamenti dello zero, lo Schmitt introduce però uno scarto: commuta alle soglie, non esattamente a zero. Soglie piccole migliorano la precisione temporale ma riducono l’immunità al rumore.

> [!warning] Correzione
> A pp. 86 e 88 il ripristino dello stato associato alla soglia bassa è descritto come impulso «maggiore» della soglia. La condizione corretta è scendere **sotto $V_{TL}$**, seguendo il verso dell’isteresi.

_(dispensa, pp. 87–88)_

![[EL-p087-1.png]]

Nel non invertente ingresso e uscita contribuiscono al potenziale del morsetto +. _(dispensa, p. 87)_

![[EL-p087-2.png]]

Nel percorso crescente lo Schmitt non invertente commuta alla soglia alta. _(dispensa, p. 87)_

![[EL-p087-3.png]]

Nel percorso decrescente commuta alla soglia bassa. _(dispensa, p. 87)_

![[EL-p088-1.png]]

Il ciclo completo mostra che la stessa tensione intermedia può corrispondere a due diverse uscite. _(dispensa, p. 88)_

![[EL-p088-2.png]]

Senza isteresi il rumore causa più commutazioni; con isteresi piccole oscillazioni vicino allo zero non cambiano lo stato. _(dispensa, p. 88)_

## Astabile RC e onda quadra

Per il ripasso: [[EL - Multivibratore astabile]].

Nell’astabile non esiste uno stato stabile permanente: un condensatore costringe il circuito ad attraversare alternativamente le due soglie. Il nodo + è $\beta v_o$; il condensatore sul nodo − si carica attraverso R verso l’attuale tensione d’uscita.

Con uscita alta, $v_C$ tende a $L^+$ finché raggiunge $\beta L^+$; l’uscita commuta bassa. Ora $v_C$ tende a $L^-$ finché raggiunge $\beta L^-$. La tensione su C resta continua a ogni commutazione.

Per $L^+=-L^-=L$ e $\tau=RC$:
$$t_{1/2}=RC\ln\frac{1+\beta}{1-\beta},\qquad T=2RC\ln\frac{1+\beta}{1-\beta}.$$
Con $\beta=1/2$, $T=2RC\ln3\simeq2.197RC$. Il primo intervallo dopo l’avvio può essere diverso dai semiperiodi a regime, perché parte da una diversa tensione iniziale.

_(dispensa, pp. 89–90)_

![[EL-p089-1.png]]

Il ramo RC sull’ingresso − trasforma un bistabile in un astabile che commuta autonomamente. _(dispensa, p. 89)_

![[EL-p089-2.png]]

A uscita fissata, il condensatore si carica attraverso R verso quella tensione. _(dispensa, p. 89)_

![[EL-p089-3.png]]

Il condensatore segue tratti esponenziali tra le soglie; ogni loro attraversamento cambia il livello dell’onda quadra. _(dispensa, p. 89)_

## Generatore di onda triangolare

Per il ripasso: [[EL - Generatore di onda triangolare]].

Il condensatore di un astabile RC ha tratti esponenziali: non produce un triangolo esatto. Per ottenere rampe lineari si usa un integratore, pilotato dall’onda quadra di uno Schmitt non invertente.

Lo Schmitt fornisce alternativamente $L^+$ e $L^-$; l’integratore ha pendenza $dv_T/dt=-v_Q/(RC)$. La sua uscita torna allo Schmitt e ne attraversa le soglie, invertendo ogni volta il verso della rampa.

Con livelli $\pm L$ e soglie triangolari $\pm V_T$, la distanza per ogni rampa è $2V_T$ e il modulo della pendenza è $L/(RC)$:
$$T=4RC\frac{V_T}{L}.$$
Nel circuito del libro $V_T=(R_1/R_2)L$, quindi $T=4RC(R_1/R_2)$, usando i nomi delle resistenze del suo Schmitt. La temporizzazione dipende dalla pendenza e dalle soglie, non da un assestamento esponenziale.

_(dispensa, p. 91)_

![[EL-p091-1.png]]

Un ingresso costante nell’integratore produce una rampa di pendenza determinata da R e C. _(dispensa, p. 91)_

![[EL-p091-2.png]]

L’integratore e lo Schmitt non invertente si pilotano reciprocamente e producono triangolare e quadra. _(dispensa, p. 91)_

![[EL-p091-3.png]]

Le due forme d’onda evidenziano che i cambi di pendenza del triangolo coincidono con i salti della quadra. _(dispensa, p. 91)_

## Monostabile e durata dell’impulso

Per il ripasso: [[EL - Multivibratore monostabile]].

Un monostabile ha uno stato stabile e uno quasi stabile. Un trigger lo sposta temporaneamente nello stato quasi stabile; la carica del condensatore lo riporta allo stato iniziale.

Nel circuito del libro un diodo limita la tensione del condensatore a $V_\gamma$, impedendo l’attraversamento della soglia che causerebbe l’oscillazione continua. Un impulso negativo sul ramo di trigger forza l’uscita da $L^+$ a $L^-$. Il condensatore parte da $V_\gamma$ e tende verso $L^-$; il ritorno avviene a $\beta L^-$.
$$v_C(t)=L^-+(V_\gamma-L^-)e^{-t/(R_3C_1)}.$$
Ponendo $v_C(T)=\beta L^-$:
$$T=R_3C_1\ln\frac{V_\gamma-L^-}{\beta L^- -L^-}
\simeq R_3C_1\ln\frac1{1-\beta}$$
se $V_\gamma\ll |L^-|$. Il condensatore di ingresso crea un impulso dai fronti del comando; il secondo diodo seleziona la polarità utile. Il tempo di recupero deve essere sufficiente a ripristinare la condizione iniziale prima del trigger successivo.

> [!warning] Correzione
> A p. 92 il modello del diodo scrive $v_D=0$ nello stato spento. Nello stato spento è la **corrente** a essere nulla; la tensione può essere diversa da zero.

_(dispensa, pp. 92–94)_

![[EL-p092-1.png]]

Con il diodo di blocco il condensatore si arresta prima di raggiungere la soglia: l’uscita alta è stabile. _(dispensa, p. 92)_

![[EL-p092-2.png]]

Il diodo in parallelo a C limita la tensione e interrompe il meccanismo di oscillazione continua. _(dispensa, p. 92)_

![[EL-p093-1.png]]

Partendo dallo stato opposto, il condensatore attraversa una soglia e il circuito torna spontaneamente allo stato stabile. _(dispensa, p. 93)_

![[EL-p093-2.png]]

Il passa-alto trasforma un fronte negativo in un impulso breve adatto al trigger. _(dispensa, p. 93)_

![[EL-p093-3.png]]

Il circuito completo aggiunge selezione di polarità al trigger e limitazione della tensione del condensatore. _(dispensa, p. 93)_

![[EL-p094-1.png]]

La durata dell’uscita temporanea è il tempo necessario a C per passare dalla tensione di blocco alla soglia opposta. _(dispensa, p. 94)_

