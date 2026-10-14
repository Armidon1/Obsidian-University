---
title: Protocollo ICMP
tags:
  - telecomunicazioni
  - concetto
  - icmp
  - livello-rete
---

# Protocollo ICMP

> [!summary] In breve
> ICMP (RFC 792) serve a host e router per scambiarsi informazioni di livello rete, soprattutto **errori**. Viaggia come payload di IP, con un **tipo**, un **codice** e l'intestazione più i primi 8 byte del datagramma che ha causato l'errore.

| Tipo/codice | Significato |
| --- | --- |
| 0/0 | risposta echo |
| 3/0, 3/1 | rete / host irraggiungibile |
| 3/3 | **porta** irraggiungibile |
| 4/0 | riduzione del tasso (raro) |
| 8/0 | richiesta echo (**ping**) |
| 11/0 | **TTL scaduto** |
| 12/0 | intestazione IP errata |

- **Traceroute**: datagrammi UDP verso una porta improbabile con TTL = 1, 2, 3…; ogni router risponde con 11/0; la destinazione con 3/3 indica che si può smettere; 3 prove per TTL.
- **ICMPv6** (RFC 4443): aggiunge "pacchetto troppo grande" e "opzioni non riconosciute".

## Collegamenti

- **Concetti correlati**: [[Traceroute]] · [[ICMP]] · [[Datagramma IPv4]] · [[Protocollo IPv6]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#5.6 ICMP (Internet control message protocol)|Capitolo 5 — 5.6 ICMP (Internet control message protocol)]]
