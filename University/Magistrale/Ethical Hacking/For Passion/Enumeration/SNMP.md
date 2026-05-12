# SNMP — Simple Network Management Protocol

Tags: #networking #enumeration #snmp #hacking-exposed #udp

---

## Cos'è

SNMP è un protocollo per il **monitoraggio e la gestione di dispositivi di rete** — router, switch, stampanti, server, firewall. Permette a un sistema centrale (NMS — Network Management Station) di interrogare e configurare dispositivi remoti.

Gira su **UDP porta 161** (query) e **UDP porta 162** (trap — notifiche spontanee dal dispositivo).

---

## Architettura SNMP

```
NMS (Network Management Station)
        │
        │  UDP 161 (query/response)
        │  UDP 162 (trap — notifiche)
        ▼
   SNMP Agent
(router, switch, server...)
        │
        ▼
   MIB (Management Information Base)
   database di oggetti gestibili
```

- **NMS** — il sistema che interroga (es. Nagios, Zabbix, SolarWinds)
- **Agent** — il demone SNMP sul dispositivo gestito
- **MIB** — database gerarchico che definisce tutti gli oggetti interrogabili (interfacce, CPU, tabella di routing, utenti...)
- **OID** (Object Identifier) — indirizzo univoco di ogni oggetto nel MIB, es. `1.3.6.1.2.1.1.1.0` = sysDescr (descrizione sistema)

---

## Le tre versioni

|Versione|Anno|Autenticazione|Cifratura|Sicurezza|
|---|---|---|---|---|
|**SNMPv1**|1988|Community string|❌ Nessuna|❌ Pessima|
|**SNMPv2c**|1996|Community string|❌ Nessuna|❌ Pessima|
|**SNMPv3**|2002|Username + password|✅ AES/DES|✅ Buona|

> v1 e v2c trasmettono tutto in **chiaro** inclusa la community string — sniffando il traffico UDP 161 ottieni le credenziali gratuitamente.

---

## Community String — il meccanismo di autenticazione debole

In SNMPv1 e v2c, l'autenticazione è basata su una **community string** — essenzialmente una password in chiaro nel pacchetto UDP.

Due community string di default universalmente note:

|Community String|Accesso|Default su|
|---|---|---|
|`public`|**Read-only**|Quasi tutti i dispositivi|
|`private`|**Read-write**|Molti dispositivi|

Se il sysadmin non le cambia — e spesso non lo fa — puoi interrogare il dispositivo con `public` e **modificarne la configurazione** con `private`.

---

## Operazioni SNMP

|Operazione|Direzione|Descrizione|
|---|---|---|
|`GET`|NMS → Agent|Richiede il valore di un OID specifico|
|`GET-NEXT`|NMS → Agent|Richiede il prossimo OID nella gerarchia|
|`GET-BULK`|NMS → Agent|Richiede blocchi di dati (v2c+)|
|`SET`|NMS → Agent|Modifica il valore di un OID|
|`TRAP`|Agent → NMS|Notifica spontanea (evento, errore)|
|`WALK`|NMS → Agent|Traversa l'intero MIB ricorsivamente|

`SNMP WALK` è quello più usato in enumerazione — scarica l'intero albero MIB del dispositivo.

---

## Cosa si può enumerare

Su un dispositivo con SNMP mal configurato (community string di default) si ottiene:

|Categoria OID|Informazioni|
|---|---|
|**System** (1.3.6.1.2.1.1)|OS, hostname, uptime, descrizione hardware|
|**Interfaces** (1.3.6.1.2.1.2)|Interfacce di rete, MAC address, velocità, stato|
|**IP** (1.3.6.1.2.1.4)|Routing table, ARP table, indirizzi IP|
|**TCP** (1.3.6.1.2.1.6)|Connessioni TCP attive, porte in ascolto|
|**UDP** (1.3.6.1.2.1.7)|Porte UDP in ascolto|
|**SNMP** (1.3.6.1.2.1.11)|Statistiche SNMP|
|**Windows MIB**|Utenti, share, processi, servizi, software installato|

Su **dispositivi Windows** con SNMP abilitato il MIB espone:

- Lista completa degli **utenti locali**
- **Share** di rete
- **Processi** in esecuzione
- **Servizi** attivi e fermi
- **Software installato**
- **Percorsi** di file e directory

---

## Enumerazione con snmpwalk

```bash
# Walk completo con community string "public"
snmpwalk -v2c -c public 192.168.1.50

# Walk completo SNMPv1
snmpwalk -v1 -c public 192.168.1.50

# Query su OID specifico — descrizione sistema
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.2.1.1.1.0

# Interfacce di rete
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.2.1.2

# Routing table
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.2.1.4.21

# Utenti Windows
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.4.1.77.1.2.25

# Processi Windows
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.2.1.25.4.2.1.2

# Software installato Windows
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.2.1.25.6.3.1.2

# Share Windows
snmpwalk -v2c -c public 192.168.1.50 1.3.6.1.4.1.77.1.2.27
```

---

## Brute force community string

Se `public` e `private` non funzionano:

```bash
# onesixtyone — scanner SNMP veloce con wordlist
onesixtyone -c /usr/share/wordlists/seclists/Discovery/SNMP/snmp.txt 192.168.1.50

# Scan su subnet intera
onesixtyone -c community_strings.txt 192.168.1.0/24

# Metasploit — SNMP community scanner
use auxiliary/scanner/snmp/snmp_login
set RHOSTS 192.168.1.50
set PASS_FILE /usr/share/wordlists/metasploit/snmp_default_pass.txt
run

# nmap NSE
nmap -sU -p 161 --script snmp-brute 192.168.1.50
```

---

## Enumerazione con Nmap NSE

```bash
# Rileva SNMP e versione
sudo nmap -sU -p 161 -sV 192.168.1.50

# Enumera informazioni di sistema
nmap -sU -p 161 --script snmp-sysdescr 192.168.1.50

# Enumera interfacce
nmap -sU -p 161 --script snmp-interfaces 192.168.1.50

# Enumera processi
nmap -sU -p 161 --script snmp-processes 192.168.1.50

# Enumera software installato
nmap -sU -p 161 --script snmp-win32-software 192.168.1.50

# Enumera utenti Windows
nmap -sU -p 161 --script snmp-win32-users 192.168.1.50

# Tutto insieme
nmap -sU -p 161 --script snmp-* 192.168.1.50
```

---

## SNMP SET — scrittura come vettore di attacco

Con la community string **read-write** (`private`) puoi **modificare** la configurazione del dispositivo:

```bash
# Modifica sysName (nome del sistema)
snmpset -v2c -c private 192.168.1.1 1.3.6.1.2.1.1.5.0 s "hacked"

# Su router Cisco — modifica routing table
# Su switch — modifica VLAN configuration
# Su Windows — modifica valori di registro esposti via SNMP
```

Su dispositivi di rete (router/switch) con `private` attivo si può:

- Modificare la routing table → redirect del traffico
- Scaricare la configurazione completa via TFTP
- Riconfigurare interfacce

---

## SNMP Trap — notifiche spontanee UDP 162

I trap sono messaggi che il dispositivo invia spontaneamente alla NMS quando avviene un evento:

```
Router → UDP 162 → NMS: "interfaccia eth0 down"
Server → UDP 162 → NMS: "CPU al 98% da 5 minuti"
Switch → UDP 162 → NMS: "nuovo dispositivo connesso alla porta 12"
```

Dal punto di vista dell'attaccante, **sniffando UDP 162** si raccolgono:

- Topologia di rete (quali dispositivi esistono)
- Community string in chiaro (nei pacchetti trap v1/v2c)
- Eventi di sicurezza in tempo reale

---

## Workflow su HTB

```
1. sudo nmap -sU -p 161 <target>
              ↓  porta aperta
2. snmpwalk -v2c -c public <target>
              ↓  dumpa il MIB
3. Cerca: utenti, processi, software, share
              ↓
4. onesixtyone se "public" non funziona
              ↓  trova community string
5. snmpwalk con community string trovata
              ↓
6. Informazioni per pivot successivo
```

---

## SNMPv3 — la versione sicura

SNMPv3 introduce autenticazione e cifratura reali:

|Feature|Dettaglio|
|---|---|
|Autenticazione|MD5 o SHA — verifica identità|
|Cifratura|DES o AES — cifra il payload|
|Username|Sostituisce la community string|
|Context|Permette SNMP su più istanze|

Anche SNMPv3 è vulnerabile a **brute force** se le credenziali sono deboli:

```bash
# Nmap — brute force SNMPv3
nmap -sU -p 161 --script snmp-brute --script-args snmp-brute.version=3 192.168.1.50
```

---

## Contromisure

|Contromisura|Dettaglio|
|---|---|
|**Usare SNMPv3**|Autenticazione + cifratura reali|
|**Cambiare community string**|Mai lasciare `public`/`private`|
|**Bloccare UDP 161/162**|Firewall — accessibile solo dalla NMS|
|**ACL sul dispositivo**|Solo IP della NMS autorizzati|
|**Disabilitare SNMP**|Se non necessario — superficie zero|
|**SNMP read-only**|Mai esporre community read-write|

---

## OID importanti da ricordare

```
1.3.6.1.2.1.1.1.0     sysDescr        — descrizione sistema (OS, versione)
1.3.6.1.2.1.1.3.0     sysUpTime       — uptime
1.3.6.1.2.1.1.5.0     sysName         — hostname
1.3.6.1.2.1.2         ifTable         — interfacce di rete
1.3.6.1.2.1.4.21      ipRouteTable    — routing table
1.3.6.1.2.1.6.13      tcpConnTable    — connessioni TCP attive
1.3.6.1.4.1.77.1.2.25 hrSWRunName     — utenti Windows
1.3.6.1.2.1.25.4.2.1.2 hrSWRunName   — processi in esecuzione
1.3.6.1.2.1.25.6.3.1.2 hrSWInstalledName — software installato
1.3.6.1.4.1.77.1.2.27  lanmanShares  — share Windows
```

---

## The real-world scenario

Good question. The confusion is understandable because SNMP is an **infrastructure management protocol** — not something end users ever touch. Let me give you a concrete mental model.

Imagine you're a sysadmin managing 200 devices — 50 routers, 30 switches, 80 servers, 40 printers. You can't physically walk to each one to check if it's working. You need a central dashboard that tells you:

- Is router #12 alive?
- What's the CPU load on server #45?
- Did any interface go down in the last hour?
- How much disk space is left on each server?

SNMP is the protocol that makes this possible. Every device runs a small **SNMP agent** in the background. Your central monitoring system (NMS) sends SNMP queries to each device, gets back numbers and strings, and displays everything on a dashboard.

---

## Concretely what happens

```
NMS asks router:    "give me OID 1.3.6.1.2.1.2.2.1.10"
Router answers:     "4382910 bytes"
NMS understands:    that's the bytes received on interface eth0
NMS displays:       a graph of network throughput over time
```

```
NMS asks server:    "give me OID 1.3.6.1.2.1.25.3.3.1.2"
Server answers:     "73"
NMS understands:    CPU load is 73%
NMS triggers:       an alert email to the sysadmin
```

The NMS does this for every device, every 60 seconds, automatically.

---

## Why it's dangerous for an attacker

The SNMP agent answers **anyone who sends the right community string**. There's no IP verification in v1/v2c, no encryption, no session.

So from an attacker's perspective:

```
You send:   snmpwalk -v2c -c public 192.168.1.1
Router:     here is my entire configuration, routing table,
            all interfaces, all connected devices,
            all active connections, my OS version,
            my hostname, my uptime...
```

You get the same data the sysadmin's dashboard gets — a complete picture of the device internals — **without authenticating**.

---

## The mental model

Think of each device as a building. SNMP is a window on the side — designed for the building manager to look inside and check everything is okay. The community string is supposed to be the lock on that window.

If the lock is the default (`public`) — which it very often is — **anyone walking by can look through the window and see everything inside**.

On Windows machines specifically, that window shows you running processes, installed software, open shares, and user accounts — which is essentially everything you need to plan the next step of an attack.

---
## Where you definitely find it

Yes, very much so — SNMP is still widely used in 2025, especially in enterprise and ISP environments.

**Network devices** — Cisco routers and switches ship with SNMP enabled by default. Every major ISP uses SNMP to monitor their backbone infrastructure. It's the backbone of tools like Nagios, Zabbix, PRTG, SolarWinds — which are standard in any enterprise NOC (Network Operations Center).

**Printers** — almost every networked printer runs an SNMP agent. It's how the print management software knows ink levels, paper jams, page counts.

**UPS and power equipment** — data centers use SNMP to monitor power units and trigger graceful shutdowns before a power failure.

**Industrial equipment** — SCADA and industrial control systems often expose SNMP for monitoring.

---

## The realistic security picture in 2025

|Environment|Reality|
|---|---|
|Large enterprise with dedicated network team|SNMPv3 with proper credentials, ACLs|
|Small/medium company, no dedicated network admin|SNMPv2c with `public`/`private` still active|
|Legacy infrastructure (old routers, old switches)|SNMPv1, default community strings, never touched|
|ISP backbone devices|SNMP heavily used, usually well secured|
|Printers|Almost always SNMPv1/v2c with `public`, never hardened|

The interesting real-world finding from pentest reports: **printers** are consistently the worst offenders. They sit on the corporate network for 10 years, nobody thinks about securing them, and their SNMP agent happily gives out network topology information to anyone who asks.

---

## The shift happening now

SNMPv3 adoption has been slow but is accelerating — mainly because compliance frameworks like PCI DSS and ISO 27001 explicitly flag SNMPv1/v2c as a risk. But the installed base of legacy devices running v1/v2c is enormous and won't disappear for decades.

The other shift is that SNMP is being partially replaced by **NETCONF/YANG** and **gRPC telemetry** on modern network devices — these are more secure and efficient protocols for the same monitoring job. But SNMP will be around for a long time simply because of how much legacy equipment depends on it.

---

## Bottom line for your studies

On a real internal pentest, finding UDP 161 open with default community strings is still very common — especially on printers, old switches, and any device that hasn't been touched since it was installed. It's not the flashiest finding but it often gives you network topology information that makes everything else easier.

---
## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- RFC 1157 — SNMPv1
- RFC 3416 — SNMPv2
- RFC 3410 — SNMPv3
- `man snmpwalk`
- `man onesixtyone`
- → vedi anche: [[Null Session]]
- → vedi anche: [[NetBIOS]] (TCP 139/445)