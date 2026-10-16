---
title: "Dipendenza e indipendenza lineare"
aliases:
  - "GEO — Dipendenza e indipendenza lineare"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "16"
pdf_pages: "241–250"
---

# Dipendenza e indipendenza lineare

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 16 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 16.1 - Dipendenza e indipendenza lineare

Vedi [[GEO - Dipendenza e indipendenza lineare]].

Una famiglia $v_1,\ldots,v_r$ è dipendente se esistono $a_i$ **non tutti nulli** con $\sum_i a_iv_i=0$. Non si richiede che ogni coefficiente sia non nullo.

Se $a_j\ne0$, si può isolare

$$v_j=-\sum_{i\ne j}\frac{a_i}{a_j}v_i.$$

Quindi almeno un vettore è combinazione degli altri e si può eliminare senza cambiare lo span. Viceversa, se un vettore è combinazione degli altri, portando tutto a primo membro si ottiene una relazione non banale.

> [!example] Non ogni vettore è eliminabile
> Per $v_1=(1,0)$, $v_2=(2,0)$, $v_3=(0,1)$ la famiglia è dipendente perché $2v_1-v_2=0$. Si può eliminare $v_1$ oppure $v_2$, ma non $v_3$: gli altri due non generano la seconda direzione.

Inserendo le coordinate dei vettori come colonne in $A$, le relazioni di dipendenza sono le soluzioni di $Aa=0$. La famiglia di $r$ vettori è indipendente se e solo se $\operatorname{rk}A=r$.

Una famiglia contenente $0$ è dipendente; una famiglia con più di $n$ vettori in uno spazio di dimensione $n$ lo è necessariamente. L’indipendenza a coppie non basta per l’intera famiglia: $(1,0)$, $(0,1)$, $(1,1)$ non sono a due a due proporzionali, ma sono dipendenti.

_(Accascina–Monti, § 16.1, libro pp. 225–230; PDF pp. 241–246.)_

## Ripasso attivo

- **Dipendenza e indipendenza lineare:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Dipendenza e indipendenza lineare]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 232 (PDF p. 248). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[15 - GEO - Generatori]] · Successiva: [[17 - GEO - Basi di spazi vettoriali]]

[[MOC - Geometria]]
