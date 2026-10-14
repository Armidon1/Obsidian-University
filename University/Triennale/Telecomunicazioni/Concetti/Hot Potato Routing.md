---
title: Hot Potato Routing
tags:
  - telecomunicazioni
  - concetto
  - bgp
  - routing
---

# Hot Potato Routing

> [!summary] In breve
> Instradamento a **patata bollente**: tra più gateway per uscire dall'AS si sceglie quello con il **minor costo intra-AS**, per far uscire il pacchetto il prima possibile senza badare al resto del percorso.

Passi per aggiungere un prefisso esterno $x$:
1. BGP: $x$ è raggiungibile tramite più gateway;
2. intra-AS (OSPF): costi verso ogni gateway;
3. si sceglie il gateway più economico;
4. si ricava l'interfaccia $I$ e si scrive $(x, I)$.

- È **egoista**: minimizza il costo dentro il proprio AS.
- Due router dello stesso AS possono scegliere percorsi diversi.
- Nella selezione BGP completa è solo la **regola 3**.

## Collegamenti

- **Concetti correlati**: [[Selezione delle Rotte BGP]] · [[Protocollo BGP]] · [[OSPF]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Instradamento hot potato|Capitolo 5 — Instradamento hot potato]]
