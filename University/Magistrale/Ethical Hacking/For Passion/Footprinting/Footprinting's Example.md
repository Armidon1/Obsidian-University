## OSINT su example.com — Workflow Completo

Prima cosa che abbiamo già scoperto: è **Studio Legale Nolèx**, uno studio legale con sedi a Roma, Napoli e Torino.

---

### Step 1 — DNS Recon con `dig`

```bash
# Chi sono? Qual è il loro IP?
dig example.com A +short

# Quali mail server usano?
dig example.com MX +short

# Quali name server?
dig example.com NS +short

# Record TXT — rivela i servizi che usano
dig example.com TXT +short

# Tutti i record insieme
dig example.com ANY +short
```

Il record TXT è particolarmente interessante — di solito contiene:

```
v=spf1 include:sendgrid.net ...   → usano SendGrid per le email
google-site-verification=...      → usano Google Search Console
```

---

### Step 2 — WHOIS

```bash
whois example.com
```

Cerca nei risultati:

- **Registrar** — dove è registrato il dominio
- **Name Servers** — chi gestisce il DNS
- **Registrant** — dati del proprietario (spesso nascosti da privacy shield)
- **Creation date** — da quando esiste il dominio

---

### Step 3 — Certificate Transparency

```bash
curl -s "https://crt.sh/?q=%.example.com&output=json" \
| python3 -c "
import json,sys
data=json.load(sys.stdin)
names=set()
for cert in data:
    for name in cert['name_value'].split('\n'):
        name=name.strip().lstrip('*.')
        if name and 'example.com' in name:
            names.add(name)
for n in sorted(names):
    print(n)
"
```

Questo ti mostra **tutti i sottodomini** che hanno mai avuto un certificato SSL.

---

### Step 4 — Shodan sull'IP trovato

Dopo aver preso l'IP dal `dig`, vai su `shodan.io` e cerca:

```bash
# Sostituisci con l'IP reale trovato al Step 1
ip:IP_TROVATO
```

Oppure da terminale se hai la API key:

```bash
shodan host IP_TROVATO
```

Shodan ti dirà:

- Quali porte sono aperte
- Quale web server usano (Apache, Nginx, IIS...)
- Versione del software
- Se è dietro Cloudflare o un CDN
- Certificati SSL

---

### Step 5 — theHarvester

```bash
theHarvester -d example.com -b google,bing,duckduckgo -l 200
```

Cerca email degli avvocati e sottodomini aggiuntivi.

---

### Cosa aspettarti — uno studio legale tipico

```
Probabilmente troverai:
✅ Hosting su provider italiano (Aruba, Register.it, OVH)
   oppure CDN come Cloudflare
✅ WordPress o CMS simile (molto comune per studi professionali)
✅ Google Analytics + Google Search Console (dai TXT record)
✅ Email su GSuite o Microsoft 365 (dai MX record)
✅ Certificato Let's Encrypt o Comodo

Improbabile trovare:
❌ Porte esotiche aperte
❌ Vulnerabilità gravi (è un sito vetrina, non un'app complessa)
```

---

> [!tip] Eseguilo ora Inizia con `dig example.com A +short` e dimmi l'IP che ottieni — da lì continuiamo insieme il workflow e ti mostro come interpretare ogni risultato.


Quello che abbiamo fatto è **footprinting** — la prima fase di qualsiasi penetration test o attacco informatico.

---

### Cos'è il Footprinting

Il footprinting è la raccolta **sistematica** di informazioni su un target prima di qualsiasi interazione diretta. L'obiettivo è costruire un quadro completo dell'infrastruttura senza lasciare tracce e senza violare nessuna legge.

```
Footprinting
    │
    ├── Passivo   → non tocchi mai il target
    │               crt.sh, Shodan, GHDB, WHOIS, theHarvester
    │               quello che abbiamo fatto su studionole.com ✅
    │
    └── Attivo    → interagisci direttamente col target
                    dig, nmap, ping, traceroute
                    lascia tracce nei log del target ⚠️
```

---

### Le 7 Fasi di un Penetration Test

Il footprinting è solo la **prima** di sette fasi:

```
1. FOOTPRINTING       ← siamo qui
   Raccogliere info pubbliche sul target
   Tool: dig, whois, theHarvester, Shodan, crt.sh, GHDB

2. SCANNING
   Scoprire host attivi, porte aperte, servizi
   Tool: nmap, masscan, nikto

3. ENUMERATION
   Estrarre info dettagliate dai servizi trovati
   Tool: enum4linux, gobuster, ffuf, dnsenum

4. VULNERABILITY ANALYSIS
   Identificare vulnerabilità nei servizi trovati
   Tool: nessus, openvas, searchsploit, nuclei

5. EXPLOITATION
   Sfruttare le vulnerabilità per accedere al sistema
   Tool: Metasploit, sqlmap, Burp Suite

6. POST-EXPLOITATION
   Mantenere l'accesso, escalare i privilegi, pivotare
   Tool: Meterpreter, LinPEAS, socat, mimikatz

7. REPORTING
   Documentare tutto, proporre remediation
   Tool: Obsidian, Cherry Tree, report scritto
```

---

### Quello che hai già studiato — mappato sulle fasi

```
Footprinting     → dig, whois, crt.sh, Shodan, theHarvester, GHDB  ✅
Scanning         → nmap  ✅
Post-Exploitation → SUID/SGID, privesc, socat, netcat  ✅
Anonymity        → Tor, Privoxy, Proxychains  ✅
```

Hai già coperto più di quanto pensi — le fondamenta sono solide.

> [!tip] Il passo naturale adesso sarebbe approfondire la fase 3 — **Enumeration** — con tool come `gobuster` per trovare directory nascoste e `nikto` per analizzare il web server. È il ponte tra il footprinting che hai imparato e l'exploitation che verrà dopo.