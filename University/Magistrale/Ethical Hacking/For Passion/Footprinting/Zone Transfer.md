# Zone Transfer — `dig AXFR`

---

### Cos'è

Lo **zone transfer** è un meccanismo legittimo del DNS che permette a un nameserver secondario di **copiare tutti i record DNS** da un nameserver primario — per sincronizzare le informazioni e garantire ridondanza.

```
NS Primario  →  "ecco tutti i record della zona"  →  NS Secondario
             ←────────────── AXFR ───────────────←
```

In un contesto legittimo serve per avere più nameserver sincronizzati. In un contesto di hacking è una **miniera d'oro** — se mal configurato espone tutta l'infrastruttura DNS del target.

---

### Perché è Pericoloso

Quando funziona su un target, ottieni **tutti i record DNS** in un colpo solo:

```
mail.example.com      → 10.0.0.5    ← mail server interno
vpn.example.com       → 10.0.0.9    ← VPN esposta
dev.example.com       → 10.0.0.12   ← ambiente di sviluppo
staging.example.com   → 10.0.0.15   ← staging con dati reali
admin.example.com     → 10.0.0.20   ← pannello admin
db.example.com        → 10.0.0.25   ← database server
backup.example.com    → 10.0.0.30   ← server di backup
internal.example.com  → 192.168.1.1 ← rete interna!
```

Tutto questo senza toccare nessun server — è una query DNS legittima.

---

### Come Farlo

```bash
# Step 1 — trova i nameserver del target
dig example.com NS +short
# → a.iana-servers.net
# → b.iana-servers.net

# Step 2 — tenta il zone transfer su ogni NS
dig @a.iana-servers.net example.com AXFR
dig @b.iana-servers.net example.com AXFR

# Sintassi alternativa
dig AXFR example.com @a.iana-servers.net

# Con nslookup (metodo del libro)
nslookup
> server a.iana-servers.net
> set type=AXFR
> example.com
```

---

### Le Due Risposte Possibili

**Server ben configurato — risposta attesa oggi:**

```
; <<>> DiG 9.18 <<>> @a.iana-servers.net example.com AXFR
;; communications error to 199.43.135.53#53: end of file
;; no servers could be reached
```

oppure:

```
; Transfer failed.
; AXFR not allowed
```

**Server mal configurato — jackpot:**

```
example.com.     SOA   ns1.example.com. admin.example.com. (
                       2024010101 ; serial
                       3600       ; refresh
                       900        ; retry
                       604800     ; expire
                       300 )      ; minimum TTL

example.com.     NS    ns1.example.com.
example.com.     NS    ns2.example.com.
example.com.     A     93.184.216.34
www              A     93.184.216.34
mail             A     10.0.0.5
vpn              A     10.0.0.9       ← trovato!
dev              A     10.0.0.12      ← trovato!
admin            A     10.0.0.20      ← trovato!
```

---

### AXFR vs IXFR

Il libro parla di AXFR ma esiste anche IXFR:

```
AXFR  → Full Zone Transfer
         copia TUTTI i record della zona
         usato per la sincronizzazione iniziale

IXFR  → Incremental Zone Transfer
         copia solo le modifiche dall'ultimo transfer
         più efficiente per aggiornamenti frequenti
         introdotto dopo il libro
```

```bash
# Tenta trasferimento incrementale
dig @ns1.example.com example.com IXFR=2024010100
#                                         ↑
#                              numero seriale dall'ultima sync
```

---

### Nel Contesto del 2026

Come il WHOIS, anche lo zone transfer è stato progressivamente bloccato:

```
2012 (Hacking Exposed era):
→ molti server permettevano AXFR a chiunque
→ era un vettore di recon molto comune

2026:
→ quasi tutti i server bloccano AXFR
→ Cloudflare, AWS Route53, Google DNS
  non lo permettono per design
→ rimane utile su:
  → target con DNS self-hosted e vecchio
  → server configurati da sysadmin inesperti
  → reti interne durante un pentest
  → ambienti di test e CTF
```

---

### Alternative Moderne allo Zone Transfer

Quando AXFR è bloccato si usano questi metodi per ottenere gli stessi risultati:

```bash
# 1. Certificate Transparency ← il più efficace oggi
curl -s "https://crt.sh/?q=%.example.com&output=json" \
| python3 -c "
import json,sys
[print(n.strip().lstrip('*.'))
 for c in json.load(sys.stdin)
 for n in c['name_value'].split('\n')
 if 'example.com' in n]"

# 2. DNS brute force con wordlist
# dnsenum
dnsenum --dnsserver ns1.example.com \
        --enum example.com \
        -f /usr/share/wordlists/dnsmap.txt

# fierce
fierce --domain example.com

# 3. theHarvester
theHarvester -d example.com -b all

# 4. Shodan — cerca sottodomini nei certificati SSL
# ssl.cert.subject.cn:"*.example.com"
```

---

### Nella Rete Interna — Ancora Utile

Durante un pentest interno, dopo aver ottenuto accesso alla rete, lo zone transfer diventa di nuovo molto utile:

```bash
# Nella rete interna i DNS interni spesso permettono AXFR
# tra i server per sincronizzazione

# Trova il DNS server interno
cat /etc/resolv.conf
# → nameserver 10.0.0.1

# Tenta AXFR sul DNS interno
dig @10.0.0.1 internal.company.lan AXFR

# Se funziona → mappa completa della rete interna
# tutti gli hostname, tutti gli IP, tutta la topologia
```

> [!tip] Per l'esame il professore probabilmente si aspetta la descrizione classica di Hacking Exposed — AXFR come tecnica di recon, `nslookup` o `dig AXFR` come tool, e la spiegazione di cosa rivela. Aggiungi una riga sul fatto che oggi è quasi sempre bloccato e che crt.sh è l'alternativa moderna — dimostra che conosci sia la teoria classica che la pratica attuale.

---
##  quindi, supponiamo che io voglia creare una web app, ho il server a casa mia, compro un dominio da aruba e da lì decido che www.miodominio.com è l'indirizzo IP statico del mio PC. inoltre decido di comprare un raspberryPi e metto l'indirizzo Ip esterno di tale raspberryPI per la vpn in vpn.miodominio.com. giusto?

Sì, hai capito perfettamente il meccanismo.

### Il Setup che Descrivi

```
miodominio.com          ← comprato da Aruba
        │
        ├── www.miodominio.com  → 151.x.x.x  (IP del tuo PC)
        │                                      server web a casa
        │
        └── vpn.miodominio.com  → 151.x.x.y  (IP del Raspberry Pi)
                                               o stesso IP con porta diversa
```

---

### Un Dettaglio Importante — IP Esterno

Probabilmente hai **un solo IP esterno** assegnato dal tuo ISP — quello del router di casa. Quindi:

```
Router di casa → IP esterno: 151.x.x.x
        │
        ├── PC (server web)      → IP interno 192.168.1.10
        └── Raspberry Pi (VPN)   → IP interno 192.168.1.20

DNS:
www.miodominio.com → 151.x.x.x  (stesso IP esterno)
vpn.miodominio.com → 151.x.x.x  (stesso IP esterno)
```

Come distingui il traffico? Con il **port forwarding** sul router:

```
Traffico in arrivo su porta 80/443  → gira al PC       (192.168.1.10)
Traffico in arrivo su porta 1194    → gira al RPi       (192.168.1.20)
                                       (porta standard OpenVPN)
```

---

### Il Setup Completo e Realistico

```
Internet
    │
    ▼
Router (IP esterno: 151.x.x.x)
    │
    │ port forwarding
    ├── :80  / :443  ──────→ PC 192.168.1.10     (web server)
    └── :1194         ──────→ RPi 192.168.1.20    (VPN server)

DNS su Aruba:
www.miodominio.com   A   151.x.x.x
vpn.miodominio.com   A   151.x.x.x   ← stesso IP, porta diversa
```

---

### Il Problema del IP Dinamico

Il tuo ISP probabilmente ti assegna un IP **dinamico** — cambia periodicamente:

```
Oggi:    151.x.x.x
Domani:  151.x.x.y  ← DNS non aggiornato → sito irraggiungibile
```

**Soluzione — DDNS dinamico tramite Aruba o script:**

```bash
# Aruba offre API per aggiornare i record DNS
# Il router o il Raspberry Pi controlla periodicamente l'IP
# e aggiorna il record A automaticamente

# Script semplice sul Raspberry Pi
#!/bin/bash
CURRENT_IP=$(curl -s https://api.ipify.org)
SAVED_IP=$(cat /var/tmp/last_ip)

if [ "$CURRENT_IP" != "$SAVED_IP" ]; then
    # aggiorna il record DNS via API Aruba
    echo "IP cambiato: $CURRENT_IP"
    echo $CURRENT_IP > /var/tmp/last_ip
fi
```

---

### Cosa Vede un Attaccante che Fa Footprinting su di Te

Tornando al cybersecurity — ecco cosa troverebbe:

```bash
dig www.miodominio.com A +short
→ 151.x.x.x

dig vpn.miodominio.com A +short
→ 151.x.x.x

whois 151.x.x.x
→ Organization: Telecom Italia / Fastweb / ecc.
→ "questo è un IP residenziale"
→ dietro c'è una rete domestica

# Shodan sull'IP
shodan host 151.x.x.x
→ porta 80   aperta  → web server
→ porta 443  aperta  → HTTPS
→ porta 1194 aperta  → OpenVPN ← sa che hai una VPN
```

---

### In Sintesi

```
Hai capito correttamente:
✅ Un dominio → controllo completo dei record DNS
✅ Sottodomini diversi per servizi diversi
✅ Stesso IP esterno → port forwarding differenzia i servizi
✅ Il DNS è solo un puntatore — l'hardware è a casa tua

Unica cosa da gestire:
⚠️ IP dinamico → DDNS o IP statico dal ISP
⚠️ Tutto è visibile nel DNS pubblico
⚠️ Shodan vede le porte aperte sul tuo IP
```

> [!tip] Questo setup è esattamente quello che fanno molti developer e homelabber. Si chiama **self-hosting** ed è un ottimo modo per imparare networking, DNS, sicurezza e Linux in modo pratico. Il Raspberry Pi come VPN server con WireGuard o OpenVPN è uno dei progetti più comuni della community homelab.