# BGP — Border Gateway Protocol

Tags: #networking #routing #bgp #internet #hacking-exposed #enumeration

---

## Cos'è

BGP è il **protocollo di routing che fa funzionare Internet**. Definito nell'**RFC 4271** (versione attuale BGP-4), è responsabile dello scambio di informazioni di instradamento tra le grandi reti che compongono Internet — gli **Autonomous System (AS)**.

Senza BGP non esisterebbe Internet come la conosciamo: ogni ISP, ogni grande azienda, ogni data center comunica con gli altri attraverso BGP per sapere come raggiungere qualsiasi indirizzo IP nel mondo.

---

## Concetti fondamentali

### Autonomous System (AS)

Un AS è una **rete o un insieme di reti** sotto un unico controllo amministrativo e con una politica di routing coerente. Ogni AS ha un numero univoco assegnato a livello globale (**ASN — Autonomous System Number**).

```
Esempi di AS:
AS15169 → Google
AS32934 → Facebook/Meta
AS13335 → Cloudflare
AS8075  → Microsoft
AS3356  → Lumen (Level 3)
AS1299  → Telia
```

Ci sono circa **100.000 AS attivi** su Internet.

### Routing tra AS — il quadro generale

```
       AS1 (TIM)              AS2 (Vodafone)
         │                        │
         ├─── peering BGP ────────┤
         │                        │
       AS3 (Cloudflare)       AS4 (Google)
         │                        │
         └─── peering BGP ────────┘
```

Ogni AS annuncia ai suoi vicini quali **prefissi IP** può raggiungere. I vicini propagano l'informazione ai loro vicini, e così via, fino a costruire la mappa completa di Internet.

---

## BGP vs altri protocolli di routing

|Protocollo|Tipo|Dove si usa|
|---|---|---|
|**RIP**|Distance Vector|Reti piccole (legacy)|
|**OSPF**|Link State|Reti aziendali interne (IGP)|
|**EIGRP**|Hybrid (Cisco)|Reti enterprise Cisco|
|**IS-IS**|Link State|ISP — instradamento interno|
|**BGP**|Path Vector|Internet — instradamento tra AS|

**IGP (Interior Gateway Protocol)** = dentro un AS (OSPF, IS-IS, EIGRP) **EGP (Exterior Gateway Protocol)** = tra AS diversi (BGP)

---

## Come funziona BGP — meccanismo base

### Sessione BGP

Due router BGP stabiliscono una sessione su **TCP porta 179**:

```
1. TCP handshake (porta 179)
       ↓
2. OPEN message — versione BGP, ASN, hold time
       ↓
3. KEEPALIVE messages — verifica peer attivo
       ↓
4. UPDATE messages — scambio di prefissi/rotte
       ↓
5. NOTIFICATION — solo in caso di errori
```

### Tipi di peering

```
eBGP (External BGP) — tra AS diversi
   AS1 ←──── eBGP ────→ AS2

iBGP (Internal BGP) — dentro lo stesso AS
   Router-A ←─── iBGP ───→ Router-B  (entrambi in AS1)
```

### UPDATE message — il cuore di BGP

Ogni UPDATE annuncia:

- **NLRI (Network Layer Reachability Information)** — prefissi IP che l'AS può raggiungere
- **AS_PATH** — sequenza di AS attraversati per raggiungere quel prefisso
- **NEXT_HOP** — IP del prossimo router
- **Attributi BGP** — informazioni per scegliere la rotta migliore

```
Esempio UPDATE:
  Prefix: 8.8.8.0/24
  AS_PATH: 1299 → 174 → 15169
  NEXT_HOP: 192.0.2.1
```

Significa: "per raggiungere 8.8.8.0/24, passa per Telia (1299) → Cogent (174) → Google (15169)".

---

## Path selection — come BGP sceglie la rotta migliore

Quando un router BGP riceve **più rotte** per lo stesso prefisso, applica un algoritmo deterministico:

```
1. Weight (Cisco)              — preferenza locale del router
2. Local Preference            — preferenza all'interno dell'AS
3. Locally originated routes   — rotte annunciate da questo router
4. AS_PATH length              — più corto = migliore
5. Origin code                 — IGP < EGP < incomplete
6. MED (Multi-Exit Discriminator) — più basso = migliore
7. eBGP > iBGP
8. IGP cost al next-hop        — più basso = migliore
9. Router ID più basso         — tiebreaker finale
```

> Il criterio più importante in pratica è l'**AS_PATH length** — meno AS da attraversare = rotta preferita.

---

## Sicurezza — il grande problema di BGP

BGP è stato progettato nel 1989 **senza nessun meccanismo di autenticazione o verifica**. Si basa interamente sulla **fiducia** tra gli ISP.

### Vulnerabilità fondamentali

|Problema|Descrizione|
|---|---|
|**No origin verification**|Chiunque può annunciare qualsiasi prefisso|
|**No path verification**|L'AS_PATH può essere falsificato|
|**No authentication**|Le sessioni BGP raramente sono autenticate|
|**Plaintext**|TCP 179 in chiaro fino a poco fa|
|**Trust-based**|Un ISP può influenzare il routing globale|

---

## BGP Hijacking

L'attacco più famoso contro BGP. Un AS malizioso (o configurato male) **annuncia prefissi che non gli appartengono**:

```
Scenario normale:
   AS15169 (Google) annuncia 8.8.8.0/24
   → tutto il mondo manda traffico per 8.8.8.0/24 a Google ✓

Hijack:
   AS_ATTACCO annuncia 8.8.8.0/24
   → router BGP nel mondo accettano l'annuncio
   → traffico per 8.8.8.0/24 viene dirottato verso AS_ATTACCO
   → l'attaccante può:
       - intercettare il traffico (man-in-the-middle)
       - causare un blackhole (denial of service)
       - falsificare risposte
```

### Casi reali famosi

|Anno|Evento|Impatto|
|---|---|---|
|2008|Pakistan Telecom hijacka YouTube|YouTube down globalmente per 2 ore|
|2018|Amazon DNS (Route53) hijack|Furto di criptovalute da MyEtherWallet|
|2019|China Telecom hijack di Google|Traffico Google instradato in Cina|
|2020|Russian Rostelecom hijack|Traffico di Apple, Google, Facebook redirezionato|
|2022|KlaySwap hijack|$1.9M rubati via attacco BGP+DNS|

---

## Route Leak

Variante meno grave ma più frequente del hijack. Un AS annuncia rotte legittime a peer **a cui non dovrebbe** annunciarle, causando instradamento subottimale:

```
Scenario normale:
   Customer → annuncia solo le proprie rotte al provider
   Provider → annuncia tutte le rotte solo ai propri customer/peer

Route leak:
   Customer riceve rotte dal Provider A
   Customer le riannuncia al Provider B (per errore)
   → traffico passa attraverso il customer
   → congestione, lentezza, potenziale MitM
```

### Caso reale famoso

**2019 — Verizon e Cloudflare**: un piccolo ISP del Pennsylvania (DQE Communications) ha leakato rotte BGP a Verizon, che le ha propagate. Cloudflare, Amazon, e molti altri sono diventati irraggiungibili per ore.

---

## Enumerazione BGP — uso passivo per recon

BGP è una miniera d'oro per il **footprinting**. Ogni AS pubblico è documentato e i suoi annunci sono visibili globalmente.

### Trovare l'ASN di un'azienda

```bash
# whois su un IP — restituisce l'AS proprietario
whois -h whois.cymru.com " -v 8.8.8.8"

# Con dig
dig +short AS15169.asn.cymru.com TXT

# bgp.he.net (Hurricane Electric) — interfaccia web
# https://bgp.he.net/AS15169
```

### Trovare tutti i prefissi di un AS

```bash
# whois con bgp.tools
curl -s https://bgp.tools/prefixes/as15169.csv

# Hurricane Electric
# https://bgp.he.net/AS15169#_prefixes

# RADb (Routing Assets Database)
whois -h whois.radb.net "!gAS15169"
```

### Cosa ottieni

```
AS15169 (Google):
  Prefissi IPv4: 8.8.4.0/24, 8.8.8.0/24, 34.0.0.0/9, 35.184.0.0/13, ...
  Prefissi IPv6: 2001:4860::/32, 2404:6800::/32, ...
  Peering: AS6939 (HE), AS174 (Cogent), AS1299 (Telia), ...
  Origine: tutti i datacenter Google nel mondo
```

Per un attaccante questo è oro: conoscere **tutti i blocchi IP di un'azienda target** senza inviare un singolo pacchetto al target.

---

## Tool per analisi BGP

```bash
# whois bgp.tools
curl https://bgp.tools/as/15169

# Tool dedicati
bgpdump        # parser per dump BGP
bgpscanner     # analisi flussi BGP
mrtparse       # parser MRT (Multi-routing Toolkit)

# BGPStream — framework di Caida
# https://bgpstream.caida.org

# RIPE RIS — Routing Information Service
# https://ris.ripe.net

# RouteViews — archivio storico annunci BGP
# http://routeviews.org
```

---

## Contromisure

### RPKI (Resource Public Key Infrastructure)

La principale contromisura moderna contro BGP hijacking:

```
Senza RPKI:
   AS annuncia 8.8.8.0/24
   → tutti accettano

Con RPKI:
   AS annuncia 8.8.8.0/24
   → router verifica firma crittografica RPKI
   → solo se firmato dal proprietario legittimo (Google) → accettato
   → altrimenti scartato
```

Adozione RPKI in 2025: **~50% dei prefissi globali** sono firmati con RPKI. In crescita ma ancora non universale.

### BGPSec

Estensione di BGP che aggiunge firme crittografiche al **path completo** (non solo all'origine come RPKI). Praticamente non implementato — troppo costoso computazionalmente per i grandi ISP.

### Filtri BGP manuali

ISP responsabili applicano filtri ai loro peering BGP per accettare solo rotte attese dai customer. Funziona ma non è scalabile.

### MD5/TCP-AO authentication

Le sessioni BGP possono essere autenticate con password condivisa (MD5) o con il più moderno TCP-AO. Protegge la sessione TCP ma non gli annunci stessi.

---

## BGP nel contesto Hacking Exposed

Hacking Exposed 7 tratta BGP nel **footprinting** come strumento per:

- Mappare l'infrastruttura di rete del target
- Identificare provider e ridondanze
- Trovare blocchi IP completi senza scansionare
- Inferire la struttura organizzativa dai pattern di peering

Non è un attacco "attivo" tipico — è enumerazione passiva di alto livello.

---

## Workflow di footprinting BGP

```
1. Identifica il dominio target → target.com
        ↓
2. Risolvi un IP → 1.2.3.4
        ↓
3. Trova l'AS proprietario → AS12345
        ↓
4. Enumera tutti i prefissi dell'AS
   → 1.2.0.0/16, 1.3.0.0/16, 5.5.5.0/24...
        ↓
5. Hai la lista completa degli IP dell'azienda
        ↓
6. Procedi con scanning su questi prefissi
```

> Tecnica preferita rispetto al brute force DNS perché completamente passiva — il target non vede nessuna query.

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Footprinting
- RFC 4271 — Border Gateway Protocol 4 (BGP-4)
- RFC 6480 — Resource Public Key Infrastructure (RPKI)
- BGP.tools: https://bgp.tools
- Hurricane Electric BGP: https://bgp.he.net
- RIPE RIS: https://ris.ripe.net
- RouteViews: http://routeviews.org
- Cloudflare Radar: https://radar.cloudflare.com/routing