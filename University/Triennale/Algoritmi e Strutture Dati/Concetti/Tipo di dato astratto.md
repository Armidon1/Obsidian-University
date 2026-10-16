---
title: Tipo di dato astratto
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - oop
  - progettazione
---

# Tipo di dato astratto

> [!summary] In breve
> Un ADT descrive **cosa** fa una struttura dati (tipo dei dati, operazioni e loro effetti, errori) senza dire **come** è implementata; in Java si esprime con un'interfaccia.

- Separa **specifica** (interfaccia pubblica) e **implementazione** (classe concreta).
- Permette di cambiare implementazione senza toccare il codice cliente (incapsulamento, modularità).
- Esempi del libro: [[Pila (ADT)]], [[Coda (ADT)]], [[Lista posizionale]], [[Coda prioritaria (ADT)]], [[Mappa (ADT)]], [[Grafo (ADT)]].

| ADT | Implementazioni |
|---|---|
| pila | array, lista concatenata |
| mappa | tabella hash, skip list, alberi di ricerca |

## Collegamenti

- **Concetti correlati**: [[Interfacce e classi astratte]] · [[Modificatori di accesso in Java]] · [[Schema adattatore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Astrazione|Lezione 2 — Astrazione]]
