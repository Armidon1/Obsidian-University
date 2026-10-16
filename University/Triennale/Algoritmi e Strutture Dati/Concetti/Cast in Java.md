---
title: Cast in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - tipi
---

# Cast in Java

> [!summary] In breve
> Il cast converte un valore o un riferimento in un altro tipo: tra primitivi può perdere informazione, tra riferimenti è un *widening* implicito verso l'alto o un *narrowing* esplicito verso il basso controllato a runtime.

- **Primitivi**: `int → double` implicito; `double → int` esplicito (`(int) 3.9` = 3, troncamento).
- **Riferimenti**:
  - *widening* (sottotipo → supertipo): implicito, sempre sicuro;
  - *narrowing* (supertipo → sottotipo): esplicito `(Sottotipo) rif`; se l'oggetto non è di quel tipo → `ClassCastException`.
- `instanceof` verifica il tipo prima del cast.

```java
Object o = "ciao";          // widening
String s = (String) o;      // narrowing ok
Integer i = (Integer) o;    // ClassCastException a runtime
```

## Collegamenti

- **Concetti correlati**: [[Ereditarietà in Java]] · [[Polimorfismo e smistamento dinamico]] · [[Classi involucro e auto-boxing]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Conversioni di tipo|Lezione 1 — Conversioni di tipo]]
> - [[02 - ASD - Progettazione orientata agli oggetti#Cast|Lezione 2 — Cast]]
