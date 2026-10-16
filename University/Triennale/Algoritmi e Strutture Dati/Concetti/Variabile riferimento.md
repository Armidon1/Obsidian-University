---
title: Variabile riferimento
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - oggetti
---

# Variabile riferimento

> [!summary] In breve
> In Java una variabile di tipo classe non contiene l'oggetto ma un **riferimento** (indirizzo) a esso; `new` crea l'oggetto nello heap e restituisce il riferimento.

- Tipi **primitivi** (`int`, `double`, `boolean`, …): la variabile contiene il valore.
- Tipi **riferimento** (classi, array): la variabile contiene un riferimento, o `null`.
- Assegnare `b = a` copia il **riferimento**: `a` e `b` diventano **alias** dello stesso oggetto.
- Usare un riferimento `null` (`a.metodo()`) lancia `NullPointerException`.
- L'operatore `.` accede a campi e metodi dell'oggetto riferito.

```java
Counter c = new Counter();   // crea l'oggetto, c lo riferisce
Counter d = c;               // alias: stesso oggetto
d.increment();               // anche c "vede" l'incremento
```

## Collegamenti

- **Concetti correlati**: [[Costruttore in Java]] · [[Passaggio per valore in Java]] · [[Allocazione nella memoria heap]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Creare e usare oggetti|Lezione 1 — Creare e usare oggetti]]
