## tags: [ethical-hacking, he7, ch6, apt, threat-intel] aliases: [apt_lifecycle, advanced_persistent_threat]

# APT — Advanced Persistent Threat

> HE7 Ch.6, sezione "What Is an APT?". È anche la nota che le note dei rootkit referenziano come `[[apt_lifecycle]]` (alias impostato nel frontmatter). Capitolo concettuale e — lo dice HE7 stesso — il più datato del libro: la parte moderna è sostanziosa.

## Definizione

Termine coniato da analisti dell'**US Air Force nel 2006** — serviva per discutere certe intrusioni (di matrice cinese) nei contesti non classificati senza nominare lo Stato. Le tre parole descrivono profilo, intento e struttura dell'attaccante:

|Parola|Significato|
|---|---|
|**Advanced**|fluente con tecniche di intrusione _e_ di amministrazione; capace di scrivere exploit e tool su misura|
|**Persistent**|ha un obiettivo a lungo termine e lavora per raggiungerlo **senza essere rilevato**|
|**Threat**|è organizzato, finanziato, motivato, e ha opportunità ubiqua|

Cos'è in sostanza: le azioni di un **gruppo organizzato** con accesso non autorizzato che manipola sistemi informativi per rubare informazioni di valore. È **spionaggio** (anche industriale). Nota importante: l'obiettivo è l'_accesso_, non il sabotaggio — l'APT rimuove gli ostacoli all'accesso, non distrugge. (Caveat di HE7: può pulire i log, e in casi drastici distruggere un sistema — ma non è la norma.)

## Cosa distingue un APT — il punto chiave

Il tratto definente: gli APT usano **funzioni native e quotidiane dell'OS** e si nascondono _"in plain sight"_. Niente malware vistoso. Non vogliono interrompere le normali operazioni dell'host compromesso — l'interruzione è rilevamento. Le loro tecniche **rispecchiano quelle amministrative della vittima stessa**.

È l'inversione rispetto al malware "commodity": quello è rumoroso e ovvio, l'APT si mimetizza. È esattamente ciò che hai visto in pratica questa sessione — `net.exe` usato per il lateral movement (**Living Off the Land**), l'host pivot per il C2: non sono tool da hacker, sono strumenti da sysadmin usati con intento ostile.

> [!tip] Filo conduttore — tecniche invisibili, artefatti no È la tesi centrale del capitolo, e HE7 la dice esplicita: le _tecniche_ sono low-profile, ma gli _artefatti_ che producono no. Lo spear-phishing è furtivo come tecnica — ma lascia tracce email ovunque. Il corollario per il difensore: poiché l'APT usa gli stessi tool di un admin legittimo, crea **gli stessi artefatti** di un utente autorizzato. Non puoi cercare "il malware". Devi cercare l'**anomalia** in attività che sembra legittima — un account che si comporta in modo statisticamente strano, un orario insolito, un percorso di accesso che un utente vero non farebbe. Detection = anomaly detection su attività legittima all'apparenza.

## Le 6 fasi (lifecycle)

Ogni APT attraversa fasi che lasciano artefatti. **Due avvertenze** prima della tabella: (a) non è una linea, è un **loop** — fasi 3 e 4 si ripetono da ogni nuovo host conquistato; (b) le fasi 1-3 ricalcano la metodologia di pentest dei primi capitoli, ma da punti di vista diversi.

|#|Fase|Cosa succede|
|---|---|---|
|1|**Targeting**|recon **esterna**: raccolta info da fonti pubbliche/private, vuln scanning, social engineering, spear-phishing. ≈ Ch.1 footprinting|
|2|**Access / compromise**|il **breach** vero + prima profilazione dell'host bucato (IP, DNS, share NetBIOS, OS, credenziali)|
|3|**Reconnaissance**|recon **interna**: mappare share, architettura di rete, name service, domain controller; testare cosa raggiungono le credenziali attuali; puntare account AD/admin|
|4|**Lateral movement**|spostarsi su altri host con credenziali valide, usando tool **già presenti** sull'OS (command shell, comandi NetBIOS, RDP/Terminal Services, VNC) — **LOTL**|
|5|**Data collection & exfiltration**|punti di raccolta, esfiltrazione via cut-out proxati, cifratura custom; _drip-fed_ (a gocce) o _fire-hosed_ (tutto e subito) a seconda della capacità di detection della vittima|
|6|**Administration & maintenance**|mantenere l'accesso nel tempo: metodi multipli di rientro, trigger/flag d'allarme, mimetizzarsi nei profili utente standard|

La distinzione **recon esterna (fase 1) vs interna (fase 3)** è il punto che un esame ama chiedere: da fuori vedi la _superficie d'attacco_, da dentro vedi il _raggio d'azione_ — dove puoi andare adesso. La fase 6 è dove vivono i `[[rootkits]]` e i loro componenti.

## Vettori d'accesso

HE7: il vettore n.1 è lo **spear-phishing** (email mirata con allegato malevolo o link a un server che consegna malware su misura). Gli altri: SQL injection di siti target, meta-exploit di web server, exploit di social network, social engineering classico (impersonare utenti col help desk), **USB drop** infette, hardware/software infetto, fino allo spionaggio con dipendenti infiltrati. HE7 lo dice netto: _un APT coinvolge sempre un qualche livello di social engineering_.

## Cut-out e C2

Gli attaccanti usano reti già compromesse come **"cut-out"** per proxare le comunicazioni di command & control e nascondersi dietro. È esattamente il concetto di **host pivot** visto questa sessione, ma applicato all'infrastruttura C2. Punto interessante per la forensics: gli _indirizzi_ dei server cut-out sono comunque indizi sull'identità del gruppo — il pivot offusca, non cancella.

## Artefatti per fase

|Fase|Artefatti tipici|
|---|---|
|Access|log email, log web server e di comunicazione, metadata|
|Recon / lateral movement|abuso di credenziali nei security event log, application history log, artefatti OS (link file, prefetch file, profili utente)|
|Exfiltration|protocolli/indirizzi nei log di firewall, IDS, DLP, web server|

Spesso reperibili nel live file system _se sai dove guardare_; a volte solo via analisi forense.

## Case study (lista HE7)

Aurora, Nitro, ShadyRAT, Lurid, Night Dragon, **Stuxnet**, **DuQu**. Nota: Stuxnet (sabotaggio delle centrifughe nucleari iraniane) e DuQu sono l'**eccezione** alla regola "APT = accesso, non sabotaggio" — Stuxnet era distruzione mirata.

## Stato moderno (2026)

Il campo APT è esploso _dopo_ il 2012, quindi il Ch.6 è concettualmente arretrato:

- **Mandiant APT1 report (feb 2013)** — nominò pubblicamente la PLA Unit 61398: il momento in cui l'attribuzione APT diventa mainstream.
- **Nomenclatura dei gruppi** — oggi hanno nomi: APT28/Fancy Bear (GRU), APT29/Cozy Bear (SVR), Lazarus (Corea del Nord), Equation Group. Ogni vendor ha la sua tassonomia (Mandiant `APTxx`, CrowdStrike `Bear/Panda/Kitten`, Microsoft `Typhoon/Blizzard`).
- **Framework** — le 6 fasi informali di HE7 sono state soppiantate dalla **Cyber Kill Chain** di Lockheed Martin e soprattutto da **MITRE ATT&CK**, che ha sistematizzato ogni tecnica in una matrice. Sapere che le 6 fasi di HE7 mappano su questi è il collegamento da fare all'esame.
- **La linea cybercrime↔APT si è confusa** — le gang ransomware (LockBit & co.) operano con sofisticazione da APT; ransomware-as-a-service, access broker, "big game hunting". Il titolo del capitolo "Cybercrime _and_ APT" nel 2026 è quasi una cosa sola a livello di TTP.
- **Era supply-chain** — SolarWinds (2020) ha reso la compromissione del fornitore un vettore d'accesso APT di primo piano → vedi [[trojan_binaries]].
- **Vettori moderni** oltre allo spear-phishing: exploit di edge device (VPN appliance, firewall), abuso di account validi.
- **Detection** — il "trovare l'anomalia in attività legittima" di HE7 era concettualmente giusto; oggi lo fanno EDR/XDR e **UEBA** (User and Entity Behavior Analytics). Il libro aveva ragione, gli strumenti l'hanno raggiunto.

## Mapping MITRE ATT&CK

ATT&CK è di fatto la formalizzazione delle "fasi APT". Le colonne (tactics) corrispondono alle fasi:

| Fase HE7                       | Tactics ATT&CK                                |
| ------------------------------ | --------------------------------------------- |
| 1 Targeting                    | Reconnaissance, Resource Development          |
| 2 Access/compromise            | Initial Access, Execution                     |
| 3 Reconnaissance               | Discovery, Credential Access                  |
| 4 Lateral movement             | Lateral Movement, Privilege Escalation        |
| 5 Collection & exfiltration    | Collection, Exfiltration, Command and Control |
| 6 Administration & maintenance | Persistence, Defense Evasion                  |
|                                |                                               |

## WHAT APTS ARE NOT

As important to understanding what APTs are is understanding what APTs are not. The
techniques previously described are actually common to both APTs and other attackers
whose objectives, often “hacks of opportunity,” are for business interruption, sabotage,
or even criminal activities.
An APT is neither a single piece of malware, a collection of malware, nor a single
activity. It represent coordinated and extended campaigns intended to achieve an objective that satisfies a purpose—whether competitive, financial, reputational, or otherwise.

## Collegamenti

- Fase 6 (maintain access) in dettaglio: [[rootkits]] e i suoi componenti
- Disattivare il logging in fase 3 = anti-forensics: [[log_cleaning]]
- Vettore supply-chain moderno: [[trojan_binaries]]
- Le fasi 1-3 ricalcano i Ch.1-3 (Footprinting, Scanning, Enumeration)