---
title: Eccezioni in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - errori
---

# Eccezioni in Java

> [!summary] In breve
> Un'eccezione è un oggetto lanciato con `throw` quando si verifica un errore; risale la pila delle chiamate finché un `try`/`catch` la cattura, altrimenti termina il programma.

```java
try {
  x = Integer.parseInt(s);
} catch (NumberFormatException e) {
  x = 0;
} finally {
  // eseguito comunque
}
```

- **Checked** (sottoclassi di `Exception`): vanno dichiarate con `throws` o catturate.
- **Unchecked** (`RuntimeException`, ad es. `IllegalArgumentException`, `IndexOutOfBoundsException`): errori di programmazione, nessun obbligo.
- Negli ADT del libro: `IllegalStateException`, `IllegalArgumentException` per operazioni non valide.

## Collegamenti

- **Concetti correlati**: [[Pila dei metodi di Java]] · [[Eccezioni]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[02 - ASD - Progettazione orientata agli oggetti#Eccezioni|Lezione 2 — Eccezioni]]
