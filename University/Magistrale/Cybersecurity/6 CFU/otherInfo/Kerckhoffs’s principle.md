# Principio di Kerckhoffs (Applicato all'Hashing)

**Tag:** #cryptography #security #hashing #principle #definizioni #design

---

## 📝 Definizione
Il **Principio di Kerckhoffs** (formulato da Auguste Kerckhoffs nel XIX secolo) afferma che un sistema crittografico deve essere sicuro anche se **tutto** del sistema è di dominio pubblico, tranne la chiave (se prevista).

> [!quote] La Massima di Shannon
> Una riformulazione moderna di Claude Shannon è: **"Il nemico conosce il sistema"**.

Applicato agli **algoritmi di Hashing**, questo significa che la sicurezza della funzione non deve dipendere dal tenere segreto il codice o la matematica dell'algoritmo (Security through Obscurity), ma esclusivamente dalla sua robustezza matematica.

---

## ⚙️ Applicazione all'Hashing
Poiché le funzioni di hash classiche (come SHA-256 o MD5) **non hanno una chiave segreta** (sono *unkeyed*), l'interpretazione del principio cambia leggermente rispetto alla crittografia simmetrica/asimmetrica:

### 1. Hashing Non Chiavato (Unkeyed - es. SHA-256)
Per queste funzioni, il principio impone che **l'algoritmo stesso deve essere pubblico e analizzato**.
* **Requisito:** La resistenza alle collisioni e alla pre-immagine deve reggere anche se l'attaccante ha il codice sorgente completo, conosce le costanti di inizializzazione e la matematica sottostante.
* **Violazione:** Se un'azienda usa un "Hash Proprietario Segreto" e la sua sicurezza crolla appena qualcuno fa reverse engineering del codice, allora violava il principio di Kerckhoffs.

### 2. Hashing Chiavato (Keyed - es. HMAC)
Qui il principio si applica nella sua forma classica.
* **Requisito:** L'algoritmo HMAC e la funzione di hash sottostante (es. SHA-256) sono pubblici. L'unica cosa che deve rimanere segreta è la **Chiave (K)** usata nel processo.
* Se l'attaccante conosce l'algoritmo ma non la chiave, non deve poter falsificare il digest.

---

## 🛡️ Perché "Security through Obscurity" fallisce nell'Hashing?

Molti sviluppatori inesperti tentano di "inventare" il proprio algoritmo di hash o di offuscare uno esistente (es. rimescolando i bit in modo strano) sperando che nessuno capisca come funziona.

| Approccio | Caratteristiche | Risultato |
| :--- | :--- | :--- |
| **Security by Obscurity** | Algoritmo segreto, mai testato da altri. | Appena il segreto è svelato (leak, reverse engineering), il sistema è rotto. |
| **Kerckhoffs's Principle** | Algoritmo pubblico (Open Design). | Migliaia di crittografi provano a romperlo per anni. Se resiste, è **fidato**. |

> [!danger] Esempio Pratico
> Immagina un sito web che usa un algoritmo di hash segreto inventato dal programmatore per salvare le password, invece di usare Argon2 o SHA-256.
> Se un hacker entra nel server e legge il codice sorgente (o il file compilato), scopre immediatamente la logica. Se la matematica è debole (e solitamente gli algoritmi "fatti in casa" lo sono), potrà generare collisioni o invertire l'hash istantaneamente.
>
> **Con Kerckhoffs:** Anche se l'hacker ha il codice di SHA-256, non può invertire l'hash perché la matematica lo impedisce, non la segretezza.

---

## ✅ Vantaggi dell'Open Design
Seguire il principio di Kerckhoffs nell'hashing porta a:

1.  **Peer Review:** Gli standard NIST (come la famiglia SHA) sono pubblici anni prima di diventare standard. Chiunque può provare a trovare debolezze.
2.  **Fiducia:** Non devi "fidarti" che lo sviluppatore sia stato bravo; la comunità scientifica ha validato la matematica.
3.  **Recupero Rapido:** Se la sicurezza risiede solo nella chiave (o nella complessità computazionale), in caso di compromissione del sistema basta cambiare le chiavi (per HMAC) o aggiornare le password (con salting), senza dover riscrivere l'intero software.

---

## 🔗 Collegamenti
* [[Funzioni di Hash]]
* [[HMAC]]
* [[Collision Resistance]]
* [[Security through Obscurity]]