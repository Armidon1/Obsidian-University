---
title: "Sottospazi vettoriali"
aliases:
  - "GEO — Sottospazi vettoriali"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "14"
pdf_pages: "217–230"
---

# Sottospazi vettoriali

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 14 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 14.1 - Sottospazi vettoriali

Vedi [[GEO - Criterio di sottospazio vettoriale]].

Un sottoinsieme $E\subseteq V$ è un sottospazio vettoriale se è non vuoto ed è chiuso rispetto a somma e prodotto per scalare. Equivalentemente contiene $0$ e contiene $au+bv$ per ogni $u,v\in E$ e $a,b\in\mathbb R$.

Il primo controllo è la presenza dello zero: se manca, l’insieme non è un sottospazio. La presenza dello zero, però, non basta: anche la chiusura va verificata.

Per esempio $E=\{(x,y,z):x+y-z=0\}$ è un sottospazio. Se due vettori soddisfano l’equazione, anche ogni loro combinazione lineare la soddisfa. In generale

$$\operatorname{Sol}(Ax=0)\text{ è un sottospazio di }\mathbb R^q.$$

Il sistema omogeneo ha sempre la soluzione banale; ne ha altre se e solo se $\operatorname{rk}A<q$. Un sistema con $b\ne0$ non può avere $0$ come soluzione e quindi il suo insieme delle soluzioni non è un sottospazio.

_(Accascina–Monti, § 14.1, libro pp. 201–206; PDF pp. 217–222.)_

## 14.2 - Sottospazi di V 2 (O) e di V 3 (O)

Vedi [[GEO - Sottospazi geometrici]].

Nel piano i sottospazi sono $\{0\}$, le rette per l’origine e l’intero piano. Nello spazio si aggiungono i piani per l’origine.

Una retta traslata, per esempio $\{(x,y):y=1\}$, non è un sottospazio: non contiene $0$ e sommando due suoi punti si ottiene ordinata $2$. La sua direzione $\{(x,y):y=0\}$ è invece un sottospazio. Questa distinzione prepara il passaggio dalla geometria vettoriale a quella affine.

_(Accascina–Monti, § 14.2, libro pp. 206–207; PDF pp. 222–223.)_

## Ripasso attivo

- **Sottospazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Criterio di sottospazio vettoriale]].
- **Sottospazi di V 2 (O) e di V 3 (O):** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Sottospazi geometrici]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 208 (PDF p. 224). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[13 - GEO - Spazi vettoriali sui reali]] · Successiva: [[15 - GEO - Generatori]]

[[MOC - Geometria]]
