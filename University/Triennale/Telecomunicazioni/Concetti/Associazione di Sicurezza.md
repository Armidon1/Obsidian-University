---
title: Associazione di Sicurezza
tags:
  - telecomunicazioni
  - concetto
  - ipsec
---

# Associazione di Sicurezza

> [!summary] In breve
> Una **SA** è la connessione logica **unidirezionale** di livello rete creata tra due entità IPsec prima di scambiarsi datagrammi sicuri. Il suo stato (SPI, interfacce, cifratura e chiave, integrità e chiave) è memorizzato nel **SAD**.

- Esempio R1 → R2: SPI di 32 bit, 200.168.1.100 → 193.68.2.23, 3DES-CBC, HMAC-MD5.
- Comunicazione bidirezionale = 2 SA.
- Si creano a mano o automaticamente con **IKE**.

## Collegamenti

- **Concetti correlati**: [[IPsec ed ESP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Associazioni di sicurezza|Capitolo 8 — Associazioni di sicurezza]]
