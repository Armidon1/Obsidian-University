---
title: Riduzione polinomiale
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
  - riduzioni
---

# Riduzione polinomiale

> [!summary] In breve
> $L_1 \le_p L_2$ se esiste $f$ calcolabile in tempo polinomiale con $x \in L_1 \iff f(x) \in L_2$. Allora $L_2$ è almeno tanto difficile quanto $L_1$.

| se… | allora… |
|---|---|
| $A$ NP-completo e $A \le_p B$ | $B$ NP-hard |
| $B \in \mathrm{P}$ e $A \le_p B$ | $A \in \mathrm{P}$ |
| $A \in \mathrm{P}$ | nulla su $B$ |

- **Transitiva**: la composizione di polinomi è un polinomio.
- Va verificata in entrambi i versi: soluzione di $A$ ⇒ soluzione di $f(x)$, e soluzione di $f(x)$ ⇒ soluzione di $A$.
- Catena del corso: SAT → 3SAT → {programmazione intera, 3-colorazione, independent set} → vertex cover, cricca.

## Collegamenti

- **Concetti correlati**: [[Riduzione tra linguaggi]] · [[NP-completezza]] · [[Problemi NP-hard]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#Riduzione fra linguaggi|Lezione 14 — Riduzione fra linguaggi]]
> - [[14 - MC - Classi P e NP e NP-completezza#Riduzioni NP: sommario|Lezione 14 — Riduzioni NP: sommario]]
> - [[14 - MC - Classi P e NP e NP-completezza#Robustezza della definizione|Lezione 14 — Robustezza della definizione]]
