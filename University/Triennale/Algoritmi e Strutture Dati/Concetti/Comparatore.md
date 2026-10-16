---
title: Comparatore
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - ordinamento
---

# Comparatore

> [!summary] In breve
> Un `Comparator<K>` è un oggetto con `compare(a, b)` (negativo, zero o positivo): permette di ordinare chiavi secondo un criterio esterno, in alternativa all'ordine naturale di `Comparable`.

```java
public class StringLengthComparator implements Comparator<String> {
  public int compare(String a, String b) {
    return Integer.compare(a.length(), b.length());
  }
}
```

- `Comparable<K>`: ordine **naturale**, `a.compareTo(b)` dentro la classe.
- `Comparator<K>`: ordine **esterno**, più criteri per lo stesso tipo.
- Il `DefaultComparator` del libro usa `compareTo` (cast a `Comparable`).

## Collegamenti

- **Concetti correlati**: [[Coda prioritaria (ADT)]] · [[Tipi generici in Java]] · [[Mappa ordinata]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Confrontare chiavi totalmente ordinate|Lezione 9 — Confrontare chiavi totalmente ordinate]]
