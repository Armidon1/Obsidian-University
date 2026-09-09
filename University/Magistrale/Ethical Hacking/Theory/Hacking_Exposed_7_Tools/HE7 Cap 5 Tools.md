---
chapter: 5
chapter_title: "Hacking UNIX"
source: Hacking Exposed 7: Network Security Secrets & Solutions
tags:
  - cybersecurity
  - hacking-exposed-7
  - tool-inventory
---

# HE7 Cap 5 Tools

Indice dei tool/programmi trattati nel capitolo 5 — *Hacking UNIX*.

> Sono esclusi comandi elementari, protocolli, vulnerabilità, tecniche e software citati solo come contesto.

**Totale:** 80

| Tool / nome normalizzato | Varianti o alias | Pagine | Categoria | Scopo descritto nel libro | Stato probabile |
| --- | --- | --- | --- | --- | --- |
| adore-ng | — | 308 | altro | Rootkit nominato nel confronto delle implementazioni kernel. | probabilmente datato |
| AIDE | — | 297, 304 | difesa/monitoraggio | Verifica dell'integrità dei file. | probabilmente attivo |
| AntiSniff | Anti-Sniff | 300 | difesa/monitoraggio | Rilevamento della presenza di strumenti di acquisizione del traffico. | probabilmente datato |
| arpredirect | — | 300 | rete | Componente dsniff citato per analisi del traffico su reti commutate. | probabilmente datato |
| badattachK | badattach | 305 | altro | Programma dimostrativo di interferenza con la registrazione degli eventi. | probabilmente datato |
| Carbonite | — | 308–309 | analisi forense | Modulo di analisi dei processi a livello kernel. | probabilmente datato |
| Check Promiscuous Mode | cpm | 300 | difesa/monitoraggio | Verifica della modalità delle interfacce di rete. | probabilmente datato |
| chkrootkit | — | 297 | difesa/monitoraggio | Ricerca di indicatori di rootkit. | probabilmente attivo |
| Crack | — | 289 | password auditing | Programma di auditing delle password UNIX, citato nel confronto con John. | probabilmente datato |
| cracklib | — | 239 | difesa/monitoraggio | Libreria per valutare la robustezza delle password. | probabilmente attivo |
| dig | — | 273 | enumerazione | Interrogazione e diagnostica DNS. | nativo / dipendente dalla piattaforma |
| dsniff (programma) | dsniff | 299–300 | rete | Analizzatore omonimo incluso nella suite dsniff. | probabilmente attivo |
| dsniff (suite) | dsniff package | 299–300 | rete | Suite di analisi del traffico di rete. | probabilmente attivo |
| enyelkm | Enye;enyelkm.ko | 306–308 | altro | Rootkit Linux descritto nel capitolo UNIX. | probabilmente datato |
| Exec Shield | — | 243 | difesa/monitoraggio | Estensione di protezione della memoria. | probabilmente datato |
| ftp (client) | FTP client | 257–258, 266 | rete | Client per accesso ai file di servizi FTP. | nativo / dipendente dalla piattaforma |
| Google Search | Google;google.com | 272 | ricognizione OSINT | Ricerca di informazioni pubbliche e applicazioni indicizzate. | probabilmente attivo |
| grsecurity | GRSecurity | 243 | difesa/monitoraggio | Suite di estensioni di sicurezza del kernel. | probabilmente attivo |
| Helix | — | 310 | analisi forense | Ambiente avviabile per attività forensi. | probabilmente datato |
| hole (Rathole) | hole | 295–296 | altro | Componente server del pacchetto Rathole. | probabilmente datato |
| HP Security Toolkit | Security Toolkit | 311 | web testing | Suite di utility di analisi integrata con WebInspect. | probabilmente datato |
| IPFilter | Ipfilter;ipf | 243 | difesa/monitoraggio | Firewall per sistemi UNIX. | probabilmente attivo |
| iptables | — | 242 | difesa/monitoraggio | Gestione delle regole di filtraggio della rete. | nativo / dipendente dalla piattaforma |
| John the Ripper | John The Ripper Jumbo;JTR;john | 280, 282–283 | password auditing | Recupero e auditing delle password; accorpate le varianti Jumbo. | probabilmente attivo |
| knark | — | 306–307, 309 | altro | Rootkit Linux descritto nel capitolo UNIX. | probabilmente datato |
| Liblogclean | — | 301 | altro | Libreria per gestione/modifica dei registri, componente del caso logclean-ng. | probabilmente datato |
| lidsadm | — | 309 | difesa/monitoraggio | Gestione della protezione LIDS. | probabilmente datato |
| Linux Intrusion Detection System | LIDS | 309 | difesa/monitoraggio | Estensione di protezione del kernel Linux. | probabilmente datato |
| logclean-ng | — | 301 | altro | Programma di modifica dei registri, descritto come strumento di occultamento. | probabilmente datato |
| Medusa | — | 237 | password auditing | Auditing delle password di servizi di rete. | probabilmente attivo |
| Metasploit Framework | Metasploit;MFS | 263, 272 | exploit framework | Framework modulare di valutazione della sicurezza. | probabilmente attivo |
| Mood-NT | — | 307 | altro | Rootkit Linux citato come derivato di SucKIT. | probabilmente datato |
| Nessus | nessusd | 233 | scanning | Scansione delle vulnerabilità di sistemi e servizi. | probabilmente attivo |
| Netcat | netcat;nc;nc.exe | 232, 257, 260–261 | rete | Utility generale per connessioni e analisi di servizi. | probabilmente attivo |
| Netcraft | Netcraft.com | 277 | ricognizione OSINT | Statistiche e identificazione delle piattaforme web. | nativo / dipendente dalla piattaforma |
| netstat | — | 295, 304, 310 | rete | Visualizzazione delle connessioni e dei servizi in ascolto. | nativo / dipendente dalla piattaforma |
| nfsshell | nfs client | 266 | rete | Client per esplorare file system NFS. | probabilmente datato |
| Nmap | Network Mapper;network mapper | 232, 263 | scanning | Scoperta di host, porte, servizi e sistemi operativi. | probabilmente attivo |
| OpenSSH | openssh | 239, 250, 252, 275–276, 291, 297, 301 | rete | Suite di connessione remota cifrata. | probabilmente attivo |
| OpenSSL | openssl | 276–277 | rete | Libreria e utility di comunicazione crittografica. | probabilmente attivo |
| OpenWall (patch) | OpenWall port | 239, 243, 280 | difesa/monitoraggio | Port/patch di protezione del sistema richiamato nella genealogia di grsecurity. | probabilmente datato |
| PAM | Pluggable Authentication Modules | 238–239, 275 | difesa/monitoraggio | Framework modulare di autenticazione. | nativo / dipendente dalla piattaforma |
| pam_cracklib | — | 238 | difesa/monitoraggio | Modulo PAM per controllare le password. | probabilmente datato |
| pam_lockout | — | 239 | difesa/monitoraggio | Modulo PAM per blocco degli account. | probabilmente datato |
| pam_passwdqc | — | 239 | difesa/monitoraggio | Modulo PAM per controllare la robustezza delle password. | probabilmente attivo |
| PaX | — | 243–244 | difesa/monitoraggio | Estensione di protezione della memoria. | probabilmente attivo |
| phalanx | — | 307 | altro | Rootkit Linux nominato nel confronto delle implementazioni. | probabilmente datato |
| ping | — | 291 | rete | Verifica della raggiungibilità di host. | nativo / dipendente dalla piattaforma |
| rat (Rathole) | rat | 295–296 | altro | Componente client del pacchetto Rathole. | probabilmente datato |
| Rathole | — | 295–296 | altro | Pacchetto di accesso remoto descritto come backdoor. | probabilmente datato |
| RIPE (database) | RIPE;ripe.net | 263 | ricognizione OSINT | Consultazione di assegnazioni Internet regionali. | nativo / dipendente dalla piattaforma |
| rkhunter | — | 297 | difesa/monitoraggio | Ricerca di indicatori di rootkit. | probabilmente attivo |
| rlogin | — | 235–236, 249, 255, 260 | rete | Client di accesso remoto UNIX. | probabilmente datato |
| rpcinfo | — | 232, 262, 264 | enumerazione | Interrogazione dei servizi RPC. | nativo / dipendente dalla piattaforma |
| rusers | — | 236 | enumerazione | Informazioni sugli utenti di sistemi remoti. | probabilmente datato |
| Samba | — | 250, 301 | altro | Suite di servizi e utility di condivisione compatibili con Windows. | probabilmente attivo |
| SELinux | — | 293, 311 | difesa/monitoraggio | Controlli di sicurezza del sistema operativo. | probabilmente attivo |
| showmount | — | 232, 266 | enumerazione | Elenco dei file system esportati tramite NFS. | nativo / dipendente dalla piattaforma |
| sniffdet | — | 300 | difesa/monitoraggio | Rilevamento di possibili sniffer. | probabilmente datato |
| Snoop | — | 271, 300 | rete | Analizzatore dei pacchetti incluso in Solaris. | probabilmente attivo |
| Snort | — | 250, 252, 301 | difesa/monitoraggio | Rilevamento delle attività sospette sul traffico di rete. | probabilmente attivo |
| Solaris Fingerprint Database | — | 297 | difesa/monitoraggio | Servizio di confronto delle impronte dei file Solaris. | probabilmente attivo |
| Solaris Security Toolkit | — | 311 | difesa/monitoraggio | Raccolta di strumenti di protezione e auditing Solaris. | probabilmente datato |
| ssh (client) | — | 235–237, 255, 271, 274–276, 291, 295, 297, 300–301 | rete | Client di connessione remota; distinto dal protocollo SSH. | nativo / dipendente dalla piattaforma |
| St. Michael | — | 309 | difesa/monitoraggio | Controllo dell'integrità del kernel. | probabilmente datato |
| SucKIT | — | 307 | altro | Rootkit Linux descritto nel capitolo UNIX. | probabilmente datato |
| TCP Wrappers | — | 242 | difesa/monitoraggio | Suite di controllo degli accessi ai servizi di rete. | probabilmente datato |
| tcpd | — | 242 | difesa/monitoraggio | Componente di TCP Wrappers per il controllo degli accessi. | probabilmente datato |
| tcpdump | — | 235, 300 | rete | Acquisizione e analisi dei pacchetti di rete. | probabilmente attivo |
| Telnet (client) | telnet client | 248, 257 | rete | Client di connessione remota e identificazione dei servizi. | probabilmente datato |
| THC Hydra | Hydra | 237 | password auditing | Auditing delle password di servizi di rete. | probabilmente attivo |
| THC-SSL-DOS | — | 276–277 | altro | Programma dimostrativo di verifica della disponibilità dei servizi SSL. | probabilmente datato |
| Tor | TOR;The Onion Router | 281 | rete | Rete e software di anonimizzazione delle connessioni. | probabilmente attivo |
| Tripwire | — | 297, 308 | difesa/monitoraggio | Verifica dell'integrità dei file. | probabilmente attivo |
| unrar | — | 284 | altro | Utility di estrazione di archivi citata nel caso UNIX. | probabilmente attivo |
| Wireshark | Ethereal;Wiireshark | 300 | rete | Analisi dei pacchetti, anche wireless e VoIP. | probabilmente attivo |
| wzap | — | 303 | altro | Programma storico di modifica del registro degli accessi. | probabilmente datato |
| xinetd | — | 242 | difesa/monitoraggio | Gestione dei servizi di rete e dei relativi accessi. | probabilmente attivo |
| xscan | — | 270 | altro | Programma storico di ricognizione e osservazione di sessioni X. | probabilmente datato |
| Yahoo! | Yahoo;yahoo.com | 273 | ricognizione OSINT | Motore di ricerca e fonte di informazioni societarie. | probabilmente attivo |
