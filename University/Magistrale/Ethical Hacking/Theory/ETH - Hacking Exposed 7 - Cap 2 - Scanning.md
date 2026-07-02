lezione precedente [[ETH - Hacking Exposed 7 - Cap 1 - Footprinting]]
# Capitolo 2 — Scanning

> [!example] Le 4 fasi dello scanning
> 
> 1. Determinare se il sistema è vivo
> 2. Determinare quali servizi sono attivi/in ascolto
> 3. Rilevare il sistema operativo
> 4. Processare e salvare i dati raccolti (fondamentale su reti grandi, per scalare)

---

## 1. Determinare se il sistema è vivo

> [!info] ARP host discovery Funziona solo sulla stessa subnet (layer 2, niente routing). Tool:
> 
> - `arp-scan` — richiede root, lista IP↔MAC
> - `nmap -PR -sn` — host discovery via ARP, salta il port scan
> - Cain (solo Windows) — va oltre il semplice discovery

> [!info] ICMP host discovery Per host/router remoti. Tipi di messaggio: ECHO REQUEST/REPLY, TIMESTAMP, ADDRESS MASK.
> 
> - `ping` — utility OS per ECHO REQUEST/REPLY
> - Nmap — ICMP ping/timestamp/address mask, ma anche ARP ping e TCP ping (porte 80/443)
> - Hping3 / nping — qualunque combinazione di flag e tipo pacchetto, spoofing MAC/IP
> - Superscan — ICMP multiplo in parallelo
> 
> ⚠️ Troppo traffico generato può far scattare un IDS — capire cosa fa davvero un tool è importante prima di lanciarlo.

> [!info] TCP/UDP host discovery Si usa quando ICMP è bloccato (in entrata e/o in uscita).
> 
> - Server → si sondano le porte di servizio note (es. 80 per HTTP)
> - Desktop → spesso hanno firewall locale, ma restano raggiungibili via RDP, file sharing o se il firewall è disattivato
> - Tool: Nmap/Superscan/Nping — scan completa (lenta, rumorosa) o su porte specifiche

> [!warning] Contromisure ping sweep 
> **Detection:** IDS (Snort), firewall commerciali (network o desktop), tool host-based (Scanlogd, courtney, ippl, protolog) che riconoscono pattern di pacchetti ICMP/TCP/UDP da un host o rete. Non solo tool automatici: anche l'occhio umano conta. 
> **Prevention:** ACL sul firewall per limitare il traffico ICMP in ingresso; permettere solo ECHO_REPLY, HOST_UNREACHABLE, TIME_EXCEEDED verso host specifici in DMZ, solo dagli IP dell'ISP; Pingd sposta la gestione ICMP dal kernel allo user space. 
> **Nota storica:** Loki2 (Phrack) usa ICMP ECHO come canale di backdoor/tunneling — non discovery ma abuso del protocollo.

### Comandi di esempio

```bash
# ARP sweep sulla rete locale
arp-scan --interface=wlan0 --localnet

# Ping ICMP semplice
ping -c 2 192.168.1.1

# Nmap host discovery via ARP, skip port scan
sudo nmap -sn -PE --send-ip 192.168.1.1
```

> [!tip] Opzioni Nmap utili per il discovery
> 
> - `-sn` → skip port scanning (solo host discovery)
> - `-PE` → skip ARP resolution, usa ICMP echo
> - `-Pn` → salta il discovery, prova direttamente la porta (default 22)
> - `-PR` → ARP ping

---

## 2. Determinare i servizi attivi (Port Scanning)

> [!info] 3-way handshake **Client:** CLOSED → SYN-SENT (invia SYN) → ESTABLISHED (riceve SYN/ACK, invia ACK) **Server:** CLOSED → LISTEN → SYN-RECEIVED (riceve SYN, invia SYN/ACK) → ESTABLISHED (riceve ACK)

> [!info] Flag del TCP header
> 
> - **URG** — il campo Urgent pointer è significativo
> - **ACK** — il campo Acknowledgment è valido; presente su tutti i pacchetti dopo il SYN iniziale
> - **PSH** — push function, forza l'invio del buffer all'applicazione
> - **RST** — reset della connessione
> - **SYN** — sincronizza i sequence number; solo sul primo pacchetto di ciascun lato
> - **FIN** — ultimo pacchetto del mittente

### Tipi di port scan

|Scan|Meccanismo|Note|
|---|---|---|
|TCP Connect|Handshake completo|Affidabile ma loggato/tracciabile|
|TCP SYN (half-open)|SYN → SYN/ACK (aperta) o RST/ACK (chiusa), handshake mai completato|Non tracciabile come il connect scan|
|TCP FIN|Invia solo FIN|Porte chiuse rispondono RST (su stack RFC-compliant)|
|TCP Xmas Tree|FIN + URG + PSH insieme|Porte chiuse → RST|
|TCP Null|Nessun flag settato|Porte chiuse → RST|
|TCP ACK|Solo ACK|Non rivela stato porta, serve a mappare regole firewall|
|TCP Window|Come ACK scan|Distingue porte filtrate da non filtrate via window size|
|TCP RPC|Specifico per servizi RPC|—|
|UDP scan|Nessuna risposta = aperta/filtrata; ICMP port unreachable = chiusa|Risultato ambiguo se manca risposta|
Con UDP non esiste un handshake, quindi nmap non può dedurre lo stato della porta da una risposta SYN/ACK come con TCP. Se la porta è chiusa, il sistema target risponde con un messaggio ICMP "port unreachable" (tipo 3, codice 3), e questo è un segnale chiaro: nmap marca la porta come closed. Se invece la porta è aperta, nella maggior parte dei casi non arriva nessuna risposta — il pacchetto UDP viene semplicemente ricevuto dal servizio in ascolto e scartato se non è nel formato atteso, senza che il servizio risponda nulla. Risultato: nmap non distingue tra porta aperta e porta filtrata da un firewall, e la marca come open|filtered, cioè ambigua.

C'è un dettaglio in più che vale la pena aggiungere al ripasso: a volte nmap riesce comunque a disambiguare, perché per certi servizi noti (DNS, SNMP, NTP, ecc.) invia probe specifici del protocollo applicativo, e se il servizio risponde con qualcosa di sensato allora la porta viene marcata con certezza come open, non più ambigua. Inoltre c'è il fenomeno dell'ICMP message quenching citato nelle slide (RFC 1812): molti sistemi limitano il rate dei messaggi ICMP di errore per non sovraccaricarsi, quindi se scansioni tante porte UDP velocemente, anche porte effettivamente chiuse possono apparire come filtered solo perché il rate limit ha bloccato la risposta ICMP, non perché ci sia davvero un firewall in mezzo. Questo è anche uno dei motivi per cui lo scan UDP è notoriamente lento e impreciso rispetto al TCP SYN scan.

> [!warning] Limite di FIN/Xmas/Null Funzionano solo contro stack TCP/IP conformi alla RFC 793. Windows non segue questo comportamento e quindi questi scan **non sono affidabili** contro host Windows.

### Esempio output

```bash
sudo nmap -sS 192.168.1.231
```

```
PORT     STATE SERVICE
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
515/tcp  open  printer
631/tcp  open  ipp
9100/tcp open  jetdirect
```

---

## 3. Rilevare il sistema operativo (OS Fingerprinting)

> [!info] Active OS detection — fonti di informazione
> 
> - **Banner grabbing** — molte applicazioni (FTP, telnet, SMTP, HTTP, POP) si "raccontano" da sole nel banner
> - **Porte disponibili** — alcuni servizi sono OS-specific
> - **Stack fingerprinting** — differenze nell'implementazione dello stack TCP/IP tra vendor

> [!info] Guess dell'OS dalle porte note 
> **Windows:** 135 (EPMAP/end-point mapper, usato da DHCP/DNS/WINS server), 139 NetBIOS (solo Win 95/98 da sola), 445 SMB, 3389 RDP **Unix/Linux:** 22 SSH, 111 RPC portmapper, 512–514 Berkeley r-services (rlogin), 2049 NFS, porte alte 3277x RPC (tipico Solaris)

> [!info] Active stack fingerprinting 
> Origine: ricerche pubblicate su Phrack Magazine — i vendor interpretano le RFC in modo diverso quando implementano lo stack TCP/IP. Nmap `-O` confronta il comportamento osservato con un database di firme (nmap-os-fingerprints).
> 
> **Probe usati:**
> 
> - FIN probe → Windows 7/200x/Vista rispondono FIN/ACK
> - Bogus flag probe → Linux rispecchia il flag indefinito inviato
> - Initial Sequence Number sampling → pattern nell'ISN
> - "Don't fragment" bit monitoring
> - TCP initial window size
> - Valore ACK di ritorno (+0 o +1 rispetto all'atteso)
> - ICMP message quenching → rate limit degli errori (RFC 1812)
> - ICMP message quoting → quantità di info quotata nei messaggi di errore
> - ICMP echoing integrity → header IP alterati nelle risposte ICMP
> - Type of Service (TOS)
> - Gestione della frammentazione
> - TCP options

> [!info] Campi del fingerprint TCP/IP Initial packet size (16 bit), Initial TTL (8 bit), window size (16 bit), MSS (16 bit), window scaling (8 bit), flag DF (1 bit), flag SACK-OK (1 bit), flag NOP (1 bit) → combinati danno una firma a **67 bit**. In pratica, spesso **TTL iniziale + window size** bastano per identificare l'OS con buona confidenza.

### Esempio output

```bash
sudo nmap -O 192.168.1.17
```

```
Device type: general purpose
Running: Microsoft Windows XP
OS details: Microsoft Windows XP SP2 or SP3
Network Distance: 1 hop
```

> [!info] Passive OS detection 
> Tecnica stealth verso un IDS: nessun pacchetto inviato, solo sniffing (es. via port mirroring su uno switch). Tool: **Siphon** — port-mapping passivo, OS identification, topologia di rete, basato su firme in `osprints.conf` (TTL, window size, flag DF, ecc.)
> 
> **Quando fallisce:**
> 
> 1. l'applicazione costruisce pacchetti custom (non segue lo stack OS standard)
> 2. non si riesce a catturare il traffico
> 3. l'host remoto cambia gli attributi della connessione (in questo caso fallisce anche l'active detection)

> [!example] Esempio pratico (attacco da slide) Telnet da `shadow` (192.168.1.10) verso `quake` (192.168.1.11). Snort cattura il pacchetto: `TTL:255`, `Win:0x2798`, flag SYN+ACK. Confrontando questi valori col database `osprints.conf` (grep su "solaris") si trova match su **Solaris 2.6–2.7**. Siphon conferma lo stesso risultato in modalità passiva live.

> [!warning] Contromisure OS detection **Detection:** stessi strumenti che rilevano lo scan stesso (es. uso di SYN flag anomalo) — Snort, Scanlogd, ecc. **Prevention:** alterare le caratteristiche uniche dello stack (sconsigliato, rischio di instabilità), proxy/firewall sicuri, Active Defence.

---

## 4. Processare e salvare i dati raccolti

> [!info] Perché serve uno storage strutturato 
> Su reti grandi l'efficienza nella gestione dei dati di scan determina la velocità con cui si riesce a compromettere più sistemi — non basta raccogliere i dati, vanno organizzati e interrogabili.

> [!info] Metasploit come database di scan Usa **PostgreSQL** come backend.
> 
> - `db_connect postgres:<password>@localhost:<port>/msf3` → connette Metasploit al DB
> - `db_nmap` (richiede root) → lancia Nmap da dentro Metasploit (più lento del Nmap diretto, ma i risultati finiscono già nel DB)
> - `db_import <file>` → importa risultati Nmap (es. XML da `-oX`) nel database
> - `hosts` → mostra host scoperti e relativo OS
> - `services` → mostra porte/servizi trovati
> - filtro `-s` → query mirate (es. tutti gli host con SSH attivo o Windows 2008)

### Workflow tipico

```bash
msf > db_connect postgres:<password>@localhost:<port>/msf3
msf > db_nmap 192.168.1.0/24
msf > hosts
msf > services -s ssh
```

Oppure import esterno:

```bash
sudo nmap -O 192.168.1.0/24 -oX subnet_192.168.1.0-OS
msf > db_import subnet_192.168.1.0-OS
```

---

## Tabella riassuntiva — quale tool per cosa

|Obiettivo|Tool principali|
|---|---|
|Host discovery (locale)|arp-scan, nmap -PR -sn|
|Host discovery (remoto)|ping, nmap, hping3/nping, Superscan|
|Port scanning|nmap (-sS, -sT, -sF, -sX, -sN, -sA, -sW), Superscan|
|OS fingerprinting attivo|nmap -O|
|OS fingerprinting passivo|Siphon|
|Storage/gestione scan su larga scala|Metasploit + PostgreSQL|
|Detection scan in corso|Snort, Scanlogd, courtney, ippl, protolog|

---

> [!question] Punto aperto dal ripasso Le slide coprono solo gli scan TCP "classici" (connect/SYN/FIN/Xmas/Null/ACK/Window/RPC) + UDP, senza decoy scan, idle/zombie scan o fragmentation scan come tecnica a sé. Verificare se il libro li tratta e se rientrano nel programma d'esame.

## Collegamenti

- [[ETHL 0x09 — Risultato e Handoff Ripasso]]
- lezione successiva [[ETH - Hacking Exposed 7 - Cap 3 - Enumeration]]