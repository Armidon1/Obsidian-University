# WHOIS — Domain & IP Intelligence

#linux #cybersecurity #osint #footprinting #dns #linux-basics-for-hackers

---

## 🗂️ Overview

**WHOIS** è un protocollo di query/risposta che permette di recuperare informazioni su chi possiede un dominio o un blocco di indirizzi IP. È uno dei primi strumenti usati nel footprinting — risponde alla domanda fondamentale: **"chi c'è dietro questo dominio o questo IP?"**

```
whois example.com   → chi possiede il dominio
whois 93.184.216.34 → chi possiede questo IP
```

nota: spesso non si trovano tutte le informazioni necessarie perché l'unione europea ha censurato determinati valori per privacy. In tal caso si può suare il comando 
```bash
curl -s https://studionole.com | grep -i "email\|telefono\|contatti\|p.iva\|partita"
```

---

## 🏛️ I Tre R — Fondamenta del Sistema

Ogni query WHOIS ruota attorno a tre attori:

```
Registry    → database autoritativo del TLD
              "Verisign possiede il db di .com"

Registrar   → intermediario accreditato ICANN
              "GoDaddy ha venduto example.com"

Registrant  → il proprietario del dominio
              "Mario Rossi possiede example.com"
              (nascosto dal GDPR dal 2018)
```

---

## 🛠️ Installazione e Uso Base

```bash
# Pre-installato su Kali/Parrot/Debian
whois --version

# Se non presente
sudo apt install whois -y
```

---

## 📋 Sintassi e Opzioni

```bash
# Uso base
whois example.com              # WHOIS del dominio
whois 93.184.216.34            # WHOIS dell'IP
whois -h whois.iana.org com    # query su server specifico
whois AS15169                  # WHOIS di un ASN (Google)

# Il client riconosce automaticamente:
# → se è un dominio → contatta il Registry del TLD
# → se è un IP     → contatta il RIR corretto (ARIN/RIPE/APNIC...)
# → se è un ASN    → recupera info sull'autonomous system
```

---

## 📖 Leggere l'Output — Campo per Campo

```bash
whois example.com
```

```
# ── REGISTRY SECTION ──────────────────────────────
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
   → ID univoco nel database Verisign

Updated Date: 2024-08-14T07:01:44Z
   → ultima modifica al record (cambio NS, rinnovo ecc.)

Creation Date: 1995-08-14T04:00:00Z
   → quando è stato registrato per la prima volta
   → dominio vecchio = organizzazione consolidata
   → dominio recente = possibile phishing/typosquatting

Registry Expiry Date: 2025-08-13T04:00:00Z
   → quando scade → possibile domain hijacking se dimentica

# ── REGISTRAR SECTION ─────────────────────────────
Registrar: ICANN
Registrar WHOIS Server: whois.iana.org
Registrar URL: http://www.iana.org
   → chi ha venduto il dominio
   → WHOIS server del Registrar per più dettagli

# ── REGISTRANT SECTION (pre-GDPR) ─────────────────
Registrant Name: REDACTED FOR PRIVACY      ← nascosto GDPR
Registrant Email: REDACTED FOR PRIVACY     ← nascosto GDPR
Registrant Phone: REDACTED FOR PRIVACY     ← nascosto GDPR
Registrant Address: REDACTED FOR PRIVACY   ← nascosto GDPR

# ── ABUSE CONTACT (sempre visibile per legge) ──────
Registrar Abuse Contact Email: abuse@registrar.com
Registrar Abuse Contact Phone: +1.4805058800
   → unico contatto non nascosto dal GDPR
   → obbligatorio per legge

# ── NAMESERVERS ────────────────────────────────────
Name Server: A.IANA-SERVERS.NET
Name Server: B.IANA-SERVERS.NET
   → chi gestisce il DNS del dominio
   → Cloudflare NS → sito protetto da CDN
   → NS proprietari → infrastruttura interna

# ── DNSSEC ─────────────────────────────────────────
DNSSEC: unsigned
   → nessuna firma crittografica DNS
   → vulnerabile a DNS spoofing
```

---

## 🌐 WHOIS su Indirizzi IP — I 5 RIR

Per gli IP il client whois contatta automaticamente il **Regional Internet Registry** corretto:

|RIR|Zona geografica|IP di esempio|
|---|---|---|
|**ARIN**|Nord America|8.8.8.8 (Google USA)|
|**RIPE NCC**|Europa, Medio Oriente, Asia Centrale|185.x.x.x|
|**APNIC**|Asia Pacifico|61.0.0.2 (India)|
|**LACNIC**|America Latina|177.x.x.x|
|**AFRINIC**|Africa|196.x.x.x|

```bash
# WHOIS su IP europeo → va automaticamente su RIPE
whois 185.42.13.7

# WHOIS su IP americano → va automaticamente su ARIN
whois 8.8.8.8

# WHOIS su ASN → mostra il range IP dell'organizzazione
whois AS15169           # Google
whois AS8075            # Microsoft
whois AS16509           # Amazon AWS

# Cercare il RIR di un IP specifico
whois -h whois.iana.org 61.0.0.2
```

### Cosa trovi nel WHOIS di un IP

```bash
whois 8.8.8.8
```

```
NetRange:       8.8.8.0 - 8.8.8.255
CIDR:           8.8.8.0/24
NetName:        LVLT-GOGL-8-8-8
Organization:   Google LLC (GOGL)
RegDate:        2014-03-14
Country:        US
OrgAbuseEmail:  network-abuse@google.com
OrgTechEmail:   arin-contact@google.com
```

---

## 🔍 Grep — Estrarre Solo Quello che Serve

```bash
# Scadenza del dominio
whois example.com | grep -i "expir"

# Nameserver
whois example.com | grep -i "name server"

# Registrar
whois example.com | grep -i "registrar"

# Data di creazione
whois example.com | grep -i "creation"

# Abuse contact (sempre visibile)
whois example.com | grep -i "abuse"

# Tutto ciò che non è REDACTED
whois example.com | grep -v "REDACTED"

# Solo le righe con contenuto (no righe vuote)
whois example.com | grep -v "^$" | grep -v "REDACTED"

# WHOIS su IP — organizzazione
whois IP | grep -iE "Organization|OrgName|NetName|Country"
```

---

## 🔗 Integrazione con Tool Moderni

### 1. Shodan — IP Lookup Approfondito

Quando WHOIS ti dà l'IP, Shodan ti dice cosa gira su quell'IP:

```bash
# Step 1 — trova l'IP con whois o dig
dig example.com A +short
# → 93.184.216.34

# Step 2 — approfondisci con Shodan
shodan host 93.184.216.34

# Oppure cerca per organizzazione trovata nel WHOIS
shodan search org:"Google LLC"
shodan search org:"Amazon Technologies" port:22
```

**Cosa aggiunge Shodan al WHOIS:**

```
WHOIS dice:   "questo IP è di Amazon"
Shodan dice:  "su questo IP girano:
               porta 80  → Apache 2.4.52
               porta 443 → Apache 2.4.52 + TLS 1.3
               porta 22  → OpenSSH 8.2p1
               screenshot del sito disponibile
               vulnerabile a CVE-2021-41773"
```

---

### 2. SecurityTrails — WHOIS Storico pre-GDPR

SecurityTrails conserva snapshot storici del WHOIS — prima che il GDPR nascondesse i dati. Spesso i dati del Registrant sono ancora visibili nelle versioni precedenti al 2018.

```
https://securitytrails.com/domain/example.com/history/whois
```

**Cosa trovi:**

```
WHOIS 2016-03-14:
  Registrant: Mario Rossi
  Email: mario.rossi@gmail.com    ← visibile pre-GDPR
  Phone: +39 02 1234567
  Address: Via Roma 1, Milano

→ email trovata → cerca su HaveIBeenPwned
→ cerca username "mario.rossi" con Sherlock
→ cerca "mario.rossi@gmail.com" su GHDB
```

**Da terminale con API:**

```bash
# SecurityTrails API (richiede account gratuito)
curl -s "https://api.securitytrails.com/v1/domain/example.com/whois" \
  -H "apikey: TUA_API_KEY" | python3 -m json.tool
```

---

### 3. DomainTools — Intelligence Avanzata

DomainTools è il più completo ma a pagamento. Offre:

```
→ WHOIS storico completo (tutti gli anni)
→ Reverse WHOIS: "chi ha registrato domini con questa email?"
→ Connessioni tra domini dello stesso proprietario
→ Risk score del dominio
→ Screenshot storici del sito
```

**Reverse WHOIS — il caso d'uso più potente:**

```
Trovi email: mario.rossi@gmail.com nel WHOIS storico
        │
        ▼
DomainTools Reverse WHOIS:
"quanti altri domini ha registrato con questa email?"
        │
        ▼
Risultato: 47 domini registrati
  → malicious.com
  → phishing-bank.net
  → fakeshop.org
  → ...
```

**Alternativa gratuita parziale:**

```bash
# ViewDNS.info — reverse whois gratuito limitato
curl "https://viewdns.info/reversewhois/?q=mario.rossi@gmail.com"
```

---

### 4. Workflow Completo — Tutto Insieme

```bash
# ════════════════════════════════════════════
# TARGET: example.com
# ════════════════════════════════════════════

# Step 1 — WHOIS base
whois example.com | grep -v "REDACTED" | grep -v "^$"

# Step 2 — Estrai info chiave
DOMAIN_IP=$(dig example.com A +short)
REGISTRAR=$(whois example.com | grep -i "Registrar:" | head -1)
CREATION=$(whois example.com | grep -i "Creation Date" | head -1)
EXPIRY=$(whois example.com | grep -i "Expiry\|Expiration" | head -1)
NS=$(whois example.com | grep -i "Name Server")
ABUSE=$(whois example.com | grep -i "abuse")

echo "IP: $DOMAIN_IP"
echo "$REGISTRAR"
echo "$CREATION"
echo "$EXPIRY"
echo "$NS"
echo "$ABUSE"

# Step 3 — WHOIS sull'IP trovato
whois $DOMAIN_IP | grep -iE "Organization|NetName|Country|CIDR"

# Step 4 — ASN dell'organizzazione
whois $DOMAIN_IP | grep -i "OriginAS"
# → AS15169 → whois AS15169 per vedere tutto il range IP

# Step 5 — Shodan sull'IP
shodan host $DOMAIN_IP 2>/dev/null || \
  echo "Cerca su https://shodan.io/host/$DOMAIN_IP"

# Step 6 — Storico su SecurityTrails
echo "Controlla: https://securitytrails.com/domain/example.com/history/whois"

# Step 7 — Certificati SSL (sottodomini)
curl -s "https://crt.sh/?q=%.example.com&output=json" \
| python3 -c "
import json,sys
data=json.load(sys.stdin)
names=set()
for cert in data:
    for name in cert['name_value'].split('\n'):
        name=name.strip().lstrip('*.')
        if name: names.add(name)
for n in sorted(names): print(n)
"
```

---

## ⚠️ WHOIS e GDPR — Lo Stato Attuale

```
Prima del 2018 (GDPR):
✅ Nome e cognome del proprietario
✅ Email personale
✅ Numero di telefono
✅ Indirizzo fisico
✅ Contatto tecnico e amministrativo

Dopo il 2018 (GDPR):
❌ REDACTED per tutti i dati personali
✅ Data di creazione e scadenza
✅ Registrar
✅ Nameserver
✅ Abuse contact (obbligatorio per legge)
✅ DNSSEC status
```

**Eccezioni — dati ancora visibili:**

```bash
# 1. Organizzazioni (non persone fisiche)
# Le aziende spesso non sono coperte dal GDPR
whois amazon.com | grep -i "Registrant"
# → "Amazon Technologies Inc." spesso visibile

# 2. ccTLD con regole proprie
# .us non applica il GDPR
whois example.us

# 3. WHOIS storico su SecurityTrails/DomainTools
# snapshot pre-2018 ancora accessibili

# 4. Abuse contact — sempre visibile
whois example.com | grep -i "abuse"
```

---

## 🕵️ Tecniche Avanzate

### Domain Expiry Monitoring

```bash
# Controlla quando scade un dominio target
whois example.com | grep -i "expir"

# Se scade presto → potenziale domain hijacking
# Il dominio entra in:
# 1. Grace Period (30gg) → il proprietario può ancora rinnovare
# 2. Redemption Period (30gg) → solo il proprietario con penale
# 3. Released → chiunque può registrarlo
```

### Reverse IP — Altri Domini sullo Stesso Server

```bash
# Trova altri domini sullo stesso IP
# (shared hosting → molti siti sullo stesso server)
curl "https://viewdns.info/reverseip/?host=93.184.216.34&t=1"

# Oppure con dig reverse
dig -x 93.184.216.34 +short
```

### ASN Lookup — Tutto il Range IP di un'Organizzazione

```bash
# Trova l'ASN dal WHOIS dell'IP
whois 20.112.52.29 | grep "OriginAS"
# → AS8075

# Tutti gli IP di Microsoft
whois AS8075

# Cerca tutti questi IP su Shodan
shodan search asn:AS8075
```

---

## 📊 WHOIS vs Tool Moderni — Confronto

|                        | whois    | Shodan    | SecurityTrails | DomainTools |
| ---------------------- | -------- | --------- | -------------- | ----------- |
| **Dati registrazione** | ✅        | ❌         | ✅ storico      | ✅ completo  |
| **Dati registrant**    | ❌ GDPR   | ❌         | ✅ pre-2018     | ✅ storico   |
| **Porte e servizi**    | ❌        | ✅         | ❌              | ❌           |
| **Sottodomini**        | ❌        | Parziale  | ✅              | ✅           |
| **Storico DNS**        | ❌        | ❌         | ✅              | ✅           |
| **Reverse WHOIS**      | ❌        | ❌         | Parziale       | ✅           |
| **Costo**              | Gratuito | Free/Paid | Free/Paid      | Paid        |
| **Velocità**           | ⚡        | ⚡         | 🟡             | 🟡          |

---

## 🔗 Command Cheat Sheet

```bash
# Base
whois example.com                              # dominio
whois 93.184.216.34                            # IP
whois AS15169                                  # ASN

# Filtri utili
whois example.com | grep -i "expir"            # scadenza
whois example.com | grep -i "name server"      # NS
whois example.com | grep -i "registrar"        # registrar
whois example.com | grep -i "abuse"            # abuse contact
whois example.com | grep -v "REDACTED"         # solo dati visibili
whois IP | grep -iE "Org|NetName|Country|CIDR" # info IP

# Server specifici
whois -h whois.iana.org com                    # TLD .com
whois -h whois.ripe.net 185.42.13.7            # RIPE diretto
whois -h whois.arin.net 8.8.8.8               # ARIN diretto
whois -h whois.nic.it example.it               # .it diretto

# Integrazione
dig example.com A +short                       # IP → poi whois sull'IP
shodan host $(dig example.com A +short)        # Shodan sull'IP
curl "https://securitytrails.com/domain/example.com/history/whois"
```

---

## 🔗 Related Notes

- [[Top Level Domain (TLD)]]
- [[Dig]]
- [[Shodan]]
- [[OSINT]]
- [[theHarvester]]
- [[LinuxCommands/Nmap]]

---

_References: https://www.iana.org/whois · https://who.is · https://securitytrails.com · https://domaintools.com · Hacking Exposed 7 — McClure, Scambray, Kurtz · Linux Basics for Hacking — OccupyTheWeb_