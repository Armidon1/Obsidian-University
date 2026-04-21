# OSINT — Open Source Intelligence

---

### Definizione

**OSINT** (Open Source Intelligence) è la raccolta e analisi di informazioni da **fonti pubblicamente disponibili** per produrre intelligence utilizzabile.

La parola chiave è **"open source"** — non significa software open source, ma fonti **aperte al pubblico**, accessibili legalmente senza hacking o intercettazioni.

```
Non è hacking.
Non è illegale.
È quello che un investigatore attento può trovare
su chiunque usando solo internet.
```

---

### Le Fonti OSINT

Qualsiasi cosa pubblicamente accessibile è una fonte OSINT:

```
Internet
├── Motori di ricerca        → Google, Bing, DuckDuckGo
├── Social media             → LinkedIn, Twitter/X, Instagram, Facebook
├── Database pubblici        → WHOIS, crt.sh, WiGLE, Shodan
├── Documenti pubblici       → PDF, presentazioni, offerte lavoro
├── News e media             → articoli, comunicati stampa
├── GitHub / GitLab          → codice, commenti, email, API key
├── Forum e community        → Reddit, Stack Overflow, Pastebin
└── Dark web                 → forum, leak database (borderline)

Mondo fisico
├── Registri aziendali       → Camera di Commercio, Registro Imprese
├── Brevetti                 → USPTO, EPO — rivelano tecnologie usate
├── Offerte di lavoro        → rivelano stack tecnologico interno
├── Conferenze               → chi parla, di cosa, slide pubbliche
└── Google Street View       → layout fisico, infrastruttura visibile
```

---

### Perché le Offerte di Lavoro sono OSINT

Questo è uno degli esempi più sottovalutati:

```
Offerta lavoro Microsoft:
"Cerchiamo Senior Engineer con esperienza in:
 - Kubernetes 1.28+
 - PostgreSQL 15
 - Palo Alto Prisma Cloud
 - Windows Server 2022"

Cosa hai appena scoperto SENZA toccare nulla:
→ Usano Kubernetes (container infrastructure)
→ PostgreSQL come database principale
→ Palo Alto per la sicurezza cloud
→ Windows Server 2022 internamente
```

Un attaccante ora sa esattamente quali CVE cercare.

---

### OSINT vs Altri Tipi di Intelligence

```
OSINT   → fonti pubbliche, legale, passivo
HUMINT  → Human Intelligence, informatori, social engineering
SIGINT  → Signal Intelligence, intercettazione comunicazioni (NSA)
TECHINT → Technical Intelligence, analisi hardware/software
CYBINT  → Cyber Intelligence, analisi di minacce digitali
```

Nel cybersecurity, OSINT è il **primo passo** — raccogliere tutto il possibile legalmente prima di toccare qualsiasi cosa.

---

### Il Ciclo dell'Intelligence

L'OSINT non è solo "cercare su Google" — è un processo strutturato:

```
1. PLANNING        → Cosa devo sapere? Qual è il target?
        │
        ▼
2. COLLECTION      → Raccolta dati da fonti multiple
   (crt.sh, Shodan, GHDB, theHarvester, LinkedIn...)
        │
        ▼
3. PROCESSING      → Pulire, organizzare, deduplicare i dati
        │
        ▼
4. ANALYSIS        → Trovare pattern, connessioni, insight
        │
        ▼
5. DISSEMINATION   → Report finale, actionable intelligence
        │
        ▼
6. FEEDBACK        → Torna al punto 1 con nuove domande
```

---

### OSINT nel Contesto del Percorso che Stai Facendo

Tutto quello che hai studiato finora **è** OSINT o lo supporta:

```
dig / DNS recon     → OSINT attivo
crt.sh              → OSINT passivo
WiGLE               → OSINT passivo
GHDB                → OSINT passivo
Shodan              → OSINT passivo
theHarvester        → OSINT aggregato
nmap                → non è OSINT (tocca il target) → scanning
```

> [!tip] La distinzione importante è **passivo vs attivo**. OSINT passivo non tocca mai il target — consulta solo fonti terze. OSINT attivo (come `dig` o `theHarvester` con DNS lookup) invia query che potrebbero lasciare tracce nei log del target.

---

### Dove Imparare OSINT in Modo Strutturato

```
OSINT Framework     → https://osintframework.com
                      directory interattiva di tutti i tool per categoria

Bellingcat           → esempi reali di inchieste OSINT (giornalismo investigativo)
                      https://www.bellingcat.com

TraceLabs            → CTF dedicati all'OSINT, trovare persone scomparse reali
                      https://www.tracelabs.org

Michael Bazzell      → podcast + libro "OSINT Techniques" (la bibbia del settore)
                      https://inteltechniques.com
```

> [!info] Curiosità Bellingcat ha usato OSINT per identificare i responsabili dell'abbattimento del volo MH17, localizzare movimenti di truppe russe e tracciare agenti dei servizi segreti — tutto usando solo fonti pubbliche. È l'esempio più famoso di OSINT applicato al giornalismo investigativo.