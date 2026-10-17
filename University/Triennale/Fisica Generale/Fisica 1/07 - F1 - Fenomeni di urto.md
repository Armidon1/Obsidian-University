---
title: "Fenomeni di urto"
aliases:
  - "F1 — Fenomeni di urto"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "194-211"
---

# Fenomeni di urto

> [!abstract]
> Gli urti avvengono in tempi brevi e con forze intense. I bilanci di impulso permettono di confrontare gli stati prima e dopo senza ricostruire la deformazione durante il contatto.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Approssimazione impulsiva e sistema isolato

Vedi [[F1 - Approssimazione impulsiva e sistema isolato]].

Durante un urto $\Delta\mathbf P=\mathbf J_{\mathrm{ext}}$. Si trascura l'impulso esterno solo quando è piccolo rispetto agli impulsi di contatto. Il peso può essere trascurabile su un intervallo molto breve, mentre la reazione di un perno può avere un impulso importante. Quantità di moto ed energia non sono automaticamente entrambe conservate: sono due bilanci con ipotesi diverse.

_(Libro, cap. 7; pagine stampate 185–202; PDF pp. 194–211.)_

## Urto elastico unidimensionale

Vedi [[F1 - Urto elastico unidimensionale]].

Si conservano quantità di moto ed energia cinetica. Le velocità finali sono
$$v_1'=\frac{m_1-m_2}{m_1+m_2}v_1+\frac{2m_2}{m_1+m_2}v_2,$$
$$v_2'=\frac{2m_1}{m_1+m_2}v_1+\frac{m_2-m_1}{m_1+m_2}v_2.$$
Equivalentemente la velocità relativa cambia segno. Per masse uguali le velocità si scambiano. In più dimensioni servono anche le informazioni geometriche sull'urto; due sole leggi scalari non determinano tutti i componenti.

_(Libro, cap. 7; pagine stampate 185–202; PDF pp. 194–211.)_

## Urto completamente anelastico

Vedi [[F1 - Urto completamente anelastico]].

Se i corpi rimangono uniti, la conservazione della quantità di moto fornisce
$$\mathbf v_f=\frac{m_1\mathbf v_1+m_2\mathbf v_2}{m_1+m_2}.$$
Con massa ridotta $\mu=m_1m_2/(m_1+m_2)$ la perdita di energia cinetica è $\tfrac12\mu|\mathbf v_1-\mathbf v_2|^2$. L'energia non scompare: viene convertita in deformazione, calore e altre forme interne. È la massima perdita compatibile con conservazione della quantità di moto e assenza di rilascio di energia interna.

![[F1-p200-1.png]]

*Figura 7.11: prima dell’urto una massa è in moto e l’altra è ferma; dopo si muovono insieme alla velocità del centro di massa. Il disegno distingue la conservazione della quantità di moto dalla perdita di energia cinetica.* _(Libro, p. 191; PDF p. 200.)_

_(Libro, cap. 7; pagine stampate 185–202; PDF pp. 194–211.)_

## Restituzione e urti con corpi rigidi

Vedi [[F1 - Restituzione e urti con corpi rigidi]].

Lungo la normale di contatto si può introdurre $e=-v_{\mathrm{rel},n}'/v_{\mathrm{rel},n}$: $e=1$ per urto elastico e $e=0$ se non c'è separazione lungo la normale. Per un urto con un corpo vincolato a un asse, la quantità di moto lineare del sottosistema può non conservarsi a causa del perno. Si conserva invece la componente del momento angolare rispetto all'asse se il momento impulsivo esterno su quell'asse è nullo. Dopo l'urto si può applicare un distinto bilancio energetico al moto successivo.

_(Libro, cap. 7; pagine stampate 185–202; PDF pp. 194–211.)_

## Derivazione guidata

Nel riferimento del centro di massa le velocità iniziali di due corpi sono $v_{1G}=m_2(v_1-v_2)/(m_1+m_2)$ e $v_{2G}=-m_1(v_1-v_2)/(m_1+m_2)$. La loro energia cinetica totale è $K_G=\mu(v_1-v_2)^2/2$. Dopo un urto completamente anelastico i corpi sono fermi in questo riferimento: viene trasformata in energia interna tutta e sola $K_G$. Nel laboratorio resta il contributo di traslazione del centro di massa.

_(Libro, cap. 7; pagine stampate 185–202; PDF pp. 194–211.)_

## Esempio svolto

> [!example] Applicazione originale
> Una massa di $2\,\mathrm{kg}$ a $3\,\mathrm{m/s}$ urta e rimane unita a una massa ferma di $1\,\mathrm{kg}$. Si ha $v_f=2\,\mathrm{m/s}$, $K_i=9\,\mathrm J$, $K_f=6\,\mathrm J$. I $3\,\mathrm J$ di differenza sono energia trasferita ai gradi di libertà interni.

## Richiami matematici

[[GEO - Somma e differenza di vettori]].

## Verifica attiva

In un urto completamente anelastico si annulla tutta l’energia cinetica?

> [!check]- Risposta ragionata
> Solo quella relativa al centro di massa. Nel laboratorio resta l’energia di traslazione del centro di massa, se la quantità di moto iniziale non è nulla.

## Navigazione

Precedente: [[06 - F1 - Dinamica del corpo rigido]] · Successivo: [[08 - F1 - Gravitazione]].
