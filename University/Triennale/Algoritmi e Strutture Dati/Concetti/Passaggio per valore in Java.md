---
title: Passaggio per valore in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - metodi
---

# Passaggio per valore in Java

> [!summary] In breve
> Java passa **sempre** i parametri per valore: per i tipi riferimento viene copiato il riferimento, quindi il metodo può modificare l'oggetto ma non far puntare altrove la variabile del chiamante.

- Primitivi: il metodo riceve una copia del valore; modificarla non cambia il chiamante.
- Riferimenti: il metodo riceve una copia del riferimento →
  - `param.campo = …` **modifica** l'oggetto condiviso;
  - `param = new …` cambia solo la copia locale.

```java
static void reset(Counter c) { c.count = 0; }   // effetto visibile al chiamante
static void swap(Counter a, Counter b) { Counter t = a; a = b; b = t; }  // nessun effetto
```

## Collegamenti

- **Concetti correlati**: [[Variabile riferimento]] · [[Pila dei metodi di Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Parametri: passaggio per valore|Lezione 1 — Parametri: passaggio per valore]]
