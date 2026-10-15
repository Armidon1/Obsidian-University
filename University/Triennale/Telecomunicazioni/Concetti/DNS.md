## tags: [eth, network-services, dns, cache-poisoning] capitolo: HE7 Ch.5 collegato: [[RPC (Remote Procedure Call)]], [[x_window_system_attacks]], [[command_injectio]]

# DNS — Architettura e Attacchi

## Cos'è e perché è critico

DNS = **Domain Name System**. Traduce nomi (`google.com`) in IP (`74.125.47.147`) e viceversa. È il servizio che rende navigabile internet.

**Perché è target privilegiato:**

- Quasi sempre esposto sul perimetro (`53/udp + 53/tcp`)
- UDP-based di default → no handshake, no autenticazione
- Critico per ogni altro servizio: web, mail, VPN, AD → compromise DNS = compromise everything downstream
- BIND (l'implementazione UNIX standard) ha storia lunga di vulnerabilità

vedi anche [[6 - CS Application Level - DNS Security]] 

---

## Protocollo Base

### Trasporto

|Porta|Uso|
|---|---|
|53/udp|Query/response standard (la maggioranza del traffico)|
|53/tcp|Risposte > 512 byte, zone transfer (AXFR/IXFR), DNSSEC|
|853/tcp|DNS-over-TLS (DoT)|
|443/tcp|DNS-over-HTTPS (DoH)|

### Formato Query

Una query DNS contiene:

- **Transaction ID** (16 bit) — match query/response
- **Flags** (recursion desired, ecc.)
- **Question section** (nome + tipo + classe)

La risposta deve avere lo **stesso TXID** per essere accettata. È l'unico meccanismo anti-spoofing nel protocollo base.

---

## Tipi di Record (i principali)

|Record|Significato|Esempio|
|---|---|---|
|**A**|Hostname → IPv4|`google.com → 74.125.47.147`|
|**AAAA**|Hostname → IPv6|`google.com → 2607:f8b0::200e`|
|**NS**|Nameserver autoritativo di un dominio|`google.com → ns1.google.com`|
|**MX**|Mail server del dominio|`google.com → smtp.google.com (priority 10)`|
|**CNAME**|Alias verso un altro nome|`www.example.com → example.com`|
|**PTR**|Reverse: IP → hostname|`147.47.125.74.in-addr.arpa → google.com`|
|**TXT**|Testo libero (SPF, DKIM, verifica dominio)|`v=spf1 include:_spf.google.com -all`|
|**SOA**|Start of Authority — metadata zona (serial, TTL, ecc.)|un solo SOA per zona|

---

## Resolution Flow

### Ruoli dei server

| Ruolo                                                                                                      | Cosa fa                                                                     |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **[[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Stub Resolver\|Stub Resolver]]** | Il client (la tua /etc/resolv.conf punta qui)                               |
| **[[Recursive Resolver DNS]]**                                                                             | Fa il lavoro per il client: interroga la catena fino alla risposta. Cachea. |
| **Authoritative NS**                                                                                       | Ha la verità per una zona specifica. Non fa ricorsione.                     |
| **Root server**                                                                                            | I 13 (logici) root NS — punto di partenza della catena (`.`)                |

### Esempio: risoluzione di `www.google.com`

```
1. client → recursive: "www.google.com?"
2. recursive → root NS: "chi è autoritativo per .com?"
   root → "i NS di .com sono a.gtld-servers.net, ..."
3. recursive → .com NS: "chi è autoritativo per google.com?"
   .com NS → "ns1.google.com, ns2.google.com, ..."
4. recursive → ns1.google.com: "che IP è www.google.com?"
   ns1.google.com → "74.125.47.147, TTL 300"
5. recursive → cachea il risultato → risponde al client
```

Il **TTL** determina quanto a lungo il risultato resta in cache. Finché è cachato, nessuna nuova query verso il NS autoritativo.

---

## Enumeration / Recon

```bash
# Query base
dig google.com               # A record
dig google.com MX            # mail server
dig google.com NS            # nameserver autoritativi
dig google.com ANY           # tutti i record (spesso disabilitato)
dig -x 74.125.47.147         # reverse lookup

# Zone transfer (se mal configurato)
dig @ns1.target.com target.com AXFR
# se risponde con tutta la zona → dump completo di tutti i record interni

# Bruteforce di sottodomini
dnsenum target.com
dnsrecon -d target.com
fierce -dns target.com
amass enum -d target.com

# Wordlist-based subdomain discovery
gobuster dns -d target.com -w subdomains.txt
```

**[[Zone Transfer]] (AXFR)** mal configurato = dump della rubrica DNS interna del bersaglio. Mostra hostname interni, server di sviluppo, infrastruttura nascosta. Tipicamente i NS autoritativi dovrebbero permettere AXFR solo verso slave NS noti, non al mondo.

---

## Attack Surface

### 1. Cache Poisoning (categoria)

Idea: ingannare un recursive resolver perché cachei una risposta falsa. Da quel momento tutti i client che usano quel resolver vengono dirottati.

Variante classica pre-2008: brute force del TXID (16 bit) sperando di arrivare prima della risposta vera. **Limitazione**: solo un tentativo per ogni TTL della entry vera.

→ Vedi sezione Kaminsky in fondo per la versione moderna.

---

### 2. DNS Amplification ([[DDoS Amplification]])

Sfruttando DNS come riflettore:

- Attaccante manda query UDP spoofata con source IP = vittima
- Server DNS risponde alla vittima con risposta molto più grande della query
- Amplification factor: query 60 byte → response 4000 byte (con record DNSSEC) = **70x**
- Usato in DDoS storici (Spamhaus 2013, ~300 Gbps)

**Fix**: response rate limiting (RRL) sui NS autoritativi, no open resolver pubblici.

---

### 3. DNS [[Hijacking]]

Diversi vettori:

- **Compromise del registrar account** → cambi gli NS del dominio → punti il mondo dove vuoi
- **BGP hijacking** → annunci la rotta verso gli IP dei root server / TLD server → intercetti traffico DNS
- **MitM sul resolver** (router compromesso, ISP malevolo) → rispondi al posto del DNS legittimo
- **Modifica `/etc/hosts`** o `resolv.conf` sulla vittima (post-exploit local)

---

### 4. DNS Tunneling (esfiltrazione / C2)

DNS attraversa firewall che bloccano tutto il resto. Encoding di dati arbitrari nei sottodomini:

```
exfil-base64data-here.attacker.com → query DNS verso attacker NS
                                   → attacker decodifica i dati
```

Strumenti: `iodine`, `dnscat2`, `dns2tcp`. Tool legittimo abusato: DNS over HTTPS.

**Detection**: query lunghissime, alto volume verso domini sospetti, entropy alta nei sottodomini. Vedi anche [[command_injection]] per back channel concept.

---

### 5. Subdomain Takeover

Pattern:

1. `dev.target.com` → CNAME → `oldapp.herokuapp.com`
2. Lo Heroku app è stato deprovisioned ma il CNAME è rimasto
3. Attaccante registra `oldapp.herokuapp.com` su Heroku
4. Ora controlla `dev.target.com` — può ospitarci phishing, rubare cookie del dominio principale, ecc.

Vulnerabilità di hygiene, non protocollo. Comunissimo, ricerche bug bounty bread-and-butter.

---

### 6. BIND Vulnerabilities Storiche

BIND ha una storia lunga di:

- Buffer overflow remoti (vari CVE pre-2010)
- DoS via query malformate
- Cache poisoning (Kaminsky e successori)
- TSIG signature bypass

Tipicamente exploitabile via Metasploit. Per l'esame: BIND è l'implementazione UNIX di riferimento, è il target storico più colpito.

---

## Countermeasures (overview)

| Mitigazione                   | Cosa risolve                                                             | Adozione                                              |
| ----------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- |
| **[[DNSSEC]]**                | Firma crittografica delle risposte → cache poisoning, hijacking risposta | Parziale (richiede firma zone + validazione resolver) |
| **DNS-over-TLS / DoH**        | Cifra il trasporto → MitM, eavesdropping                                 | Crescente (browser, public resolver)                  |
| **Source port randomization** | Cache poisoning brute force (post-Kaminsky)                              | Universale dal 2008                                   |
| **0x20 encoding**             | Aggiunge entropia mescolando maiuscole/minuscole nel query name          | Minoritaria                                           |
| **Response Rate Limiting**    | DNS amplification                                                        | Standard sui NS pubblici seri                         |
| **AXFR restricting**          | Zone transfer leak                                                       | Best practice, spesso ignorata                        |
| **DNS over QUIC**             | Trasporto cifrato + performance                                          | Emergente                                             |

**DNSSEC** è l'unico fix strutturale: anche se l'attaccante avvelena la cache, il client verifica la firma e rifiuta. Ma richiede che ogni zona sia firmata e che ogni resolver validi — adozione frammentata, soprattutto sui domini secondari.

---

## TL;DR esame

1. DNS = UDP/53 non autenticato → attack surface enorme
2. Record principali: A, NS, MX, CNAME, PTR, TXT, SOA
3. Catena: stub → recursive → root → TLD → authoritative → cache
4. Cache poisoning = avvelenare risposta nel resolver → dirottamento di tutti i client
5. AXFR = zone transfer leak se mal configurato
6. DNS amplification = DDoS reflector
7. DNS tunneling = esfiltrazione/C2 sotto traveste
8. DNSSEC = fix strutturale (firma crittografica); DoH/DoT = solo trasporto

---

---

# Appendice — Kaminsky Attack (2008)

## Il problema con il cache poisoning classico

Pre-2008, l'attacco era: brute-force del TXID a 16 bit sperando di battere la risposta vera. Limitazione fondamentale:

> Se la entry vera è già in cache, il resolver non interroga il NS finché il TTL non scade. Quindi: **un tentativo ogni TTL** (minuti/ore). Con 65536 possibilità → anni statisticamente.

## L'innovazione di Kaminsky

Invece di poisonare una entry cachata, **forza il resolver a fare nuove query continuamente** chiedendo sottodomini casuali che non esistono:

```
"aabbcc1234.google.com"  ← mai visto, resolver deve interrogare il NS
"xxyyzz5678.google.com"  ← idem
"qqwweerrtt99.google.com" ← idem
... migliaia al secondo
```

Ogni query = nuova finestra di race = nuovo TXID da indovinare.

L'attaccante flooda risposte spoofate per ogni query, contenenti **un NS record avvelenato** per il dominio padre:

```
"aabbcc1234.google.com è 1.2.3.4 — e by the way,
 l'authoritative NS di google.com è ns1.attacker.com (6.6.6.6)"
```

Se una risposta spoofata vince la race con TXID corretto → il resolver cachea **il NS record avvelenato per google.com**, non solo la entry richiesta. Da quel momento _tutto_ `*.google.com` va all'attaccante.

## Debolezze combinate

|Debolezza|Impatto|
|---|---|
|TXID solo 16 bit|65536 combinazioni — brute-forceable rapidamente|
|**Source port fissa**|Riduce search space totale a soli 16 bit. Con porta random sarebbero 32 bit (~4 miliardi)|
|Multiple outstanding queries|Più finestre parallele aperte simultaneamente|

Math: migliaia di query/sec × 1/65536 chance = avvelenamento in secondi/minuti, non anni.

## Impatto storico

- Disclosure coordinato luglio 2008, patch vendor in segreto
- Leak prematuro → exploit pubblico su Milw0rm in giorni
- Metasploit rilasciò modulo → **i server DNS di AT&T che risolvevano metasploit.com vennero avvelenati con quel modulo** → metasploit.com redirezionato per ad fraud per un po' 🤡

## Implementazioni vulnerabili (al momento del 2008)

- BIND 8 (sostanzialmente abbandonato dopo)
- BIND 9 unpatched (versioni pre-9.5.0-P1 / 9.4.2-P1)
- Microsoft DNS unpatched (pre-MS08-037)

**Oggi**: queste implementazioni patchate non sono più vulnerabili al Kaminsky originale. BIND 8 è morto. BIND 9 e Microsoft DNS sono patchati di default da quasi 20 anni. Vulnerabili oggi solo versioni antiche su infrastrutture legacy abbandonate.

## Fix

1. **Source port randomization** (RFC 5452) — fix immediato post-disclosure, search space → ~4 miliardi
2. **DNSSEC** — fix strutturale, firme crittografiche

## Sequel: SAD DNS (2020)

Attacco follow-up che usa side channel ICMP per inferire la source port UDP del resolver, **bypassando la source port randomization**. Riporta il search space ai livelli pre-fix. CVE-2020-25705.

Mitigazione: rate limiting dei messaggi ICMP, validazione DNSSEC. Conferma che senza DNSSEC il protocollo resta fragile.