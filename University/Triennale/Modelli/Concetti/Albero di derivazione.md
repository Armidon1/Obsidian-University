---
title: Albero di derivazione
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - parsing
---

# Albero di derivazione

> [!summary] In breve
> Per una grammatica di tipo 2, l'albero che rappresenta una derivazione: radice = assioma, nodi interni = non terminali con figli la parte destra della produzione, foglie (da sinistra) = la stringa.

- Dimentica l'**ordine** delle derivazioni: derivazioni diverse con le stesse produzioni sugli stessi nodi danno lo stesso albero.
- A ogni albero corrispondono **una** derivazione sinistra e **una** destra.
- Un parser top-down costruisce l'albero in **pre-ordine** dalla radice; uno bottom-up in **post-ordine** dalle foglie.
- Due alberi diversi per la stessa stringa ⇒ [[Grammatica ambigua|grammatica ambigua]].

## Collegamenti

- **Concetti correlati**: [[Grammatica ambigua]] · [[Grammatica generativa]] · [[Parser a discesa ricorsiva]] · [[Parsing shift-reduce]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Alberi sintattici|Lezione 9 — Alberi sintattici]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Esempio di albero di derivazione|Lezione 11 — Esempio di albero di derivazione]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Bottom-up e top-down|Lezione 11 — Bottom-up e top-down]]
