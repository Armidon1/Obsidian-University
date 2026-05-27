## tags: [ethical-hacking, he7, ch5, post-exploitation, rootkit, kernel]

# Kernel rootkits

> Ultimo componente di [[rootkits]] — chiude la nota-hub e con essa il **Ch.5**. HE7 Ch.5, sezione "Kernel Rootkits". Argomento denso; HE7 qui è molto datato (kernel 2.2/2.4/2.6), la parte moderna è sostanziosa.

## Concetto — spostare la bugia nel kernel

Un rootkit tradizionale (`[[trojan_binaries]]`) mente **rimpiazzando il programma**: il tuo `ps` è falso. Un kernel rootkit fa l'opposto: lascia `ps` **autentico** e fa mentire **il kernel**. `ps` riferisce fedelmente — ma il kernel gli serve un sottoinsieme curato della realtà. È questo il senso della frase di HE7: _"fool all system programs without modifying the programs themselves"_.

Conseguenza cruciale, ed è il motivo per cui il kernel rootkit è superiore: **batte la contromisura di `[[trojan_binaries]]`**. Tripwire/AIDE confrontano i checksum dei binari — ma qui i binari sono _genuinamente intatti_. Non puoi checksummarti fuori dal problema. E non puoi nemmeno fidarti del kernel che esegue il checksummer. HE7 lo dice secco: _non puoi fidarti né dei binari né del kernel stesso_.

Caveat di HE7: i kernel rootkit pubblici sono **fragili** — legati a versioni specifiche del kernel, le cui strutture dati e API evolvono di continuo (enyelkm è scritto per il 2.6.x e non compila altrove senza modifiche). Non è roba plug-and-play: l'attaccante serio se lo adatta.

## I due assi: injection e interception

HE7 struttura il tema su due assi **ortogonali**:

- **Injection** — come il codice del rootkit _entra_ nel kernel.
- **Interception** — come, una volta dentro, _altera_ il comportamento del sistema.

Sono indipendenti: una stessa tecnica di interception può essere consegnata da iniezioni diverse.

## Asse 1 — Injection (come entrare nel kernel)

|Metodo|Come|Esempi|Spinto da|
|---|---|---|---|
|**LKM** (loadable kernel module)|un modulo si carica nel kernel vivo via `modprobe`/`insmod` — invece di un driver, carica codice ostile|knark, adore, enyelkm|è il metodo originale e più diffuso|
|**`/dev/kmem`**|lettura/scrittura **diretta** della memoria kernel da userland, **senza LKM**|SucKIT (Phrack 58), Mood-NT|risposta agli admin che disabilitavano gli LKM|
|**`/dev/mem`**|come sopra, su un'altra interfaccia di memoria|phalanx|risposta alle distro che eliminavano `/dev/kmem`|

Già qui si vede l'arms race: ogni metodo nasce perché il precedente è stato chiuso.

## Asse 2 — Interception (come sovvertire dall'interno)

|Tecnica|Come|Esempi|Nota|
|---|---|---|---|
|**Syscall table modification**|si scambiano i puntatori nella tabella delle syscall|knark|la più vecchia e rozza — gli integrity checker la beccano|
|**Syscall handler modification**|non si tocca la tabella: si patcha l'_handler_ che la invoca, facendolo puntare a una tabella del rootkit|SucKIT, enyelkm (patcha `system_call`/`sysenter_entry`)|richiede patching del kernel a runtime|
|**IDT modification**|si alterano le voci della Interrupt Descriptor Table o gli interrupt handler|kad (Phrack 59)|intercetta a livello di interrupt|
|**VFS subversion**|non tocca la syscall table _affatto_: sanifica i dati al livello del Virtual File System|adore-ng|"tutto è un file" → tutte le syscall sui file passano dal VFS|

Anche questo è un arms race: ogni tecnica evade il _rilevamento_ della precedente. La syscall table si becca con un integrity checker → allora patcha l'handler; poi si scende all'IDT; infine adore-ng abbandona del tutto la syscall table e colpisce un layer più in basso (VFS).

## enyelkm — l'esempio concreto

LKM rootkit per Linux 2.6.x (modulo `enyelkm.ko`), caricato con `/sbin/modprobe enyelkm`. Funzioni: nasconde file/directory/processi, nasconde _porzioni_ di file, si nasconde da `lsmod`, dà root via opzione `kill`, accesso remoto via richiesta ICMP speciale + reverse shell.

Demo HE7: `kill -s 58 12345` → `id` passa da uid 1000 a **uid 0**. Il segnale `kill` arriva al kernel, il rootkit in agguato lo riconosce come **trigger magico** ed esegue l'azione (privilege elevation). Concetto chiave: il _magic trigger_ — un input innocuo che solo il rootkit interpreta.

> [!tip] Filo conduttore — qui la "corsa verso il basso" si vede in dettaglio La nota [[rootkits]] introduce la gara di profondità; **questa nota ne è il dettaglio**. Entrambi gli assi sono la stessa mossa: _trovare un layer che il difensore non sta guardando_. Injection: LKM → `/dev/kmem` → `/dev/mem`. Interception: syscall table → syscall handler → IDT → VFS. E non finisce con adore-ng: la corsa continua oltre il libro (ftrace, eBPF) — e, punto chiave del 2026, **scende sotto il kernel** (firmware, hypervisor). La simmetria interessante: oggi anche il _difensore_ è costretto a scendere — vedi sotto.

## Countermeasures (HE7)

HE7 parte dall'ammissione dura: kernel rootkit devastanti e difficili da trovare, Tripwire **inutile** se il kernel è compromesso.

- **Carbonite** — modulo kernel che "congela" lo stato di ogni processo nella `task_struct` (la struttura kernel della process list); cattura info tipo `ps`/`lsof` + copia dell'immagine eseguibile, e ci riesce **anche sui processi nascosti** (es. da knark) perché gira _nel contesto kernel_.
- **LIDS** (Linux Intrusion Detection System) — patch del kernel: "sigilla" il kernel dalle modifiche, blocca load/unload dei moduli, attributi immutable/append-only, lock dei segmenti di memoria condivisa, protezione PID, protezione di `/dev/` sensibili. Si applica la patch, si ricompila il kernel, si sigilla con `lidsadm`.
- **Disabilitare il supporto LKM** sui sistemi ad alta sicurezza (soluzione poco elegante, ferma gli script kiddie).
- **St. Michael** — LKM che rileva/devia l'installazione di backdoor kernel monitorando `init_module`/`delete_module` per cambi nella syscall table.

> Nota: Carbonite, LIDS e St. Michael sono **obsoleti** oggi. Il loro _principio_ sopravvive, l'implementazione no — vedi sotto.

## Stato moderno (2026)

**L'asse injection è cambiato molto:**

- **`/dev/kmem` rimosso** dal kernel mainline; **`/dev/mem` ristretto** da `CONFIG_STRICT_DEVMEM` (accesso solo a una allowlist, non alla memoria kernel arbitraria). SucKIT/phalanx-style da userland: morti.
- **L'LKM resta il metodo dominante**, ma è blindato: **module signing** (`CONFIG_MODULE_SIG_FORCE`), **UEFI Secure Boot**, `kernel.modules_disabled=1`, e soprattutto la **kernel lockdown LSM** (mainline da 5.4) — è la risposta sistematica moderna: blocca `/dev/mem`, kexec, moduli non firmati, ecc.
- **Nuove superfici di iniezione:**
    - **eBPF** — codice (verificato, ma) utile all'attaccante caricato nel kernel _senza modulo_. Aggancia tracepoint/kprobe, può leggere e modificare argomenti e valori di ritorno delle syscall, nascondere processi. È l'LKM-equivalente _legittimo by design_ → difficile da vietare. Rootkit reali: TripleCross, ebpfkit, **BPFDoor**.
    - **Exploit di una vulnerabilità kernel** → write/exec arbitrario in ring 0: non ti serve un modulo, l'exploit _è_ l'iniezione. È qui che rientra il trucco dello **overwrite di `modprobe_path`** (vedi la discussione su `modprobe`): con una kernel write primitive sovrascrivi quel globale e ottieni esecuzione da root.
    - **DKOM** (Direct Kernel Object Manipulation) — sganci la tua `task_struct` dalla lista dei processi per sparire. Concetto vecchio (Carbonite era già un detector DKOM), ancora valido.

**L'asse interception è cambiato:**

- La **syscall table** oggi è in memoria **read-only** e non più esportata: per patcharla il rootkit deve disattivare la write protection (clear del bit `CR0.WP`) — operazione di per sé sospetta e rilevabile.
- La tecnica in voga è l'**hooking via ftrace** — si usa il framework di tracing _del kernel stesso_ per agganciare le syscall senza toccare la tabella (es. il rootkit Diamorphine). È l'enyelkm "handler salting" in versione 2020s: sfrutta un meccanismo sanzionato.
- **kprobes** ed **eBPF** servono sia da iniezione sia da interception.
- I **magic trigger** sopravvivono identici: la richiesta ICMP speciale di enyelkm è il _magic packet_ di BPFDoor — stesso concetto, edizione 2024 con eBPF.

**Le difese moderne** (il principio di HE7 sopravvive, gli strumenti no):

- **LSM** al posto di LIDS: SELinux, AppArmor, e la **lockdown LSM**.
- **IMA/EVM** — Integrity Measurement Architecture: misura e _appraisal_ dei file, ancorabile a un **TPM**.
- **Integrità basata su hypervisor** — poiché un kernel compromesso non può verificare sé stesso, si mette il guardiano _sotto_ il kernel: VBS / HVCI / Secure Kernel su Windows, introspezione VM (LibVMI) lato Linux/ricerca. È la "corsa verso il basso" **applicata al difensore**.
- **Secure/Measured Boot + attestazione TPM**, `dm-verity` per il rootfs.
- **EDR basato su eBPF** (Falco, Tetragon): eBPF è il campo di battaglia da entrambi i lati.

> [!tip] Meta-principio (4ª comparsa, e qui nella forma più fondamentale) Già visto in [[rootkits]], [[trojan_binaries]], [[log_cleaning]]: **un sistema compromesso non può essere fidato a riferire su sé stesso.** Al livello del kernel è la forma più pura del principio — un kernel ostile controlla _tutto_ ciò che gira sopra di esso. Le uniche risposte sane: **osservare dal basso/fuori** (hypervisor, TPM, telemetria out-of-band) e **prevenire** (lockdown, module signing, Secure Boot). La detection _dall'interno_ è strutturalmente perdente.

## Mapping MITRE ATT&CK

|Tecnica|ID|
|---|---|
|Rootkit|T1014|
|Boot/Logon Autostart: Kernel Modules and Extensions|T1547.006|
|Exploitation for Privilege Escalation (rotta exploit→ring0)|T1068|
|Hide Artifacts (file/processi nascosti)|T1564|
|Impair Defenses|T1562|

## Collegamenti

- Nota-hub completata: [[rootkits]] → con questa il **Ch.5 è chiuso**
- Batte la contromisura dei trojan userland (i checksum): [[trojan_binaries]]
- Filtra i record audit / nasconde il log cleaner: [[log_cleaning]]
- Nasconde il processo dello sniffer in modalità promiscua: [[Sniffer]]
- Rotta iniezione via exploit kernel + overwrite di `modprobe_path` → vedi le note di privilege escalation del capitolo