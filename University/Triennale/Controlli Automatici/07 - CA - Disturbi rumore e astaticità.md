---
title: "Disturbi rumore e astaticità"
aliases:
  - "CA — Disturbi rumore e astaticità"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "55-60"
class_label: "17/03"
---

# Disturbi rumore e astaticità

> [!abstract]
> Questa lezione sviluppa disturbi rumore e astaticità seguendo il blocco delle pagine 55–60 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 17/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[06 - CA - Specifiche statiche tipo del sistema ed errore a regime]]. **Dopo:** [[08 - CA - Specifiche dinamiche e simulazioni di controllo]].

## Specifiche per riferimenti sinusoidali

Vedi [[CA - Errore sinusoidale]].

Per $r(t)=a\sin\omega t$, l'ampiezza dell'errore di regime è $a|S(j\omega)|$. Richiedere errore relativo non superiore a $\varepsilon$ su una banda equivale a $|S(j\omega)|\le\varepsilon$ in tutta la banda. Con $|F|\gg1$, si usa l'approssimazione $|S|\simeq1/|F|$: un errore del 10% suggerisce almeno 20 dB di anello, ma la verifica esatta è su $1/(1+F)$.

Non esiste in generale una disuguaglianza esatta $|F|\ge1/\varepsilon$ equivalente alla specifica: conta anche la fase, perché nel denominatore compare la somma complessa $1+F$. L'approssimazione è utile lontano dal punto critico.

_(Dispensa commentata, pagine PDF 55–56; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 55
> ![[CA-p055-1.jpg]]
> La specifica sinusoidale introduce un limite all'ampiezza dell'errore in una banda di frequenze, anziché un solo valore statico.

> [!example]- Materiale originale — pagina PDF 56
> ![[CA-p056-1.jpg]]
> Il diagramma mostra la stima ad alto guadagno del vincolo sinusoidale: l'ineguaglianza esatta contiene la somma complessa 1 più F.

## Disturbi costanti e posizione degli integratori

Vedi [[CA - Astaticità]] · [[CA - Disturbo in ingresso]] · [[CA - Disturbo in uscita]].

Un sistema è astatico rispetto a una classe di disturbi se il loro effetto sull'uscita si annulla a regime. Per un disturbo costante all'uscita $Y_d=S d_0/s$: serve $S(0)=0$. Per un disturbo costante in ingresso al processo $Y_d=PS d_0/s$: serve invece $(PS)(0)=0$.

Se $|GP|\to\infty$ a bassa frequenza, $PS\simeq1/G$. Un integratore nel **processo** può annullare l'errore di riferimento ma non basta per rigettare un disturbo che entra prima del processo. L'integratore deve essere nel tratto opportuno del controllore, a monte del punto d'iniezione lungo la catena diretta.

> [!example] Stesso anello, due disturbi diversi
> Con $P=1/[s(s+1)]$ e $G=k>0$, $S=s(s+1)/[s(s+1)+k]$ e $PS=1/[s(s+1)+k]$. Il disturbo costante all'uscita è rigettato; quello in ingresso lascia offset $d_0/k$.

_(Dispensa commentata, pagine PDF 57–59; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 57
> ![[CA-p057-1.jpg]]
> Il confronto degli integratori evidenzia che il rigetto dei disturbi dipende da dove entrano rispetto alla catena diretta.

> [!example]- Materiale originale — pagina PDF 58
> ![[CA-p058-1.jpg]]
> I primi schemi di disturbo distinguono perturbazioni all'uscita e all'ingresso del processo: i trasferimenti chiusi non sono uguali.

> [!example]- Materiale originale — pagina PDF 59
> ![[CA-p059-1.jpg]]
> I limiti a bassa frequenza del canale del disturbo identificano quando compare un offset e quando il sistema è astatico.

## Rumore di misura e compromesso con il riferimento

Vedi [[CA - Rumore di misura]].

Il rumore additivo di misura entra con trasferimento $-T$. A bassa frequenza un buon inseguimento richiede $T\simeq1$, quindi un errore di misura costante viene trasferito quasi interamente all'uscita con segno opposto. Il controllore porta la **misura** al riferimento, e non può distinguere un errore del sensore da una variazione vera dell'uscita senza informazioni aggiuntive.

Ad alta frequenza il progetto impone invece $|T|\ll1$ per non inseguire il rumore. L'identità $S+T=1$ impedisce di renderle entrambe piccole alla stessa frequenza. Questo motiva la separazione fra banda utile di regolazione e banda del rumore.

_(Dispensa commentata, pagine PDF 60–60; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 60
> ![[CA-p060-1.jpg]]
> Il foglio riepiloga ingressi di disturbo e misura: un bias del sensore viene interpretato dal controllore come un errore reale.

## Esercizi collegati

[[E02 - CA - Prova intermedia 2019-2020]] · [[E04 - CA - Prova intermedia 2021-2022]] · [[E06 - CA - Prova intermedia 2023-2024]]
