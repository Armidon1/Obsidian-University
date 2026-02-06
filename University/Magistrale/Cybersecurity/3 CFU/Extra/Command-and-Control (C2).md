# Command-and-Control (C2) Infrastructure

**Tags:** #CyberSecurity #Malware #Botnet #DNS #NetworkSecurity 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Definizione

Il **Command-and-Control (C2)** è l'infrastruttura server utilizzata dagli attaccanti per comunicare con i dispositivi compromessi (malware o bot). Attraverso il C2, l'attaccante:

1. Invia comandi da eseguire (es. "lancia un attacco DDoS", "scarica questo payload").
2. Riceve i dati esfiltrati dalla vittima (es. password, informazioni di sistema).

## 🕵️‍♂️ Ruolo del DNS nel C2

Il DNS è un protocollo critico per le operazioni C2 perché il traffico DNS è solitamente **permesso dai firewall** e considerato "fidato". Le moderne tecniche di malware sfruttano il DNS per tre scopi principali: identificazione, comunicazione nascosta e protezione.

### 1. Identificazione Dinamica (DGA)

Per evitare che il server C2 venga bloccato tramite blacklist statiche di domini o IP, i malware utilizzano **[[Domain Generation Algorithms (DGA)]]**.

- **Funzionamento:** Il malware genera deterministicamente migliaia di nomi di dominio pseudo-casuali (es. basandosi sulla data o su semi crittografici).
- **Connessione:** Il malware tenta di risolvere questi domini in sequenza finché non ne trova uno che risponde (quello registrato dall'attaccante per quel giorno).
- **Obiettivo:** Resilienza ai takedown e "Asymmetric advantage" (l'attaccante deve registrarne solo uno, il difensore deve bloccarne migliaia).

### 2. Comunicazione Occulta (DNS Tunneling)

Il C2 usa il DNS come canale di trasporto dati per aggirare i monitoraggi di rete.

- **Uscita (Exfiltration):** I dati rubati vengono codificati nei **nomi di dominio** delle query (es. `password123.evil.com`).
- **Entrata (Command):** I comandi dell'attaccante vengono codificati nei campi di **risposta DNS** (es. record TXT, o falsi indirizzi IP nei record A/AAAA).

### 3. Protezione dell'Infrastruttura (Fast-Fluxing)

Per nascondere la posizione reale del server C2 ("backend server"), gli attaccanti usano il **DNS Fast-Fluxing**.

- **Proxying:** Il dominio malevolo non risolve all'IP del C2, ma agli IP di computer compromessi (bot) che agiscono come **reverse proxies**.
- **Rotazione:** I record DNS hanno un **TTL bassissimo** (es. 60 secondi) e cambiano costantemente, ruotando tra migliaia di IP di bot diversi. Questo rende difficile abbattere l'infrastruttura.

---

## ⚠️ C2 e Protocolli Moderni (DoH)

L'evoluzione verso **DNS over HTTPS (DoH)** rappresenta una nuova sfida per rilevare il traffico C2.

- Poiché DoH mischia le query DNS con il normale traffico HTTPS (Porta 443), offre un canale cifrato e difficile da bloccare o analizzare per gli amministratori di rete, diventando un vettore ideale per le comunicazioni C2.

---

## 🔗 Collegamenti

- [[Domain Generation Algorithm (DGA)]]
- [[DNS Tunneling]]
- [[DNS Fast-Fluxing]]
- [[Botnet]]
- [[DNS over HTTPS (DoH)]]