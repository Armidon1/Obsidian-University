## tags: [ethical-hacking, he7, ch6, apt, case-study, forensics, linux] aliases: [lost_linux_host]

# Linux APT Attack — case study

> HE7 Ch.6, secondo case study. Specchio del difensore di `[[apt]]`, versione **Linux**. È utilissimo perché **ricuce mezzo Ch.5** (SUID, file nascosti, `/etc/passwd`, sudo) dentro lo scenario APT. Contrasto con `[[gh0st_attack]]`: lì Windows + RAT + phishing, qui Linux + credenziali deboli + tool piccoli e custom.

## Lo scenario

Host Linux con Tomcat, credenziali deboli. Catena dell'attacco:

1. Tomcat con credenziali `tomcat/s3cret` — **copiate pari pari dall'esempio nella documentazione**.
2. Metasploit → shell sulla macchina via Tomcat (deploy di un'app malevola via HTTP `PUT`).
3. Trovato `shadow.bak` (un backup di `/etc/shadow` lasciato accessibile) → hash crackati offline.
4. `cat /etc/passwd` (world-readable) → scoperti l'account di servizio `nagios` e l'admin `jack`.
5. `jack` ha la password ricavabile dal **campo GECOS** (gecos: "Jack Black" → password: `jackblack`).
6. `sudo su -` → root, perché il server ha la configurazione sudo di default non hardenata.
7. Da root: backdoor PHP, **SUID root shell** per rientrare, evidenze di scanning in un **RAM drive** (volatile), e **host pivot** per lasciare pochissimo sulla macchina.

> [!tip] Filo conduttore — la catena di errori banali Nota una cosa: in tutto l'attacco **non c'è un solo exploit, non c'è uno 0-day**. C'è solo una pila di configurazioni pigre: Tomcat con creds di default → `shadow.bak` lasciato leggibile → `/etc/passwd` world-readable che svela gli username → account `nagios` con password `nagios` → SSH aperto su Internet → password di Jack derivabile dal GECOS → sudo di default. La lezione (collega a `[[apt]]`): "Advanced" in APT non vuol dire necessariamente _exploit sofisticati_ — vuol dire **persistenza e organizzazione**. Quando il bersaglio è così molle, non ti serve essere sofisticato per entrare; la sofisticazione la metti nel _restarci_.

## L'attacco mappato su `[[apt]]`

|Fase APT|Cosa ha fatto l'attaccante|
|---|---|
|1 Targeting|scansione/scoperta del servizio Tomcat esposto via NAT|
|2 Access|credenziali Tomcat di default → deploy via `PUT` → shell con Metasploit|
|3 Recon|`cat /etc/passwd`, crack di `shadow.bak`, ping sweep interno con tool custom, `ppscan`|
|4 Lateral movement|host pivot via Metasploit verso altri target interni|
|5 Collection|(in corso — stava cercando altri target e dati)|
|6 Admin & maintenance|SUID root shell, backdoor PHP, account `nagios`/`jack` → vie di rientro multiple|

## L'indagine — "Lost Linux Host"

**Setup.** Web server sorgente di traffico strano, nessun segno ovvio di compromissione. Il cliente **non ha spento il server** (cruciale — vedi sotto) ma ha bloccato tutto al firewall. Il server sta sulla rete interna con un NAT statico nel firewall perimetrale. Niente intenzione di azione legale → chain of custody meno critica, ma ci si prepara comunque.

**Approccio — baseline.** Unico admin (Jack) → si parte dalla sua shell history per stabilire cosa sia "comportamento normale", così da riconoscere ciò che è fuori carattere.

**IOC dalla history di Jack:**

- `test-cgi.php` — Jack non ricorda di averlo creato.
- `system.sh` — filename che non riconosce.
- L'uso di `sudo su -` segnala una config sudo di default non hardenata.

**Log di Tomcat** (`localhost_access*`) → entry `PUT` da **un IP su Internet** che deploya un'app con un nome poco user-friendly → qualcuno ha accesso amministrativo a Tomcat. Jack conferma: `tomcat/s3cret` preso dall'esempio nei docs. Finestra di compromissione: **31 dic, 18:25–21:32**.

**Verifica live** — `netstat -anlp`, `lsof -i` → niente di anomalo.

> [!note] Caveat del libro HE7 lo dice esplicito: se il sistema ha un rootkit, l'output dei comandi installati **non è affidabile**; e se è un rootkit con syscall hooking, nemmeno binari clean e noti aiutano → `[[kernel_rootkits]]`. È l'argomento per osservare _dall'esterno/sotto_ l'OS.

**La caccia ai file nascosti.** Posti tipici dove un attaccante nasconde file (lista HE7):

- RAM drive (volatili — spariscono allo spegnimento)
- slack space del disco
- il filesystem `/dev`
- file/dir "difficili da vedere" — in Linux puoi creare una directory chiamata `".. "` (**dot-dot-spazio**)
- `/tmp` e `/var/tmp` — world-writable e posti dove l'admin non guarda spesso

La history aveva entry su `/var/tmp` → si parte da lì. `ls -la` mostra **due** directory `..`; con `-b` (escape dei caratteri speciali) si vede che una è `".. "` (dot-dot-spazio) → nascondiglio.

Dentro: un file chiamato `"..."` con **SUID set e owner root**, e lo script `system.sh`. `system.sh` crea un RAM drive e lo monta in una dir dal nome innocuo in `/var/tmp` (`df` conferma il mount).

`strings` sul file `"..."` → `execve` e `/bin/sh`: un **SUID root shell classico** — l'attaccante lo nasconde per riprendersi root se perde l'accesso. Questo _è_ l'argomento della nota `[[suid_binaries]]`: un binario SUID-root che fa solo `execve("/bin/sh")` ti dà una shell con privilegi di root. È persistenza pura.

`find -type f -maxdepth 2 -daystart -ls` → trova i file nascosti nel RAM drive (per fortuna Jack non ha spento il server — **ordine di volatilità**: quelle evidenze sarebbero sparite).

In `/var/tmp/syslog`: evidenze di **recon interna** — uno script che fa ping sweep per host vivi (l'attaccante usa tool propri, niente Nmap sulla box), una lista di target generata, e `ppscan`, un piccolo port scanner standalone (di cui `strings` rivela versione e autore).

**Come hanno preso root?** `last` → l'account `nagios` ha fatto login — un service account che non dovrebbe **mai** loggarsi, men che meno da Internet. SSH è aperto per l'amministrazione remota. Password di `nagios`: `nagios`. Shell valida: `/bin/bash`. Come sapevano di `nagios`? `cat /etc/passwd`, world-readable. Da lì: shell come nagios → password di Jack indovinata dal GECOS → `sudo su -` → game over.

**`test-cgi.php`** — non è un file PHP innocuo: è una **web shell di backdoor**, coerente con l'output del toolkit **Webacoo**. Nome scelto per sembrare un file CGI di test legittimo → masquerading.

## Tabella IOC — artefatto → azione → fase

|Artefatto trovato|Cosa rivela|Fase APT|
|---|---|---|
|`PUT` da IP Internet nei log Tomcat|accesso admin a Tomcat, deploy app malevola|2|
|`shadow.bak` accessibile|furto hash → crack offline|2 / 3|
|Login di `nagios` da Internet (`last`)|abuso di service account debole|2|
|`sudo su -` nella history di Jack|escalation via password GECOS + sudo default|2|
|Dir `".. "` in `/var/tmp` + file `"..."` SUID-root|SUID root shell = persistenza|6|
|`system.sh`, RAM drive montato (`df`)|storage volatile per nascondere tool|6|
|`/var/tmp/syslog`, ping sweep, `ppscan`|recon della rete interna|3|
|`test-cgi.php` (Webacoo)|backdoor PHP, via di rientro|6|

## Tecniche Linux-specifiche — consolidamento Ch.5

Questo case study tocca quasi tutto il Ch.5:

- **File nascosti**: dot-dot-spazio, `/var/tmp`, `/dev`, slack space, RAM drive.
- **SUID root shell** come persistenza → `[[suid_binaries]]` (ancora da scrivere — questo è il motivatore perfetto).
- **`/etc/passwd` world-readable** → username disclosure; **campo GECOS** (5° campo, storicamente nome/ufficio) → mai derivarci password, è pubblico.
- **`shadow.bak`** → un backup di `/etc/shadow` vanifica tutto il punto dello shadowing.
- **Service account deboli** (`nagios/nagios`) — superficie spesso dimenticata.

## Stato moderno (2026)

- **Tomcat con credenziali deboli** è ancora oggi uno dei finding più comuni nei pentest; le **web shell PHP** (Webacoo, China Chopper, p0wny-shell) sono ancora ovunque.
- La **catena di errori banali** è senza tempo — l'equivalente cloud 2026 è: chiave AWS hardcoded in un repo, IAM permissivo di default, bucket S3 pubblico, security group `0.0.0.0/0`. Cambia il vocabolario, non il pattern.
- **Host pivot + Meterpreter in-memory** — il case study finisce esattamente qui: una macchina compromessa diventa pivot, e Meterpreter gira in RAM senza scrivere su disco. È il C2 moderno (Sliver, Havoc fanno lo stesso) → vedi la discussione su host pivot.
- I trucchi di occultamento (`/var/tmp`, `/dev`, dot-dot-spazio) sopravvivono, ma oggi un difensore serio ha **auditd** e **AIDE** che monitorano quelle directory; la detection moderna su Linux usa EDR/eBPF (Falco, Tetragon).
- Il **caveat del rootkit** del libro è più valido che mai: è la ragione per cui l'IR moderno cattura memoria + immagine disco e analizza _offline_, e si fida della telemetria EDR raccolta _prima_ della compromissione.

## Mapping MITRE ATT&CK

|Tecnica|ID|
|---|---|
|Exploit Public-Facing Application (Tomcat)|T1190|
|Valid Accounts (`nagios`, `jack`)|T1078|
|Brute Force: Password Guessing|T1110.001|
|OS Credential Dumping: `/etc/passwd` & `/etc/shadow`|T1003.008|
|Abuse Elevation Control: Setuid/Setgid|T1548.001|
|Server Software Component: Web Shell (Webacoo)|T1505.003|
|Hide Artifacts: Hidden Files and Directories|T1564.001|
|Proxy / pivot|T1090|

## Collegamenti

- Lifecycle di riferimento: `[[apt]]`
- Contrasto Windows/RAT/phishing vs Linux/LOTL: `[[gh0st_attack]]`
- Il SUID root shell è l'argomento di: `[[suid_binaries]]`
- Caveat "non fidarti dei binari" se c'è un rootkit: `[[rootkits]]`, `[[kernel_rootkits]]`
- Backdoor che si maschera da file legittimo (`test-cgi.php`): masquerading, come in `[[trojan_binaries]]`