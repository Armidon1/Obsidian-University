---
title: "Amplificatori"
aliases:
  - "EL — Amplificatori"
tags:
  - elettronica
  - lezione
source: "pdf/Appunti di Elettronica.pdf"
---

# Amplificatori

> [!abstract]
> Guadagno, impedenze e banda descrivono che cosa un amplificatore riesce a trasferire dalla sorgente al carico.
> Percorso completo: [[MOC - Elettronica]]. Fonte: dispensa di Valerio Spagnoli, pagine PDF 27–36.

Precedente: [[03 - EL - Reti a due porte]] · Successiva: [[05 - EL - Reti STC e risposta nel tempo]]

## Guadagno, alimentazione e rendimento

Per il ripasso: [[EL - Guadagni e decibel]] · [[EL - Rendimento di un amplificatore]].

Un amplificatore ideale riproduce la forma d’onda d’ingresso con una diversa ampiezza. Un dispositivo reale può approssimare questo comportamento soltanto entro limiti di ampiezza e frequenza. Il guadagno di tensione è $A_v=v_o/v_i$, quello di corrente $A_i=i_o/i_i$. Per potenze correttamente definite $A_p=P_o/P_i$; nel caso resistivo con riferimenti coerenti $A_p=A_vA_i$.

I guadagni logaritmici sono $20\log_{10}|A_v|$, $20\log_{10}|A_i|$ e $10\log_{10}A_p$. Per esempio $|A_v|=10$ equivale a 20 dB. Un guadagno negativo inverte la polarità; il modulo in dB non conserva questo segno. Per collegare dB di tensione e rapporto di potenza bisogna considerare anche le impedenze.

Il guadagno di potenza proviene dall’alimentazione, non dalla creazione di energia:
$$P_{DC}+P_i=P_o+P_{diss},\qquad \eta=\frac{P_o}{P_{DC}}.$$
L’approssimazione $P_i\ll P_{DC}$ permette di trascurare la potenza del segnale d’ingresso. Un trasformatore passivo può aumentare la tensione riducendo la corrente, ma non fornire guadagno di potenza.

_(dispensa, pp. 27–28)_

![[EL-p027-1.png]]

Il simbolo generale distingue una porta d’ingresso e una d’uscita. _(dispensa, p. 27)_

![[EL-p027-2.png]]

Nel simbolo con riferimento comune entrambe le tensioni sono misurate rispetto a massa. _(dispensa, p. 27)_

![[EL-p027-3.png]]

Le frecce definiscono i riferimenti delle correnti e la polarità della tensione sul carico. _(dispensa, p. 27)_

![[EL-p027-4.png]]

La pendenza della transcaratteristica lineare rappresenta il guadagno di tensione. _(dispensa, p. 27)_

![[EL-p028-1.png]]

Le due sorgenti di alimentazione forniscono la potenza che l’amplificatore trasferisce al carico. _(dispensa, p. 28)_

## Saturazione e polarizzazione

Per il ripasso: [[EL - Polarizzazione e punto di lavoro]] · [[EL - Clipping e dinamica]].

La transcaratteristica lega ingresso e uscita. Nel tratto lineare ideale $v_o=A_vv_i$, mentre fuori dai limiti l’uscita si avvicina a $L^+$ o $L^-$. Per $A_v>0$ l’intervallo lineare d’ingresso è $L^-/A_v<v_i<L^+/A_v$. I limiti reali d’uscita dipendono anche dalla distanza dalle alimentazioni e dal carico.

Il **clipping** è il taglio dei picchi quando si richiede un’uscita oltre i limiti. Diminuire il guadagno amplia l’intervallo ammissibile d’ingresso; aumentare l’ampiezza d’ingresso non risolve la saturazione.

La polarizzazione imposta un punto di riposo $Q=(V_I,V_O)$. Si scrive $v_I(t)=V_I+v_i(t)$ e, localmente, $v_O(t)\simeq V_O+A_vv_i(t)$, con $A_v=dv_O/dv_I|_Q$. Il segnale deve restare sufficientemente piccolo perché la tangente rappresenti bene la curva e non raggiunga i limiti. La polarizzazione non rende amplificabile un segnale di ampiezza arbitraria.

_(dispensa, pp. 29–30)_

![[EL-p029-1.png]]

L’uscita segue il tratto lineare finché i picchi raggiungono i limiti: oltre quei punti compare clipping. _(dispensa, p. 29)_

![[EL-p029-2.png]]

Su una caratteristica curva, la pendenza e quindi il guadagno locale cambiano con il punto di lavoro. _(dispensa, p. 29)_

![[EL-p030-1.png]]

La sorgente continua somma una polarizzazione al segnale variabile. _(dispensa, p. 30)_

![[EL-p030-2.png]]

Il punto Q colloca il segnale nel tratto utile della transcaratteristica; le escursioni devono restare limitate. _(dispensa, p. 30)_

## Impedenze e quattro tipi di amplificatore

Per il ripasso: [[EL - Quattro tipi di amplificatore]] · [[EL - Caricamento degli amplificatori]].

Per un amplificatore di tensione unilaterale con guadagno a vuoto $A_{v0}$:
$$\frac{v_o}{v_s}=\frac{R_i}{R_s+R_i}\,A_{v0}\,\frac{R_L}{R_o+R_L}.$$
Il primo fattore esprime la perdita all’ingresso; l’ultimo la perdita sul carico. Si vuole $R_i\gg R_s$ e $R_o\ll R_L$. Non è il criterio di massimo trasferimento di potenza: qui si vuole preservare la tensione.

Per l’amplificatore di corrente, la frazione acquisita è $R_s/(R_s+R_i)$ e quella erogata al carico è $R_o/(R_o+R_L)$: si vogliono ingresso a bassa resistenza e uscita ad alta resistenza.

| Tipo | Trasferimento | Unità | $R_i$ ideale | $R_o$ ideale |
|---|---|---|---|---|
| Tensione | $v_o=A_vv_i$ | V/V | $\infty$ | 0 |
| Corrente | $i_o=A_ii_i$ | A/A | 0 | $\infty$ |
| Transconduttanza | $i_o=G_mv_i$ | A/V = S | $\infty$ | $\infty$ |
| Transresistenza | $v_o=R_mi_i$ | V/A = $\Omega$ | 0 | 0 |

Questi quattro modelli corrispondono alle quattro combinazioni delle grandezze d’ingresso e d’uscita. La resistenza d’ingresso appartiene all’intero circuito visto dalla sorgente; non coincide necessariamente con quella del singolo transistor o operazionale.

_(dispensa, pp. 31–33)_

![[EL-p031-1.png]]

Il modello di tensione mostra i due partitori: sorgente-ingresso e uscita-carico. _(dispensa, p. 31)_

![[EL-p032-1.png]]

Il modello di corrente richiede impedenza d’ingresso bassa e d’uscita alta per ridurre le correnti perse. _(dispensa, p. 32)_

## Stadi in cascata

Per il ripasso: [[EL - Amplificatori in cascata]].

Una cascata ripartisce i compiti: il primo stadio acquisisce bene il segnale, quelli centrali forniscono guadagno, l’ultimo pilota il carico. Il guadagno complessivo è il prodotto dei guadagni **effettivamente caricati**:
$$A_{tot}=A_1A_2A_3.$$
Se si usano invece i guadagni a vuoto, occorre aggiungere i partitori tra l’uscita di uno stadio e l’ingresso del successivo. In dB i guadagni si sommano. Un buffer può avere guadagno circa unitario ed essere comunque indispensabile per isolare le impedenze.

_(dispensa, p. 34)_

![[EL-p034-1.png]]

La cascata assegna funzioni differenti ai tre stadi e mostra i caricamenti intermedi. _(dispensa, p. 34)_

![[EL-p034-2.png]]

Il modello complessivo riassume impedenza d’ingresso, guadagno e impedenza d’uscita dell’intera cascata. _(dispensa, p. 34)_

## Banda passante e accoppiamento

Per il ripasso: [[EL - Banda passante di un amplificatore]].

Un amplificatore può avere una regione di guadagno quasi costante tra $f_L$ e $f_H$. Capacità di accoppiamento bloccano la continua e introducono limiti alle basse frequenze; capacità parassite e interne limitano le alte frequenze.

Un condensatore tra due stadi evita che la polarizzazione del primo alteri quella del secondo. Per passare il segnale con poca attenuazione deve avere impedenza piccola rispetto alle resistenze viste nella banda utile. Le reti STC permetteranno di quantificare questa condizione.

> [!warning] Correzione
> A p. 36 si propone $\omega_L=\omega_H$ come filtro che lascia passare una sola frequenza. Due tagli coincidenti non realizzano una selezione infinitamente stretta: la risposta dipende dalla funzione di trasferimento completa e resta distribuita in frequenza. Anche l’affermazione di una banda alta generalmente nell’ordine dei THz non è una proprietà generale degli amplificatori.

_(dispensa, pp. 35–36)_

![[EL-p035-1.png]]

La banda passante è delimitata dalle frequenze alle quali il guadagno inizia a scendere significativamente. _(dispensa, p. 35)_

![[EL-p035-2.png]]

L’interconnessione su livelli diversi richiama l’origine geometrica delle capacità parassite. _(dispensa, p. 35)_

![[EL-p036-1.png]]

I condensatori fra stadi interrompono la continua e lasciano indipendenti i punti di polarizzazione. _(dispensa, p. 36)_

![[EL-p036-2.png]]

La risposta selettiva ha un picco e una larghezza finita: non equivale al passaggio di una sola frequenza esatta. _(dispensa, p. 36)_

