---
title: Checksum Internet
tags:
  - telecomunicazioni
  - concetto
  - livello-trasporto
  - errori
---

# Checksum Internet

> [!summary] In breve
> È il checksum di UDP e TCP: il **complemento a 1** della somma di tutte le parole da 16 bit del segmento, con il riporto sommato in fondo. In ricezione la somma di tutto, checksum compreso, deve dare tutti 1.

```text
  0110011001100000
+ 0101010101010101
+ 1000111100001100   (riporto sommato al bit meno significativo)
= 0100101011000010
checksum = 1011010100111101   (complemento a 1)
```

- Ricezione: somma di parole + checksum = `1111111111111111`; uno `0` significa errore.
- Rileva ma **non corregge** (UDP scarta o avverte).
- Serve anche se il collegamento controlla già gli errori: non tutti i collegamenti lo fanno, e gli errori possono nascere **nella memoria dei router** → **principio end-to-end**.

## Collegamenti

- **Concetti correlati**: [[Protocollo UDP]] · [[Trasferimento Dati Affidabile]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Checksum UDP|Capitolo 3 — Checksum UDP]]
