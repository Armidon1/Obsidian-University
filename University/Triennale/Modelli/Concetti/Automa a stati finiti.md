---
title: Automa a stati finiti
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - automi
  - linguaggi-regolari
---

# Automa a stati finiti

> [!summary] In breve
> $A = \langle \Sigma, Q, F, q_0, \delta \rangle$ con $\delta: \Sigma \times Q \to Q$: legge la stringa una volta, cambiando stato a ogni simbolo, e accetta se finisce in uno stato finale. Riconosce esattamente i linguaggi regolari.

- $L(A) = \{x \mid \bar\delta(x, q_0) \in F\}$; configurazioni $(q, x)$ e transizioni $(q, aw) \vdash (q', w)$.
- Tempo lineare, memoria finita: non può "contare" ($a^n b^n$ non è regolare).
- ASF = GR3: arco $A \xrightarrow{c} B$ ↔ produzione $A \to cB$ (e $A \to c$ se $B$ è finale).
- Chiusura: unione, concatenazione, stella, complemento (su ASFD completo, invertendo i finali), intersezione.
- Decidibili: vuoto, finito/infinito, equivalenza.

> [!example] Parità
> Stati PP, PD, DP, DD (parità di 0 e di 1); con $F = \{PP\}$ accetta le stringhe con un numero pari di 0 e di 1.

## Collegamenti

- **Concetti correlati**: [[Automa a stati finiti non deterministico]] · [[Espressione regolare]] · [[Pumping lemma per linguaggi regolari]] · [[Gerarchia di Chomsky]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Automa a stati finiti|Lezione 10 — Automa a stati finiti]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Linguaggi regolari e grammatiche di tipo 3|Lezione 10 — Linguaggi regolari e grammatiche di tipo 3]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Proprietà di chiusura dei linguaggi regolari|Lezione 10 — Proprietà di chiusura dei linguaggi regolari]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Problemi di decidibilità sui linguaggi regolari|Lezione 10 — Problemi di decidibilità sui linguaggi regolari]]
