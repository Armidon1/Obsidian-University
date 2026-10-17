---
title: "Inseguimento di riferimenti e modello interno"
aliases:
  - "CA — Inseguimento di riferimenti e modello interno"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "187-193"
class_label: "04/05"
---

# Inseguimento di riferimenti e modello interno

> [!abstract]
> Questa lezione sviluppa inseguimento di riferimenti e modello interno seguendo il blocco delle pagine 187–193 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 04/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]]. **Dopo:** [[25 - CA - Equilibri e stabilità dei sistemi non lineari]].

## Dalla stabilizzazione all’inseguimento

Vedi [[CA - Prefiltro statico]] · [[CA - Inseguimento nello stato]].

La retroazione dello stato stabilizza i modi, ma non impone automaticamente guadagno statico unitario dal riferimento all'uscita. Se $A+BK$ è Hurwitz e $D=0$, con $u=Kx+Nr$ il guadagno statico è $-C(A+BK)^{-1}BN$. Si sceglie $N$ per renderlo uguale a uno, se il fattore è invertibile e non nullo.

Il prefiltro usa il modello nominale: può ottenere errore nullo per un riferimento costante senza aggiungere integratori, ma non rigetta in modo robusto disturbi costanti o incertezze del processo. Non confondere una taratura statica nominale con il principio del modello interno.

La scelta dei poli regola il transitorio del sistema stabilizzato; $N$ regola il guadagno del canale del riferimento. Il comando e l'eventuale osservatore devono essere alimentati con lo stesso ingresso effettivo.

_(Dispensa commentata, pagine PDF 187–188; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 187
> ![[CA-p187-1.jpg]]
> Il problema di inseguimento distingue la scelta dei poli dalla taratura del guadagno statico del riferimento.

> [!example]- Materiale originale — pagina PDF 188
> ![[CA-p188-1.jpg]]
> La scelta dei poli e del prefiltro costruisce una risposta nominale desiderata, senza garantire automaticamente rigetto robusto di un disturbo ignoto.

## Aggiungere l’integrale dell’errore

Vedi [[CA - Modello interno]] · [[CA - Stato integrale]] · [[CA - Regolazione robusta]].

Per riferimenti e disturbi costanti si introduce $\dot z=r-y$ e si usa $u=K_xx+K_iz$. Con $D=0$ il modello aumentato, prima del feedback, è
$$\binom{\dot x}{\dot z}=\begin{pmatrix}A&0\\-C&0\end{pmatrix}\binom xz+\binom B0u+\binom01r.$$
Se il sistema aumentato è stabilizzabile, si assegna il guadagno $[K_x\ K_i]$. A equilibrio $\dot z=0$ impone $y=r$. L'azione integrale realizza un modello del generatore dei segnali costanti, che ha autovalore zero.

Per un SISO, una condizione cruciale per poter controllare il nuovo modo in origine è
$$\operatorname{rank}\begin{pmatrix}A&B\\C&0\end{pmatrix}=n+1.$$
Uno zero di trasmissione nell'origine può ostacolare l'integrazione necessaria. La stabilizzabilità del processo originale non basta da sola.

> [!example] Regolazione integrale verificata
> $\dot x=-x+u$, $y=x$, $\dot z=r-x$, $u=-2x+2z$. La matrice chiusa è $\begin{pmatrix}-3&2\\-1&0\end{pmatrix}$ e il polinomio è $s^2+3s+2$, con poli $-1,-2$. Un disturbo costante additivo all'ingresso cambia $z$ a regime, mentre $x=r$ resta imposto dalla sua equazione.

_(Dispensa commentata, pagine PDF 189–191; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 189
> ![[CA-p189-1.jpg]]
> L'inserimento dell'integratore dell'errore realizza il modello interno dei segnali costanti e aumenta l'ordine del problema.

> [!example]- Materiale originale — pagina PDF 190
> ![[CA-p190-1.jpg]]
> I diversi schemi di regolazione confrontano prefiltro e integrazione, mostrando dove il riferimento entra nella dinamica aumentata.

> [!example]- Materiale originale — pagina PDF 191
> ![[CA-p191-1.jpg]]
> La matrice aumentata permette di controllare la raggiungibilità del nuovo modo in origine e la possibilità di assegnarne i poli.

## Verificare il problema aumentato

Vedi [[CA - Raggiungibilità aumentata]] · [[CA - Ordine della regolazione]].

Negli esempi si controlla il rango della matrice aumentata e si assegna un polinomio di grado $n+1$. Un osservatore dello stato originale, quando necessario, deve tenere conto di tutto l'ingresso noto, inclusa l'azione integrale; l'integratore $z$ è già disponibile al controllore e non richiede di essere stimato come una misura ignota.

Per rampe o sinusoidi servono modelli interni diversi: più integratori per polinomi, una coppia oscillante per una frequenza sinusoidale nota. Queste sono conseguenze del principio generale; nel materiale della lezione il progetto svolto riguarda soprattutto i segnali costanti.

_(Dispensa commentata, pagine PDF 192–193; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 192
> ![[CA-p192-1.jpg]]
> L'esercizio calcola il rango del sistema aumentato e verifica la compatibilità della regolazione con il processo.

> [!example]- Materiale originale — pagina PDF 193
> ![[CA-p193-1.jpg]]
> La scelta del guadagno integrale conclude l'assegnazione del polinomio di grado superiore.

## Esercizi collegati

[[E07 - CA - Prova intermedia 2024-2025]]
