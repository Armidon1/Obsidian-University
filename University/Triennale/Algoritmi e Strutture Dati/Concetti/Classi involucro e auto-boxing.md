---
title: Classi involucro e auto-boxing
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - tipi
---

# Classi involucro e auto-boxing

> [!summary] In breve
> Ogni tipo primitivo ha una classe involucro (`Integer`, `Double`, …); Java converte automaticamente tra primitivo e oggetto (auto-boxing / unboxing), necessario ad esempio con i tipi generici.

| Primitivo | Involucro |
|---|---|
| `int` | `Integer` |
| `double` | `Double` |
| `char` | `Character` |
| `boolean` | `Boolean` |

```java
List<Integer> l = new ArrayList<>();
l.add(5);            // auto-boxing: Integer.valueOf(5)
int x = l.get(0);    // unboxing: intValue()
```

Attenzione: `==` tra due `Integer` confronta i riferimenti, non i valori (usare `equals`); l'unboxing di `null` lancia `NullPointerException`.

## Collegamenti

- **Concetti correlati**: [[Tipi generici in Java]] · [[Metodo equals]] · [[Cast in Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Classi involucro (wrapper)|Lezione 1 — Classi involucro (wrapper)]]
