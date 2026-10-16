---
title: Teorema di Lagrange
tags:
  - analisi-1
  - concetto
  - derivate
---

# Teorema di Lagrange

> [!summary] In breve
> Se f ∈ C[a, b] è derivabile in (a, b), esiste c con f'(c) = (f(b) − f(a))/(b − a): una tangente parallela alla secante. Collega i valori di f alla sua derivata.

$$f(x_2) = f(x_1) + f'(c)(x_2 - x_1), \qquad c \text{ tra } x_1 \text{ e } x_2$$

Conseguenze:
- **test di monotonia**: $f' \ge 0 \iff f$ crescente; $f' > 0 \Rightarrow$ strettamente crescente;
- **funzioni costanti**: $f' = 0$ su un **intervallo** $\iff$ $f$ costante;
- **criterio per estremi**: $f'$ cambia segno da $+$ a $-$ $\Rightarrow$ massimo;
- **lipschitzianità**: $|f'| \le L \Rightarrow |f(x_2) - f(x_1)| \le L|x_2 - x_1|$;
- è il resto di Taylor di ordine 0.

## Collegamenti

- **Concetti correlati**: [[Teorema di Rolle]] · [[Formula di Taylor]] · [[Studio di funzione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Teorema di Lagrange|Lezione 5 — Teorema di Lagrange]]
> - [[05 - AN1 - Calcolo Differenziale#Conseguenze del Teorema di Lagrange|Lezione 5 — Conseguenze del Teorema di Lagrange]]
> - [[05 - AN1 - Calcolo Differenziale#Test di monotonia|Lezione 5 — Test di monotonia]]
