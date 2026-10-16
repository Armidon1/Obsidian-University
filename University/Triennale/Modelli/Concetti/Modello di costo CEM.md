---
title: Modello di costo CEM
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - analisi-algoritmi
---

# Modello di costo CEM

> [!summary] In breve
> La CEM (*C Elementary Machine*) è una macchina astratta che esegue direttamente codice C: ogni istruzione elementare costa 1, i cicli costano test più corpo. Serve a esprimere il costo di un algoritmo come funzione della dimensione dell'input, indipendente da hardware, linguaggio e compilatore.

- **istruzione semplice** (assegnazione, espressione senza chiamate): costo 1;
- **if**: test + ramo eseguito; **while** con $p$ iterazioni: $(p+1)$ test + $p$ corpi;
- **chiamata di funzione**: costo del corpo della funzione (+1).

Perché funziona: due istruzioni semplici diverse costano $t_1$ e $t_2$ con $c \cdot t_1 \ge t_2$ per una costante $c$. I costi uniformi introducono errori **costanti**, non differenze **asintotiche**.

> [!warning] Limite del modello
> Interi di grandezza arbitraria a costo 1 portano a risultati assurdi (un intero può codificare un programma intero). Il modello realistico è la RAM a **costi logaritmici**.

Esempio: `ricercaSequenziale` costa $1 + (2n+1) + 2 = 2n + 4$.

## Collegamenti

- **Concetti correlati**: [[Dimensione dell'input]] · [[Analisi del caso peggiore]] · [[Istruzione dominante]] · [[Notazione O grande]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[01 - MC - Costo degli algoritmi e modello CEM#Calcolo del costo di esecuzione di un programma|Lezione 1 — Calcolo del costo di esecuzione di un programma]]
> - [[01 - MC - Costo degli algoritmi e modello CEM#Perché i costi uniformi non sono "grossolani"|Lezione 1 — Perché i costi uniformi non sono "grossolani"]]
> - [[08 - MC - Macchine di Turing e calcolabilità#Modelli di costo per le RAM|Lezione 8 — Modelli di costo per le RAM]]
