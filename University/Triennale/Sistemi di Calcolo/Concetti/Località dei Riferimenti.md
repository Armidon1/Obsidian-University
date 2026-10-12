---
title: Località dei Riferimenti
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - cache
  - prestazioni
---

# Località dei Riferimenti

> [!summary] In breve
> Temporale: un indirizzo usato ora sarà riusato presto. Spaziale: verranno usati anche gli indirizzi vicini. Le cache funzionano grazie alla località, e il programmatore deve scrivere codice che ne abbia.

```c
for (i…) for (j…) s += m[i][j];   // per righe: 1 miss ogni 16 int (linea da 64 B)
for (i…) for (j…) s += m[j][i];   // per colonne: 1 miss per accesso
```

- Nell'esperimento della dispensa la versione per righe è circa **5×** più veloce.
- In C le matrici sono **row-major**: il ciclo interno deve scorrere l'ultimo indice.
- La stessa idea sta dietro il working set della memoria virtuale.

## Collegamenti

- **Concetti correlati**: [[Memoria Cache]] · [[Gerarchia di Memoria]] · [[Thrashing e Working Set]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SDC - Gestione dei dati in memoria centrale#Località spaziale e temporale|Lezione 7 — Località spaziale e temporale]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Somma di una matrice|Lezione 7 — Somma di una matrice]]
