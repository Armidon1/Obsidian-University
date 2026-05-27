## tags: [ethical-hacking, he7, ch5, post-exploitation, rootkit, anti-forensics]

# Log cleaning

> Componente di [[rootkits]] — HE7 Ch.5, sezione "Log Cleaning". Più la parte moderna: il libro qui descrive il mondo `syslogd` + log locali, oggi superato.

## Concetto

Il log cleaning è **anti-forensics**: l'attaccante rimuove il proprio percorso dai registri di sistema, soprattutto per non lasciare prove a un'eventuale indagine. È un componente standard di ogni rootkit serio.

Differenza dagli altri componenti di [[rootkits]]: `[[trojan_binaries]]` e `[[kernel_rootkits]]` nascondono la **presenza attuale** dell'attaccante; il log cleaning cancella la **storia** — ciò che è già successo ed è stato registrato. È l'unico componente che lavora sul passato.

## Dove stanno i log — la ricognizione

Prima di pulire bisogna sapere _dove_ il sistema scrive. Il primo passo di HE7 è leggere `/etc/syslog.conf` (oggi `rsyslog.conf` o la config di journald): ogni riga è `facility.severity → destinazione`. Da lì l'attaccante mappa le `facility` (`auth`, `authpriv`, `cron`, `daemon`, `kern`, `mail`...) sui file in `/var/log`.

File chiave su cui intervenire: `messages`, `secure`/`auth.log`, `wtmp`, `xferlog`, `cron`, `maillog`.

I file di login sono **binari** — non si editano con un editor di testo, servono tool dedicati:

|File|Contenuto|Letto da|
|---|---|---|
|`utmp` (`/run/utmp`)|utenti **attualmente** loggati|`who`, `w`|
|`wtmp` (`/var/log/wtmp`)|**storico** login/logout|`last`|
|`btmp` (`/var/log/btmp`)|tentativi di login **falliti**|`lastb`|
|`lastlog` (`/var/log/lastlog`)|ultimo login **per utente**|`lastlog`|

(HE7 dice "`wtmp` usato da `who`": impreciso — `who` legge `utmp`, `last` legge `wtmp`. Nell'esempio del libro `who` legge `wtmp` solo perché gli viene passato esplicitamente il file.)

## Round 1 — pulizia reattiva (cancellare _dopo_)

- **logclean-ng** (su libreria _Liblogclean_) — wiper versatile: supporta `wtmp`/`utmp`/`lastlog`/`syslog`/samba/snort/accounting, rimozione selettiva, modifica dei timestamp.
- **wzap** — specifico per `wtmp`, elimina un singolo utente.
- Esempio HE7: `./logcleaner-ng -w /var/log/wtmp -u w00t -r root` → toglie l'utente `w00t` dallo storico.
- **Cronologia della shell** — `.bash_history`. Tre mosse:
    - editare il file e poi `touch` per riallineare l'atime;
    - disabilitare la history: `unset HISTFILE; unset SAVEHIST`;
    - collegare la history al vuoto: `ln -s /dev/null ~/.bash_history`.

## La difesa che rompe il Round 1

HE7 è esplicito: la pulizia reattiva funziona **solo** se valgono due condizioni — (1) i log stanno sul server locale **e** (2) non sono monitorati/allertati in tempo reale. L'azienda moderna rompe entrambe spedendo i log a un **syslog server remoto**. Non puoi cancellare ciò che è già altrove.

## Round 2 — pulizia proattiva (intercettare _prima_ della scrittura)

Se non puoi cancellare dopo, impedisci la scrittura. Tool HE7: **badattachK** (Matias Sedalo).

Meccanismo — la syscall **`ptrace()`**: permette a un processo di controllare l'esecuzione di un altro (è la stessa API che usa `gdb`). Il cleaner si **attacca al PID di `syslogd`**, intercetta le sue `recv()` (le righe di log arrivano a syslogd via socket), e **scarta le righe** che contengono un valore della `strings.list` (IP dell'attaccante, account compromesso) **prima** che vengano scritte.

Risultato: `grep` su `auth.log` → niente. E vale anche con il forwarding syslog attivo, perché la riga viene uccisa a monte. HE7 nota: l'attaccante vero lo fa in silenzio e usa anche un `[[kernel_rootkits]]` per nascondere processo e file del cleaner.

> [!tip] Filo conduttore — la scala del log cleaning Questo è l'arms race più pulito di tutto il Ch.5, una scala a gradini:
> 
> 1. **Attaccante**: cancella le righe a posteriori (logclean-ng, wzap, `.bash_history`).
> 2. **Difesa**: log spediti off-box in tempo reale → _"non cancelli ciò che è già andato"_.
> 3. **Attaccante**: intercetta _prima_ della scrittura (badattachK + `ptrace` su syslogd) → acceca il logger.
> 4. **Difesa**: logging **tamper-evident** (sealing crittografico) + l'agente forwarda all'istante.
> 5. **Attaccante** (2026): uccide/acceca il _collector_ stesso, sgancia auditd, non genera proprio l'evento.
> 6. **Difesa** (2026): il log sink sta in un **dominio di fiducia separato**, irraggiungibile dalle credenziali dell'host; storage immutabile; e un logger che va silente è _di per sé_ un alert.
> 
> Meta-principio: **non puoi impedire a un attaccante root di toccare lo stato locale — puoi solo rendere lo stato locale irrilevante (off-box, real-time, fiducia separata) e rendere la manomissione rumorosa (tamper-evident).** È lo stesso principio già visto in [[rootkits]] ("fidati di telemetria fuori banda").

## Countermeasures

HE7 dà due contromisure:

- **Flag append-only** — filesystem con extended attributes: `chattr +a` su un file di log permette solo append, non modifica. _Non è una panacea_: un attaccante root fa `chattr -a` e lo toglie. Mitiga, non risolve.
- **Secure remote log host** — la contromisura vera. Se la macchina è compromessa **non puoi fidarti dei log che stanno su di essa**.

## Stato moderno (2026)

- **`syslog` → `systemd-journald`.** Linux moderno ha rimpiazzato `syslogd` col journal: binario, indicizzato. Ha la **Forward Secure Sealing (FSS)** — il journal viene sigillato crittograficamente a intervalli, con una chiave di verifica tenuta **fuori dall'host**; `journalctl --verify` rivela manomissioni. Nota la natura: FSS dà tamper-**evidence**, non tamper-**prevention** — puoi ancora cancellare tutto, ma non _alterare di nascosto_.
- **`auditd` / audit framework del kernel.** È oggi il log autorevole per gli eventi di sicurezza: gli eventi arrivano dal **kernel** via netlink, quindi è più difficile da falsificare di un file di testo. L'attaccante non lo edita: lo **disabilita** (`auditctl -e 0`), ne cancella le regole, ne uccide il processo, o usa un `[[kernel_rootkits]]` per filtrare i record audit. → ATT&CK **T1562.012**.
- **SIEM e forwarding in tempo reale.** Splunk, Elastic, Sentinel, Wazuh: la riga di log viene replicata off-box _nell'istante_ in cui nasce. Anche "intercettare prima della scrittura locale" non basta se l'agente la sta già spedendo.
- **La mossa moderna dell'attaccante** non è più cancellare i file: è **accecare il collector** — uccidere/sganciare l'agente EDR o syslog, manomettere le regole auditd, evasione via eBPF — oppure **non generare l'evento** (niente shell interattive, usare impianti). È la famiglia ATT&CK **T1562 Impair Defenses**; badattachK è l'antenato di **T1562.006 Indicator Blocking**.
- **`.bash_history` è teatro.** Un SOC vero non ci fa affidamento: usa la telemetria `execve` di auditd / EDR. Anzi, una `HISTFILE` che punta a `/dev/null` è _essa stessa_ un IOC — la "contromisura" dell'attaccante lo tradisce.
- **`ptrace` è più ristretto.** Il LSM **Yama** (`kernel.yama.ptrace_scope`, default `1` su gran parte delle distro) limita chi può fare `ptrace` di chi; i container spesso droppano `CAP_SYS_PTRACE`. Da root il trucco badattachK funziona ancora, ma in scenari non-root è bloccato, e un attach `ptrace` è a sua volta un evento auditabile.

## Mapping MITRE ATT&CK

|Tecnica|ID|
|---|---|
|Indicator Removal|T1070|
|— Clear Linux or Mac System Logs|T1070.002|
|— Clear Command History|T1070.003|
|— Timestomp|T1070.006|
|Impair Defenses|T1562|
|— Disable or Modify Tools|T1562.001|
|— Indicator Blocking (badattachK)|T1562.006|
|— Disable or Modify Linux Audit System|T1562.012|

## Collegamenti

- Nota-hub: [[rootkits]]
- Nascondere processo/file del cleaner, filtrare l'audit nel kernel: [[kernel_rootkits]]
- Il timestomping compare anche come evasione dei trojan: [[trojan_binaries]]
- Stesso meta-principio "non fidarti dell'host, fidati del fuori banda": [[rootkits]]