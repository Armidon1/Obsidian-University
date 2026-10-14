---
title: Record DNS
tags:
  - telecomunicazioni
  - concetto
  - dns
---

# Record DNS

> [!summary] In breve
> Il database DNS contiene **resource record** `(Name, Value, Type, TTL)`. I tipi principali sono A (nome → IP), NS (dominio → server autoritativo), CNAME (alias → nome canonico) e MX (alias → mail server).

| Type | Esempio |
| --- | --- |
| **A** | `(relay1.bar.foo.com, 145.37.93.126, A)` |
| **NS** | `(foo.com, dns.foo.com, NS)` |
| **CNAME** | `(foo.com, relay1.bar.foo.com, CNAME)` |
| **MX** | `(foo.com, mail.bar.foo.com, MX)` |

- **Messaggio DNS**: query e risposta hanno lo stesso formato. Intestazione di 12 byte (ID di 16 bit, flag query/risposta, autoritativo, recursion-desired, recursion-available, contatori) + sezioni **domande**, **risposte**, **autoritativa** e **aggiuntiva**.
- Registrazione di un dominio: il **registrar** (accreditato ICANN) inserisce nei TLD i record NS e A dei tuoi server autoritativi.
- Per provare: `nslookup`.

## Collegamenti

- **Concetti correlati**: [[Gerarchia dei DNS Server]] · [[Query DNS Ricorsive e Iterative]] · [[DNS]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Record e messaggi DNS|Capitolo 2 — Record e messaggi DNS]]
> - [[02 - TLC - Livello di applicazione#Messaggi DNS|Capitolo 2 — Messaggi DNS]]
> - [[02 - TLC - Livello di applicazione#Inserimento di record nel database DNS|Capitolo 2 — Inserimento di record nel database DNS]]
