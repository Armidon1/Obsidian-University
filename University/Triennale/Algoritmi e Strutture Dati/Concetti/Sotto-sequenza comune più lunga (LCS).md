---
title: Sotto-sequenza comune più lunga (LCS)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - programmazione-dinamica
---

# Sotto-sequenza comune più lunga (LCS)

> [!summary] In breve
> Date due stringhe $X$ e $Y$, trovare la più lunga stringa che sia sotto-sequenza (caratteri nello stesso ordine, non contigui) di entrambe; con la programmazione dinamica costa $O(nm)$.

$L_{j,k}$ = lunghezza LCS di $X[0..j-1]$ e $Y[0..k-1]$:
$$L_{j,k} = \begin{cases} 0 & j = 0 \text{ o } k = 0 \\ 1 + L_{j-1,k-1} & x_{j-1} = y_{k-1} \\ \max(L_{j-1,k},\ L_{j,k-1}) & \text{altrimenti} \end{cases}$$

- Tabella $(n+1) \times (m+1)$ riempita riga per riga: $O(nm)$ (forza bruta $O(2^n m)$).
- La sotto-sequenza si **ricostruisce** a ritroso da $L_{n,m}$: passo diagonale se i caratteri coincidono, altrimenti verso il valore maggiore; $O(n + m)$.
- Applicazioni: confronto di DNA, `diff` tra file.

## Collegamenti

- **Concetti correlati**: [[Programmazione dinamica]] · [[Pattern matching su stringhe]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#DNA e allineamento di sequenze di caratteri|Lezione 13 — DNA e allineamento di sequenze di caratteri]]
