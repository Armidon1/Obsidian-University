---
title: TDS - Risposta impulsiva
tags:
  - teoria-dei-sistemi
  - concetto
  - rappresentazione-con-lo-stato
---

# TDS - Risposta impulsiva

> [!summary] In breve
> $W(t)=Ce^{At}B+D\delta(t)$: l\'uscita forzata è la convoluzione dell\'ingresso con $W$, una "media pesata" degli ingressi passati.

- $y_F(t)=\int_0^tW(t-\tau)u(\tau)\,d\tau$; il peso $W(t-\tau)$ dice quanto conta l'ingresso all'istante $\tau$.
- Colonne di $W$ = risposte forzate a impulsi su un singolo ingresso.
- Contiene solo i modi **eccitabili e osservabili**.
- $\mathcal L[W(t)]=W(s)$, la [[TDS - Funzione di trasferimento]].
- Discreto: $W(t)=CA^{t-1}B$ per $t\ge1$, $W(0)=D$.

## Collegamenti

- **Concetti correlati**: [[TDS - Funzione di trasferimento]] · [[TDS - Evoluzione libera e forzata]] · [[TDS - Eccitabilità e osservabilità dei modi]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[04 - TDS - Uscita forzata e dalla forma esplicita alla implicita#Uscita forzata|Lezione 4 — Uscita forzata]]
> - [[06 - TDS - Modi naturali#Modi naturali non eccitabili|Lezione 6 — Modi naturali non eccitabili]]
