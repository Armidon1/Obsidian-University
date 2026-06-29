Ecco una serie di domande di simulazione dell'esame basate sull'archivio delle domande del tuo professore, focalizzate sul **Capitolo 4 (Hacking Windows)** di Hacking Exposed. Per ogni domanda, ti fornisco una traccia dettagliata della risposta per aiutarti a ripassare i concetti chiave richiesti.

### Domanda 1: Compromissione e Ripristino (Post-Exploitation)

**Domanda d'esame:** L'account Administrator di un server Windows è stato compromesso. Il software host non può essere reinstallato per motivi aziendali. Con queste premesse, come pianifichi e implementi le attività di post-exploit per il recupero dell'host? Elenca le aree del sistema su cui intervenire per ripristinare la sicurezza e discutine una nel dettaglio, elencando strumenti e comandi da usare.

**Come rispondere per il ripasso:** In assenza della possibilità di formattare il sistema (che sarebbe la prassi consigliata in caso di compromissione privilegiata), la bonifica deve concentrarsi su quattro aree principali del sistema operativo:

- **Nomi dei file (Filenames):** Gli attaccanti nascondono strumenti come `netcat`, `psexec` o `pwdump` rinominandoli. È essenziale controllare la presenza di file anomali nelle directory di esecuzione automatica (Startup directories come `%systemroot%\profiles\%username%\Start Menu\programs\startup\`). **Strumento utile:** software anti-malware o strumenti di checksumming come **Tripwire** per individuare modifiche al file system.
- **Chiavi di Registro (Registry Entries):** Molti programmi di controllo remoto (come WINVNC o backdoor netcat) inseriscono valori in chiavi di avvio automatico (ASEP - Autostart Extensibility Points) come `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`. **Comando utile:** `reg delete [value] \\machine` per eliminare chiavi sospette.
- **Processi in esecuzione (Running processes):** Cerca processi che consumano molta CPU o thread anomali. **Strumenti utili:** Il _Task Manager_ di Windows o l'utilità da riga di comando `taskkill` per terminare i processi malevoli. È importante controllare anche la coda del **Task Scheduler** tramite il comando `at` o `schtasks`, poiché gli hacker lo usano per eseguire processi con privilegi SYSTEM.
- **Porte (Ports):** Gli attaccanti lasciano porte in ascolto per backdoor o strumenti di reindirizzamento come `fpipe`. **Comando utile:** `netstat -an` (o `netstat -o` per associare la porta al processo) per individuare sessioni TCP stabilite dirottate.

---

### Domanda 2: Copertura delle tracce e File nascosti

**Domanda d'esame:** Spiega quali passi dovrebbe intraprendere un attaccante per coprire le proprie tracce dopo aver ottenuto i privilegi di amministratore su un sistema Windows per evitare il rilevamento. Come possono gli attaccanti nascondere i loro file nel sistema?

**Come rispondere per il ripasso:** Un attaccante amministratore copre le sue tracce operando su vari fronti:

- **Disabilitare l'Auditing:** Per evitare che le azioni vengano registrate, un attaccante disabilita le politiche di audit. **Strumento:** usa il comando del Resource Kit `auditpol /disable` per spegnere l'audit e, alla fine del lavoro, `auditpol /enable` per riaccenderlo passando inosservato.
- **Pulizia degli Event Log (Clearing the Event Log):** Se sono state lasciate tracce, l'attaccante può cancellare interamente i log tramite l'Event Viewer di Windows o usando strumenti a riga di comando come **ELSave** (es. `elsave -s \\server -l "Security" -C`) o alterando i file in `\winnt\system32` manualmente.
- **Nascondere i file (Hiding Files):**
    - _Metodo base:_ Usare il comando DOS `attrib +h [directory]`. Questo nasconde i file dalla riga di comando, ma è facilmente aggirabile se un difensore attiva l'opzione "Mostra file nascosti" in Esplora risorse.
    - _Metodo avanzato (Alternate Data Streams - ADS):_ Su file system NTFS, un hacker può nascondere un eseguibile o un toolkit (adminkit) "dietro" un file legittimo creando un flusso di dati alternativo. Utilizzando comandi come `cp nc.exe oso001.009:nc.exe`, la dimensione e il nome del file frontale non cambiano, rendendo la backdoor invisibile. L'eseguibile può comunque essere avviato usando il comando `start oso001.009:nc.exe`.

---

### Domanda 3: Protocolli di rete, Pass-the-Hash e Pass-the-Ticket

**Domanda d'esame:** Quali sono i tre principali protocolli di scambio password di rete utilizzati nei sistemi Windows? Descrivi gli attacchi Pass-the-Hash e Pass-the-Ticket e le relative contromisure.

**Come rispondere per il ripasso:**

- **I Tre Protocolli:** I protocolli principali per l'autenticazione in Windows sono **LM** (Lan Manager - obsoleto e debole), **NTLM** (più moderno e robusto) e **Kerberos** (basato sull'uso di ticket).
- **Attacco Pass-the-Hash:** Sfrutta le debolezze di NTLM/LM. Dato che gli hash NTLM sono funzionalmente equivalenti alle password in chiaro, l'attaccante, invece di crackare l'hash offline, lo "inietta" o "ripete" per autenticarsi direttamente ai server remoti. Per farlo, gli attaccanti usano tool di post-exploitation come il **Windows Credentials Editor (WCE)** che estraggono gli hash di LM e NTLM salvati in chiaro nella memoria RAM del sottosistema di autenticazione, anche se gli utenti hanno già effettuato la disconnessione (molto pericoloso se un Domain Admin si collega via RDP a una macchina compromessa).
- **Attacco Pass-the-Ticket:** Simile al precedente ma applicato al protocollo Kerberos. Permette di fare il "dump" dei ticket Kerberos dalla memoria e riutilizzare un Ticket Granting Ticket (TGT) per creare nuovi ticket per altri servizi, garantendo accesso non autorizzato sia su sistemi Windows che UNIX. Anche qui, **WCE** è lo strumento di riferimento per caricare (load) questi ticket nella sessione locale.
- **Contromisure:** Poiché per eseguire l'attacco serve prima ottenere i privilegi di amministratore e leggere dalla memoria del sistema (post-exploitation), non esiste un "proiettile d'argento" per bloccare strumenti come WCE. La difesa migliore si basa sul **"defense-in-depth"**: prevenire le intrusioni primarie, usare l'autenticazione a due fattori, e proibire fermamente agli amministratori di dominio di usare RDP su macchine/server potenzialmente vulnerabili o sconosciute.

---

### Domanda 4: Funzionalità di sicurezza di Windows

_(Attenzione: Il professore in questa domanda richiede espressamente di NON descrivere Windows Firewall e Automated Updates)_ **Domanda d'esame:** Descrivi almeno tre funzionalità di sicurezza di Windows disponibili da Windows 2000 in poi. Ci sono attacchi pubblicati che aggirano queste funzionalità?

**Come rispondere per il ripasso:** Puoi descrivere queste tre funzionalità e i relativi limiti/bypass:

1. **Data Execution Prevention (DEP) / ASLR (tramite EMET):**
    - _DEP_ è una funzionalità supportata sia a livello hardware che software (SafeSEH) progettata per prevenire gli attacchi di buffer overflow basati sullo stack, marcando determinate porzioni di memoria come non eseguibili.
    - _ASLR_ (Address Space Layout Randomization) randomizza le posizioni di memoria dove vengono caricate immagini eseguibili, heap e stack, rendendo inaffidabili gli exploit. L'utente può gestire queste impostazioni tramite l'Enhanced Mitigation Experience Toolkit (**EMET**).
    - _Bypass:_ Sebbene molto efficaci, nel corso degli anni sono stati sviluppati e pubblicati numerosi exploit avanzati che riescono ad aggirare DEP e ASLR combinandoli con altre vulnerabilità.
2. **BitLocker Drive Encryption (BDE):**
    - Introdotto per crittografare l'intero volume del disco anziché i singoli file (come faceva EFS). L'obiettivo è prevenire attacchi offline e mantenere l'integrità del sistema in caso di furto fisico, in quanto l'OS non si caricherà senza la chiave crittografica immagazzinata in modo sicuro (solitamente in un chip TPM).
    - _Bypass (Cold-boot attack):_ È stato pubblicato uno studio (ad es. dall'Università di Princeton) che dimostra come aggirare BDE con i _cold-boot attack_. In pratica, l'attaccante "congela" fisicamente i chip DRAM per mantenere i dati nella memoria volatile più a lungo, estraendo così la chiave crittografica necessaria a sbloccare il sistema dopo averlo estratto o riavviato. L'unica vera contromisura è spegnere completamente il PC protetto (che cancella la memoria RAM) e conservare separatamente chiavi o hardware necessari.
3. **Group Policy / Security Policy:**
    - I Group Policy Objects (GPO) permettono l'applicazione e l'imposizione centralizzata di configurazioni di sicurezza (es. lunghezza delle password, impostazioni per disabilitare la memorizzazione dell'hash LM obsoleto) a livello di foresta o dominio tramite Active Directory. Questo riduce drasticamente l'errore umano di configurazione locale in ambienti estesi.