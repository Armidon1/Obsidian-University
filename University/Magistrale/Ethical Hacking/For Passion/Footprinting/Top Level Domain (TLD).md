# Top Level Domain (TLD)

#linux #cybersecurity #networking #dns #osint #linux-basics-for-hackers

---

## 🗂️ Overview

Il **Top Level Domain (TLD)** è l'ultima parte di un nome di dominio — quello che segue l'ultimo punto. È la radice della gerarchia DNS e determina sotto quale [[Registry]] e giurisdizione si trova un dominio.

```
www   .   example   .   com
 │            │           │
prefisso   dominio      TLD
(www)     secondo      (Top Level Domain)
           livello
```

La gerarchia completa DNS è:

```
. (root)
└── com (TLD)
    └── example (Second Level Domain)
        └── www (subdomain)
```

---

## 📂 Categorie di TLD

### 1. gTLD — Generic Top Level Domain

Non legati a nessuna nazione — i più diffusi al mondo:

|TLD|Significato originale|Uso reale|
|---|---|---|
|`.com`|Commercial|Tutto — il più usato in assoluto|
|`.org`|Organization|No-profit, community, open source|
|`.net`|Network|Provider, infrastrutture, tool|
|`.edu`|Education|Solo istituzioni accademiche USA|
|`.gov`|Government|Solo enti governativi USA|
|`.mil`|Military|Solo militare USA|
|`.int`|International|Solo organizzazioni internazionali (ONU ecc.)|
|`.info`|Information|Siti informativi|
|`.biz`|Business|Commerciale alternativo a .com|

---

### 2. ccTLD — Country Code Top Level Domain

Due lettere ISO, legati a una nazione specifica:

```
.it   → Italia          (gestito da Registro.it — IIT-CNR, Pisa)
.de   → Germania        (DENIC)
.fr   → Francia         (AFNIC)
.uk   → Regno Unito     (Nominet)
.es   → Spagna          (Red.es)
.ru   → Russia          (RU-CENTER)
.cn   → Cina            (CNNIC)
.us   → Stati Uniti     (NeuStar)
.jp   → Giappone        (JPRS)
.br   → Brasile         (Registro.br)
.au   → Australia       (auDA)
```

**ccTLD usati come brand (non per nazione):**

```
.io   → British Indian Ocean Territory
        usatissimo da startup tech e tool
        (GitHub, Replit, Shodan...)

.ai   → Anguilla (isola caraibica)
        usato da aziende di Artificial Intelligence

.tv   → Tuvalu (isola del Pacifico)
        usato da piattaforme video e streaming

.me   → Montenegro
        usato per siti personali/portfolio

.co   → Colombia
        usato come alternativa a .com
        attenzione: spesso usato per phishing
```

---

### 3. New gTLD — Dal 2013

ICANN ha aperto la registrazione di TLD personalizzati — oggi esistono oltre 1500 TLD:

```
# Tech e sviluppo
.dev        → sviluppatori (registry Google)
.app        → applicazioni (registry Google)
.tech       → tecnologia
.cloud      → servizi cloud
.software   → software

# Professioni
.legal      → studi legali
.law        → avvocati
.dental     → dentisti
.doctor     → medici
.bank       → banche (molto restrittivo)
.academy    → scuole e formazione

# E-commerce
.shop       → negozi online
.store      → negozi online
.market     → marketplace

# Altro
.ninja      → usato in modo creativo
.wtf        → esiste davvero
.pizza      → esiste davvero
.onion      → caso speciale: dark web (Tor)
```

---

## 🏛️ Chi Gestisce i TLD — La Gerarchia

```
ICANN (Internet Corporation for Assigned Names and Numbers)
    → organismo internazionale che coordina tutto il sistema DNS
    → approva i nuovi TLD
    → stabilisce le regole
         │
         ▼
Registry (uno per TLD)
    → gestisce il database di tutti i domini per quel TLD
    → .com → Verisign
    → .org → Public Interest Registry
    → .it  → Registro.it (IIT-CNR, Pisa)
    → .de  → DENIC
         │
         ▼
Registrar (migliaia)
    → vendono i domini agli utenti finali
    → GoDaddy, Namecheap, Aruba, Register.it,
      Google Domains, OVH, Cloudflare...
         │
         ▼
Registrant
    → chi possiede il dominio
```

---

## 🔍 TLD e DNS — Come Si Collegano

Quando fai `dig example.com A` il sistema passa attraverso i TLD server:

```
1. Il tuo resolver chiede ai Root Server
   "chi gestisce .com?"

2. Root Server risponde:
   "i TLD server di Verisign"
   → a.gtld-servers.net (192.5.6.30)
   → b.gtld-servers.net ... (13 in totale)

3. Il resolver chiede al TLD server Verisign
   "chi gestisce example.com?"

4. TLD server risponde:
   "i name server autoritativi"
   → a.iana-servers.net
   → b.iana-servers.net

5. Il resolver chiede al NS autoritativo
   "qual è l'IP di example.com?"

6. NS risponde: 93.184.216.34 ✅
```

```bash
# Vedere i TLD server di .com
dig com NS +short

# Vedere i TLD server di .it
dig it NS +short

# Vedere i TLD server di .org
dig org NS +short

# Query diretta al TLD server
dig @a.gtld-servers.net example.com NS
```

---

## 🕵️ TLD nel Footprinting e OSINT

### Un'organizzazione può avere TLD multipli

```bash
# Controlla tutti i TLD di example
for tld in com org net io it de fr uk; do
    result=$(dig example.$tld A +short 2>/dev/null)
    if [ -n "$result" ]; then
        echo "example.$tld → $result"
    fi
done
```

Ognuno può avere infrastruttura diversa, configurazione diversa, vulnerabilità diverse.

---

### Typosquatting — TLD usati per attacchi

Attaccanti registrano domini simili al target per ingannare gli utenti:

```
example.com       → sito legittimo
examp1e.com       → typosquatting (1 al posto della l)
example.net       → potrebbe essere squattato
example.co        → visivamente simile a .com
example-login.com → phishing
secure-example.com → phishing
```

```bash
# Verifica quali varianti sono già registrate
whois example.net
whois example.co
whois example.org
```

---

### TLD e Giurisdizione Legale

Il TLD determina sotto quale legge si trova il dominio:

```
.com / .net / .org  → giurisdizione USA (ICANN/Verisign)
                      più difficile da sequestrare
                      per governi europei

.it                 → giurisdizione italiana
                      soggetto a leggi italiane
                      GDPR obbligatorio
                      registrazione richiede dati verificati
                      sequestro più facile da autorità IT

.ru                 → giurisdizione russa
                      praticamente fuori portata
                      delle autorità occidentali

.onion              → nessuna giurisdizione
                      accessibile solo via Tor
                      nessun registry centrale
```

> [!tip] Hacking Note I cybercriminali scelgono accuratamente il TLD dei loro domini in base alla giurisdizione — `.ru`, `.cn` o TLD di paesi con scarsa cooperazione internazionale rendono il takedown molto più difficile.

---

### `.onion` — Il TLD Speciale

`.onion` non è un TLD ICANN — è uno **pseudo-TLD** riconosciuto solo dalla rete Tor:

```
Caratteristiche:
→ Non registrabile su nessun registry
→ Generato crittograficamente dalla chiave pubblica del server
→ Accessibile solo tramite Tor Browser o proxychains+tor
→ Garantisce anonimità sia per client che per server
→ Nessuna geolocalizzazione possibile dell'IP

Esempio reale:
facebookwkhpilnemxj7ascrwwwg5yvmrygmwlnhqopxqyyzxpqxrknyd.onion
→ Facebook accessibile via Tor
```

---

## 🔗 Comandi Utili

```bash
# Struttura base
dig example.com A +short            # IP del dominio
dig example.com NS +short           # name server
dig example.com MX +short           # mail server
dig example.com TXT +short          # record TXT

# TLD server
dig com NS +short                   # NS del TLD .com
dig it NS +short                    # NS del TLD .it
dig @a.gtld-servers.net example.com # query diretta al TLD

# WHOIS del dominio
whois example.com                   # info registrazione

# WHOIS del TLD (chi gestisce .com)
whois -h whois.iana.org com

# Controlla più TLD dello stesso nome
for tld in com org net io it de fr; do
    result=$(dig example.$tld A +short 2>/dev/null)
    [ -n "$result" ] && echo "example.$tld → $result"
done

# Zone transfer sul TLD (quasi sempre bloccato)
dig @a.gtld-servers.net example.com AXFR

# DNSSEC
dig example.com DS +short           # delegation signer
dig example.com DNSKEY +short       # chiavi DNSSEC
```

---

## 📊 Tabella Riepilogativa

|Tipo|Esempio|Registry|Restrizioni|Anonimato|
|---|---|---|---|---|
|gTLD classico|`.com`|Verisign|Nessuna|Possibile|
|gTLD riservato|`.gov`|GSA (USA)|Solo enti USA|No|
|ccTLD nazionale|`.it`|Registro.it|Dati verificati|Basso|
|ccTLD brand|`.io`|ICB|Nessuna|Possibile|
|New gTLD|`.dev`|Google|Nessuna|Possibile|
|Pseudo-TLD|`.onion`|Nessuno|Nessuna|Massimo|

---

## 🔗 Related Notes

- [[DNS Reconnaissance — dig]]
- [[OSINT & Footprinting]]
- [[Tor]]
- [[LinuxCommands/Nmap]]
- [[GHDB_Google_Hacking_Database]]

---

_References: https://www.iana.org/domains/root/db · https://www.icann.org · https://registro.it · Linux Basics for Hacking — OccupyTheWeb_