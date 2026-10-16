---
title: Albero (2,4)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - bilanciamento
---

# Albero (2,4)

> [!summary] In breve
> Albero di ricerca a più vie in cui ogni nodo interno ha 2, 3 o 4 figli e tutte le foglie sono alla stessa profondità: altezza $\Theta(\log n)$, aggiornamenti con split (overflow) e trasferimenti/fusioni (underflow).

- Altezza: $\frac{1}{2}\log(n+1) \le h \le \log(n+1)$.
- **Inserimento**: nel nodo più in basso; se diventa un 5-nodo (*overflow*) lo si **divide**: la terza chiave sale nel genitore (può propagarsi fino a creare una nuova radice).
- **Rimozione**: ci si riporta a un nodo con soli figli esterni (scambio con il predecessore); se resta senza chiavi (*underflow*): **trasferimento** da un fratello 3- o 4-nodo, altrimenti **fusione** con un fratello (può propagarsi).
- Tutte le operazioni $O(\log n)$. Corrisponde agli [[Albero rosso-nero|alberi rosso-nero]].

## Collegamenti

- **Concetti correlati**: [[Albero di ricerca a più vie]] · [[Albero rosso-nero]] · [[Albero (a,b)]] · [[B-albero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Operazioni in un albero (2,4)|Lezione 11 — Operazioni in un albero (2,4)]]
