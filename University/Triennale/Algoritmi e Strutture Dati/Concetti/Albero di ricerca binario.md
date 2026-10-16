---
title: Albero di ricerca binario
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - bst
---

# Albero di ricerca binario

> [!summary] In breve
> BST: albero binario in cui ogni nodo ha chiave maggiore di quelle del sottoalbero sinistro e minore di quelle del destro; ricerca, inserimento e rimozione costano $O(h)$, ma $h$ può arrivare a $n$.

- **Ricerca**: confronta e scendi a sinistra o a destra; termina in una foglia se la chiave manca.
- **Inserimento**: dove la ricerca fallisce.
- **Rimozione**: con al più un figlio interno, il figlio sale al posto del nodo; con due, si copia il **predecessore** (massimo del sottoalbero sinistro) e si rimuove quello.
- L'attraversamento **in ordine simmetrico** dà le chiavi ordinate.
- Altezza: $O(\log n)$ attesa con inserimenti casuali, ma $n$ con chiavi già ordinate → servono alberi **bilanciati**.

## Collegamenti

- **Concetti correlati**: [[Rotazione e ristrutturazione di una terna]] · [[Albero AVL]] · [[Albero rosso-nero]] · [[Mappa ordinata]] · [[Attraversamenti di un albero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Alberi di ricerca binari|Lezione 11 — Alberi di ricerca binari]]
