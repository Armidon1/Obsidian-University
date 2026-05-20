# Architettura di un Windows Server aziendale

## Per chi è questa nota

Questa nota serve a chi:

- Ha esperienza Linux ma zero esperienza con Windows enterprise/server
- Sta studiando attacchi AD ma fa fatica a capire dove si incastrano tutti i protocolli ([[LDAP]], [[Kerberos]], [[SMB]], [[NetBIOS]], [[NTLM]], DNS, [[RPC (Remote Procedure Call)]]...)
- Vuole il **modello mentale unificato** per non dover ricordare tutto come fatti separati

L'obiettivo è darti la **mappa concettuale** che ti permette di posizionare ogni nuovo dettaglio in un contesto, invece di accumulare informazioni isolate.

---

## 1. Il problema che Windows Server risolve

Pensa a un'azienda con 200 dipendenti e 300 computer (workstation, laptop, server). Senza una soluzione enterprise, dovresti:

- Creare 200 account su ogni macchina (200 × 300 = 60.000 account da gestire)
- Aggiornare la password di un utente su tutti i computer dove ha accesso
- Configurare i permessi sui file separatamente su ogni server
- Gestire 300 set di policy di sicurezza diverse

È ingestibile. La soluzione è **centralizzare**:

- Un singolo database di identità (utenti, gruppi, computer)
- Un singolo punto di autenticazione
- Un singolo punto di policy management
- Single Sign-On: l'utente fa login una volta, accede a tutto ciò a cui ha diritto

Questo è quello che fa **Active Directory**.

> [!analogy] Linux parallel Stesso problema, stesse soluzioni. In ambiente Linux usi: LDAP server (per directory), Kerberos (per auth), NFS/Samba (per file), NIS o sssd (per integrazione client). **FreeIPA** mette tutto insieme in un unico prodotto — è l'equivalente più diretto di AD in ecosistema Linux.

---

## 2. Workgroup vs Domain — i due modelli Windows

### Modello Workgroup (peer-to-peer)

Ogni macchina è autonoma:

- Ha il suo database locale di account (**SAM** — Security Account Manager)
- Conosce solo i suoi utenti locali
- Per accedere a una risorsa su un'altra macchina, devi avere un account su quella macchina
- Nessuna gerarchia, nessun controllo centralizzato

Va bene per casa, piccoli uffici (< 10 macchine). Sopra quel numero diventa caotico.

### Modello Domain (client-server gerarchico)

Esiste un **Domain Controller** (DC) — un server che ospita il database centrale di identità (Active Directory). Le macchine "client" (workstation, server membri) si **joinano** al dominio:

- Tutti gli utenti del dominio sono visibili da ogni macchina joinata
- Login con credenziali di dominio (`CORP\alice`) verificate dal DC
- Permessi e policy gestiti centralmente
- Single Sign-On: ottieni un ticket Kerberos al login, lo riusi per tutto

> [!note] Cosa significa "joinare al dominio" tecnicamente Quando joini WS01 al dominio `corp.local`:
> 
> 1. WS01 genera una password random per se stesso (la "machine account password")
> 2. Si crea automaticamente un account computer in AD chiamato `WS01$`
> 3. Da quel momento WS01 può autenticarsi al DC come se fosse un utente, ma per "uso macchina"
> 4. Gli utenti del dominio possono fare login su WS01 perché WS01 sa come chiedere al DC se le loro credenziali sono valide
> 
> L'account `WS01$` esiste in AD ed è la base della relazione di trust tra WS01 e il dominio.

---

## 3. Active Directory Domain Services (AD DS) — il sistema nervoso centrale

**AD DS** è il servizio (software) che gira sui Domain Controller. È il "cervello" che:

- Mantiene il database degli oggetti (`NTDS.dit`)
- Risponde a query sulla directory (via LDAP)
- Emette ticket di autenticazione (via Kerberos)
- Risolve nomi (via DNS)
- Replica le modifiche tra DC del forest
- Applica le Group Policy

Quando installi il ruolo "Active Directory Domain Services" su un Windows Server e lo promuovi a DC, quella macchina diventa un Domain Controller che ospita una copia (master) del database AD.

### Il database AD

Tutto in AD è un **oggetto** con **attributi**. I tipi principali:

|Tipo oggetto|Cosa rappresenta|
|---|---|
|`user`|Un account utente di dominio|
|`computer`|Una macchina joinata al dominio|
|`group`|Un gruppo di utenti/computer/altri gruppi|
|`organizationalUnit` (OU)|Contenitore gerarchico per organizzare oggetti|
|`groupPolicyContainer`|Una Group Policy Object (GPO)|

Organizzati in albero gerarchico (vedi [[LDAP]] per il dettaglio sulla struttura DN).

---

## 4. Lo stack di protocolli — vista d'insieme

Qui sta il modello mentale che risolve la confusione. **Un Domain Controller non parla "un protocollo" — parla decine di protocolli contemporaneamente**, ognuno per uno scopo diverso. Sono servizi distinti che girano sulla stessa macchina.

```
┌──────────────────────────────────────────────────────────────┐
│              DOMAIN CONTROLLER (es. DC01)                    │
│                                                              │
│  ┌─ LIVELLO RISOLUZIONE NOMI ───────────────────────────┐    │
│  │ DNS Server        :53/UDP+TCP                         │    │
│  │ NetBIOS NS        :137/UDP (legacy)                   │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─ LIVELLO AUTENTICAZIONE ─────────────────────────────┐    │
│  │ Kerberos KDC      :88/TCP+UDP                         │    │
│  │ NTLM via NetLogon :135 + dinamica                     │    │
│  │ kpasswd           :464                                │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─ LIVELLO DIRECTORY / QUERY ──────────────────────────┐    │
│  │ LDAP              :389/TCP                            │    │
│  │ LDAPS             :636/TCP                            │    │
│  │ Global Catalog    :3268/TCP (LDAP) :3269 (LDAPS)      │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─ LIVELLO ACCESSO RISORSE ────────────────────────────┐    │
│  │ SMB direct        :445/TCP                            │    │
│  │ SMB over NetBIOS  :139/TCP                            │    │
│  │ RPC endpoint map  :135/TCP                            │    │
│  │ RPC dinamica      :49152-65535/TCP                    │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─ LIVELLO REMOTE MANAGEMENT ──────────────────────────┐    │
│  │ WinRM HTTP        :5985/TCP                           │    │
│  │ WinRM HTTPS       :5986/TCP                           │    │
│  │ RDP               :3389/TCP                           │    │
│  └───────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

### I cinque livelli, spiegati

**Livello risoluzione nomi**: come trovi qualcosa in rete. "Dove sta `dc01.corp.local`?" → DNS risponde con un IP. Prima del 2000 si usava NetBIOS (broadcast), oggi DNS è la base. NetBIOS sopravvive solo per backward compatibility.

**Livello autenticazione**: come dimostri di essere chi dici di essere. Kerberos è il default moderno (ticket-based, scala bene), NTLM è il fallback legacy (challenge-response, meno sicuro, ma onnipresente per compatibilità).

**Livello directory**: come ottieni informazioni sul dominio. "Quali sono i Domain Admin?", "A che gruppi appartiene alice?", "Quali computer ci sono nel dominio?" → tutto LDAP.

**Livello accesso risorse**: come usi davvero le cose. File su una share? SMB. Eseguire un comando remoto? RPC. Modificare il registry remoto? RPC.

**Livello remote management**: come amministri da remoto. RDP per desktop interattivo, WinRM per PowerShell remoto (l'equivalente moderno di SSH).

---

## 5. Tabella di sopravvivenza delle porte

Da memorizzare come pattern di riconoscimento — quando vedi questo profilo di porte aperte, sai cos'è:

|Porta|Servizio|Significato|
|---|---|---|
|53|DNS|Server DNS (su DC quasi sempre)|
|88|Kerberos|KDC presente → è un DC|
|135|RPC endpoint mapper|"Telefono" per scoprire altri servizi RPC|
|137/138/139|NetBIOS|Legacy name resolution + SMB session|
|389|LDAP|Directory query|
|445|SMB|File sharing moderno|
|464|kpasswd|Cambio password Kerberos|
|593|RPC over HTTP|Spesso Exchange|
|636|LDAPS|LDAP cifrato|
|3268/3269|Global Catalog|Multi-domain forest queries|
|3389|RDP|Desktop remoto|
|5985/5986|WinRM|PowerShell remoting|

> [!tip] Pattern riconoscitivo del DC Quando vedi **88 + 389 + 53** tutti aperti, hai un Domain Controller con confidenza altissima. Aggiungi 3268 (Global Catalog) e sei al 100%.

---

## 6. Server vs Desktop e il concetto di Ruoli

### Windows Server vs Windows Desktop

**Windows Server** (Server 2019, 2022, 2025) è una versione di Windows pensata per girare servizi 24/7:

- Stack di sicurezza simile a Windows Desktop ma ottimizzato per server
- Niente Start menu pieno di app consumer
- **Server Manager** GUI per gestire i ruoli
- Versione "Core" senza GUI (solo CLI/PowerShell) per produzione

**Windows Desktop** (Windows 10/11 Pro, Enterprise) è quello che gira sulle workstation. Può joinare un dominio, ma non può **essere** un DC.

### I "Ruoli"

Un Windows Server "vuoto" non fa quasi niente. Lo trasformi in qualcosa di specifico **abilitando ruoli**. Ogni ruolo è un set di servizi modulari:

|Ruolo|Cosa fa|Analogo Linux|
|---|---|---|
|**AD DS**|Domain Controller|FreeIPA / OpenLDAP+Kerberos|
|**DNS Server**|Server DNS|BIND, dnsmasq|
|**DHCP Server**|Assegnazione IP automatica|dnsmasq, isc-dhcp|
|**File Server**|Condivisione file via SMB|Samba|
|**Print Server**|Server di stampa|CUPS|
|**Hyper-V**|Hypervisor|KVM/libvirt|
|**IIS**|Web server|Apache, nginx|
|**AD CS**|Certificate Authority|step-ca, OpenSSL CA|
|**NPS**|RADIUS server|FreeRADIUS|
|**WSUS**|Server di aggiornamenti Windows|apt-mirror, repo locale|

**Un singolo server può ospitare più ruoli contemporaneamente.** Il tuo DC01 del lab ha AD DS + DNS — due ruoli sulla stessa macchina. In produzione spesso un DC fa anche da DNS e da Global Catalog. Aziende più grandi separano i ruoli su macchine diverse per resilienza.

---

## 7. Cosa succede quando alice fa login — case study completo

Questo è il momento "aha". Seguiamo passo passo cosa succede quando alice digita username/password su WS01.

```
PASSO 0: alice digita "CORP\alice" + "Password123" sulla lock screen
         
PASSO 1: Winlogon (servizio Windows) riceve le credenziali
         → le passa a LSASS (Local Security Authority Subsystem)
         
PASSO 2: LSASS riconosce che è un dominio account (CORP\)
         → invoca il provider Kerberos
         
PASSO 3: WS01 deve trovare il DC. Chiede al DNS:
         "Quale macchina serve _kerberos._tcp.corp.local?"
         → DNS risponde: dc01.corp.local
         → WS01 risolve dc01.corp.local in IP (10.10.10.10)
         
PASSO 4: WS01 manda AS-REQ a DC01:88 (Kerberos):
         "Voglio un TGT per alice@CORP.LOCAL"
         → il pacchetto è cifrato con la password di alice
            (preauth: dimostra che conosci la password senza inviarla)
         
PASSO 5: DC01 verifica la preauth:
         → cerca alice in AD (internamente via LDAP)
         → recupera l'hash della sua password da NTDS.dit
         → tenta di decifrare la preauth con quell'hash
         → se OK → genera un TGT (Ticket Granting Ticket)
         → rimanda AS-REP al WS01
         
PASSO 6: WS01 conserva il TGT nel suo Kerberos cache
         → alice è "loggata" dal punto di vista di Windows
         → LSASS conserva in memoria anche l'NT hash (per fallback NTLM)
         
PASSO 7: Windows applica le GPO:
         → WS01 chiede al DC via LDAP "che GPO si applicano a CORP\alice?"
         → DC risponde con le GPO applicabili
         → WS01 le scarica dalla share \\corp.local\SYSVOL via SMB
         → le applica (cambia setting di sistema, monta drive, etc.)
         
PASSO 8: alice vede il desktop. Login completato.
```

**Cosa hai imparato leggendo questo:**

- **DNS** è il primo passo (serve a trovare il DC)
- **Kerberos** è il protocollo di autenticazione (porta 88)
- **LDAP** viene usato dal DC internamente per cercare alice e per dire a WS01 quali GPO applicare
- **SMB** trasferisce le GPO dalla SYSVOL share
- **LSASS** conserva le credenziali in memoria (è il motivo per cui si fa "dump LSASS")
- **NTDS.dit** è il database degli hash sul DC (è il motivo per cui si fa DCSync)

Hai appena visto **come si incastrano tutti i protocolli che hai studiato** in un singolo login.

---

## 8. Cosa succede quando alice apre una share — case study 2

```
alice (loggata su WS01) digita \\fileserver.corp.local\dati in Esplora File

PASSO 1: WS01 risolve fileserver.corp.local via DNS → 10.10.10.30

PASSO 2: WS01 vuole un Service Ticket per CIFS/fileserver.corp.local
         → manda TGS-REQ a DC01:88, allegando il TGT di alice
         → DC01 verifica il TGT, genera il TGS, lo rimanda

PASSO 3: WS01 si connette a fileserver.corp.local:445 (SMB)
         → presenta il TGS
         → fileserver lo valida (senza chiamare il DC perché contiene già 
           tutte le info sui gruppi di alice firmate dal KDC)

PASSO 4: fileserver controlla i permessi della share:
         → "CORP\alice è autorizzata a leggere \\fileserver\dati?"
         → controlla le ACL: sì (membro del gruppo Domain Users)

PASSO 5: fileserver apre la share, mostra i file
         → ogni operazione (read, write, delete) viene autorizzata dalle ACL
```

Cose da osservare:

- alice **non ha rifatto login** — il TGT ottenuto a passo 5 del login originale serve a generare il TGS senza ulteriori password
- fileserver **non chiede al DC se alice è valida** — il TGS contiene tutte le info necessarie firmate dal KDC
- Questo è il **Single Sign-On** in azione

> [!note] L'eleganza di Kerberos Il motivo per cui Kerberos è dominante in enterprise: **scala**. Un fileserver con 1000 client che si connettono al secondo non deve chiamare il DC ogni volta. Valida i ticket in locale grazie alla firma del KDC. Per questo le aziende possono avere migliaia di server che condividono un'identità centralizzata senza congestionare i DC.

---

## 9. Dove vivono i dati — mappa delle credenziali

Quando dumpi credenziali (con [[Mimikatz]], secretsdump, etc.) le prendi da posti specifici. Capire dove vivono ti aiuta a sapere cosa cerchi.

### Sulla workstation (WS01)

| Cosa                                 | Dove vive                                     | Come si ottiene                                            |
| ------------------------------------ | --------------------------------------------- | ---------------------------------------------------------- |
| Account locali (Administrator, ecc.) | Registry SAM hive `HKLM\SAM`                  | secretsdump locale, mimikatz `lsadump::sam`                |
| Hash NTLM utenti loggati             | Memoria del processo `lsass.exe`              | mimikatz `sekurlsa::logonpasswords`, dump LSASS + pypykatz |
| Cached domain credentials (DCC2)     | Registry `HKLM\SECURITY\Cache`                | secretsdump, mimikatz `lsadump::cache`                     |
| Service account passwords            | LSA Secrets in `HKLM\SECURITY\Policy\Secrets` | secretsdump, mimikatz `lsadump::secrets`                   |
| Machine account password (WS01$)     | LSA Secrets                                   | secretsdump                                                |
| Ticket Kerberos                      | Memoria di lsass.exe                          | mimikatz `sekurlsa::tickets`                               |

### Sul Domain Controller (DC01)

| Cosa                       | Dove vive                                       | Come si ottiene                                     |
| -------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| Tutti gli hash del dominio | `C:\Windows\NTDS\NTDS.dit` (database AD)        | DCSync, copia offline del file                      |
| Hash di krbtgt             | NTDS.dit                                        | DCSync (per [[Golden Ticket]])                      |
| Tutti i ticket attivi      | Memoria del KDC                                 | Praticamente non si dumpa, si forgia con krbtgt     |
| GPO files                  | `C:\Windows\SYSVOL\sysvol\corp.local\Policies\` | Share SMB \corp.local\SYSVOL, leggibile da chiunque |

### Sul filesystem (entrambi)

|Cosa|Dove vive|
|---|---|
|Credential Manager|`%APPDATA%\Microsoft\Credentials\` cifrato con DPAPI|
|File con password sparse|OneDrive, Documents, Desktop (ricerca con SeatBelt, snaffler)|
|GPP cPassword (legacy)|`\\domain\SYSVOL\...\Groups.xml` (decifrabile con chiave nota)|

---

## 10. Group Policy in 5 minuti

Le **[[Group Policy Object (GPO)]]** sono il meccanismo con cui l'admin del dominio impone configurazioni a utenti e macchine.

**Workflow:**

1. Admin crea una GPO nel Group Policy Management Console
2. La GPO viene salvata in due posti:
    - **Metadati** in AD (oggetto LDAP `groupPolicyContainer`)
    - **Settings veri** in `\\corp.local\SYSVOL\sysvol\corp.local\Policies\{GUID}\`
3. La GPO viene "linkata" a un'OU, dominio, o sito
4. Ogni computer/utente in quella OU applica la GPO al login (o ogni 90 minuti circa)

**Cosa può fare una GPO:**

- Cambiare quasi qualsiasi setting di Windows (registry, security policy, software install)
- Mappare drive di rete
- Distribuire software via MSI
- Eseguire script di logon/startup
- Definire policy di sicurezza (lockout, password complexity, ecc.)

**Perché conta per il pentest:**

- **SYSVOL è una share leggibile da qualunque utente di dominio** — puoi enumerare TUTTE le GPO senza essere admin
- Storicamente le GPO contenevano password cifrate con chiave nota (**GPP cPassword** vulnerability)
- Modificare una GPO che si applica a Domain Admins = privilege escalation diretta

> [!analogy] Linux parallel Concetto equivalente: **Ansible playbooks distribuiti automaticamente** dove l'orchestrator è il DC, l'inventory è AD, e i target sono tutte le macchine joinate. Un altro parallelo è **Puppet/Chef** in modalità pull. Niente di esatto su Linux standard, ma `sssd` + GPO via Samba è il più vicino.

---

## 11. Forest, Tree, Domain — quando servono più domini

Per ora hai studiato single-domain (`corp.local` nel lab, `egotistical-bank.local` su [[HTB - Sauna]]). In aziende reali la struttura può essere più complessa.

### Domain

Un singolo namespace AD. Es: `corp.local`. Ha uno o più DC che replicano tra loro.

### Tree

Domini con un namespace DNS contiguo. Es:

- `corp.local` (parent)
- `it.corp.local`, `us.corp.local`, `eu.corp.local` (child)

I child domini ereditano alcune cose dal parent (trust automatico).

### Forest

Tutte le tree che condividono lo stesso schema e configurazione AD. Anche tree con namespace diversi (`corp.local` e `acme.com`) possono essere nello stesso forest.

### Trust relationships

Connessioni tra domini diversi che permettono autenticazione cross-domain:

- **Two-way trust**: bidirezionale, default tra domini dello stesso forest
- **External trust**: tra forest diversi
- **Forest trust**: trust completo tra due forest

> [!note] Perché conta nel pentest Quando bucki una macchina in `it.corp.local`, puoi potenzialmente muoverti verso `us.corp.local` se esiste un trust. Tool come [[BloodHound]] mappano questi trust automaticamente. **Enterprise Admins** ha potere su tutto il forest (anche sui domini child), mentre **Domain Admins** ha potere solo sul suo dominio.

---

## 12. La traduzione Linux — parallelismi completi

Tabella di conversione per il tuo background da sysadmin Linux:

|Windows / AD|Linux equivalente|Note|
|---|---|---|
|Active Directory Domain Services|FreeIPA / OpenLDAP + Kerberos + DNS|FreeIPA è il più vicino|
|Domain Controller|FreeIPA server|Macchina che ospita tutto|
|LDAP|OpenLDAP, 389 Directory Server|Identico protocollo|
|Kerberos (AD KDC)|MIT Kerberos, Heimdal|Letteralmente lo stesso protocollo|
|NTLM|Niente di nativo Linux (esiste in Samba)|Solo Windows|
|Domain account|utente UID in directory|sssd integra|
|Local account (SAM)|utente in /etc/passwd|Locale alla macchina|
|Group Policy|Ansible / Puppet (concettualmente)|Niente di nativo equivalente|
|GPO + SYSVOL|File di config + script in share|Idem|
|SMB / CIFS|Samba|Samba implementa SMB|
|SMB share|NFS export, Samba share|NFS è il più Linux-puro|
|NTDS.dit|LDAP database (ldif backend)|Stesso ruolo|
|LSASS|Niente di esatto — gestione cred sparsa tra pam, sssd, krb5cc||
|Registry HKLM\SAM|/etc/shadow|Hash account locali|
|LSA Secrets|/etc/krb5.keytab + altri keytab|Service account credentials|
|Cached creds (DCC2)|sssd cache (`/var/lib/sss/db/cache_*.ldb`)|Login offline|
|RDP|x2go, VNC, NoMachine|Desktop remoto|
|WinRM|SSH|Remote shell|
|WMI|Niente di esatto (D-Bus + interfacce remote ci si avvicina)||
|Service Account|utente di servizio (postgres, www-data)|Concetto identico|
|Domain Admins|gruppo `wheel` o `sudo` per FreeIPA admin|Privilegi totali|
|Enterprise Admins|(in FreeIPA non c'è distinzione forest/domain)||
|Forest|Realm Kerberos federato (raro su Linux)||
|Trust relationship|Cross-realm Kerberos trust||

---

## 13. Perché capire l'architettura è la chiave per il pentest

Ogni attacco AD è una **conseguenza diretta dell'architettura**. Vediamone alcuni:

| Attacco                  | Perché funziona (in termini di architettura)                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **[[Kerberoasting]]**    | Kerberos cifra i TGS con la password del service account → se è debole, lo cracchi offline                                     |
| **AS-REP Roasting**      | Se un account ha DONT_REQUIRE_PREAUTH, il KDC manda l'AS-REP cifrato con la password senza richiedere prove → cracking offline |
| **[[Pass-the-Hash]]**    | NTLM usa l'hash come "password equivalent" → se ce l'hai, ti autentichi                                                        |
| **DCSync**               | I DC si replicano tra loro via RPC → se hai il privilegio di replica, simuli un DC e chiedi gli hash                           |
| **[[Golden Ticket]]**    | I TGT sono firmati con la chiave di krbtgt → se hai quella chiave, forgi TGT validi                                            |
| **NTLM Relay**           | NTLM non lega l'autenticazione al canale di destinazione → puoi forwardare un'auth catturata a un altro server                 |
| **GPP cPassword**        | Microsoft ha distribuito password cifrate con chiave nota in SYSVOL → SYSVOL è leggibile da tutti                              |
| **[[BloodHound]] paths** | Tutti i permessi in AD sono ACL espliciti, leggibili via LDAP → analisi a grafo trova chain di esecuzione                      |

**Ogni nome che memorizzi (Kerberoasting, DCSync, Golden Ticket) è solo l'etichetta di una conseguenza dell'architettura.** Non li memorizzi come fatti isolati — li deduci dalla struttura.

---

## 14. La tabella riassuntiva (one-page reference)

```
┌─────────────────────────────────────────────────────────────┐
│ COMPONENTE         │ FUNZIONE          │ PORTA   │ ATTACCO  │
├─────────────────────────────────────────────────────────────┤
│ DNS                │ name resolution   │ 53      │ DNS hijack│
│ Kerberos KDC       │ ticket auth       │ 88      │ Roasting │
│ RPC endpoint mapper│ service discovery │ 135     │ enum     │
│ NetBIOS Session    │ legacy SMB        │ 139     │ SMB attack│
│ LDAP               │ directory query   │ 389     │ enum, relay│
│ SMB                │ file/RPC          │ 445     │ PtH, relay│
│ kpasswd            │ Kerberos pwd      │ 464     │ pwd reset│
│ LDAPS              │ LDAP+TLS          │ 636     │ relay    │
│ Global Catalog     │ forest-wide LDAP  │ 3268    │ enum     │
│ RDP                │ remote desktop    │ 3389    │ PtH, BF  │
│ WinRM              │ remote shell      │ 5985/6  │ PtH      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DOVE VIVONO LE CREDENZIALI                                  │
├─────────────────────────────────────────────────────────────┤
│ Hash account locali     │ HKLM\SAM (workstation)            │
│ Hash dominio attivi     │ Memoria di lsass.exe (workstation)│
│ Hash dominio (database) │ NTDS.dit (DC)                     │
│ Service account passwds │ LSA Secrets (workstation+DC)      │
│ Cached domain creds     │ HKLM\SECURITY\Cache (workstation) │
│ Ticket Kerberos         │ Memoria lsass.exe                 │
│ GPP passwords (legacy)  │ \\domain\SYSVOL\...\Groups.xml    │
└─────────────────────────────────────────────────────────────┘
```

---

## Takeaways

1. **Active Directory è un servizio (AD DS) che gira su un server (DC) e gestisce un database di oggetti (utenti, computer, gruppi)**. È il punto centrale di identità in un dominio Windows.
    
2. **Il DC parla decine di protocolli contemporaneamente**, ognuno per uno scopo: DNS (risoluzione), Kerberos (auth), LDAP (query), SMB (file), RPC (servizi remoti), WinRM/RDP (management).
    
3. **Ogni protocollo è un'opportunità di attacco diversa**, ma tutti dipendono dall'architettura sottostante. Capisci l'architettura → deduci gli attacchi.
    
4. **Single Sign-On funziona grazie a Kerberos**: ottieni un TGT al login, lo riusi per generare TGS per ogni servizio senza ridigitare la password.
    
5. **Tutti i protocolli che esistono in AD esistono anche su Linux**: LDAP, Kerberos, SMB (Samba), DNS. La differenza è che Microsoft li ha integrati in un singolo prodotto coerente con tooling enterprise-grade. FreeIPA è l'equivalente Linux più vicino.
    
6. **Group Policy è il meccanismo di policy management** — distribuisce config via SYSVOL share. È leggibile da qualunque utente di dominio, quindi è una superficie di enumerazione importante.
    
7. **Le credenziali vivono in posti specifici e diversi tra workstation e DC**. Capire dove cercare = capire cosa dumpare con quale tool.
    

---

## Wiki-links

- [[LDAP]] — il protocollo per interrogare AD nel dettaglio
- [[Impacket]] — il toolkit per sfruttare praticamente tutto quello descritto qui
- [[lab_active_directory_fedora]] — il lab dove vedi tutto questo in piccolo
- [[windows_domain_logon]] — il flow di login Kerberos approfondito
- [[credential_dumping_lsa_vs_lsass]] — dove vivono le credenziali (sezione 9 espansa)
- [[lab_session_3_lsass_dump_windows11_defenses]] — la sessione dove tutto questo viene attaccato in pratica