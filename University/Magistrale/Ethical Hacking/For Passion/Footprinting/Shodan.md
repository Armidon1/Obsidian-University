## Shodan — Il Search Engine per Dispositivi

### Cos'è

Shodan è un motore di ricerca, come Google, ma invece di cercare siti web, cerca dispositivi connessi a internet — dai router e server, ai dispositivi IoT come termostati e baby monitor, fino a sistemi complessi che governano settori come energia, elettricità e trasporti.

La differenza fondamentale con Google:

```
Google  → indicizza pagine web (contenuto)
Shodan  → indicizza dispositivi (banner, porte aperte, versioni software)
```

Shodan indicizza banner di servizio, header HTTP e altri metadati dallo spazio di indirizzi IPv4 per rivelare sistemi esposti e rischi di configurazione.

---

### Come funziona

Shodan scansiona i dispositivi che rispondono su porte aperte. Quando un dispositivo risponde, Shodan raccoglie le informazioni del banner — inclusi tipo di dispositivo, sistema operativo, servizi in esecuzione e versioni software.

---

### I Filtri — Shodan Dorks

Proprio come i Google dork, gli Shodan dork sono query keyword usate per estrarre informazioni altamente specifiche dal vasto pool di dispositivi indicizzati.

```bash
# Filtri principali
hostname:microsoft.com          # dispositivi di un hostname
org:"Microsoft"                 # dispositivi di un'organizzazione
net:192.168.0.0/24              # range IP in notazione CIDR
ip:8.8.8.8                      # IP specifico
port:22                         # porta specifica
os:"Windows Server 2019"        # sistema operativo
country:IT                      # paese (codice ISO)
city:"Rome"                     # città
product:"Apache"                # software specifico
version:"2.4.41"                # versione specifica
vuln:CVE-2021-44228             # dispositivi vulnerabili a un CVE
ssl.cert.subject.cn:google.com  # certificato SSL per dominio
has_screenshot:true             # solo host con screenshot catturato
```

### Query utili combinate

```bash
# Server Apache in Italia
Apache country:IT

# SSH aperto negli USA
port:22 country:US

# MongoDB senza autenticazione ← database esposti
"MongoDB Server Information" port:27017 -authentication

# RDP esposto (vettore ransomware comune)
port:3389 country:IT

# Pannelli admin esposti
http.title:"Admin Panel"

# Telecamere IP con stream live
has_screenshot:true port:554

# Default password nei banner
"default password"

# Cisco in una subnet specifica
cisco net:211.114.3.0/24

# VPN Palo Alto esposte
GlobalProtect port:443

# Industrial Control Systems
"SCADA" port:102
```

---

### Cosa vedi per ogni risultato

Cliccando su un IP in Shodan ottieni:

```
IP: 93.184.216.34
Organization: Edgecast Inc.
Country: United States
────────────────────────────
Open Ports:
  80/tcp   HTTP   Apache/2.4.41
  443/tcp  HTTPS  Apache/2.4.41
  22/tcp   SSH    OpenSSH 8.2p1
────────────────────────────
Banner (porta 80):
  HTTP/1.1 200 OK
  Server: Apache/2.4.41 (Ubuntu)
  X-Powered-By: PHP/7.4.3
────────────────────────────
Vulnerabilities:
  CVE-2021-41773  (Apache path traversal)
  CVE-2021-42013
```

Tutto questo **senza toccare il target** — Shodan ha già fatto la scansione per te.

---

### Shodan CLI — usarlo dal terminale

```bash
# Installazione
pip install shodan --break-system-packages

# Configurazione con API key (account gratuito su shodan.io)
shodan init TUA_API_KEY

# Ricerche da terminale
shodan search "Apache country:IT"
shodan search "port:3389 country:IT" --fields ip_str,port,org

# Info su un IP specifico
shodan host 8.8.8.8

# Info sul tuo IP
shodan myip

# Conta i risultati di una query
shodan count "Apache country:IT"

# Scarica i risultati in JSON
shodan download output "Apache country:IT"
shodan parse output.json.gz
```

---

### Nel contesto del Pentesting

Shodan può essere usato per trovare nuovi host appena aggiunti alla rete di un'organizzazione, o host accidentalmente esposti e spesso dimenticati che non dovrebbero essere su internet.

Il workflow tipico in un pentest:

```
1. crt.sh          → trova i sottodomini
        │
        ▼
2. Shodan           → per ogni sottodominio/IP trovato,
                      vedi porte aperte, servioni, versioni
        │
        ▼
3. searchsploit     → cerca CVE per le versioni trovate
        │
        ▼
4. nmap             → conferma i risultati (su target autorizzato)
```

---

### Legalità

Shodan è generalmente considerato legale ed etico per la ricognizione passiva durante un penetration test — è un motore di ricerca che raccoglie informazioni pubblicamente disponibili. Tuttavia, l'interazione impropria con un sistema target senza la dovuta autorizzazione può portare ad attività illegali come lo sfruttamento di vulnerabilità o il tentativo di accedere a sistemi.

> [!warning] Trovare un sistema vulnerabile su Shodan **non ti autorizza ad attaccarlo**. La ricognizione passiva è legale. Qualsiasi interazione attiva richiede autorizzazione esplicita.

### Alternative a Shodan

|Tool|Focus|
|---|---|
|**Censys**|Simile a Shodan, più dati sui certificati|
|**FOFA**|Alternativa cinese, fingerprinting avanzato|
|**ZoomEye**|Cinese, va più in profondità nel layer applicativo|
|**Netlas**|Più recente, buon free tier|

---
# Usare Shodan nel Modo Migliore

### Il Mindset Giusto

La maggior parte dei principianti usa Shodan come un motore di ricerca normale — cerca una parola e guarda cosa esce. Questo produce risultati generici e rumorosi.

Il modo professionale è diverso:

```
❌ Approccio naive:   cercare "apache" e sperare in qualcosa di utile
✅ Approccio corretto: avere un target → costruire query precise → pivotare sui risultati
```

---

### Livello 1 — Ricerca su un Target Specifico

Parti sempre dal dominio o dall'organizzazione, non da keyword generiche.

```bash
# Per organizzazione
org:"Microsoft Corporation"
org:"Telecom Italia"

# Per hostname
hostname:microsoft.com
	hostname:.gov.it             # tutti i gov italiani

# Per IP specifico
ip:8.8.8.8

# Per range IP (CIDR)
net:216.58.200.0/24
```

Questo ti dà **solo** i risultati relativi al tuo target — niente rumore.

---

### Livello 2 — Filtrare per Servizio e Porta

```bash
# Combinazione org + porta
org:"Telecom Italia" port:22          # SSH esposti
org:"Telecom Italia" port:3389        # RDP esposti
org:"Telecom Italia" port:21          # FTP esposti

# Servizi specifici
org:"Target Corp" product:"Apache"
org:"Target Corp" product:"nginx"
org:"Target Corp" product:"Microsoft IIS"

# Versioni specifiche → cercabili su searchsploit
org:"Target Corp" product:"Apache" version:"2.4.49"
```

---

### Livello 3 — Cercare Vulnerabilità Specifiche

```bash
# Per CVE direttamente
vuln:CVE-2021-44228              # Log4Shell — tutti i sistemi vulnerabili
vuln:CVE-2021-34527              # PrintNightmare
vuln:CVE-2022-0847               # Dirty Pipe

# Combinare CVE + organizzazione
vuln:CVE-2021-44228 org:"Target Corp"
```

> [!tip] Hacking Note `vuln:` è uno dei filtri più potenti di Shodan — mostra i sistemi che Shodan ha già identificato come vulnerabili a un CVE specifico. Richiede un account a pagamento ma vale ogni centesimo.

---

### Livello 4 — Pivoting sui Risultati

Il **pivoting** è la tecnica più avanzata — usi un'informazione trovata per trovarne altre.

#### Pivot da IP → ASN → Tutti gli IP dell'organizzazione

```bash
# 1. Trovi un IP del target: 93.184.216.34
# 2. Cerchi il suo ASN su Shodan
ip:93.184.216.34                 # vedi il campo "asn"

# 3. Cerchi tutti gli IP con quell'ASN
asn:AS15133                      # tutti i server di quell'organizzazione
```

#### Pivot da Certificato SSL → Infrastruttura nascosta

```bash
# Un certificato SSL contiene il nome dell'organizzazione
# Usalo per trovare server non pubblicizzati
ssl.cert.subject.cn:"*.microsoft.com"
ssl.cert.subject.o:"Microsoft Corporation"

# Trova tutti i sottodomini nei certificati
ssl:"target.com"
```

#### Pivot da Tecnologia → Target simili

```bash
# Trovato che il target usa Cisco ASA?
# Cerca tutti i Cisco ASA nella stessa nazione
product:"Cisco ASA" country:IT

# Trovato un pannello di login specifico?
http.title:"Fortinet SSL VPN" country:IT
```

---

### Livello 5 — Query ad Alto Valore

Queste sono le query che i professionisti usano per trovare sistemi critici:

```bash
# Database esposti senza autenticazione
"MongoDB Server Information" port:27017
"Redis" port:6379 -authentication
"elasticsearch" port:9200

# Pannelli admin esposti
http.title:"Admin Panel" country:IT
http.title:"phpMyAdmin" country:IT
http.title:"Webmin" port:10000

# VPN e accesso remoto esposti
product:"GlobalProtect" country:IT       # Palo Alto VPN
http.title:"Citrix Gateway" country:IT
product:"Pulse Connect Secure" country:IT

# Dispositivi industriali (SCADA/ICS)
product:"Siemens" port:102               # Siemens S7
"SCADA" country:IT

# Telecamere senza autenticazione
"Server: yawcam" has_screenshot:true
product:"Hikvision" has_screenshot:true

# RDP esposto (vettore ransomware)
port:3389 country:IT os:"Windows Server 2019"

# Sistemi con screenshot catturati da Shodan
has_screenshot:true org:"Target Corp"    # vedi cosa è esposto visivamente
```

---

### Livello 6 — Shodan CLI per Automatizzare

La CLI è dove Shodan diventa veramente potente — puoi integrarlo in script.

```bash
# Installa
pip install shodan --break-system-packages
shodan init TUA_API_KEY

# Ricerche
shodan search "org:\"Telecom Italia\" port:22"
shodan search --fields ip_str,port,org,product "apache country:IT"

# Info su un IP specifico
shodan host 8.8.8.8

# Conta risultati senza scaricarli
shodan count "vuln:CVE-2021-44228"

# Scarica risultati in JSON
shodan download output.json "org:\"Target\" port:443"
shodan parse output.json.gz

# Alert — monitora nuovi dispositivi esposti di un'org
shodan alert create "Target Monitor" "org:\"Target Corp\""
shodan alert list
```

---

### Livello 7 — Integrazione con Altri Tool

```bash
# 1. theHarvester trova IP del target
theHarvester -d target.com -b all

# 2. Per ogni IP trovato, query Shodan
shodan host 93.184.216.34

# 3. Se Shodan trova porte aperte, scan con nmap per confermare
nmap -sV -p 80,443,22 93.184.216.34

# 4. Versione trovata → searchsploit
searchsploit Apache 2.4.49
```

---

### I Filtri Completi — Riferimento Rapido

```bash
# Geografici
country:IT
city:"Milano"
geo:"45.4654,9.1859,10"          # lat, lon, raggio in km

# Rete
port:443
net:192.168.0.0/24
asn:AS15169
ip:8.8.8.8

# Servizio
product:"Apache httpd"
version:"2.4.49"
os:"Windows Server 2019"
hostname:target.com

# Web
http.title:"Login"
http.html:"password"
http.status:200

# SSL
ssl:"target.com"
ssl.cert.subject.cn:"*.target.com"
ssl.cert.expired:true            # certificati scaduti ← spesso sistemi abbandonati

# Speciali
has_screenshot:true
vuln:CVE-2021-44228
org:"Microsoft"
before:2024-01-01                # risultati prima di una data
after:2024-01-01                 # risultati dopo una data
```

---

### L'Ordine Corretto in un Pentest

```
1. org:"Target"                          # chi sono, quanti server
2. org:"Target" has_screenshot:true      # cosa mostrano visivamente
3. org:"Target" port:22,80,443,3389      # servizi principali
4. org:"Target" ssl.cert.expired:true    # sistemi abbandonati/dimenticati
5. org:"Target" vuln:CVE-XXXX-XXXX       # vulnerabilità note (se account paid)
6. Pivota: asn → ssl → http.title        # espandi la superficie
```

> [!warning] Trovare qualcosa su Shodan non autorizza a toccarlo. Shodan è ricognizione passiva — i dati sono già stati raccolti da Shodan, non da te. Qualsiasi interazione attiva con i sistemi trovati richiede autorizzazione esplicita.