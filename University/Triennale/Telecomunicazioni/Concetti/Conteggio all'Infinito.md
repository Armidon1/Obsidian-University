---
title: Conteggio all'Infinito
tags:
  - telecomunicazioni
  - concetto
  - routing
  - bellman-ford
---

# Conteggio all'Infinito

> [!summary] In breve
> Nel distance-vector le **cattive notizie** (un costo che aumenta) si propagano lentamente: due nodi si rimandano stime sbagliate in un **ciclo di instradamento**. L'**inversione avvelenata** lo evita solo per cicli di due nodi.

- **Buone notizie** (y–x da 4 a 1): quiete in 2 iterazioni.
- **Cattive notizie** (y–x da 4 a 60, c(x,z) = 50):
  - $D_y(x) = \min\{60, 1 + 5\} = 6$ (sbagliato: si passa per z, che passa per y), poi $D_z(x) = 7$, $D_y(x) = 8$…;
  - servono **44 iterazioni** prima che z scelga il collegamento diretto (50).
- **Poisoned reverse**: se z instrada verso x via y, dice a y che $D_z(x) = \infty$.
- Non risolve i cicli con **3 o più** nodi.

## Collegamenti

- **Concetti correlati**: [[Instradamento Distance-Vector]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Modifica dei costi e guasti dei collegamenti|Capitolo 5 — Modifica dei costi e guasti dei collegamenti]]
> - [[05 - TLC - Livello di rete - piano di controllo#Inversione avvelenata|Capitolo 5 — Inversione avvelenata]]
