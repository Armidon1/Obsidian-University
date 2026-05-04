# Maltego — Visual OSINT & Link Analysis

#linux #cybersecurity #osint #reconnaissance #linux-basics-for-hackers

---

## 🗂️ Overview

**Maltego** è una piattaforma OSINT e di **link analysis visuale** sviluppata da Paterva. A differenza di tutti gli altri tool che hai studiato — che producono output testuale — Maltego produce un **grafo interattivo** che mostra le relazioni tra entità diverse.

```
theHarvester → lista di testo
Sherlock     → lista di testo
Nmap         → lista di testo

Maltego      → GRAFO VISUALE
               dominio ──→ IP ──→ ASN ──→ organizzazione
                  │                           │
                  └──→ email ──→ persona ──→ LinkedIn
                  └──→ sottodomini ──→ server ──→ porte
```

Il concetto chiave è il **pivoting visuale** — ogni nodo nel grafo può essere espanso per trovare nuove connessioni, costruendo progressivamente una mappa completa del target.

---

## 💰 Edizioni

|Edizione|Costo|Limitazioni|
|---|---|---|
|**Community (CE)**|Gratuita|12 risultati per transform, watermark sui grafi|
|**Maltego One**|~999$/anno|Accesso completo, transform illimitati|
|**Enterprise**|Custom|Multi-utente, API avanzate|

> [!tip] Per studiare e fare pratica la **Community Edition è sufficiente**. Il limite di 12 risultati per transform è fastidioso ma non blocca l'apprendimento del flusso di lavoro.

---

## 🛠️ Installazione

```bash
# Pre-installato su Kali Linux
maltego

# Se non presente
sudo apt update && sudo apt install maltego -y

# Oppure scarica dal sito ufficiale
# https://www.maltego.com/downloads/
```

Al primo avvio richiede registrazione — crea un account gratuito su maltego.com.

---

## 🧠 Concetti Fondamentali

### Entities (Entità)

Le entità sono i **nodi del grafo** — ogni oggetto che Maltego conosce:

```
Infrastruttura:    Domain, IP Address, URL, Website,
                   DNS Name, MX Record, Netblock, ASN

Persone:           Person, Email Address, Phone Number,
                   Alias, Social Media Profile, Image

Organizzazioni:    Organization, Company, Location

File:              Document, File, Hash

Social:            Twitter/X, LinkedIn, Instagram, GitHub
```

### Transforms (Trasformazioni)

Le transform sono **query che espandono un nodo** — prendono un'entità come input e restituiscono entità correlate come output.

```
Input: Domain "microsoft.com"
Transform: "To IP Address"
Output: IP 20.112.52.29

Input: IP 20.112.52.29
Transform: "To ASN"
Output: AS8075 (Microsoft)

Input: AS8075
Transform: "To Netblock"
Output: 20.0.0.0/8
```

Ogni right-click su un nodo mostra le transform disponibili per quel tipo di entità.

### Machines (Macchine)

Le machine sono **sequenze automatizzate di transform** — eseguono una serie di operazioni in catena senza input manuale.

```
Machine: "Footprint L1"
→ Esegue automaticamente: NS lookup, MX lookup,
  IP resolution, WHOIS, DNS brute force
→ In un click ottieni il footprint completo di un dominio
```

---

## 🔄 Il Transform Hub

Il Transform Hub è il **marketplace delle transform** — estensioni che aggiungono nuove fonti dati.

Transform più importanti disponibili:

```
Shodan          → integrazione diretta con Shodan
Have I Been Pwned → verifica email in breach database
VirusTotal      → analisi malware e reputazione domini
Hunter.io       → email harvesting
FullContact     → enrichment dati personali
GitHub          → repository e utenti
Censys          → certificati SSL e host
URLScan         → analisi URL e screenshot
Wayback Machine → storico versioni siti web
```

```bash
# Nel Transform Hub (dentro Maltego)
# Transforms → Transform Hub → installa quello che ti serve
```

---

## 🗺️ Workflow — Investigazione su un Dominio

### Step 1 — Crea un nuovo grafo

```
File → New → Blank Graph
```

### Step 2 — Aggiungi l'entità iniziale

```
Entity Palette (sinistra) → trascina "Domain" nel canvas
Double-click sul nodo → inserisci "example.com"
```

### Step 3 — Lancia le transform

```
Right-click sul dominio →
  Run Transform →
    To DNS Name [NS]         → name server
    To DNS Name [MX]         → mail server
    To IP Address [DNS]      → IP del sito
    To Email Address [...]   → email trovate
    To Website [Quick Lookup] → sito web
```

### Step 4 — Espandi ogni nodo trovato

```
Right-click sull'IP trovato →
  Run Transform →
    To ASN                   → autonomous system
    To Netblock              → range IP dell'organizzazione
    To Location [city]       → geolocalizzazione

Right-click sull'email trovata →
  Run Transform →
    To Person                → identità collegata
    To Social Media [...]    → profili social
    Have I Been Pwned        → leak nei breach database
```

### Step 5 — Il grafo cresce automaticamente

```
example.com
    ├── ns1.googledomains.com (NS)
    ├── 15.197.x.x (IP)
    │       ├── Amazon Technologies (ASN)
    │       ├── Seattle, USA (Location)
    │       └── 15.196.0.0/14 (Netblock)
    ├── mail.example.com (MX)
    └── info@example.com (Email)
            └── Mario Rossi (Person)
                    └── linkedin.com/in/mario-rossi
```

---

## 🔍 Workflow — Investigazione su una Persona

```
1. Aggiungi entità "Person" con il nome target

2. Transform disponibili:
   To Email Address      → email associate
   To Phone Number       → numeri di telefono
   To Social Networks    → profili social
   To Document           → documenti pubblici collegati
   To Company            → aziende associate

3. Da ogni email trovata:
   Have I Been Pwned     → in quali breach è comparsa?
   To Person             → conferma identità
   To Domain             → domini registrati con quell'email

4. Da ogni profilo social:
   To Alias              → altri username
   To Person             → connessioni personali
   To Location           → geolocalizzazione dei post
```

---

## ⚡ Machines — Automazione Completa

Le machine eseguono workflow predefiniti con un solo click:

```
# Disponibili nella Community Edition:
Footprint L1    → footprint leggero di un dominio
                  NS, MX, IP, WHOIS
Footprint L2    → footprint medio
                  + sottodomini, email, banner
Footprint L3    → footprint pesante (lento)
                  tutto + brute force

# Come usarle:
Aggiunto dominio nel canvas →
Machines (menu) → Run Machine → seleziona la machine
```

> [!warning] `Footprint L3` è **molto rumoroso** — genera decine di query verso il target. Usarlo solo su target autorizzati.

---

## 🔗 Integrazione con Altri Tool

Maltego non sostituisce gli altri tool — li **integra e visualizza**:

```
theHarvester → trova email e sottodomini
      │
      ↓ importa risultati in Maltego
Maltego      → visualizza le relazioni
      │        espande ogni entità trovata
      │        pivota verso nuove informazioni
      ↓
Sherlock     → per ogni username trovato
               cerca la presenza su 400+ siti

Exiftool     → per ogni documento trovato
               estrai metadati → importa autore in Maltego
```

### Integrazione Sherlock + Maltego

È possibile creare una transform personalizzata che lancia Sherlock da dentro Maltego:

```python
# Transform che collega Maltego a Sherlock
# Input: Alias (username)
# Output: Social Media Profile entities
# Documentazione: github.com/sherlock-project/sherlock
```

---

## 📊 Maltego vs Altri Tool OSINT

|                         | Maltego       | theHarvester | Sherlock  | Recon-ng |
| ----------------------- | ------------- | ------------ | --------- | -------- |
| **Output**              | Grafo visuale | Testo        | Testo     | Testo    |
| **Pivoting visuale**    | ⭐⭐⭐⭐⭐         | ❌            | ❌         | ❌        |
| **Fonti integrate**     | 100+          | 40+          | 400+ siti | 60+      |
| **Automazione**         | ✅ Machines    | Parziale     | ❌         | ✅        |
| **Difficoltà**          | ⭐⭐⭐           | ⭐            | ⭐         | ⭐⭐       |
| **Gratuito**            | CE limitata   | ✅            | ✅         | ✅        |
| **Pre-installato Kali** | ✅             | ✅            | ✅         | ✅        |
| **Persone fisiche**     | ⭐⭐⭐⭐⭐         | ⭐⭐           | ⭐⭐⭐       | ⭐⭐       |
| **Infrastruttura**      | ⭐⭐⭐⭐          | ⭐⭐⭐⭐⭐        | ❌         | ⭐⭐⭐⭐     |

---

## ⚠️ Limitazioni

```
❌ Community Edition → max 12 risultati per transform
❌ Richiede registrazione anche per l'edizione gratuita
❌ Alcune transform richiedono API key di servizi terzi
❌ Pesante → richiede almeno 4GB RAM per lavorare bene
❌ Curva di apprendimento più alta degli altri tool
❌ Alcune transform premium sono molto costose
```

---

## 🎯 Quando Usare Maltego vs Gli Altri Tool

```
Stai mappando l'infrastruttura di una rete?
→ theHarvester + Nmap + poi visualizza in Maltego

Stai cercando un username su social?
→ Sherlock (più veloce e completo per questo)

Stai costruendo un profilo completo di un'organizzazione
con relazioni tra persone, domini, IP, email?
→ Maltego — è il suo punto di forza assoluto

Stai facendo recon veloce su un singolo dominio?
→ theHarvester (più veloce, meno setup)

Stai presentando risultati a un cliente?
→ Maltego — il grafo è il modo migliore per
  comunicare la superficie d'attacco visivamente
```

---

## 🔗 Command Cheat Sheet

```bash
# Avvio
maltego                                    # apri Maltego

# Dentro Maltego — shortcut
Ctrl+N                                     # nuovo grafo
Ctrl+S                                     # salva grafo
Ctrl+Z                                     # undo
Ctrl+A                                     # seleziona tutto
Ctrl+scroll                                # zoom in/out
Right-click su nodo → Run Transform        # lancia transform
Right-click su nodo → Run Machine          # lancia machine
Ctrl+click su più nodi → run su selezione  # transform multipli

# Export risultati
File → Export → PNG/PDF/CSV/XML
```

---

## 🔗 Related Notes

- [[Sherlock]]
- [[Exiftool]]
- [[theHarvester]]
- [[LinuxCommands/Nmap]]
- [[GHDB_Google_Hacking_Database]]
- [[OSINT & Footprinting]]

---

_References: https://www.maltego.com · https://docs.maltego.com · https://book.hacktricks.xyz · Linux Basics for Hacking — OccupyTheWeb_