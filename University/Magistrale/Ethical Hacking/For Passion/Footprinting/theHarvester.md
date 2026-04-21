# theHarvester — OSINT Aggregator

---

### Cos'è

theHarvester è uno strumento [[OSINT]] progettato per raccogliere informazioni pubbliche relative a domini specifici. Creato originariamente da Christian Martorella, è disponibile su GitHub come parte del progetto EdgeSecurity.

La differenza chiave rispetto agli altri tool che hai visto:

```
crt.sh        → solo sottodomini via certificati
Shodan        → solo dispositivi e porte
GHDB          → solo Google dork
theHarvester  → tutto insieme, da 40+ fonti simultaneamente
```

Quello che rende theHarvester unico è il suo approccio minimalista, l'alta velocità di esecuzione e la capacità di operare in modalità completamente passiva — non interagisce direttamente con i server del target.

---

### Cosa raccoglie

theHarvester raccoglie email, host, sottodomini, IP, nomi di dipendenti, porte aperte e banner da diverse fonti pubbliche come motori di ricerca, server PGP e il database Shodan.

```
Email addresses     → per phishing e social engineering
Subdomains          → per mappare la superficie d'attacco
IP addresses        → per identificare l'infrastruttura
Employee names      → per social engineering e LinkedIn recon
Open ports          → tramite integrazione Shodan
Virtual hosts       → più siti sullo stesso server
URLs                → pagine indicizzate pubblicamente
```

---

### Installazione

```bash
# Pre-installato su Kali Linux — verifica:
theHarvester --help

# Aggiornare all'ultima versione
sudo apt update && sudo apt install theharvester -y

# Oppure dalla sorgente (versione più aggiornata)
git clone https://github.com/laramies/theHarvester
cd theHarvester
pip install -r requirements/base.txt --break-system-packages
```

---

### Sintassi Base

```bash
theHarvester -d [dominio] -b [fonte] [opzioni]
```

|Flag|Significato|
|---|---|
|`-d`|Dominio target|
|`-b`|Source/backend da usare|
|`-l`|Limite di risultati (default 500)|
|`-f`|Salva output su file|
|`-v`|Verbose — mostra virtual host|
|`-n`|Esegui DNS lookup sui risultati|
|`-c`|Brute force sottodomini con wordlist|
|`-e`|DNS server da usare|
|`-p`|Porta per DNS brute force|
|`-s`|Usa Shodan per info sugli IP trovati|
|`-g`|Usa Google dork|

---

### Le Fonti — `-b`

theHarvester richiede Python 3.12 o superiore e supporta numerose fonti tra cui bevigil, brave, bufferoverun e molte altre.

```bash
# Fonti principali disponibili
google          → motore di ricerca Google
bing            → motore di ricerca Bing (spesso più permissivo)
yahoo           → motore di ricerca Yahoo
duckduckgo      → DuckDuckGo
linkedin        → nomi dipendenti ← molto utile per social engineering
twitter         → account e info pubbliche
github          → repository e email esposte nel codice
shodan          → dispositivi e porte aperte
censys          → certificati SSL e sottodomini
dnsdumpster     → sottodomini e record DNS
urlscan         → URL scansionati pubblicamente
securitytrails  → dati DNS storici e attuali
virustotal      → analisi malware + sottodomini
hunter          → email aziendali (richiede API key)
all             → usa TUTTE le fonti disponibili
```

---

### Esempi Pratici

```bash
# Ricerca base su Google
theHarvester -d microsoft.com -b google

# Aumentare il limite di risultati
theHarvester -d microsoft.com -b google -l 1000

# Fonti multiple combinate
theHarvester -d microsoft.com -b google,bing,duckduckgo

# Nomi dipendenti via LinkedIn ← ottimo per social engineering
theHarvester -d microsoft.com -b linkedin

# Tutto da tutte le fonti (lento ma massimale)
theHarvester -d microsoft.com -b all

# Con integrazione Shodan sui risultati
theHarvester -d microsoft.com -b google -s

# Salvare i risultati
theHarvester -d microsoft.com -b all -f microsoft_recon

# DNS brute force sottodomini
theHarvester -d microsoft.com -b google -c

# Lookup DNS sui risultati trovati
theHarvester -d microsoft.com -b bing -n
```

---

### API Keys — Sbloccare le Fonti Premium

Alcune fonti richiedono API key per funzionare:

```bash
nano ~/.theHarvester/api-keys.yaml
```

```yaml
google: TUA_GOOGLE_API_KEY
bing: TUA_BING_API_KEY
github: TUA_GITHUB_TOKEN
shodan: TUA_SHODAN_API_KEY
hunter: TUA_HUNTER_API_KEY
securitytrails: TUA_ST_API_KEY
```

> [!tip] Shodan offre un piano free con API key. Hunter.io offre 25 ricerche gratis al mese. Entrambi valgono la pena di configurare anche solo con l'account gratuito.

---

### Output — Cosa Aspettarsi

```
[*] Emails found: 12
---------------------------
j.smith@microsoft.com
security@microsoft.com
abuse@microsoft.com

[*] Hosts found: 47
---------------------
mail.microsoft.com:104.47.0.1
vpn.microsoft.com:13.107.6.152
dev.microsoft.com:20.112.52.29      ← interessante
staging.microsoft.com:20.54.232.182 ← molto interessante

[*] IPs found: 23
------------------
13.107.6.152
20.112.52.29
104.47.0.1
```

---

### Nel Workflow di Reconnaissance

```
theHarvester
      │
      ├── Email trovate
      │       └── phishing, password spraying, breach check su HaveIBeenPwned
      │
      ├── Sottodomini trovati
      │       └── dig → risolvi IP → nmap → cerca servizi
      │
      ├── IP trovati
      │       └── Shodan → porte e versioni → searchsploit → CVE
      │
      └── Nomi dipendenti
              └── LinkedIn → organigramma → social engineering
```

---

### theHarvester vs strumenti simili

||theHarvester|Maltego|recon-ng|SpiderFoot|
|---|---|---|---|---|
|**Facilità d'uso**|⭐⭐⭐⭐⭐|⭐⭐⭐|⭐⭐⭐|⭐⭐⭐⭐|
|**Fonti**|40+|100+|60+|200+|
|**Output visuale**|❌|✅ grafo|❌|✅|
|**Pre-installato Kali**|✅|✅|✅|❌|
|**Gratuito**|✅|Parziale|✅|✅|
|**Email harvesting**|⭐⭐⭐⭐⭐|⭐⭐⭐|⭐⭐⭐|⭐⭐⭐⭐|
|**Velocità**|⚡ Fast|🐢 Slow|🟡 Medium|🟡 Medium|

---
# theHarvester vs Shodan
### theHarvester e Shodan non fanno la stessa cosa

È un malinteso comune. theHarvester **usa** Shodan come una delle sue fonti, ma lo fa in modo superficiale:

```
theHarvester -b shodan
→ interroga Shodan per trovare host associati al dominio
→ ti restituisce una lista di IP e porte
→ si ferma qui
```

Shodan direttamente:

```
org:"Target Corp" port:3389 os:"Windows Server 2019" vuln:CVE-2021-34527
→ filtra per organizzazione
→ filtra per porta specifica
→ filtra per OS specifico
→ filtra per vulnerabilità specifica
→ ti restituisce screenshot, banner completi, certificati SSL,
   geolocalizzazione, ASN, storico delle scansioni, tutto
```

---

### La differenza concreta

Pensa a theHarvester come a **una rete da pesca** — la lanci e recuperi tutto quello che viene su, da 40 fonti diverse, velocemente.

Pensa a Shodan come a **un bisturi** — vai esattamente dove vuoi, con precisione chirurgica, e estrai informazioni che theHarvester non può nemmeno vedere.

```
theHarvester ti dice:  "ho trovato questi 23 IP associati al target"
Shodan ti dice:        "questo IP specifico gira Windows Server 2019,
                        ha la porta 3389 aperta, il certificato SSL
                        è scaduto da 6 mesi, ed è vulnerabile a
                        CVE-2021-34527 — ed ecco uno screenshot
                        del desktop RDP che Shodan ha catturato"
```

---

### Cosa fa theHarvester che Shodan non fa

```
✅ Email harvesting          → Shodan non raccoglie email
✅ Nomi dipendenti           → Shodan non va su LinkedIn
✅ GitHub recon              → Shodan non analizza repository
✅ Aggregazione veloce       → 40 fonti in un comando
✅ DNS brute force           → Shodan non fa brute force
```

### Cosa fa Shodan che theHarvester non fa

```
✅ Query precise e complesse → filtri combinati avanzati
✅ Dati di vulnerabilità     → vuln:CVE-XXXX integrato
✅ Screenshot dei servizi    → vedi il pannello di login visivamente
✅ Storico scansioni         → come era il server 6 mesi fa
✅ Pivoting avanzato         → da SSL a ASN a org a geo
✅ Alert in tempo reale      → notifica quando appaiono nuovi host
✅ Dati banner completi      → tutto quello che il servizio espone
✅ Integrazione con Metasploit, Maltego, recon-ng
```

---

### In pratica li usi in sequenza, non in alternativa

```
Step 1 — theHarvester
   → ricognizione rapida e broad
   → raccogli email, sottodomini, IP, nomi
   → 5 minuti, quadro generale

Step 2 — Shodan
   → prendi gli IP trovati da theHarvester
   → approfondisci ogni IP interessante
   → cerca vulnerabilità, servizi, screenshot
   → pivot su ASN e certificati SSL

Step 3 — nmap
   → conferma e approfondisci i risultati Shodan
   → su target autorizzato
```

> Un professionista non sceglie tra i due — li usa entrambi perché si **completano**. theHarvester è la larghezza, Shodan è la profondità.