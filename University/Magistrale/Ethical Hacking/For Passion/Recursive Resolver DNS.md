# Recursive Resolver DNS

#linux #cybersecurity #networking #dns #linux-basics-for-hackers

---

## 🗂️ Overview

Il **Recursive Resolver** (o resolver ricorsivo, o full-service resolver) è il server DNS che fa il **lavoro pesante** — quando lo stub resolver gli chiede di risolvere un dominio, lui naviga autonomamente tutta la gerarchia DNS fino a trovare la risposta.

È chiamato "ricorsivo" perché **itera attraverso più livelli** della gerarchia DNS per conto del client, restituendo solo la risposta finale.

```
Stub Resolver (tuo PC)
      │ "risolvimi example.com"
      ▼
Recursive Resolver     ← fa tutto il lavoro
      │
      ├── chiede ai Root Server
      │       ▼
      ├── chiede ai TLD Server (.com)
      │       ▼
      ├── chiede al NS Autoritativo
      │       ▼
      └── risponde allo Stub Resolver
          "93.184.216.34"
```

→ Vedi [[Stub_Resolver]] per capire chi gli fa le domande

---

## 🔄 Il Processo Passo per Passo

### Esempio: risolvere `www.example.com`

```
STUB RESOLVER → "risolvimi www.example.com"
                        │
                        ▼
RECURSIVE RESOLVER — controlla la cache
                        │
               ┌────────┴────────┐
            Cache HIT         Cache MISS
               │                  │
               ▼                  ▼
          risponde           inizia la ricerca
          subito             iterativa
                                  │
                        ┌─────────▼──────────┐
                        │   ROOT SERVER      │
                        │ (uno dei 13 root)  │
                        │ "per .com vai da:  │
                        │  a.gtld-servers.net"│
                        └─────────┬──────────┘
                                  │
                        ┌─────────▼──────────┐
                        │   TLD SERVER .com  │
                        │ (Verisign)         │
                        │ "per example.com   │
                        │  vai da:           │
                        │  a.iana-servers.net"│
                        └─────────┬──────────┘
                                  │
                        ┌─────────▼──────────┐
                        │  NS AUTORITATIVO   │
                        │ (a.iana-servers.net)│
                        │ "www.example.com   │
                        │  = 93.184.216.34"  │
                        └─────────┬──────────┘
                                  │
                        Salva in cache (TTL 3600s)
                                  │
                                  ▼
                        STUB RESOLVER ← "93.184.216.34"
```

---

## 🌍 I Root Server — Il Punto di Partenza

Il recursive resolver inizia sempre dai **Root Server** — 13 server logici che conoscono i nameserver di tutti i TLD.

```
Sono 13 indirizzi IP logici (da a. a m.)
Ma fisicamente sono centinaia di macchine
distribuite in tutto il mondo via Anycast

a.root-servers.net  → Verisign
b.root-servers.net  → USC Information Sciences Institute
c.root-servers.net  → Cogent Communications
d.root-servers.net  → University of Maryland
e.root-servers.net  → NASA
f.root-servers.net  → Internet Systems Consortium
g.root-servers.net  → US DOD Network Information Center
h.root-servers.net  → US Army Research Lab
i.root-servers.net  → Netnod (Svezia)
j.root-servers.net  → Verisign
k.root-servers.net  → RIPE NCC (Europa)
l.root-servers.net  → ICANN
m.root-servers.net  → WIDE Project (Giappone)
```

```bash
# Vedere i root server
dig . NS +short

# Query diretta a un root server
dig @a.root-servers.net example.com

# Il root server non risponde con l'IP finale
# risponde con "vai a chiedere al TLD server"
# → risposta di tipo REFERRAL non ANSWER
```

---

## 💾 La Cache — Il Componente Più Importante

La cache è ciò che rende il recursive resolver **efficiente**. Senza cache ogni richiesta richiederebbe 3+ query verso server distribuiti nel mondo.

```
Prima query: www.example.com
→ root server → TLD → NS → risposta
→ salva in cache: www.example.com = 93.184.216.34 (TTL 3600s)

Seconda query (entro 3600s): www.example.com
→ risponde dalla cache in <1ms
→ nessuna query esterna necessaria
```

### TTL — Time To Live

```bash
# Vedere il TTL di una risposta
dig example.com A

# Output:
;; ANSWER SECTION:
example.com.    3600    IN    A    93.184.216.34
                 ↑
                 TTL in secondi
                 dopo 3600s il record viene eliminato dalla cache
                 e la prossima query farà una nuova richiesta
```

### TTL e Footprinting

```bash
# TTL basso (< 300s) → il sito cambia IP spesso
#   → probabilmente usa CDN o load balancer
#   → l'IP trovato oggi potrebbe non essere quello di domani

# TTL alto (> 86400s = 1 giorno) → infrastruttura stabile
#   → l'IP è probabilmente fisso
#   → più utile per il footprinting

dig example.com A +ttlid      # mostra TTL completo
dig example.com A | grep "^;; ANSWER" -A5
```

---

## 🌐 Resolver Ricorsivi Pubblici

I più comuni che trovi configurati nei sistemi:

|Provider|IPv4|IPv6|Caratteristiche|
|---|---|---|---|
|**Google**|8.8.8.8 / 8.8.4.4|2001:4860:4860::8888|Veloce, log delle query|
|**Cloudflare**|1.1.1.1 / 1.0.0.1|2606:4700:4700::1111|Privacy-focused, no log|
|**OpenDNS**|208.67.222.222|-|Filtri contenuti, enterprise|
|**Quad9**|9.9.9.9|2620:fe::fe|Blocca malware noti|
|**AdGuard**|94.140.14.14|-|Blocca ads e tracker|
|**ISP**|variabile|-|Default, spesso lento|

```bash
# Confronta velocità dei resolver
for dns in 8.8.8.8 1.1.1.1 9.9.9.9 208.67.222.222; do
    time=$(dig @$dns example.com A +stats 2>&1 | grep "Query time" | awk '{print $4}')
    echo "$dns → ${time}ms"
done
```

---

## 🏠 Resolver Ricorsivo Locale — Raspberry Pi

Puoi trasformare un Raspberry Pi in un **resolver ricorsivo completo** — bypassa completamente i resolver degli ISP.

### Opzione 1 — Pi-hole (con resolver upstream)

```
Pi-hole non è un resolver ricorsivo completo
È un DNS sink che filtra ads/tracker
e poi inoltra le query a un resolver upstream (es. 8.8.8.8)

PC → Pi-hole → 8.8.8.8 (resolver ricorsivo esterno)
```

### Opzione 2 — Unbound (resolver ricorsivo completo)

```
Unbound è un resolver ricorsivo completo
Naviga la gerarchia DNS autonomamente
Nessun resolver esterno necessario

PC → Pi-hole → Unbound → Root Server → TLD → NS
                ↑
              tuo Raspberry Pi fa tutto
```

```bash
# Installare Unbound su Raspberry Pi
sudo apt install unbound -y

# Configurazione base
sudo nano /etc/unbound/unbound.conf.d/pi-hole.conf
```

```yaml
server:
    verbosity: 0
    interface: 127.0.0.1
    port: 5335
    do-ip4: yes
    do-udp: yes
    do-tcp: yes
    do-ip6: no

    # Root hints — lista dei root server
    root-hints: "/var/lib/unbound/root.hints"

    # Sicurezza
    harden-glue: yes
    harden-dnssec-stripped: yes
    use-caps-for-id: no

    # Privacy
    hide-identity: yes
    hide-version: yes

    # Cache
    cache-min-ttl: 3600
    cache-max-ttl: 86400

    # Performance
    prefetch: yes
    num-threads: 1
```

```bash
# Aggiorna i root hints (lista dei 13 root server)
curl -o /var/lib/unbound/root.hints \
  https://www.internic.net/domain/named.root

# Avvia Unbound
sudo systemctl enable unbound
sudo systemctl start unbound

# Test
dig @127.0.0.1 -p 5335 example.com A +short
# → risolve autonomamente senza resolver esterno ✅

# Poi configura Pi-hole per usare Unbound
# Pi-hole Admin → Settings → DNS → Custom: 127.0.0.1#5335
```

### Vantaggi di Unbound su Raspberry Pi

```
✅ Nessuna query va a Google/Cloudflare/ISP
✅ Privacy completa — solo tu vedi le tue query
✅ Cache locale velocissima per la tua rete
✅ DNSSEC nativo — verifica le firme crittografiche
✅ Zero dipendenza da servizi esterni
```

---

## 🔒 DNSSEC — Autenticazione delle Risposte DNS

Il recursive resolver può verificare che le risposte DNS siano autentiche tramite **DNSSEC** (DNS Security Extensions).

```
Senza DNSSEC:
Recursive Resolver → NS Autoritativo
"example.com = 93.184.216.34"
→ il resolver accetta la risposta senza verificarla
→ un attaccante può iniettare risposte false

Con DNSSEC:
Ogni risposta DNS è firmata crittograficamente
Il resolver verifica la firma prima di accettarla
→ DNS cache poisoning molto più difficile
```

```bash
# Verificare se un dominio usa DNSSEC
dig example.com DNSKEY +short    # chiave pubblica
dig example.com DS +short        # delegation signer

# Verificare la catena DNSSEC completa
dig example.com A +dnssec

# Testare la validazione DNSSEC
dig @8.8.8.8 sigfail.verteiltesysteme.net A
# → SERVFAIL se DNSSEC è validato correttamente
# → questo dominio ha una firma DNSSEC intenzionalmente invalida
```

---

## 🕵️ Rilevanza nel Cybersecurity

### 1. DNS Cache Poisoning

```
L'attaccante inietta record falsi nella cache
del recursive resolver

example.com = 93.184.216.34  ← risposta legittima
example.com = 10.0.0.1       ← risposta iniettata dall'attaccante

→ tutti gli utenti che usano quel resolver
  vengono reindirizzati all'IP malevolo
  fino allo scadere del TTL

Difesa: DNSSEC + resolver aggiornato
```

### 2. DNS Amplification Attack (DDoS)

```
I resolver ricorsivi aperti (open resolvers)
possono essere usati per amplificare attacchi DDoS

Attaccante invia query con IP sorgente falsificato
(IP della vittima) al resolver ricorsivo
→ il resolver risponde alla vittima con risposte
  molto più grandi della query
→ amplificazione fino a 70x

Difesa: i resolver pubblici limitano le query
        per IP — rate limiting
```

### 3. DNS Tunneling

```
Il traffico DNS bypassa molti firewall
→ un attaccante può esfiltrare dati
  codificandoli nelle query DNS

query: dati-rubati-codificati-in-base64.malicious.com
→ il resolver ricorsivo risolve questa query
→ i dati arrivano al server dell'attaccante

Difesa: DNS inspection, blocco di domini sospetti,
        soluzioni come Cisco Umbrella
```

### 4. Analisi del TTL nel Footprinting

```bash
# TTL basso → CDN → IP non utile
dig target.com A
# TTL: 60 → Cloudflare o simile → cerca l'IP origin

# TTL alto → server stabile → IP probabilmente reale
dig target.com A
# TTL: 86400 → server stabile → usa per nmap, Shodan

# Confronta TTL da resolver diversi
dig @8.8.8.8 target.com A
dig @1.1.1.1 target.com A
# TTL diversi → il resolver ha la risposta in cache
# da tempi diversi → calcola l'età della cache
```

---

## 📊 Tipi di Risposta DNS

Il recursive resolver può ricevere diversi tipi di risposta dai server che interroga:

|Tipo|Significato|
|---|---|
|**ANSWER**|Risposta definitiva con il record richiesto|
|**REFERRAL**|"Non so, chiedi a questi server" (root e TLD rispondono così)|
|**NXDOMAIN**|Il dominio non esiste|
|**SERVFAIL**|Errore del server (spesso DNSSEC fallito)|
|**REFUSED**|Il server rifiuta di rispondere|
|**NOERROR + empty**|Il dominio esiste ma non ha quel tipo di record|

```bash
# Vedere il tipo di risposta
dig example.com A
# ;; ->>HEADER<<- opcode: QUERY, status: NOERROR
#                                        ↑
#                              tipo di risposta

dig nonexistent.example.com A
# status: NXDOMAIN ← dominio non esiste

dig @a.root-servers.net example.com A
# status: NOERROR ma sezione ANSWER vuota
# sezione AUTHORITY piena → REFERRAL
```

---

## 🔗 Command Cheat Sheet

```bash
# Query base
dig example.com A                              # risoluzione standard
dig @8.8.8.8 example.com A +short             # usa Google resolver
dig @1.1.1.1 example.com A +short             # usa Cloudflare resolver
dig @127.0.0.1 -p 5335 example.com            # usa Unbound locale

# TTL e cache
dig example.com A +ttlid                       # mostra TTL
dig example.com A +nocache                     # ignora cache locale

# Root server
dig . NS +short                                # lista root server
dig @a.root-servers.net example.com            # query a root server

# DNSSEC
dig example.com DNSKEY +short                  # chiave pubblica
dig example.com DS +short                      # delegation signer
dig example.com A +dnssec                      # risposta con firma

# Trace — simula il percorso del resolver ricorsivo
dig example.com +trace
# → mostra ogni step: root → TLD → NS → risposta

# Benchmark resolver
for dns in 8.8.8.8 1.1.1.1 9.9.9.9; do
    time=$(dig @$dns example.com A +stats 2>&1 \
           | grep "Query time" | awk '{print $4}')
    echo "$dns → ${time}ms"
done
```

---

## 🔗 Related Notes

- [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Stub Resolver|Stub Resolver]] ← chi gli fa le domande
- [[Dig]] ← usare dig per il footprinting
- [[Top Level Domain (TLD)]] ← i TLD che il resolver naviga
- [[WHOIS]] ← chi possiede i domini che risolve
- [[Hijacking]] ← DNS hijacking e cache poisoning
- [[Tor]] ← DNS e anonimità

---

_References: man unbound · https://www.cloudflare.com/learning/dns/dns-server-types · https://root-servers.org · RFC 1034, RFC 1035 · Linux Basics for Hacking — OccupyTheWeb_