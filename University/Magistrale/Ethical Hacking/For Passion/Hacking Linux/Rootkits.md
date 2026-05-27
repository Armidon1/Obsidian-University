## tags: [ethical-hacking, he7, ch5, post-exploitation, rootkit]

# Rootkits

> Nota-hub del paragrafo HE7 Ch.5 "Rootkits". Le singole componenti sono approfondite nelle note collegate — qui solo concetto, tassonomia, contromisure di sistema e stato moderno.

## Concetto

Un rootkit **non è un exploit**: è ciò che l'attaccante installa _dopo_ aver ottenuto root. Il sistema compromesso diventa il punto d'accesso centrale per gli attacchi successivi, quindi servono due cose:

1. **Mantenere l'accesso** — rientrare quando vuole, senza ri-exploitare la macchina.
2. **Restare invisibile** — nascondere file, processi, connessioni e log all'amministratore e agli strumenti di sistema.

Il nome è "root" + "kit": il kit di strumenti per _conservare_ root. Vive interamente nella fase di **post-exploitation** → vedi [[apt_lifecycle]] (fasi "maintain access" / "covering tracks").

## Le 4 categorie classiche (UNIX rootkit)

HE7 scompone un rootkit UNIX tipico in quattro gruppi di tool, tutti specifici per piattaforma e versione del kernel:

| Categoria               | Funzione                                                                                                                                                                                 | Nota dedicata    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Trojan programs**     | binari di sistema rimpiazzati (`login`, `ps`, `netstat`, `ifconfig`, `ssh`, `ls`...) che fanno il loro lavoro normale **+** logica nascosta (logging delle password, occultamento di sé) | [[Trojans]]      |
| **Backdoors**           | canali di rientro persistenti: inetd insertion, listener TCP (es. _rathole_ su porta 1337), reverse shell, port knocking, covert channel                                                 | [[Backdoors]]    |
| **Interface sniffers**  | cattura del traffico sul segmento locale — colpisce _ogni_ host che parla con la macchina bucata                                                                                         | [[Sniffer]]      |
| **System log cleaners** | rimozione/alterazione delle tracce nei log (`wtmp`, `utmp`, `auth`, `.bash_history`)                                                                                                     | [[Log Cleaning]] |

> [!note] HE7 elenca "Backdoors" come categoria a sé ma poi la tratta _dentro_ la sezione Trojans (è lì che compare rathole). Decidi tu se fonderle in [[Trojans]] o tenere [[Backdoors]] separata.

Logica della tassonomia: ogni categoria acceca una facoltà diversa del difensore — il _trojan_ mente sui programmi, il _log cleaner_ mente sui registri, lo _sniffer_ estende il bottino, la _backdoor_ garantisce il ritorno.

## Userland → kernel: l'evoluzione

I rootkit "classici" (le 4 categorie sopra) lavorano in **userland**: modificano file su disco. Difetto fatale → un integrity checker che confronta i checksum li smaschera.

La generazione successiva è **kernel-based**: invece di toccare i programmi, modifica il **kernel in esecuzione**, così tutti i programmi vengono ingannati _senza essere alterati_. Il tuo `ps` è il binario genuino — ma il kernel gli mente su quali processi esistono.

Dettagli (injection via LKM / `/dev/kmem` / `/dev/mem`, interception via syscall table / IDT / VFS, caricamento con `modprobe`, knark/adore/enyelkm/SucKIT) → [[Kernel Rootkits]].

> [!tip] Filo conduttore — la corsa verso il basso La storia dei rootkit è una **gara di profondità**: ogni layer di detection spinge l'attaccante un livello più in basso, dove il difensore non guarda ancora. userland (trojan binari) → _i checksum li beccano_ → syscall table → _gli integrity checker la beccano_ → modifica runtime del kernel → _si disabilita LKM_ → `/dev/kmem` → _viene rimosso_ → `/dev/mem` → oggi: **firmware/UEFI** ed **eBPF**. È lo stesso schema visto altrove: quando una difesa si consolida, l'attacco non sparisce, **cambia layer**.

## Countermeasures generali

Le contromisure specifiche stanno nelle note dei singoli componenti. A livello di sistema:

- **File Integrity Monitoring** — checksum crittografici di tutti i binari, con le firme conservate **offline** (un rootkit che controlla la macchina può falsificare un DB locale). Tool: Tripwire, AIDE.
- **Verifica via package manager** — molti pacchetti hanno già hash forti integrati. `rpm -V <pacchetto>` su sistemi RPM-based confronta i file installati col DB (checksum MD5); su Solaris c'è la Fingerprint Database + il comando `digest`. Usare sempre una copia _known-good_ del package manager.
- **Rootkit scanner** — `chkrootkit`, `rkhunter`. Limite importante: funzionano bene solo contro rootkit pubblici "in scatola", non personalizzati → roba da script kiddie, non da attaccante serio.
- **Prevenzione > detection** — la vera contromisura è impedire la modifica dei binari _in primo luogo_ (filesystem con flag append-only / immutable — vedi [[Log Cleaning]]).
- **Dopo la compromissione**: ricostruire dal supporto originale. **Mai** fidarsi dei backup → con ogni probabilità sono infetti anch'essi.

## Rootkit recovery

Quando arriva "quella telefonata" (_i tuoi sistemi stanno attaccando i miei_):

- Ogni azione sulla macchina altera le evidenze — anche solo _aprire_ un file cambia l'atime.
- Serve un **toolkit di binari statically-linked**, verificati crittograficamente, preparato **prima** dell'incidente su supporto esterno read-only (CD/USB): `ls`, `ps`, `netstat`, `login`, `du`, `df`, `lsof`, `w`, `finger`, `grep`, `sh`...
- Lo static linking è obbligatorio: se l'attaccante ha modificato le shared library, un binario dinamico eseguirebbe codice ostile → vedi [[Shared Library Hijacking]].
- Preservare i **3 timestamp** di ogni file:
    - `ls -alRu` → last **access** time
    - `ls -alRc` → last **modification** time
    - `ls -alR` → standard (creation)
- Boot da supporto sicuro (tipo Helix) per l'analisi forense.
- **Se il kernel è compromesso, ogni risultato userland è inaffidabile** — `ps`, `ls`, persino Tripwire diventano inutili → [[Kernel Rootkits]].

## Stato moderno (2026)

HE7 qui mostra l'età: l'elenco di rootkit (knark, adore, enyelkm, SucKIT, phalanx, Mood-NT) è tutto era kernel 2.2/2.4/2.6. Mappa aggiornata:

- **Rootkit userland** — quasi morti come li descrive il libro. FIM (AIDE/Tripwire), verifica dei pacchetti firmati e soprattutto le distro con **verified boot / rootfs immutabile** (dm-verity: Android, ChromeOS, Fedora Silverblue) rendono difficilissimo modificare un binario di sistema senza farsene accorgere.
- **`/dev/kmem` rimosso** dai kernel moderni (~5.13); `/dev/mem` ristretto da `CONFIG_STRICT_DEVMEM`. Le vie di injection di SucKIT/phalanx sono chiuse.
- **LKM rootkit** — ancora possibili ma frenati da **module signing** (`CONFIG_MODULE_SIG_FORCE`), **UEFI Secure Boot** e **kernel lockdown mode**: un modulo non firmato non si carica.
- **La frontiera si è spostata** (la "corsa verso il basso" continua):
    - **eBPF rootkit** — eBPF permette di agganciare il comportamento del kernel _senza_ LKM ed è legittimo by design → difficile da vietare. Casi reali: BPFDoor, Symbiote, ebpfkit.
    - **Bootkit / UEFI rootkit** — sotto il SO, nel firmware: LoJax, MoonBounce, BlackLotus (quest'ultimo bypassa Secure Boot).
    - **Hypervisor rootkit** — il SO viene virtualizzato a sua insaputa (concetto "Blue Pill").
- **Detection moderna** — EDR, memory forensics (Volatility), e il principio chiave: _non fidarti della macchina compromessa, fidati di telemetria fuori banda_. È la versione 2026 del "remote syslog server" che HE7 già consigliava in [[Log Cleaning]].

## Collegamenti

- Componenti: [[Trojans]] · [[Backdoors]] · [[Sniffer]] · [[Log Cleaning]] · [[Kernel Rootkits]]
- Fase di attacco: [[apt_lifecycle]]
- Il recovery dipende da: [[shared_library_hijacking]]
- Chiude il **Ch.5 — Hacking UNIX**

# Altre infromazioni da cybersecr

- Gain full system control after gaining access  
- Hide from detection by modifying kernel or OS processes  
- Often include backdoors for remote control  

---
Un **rootkit** è una tipologia di malware estremamente subdola, progettata non tanto per causare un danno immediato (come farebbe un ransomware), ma per ottenere e mantenere un accesso privilegiato a un sistema, **nascondendo attivamente la propria presenza** e quella di altri software malevoli agli occhi degli amministratori e degli strumenti di sicurezza.

Il nome deriva dall'unione di due concetti fondamentali dell'informatica: **"root"** (l'utente con privilegi massimi nei sistemi Unix-like) e **"kit"** (un insieme di strumenti software).

Per comprendere appieno la loro pericolosità, è utilissimo inquadrarli nell'architettura dei livelli di privilegio di un sistema operativo (i cosiddetti _Protection Rings_).

### L'Arte dell'Invisibilità: Come Funzionano

Il trucco principale di un rootkit è l'**alterazione del flusso di esecuzione standard del sistema operativo**.

Se un antivirus o un task manager chiede al sistema operativo "Dammi la lista dei processi in esecuzione", questa richiesta passa attraverso specifiche API di sistema. Un rootkit si aggancia a queste chiamate (tecnica nota come **API Hooking**) o manipola direttamente le strutture dati in memoria (**DKOM** - _Direct Kernel Object Manipulation_).

Il malware intercetta la richiesta, rimuove i propri processi dalla lista, e restituisce all'antivirus un elenco apparentemente pulito. In sintesi: **se il cuore del sistema operativo è compromesso, non puoi più fidarti di nessuna informazione che ti restituisce.**

### Classificazione per Livello di Privilegio

I rootkit si dividono principalmente in base al livello in cui riescono a infiltrarsi:

1. **User-Mode Rootkit (Ring 3):**
    
    Operano a livello applicativo. Intercettano le chiamate alle API tramite tecniche come la _DLL injection_. Sono i meno complessi e i più facili da rilevare, poiché le moderne soluzioni di sicurezza (EDR) che operano a livello kernel riescono a scavalcarli e smascherarli.
    
2. **Kernel-Mode Rootkit (Ring 0):**
    
    Modificano direttamente il "cuore" del sistema operativo. Poiché operano con gli stessi privilegi (o superiori) dei software di difesa, sono estremamente complessi da individuare. Il loro sviluppo richiede competenze avanzate: un singolo errore nel codice del rootkit causa spesso il crash irreversibile del sistema (il classico _Blue Screen of Death_).
    
3. **Bootkit:**
    
    Infettano il Master Boot Record (MBR), il Volume Boot Record (VBR) o, nei sistemi moderni, il firmware UEFI. Si caricano _prima_ del sistema operativo stesso, garantendosi un controllo totale sull'intera catena di avvio fin dal momento dell'accensione della macchina.
    
4. **Firmware / Hardware Rootkit:**
    
    Rappresentano il livello più profondo. Si annidano nel firmware di componenti fisici (schede di rete, hard disk, GPU). Possono sopravvivere non solo alla formattazione del disco, ma persino alla sostituzione completa dell'hard disk.
    

### Come si individuano e si rimuovono?

Poiché un sistema infetto "mente", le tradizionali scansioni basate su firma (_signature-based_) del normale antivirus servono a poco. In ambito di analisi e risposta agli incidenti informatici si ricorre a tecniche più avanzate:

- **Analisi comportamentale:** Si cercano anomalie fisiche o di rete, come un traffico in uscita criptato o un utilizzo anomalo della CPU che non corrisponde a nessun processo visibile.
    
- **Memory Forensics:** Si analizza un _dump_ della memoria RAM (acquisito in modo isolato) alla ricerca di strutture dati nascoste che il sistema operativo corrotto non mostra.
    
- **Scansioni Offline:** Si avvia la macchina tramite un sistema operativo pulito esterno (es. una Live USB Linux). Poiché il rootkit residente sul disco infetto non viene eseguito durante questo avvio, perde i suoi "poteri" di occultamento e i suoi file diventano visibili e analizzabili come dati normali.
    

Considerando i tuoi studi in Intelligenza Artificiale, hai mai approfondito come i modelli di Machine Learning vengano impiegati oggi nella _behavioral analysis_ per automatizzare il rilevamento di queste minacce così elusive?

---


**Detection via Signatures:**

- ❌ **No direct file signature**: Rootkits operate at a deeper level (kernel space), so traditional file-based signatures fail.  
- ✅ **Behavioral and system call signatures**: Detect unusual behavior like:  
  - Unexplained process listing  
  - Hidden processes in task manager  
  - Altered boot logs or registry entries  

**Detection Methodology Insight:**  
Rootkits are **hard to detect with signature-based methods alone**. Detection relies on:  
- **Integrity checking tools** (e.g., system hash comparisons)  
- **Hardware root-of-trust solutions**  
- **Behavioral analytics and endpoint detection (EDR)**  

> 🔍 Key Takeaway: Rootkits are a major challenge for traditional signature-based systems — requiring **layered defense with behavior monitoring, memory scanning, and real-time telemetry**.
