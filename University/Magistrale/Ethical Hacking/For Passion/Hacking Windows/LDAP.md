# LDAP — Lightweight Directory Access Protocol

## Cos'è e perché esiste

LDAP è un **protocollo per interrogare e modificare directory service**. Una "directory" in questo contesto non è una cartella nel filesystem — è un database specializzato per memorizzare informazioni gerarchiche su utenti, gruppi, computer, e altre entità di un'organizzazione.

LDAP è la versione "leggera" di un protocollo più vecchio chiamato **X.500/DAP** (Directory Access Protocol), che girava su stack OSI completo ed era troppo pesante per essere usato in pratica. LDAP gira su TCP/IP direttamente, è semplice da implementare, ed è diventato lo standard de facto.

> [!analogy] Concetto familiare Pensa a LDAP come a un **database read-heavy** ottimizzato per:
> 
> - Letture frequenti (lookup utente, lookup gruppi, autenticazione)
> - Strutture gerarchiche (organizzazioni con divisioni, dipartimenti, team)
> - Schemi rigidi (ogni entità ha campi predefiniti)
> 
> È simile a un albero (filesystem hierarchy) ma con attributi tipizzati su ogni nodo.

### Porte

|Servizio|Porta|Note|
|---|---|---|
|LDAP|389/TCP|Plaintext (o StartTLS)|
|LDAPS|636/TCP|LDAP su TLS dall'inizio|
|Global Catalog|3268/TCP|Subset dell'AD forest-wide|
|GC over SSL|3269/TCP|Idem ma cifrato|

---

## Il modello dati: l'albero della directory

LDAP organizza i dati in un **albero gerarchico** (DIT — Directory Information Tree). Ogni nodo dell'albero è un **entry**, identificato univocamente dal suo **Distinguished Name (DN)**.

```
                 dc=corp,dc=local            ← root del dominio
                /              \
           ou=Users          ou=Computers
          /    |    \           |    \
     alice  bob   admin       WS01   WS02
```

Esempio di DN completo per l'utente alice:

```
cn=alice,ou=Users,dc=corp,dc=local
```

Lettura da destra a sinistra (come un path inverso):

- `dc=local` — top-level domain component
- `dc=corp` — secondo livello
- `ou=Users` — organizational unit "Users"
- `cn=alice` — common name "alice"

### Componenti del DN

|Codice|Significato|Esempio|
|---|---|---|
|`dc`|Domain Component|`dc=corp,dc=local`|
|`ou`|Organizational Unit|`ou=Sales`|
|`cn`|Common Name|`cn=Alice Smith`|
|`o`|Organization|`o=Acme Corp`|
|`c`|Country|`c=IT`|
|`uid`|User ID (more in OpenLDAP)|`uid=alice`|

> [!note] DN vs RDN Il **DN** è il path assoluto completo dell'entry. L'**RDN** (Relative DN) è solo l'ultimo pezzo — il nome dell'entry relativo al suo parent. `cn=alice` è l'RDN, `cn=alice,ou=Users,dc=corp,dc=local` è il DN.

---

## Schema e attributi

Ogni entry LDAP ha:

1. Un **DN** che lo identifica univocamente
2. Una o più **objectClass** che definiscono il "tipo" dell'entry
3. Una serie di **attributi** con valori

Esempio entry utente in AD:

```ldif
dn: cn=alice,ou=Users,dc=corp,dc=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: alice
sAMAccountName: alice
userPrincipalName: alice@corp.local
displayName: Alice Smith
memberOf: cn=Domain Users,cn=Users,dc=corp,dc=local
userAccountControl: 512
pwdLastSet: 133450123456789012
servicePrincipalName: HTTP/webserver.corp.local
```

Le **objectClass** sono come tipi/classi in un linguaggio OO: definiscono quali attributi sono obbligatori e quali opzionali. L'entry sopra è un `user`, che eredita da `organizationalPerson`, che eredita da `person`, che eredita da `top`.

### Attributi importanti per il pentest

Questi sono gli attributi che cercherai durante l'enumerazione AD:

|Attributo|Cosa contiene|Perché ti interessa|
|---|---|---|
|`sAMAccountName`|Username (legacy)|Identificativo principale dell'utente|
|`userPrincipalName`|username@domain.com|Identificativo Kerberos|
|`memberOf`|Gruppi a cui l'utente appartiene|Trovare Domain Admins, privileged groups|
|`userAccountControl`|Flag bit-encoded|AS-REP roastable, password not required, etc.|
|`servicePrincipalName` (SPN)|Servizi associati all'account|**Kerberoasting target**|
|`pwdLastSet`|Quando è stata cambiata l'ultima password|Account abbandonati|
|`description`|Campo libero|Spesso contiene password in chiaro 🤦|
|`lastLogonTimestamp`|Ultimo login|Account dormienti|
|`nTSecurityDescriptor`|ACL dell'oggetto|Privilege escalation paths (BloodHound)|
|`unicodePwd`|Hash della password|Modificabile con permessi DCSync|

### userAccountControl flags

`userAccountControl` è un campo bit-encoded — un singolo intero che codifica decine di proprietà dell'account. I valori comuni:

|Valore|Flag|Significato|
|---|---|---|
|512|NORMAL_ACCOUNT|Account utente normale|
|514|DISABLED|Account disabilitato (512 + 2)|
|4194304|DONT_REQUIRE_PREAUTH|**AS-REP Roasting target**|
|8192|SERVER_TRUST_ACCOUNT|Domain Controller|
|528|LOCKOUT|Account bloccato|
|66048|DONT_EXPIRE_PASSWORD|Password non scade (512 + 65536)|

Filtrare per `userAccountControl=4194304` ti dà tutti gli account AS-REP roastable.

---

## LDAP e Active Directory

Active Directory **è** essenzialmente un directory service LDAP-compliant con estensioni proprietarie Microsoft. Quando interroghi un DC su porta 389, parli LDAP standard. Le estensioni AD includono:

- Replicazione multi-master tra DC
- Integrazione con Kerberos per l'autenticazione
- Group Policy distribuita
- Schema esteso con classi Microsoft-specific (`user`, `computer`, `group`)

> [!analogy] Linux parallel
> 
> - **OpenLDAP** è l'equivalente Linux pure di Active Directory (solo la parte LDAP, niente Kerberos integrato di default)
> - **FreeIPA** / **Red Hat IDM** è l'equivalente più completo: include LDAP + Kerberos + DNS + autorità di certificazione, esattamente come AD
> - Da Linux puoi joinare un dominio AD con `realmd`/`sssd` e diventare "client AD" — usi LDAP per query, Kerberos per auth

Quindi quando attacchi AD via LDAP, stai usando gli stessi tool e tecniche che useresti contro un server FreeIPA o OpenLDAP enterprise. La sintassi del protocollo è la stessa.

---

## Autenticazione LDAP

LDAP supporta diversi meccanismi di autenticazione (bind):

### 1. Anonymous Bind

Nessuna credenziale. Lo storico problema di sicurezza: molti server LDAP permettono di leggere parte della directory senza autenticarsi.

```bash
ldapsearch -x -H ldap://10.10.10.10 -b "dc=corp,dc=local"
```

In AD moderno, l'anonymous bind è **disabilitato di default** da Windows Server 2003 in poi. Su Windows Server 2003-2012 senza hardening puoi ancora trovarlo. Su sistemi vecchi o configurati male restituisce naming context e altre info preliminari.

### 2. Simple Bind

Username + password **in chiaro** sul filo:

```bash
ldapsearch -x -H ldap://10.10.10.10 -D "cn=alice,ou=Users,dc=corp,dc=local" -w "Lab123!!" -b "dc=corp,dc=local"
```

> [!warning] Mai senza TLS Simple bind senza StartTLS (porta 389) trasmette la password in chiaro. Su un network sniffabile è equivalente a non avere password. Sempre usare LDAPS (636) o LDAP+StartTLS in produzione.

### 3. SASL (GSSAPI / Kerberos)

Autenticazione tramite Kerberos ticket invece di password:

```bash
kinit alice@CORP.LOCAL
ldapsearch -Y GSSAPI -H ldap://dc01.corp.local -b "dc=corp,dc=local"
```

È il metodo nativo in AD. Dopo `kinit`, il ticket viene usato automaticamente per le query LDAP.

---

## Query LDAP: filtri e sintassi

Le query LDAP usano una **sintassi a parentesi** in notazione prefissa:

```
(attribute=value)                   semplice equality
(&(filter1)(filter2))               AND logico
(|(filter1)(filter2))               OR logico
(!(filter1))                        NOT logico
(attribute=*)                       presence (attributo esiste)
(attribute=val*)                    wildcard (LIKE)
(attribute>=val)                    greater than or equal
```

### Esempi pratici per pentest

**Tutti gli utenti del dominio:**

```
(&(objectCategory=person)(objectClass=user))
```

**Utenti AS-REP roastable:**

```
(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))
```

L'OID `1.2.840.113556.1.4.803` è il "bitwise AND" matching rule — necessario per filtrare su userAccountControl che è bit-encoded.

**Account con SPN (Kerberoasting target):**

```
(&(objectCategory=person)(servicePrincipalName=*))
```

**Domain Admins:**

```
(memberOf=cn=Domain Admins,cn=Users,dc=corp,dc=local)
```

**Account con password non-required:**

```
(userAccountControl:1.2.840.113556.1.4.803:=32)
```

**Computer del dominio:**

```
(objectCategory=computer)
```

**Account amministrativi (Admin Count = 1):**

```
(adminCount=1)
```

L'attributo `adminCount=1` viene impostato automaticamente da AD su tutti gli account che appartengono a gruppi privilegiati (Domain Admins, Enterprise Admins, etc.). Cercare `adminCount=1` è un modo veloce per trovare account ad alto valore.

---

## Enumerazione LDAP per pentest

### ldapsearch (Linux)

```bash
# Anonymous query (vedi se ti lascia leggere il naming context)
ldapsearch -x -H ldap://10.10.10.10 -s base namingContexts

# Con credenziali
ldapsearch -x -H ldap://10.10.10.10 \
    -D "alice@corp.local" -w "Lab123!!" \
    -b "dc=corp,dc=local" \
    "(objectClass=user)" sAMAccountName memberOf
```

### netexec / nxc

```bash
# Enumerazione utenti via LDAP
nxc ldap 10.10.10.10 -u alice -p 'Lab123!!' --users

# Tutti gli admin
nxc ldap 10.10.10.10 -u alice -p 'Lab123!!' --admin-count

# AS-REP roastable
nxc ldap 10.10.10.10 -u alice -p 'Lab123!!' --asreproast asrep.txt

# Kerberoastable
nxc ldap 10.10.10.10 -u alice -p 'Lab123!!' --kerberoasting krb.txt
```

### impacket

```bash
# Get users con SPN per Kerberoasting
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request

# AS-REP Roasting
impacket-GetNPUsers corp.local/ -dc-ip 10.10.10.10 -usersfile users.txt -no-pass
```

### BloodHound / SharpHound

Il tool definitivo per analisi AD via LDAP. Funziona così:

1. **Collector** (SharpHound su Windows, bloodhound-python su Linux) interroga LDAP per estrarre ogni informazione possibile: utenti, gruppi, computer, ACL, group memberships, sessions, GPO, trust
2. I dati vengono importati in **Neo4j** (database a grafo)
3. **BloodHound GUI** mostra il dominio come un grafo navigabile e calcola percorsi di privilege escalation

```bash
# Raccolta dati (Linux)
bloodhound-python -u alice -p 'Lab123!!' -d corp.local -dc dc01.corp.local -c all

# Importa i file .json nella GUI di BloodHound
```

Tipiche query BloodHound:

- "Shortest path to Domain Admins from user X"
- "Find all Kerberoastable users"
- "Find shortest path from owned principals"
- "Find computers where X has admin rights"

### ADExplorer (Sysinternals)

Se hai accesso GUI a una macchina Windows del dominio, **ADExplorer.exe** di Sysinternals ti permette di navigare AD visualmente come un file explorer. Utile per esplorare la struttura quando vuoi capire il dominio senza scrivere query LDAP a mano.

Puoi anche fare **snapshot** dell'intero AD per analisi offline:

```cmd
ADExplorer.exe -snapshot "" snapshot.dat /accepteula
```

Poi apri lo snapshot offline su un'altra macchina (anche non joinata al dominio) e fai tutta l'enumerazione che vuoi senza generare traffico LDAP.

---

## Attacchi che dipendono da LDAP

LDAP è il **canale di enumerazione** che precede praticamente ogni altro attacco AD. Senza LDAP non sai contro cosa attaccare.

### Kerberoasting

1. **LDAP query**: trova tutti gli account con `servicePrincipalName=*`
2. Richiedi un TGS per ogni SPN trovato
3. Cracka il TGS offline con hashcat (-m 13100)

### AS-REP Roasting

1. **LDAP query**: trova tutti gli account con flag DONT_REQUIRE_PREAUTH
2. Richiedi un AS-REP senza pre-authentication
3. Cracka offline (-m 18200)

### BloodHound attack path

1. **LDAP enumeration completa**
2. Analisi del grafo: trova percorsi user → DA basati su gruppo, ACL, session, delegation
3. Esegui gli step del percorso

### ACL abuse

1. **LDAP query**: leggi il `nTSecurityDescriptor` degli oggetti
2. Trova ACE che ti permettono di scrivere su oggetti privilegiati (es. `GenericWrite` su Domain Admins → puoi aggiungerti)
3. Esegui la modifica via LDAP write

### GPP cPassword (storico)

1. LDAP query per `gpPath` dei GPO
2. Leggi `Groups.xml` da SYSVOL
3. Decifra il `cPassword` con una chiave AES nota pubblicamente

---

## Difese principali

### LDAP Signing

Forza la firma digitale delle query LDAP — previene **NTLM relay** verso LDAP. Configurabile via GPO:

```
Domain controller: LDAP server signing requirements = Require signing
```

### LDAP Channel Binding

Lega la sessione LDAP al canale TLS sottostante — previene relay verso LDAPS. Da Windows Server 2019 raccomandato come "Always".

### Anonymous bind disabilitato

Default su tutti i Windows Server moderni. Verifica:

```powershell
Get-ADRootDSE | Select dsHeuristics
```

Il 7° carattere di dsHeuristics controlla anonymous bind (`0`=disabled, `2`=enabled).

### LAPS (Local Administrator Password Solution)

Gestisce password admin locali random per ogni macchina, salvate in attributo LDAP `ms-Mcs-AdmPwd`. Leggibile solo da admin autorizzati — abuso comune: scoprire chi può leggere LAPS via ACL.

### Audit / detection

Loggare le query LDAP "anormali" — soprattutto query massive che enumerano tutti gli utenti contemporaneamente (signature classica di BloodHound). Microsoft Defender for Identity (MDI) lo fa di default.

---

## Tabella di sopravvivenza per il pentest

|Cosa vuoi fare|Tool|Comando essenziale|
|---|---|---|
|Verifica anonymous bind|`ldapsearch`|`ldapsearch -x -H ldap://target`|
|Enum utenti|`nxc`|`nxc ldap target -u U -p P --users`|
|Trova SPN (Kerberoast)|`impacket`|`impacket-GetUserSPNs ...`|
|Trova AS-REP|`impacket`|`impacket-GetNPUsers ...`|
|Mappa completa AD|`bloodhound-python`|`-c all`|
|Esplorazione visuale|ADExplorer|snapshot + apri offline|
|Query LDAP arbitraria|`ldapsearch`|filter syntax `(&(...)(...))`|

---

## Takeaways

1. **LDAP è il "Google" di un dominio AD.** Prima di qualsiasi attacco, fai enumerazione LDAP — è da lì che capisci la topologia, trovi target Kerberoastable, identifichi privilege escalation path.
    
2. **AD è LDAP + Kerberos + DNS + replicazione.** La componente LDAP gestisce il modello dati, Kerberos l'autenticazione, DNS la risoluzione, e la replicazione tra DC mantiene tutto sincronizzato.
    
3. **Le query LDAP usano sintassi a parentesi**, ma 9 volte su 10 i tool moderni (nxc, BloodHound, impacket) le scrivono per te. Devi solo sapere quali attributi cercare.
    
4. **`userAccountControl` è bit-encoded** — un singolo intero codifica decine di proprietà dell'account. Il filter `1.2.840.113556.1.4.803` è la sintassi per matching bit-wise.
    
5. **BloodHound è lo standard moderno.** Qualunque cosa tu voglia trovare in AD, BloodHound l'ha già fatto. Imparalo presto perché lo userai in tutti i pentest AD.
    
6. **Senza LDAP signing/channel binding, AD è vulnerabile a NTLM relay verso LDAPS** — un classico path per attacchi senza credenziali iniziali (es. con `ntlmrelayx`).
    

---

## Wiki-links

- [[lab_active_directory_fedora]] — il lab dove userai LDAP enumeration in pratica
- [[windows_domain_logon]] — autenticazione AD, complementare a LDAP per query
- [[credential_dumping_lsa_vs_lsass]] — dove finiscono le credenziali ottenute da query LDAP
- [[lab_session_3_lsass_dump_windows11_defenses]] — sessione lab dove l'enumerazione LDAP è il primo step