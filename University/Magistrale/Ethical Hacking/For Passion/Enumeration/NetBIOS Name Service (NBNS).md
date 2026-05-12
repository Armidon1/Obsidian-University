# NetBIOS Name Service (NBNS) — UDP 137

Tags: #networking #enumeration #netbios #windows #hacking-exposed

---

## Cos'è

NBNS è essenzialmente il **DNS per reti locali Windows** — risolve nomi human-readable come `DESKTOP-CORP01` in indirizzi IP, ma funziona tramite **broadcast sulla subnet locale** invece di un server DNS dedicato.

---

## Le tre porte NetBIOS

|Porta|Protocollo|Servizio|Scopo|
|---|---|---|---|
|UDP 137|NetBIOS-NS|Name Service|Registrazione e risoluzione nomi|
|UDP 138|NetBIOS-DGM|Datagram Service|Messaggi connectionless e broadcast|
|TCP 139|NetBIOS-SSN|Session Service|Trasferimento dati reale (file/print sharing)|

> La porta 137 è quella che espone più informazioni durante l'enumerazione.

---

## Come funziona

Ogni macchina Windows **registra il proprio nome** broadcastando su UDP 137:

```
DESKTOP-CORP01 → broadcast UDP 137 → "Sono DESKTOP-CORP01, il mio IP è 192.168.1.50"
```

Quando un'altra macchina cerca `DESKTOP-CORP01` può:

- Broadcastare una **Name Query Request** su UDP 137
- Interrogare un **WINS server** (Windows Internet Name Service — server NetBIOS dedicato per reti grandi)

---

## Record NetBIOS — i suffissi

Ogni macchina registra **più nomi** con suffissi diversi che indicano il ruolo del servizio:

|Nome|Suffisso|Tipo|Significato|
|---|---|---|---|
|`MACHINENAME`|`<00>`|Unique|Workstation service — macchina attiva in rete|
|`MACHINENAME`|`<20>`|Unique|File Server service — **file sharing attivo** ⚠️|
|`MACHINENAME`|`<03>`|Unique|Messenger service|
|`DOMAIN`|`<00>`|Group|Appartenenza al dominio/workgroup|
|`DOMAIN`|`<1C>`|Group|**Domain Controllers** del dominio ⚠️|
|`DOMAIN`|`<1B>`|Unique|Domain Master Browser|
|`USERNAME`|`<03>`|Unique|**Utente attualmente loggato** ⚠️|

> Il suffisso `<20>` indica file sharing attivo → target per SMB enumeration Il suffisso `<1C>` identifica i Domain Controllers → pivot verso DC Il suffisso `<03>` sul nome utente rivela chi è loggato in questo momento

---

## Enumerazione da Windows — nbtstat

```cmd
# Interroga la tabella NetBIOS di una macchina specifica
nbtstat -a 192.168.1.50

# Interroga per nome
nbtstat -A DESKTOP-CORP01

# Mostra la propria tabella NetBIOS
nbtstat -n

# Mostra la cache dei nomi risolti di recente
nbtstat -c
```

### Esempio output `nbtstat -a 192.168.1.50`

```
Name               Type         Status
----------------------------------------------
DESKTOP-CORP01 <00>  UNIQUE      Registered   ← workstation attiva
CORPORATE      <00>  GROUP       Registered   ← membro del dominio CORPORATE
DESKTOP-CORP01 <20>  UNIQUE      Registered   ← file sharing attivo ⚠️
CORPORATE      <1C>  GROUP       Registered   ← DC presente nel dominio ⚠️
JOHN           <03>  UNIQUE      Registered   ← utente JOHN loggato ⚠️
```

Da questa singola query conosci: nome macchina, dominio, che file sharing è attivo, e **chi è loggato**.

---

## Enumerazione da Linux

```bash
# nmblookup — interroga nomi NetBIOS da Linux
nmblookup -A 192.168.1.50

# Scansiona intera subnet per nomi NetBIOS
nmblookup -A 192.168.1.0/24

# enum4linux — enumerazione completa NetBIOS/SMB
enum4linux -a 192.168.1.50

# nbtscan — scanner dedicato per NetBIOS su subnet
nbtscan 192.168.1.0/24
```

### Output tipico nbtscan

```bash
nbtscan 192.168.1.0/24

192.168.1.50    DESKTOP-CORP01  CORPORATE       JOHN
192.168.1.51    DC01            CORPORATE       <server>
192.168.1.52    FILESERVER      CORPORATE       <server>
```

In un comando solo: tutte le macchine Windows attive, nomi, dominio, e utenti loggati.

---

## Cosa estrae un attaccante da NBNS

|Informazione|Come è utile|
|---|---|
|Nomi delle macchine|Identificare DC, file server, workstation|
|Nome del dominio|Conferma ambiente AD, necessario per attacchi successivi|
|Utenti loggati|Lista username per attacchi a password|
|File sharing attivo (`<20>`)|Target per SMB enumeration|
|DC identificato (`<1C>`)|Pivot verso Domain Controller|

---

## NBNS Spoofing — uso offensivo

Oltre all'enumerazione passiva, UDP 137 è sfruttabile attivamente. Poiché NBNS usa **broadcast non autenticati**, un attaccante può **rispondere alle query prima del server legittimo**:

```
Victim broadcast:  "chi è FILESERVER?"
Attaccante:        "Sono io FILESERVER, IP 192.168.1.99"  ← IP attaccante
Victim:            si connette all'attaccante credendo sia FILESERVER
```

Questa è la base di **Responder** — uno dei tool più potenti nel pentesting di reti interne. Avvelena le risposte NBNS (e LLMNR) per catturare **hash NTLMv2** dalle macchine che tentano di autenticarsi al server falso.

```bash
# Lancia Responder sulla tua interfaccia
sudo responder -I eth0

# Le vittime che si connettono al server fake inviano hash NTLMv2
# → crackabili offline con hashcat
hashcat -m 5600 captured.hash rockyou.txt
```

> 🔥 Responder/NBNS spoofing è ancora estremamente efficace anche su reti moderne — è una delle prime cose che un pentester lancia su un engagement interno.

---

## net view — enumerazione domini e workgroup

```cmd
# Lista tutti i workgroup e domini visibili in rete
net view /domain

# Lista tutte le macchine in un dominio/workgroup specifico
net view /domain:CORPORATE

# Lista le risorse condivise di una macchina specifica
net view \\DC01
```

### Workflow classico

```cmd
net view /domain              → scopri nomi dei domini
net view /domain:CORPORATE    → lista macchine nel dominio
net view \\DC01               → lista share sul DC
net use \\DC01\IPC$ "" /user:"" → tentativo null session
```

> La **null session** (credenziali vuote su IPC$) funzionava su Windows NT/2000/XP — bloccata di default su Windows moderni.

---

## Limitazioni

- `net view` richiede di essere già **su una macchina Windows** nella rete
- NetBIOS non instrada → vedi solo macchine sulla **stessa subnet**
- **Browser Service disabilitato di default** su Windows 10/11 recenti e Server 2019+
- Firewall che blocca **UDP 137/138 / TCP 139** interrompe tutto

---

## Rilevanza oggi

L'enumerazione NBNS grezza è meno impattante su reti moderne ben configurate, ma rimane viva su:

- Reti enterprise legacy con Windows Server 2008/2012
- Reti che non hanno disabilitato NetBIOS esplicitamente
- Macchine HTB che simulano ambienti realistici datati

Il **NBNS spoofing con Responder** è invece pienamente attuale e uno dei vettori più efficaci su engagement interni reali.

---

## Contromisure

- Disabilitare NetBIOS over TCP/IP su tutte le macchine che non ne hanno bisogno
- Bloccare UDP 137/138 e TCP 139 sul perimetro di rete
- Monitorare NBNS spoofing con IDS di rete
- Usare solo DNS moderno dove possibile

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- `man nbtscan`
- `man nmblookup`
- Responder: https://github.com/lgandx/Responder