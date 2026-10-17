---
title: "Progetto mediante luogo delle radici"
aliases:
  - "CA — Progetto mediante luogo delle radici"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "106-112"
class_label: "30/03"
---

# Progetto mediante luogo delle radici

> [!abstract]
> Questa lezione sviluppa progetto mediante luogo delle radici seguendo il blocco delle pagine 106–112 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 30/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[12 - CA - Dal modello di stato alla sintesi in frequenza]]. **Dopo:** [[14 - CA - Punti multipli e costruzione del luogo delle radici]].

## Prestazioni come regioni del piano complesso

Vedi [[CA - Luogo delle radici]] · [[CA - Regioni ammissibili dei poli]].

Il progetto nel piano $s$ impone direttamente dove devono trovarsi i poli chiusi. Un vincolo sul tempo di assestamento diventa approssimativamente un limite sulla parte reale; un vincolo sullo smorzamento delimita un settore attorno al semiasse reale negativo. Queste traduzioni sono affidabili quando i poli dominanti descrivono bene il transitorio.

Con $F(s)=kN(s)/D(s)$, il polinomio chiuso è $D(s)+kN(s)$. Il luogo delle radici (LdR) è l'insieme delle sue radici al variare di $k$. Per $k=0$ i rami partono dai poli di $F_0=N/D$; per $|k|\to\infty$ arrivano agli zeri finiti o all'infinito. Non confondere i poli del processo con quelli dell'intero anello dopo l'inserimento del controllore.

Il luogo mostra come un parametro sposta contemporaneamente tutti i poli: non consente di scegliere ogni radice in modo indipendente. Se nessun tratto entra nella regione ammissibile, occorre cambiare la struttura del controllore aggiungendo poli o zeri.

_(Dispensa commentata, pagine PDF 106–108; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 106
> ![[CA-p106-1.jpg]]
> Il progetto nel piano complesso traduce le specifiche di transitorio in regioni in cui collocare i poli chiusi.

> [!example]- Materiale originale — pagina PDF 107
> ![[CA-p107-1.jpg]]
> Le regioni ammissibili delimitano rapidità e smorzamento: il luogo deve attraversarle prima di scegliere un guadagno.

> [!example]- Materiale originale — pagina PDF 108
> ![[CA-p108-1.jpg]]
> I primi esempi mostrano i poli chiusi al variare del guadagno e introducono la condizione 1 più F uguale a zero.

## Condizioni di fase e modulo

Vedi [[CA - Condizione di fase del luogo]] · [[CA - Condizione di modulo del luogo]].

Da $1+kF_0(s)=0$ segue $kF_0(s)=-1$. Per $k>0$:
$$\arg F_0(s)=(2\ell+1)\pi,\qquad k=\frac1{|F_0(s)|}.$$
Per $k<0$ la fase di $F_0$ è $2\ell\pi$ e $|k|=1/|F_0|$. La condizione di fase stabilisce se un punto appartiene al luogo, quella di modulo dà il guadagno corrispondente.

Se $F_0$ è un rapporto di prodotti, la fase è la somma degli angoli dei vettori dagli zeri al punto meno la somma degli angoli dai poli al punto. Sul reale, il luogo per $k>0$ occupa gli intervalli con un numero dispari di poli e zeri reali alla destra del punto; per $k<0$ il numero è pari. Le molteplicità vanno contate.

> [!example] Due poli e nessuno zero
> Per $F_0=1/[s(s+2)]$, $\chi=s^2+2s+k$. I poli sono $-1\pm\sqrt{1-k}$: per $0<k<1$ stanno sul segmento $(-2,0)$, si incontrano in $-1$ a $k=1$ e poi si muovono sulla verticale $\Re s=-1$. Il sistema è AS per ogni $k>0$, ma lo smorzamento diminuisce all'aumentare di $k$.

_(Dispensa commentata, pagine PDF 109–110; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 109
> ![[CA-p109-1.jpg]]
> Le condizioni di fase e modulo stabiliscono appartenenza al luogo e valore del parametro; la verifica del segno di k è indispensabile.

> [!example]- Materiale originale — pagina PDF 110
> ![[CA-p110-1.jpg]]
> Gli asintoti descrivono i rami che vanno all'infinito e dipendono dal grado relativo dell'anello completo.

## Asintoti e frontiere di stabilità

Vedi [[CA - Asintoti del luogo]].

Se $n=\deg D>m=\deg N$, ci sono $n-m$ rami all'infinito. Per polinomi monici e guadagno positivo, gli asintoti hanno angoli $\theta_\ell=(2\ell+1)\pi/(n-m)$ e centro
$$\sigma_a=\frac{\sum p_i-\sum z_i}{n-m}.$$
Per il luogo negativo gli angoli diventano $2\ell\pi/(n-m)$. La somma include molteplicità e poli/zeri complessi. Il grado relativo determina quanti rami arrivano all'infinito, non il grado del solo processo.

Gli attraversamenti dell'asse immaginario si ricavano da $D(j\omega)+kN(j\omega)=0$ separando parte reale e immaginaria, oppure con Routh. Così si distingue il disegno qualitativo dagli intervalli esatti di stabilità.

_(Dispensa commentata, pagine PDF 111–112; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 111
> ![[CA-p111-1.jpg]]
> L'esempio a tre rami confronta il luogo con gli attraversamenti dell'asse immaginario ricavati algebricamente.

> [!example]- Materiale originale — pagina PDF 112
> ![[CA-p112-1.jpg]]
> La tabella di Routh identifica gli intervalli AS del luogo: i disegni delle radici aiutano a leggere i modi dominanti.
