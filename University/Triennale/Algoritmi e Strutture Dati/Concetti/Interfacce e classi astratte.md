---
title: Interfacce e classi astratte
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - oop
  - java
---

# Interfacce e classi astratte

> [!summary] In breve
> Un'interfaccia dichiara solo firme di metodi (un contratto); una classe astratta può avere anche campi e metodi implementati ma non si può istanziare: entrambe servono a definire ADT e gerarchie.

| | Interfaccia | Classe astratta |
|---|---|---|
| istanziabile | no | no |
| metodi implementati | no (salvo `default`) | sì |
| campi d'istanza | no | sì |
| ereditarietà | una classe ne implementa **molte** | una classe ne estende **una** |

Uso tipico nel libro: interfaccia per l'ADT (`Queue<E>`), classe astratta con il codice comune (`AbstractTree<E>`), classe concreta (`LinkedBinaryTree<E>`).

## Collegamenti

- **Concetti correlati**: [[Tipo di dato astratto]] · [[Ereditarietà in Java]] · [[Schema template method]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Interfacce in Java|Lezione 2 — Interfacce in Java]]
