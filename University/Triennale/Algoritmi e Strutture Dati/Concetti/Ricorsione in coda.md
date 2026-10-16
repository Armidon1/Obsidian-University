---
title: Ricorsione in coda
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
---

# Ricorsione in coda

> [!summary] In breve
> Una ricorsione è in coda se la chiamata ricorsiva è l'ultima operazione e il suo risultato è restituito direttamente: si può trasformare meccanicamente in un ciclo, risparmiando lo spazio della pila.

- Ricerca binaria e inversione di un array sono in coda; il fattoriale `n * factorial(n-1)` **no** (dopo la chiamata c'è una moltiplicazione).
- Trasformazione: si aggiornano i parametri e si ripete in un `while`.

```java
while (low <= high) {
  int mid = (low + high) / 2;
  if (target == data[mid]) return true;
  else if (target < data[mid]) high = mid - 1;
  else low = mid + 1;
}
return false;
```

## Collegamenti

- **Concetti correlati**: [[Ricorsione]] · [[Ricerca binaria]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Eliminare la ricorsione in coda|Lezione 5 — Eliminare la ricorsione in coda]]
