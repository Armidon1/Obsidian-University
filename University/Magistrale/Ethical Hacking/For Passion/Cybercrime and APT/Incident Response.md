## tags: [eth, ch6, apt, incident-response, forensics, detection] aliases: [order_of_volatility, forensic_toolkit]

# Incident Response — investigare un host compromesso

Quando sospetti che una macchina sia compromessa — che sia un [[apt_lifecycle|APT]] o malware commodity — non improvvisi: segui un metodo. Il metodo risponde a due domande separate:

1. **Cosa cercare?** → la **persistenza** (il malware deve sopravvivere al reboot, e per farlo deve lasciare una traccia)
2. **In che ordine raccogliere le prove?** → l'**ordine di volatilità** (RFC 3227)

Il [[#Il toolkit forense|toolkit]] è solo lo strumento con cui esegui le due cose.

---

## 1. La persistenza — il tallone d'Achille del malware

Il "perché" che HE7 dà per scontato: un processo vive in **RAM**. Reboot = RAM azzerata = malware morto. L'unico modo per sopravvivere è piazzare un **gancio su storage non volatile** (disco, registro, MBR, firmware) che al boot/login rilancia il payload.

Questo è il punto debole strutturale dell'attaccante, e ricuce il filone APT **"tecniche invisibili, artefatti no"**: l'APT può essere invisibile _mentre gira_, ma per sopravvivere al reboot **deve scrivere qualcosa da qualche parte**. Quel "qualcosa" è l'artefatto su cui lo prendi.

La lista di HE7, riordinata per **profondità** — ed è di nuovo una **"corsa verso il basso"**, esattamente come l'evoluzione dei [[rootkits|rootkit]]:

|Meccanismo|Logica|Profondità|Dove lo trovi|
|---|---|---|---|
|**Run Registry keys**|Chiave nel registro che lancia un eseguibile al login utente|Userland, rumoroso|[[#Il toolkit forense\|Autoruns]]|
|**Scheduled task**|Lo scheduler dell'OS rilancia il payload a orario/evento|OS userland|Autoruns|
|**Creare un servizio**|Nuovo servizio che parte al boot, gira come SYSTEM|Boot, privilegi alti|Autoruns|
|**Hook su servizio esistente**|Dirotta un servizio legittimo (DLL hijack / service DLL sostituita) — nessuna _nuova_ entry|Più stealth: niente da notare in più|Autoruns + diff DLL|
|**Overwrite del MBR**|Bootkit: codice eseguito _prima_ dell'OS e dell'AV|Pre-OS|Confronto immagine / tool dedicati|
|**Overwrite del BIOS/firmware**|Persistenza nel firmware: sopravvive anche a wipe del disco e reinstallazione OS|Pre-tutto|Firmware forensics|

> [!warning] "Disguising communications as valid traffic" non è persistenza HE7 la mette nella stessa lista, ma la logica è diversa. Mascherare il C2 come traffico legittimo **non aiuta il malware a sopravvivere al reboot** — serve a non farsi notare _mentre comunica_. È **defense evasion / C2 obfuscation**, non persistenza. Tienile separate: una protegge il _gancio_, l'altra protegge il _canale_.

---

## 2. L'ordine di volatilità (RFC 3227)

Il "perché" della sequenza: raccogli le prove **dalla più effimera alla più durevole**, perché l'atto stesso di raccogliere (o anche solo il tempo che passa) **distrugge** ciò che è effimero. Se imagini il disco per primo, nel frattempo la RAM è già cambiata mille volte.

|#|Fonte|Perché è lì nella scala|
|---|---|---|
|1|**Memoria (RAM)**|Sparisce alla perdita di alimentazione, cambia ogni millisecondo|
|2|**Page / swap file**|Su disco, ma sovrascritto di continuo durante l'uso|
|3|**Processi in esecuzione**|Spariscono appena il processo termina|
|4|**Dati di rete** (porte in ascolto, connessioni)|Le connessioni si chiudono, le porte cadono|
|5|**Registro di sistema**|Relativamente stabile ma muta|
|6|**Log di sistema / applicativi**|Cambiano col tempo, possono ruotare|
|7|**Immagine forense del disco**|Stabile, persiste|
|8|**Supporti di backup**|Il dato più durevole|

Il limite di questo schema: ti dice _in che ordine_ raccogliere on-host, **non ti dice di chi fidarti**. Vedi il callout sotto.

---

## 3. Il toolkit forense

Strumenti del case study [[Gh0st Attack]] (mix Sysinternals + forensics), mappati sullo stadio di volatilità che coprono:

|Tool|Cosa fa|Stadio RFC 3227|Analogia Linux|
|---|---|---|---|
|**AccessData FTK Imager**|Immagine forense di RAM e disco, con hash per catena di custodia|1 e 7|`dd` + LiME (Linux Memory Extractor)|
|**Process Explorer**|Task Manager potenziato: albero padre-figlio, DLL caricate, firme digitali|3|`ps`/`htop`, ma con albero e mapping DLL|
|**Process Monitor**|Intercetta in real-time ogni operazione su file system, registro, rete, processi|3 (live)|`strace` / `auditd`|
|**Vmmap**|Mappa la memoria virtuale di un processo: heap, stack, DLL, regioni anonime sospette|3|`pmap`, `/proc/PID/maps`|
|**Currports**|Connessioni TCP/UDP attive col processo associato|4|`ss -tulnp` / `netstat -b`|
|**Autoruns**|Tutto ciò che parte da solo: Run keys, servizi, task, driver, hook|5|`systemctl list-unit-files` + `crontab -l` + autostart|
|**WinMerge**|Diff di file e directory: confronto vs baseline pulita|8|`diff -r`, AIDE / Tripwire (integrity)|

### Workflow investigativo

```
FTK Imager       → acquisisci RAM e disco PRIMA di toccare nulla
Process Explorer → quale processo è il malware?
Currports        → verso dove sta parlando (C2)?
Process Monitor  → cosa sta facendo (file, registro)?
Vmmap            → ha iniettato codice in altri processi?
Autoruns         → dov'è il gancio di persistenza?
WinMerge         → cosa ha modificato sul filesystem?
```

L'ordine pratico privilegia il **volatile live** (processi, rete) prima di staccare la spina e imageare il disco — coerente con RFC 3227.

## Più dettagli

Li raggruppo per funzione, non per ordine alfabetico.

---

## 1. Acquisizione forense

**AccessData FTK Imager** — crea immagini forensi di disco e RAM. Prima cosa che fai: _prima di toccare qualsiasi cosa_, acquisisci. Equivalente Windows di `dd` + dump di memoria. Preserva l'evidenza con hash per catena di custodia.

---

## 2. Persistenza — cosa sopravvive al reboot?

**Sysinternals Autoruns** — mostra _tutto_ ciò che si avvia automaticamente: registry run keys, servizi, scheduled task, driver, browser extension, LSA provider, Winlogon hook... È il tool più completo che esista per questa cosa su Windows. Primo posto dove un investigatore cerca il foothold del RAT.

---

## 3. Processi live — cosa sta girando e cosa fa?

**Sysinternals Process Explorer** — Task Manager potenziato. Mostra albero padre-figlio dei processi, DLL caricate, hash degli eseguibili, firma digitale. Utile per trovare processi con nomi legittimi ma percorso anomalo, o DLL iniettate.

**Sysinternals Process Monitor** — intercetta in real-time ogni operazione di file system, registro, rete, processo. È lo `strace`/`inotifywait` di Windows, ma anche più. Genera rumore enorme ma filtrato bene è chirurgico.

**Sysinternals Vmmap** — mappa la memoria virtuale di un singolo processo: mostra cosa è mappato dove (heap, stack, DLL, regioni anonime sospette). Utile per trovare codice iniettato o shellcode in memoria che non corrisponde a nessun file su disco.

---

## 4. Rete — chi sta parlando con chi?

**Currports** — lista connessioni TCP/UDP attive con il processo associato. Equivalente di `ss -tulnp` su Linux. Utile per vedere il RAT che mantiene il C2 aperto — nel caso Gh0st, la connessione verso il server di comando cinese era visibile qui.

---

## 5. Confronto filesystem — cosa è cambiato?

**WinMerge** — diff di file e directory. Se hai una baseline pulita (immagine pre-compromissione o golden image), confronti e vedi esattamente cosa è stato aggiunto/modificato. È l'approccio "trusted reference" — invece di cercare il male, cerchi la _differenza_.

---

## Workflow investigativo implicito

```
FTK Imager          ← acquisisci prima di tutto
    ↓
Autoruns            ← dove si nasconde la persistenza?
    ↓
Process Explorer    ← quale processo è il RAT?
    ↓
Currports           ← verso dove sta parlando?
    ↓
Process Monitor     ← cosa sta facendo (file, registry)?
    ↓
Vmmap               ← ha iniettato codice in altri processi?
    ↓
WinMerge            ← cosa ha modificato sul filesystem?
```

Nota: tutto questo è _on-host_, quindi soggetto al limite che conosci — [[kernel_rootkits]] o un RAT con driver possono falsificare quello che questi tool vedono. Il dato più affidabile rimane la telemetria di rete catturata fuori dalla macchina.

---

> [!tip] Il filo conduttore — non fidarti della macchina compromessa L'ordine di volatilità ti dice _in che sequenza_ raccogliere, **non di chi fidarti**. E qui c'è la tensione: quasi tutto questo toolkit è **on-host**. Un [[kernel_rootkits|rootkit kernel]] falsifica ciò che Process Explorer e Currports ti mostrano _anche se li usi nell'ordine corretto_; [[log_cleaning|l'anti-forensics]] ti svuota i log dello stadio 6.
> 
> Quindi: l'ordine di volatilità è **necessario ma non sufficiente**. Le due prove davvero affidabili sono (a) **l'immagine di memoria analizzata offline** — la RAM la puoi falsificare _a runtime_, ma una volta dumpata e analizzata da un'altra macchina il rootkit non può più mentirti — e (b) la **telemetria di rete catturata fuori banda**. Si raccoglie _dalla_ macchina compromessa, ci si fida _di_ ciò che sta fuori.

---

## Stato moderno (2026)

- I tool **Sysinternals** sono ancora lo standard de facto per la triage manuale su Windows, tuttora mantenuti.
- L'IR moderno è centrato sugli **EDR** (CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne): telemetria raccolta in continuo e centralizzata **off-host**. È esattamente il meta-principio "telemetria fuori banda" istituzionalizzato — non vai più _a cercare_ il male sull'host compromesso, lo hai già registrato altrove.
- **Memory forensics**: l'immagine RAM si analizza con **Volatility 3**, lo standard. **Velociraptor** / GRR per live forensics remota su flotte di host.
- La voce "overwrite del BIOS" di HE7 (~2012) oggi è realtà concreta: **bootkit UEFI** come BlackLotus (2023) bypassano Secure Boot. Difesa: Secure Boot + misurazione TPM.
- "Disguising communications as valid traffic" oggi significa **C2 su HTTPS**, domain fronting, e servizi cloud legittimi come canale (Slack, Discord, Google Drive). Currports ti mostra solo "connessione verso un IP Microsoft" — il _contenuto_ è cifrato, ma i **metadati di rete** (volume, timing, beaconing) restano visibili: di nuovo, l'analisi fuori banda batte l'ispezione on-host.
- **Cloud**: l'host è effimero; la persistenza si sposta su ruoli IAM, funzioni serverless, `cloud-init`. Superficie di artefatti diversa, stessa logica.

## Mapping MITRE ATT&CK

|Tecnica avversaria|ID|Note|
|---|---|---|
|Boot or Logon Autostart — Registry Run Keys|T1547.001|Visibile in Autoruns|
|Create or Modify System Process — Windows Service|T1543.003|Nuovo servizio o hijack|
|Scheduled Task/Job|T1053.005||
|Hijack Execution Flow — DLL|T1574.001|"Hook su servizio esistente"|
|Pre-OS Boot — Bootkit (MBR)|T1542.003||
|Pre-OS Boot — System Firmware (BIOS/UEFI)|T1542.001||
|Application Layer Protocol — Web/HTTPS C2|T1071.001|"Disguise comms as valid traffic"|
|**Lato difensore** ↓|||
|Order of volatility / evidence collection|—|RFC 3227 (procedura IR, non tecnica ATT&CK)|

## Collegamenti

- [[apt_lifecycle]] — la persistenza si pianta nella fase _establish foothold_ del lifecycle
- [[gh0st_attack]] — il case study da cui viene questo toolkit
- [[rootkits]] / [[kernel_rootkits]] — la "corsa verso il basso" della persistenza, e perché i tool on-host mentono
- [[log_cleaning]] — l'attaccante combatte l'investigatore allo stadio 6 (log)
- [[trojan_binaries]] — binario trojanizzato come gancio di persistenza
- [[backdoors]] — il payload che la persistenza tiene in vita
- [[linux_apt_attack]] — l'equivalente del workflow lato UNIX