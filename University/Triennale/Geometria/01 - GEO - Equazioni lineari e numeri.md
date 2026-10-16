---
title: "Equazioni lineari e numeri"
aliases:
  - "GEO — Equazioni lineari e numeri"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "1"
pdf_pages: "17–40"
---

# Equazioni lineari e numeri

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 1 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 1.1 - Una equazione in una incognita

Vedi [[GEO - Equazione lineare in una incognita]].

Un’equazione lineare in una incognita ha forma $ax=b$, con $a,b\in\mathbb R$. Risolverla significa trovare **tutti** i numeri che rendono vera l’uguaglianza. La distinzione iniziale è se il coefficiente dell’incognita è nullo: dividere per $a$ prima di controllarlo può eliminare casi interi.

| Condizione | Soluzioni |
|---|---|
| $a\ne0$ | Unica: $x=b/a$ |
| $a=0$, $b\ne0$ | Nessuna |
| $a=b=0$ | Ogni $x\in\mathbb R$ |

Per esempio $3x=2$ dà $x=2/3$, $0x=2$ è impossibile e $0x=0$ è un’identità. Questi tre casi anticipano la classificazione dei sistemi lineari.

_(Accascina–Monti, § 1.1, libro pp. 1–3; PDF pp. 17–19.)_

## 1.2 - Due equazioni in due incognite

Vedi [[GEO - Sistemi in due incognite]].

Una soluzione di un sistema in $x,y$ è una **coppia ordinata** che soddisfa contemporaneamente tutte le equazioni. Soddisfarne una sola non basta.

> [!example] Eliminare un’incognita
> Nel sistema $x+2y=4$, $x+5y=6$, sottraiamo la prima equazione dalla seconda: $3y=2$. Quindi $y=2/3$ e $x=4-4/3=8/3$. Il controllo nelle equazioni iniziali dà rispettivamente $4$ e $6$.

Due equazioni proporzionali possono descrivere lo stesso vincolo; se invece hanno primi membri proporzionali e termini noti incompatibili, non esiste soluzione. Il numero di equazioni, da solo, non determina il numero di soluzioni.

_(Accascina–Monti, § 1.2, libro pp. 3–6; PDF pp. 19–22.)_

## 1.3 - Molte equazioni in molte incognite

Vedi [[GEO - Sistemi lineari generali]].

Per $p$ equazioni in $q$ incognite si scrive

$$\sum_{j=1}^{q}a_{ij}x_j=b_i,\qquad i=1,\ldots,p.$$

Una soluzione è una $q$-upla $(x_1,\ldots,x_q)\in\mathbb R^q$. I coefficienti formano una tabella $A=(a_{ij})$ con $p$ righe e $q$ colonne. Le equazioni sono lineari perché le incognite compaiono solo al primo grado, senza prodotti tra loro: $xy=1$ e $x^2+y=0$ non sono equazioni lineari.

L’obiettivo sarà distinguere esistenza, unicità e parametrizzazione delle soluzioni attraverso proprietà della matrice $A$.

_(Accascina–Monti, § 1.3, libro pp. 6–7; PDF pp. 22–23.)_

## 1.4 - Sistemi equivalenti

Vedi [[GEO - Equivalenza dei sistemi]].

Nel libro due sistemi nelle stesse incognite sono detti **equivalenti** se si passa dall’uno all’altro con un numero finito di operazioni consentite: scambio di equazioni, moltiplicazione per uno scalare non nullo, somma di un multiplo di un’altra equazione, aggiunta o eliminazione di identità.

Queste operazioni conservano le soluzioni perché sono reversibili. Per esempio $E_2\leftarrow E_2-3E_1$ si annulla con $E_2\leftarrow E_2+3E_1$.

> [!important] Ipotesi essenziale
> Moltiplicare un’equazione per zero non è un’operazione equivalente: $x=1$ diventerebbe $0=0$, perdendo il vincolo su $x$.

L’equivalenza è riflessiva, simmetrica e transitiva. È la giustificazione teorica del successivo metodo di Gauss.

_(Accascina–Monti, § 1.4, libro pp. 7–10; PDF pp. 23–26.)_

## 1.5 - Numeri e insiemi

Vedi [[GEO - Insiemi numerici]].

Gli insiemi numerici soddisfano $\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R$. Il libro adotta $\mathbb N=\{1,2,3,\ldots\}$: altre convenzioni includono lo zero. I razionali hanno forma $m/n$ con $n\ne0$; i reali comprendono anche gli irrazionali.

La notazione $a\in A$ indica appartenenza, $A\subseteq B$ inclusione e $A\setminus B$ differenza. La cancellazione $ac=bc\Rightarrow a=b$ richiede $c\ne0$; quella additiva $a+c=b+c\Rightarrow a=b$ vale sempre.

Nei calcoli del corso conviene conservare frazioni e radicali esatti. Un’approssimazione prematura può nascondere un coefficiente nullo e alterare la classificazione di un sistema.

_(Accascina–Monti, § 1.5, libro pp. 10–14; PDF pp. 26–30.)_

## Ripasso attivo

- **Una equazione in una incognita:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equazione lineare in una incognita]].
- **Due equazioni in due incognite:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Sistemi in due incognite]].
- **Molte equazioni in molte incognite:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Sistemi lineari generali]].
- **Sistemi equivalenti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equivalenza dei sistemi]].
- **Numeri e insiemi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Insiemi numerici]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 21 (PDF p. 37). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Successiva: [[02 - GEO - Matrici e insiemi]]

[[MOC - Geometria]]
