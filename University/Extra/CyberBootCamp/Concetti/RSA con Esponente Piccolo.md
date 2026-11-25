---
title: RSA con Esponente Piccolo
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - rsa
  - attack
---

# RSA con Esponente Piccolo

> [!summary] In breve
> Se $e$ è piccolo (es. 3) e il messaggio è corto, $m^e < N$: il modulo non interviene mai e $m$ è la radice $e$-esima **intera** del ciphertext.

$$c = m^e \bmod N = m^e \quad\Rightarrow\quad m = \sqrt[e]{c}$$
```python
import gmpy2
m, exact = gmpy2.iroot(c, e)    # exact == True se è davvero una potenza
```
- Non usare `c ** (1/e)`: in virgola mobile si perdono le cifre.
- Lo impedisce il padding ([[PKCS1]], [[RSA-OAEP]]), che riempie tutto il modulo.
- Con lo stesso $m$ inviato a $e$ destinatari: [[Håstad Broadcast Attack]].

## Collegamenti

- **Concetti correlati**: [[Håstad Broadcast Attack]] · [[RSA-OAEP]] · [[Fattorizzare il Modulo RSA]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Esponente piccolo|Lezione 7 — Esponente piccolo]]
