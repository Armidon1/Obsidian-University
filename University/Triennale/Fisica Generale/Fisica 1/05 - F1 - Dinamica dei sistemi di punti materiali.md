---
title: "Dinamica dei sistemi di punti materiali"
aliases:
  - "F1 — Dinamica dei sistemi di punti materiali"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "128-149"
---

# Dinamica dei sistemi di punti materiali

> [!abstract]
> Per molti punti materiali si separa il moto complessivo dai moti interni. Il centro di massa e i bilanci delle grandezze totali evitano di risolvere tutte le interazioni una per una.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Forze interne e centro di massa

Vedi [[F1 - Forze interne e centro di massa]].

Per masse costanti $M=\sum_im_i$ e
$$\mathbf R_G=\frac1M\sum_im_i\mathbf r_i,\qquad\mathbf P=M\mathbf V_G.$$
Sommando le equazioni di Newton, le forze interne si cancellano a coppie se rispettano azione e reazione, quindi $M\mathbf A_G=\mathbf F_{\mathrm{ext}}$. Il centro di massa può essere fuori dal materiale, come in un anello. La sua traiettoria descrive la traslazione globale ma non determina la configurazione dei singoli punti.

![[F1-p132-1.png]]

*Figura 5.10: per tre masse uguali ai vertici di un triangolo equilatero il centro di massa coincide con il baricentro. La media pesata delle coordinate individua un punto geometrico, che non deve contenere materia.* _(Libro, p. 123; PDF p. 132.)_

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Conservazione della quantità di moto totale

Vedi [[F1 - Conservazione della quantità di moto totale]].

Per un sistema chiuso $\Delta\mathbf P=\int\mathbf F_{\mathrm{ext}}dt$. Se la risultante esterna è nulla, il centro di massa si muove uniformemente anche se i componenti interagiscono intensamente. Può conservarsi una sola componente: basta che sia nullo l'impulso esterno lungo quella direzione. Prima di applicare una conservazione bisogna dichiarare quali corpi appartengono al sistema e su quale intervallo temporale si calcola l'impulso.

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Momento angolare di un sistema

Vedi [[F1 - Momento angolare di un sistema]].

Con forze interne centrali i momenti interni si cancellano. Per un polo fisso inerziale $\dot{\mathbf L}_O=\boldsymbol\tau_{O,\mathrm{ext}}$; l'analogo teorema vale rispetto al centro di massa anche quando questo accelera. Un momento esterno nullo conserva il momento angolare. La condizione è diversa da risultante esterna nulla: una coppia di forze ha risultante zero ma momento non nullo.

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Teoremi di König e moto interno

Vedi [[F1 - Teoremi di König e moto interno]].

Scrivendo $\mathbf v_i=\mathbf V_G+\mathbf v_i'$ e usando $\sum_im_i\mathbf v_i'=0$ si ottengono
$$K=\tfrac12MV_G^2+K_G,\qquad\mathbf L_O=\mathbf R_G\times M\mathbf V_G+\mathbf L_G.$$
Il primo termine è il contributo del moto del centro di massa; il secondo misura il moto rispetto a esso. Nel riferimento del centro di massa la quantità di moto totale è nulla, ma energia cinetica e momento angolare interno possono essere non nulli.

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Energia e sistemi di forze

Vedi [[F1 - Energia e sistemi di forze]].

Il teorema dell'energia cinetica del sistema comprende sia lavoro esterno sia lavoro interno: $\Delta K=W_{\mathrm{ext}}+W_{\mathrm{int}}$. Forze interne opposte non implicano lavori opposti, perché agiscono su spostamenti diversi. Se le interazioni interne sono conservative si introducono le loro energie potenziali. Per un corpo esteso la stessa risultante applicata in punti diversi può produrre evoluzioni rotazionali diverse: occorre conoscere anche il momento risultante.

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Derivazione guidata

Nell'identità $\mathbf v_i=\mathbf V_G+\mathbf v_i'$ espandi il quadrato e somma: $\sum_i m_iv_i^2=M V_G^2+2\mathbf V_G\cdot\sum_i m_i\mathbf v_i'+\sum_i m_iv_i'^2$. Il termine misto è nullo perché nel riferimento del centro di massa la quantità di moto totale è zero. Dividere per 2 dà il teorema di König dell'energia. La cancellazione riguarda il termine misto, non l'energia del moto interno.

_(Libro, cap. 5; pagine stampate 119–140; PDF pp. 128–149.)_

## Esempio svolto

> [!example] Applicazione originale
> Due pattinatori di $60$ e $40\,\mathrm{kg}$ partono fermi e si spingono su ghiaccio ideale. Dopo la spinta $60v_1+40v_2=0$. Se il primo ha $v_1=2{,}0\,\mathrm{m/s}$, il secondo ha $v_2=-3{,}0\,\mathrm{m/s}$. Il centro di massa resta fermo; l'energia cinetica finale, $300\,\mathrm J$, proviene dall'energia interna dei pattinatori.

## Richiami matematici

[[GEO - Somma e differenza di vettori]] · [[10 - AN1 - Integrali Multipli]].

## Verifica attiva

Le forze interne di un sistema si cancellano: si cancellano anche i loro lavori?

> [!check]- Risposta ragionata
> Non in generale: le forze opposte agiscono su punti che possono avere spostamenti differenti. Una molla interna può trasformare energia potenziale in energia cinetica relativa.

## Navigazione

Precedente: [[04 - F1 - Lavoro, energia e momento angolare]] · Successivo: [[06 - F1 - Dinamica del corpo rigido]].
