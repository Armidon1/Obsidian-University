---
title: TDS - Criterio di Jury
tags:
  - teoria-dei-sistemi
  - concetto
  - stabilita
  - tempo-discreto
---

# TDS - Criterio di Jury

> [!summary] In breve
> L\'analogo discreto di Routh: dice se tutte le radici hanno modulo minore di 1, con tre condizioni necessarie e una tabella di determinanti.

- Necessarie (con $a_n>0$): $p(1)>0$, $(-1)^np(-1)>0$, $|a_0|<a_n$.
- Tabella: righe e righe invertite; $b_i=\begin{vmatrix}a_0&a_{n-i}\\a_n&a_i\end{vmatrix}$; si arriva a righe di 3 elementi.
- Condizioni: $|b_{n-1}|<|b_0|$, $|c_{n-2}|<|c_0|$, …
- Alternativa: trasformazione bilineare $\lambda=\frac{1+s}{1-s}$ e Routh.

## Collegamenti

- **Concetti correlati**: [[TDS - Criterio di Routh]] · [[TDS - Sistemi a tempo discreto]] · [[TDS - Stabilità]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[14 - TDS - Stabilità nel tempo discreto ed esempi#Condizioni necessarie per la stabilità nel tempo discreto|Lezione 14 — Condizioni necessarie per la stabilità nel tempo discreto]]
> - [[14 - TDS - Stabilità nel tempo discreto ed esempi#Criterio di Jury|Lezione 14 — Criterio di Jury]]
> - [[14 - TDS - Stabilità nel tempo discreto ed esempi#Passaggio da un criterio all'altro|Lezione 14 — Passaggio da un criterio all'altro]]
