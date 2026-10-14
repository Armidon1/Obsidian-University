---
title: BitTorrent
tags:
  - telecomunicazioni
  - concetto
  - p2p
---

# BitTorrent

> [!summary] In breve
> Protocollo P2P per la distribuzione di file: i peer di un **torrent** si scambiano **chunk** da 256 kB, trovano gli altri tramite un **tracker**, chiedono prima i chunk più rari (*rarest first*) e ricambiano chi li serve meglio (*tit-for-tat*).

- **Tracker**: dà al nuovo peer una lista casuale di ~50 peer; quelli raggiunti via TCP sono i **vicini**.
- **Rarest first**: si richiedono prima i chunk con meno copie tra i vicini, così le copie si uniformano.
- **Tit-for-tat**:
  - si inviano chunk ai **4 vicini più veloci** (*unchoked*), ricalcolati ogni 10 s;
  - ogni 30 s si sceglie un vicino a caso (*optimistically unchoked*);
  - gli altri sono *choked*.
- Lo scopo è scoraggiare i **free-rider**.
- **DHT**: database distribuiti tra i peer.

## Collegamenti

- **Concetti correlati**: [[Distribuzione di File P2P]] · [[Architetture Client-Server e P2P]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#BitTorrent|Capitolo 2 — BitTorrent]]
