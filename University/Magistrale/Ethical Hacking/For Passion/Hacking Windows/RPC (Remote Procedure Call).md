# RPC — Remote Procedure Call

**Tags:** #windows #protocol #enumeration #post-exploitation #htb  
**Fonte:** Hacking Exposed 7 — Cap. 3 + Cap. 4  
**Correlato:** [[NetBIOS_NBSS]] · [[SMB]] · [[Null_Session]] · [[Active_Directory]] · [[DCOM]]

---

## Cos'è

RPC è un meccanismo che permette a un processo di **chiamare una funzione che gira su un altro processo o su un altro host**, come se fosse una chiamata locale. Il chiamante non sa (e non gli interessa) dove fisicamente viene eseguito il codice.

```
Programma A                         Programma B (anche su host remoto)
─────────────────────────           ──────────────────────────────────
risultato = somma(3, 5)   ───────►  int somma(int a, int b) { return a+b; }
                          ◄───────  ritorna 8
```

Il meccanismo che rende tutto questo trasparente si chiama **stub**.

---

## Come funziona — i concetti chiave

### Stub e marshaling

Per ogni funzione esposta via RPC esistono due stub automaticamente generati:

|Stub|Dove gira|Cosa fa|
|---|---|---|
|**Client stub**|lato chiamante|serializza i parametri (**marshaling**), invia la richiesta|
|**Server stub**|lato ricevente|deserializza i parametri (**unmarshaling**), chiama la funzione reale, rimanda il risultato|

**Marshaling** = convertire i parametri in un formato trasmissibile in rete (byte stream). Gestisce differenze di architettura (endianness, dimensione dei tipi), puntatori, strutture complesse.

### Endpoint Mapper

Il server RPC non ascolta su una porta fissa per ogni servizio. Usa un componente centrale chiamato **Endpoint Mapper (EPM)**:

```
Client                        Endpoint Mapper (porta 135)        Servizio reale
  │                                      │                              │
  │── "dove trovo il servizio X?" ──────►│                              │
  │◄─────────────── "porta 49152" ───────│                              │
  │                                      │                              │
  │─────────────── connessione diretta ──────────────────────────────►  │
```

**Porta 135/TCP** = sempre l'Endpoint Mapper. Le porte effettive dei servizi sono **dinamiche** (range 49152–65535 su Windows moderno, 1024–65535 su sistemi legacy).

### Interface UUID

Ogni servizio RPC si identifica con un **UUID** (Universally Unique Identifier), ad esempio:

```
SAMR  (SAM Remote):      12345778-1234-abcd-ef00-0123456789ac
LSARPC (LSA Remote):     12345778-1234-abcd-ef00-0123456789ab
SVCCTL (Service Control): 367abb81-9844-35f1-ad32-98f038001003
```

Il client chiede all'EPM: "dammi l'endpoint per questo UUID" → riceve la porta dinamica → si connette.

---

## MSRPC — l'implementazione Microsoft

Microsoft ha implementato RPC su Windows basandosi su **DCE/RPC** (Distributed Computing Environment, standard Open Group). La versione Microsoft si chiama **MSRPC**.

### Transport supportati

|Transport|Dettaglio|
|---|---|
|**TCP/IP**|Più comune, usa EPM su porta 135|
|**Named Pipes (SMB)**|RPC tunnelato dentro SMB — porta 445. Usato da molti servizi AD|
|**NetBIOS**|Legacy, porta 139|
|**HTTP**|RPC over HTTP — per accesso remoto attraverso firewall|

> Molti servizi Windows usano **RPC over Named Pipes**: la comunicazione RPC viaggia dentro una pipe SMB. Per questo SMB/445 è così critico in ambienti AD.

### Servizi Windows che usano MSRPC

|Servizio|UUID / Pipe|Cosa espone|
|---|---|---|
|**SAMR**|`\pipe\samr`|Gestione account SAM — utenti, gruppi locali|
|**LSARPC**|`\pipe\lsarpc`|Policy LSA, SID lookup, trust|
|**SVCCTL**|`\pipe\svcctl`|Service Control Manager — start/stop servizi|
|**WINREG**|`\pipe\winreg`|Accesso remoto al registry|
|**DRSUAPI**|dinamico|Directory Replication Service — usato da DCSync|
|**NETLOGON**|`\pipe\netlogon`|Autenticazione domain, Secure Channel|
|**EPMAPPER**|porta 135|Endpoint Mapper stesso|

---

## Rilevanza offensiva

### Enumerazione via rpcclient (null session o credenziali)

`rpcclient` permette di chiamare funzioni MSRPC direttamente da riga di comando.

```bash
# Connessione con null session
rpcclient -U "" -N 10.10.10.x

# Connessione con credenziali
rpcclient -U "user%password" 10.10.10.x
```

**Comandi utili una volta connesso:**

```bash
# Enumerazione utenti
enumdomusers                  # lista utenti del dominio
enumdomgroups                 # lista gruppi
queryuser 0x3e8               # dettagli su un utente (RID in hex)
querygroupmem 0x200           # membri di un gruppo (es. Domain Admins = 0x200)

# SID/RID lookup
lookupnames Administrator     # ottieni SID da nome
lookupsids S-1-5-21-...-500   # ottieni nome da SID

# Info sistema
srvinfo                       # info sul server
netshareenumall               # share disponibili

# LSA
lsaquery                      # policy LSA
dsrolegetprimarydomininfo     # ruolo del DC
```

### Enumerazione automatica — enum4linux / enum4linux-ng

Wrapper che usa rpcclient, smbclient, nmblookup automaticamente:

```bash
enum4linux -a 10.10.10.x          # full enum (users, groups, shares, OS)
enum4linux-ng -A 10.10.10.x       # versione modernizzata
```

### Footprinting dell'Endpoint Mapper

```bash
# Scopri tutti i servizi RPC esposti (con nmap)
nmap -p 135 --script msrpc-enum 10.10.10.x

# Con impacket
python3 rpcdump.py 10.10.10.x
# → lista UUID, nomi servizi, porte dinamiche assegnate
```

Output tipico di rpcdump:

```
Protocol: [MS-SAMR]: Security Account Manager
Provider: samsrv.dll
UUID    : 12345778-1234-ABCD-EF00-0123456789AC v1.0
Bindings:
          ncacn_np:\\HOSTNAME[\pipe\samr]
          ncacn_ip_tcp:10.10.10.x[49670]
```

### DCSync via DRSUAPI

DCSync (Mimikatz `lsadump::dcsync`) usa l'interfaccia RPC **DRSUAPI** per simulare una replica tra DC. Non tocca LSASS del DC — fa chiamate RPC legittime.

```
Mimikatz → DRSUAPI RPC → DC → risponde con hash utenti
```

→ collegamento diretto con [[Mimikatz]] e [[Golden_Ticket]].

---

## Vettori di attacco comuni

|Attacco|Meccanismo RPC|
|---|---|
|**Null Session**|SAMR/LSARPC accessibili senza autenticazione — enumerazione utenti/gruppi|
|**MS03-026**|Buffer overflow nel parser RPC di Windows XP/2003 — portò a Blaster worm|
|**MS17-010 (EternalBlue)**|SMBv1, ma il payload interagisce con servizi via named pipe RPC|
|**DCSync**|Abuso legittimo di DRSUAPI — richiede privilegi alti|
|**PetitPotam**|EFSRPC (Encrypting File System RPC) — coerce NTLM auth del DC verso un relay|
|**PrintNightmare**|RPRN (Print Spooler RPC) — RCE / LPE|

---

## Workflow tipico in HTB

```
1. nmap -p 135,445 → porta 135 aperta
       ↓
2. rpcdump.py → scopri servizi esposti (SAMR? LSARPC? DRSUAPI?)
       ↓
3a. rpcclient null session → enumdomusers → lista utenti
3b. enum4linux-ng → dump completo
       ↓
3. Utenti trovati → password spray / brute force
       ↓
4. Con credenziali → rpcclient con auth → più info (gruppi, SID)
       ↓
5. Se DA → lsadump::dcsync via DRSUAPI → hash krbtgt → Golden Ticket
```

---

## Difese

|Difesa|Effetto|
|---|---|
|Firewall su porta 135|Blocca accesso esterno all'EPM|
|`RestrictAnonymous = 2`|Disabilita null session su SAMR/LSARPC|
|Disabilitare servizi RPC non necessari|Riduce superficie (es. Print Spooler se non serve)|
|Segmentazione di rete|Limita chi può raggiungere i DC su 135/445|

---

## Note rapide

- Porta **135** = sempre EPM. Le porte effettive dei servizi sono **dinamiche**.
- RPC over Named Pipes viaggia su **SMB/445** — se 445 è aperto, molti servizi RPC sono raggiungibili anche senza 135.
- **impacket** (Python) ha molti tool RPC: `rpcdump.py`, `samrdump.py`, `lookupsid.py`, `secretsdump.py` — fondamentali in HTB.
- `secretsdump.py` di impacket usa DRSUAPI + SAMR per dumpare hash remoti senza Mimikatz.

---

## Riferimenti

- HE7 Cap. 3 — Enumeration
- HE7 Cap. 4 — Hacking Windows
- [[Null_Session]] — IPC$, RestrictAnonymous
- [[SMB]] — named pipes, trasporto RPC
- [[Mimikatz]] — DCSync via DRSUAPI
- [[NetBIOS_NBSS]] — trasporto legacy RPC