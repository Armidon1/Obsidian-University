---
title: Modello OSI e TCP-IP
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
---

# Modello OSI e TCP-IP

> [!summary] In breve
> OSI: 7 livelli (fisico, collegamento, rete, trasporto, sessione, presentazione, applicazione). TCP/IP: applicazione, trasporto (TCP/UDP), internet (IP), accesso alla rete, fisico.

| OSI | TCP/IP | Esempi |
| --- | --- | --- |
| Applicazione, presentazione, sessione | Applicazione | HTTP, SMTP, FTP, SSH, DNS |
| Trasporto | Trasporto | TCP, UDP |
| Rete | Internet | IP (+ ARP, ICMP) |
| Collegamento, fisico | Accesso alla rete, fisico | Ethernet, Wi-Fi |

- TCP/IP ha la forma a **clessidra**: tante applicazioni e tante reti, un solo IP in mezzo.
- I router implementano solo fino al livello rete.
- Indirizzi: nome DNS → IP → MAC.

## Collegamenti

- **Concetti correlati**: [[Architettura a Livelli dei Protocolli]] · [[Protocollo IP]] · [[TCP e UDP]] · [[ARP]] · [[DNS]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[06 - SDC2 - Reti di Calcolatori#Il modello OSI|Lezione 6 — Il modello OSI]]
> - [[06 - SDC2 - Reti di Calcolatori#Architettura a 3 livelli e TCP/IP|Lezione 6 — Architettura a 3 livelli e TCP/IP]]
> - [[06 - SDC2 - Reti di Calcolatori#TCP/IP|Lezione 6 — TCP/IP]]
> - [[07 - SDC2 - Socket#Architettura TCP/IP|Lezione 7 — Architettura TCP/IP]]
