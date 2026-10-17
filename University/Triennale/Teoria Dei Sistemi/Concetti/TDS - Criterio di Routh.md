---
title: TDS - Criterio di Routh
tags:
  - teoria-dei-sistemi
  - concetto
  - stabilita
  - criterio-di-routh
---

# TDS - Criterio di Routh

> [!summary] In breve
> Tabella costruita dai coefficienti del polinomio caratteristico: ogni variazione di segno nella prima colonna è una radice a parte reale positiva, ogni permanenza una negativa.

- Condizione necessaria: coefficienti tutti dello stesso segno (sufficiente solo per $n\le2$).
- $b_1=\dfrac{a_{n-1}a_{n-2}-a_na_{n-3}}{a_{n-1}}$; si può moltiplicare una **riga** per un fattore positivo.
- Primo elemento nullo: si trasla la riga cambiando segno e si somma.
- Riga tutta nulla (indice dispari): radici simmetriche rispetto all'origine; si sostituisce con la derivata del polinomio ausiliario.
- Utile con parametri (es. valore critico di un guadagno).

## Collegamenti

- **Concetti correlati**: [[TDS - Stabilità]] · [[TDS - Criterio di Jury]] · [[TDS - Criterio di Nyquist]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[11 - TDS - Punti di equilibrio e stabilità#Segno degli autovalori senza calcolarli|Lezione 11 — Segno degli autovalori senza calcolarli]]
> - [[12 - TDS - Criterio di Routh e linearizzazione#Criterio di Routh|Lezione 12 — Criterio di Routh]]
> - [[12 - TDS - Criterio di Routh e linearizzazione#Caso in cui un'intera riga è nulla|Lezione 12 — Caso in cui un'intera riga è nulla]]
> - [[36 - TDS - Nyquist con poli sull'asse immaginario#Verifica della stabilità con Routh|Lezione 36 — Verifica della stabilità con Routh]]
