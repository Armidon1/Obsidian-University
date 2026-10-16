---
title: Verifica di delimitatori con una pila
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - pile
  - applicazioni
---

# Verifica di delimitatori con una pila

> [!summary] In breve
> Per controllare che parentesi o tag HTML siano bilanciati si fa `push` di ogni apertura e, a ogni chiusura, `pop` verificando che corrisponda: corretto se alla fine la pila è vuota.

```text
per ogni carattere c:
  se c è un'apertura  → push(c)
  se c è una chiusura → se pila vuota o pop() non corrisponde a c: errore
alla fine: corretto se e solo se la pila è vuota
```

Tempo $O(n)$. Esempio: `[(5+x)-(y+z)]` corretto, `([)]` errato. Per l'HTML si confrontano i nomi di `<tag>` e `</tag>`.

## Collegamenti

- **Concetti correlati**: [[Pila (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Corrispondenza tra parentesi e tra marcatori HTML|Lezione 6 — Corrispondenza tra parentesi e tra marcatori HTML]]
