# Traceroute

#linux #cybersecurity #networking #footprinting #linux-basics-for-hackers

---

## 🗂️ Overview

**Traceroute** è uno strumento di diagnostica di rete che mostra il **percorso** che i pacchetti seguono dalla tua macchina fino a una destinazione — rivelando ogni router intermedio (hop) attraversato lungo il cammino.

```
Tu → Router ISP → Router A → Router B → Router C → Destinazione
  1              2           3           4           5
```

Ogni linea dell'output rappresenta un **hop** — un router che ha gestito il pacchetto nel suo viaggio verso la destinazione.

---

## 🔧 Come Funziona — TTL Manipulation

Traceroute sfrutta il campo **TTL (Time To Live)** dell'header IP in modo creativo:

```
Ogni pacchetto IP ha un TTL
→ ogni router che lo attraversa decrementa il TTL di 1
→ quando TTL raggiunge 0 → il router scarta il pacchetto
→ e manda un messaggio ICMP "Time Exceeded" al mittente

Traceroute sfrutta questo:

Manda pacchetto con TTL=1
→ il primo router lo scarta → manda ICMP "Time Exceeded"
→ traceroute registra l'IP del primo router

Manda pacchetto con TTL=2
→ il secondo router lo scarta → manda ICMP "Time Exceeded"
→ traceroute registra l'IP del secondo router

... e così via fino alla destinazione
```

---

## 🛠️ Installazione e Varianti

```bash
# Linux — traceroute classico (UDP)
sudo apt install traceroute -y
traceroute example.com

# Linux — traceroute ICMP (come Windows)
sudo apt install iputils-tracepath -y
tracepath example.com

# Linux — MTR (My Traceroute) — il più potente
sudo apt install mtr -y
mtr example.com

# Windows equivalente
tracert example.com
```

---

## 📋 Sintassi e Opzioni

```bash
# Base
traceroute example.com             # UDP (default su Linux)
traceroute -I example.com          # ICMP (come ping)
traceroute -T example.com          # TCP SYN (bypassa molti firewall)
traceroute -n example.com          # no DNS resolution (più veloce)
traceroute -q 1 example.com        # 1 sola probe per hop (default 3)

# Porte e protocolli
traceroute -T -p 80 example.com    # TCP su porta 80
traceroute -T -p 443 example.com   # TCP su porta 443 (HTTPS)
traceroute -U -p 53 example.com    # UDP su porta 53 (DNS)

# Controllo percorso
traceroute -m 30 example.com       # max 30 hop (default)
traceroute -m 5 example.com        # solo primi 5 hop
traceroute -f 5 example.com        # parti dall'hop 5 (skip iniziali)
traceroute -s SOURCE_IP example.com # specifica IP sorgente

# Output
traceroute -n example.com          # mostra solo IP (no hostname)
traceroute -A example.com          # mostra ASN per ogni hop
```

---

## 📖 Leggere l'Output

```bash
traceroute example.com
```

```
traceroute to example.com (93.184.216.34), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)        1.2 ms   1.1 ms   1.0 ms
 2  10.x.x.1 (10.x.x.1)             8.4 ms   8.2 ms   8.5 ms
 3  * * *
 4  185.x.x.1 (185.x.x.1)          12.1 ms  11.9 ms  12.3 ms
 5  ae-1.r00.roma01.it.bb.gin.ntt.net  15.2 ms  14.8 ms  15.1 ms
 6  ae-0.r21.frnkge04.de.bb.gin.ntt.net  32.4 ms  31.9 ms  32.1 ms
 7  93.184.216.34 (93.184.216.34)   89.3 ms  89.1 ms  89.4 ms
```

### Campo per Campo

```
Hop 1: 192.168.1.1
→ il tuo router di casa
→ IP privato → rete domestica

Hop 2: 10.x.x.1
→ primo router del tuo ISP
→ IP privato → infrastruttura interna ISP

Hop 3: * * *
→ tre asterischi = nessuna risposta
→ il router ha bloccato i pacchetti ICMP
→ oppure scarta silenziosamente
→ non significa che il percorso sia interrotto

Hop 4: 185.x.x.1
→ router pubblico dell'ISP o di un carrier
→ IP pubblico → inizia la rete pubblica

Hop 5: ae-1.r00.roma01.it.bb.gin.ntt.net
→ router NTT a Roma
→ il nome rivela: città (roma), paese (it),
   provider (NTT = Nippon Telegraph and Telephone)

Hop 6: ae-0.r21.frnkge04.de.bb.gin.ntt.net
→ router NTT a Francoforte (frnkge04.de)
→ il traffico è passato in Germania

Hop 7: 93.184.216.34
→ destinazione raggiunta
→ tre misurazioni del RTT (Round Trip Time)
```

---

## ⭐ MTR — La Versione Avanzata

**MTR** (My Traceroute) combina traceroute e ping in un'interfaccia live che si aggiorna continuamente:

```bash
# Interattivo (aggiornamento continuo)
mtr example.com

# Report statico (utile per log)
mtr --report example.com
mtr --report-cycles 100 example.com  # 100 cicli poi stampa

# Con ASN
mtr -z example.com

# No DNS (solo IP)
mtr -n example.com

# TCP invece di ICMP (bypassa firewall)
mtr --tcp --port 443 example.com
```

### Output MTR

```
                             My traceroute
Host                         Loss%  Snt  Last   Avg  Best  Wrst
1. 192.168.1.1               0.0%   10   1.2   1.1   0.9   1.4
2. 10.x.x.1                  0.0%   10   8.4   8.2   7.9   8.8
3. (waiting for reply)
4. 185.x.x.1                 0.0%   10  12.1  11.9  11.5  12.5
5. ae-1.r00.roma01.it        0.0%   10  15.2  14.8  14.2  15.8
6. 93.184.216.34              0.0%   10  89.3  89.1  88.7  89.9
```

|Campo|Significato|
|---|---|
|`Loss%`|Percentuale di pacchetti persi|
|`Snt`|Pacchetti inviati|
|`Last`|RTT ultimo pacchetto (ms)|
|`Avg`|RTT medio|
|`Best`|RTT migliore|
|`Wrst`|RTT peggiore|

---

## 🕵️ Traceroute nel Footprinting

### 1. Mappare l'Infrastruttura di Rete del Target

```bash
# Traccia il percorso verso il target
traceroute -A -n target.com

# -A mostra l'ASN di ogni hop
# → rivela quali provider attraversa il traffico
# → rivela la topologia di rete del target

# Output esempio:
# 5. [AS3356] 4.69.x.x    → Level3 Communications
# 6. [AS16509] 54.x.x.x   → Amazon AWS
#                            → il target è su AWS
```

### 2. Identificare il Provider Reale

```bash
# Se il sito usa Cloudflare, traceroute si ferma a Cloudflare
traceroute cloudflare-protected-site.com
→ ultimo hop: 104.16.x.x  ← Cloudflare
→ non arrivi mai al server reale
→ conferma che il sito è dietro CDN

# Se traceroute arriva fino al server
traceroute target.com
→ ultimo hop: 93.184.216.34  ← server reale
→ IP direttamente raggiungibile
→ utile per nmap
```

### 3. Identificare Firewall e IDS

```bash
# Gli asterischi rivelano punti di filtro
traceroute target.com

# Pattern tipico:
# 1-4:  hop normali
# 5:    * * *        ← firewall perimetrale
# 6-8:  hop normali
# 9:    * * *        ← secondo layer di sicurezza
# 10:   destinazione

# Più asterischi = più layer di sicurezza
# Organizzazione attenta alla sicurezza
```

### 4. Geolocalizzare il Server

```bash
# I nomi degli hop spesso contengono la città
traceroute -n target.com | grep -v "\* \* \*"

# ae-1.r00.roma01.it.bb.gin.ntt.net
#         ↑    ↑  ↑
#         |    |  paese
#         |    città
#         router ID

# Rivela:
# → dove fisicamente si trova il server
# → quale carrier porta il traffico
# → il percorso internazionale dei dati
```

### 5. Confrontare Percorsi da Punti Diversi

```bash
# Da casa tua
traceroute target.com

# Da un server in un'altra nazione (via proxychains)
proxychains traceroute target.com

# Percorsi diversi → topologia di rete diversa
# Utile per capire la distribuzione geografica
# dell'infrastruttura del target
```

---

## 🔥 Traceroute TCP — Bypassare i Firewall

Il traceroute classico usa **UDP** su Linux — molti firewall lo bloccano. Il traceroute TCP bypassa questi filtri:

```bash
# TCP SYN su porta 80 (HTTP) — raramente bloccato
sudo traceroute -T -p 80 example.com

# TCP SYN su porta 443 (HTTPS) — quasi mai bloccato
sudo traceroute -T -p 443 example.com

# Con MTR — TCP
sudo mtr --tcp --port 443 example.com
```

```
Perché funziona:
I firewall permettono TCP verso porta 80/443
perché è traffico web legittimo
→ i pacchetti SYN passano
→ i router lungo il percorso rispondono
  con ICMP Time Exceeded
→ traceroute funziona anche attraverso i firewall
```

---

## ⚠️ Interpretare gli Asterischi

Gli `* * *` non sempre significano la stessa cosa:

```
Caso 1 — Router blocca ICMP
→ il router c'è ma scarta i messaggi ICMP
→ il percorso continua normalmente
→ gli hop successivi rispondono

Caso 2 — Packet loss reale
→ il router non risponde per congestione
→ MTR mostra Loss% > 0%
→ problema di rete reale

Caso 3 — Firewall perimetrale
→ il firewall blocca le probe di traceroute
→ ma permette il traffico applicativo
→ il sito è raggiungibile normalmente
→ il firewall non vuole rivelare la topologia

Caso 4 — Fine del percorso
→ * * * alla fine = destinazione non raggiunge
→ il target è completamente irraggiungibile
→ o è down, o blocca tutto il traffico
```

---

## 🔄 Traceroute vs Ping vs MTR

| |Ping|Traceroute|MTR|
|---|---|---|---|
|**Mostra hop**|❌|✅|✅|
|**RTT continuo**|✅|❌|✅|
|**Loss per hop**|❌|❌|✅|
|**Live update**|✅|❌|✅|
|**ASN**|❌|✅ (-A)|✅ (-z)|
|**TCP mode**|❌|✅ (-T)|✅ (--tcp)|
|**Migliore per**|Latenza base|Percorso una tantum|Diagnosi completa|

---

## 🔗 Command Cheat Sheet

```bash
# Base
traceroute example.com                    # UDP default
traceroute -I example.com                 # ICMP
traceroute -T -p 443 example.com          # TCP HTTPS
traceroute -n example.com                 # solo IP, no DNS
traceroute -A example.com                 # con ASN

# MTR
mtr example.com                           # interattivo
mtr --report example.com                  # report statico
mtr --tcp --port 443 example.com          # TCP mode
mtr -z example.com                        # con ASN
mtr -n example.com                        # solo IP

# Diagnostica
traceroute -m 5 example.com               # solo 5 hop
traceroute -q 1 example.com               # 1 probe per hop
traceroute -f 3 example.com               # parti dall'hop 3

# Footprinting
traceroute -A -n target.com               # ASN + IP
sudo traceroute -T -p 443 -n target.com   # TCP bypass firewall
mtr --report --tcp --port 443 target.com  # report completo
```

---

## 🔗 Related Notes

- [[Nmap]]
- [[Dig]]
- [[Stub Resolver]]
- [[Recursive Resolver DNS]]
- [[Hijacking]]
- [[OSINT]]

---

_References: man traceroute · man mtr · https://book.hacktricks.xyz · Hacking Exposed 7 — McClure, Scambray, Kurtz · Linux Basics for Hacking — OccupyTheWeb_