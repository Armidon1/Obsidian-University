---
title: Firewall e Intrusion Detection
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sicurezza
  - reti
---

# Firewall e Intrusion Detection

> [!summary] In breve
> Il firewall è un punto di controllo che filtra i pacchetti (packet filter, stateful, application/circuit proxy). Un IDS rileva le intrusioni per anomalie o per firme. Gli honeypot sono esche.

- Politiche di default: **discard** (vieta tutto tranne…, più sicura) o **forward**.
- Stateful: tiene la tabella delle connessioni TCP e accetta in ingresso solo le risposte.
- Topologia: router → firewall esterno → **DMZ** (web, mail, DNS) → firewall interno → rete interna; firewall distribuiti sugli host.
- Limiti: non protegge da chi lo aggira, dagli insider, dai dispositivi infettati fuori.
- IDS: anomaly detection (soglie, profili) e signature detection; i profili di intrusi e utenti si sovrappongono (falsi positivi e negativi).

## Collegamenti

- **Concetti correlati**: [[Triade CIA]] · [[TCP e UDP]] · [[Botnet e DDoS]] · [[Malware]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[10 - SDC2 - Sicurezza#Firewall|Lezione 10 — Firewall]]
> - [[10 - SDC2 - Sicurezza#Packet filtering|Lezione 10 — Packet filtering]]
> - [[10 - SDC2 - Sicurezza#Stateful inspection|Lezione 10 — Stateful inspection]]
> - [[10 - SDC2 - Sicurezza#Intrusion detection|Lezione 10 — Intrusion detection]]
> - [[10 - SDC2 - Sicurezza#Honeypot|Lezione 10 — Honeypot]]
