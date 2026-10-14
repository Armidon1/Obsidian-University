---
title: Fairness TCP
tags:
  - telecomunicazioni
  - concetto
  - tcp
  - congestione
---

# Fairness TCP

> [!summary] In breve
> Un controllo di congestione è **fair** se $K$ connessioni su un collo di bottiglia di capacità $R$ ottengono circa $R/K$ ciascuna. AIMD converge alla divisione equa, ma UDP e le connessioni parallele rompono l'equità.

- Due connessioni: l'incremento è a 45°, il dimezzamento porta verso l'origine, quindi oscillano lungo la **bisettrice** (equa condivisione) vicino alla linea di pieno utilizzo $R$.
- In pratica le connessioni con **RTT minore** ottengono di più.
- **UDP** non riduce la velocità, quindi può soffocare TCP.
- **Connessioni parallele**: con 9 app da 1 connessione, una nuova app con 11 connessioni ottiene $11/20 \cdot R = 0{,}55R$.

## Collegamenti

- **Concetti correlati**: [[AIMD]] · [[Protocollo UDP]] · [[Controllo di Congestione TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[03 - TLC - Livello di trasporto#Fairness|Capitolo 3 — Fairness]]
> - [[03 - TLC - Livello di trasporto#Fairness e UDP|Capitolo 3 — Fairness e UDP]]
> - [[03 - TLC - Livello di trasporto#Fairness e connessioni TCP parallele|Capitolo 3 — Fairness e connessioni TCP parallele]]
