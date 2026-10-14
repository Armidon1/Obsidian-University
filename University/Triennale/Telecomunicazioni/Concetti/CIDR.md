---
title: CIDR
tags:
  - telecomunicazioni
  - concetto
  - ip
  - indirizzamento
---

# CIDR

> [!summary] In breve
> **Classless InterDomain Routing**: l'indirizzo a.b.c.d/x ha un prefisso di rete di **x bit** di lunghezza arbitraria. Ha sostituito il **classful addressing** (classi A/B/C con prefissi da 8/16/24 bit), che sprecava indirizzi.

- I router esterni guardano solo gli $x$ bit del prefisso; i $32 - x$ bit restanti sono interni (con eventuali sottoreti).
- Classe C (/24): $2^8 - 2 = 254$ host. Classe B (/16): $2^{16} - 2 = 65.534$ host. 2000 host in una classe B → **63.000** indirizzi sprecati.
- Divisione di un blocco: 200.23.16.0/**20** → 8 blocchi /**23** (3 bit in più), da 512 indirizzi ciascuno: .16, .18, .20 … .30.

## Collegamenti

- **Concetti correlati**: [[Indirizzamento IPv4]] · [[Sottorete]] · [[Aggregazione di Indirizzi]] · [[Longest Prefix Match]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#CIDR|Capitolo 4 — CIDR]]
> - [[04 - TLC - Livello di rete - piano dei dati#Come ottenere un blocco di indirizzi|Capitolo 4 — Come ottenere un blocco di indirizzi]]
